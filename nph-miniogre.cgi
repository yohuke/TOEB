#!/usr/local/bin/perl

#=================================================================================
#	mini BBS++ ver2.73
#
#  last update: 09/12/2001
#       author: ���L
#          url: http://www.midnightroam.org/
#
#  �����ʂ菬���Ȍf���ł��B�e���v���[�gHTML��
#  �ǂݍ��݁CBBS������ǉ����ĕ\�����܂��B
#  �r�炵�΍�ɂ̓����_���R�[�h���g�p���Ă��܂��B
#  �摜���ɂ���ꍇ�C0�`9�̉摜��
#  �摜�A��CGI�umakeimage.cgi�v�����ꂼ��ʓr�K�v�ł��B
#
#	Copyright (c) 2000,2001  Twilight Heaven
#=================================================================================
use strict;
#==============================================
# �����ݒ�
#==============================================
#�����̃t�@�C���̖��O �K���ɕς��Ă�������
my $script = './nph-miniogre.cgi';
#���摜�A�����\��CGI�̃p�X�y�摜���ɂ���Ȃ�K�{�@����ȊO�Ȃ�󗓂Ɂz
my $make_image_script = '';
#���e���v���[�gHTML�t�@�C���y�K�{�z
my $html_file = './tmp.html';
#���������݂�ۑ����郍�O�t�@�C���y�K�{�z
my $logfile ='./bvuetr/cvw5eym.cgi';
#���A�N�Z�X���O�擾�p�̃��O�t�@�C���y�K�{�z
my $access_logfile = './bvuetr/vqu1edd.cgi';
#�����b�N�t�@�C�����쐬����f�B���N�g���y�K���쐬���Ă������� �p�[�~�b�V������707��������777�z
my $lockfile_dir = './bvuetr/';
#���Ǘ��l�p�p�X���[�h  ���e�R�[�h�L�����ɏ������ނ��Ƃ��x���h���܂��y�K���ύX���Ă��������z
my $admin_code = 'vcxz0120';
#���Ǘ��l�p���O  ��̃p�X���[�h���L������ƐF���ς��܂�
my $admin_name = '�Ǘ��l304';
#���������ݍ폜�p�p�X���[�h  �R�[�h�L�����ɓ��͂��ĉ������y�K���ύX���Ă��������z
my $delete_code = 'vcxz0120';
#���ő�L���L�^�����y�A�N�Z�X���O�L�^���������˂܂��z
my $max = 200;
#����x�ɕ\������L����
my $display = 10;
#�����������N(1 -> on , 0 -> off)
my $autolink = 0;
#==============================================
# �F�w��Ȃ�
#==============================================
#�����t�̕����F
my $date_color = '#5F4943';
#���������ݔԍ��̕����F
my $num_color  = '#CFCFCF';
#��BBS�́uname�v�C�ucomment�v�Ȃǂ̕����F
my $moji_color = '#778899';
#�����O�̕����F
my $name_color = '#BE6B6B';
#�����O�ƃR�����g����؂�u>�v�̐F
my $divide_color = '#CFCFCF';
#���R�����g�̕����F
my $comment_color  = '#CFCFCF';
#���Ǘ��l�p�̕����F
my $admin_color = '#627D6E';
#��BBS�̃Z��(�㉺����)�̐F
my $cell_color = '#373333';
#���R�����g�\�����̔w�i�̐F
my $view_color = '#373333';
#�����O�̔��p�ł̌��E������
my $max_name = 20;
#���R�����g�̔��p�ł̌��E������
my $max_comment = 80;
#==============================================
# ���̑��̐ݒ�
#==============================================
#���R�����g���̃J���[�������_���ɂ���(1 -> yes , 0 -> no)
my $random_color_mode = 0;
#��JP�h���C���ȊO�̏������݂����ۂ���(1 -> yes , 0 -> no)
my $deny_proxy = 0;
#���R������\��������y�ʔz�z��Column CGI���g�p���Ă���ꍇ�z( 1 -> yes, 0 -> no)
my $column_view = 0;
#���R�����̃��O�t�@�C��������f�B���N�g���y�\��������ꍇ�K�{�z
my $column_dir = './column/';
#���R��������x�ɕ\��������������
my $column_number = 2;
#�����쌠�\��  �폜|�ύX|�ǋL|�ȗ����͂�������������
my $copyright = "<FONT color=\"$moji_color\">[mini BBS++ ver2.73] by </FONT><A href=\"http://www.midnightroam.org/\" target=\"_top\">Twilight Heaven</A>";
#���A�N�Z�X�͋֎~
my $denysan = "218.228.170.|218.228.171.";
#=============================================
#����{�I�Ȑݒ�͂����܂�
#=============================================
my $method = 'POST';
my $agent   = $ENV{'HTTP_USER_AGENT'};
my $addr    = $ENV{'REMOTE_ADDR'};
my $host    = $ENV{'REMOTE_HOST'};
my $referer = $ENV{'HTTP_REFERER'};
#if ($agent !~ m/MSIE/i){&error("Error: ���̃Q�[����IE��p�ł��B");}
if (($host eq $addr) || ($host eq '')) {
	$host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;
}
my $lockfile = $lockfile_dir . 'tmp.lock';
my($submit_code, $name, $comment, $mode, $line_num, %FORM) = &form_decode;
my($year,$mon,$date) = &get_time;
if ($host =~ /$denysan/ || $addr =~ /$denysan/) {&error("Error: �A�N�Z�X�͋֎~�ł��B");}

&main;
#=============================================
#�����C������
#=============================================
sub main {
	
	my(
		$count,
		$random_code,
		$column_data,
		$match,
		$html_start,
		$html_end,
		$image_tag,
		$log_form,
		$k,
		@lines
	);
	
	if ($mode eq 'regist' and $submit_code ne $delete_code) {
		&regist;
	}
	elsif ($mode eq 'regist' and $submit_code eq $delete_code) {
		&admin;
	}
	elsif ($mode eq 'delete_log' and $submit_code eq $delete_code) {
		&delete;
	}
	
	if (uc($ENV{'REQUEST_METHOD'}) eq 'GET') {
		$count = &log;
	}
	
	if ($count eq '') {
		open(IN, "$access_logfile") || &error("Error: �A�N�Z�X���O�ۑ��p�̃��O�t�@�C�����J���܂���B");
		$count = <IN>;
		chomp $count;
		close(IN);
	}
	
	open(IN, "$logfile") || &error("Error: �������ݕۑ��p�̃��O�t�@�C�����J���܂���B");
	@lines = <IN>;
	close(IN);
	
	$random_code = $lines[0];
	chomp $random_code;
	
	if ($column_view) { $column_data = &column_output; }
	
	open(FILE, "$html_file") || &error("Error: �e���v���[�g��HTML�t�@�C�����J���܂���B");
	if ($column_view) {
		while ( <FILE> ) {
			if ($_ =~ /<!--bbs-->/) {
				last;
			}
			else {
				$match = $_ =~ s/<!--column-->/$column_data/i;
				$html_start .= $_;
			}
		}
		while ( <FILE> ) {
			if (!$match) { $_ =~ s/<!--column-->/$column_data/i; }
			$html_end .= $_;
		}
	}
	else {
		while ( <FILE> ) {
			if ($_ =~ /<!--bbs-->/) {
				last;
			}
			else {
				$html_start .= $_;
			}
		}
		while ( <FILE> ) {
			$html_end .= $_;
		}
	}
	
	close(FILE);
	
	print "HTTP/1.1 200 OK\n";
	print "Content-Type: text/html\n";
	print "\n";
	print $html_start;
	
	if ($make_image_script ne '') {
		$image_tag = "<FONT color=\"$moji_color\"> -&gt; <IMG src=\"$make_image_script?$$\" align=absmiddle></FONT>";
	}
	else {
		$image_tag = '';
	}
	
	print <<"__START_BBS__";
<DIV align=center>
<TABLE border=0 bgColor="$cell_color" width="" height="" cellPadding=0 cellSpacing=0>
<TR>
<TD colSpan=2>
<TABLE border=0 bgColor="$cell_color" width="" height="" cellPadding=0 cellSpacing=0>
<FORM name="bbs" action="$script" method="$method">
<TR>
<TD bgColor="$cell_color" align=left noWrap><FONT color="$moji_color">���e�R�[�h�F</FONT></TD>
<TD colSpan=2 bgColor="$cell_color" align=left noWrap><INPUT type=text name="submit_code" size=8 value="$random_code">$image_tag</TD>
</TR>
<TR>
<TD bgColor="$cell_color" align=left noWrap><FONT color="$moji_color">���O�F</FONT></TD>
<TD colSpan=2  bgColor="$cell_color" align=left noWrap><INPUT type=text name=name size=8 value="$name"></TD>
</TR>
<TR>
<TD bgColor="$cell_color" align=left noWrap><FONT color="$moji_color">�R�����g�F</FONT></TD>
<TD bgColor="$cell_color" align=left noWrap><INPUT type=text name=comment size=40 value=""><INPUT type=hidden name=mode value=regist><INPUT type=submit value=��������><INPUT type=reset value=���Z�b�g>
<TD bgColor="$cell_color" align=right noWrap><FONT color="$moji_color">[ $count ]</FONT></TD>
</TR>
</FORM>
</TABLE>
</TD>
</TR>
<TR>
<TD colSpan=2 bgColor="$view_color">
__START_BBS__
	
	if ($mode eq 'log') {
		$display = $line_num;
	}
	
	foreach (1..$display) {
		
		if (!$lines[$_]) { last; }
		my($num,$date,$name,$admin,$comment,$r_color,$addr,$host,$agent) = split(/<>/, $lines[$_]);
		
		print "<FONT color=\"$num_color\">[$num]</FONT>&nbsp;";
		
		if ($admin) {
			print "<FONT color=\"$admin_color\">$name</FONT>&nbsp;<FONT color=\"$divide_color\">&gt;</FONT>&nbsp;\n";
		}
		else {
			print "<FONT color=\"$name_color\">$name</FONT>&nbsp;<FONT color=\"$divide_color\">&gt;</FONT>&nbsp;\n";
		}
		
		if ($autolink) {
			$comment =~ s/(https?|ftp|gopher|telnet|whois|news):\/\/([\w|\!\#\$\%\&\'\(\)\=\-\^\`\\\|\@\~\[\{\]\}\;\+\:\*\,\.\?\/]+)/<A href=\"$1:\/\/$2\">$1:\/\/$2<\/A>/g;
			$comment =~ s/([\w|\!\#\$\%\'\=\-\^\`\\\|\~\[\{\]\}\+\*\.\?\/]+)\@([\w|\!\#\$\%\'\(\)\=\-\^\`\\\|\~\[\{\]\}\+\*\.\?\/]+)/<A href="mailto:$1\@$2">$1\@$2<\/A>/g;
		}
		
		if ($random_color_mode) {
			print "<FONT color=\"$r_color\">$comment</FONT>";
		}
		else {
			print "<FONT color=\"$comment_color\">$comment</FONT>";
		}
		
		print "&nbsp;&nbsp;<FONT color=\"$date_color\"><SMALL>[$date]</SMALL></FONT><BR>\n";
	}
	
	$log_form = <<"__LOG_FORM__";
<FORM action="$script" method="$method">
<TD align=left bgColor="$cell_color">
<INPUT type=submit value="Log / Reload"><INPUT type=hidden name=mode value=log>
<SELECT name=line_num>
<OPTION selected>10
__LOG_FORM__
	
	for ($k=20; $k<=$max; $k+=10) {
		$log_form .= "<OPTION>$k\n";
	}
	
	$log_form .= "</SELECT></TD>\n</FORM>\n";
	
	print <<"__END_BBS__";
</TD>
</TR>
<TR>
$log_form
<TD align=right bgColor="$cell_color">
$copyright
</TD>
</TR>
</TABLE>
</DIV>
__END_BBS__
	
	print $html_end;
	exit;
}
#=============================================
#�����e���Ԃ��擾
#=============================================
sub get_time {
	
	my(
		$sec,
		$min,
		$hour,
		$mday,
		$mon,
		$year,
		$wday,
		$yday,
		$isdst,
		$day,
		$date
	);
	
	$ENV{'TZ'} = 'JST-9';
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
	$day = ('��','��','��','��','��','��','�y')[$wday];
	$year = $year + 1900;
	$mon = $mon + 1;
	$date = sprintf("%04d/%02d/%02d(%s) %02d:%02d:%02d",$year,$mon,$mday,$day,$hour,$min,$sec);
	
	return($year,$mon,$date);
}
#=============================================
#���t�H�[���f�[�^�̃f�R�[�h
#=============================================
sub form_decode {
	
	my(
		$data,
		$submit_code,
		$name,
		$comment,
		$mode,
		$line_num,
		@data,
		%FORM
	);
	
	if (uc($ENV{'REQUEST_METHOD'}) eq 'POST') {
		read(STDIN, $data, $ENV{'CONTENT_LENGTH'});
		@data = split(/&/, $data);
		foreach (@data) {
			my($name,$value) = split(/=/, $_);
			$value =~ tr/+/ /;
			$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
			$value =~ s/&/&amp;/g;
			$value =~ s/</&lt;/g;
			$value =~ s/>/&gt;/g;
			$value =~ s/\"/&quot;/g;
			$FORM{$name} = $value;
		}
		
		$submit_code = $FORM{'submit_code'};
		$name        = $FORM{'name'};
		$comment     = $FORM{'comment'};
		$mode        = $FORM{'mode'};
		$line_num    = $FORM{'line_num'};
		$name        =~ s/\r\n//g;
		$name        =~ s/\r|\n//g;
		$comment     =~ s/\r\n//g;
		$comment     =~ s/\r|\n//g;
	}
	
	return($submit_code, $name, $comment, $mode, $line_num, %FORM);
}
#=============================================
#���������݂��`�F�b�N�ネ�O�t�@�C���ɋL�^
#=============================================
sub regist {
	
	my(
		$r_color,
		$name_length,
		$comment_length,
		$random_code,
		$admin,
		$bno,
		$bdate,
		$bname,
		$badmin,
		$bcomment,
		$bcolor,
		$baddr,
		$bhost,
		$bagent,
		$no,
		$new_random_code,
		@lines
	);
	
	&deny_proxy if $deny_proxy;
	$r_color = &randomcolor;
	
	$name_length = length $name;
	$comment_length = length $comment;
	
	if ($name_length > $max_name) {
		&error("Error: HN���������ł��B�ő� $max_name �����ł��B���� $name_length �����ł��B");
	}
	if ($comment_length > $max_comment) {
		&error("Error: �R�����g���������ł��B�ő� $max_comment �����ł��B���� $comment_length �����ł��B");
	}
	
	if ($comment eq '') {
		&error("Error: �R�����g���L������Ă��܂���B");
	}
	if ($comment =~ /ON|�n�m|On|�n��|on|����|�E����|���Ȃ���|�Q�풆|�U�������|���j�����|��߂�|�����܂���|�I����|�I�����|�I����|�I����|����|�J����Ȃ���|�J�����/i) {
		&error("Error: �m�f���[�h������܂��B�`���E�f���E�`���b�g�ŁA�Q�풆�ɍU�����ꂽ�ȂǂƏ������ނ̂͋֎~�ł��B<br>����Ȃ��Ə����Ă��Ȃ��ꍇ�͕\\����ς��Ă݂ĉ������B");
	}
	
	open(LOG,"$logfile") || &error("Error: �������ݕۑ��p�̃��O�t�@�C�����J���܂���B");
	@lines = <LOG>;
	close(LOG);
	
	$random_code = shift @lines;
	chomp $random_code;
	
	if ($submit_code eq $admin_code) {
		$admin = 1;
		$name = $admin_name;
	}
	elsif ($submit_code eq $random_code) {
		$admin = 0;
	}
	else {
		&error("Error: ���e�R�[�h���X�V����Ă��܂��B�����[�h���Ă��������x��������ŉ������B");
	}
	
	if ($name eq '') {
		&error("Error: HN���L������Ă��܂���B");
	}
	
	($bno, $bdate, $bname, $badmin, $bcomment, $bcolor, $baddr, $bhost, $bagent) = split(/<>/, $lines[0]);
	
	if ($name eq $bname and $comment eq $bcomment) {
		&error("Error: ��d���e�ł��B");
	}
	
	$no = $bno + 1;
	
	$new_random_code = int(rand(100000));
	
	while ($max <= @lines) { pop @lines; }
	
	unshift(@lines, "$new_random_code\n$no<>$date<>$name<>$admin<>$comment<>$r_color<>$addr<>$host<>$agent\n");
	
	&lock;
	open(OUT,">$logfile") || &error("Error: �������ݕۑ��p�̃��O�t�@�C�����J���܂���B");
	print OUT @lines;
	close(OUT);
	&unlock;
	
}
#=============================================
#�������_���J���[�쐬
#=============================================
sub randomcolor {
	
	my(
		$red,
		$green,
		$blue,
		$r_color
	);
	
	srand(time|$$);
	$red = int(rand(256));
	$green = int(rand(256));
	$blue = int(rand(256));
	$r_color = uc(sprintf("#%02lx%02lx%02lx", $red, $green, $blue));
	
	return $r_color;
}
#=============================================
#���w��z�X�g�L�b�N
#=============================================
sub deny_proxy {
	
	if ( $host =~/\.jp$/i ) {
		&error("Error: jp�h���C���ȊO�̏������݂͋֎~����Ă��܂��B");
	}
}
#=============================================
#���G���[�������͂����ɋً}���
#=============================================
sub error {
	
	my $error_var = shift;
	
	&unlock;
	print "HTTP/1.1 200 OK\n";
	print "Content-Type: text/html\n";
	print "\n";
	print "<HTML>\n<BODY bgColor=#000000 text=#CFCFCF>\n$error_var\n<BR><BR>���h��<A href=\"$script\">��</A></BODY>\n</HTML>";
	exit;
}
#=============================================
#���Ǘ����[�h
#=============================================
sub admin {
	
	my $i = 1;
	my(
		$random_code,
		$num,
		$date,
		$name,
		$admin,
		$comment,
		$r_color,
		$addr,
		$host,
		$agent
	);

		print <<"__HTML__";
HTTP/1.1 200 OK
Content-Type: text/html

<HTML>
<HEAD>
<TITLE>�Ǘ��҃��[�h</TITLE>
</HEAD>
<BODY bgColor=#000000 text=#FFFFFF>
<FORM action="$script" method="$method">
<INPUT type=hidden name=submit_code value="$submit_code">
<INPUT type=hidden name=mode value="delete_log">
<TABLE>
__HTML__
	
	open(FILE, "$logfile") || &error("Error: �������ݕۑ��p�̃��O�t�@�C�����J���܂���B");
	<FILE>;
	while ( <FILE> ) {
		last if $_ =~ /^$/;
		($num,$date,$name,$admin,$comment,$r_color,$addr,$host,$agent) = split(/<>/, $_);
		print "<TR><TD><INPUT type=checkbox name=\"$i\">[$num]  $name &lt; $comment</TD></TR>\n";
		$i++;
	}
	close(FILE);
	
	print <<"__HTML__";
</TABLE>
<INPUT type=submit value="Delete">
</FORM>
<BR>
$copyright
</BODY>
</HTML>
__HTML__
	
	exit;
}
#=============================================
#���L���폜
#=============================================
sub delete {
	
	my($key, @lines);
	
	open(LOG,"$logfile") || &error("Error: �������ݕۑ��p�̃��O�t�@�C�����J���܂���B");
	@lines = <LOG>;
	close(LOG);
	
	foreach $key (keys %FORM) {
		if ($key =~ /^\d+$/) { $lines[$key] = ''; }
	}
	
	&lock;
	open(OUT,">$logfile") || &error("Error: �������ݕۑ��p�̃��O�t�@�C�����J���܂���B");
	print OUT @lines;
	close(OUT);
	&unlock;
}
#=============================================
#���A�N�Z�X���O�擾
#=============================================
sub log {
	
	my(
		$count,
		@lines
	);
	
	open(IN,"$access_logfile") || &error("Error: �A�N�Z�X���O�ۑ��p�̃��O�t�@�C�����J���܂���B");
	@lines = <IN>;
	close(IN);
	
	$count = shift @lines;
	$count++;
	while ($max <= @lines) { pop @lines; }
	unshift(@lines, "$count\n[$date] - $referer - $host - $addr - $agent\n");
	
	&lock;
	open(OUT,">$access_logfile") || &error("Error: �A�N�Z�X���O�ۑ��p�̃��O�t�@�C�����J���܂���B");
	print OUT @lines;
	close(OUT);
	&unlock;
	return $count;
}
#=============================================
#���t�@�C�����b�N
#=============================================
sub lock {
	
	my $flag = 0;
	
	foreach (1..10) {
		if (-e $lockfile) {
			sleep 1;
		}
		else {
			open(LOCK, ">$lockfile") || &error("Error: ���b�N�t�@�C�����J���܂���B<BR>�w�肵���f�B���N�g���̃p�[�~�b�V������707�ɂ��čēx�����Ă��������B");
			close(LOCK);
			$flag = 1;
			last;
		}
	}
	
#	if (!$flag) { &error("Error: ���ݏ������ݒ��ł��B���΂炭���҂����������B"); }
}
#=============================================
#�����b�N����
#=============================================
sub unlock {
	if (-e $lockfile) { unlink $lockfile; }
}
#=============================================
#���R�����L�����o
#=============================================
sub column_output {
	
	my $column_logfile = $column_dir . $year . '_' . $mon;
	my @lines;
	my $column_data;
	
	if (-e $column_logfile) {
		open(LOG,"$column_logfile");
		@lines = <LOG>;
		close(LOG);
	}
	else {
		return("�R�����̃��O�t�@�C����������܂���B");
	}
	
	foreach (1..$column_number) {
		if (!$lines[$_-1]) { last; }
		my($date,$com) = split(/<>/, $lines[$_-1]);
		chomp $com;
		#���������N
		if ($autolink) {
			$com =~ s/([^=^\"]|^)(http\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#]+)/$1<A href=$2 target=\"_top\">$2<\/A>/g;
		}
		
$column_data .= <<"__PRINT__";
$date
<BLOCKQUOTE>
$com
</BLOCKQUOTE>
<BR>
<BR>
__PRINT__
		
	}
	
	return($column_data);
}



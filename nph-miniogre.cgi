#!/usr/local/bin/perl

#=================================================================================
#	mini BBS++ ver2.73
#
#  last update: 09/12/2001
#       author: 長猫
#          url: http://www.midnightroam.org/
#
#  文字通り小さな掲示板です。テンプレートHTMLを
#  読み込み，BBS部分を追加して表示します。
#  荒らし対策にはランダムコードを使用しています。
#  画像式にする場合，0～9の画像と
#  画像連結CGI「makeimage.cgi」がそれぞれ別途必要です。
#
#	Copyright (c) 2000,2001  Twilight Heaven
#=================================================================================
use strict;
#==============================================
# 初期設定
#==============================================
#■このファイルの名前 適当に変えてください
my $script = './nph-miniogre.cgi';
#■画像連結＆表示CGIのパス【画像式にするなら必須　それ以外なら空欄に】
my $make_image_script = '';
#■テンプレートHTMLファイル【必須】
my $html_file = './tmp.html';
#■書き込みを保存するログファイル【必須】
my $logfile ='./bvuetr/cvw5eym.cgi';
#■アクセスログ取得用のログファイル【必須】
my $access_logfile = './bvuetr/vqu1edd.cgi';
#■ロックファイルを作成するディレクトリ【必ず作成してください パーミッションは707もしくは777】
my $lockfile_dir = './bvuetr/';
#■管理人用パスワード  投稿コード記入欄に書き込むことで騙りを防ぎます【必ず変更してください】
my $admin_code = 'vcxz0120';
#■管理人用名前  上のパスワードを記入すると色が変わります
my $admin_name = '管理人304';
#■書き込み削除用パスワード  コード記入欄に入力して下さい【必ず変更してください】
my $delete_code = 'vcxz0120';
#■最大記事記録件数【アクセスログ記録件数も兼ねます】
my $max = 200;
#■一度に表示する記事数
my $display = 10;
#■自動リンク(1 -> on , 0 -> off)
my $autolink = 0;
#==============================================
# 色指定など
#==============================================
#■日付の文字色
my $date_color = '#5F4943';
#■書き込み番号の文字色
my $num_color  = '#CFCFCF';
#■BBSの「name」，「comment」などの文字色
my $moji_color = '#778899';
#■名前の文字色
my $name_color = '#BE6B6B';
#■名前とコメントを区切る「>」の色
my $divide_color = '#CFCFCF';
#■コメントの文字色
my $comment_color  = '#CFCFCF';
#■管理人用の文字色
my $admin_color = '#627D6E';
#■BBSのセル(上下部分)の色
my $cell_color = '#373333';
#■コメント表示部の背景の色
my $view_color = '#373333';
#■名前の半角での限界文字数
my $max_name = 20;
#■コメントの半角での限界文字数
my $max_comment = 80;
#==============================================
# その他の設定
#==============================================
#■コメント文のカラーをランダムにする(1 -> yes , 0 -> no)
my $random_color_mode = 0;
#■JPドメイン以外の書き込みを拒否する(1 -> yes , 0 -> no)
my $deny_proxy = 0;
#■コラムを表示させる【別配布のColumn CGIを使用している場合】( 1 -> yes, 0 -> no)
my $column_view = 0;
#■コラムのログファイルがあるディレクトリ【表示させる場合必須】
my $column_dir = './column/';
#■コラムを一度に表示させたい件数
my $column_number = 2;
#■著作権表示  削除|変更|追記|省略等はご遠慮ください
my $copyright = "<FONT color=\"$moji_color\">[mini BBS++ ver2.73] by </FONT><A href=\"http://www.midnightroam.org/\" target=\"_top\">Twilight Heaven</A>";
#■アクセスは禁止
my $denysan = "218.228.170.|218.228.171.";
#=============================================
#■基本的な設定はここまで
#=============================================
my $method = 'POST';
my $agent   = $ENV{'HTTP_USER_AGENT'};
my $addr    = $ENV{'REMOTE_ADDR'};
my $host    = $ENV{'REMOTE_HOST'};
my $referer = $ENV{'HTTP_REFERER'};
#if ($agent !~ m/MSIE/i){&error("Error: このゲームはIE専用です。");}
if (($host eq $addr) || ($host eq '')) {
	$host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;
}
my $lockfile = $lockfile_dir . 'tmp.lock';
my($submit_code, $name, $comment, $mode, $line_num, %FORM) = &form_decode;
my($year,$mon,$date) = &get_time;
if ($host =~ /$denysan/ || $addr =~ /$denysan/) {&error("Error: アクセスは禁止です。");}

&main;
#=============================================
#■メイン処理
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
		open(IN, "$access_logfile") || &error("Error: アクセスログ保存用のログファイルが開けません。");
		$count = <IN>;
		chomp $count;
		close(IN);
	}
	
	open(IN, "$logfile") || &error("Error: 書き込み保存用のログファイルが開けません。");
	@lines = <IN>;
	close(IN);
	
	$random_code = $lines[0];
	chomp $random_code;
	
	if ($column_view) { $column_data = &column_output; }
	
	open(FILE, "$html_file") || &error("Error: テンプレートのHTMLファイルが開けません。");
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
<TD bgColor="$cell_color" align=left noWrap><FONT color="$moji_color">投稿コード：</FONT></TD>
<TD colSpan=2 bgColor="$cell_color" align=left noWrap><INPUT type=text name="submit_code" size=8 value="$random_code">$image_tag</TD>
</TR>
<TR>
<TD bgColor="$cell_color" align=left noWrap><FONT color="$moji_color">名前：</FONT></TD>
<TD colSpan=2  bgColor="$cell_color" align=left noWrap><INPUT type=text name=name size=8 value="$name"></TD>
</TR>
<TR>
<TD bgColor="$cell_color" align=left noWrap><FONT color="$moji_color">コメント：</FONT></TD>
<TD bgColor="$cell_color" align=left noWrap><INPUT type=text name=comment size=40 value=""><INPUT type=hidden name=mode value=regist><INPUT type=submit value=書き込む><INPUT type=reset value=リセット>
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
#■投稿時間を取得
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
	$day = ('日','月','火','水','木','金','土')[$wday];
	$year = $year + 1900;
	$mon = $mon + 1;
	$date = sprintf("%04d/%02d/%02d(%s) %02d:%02d:%02d",$year,$mon,$mday,$day,$hour,$min,$sec);
	
	return($year,$mon,$date);
}
#=============================================
#■フォームデータのデコード
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
#■書き込みをチェック後ログファイルに記録
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
		&error("Error: HNが長すぎです。最大 $max_name 文字です。現在 $name_length 文字です。");
	}
	if ($comment_length > $max_comment) {
		&error("Error: コメントが長すぎです。最大 $max_comment 文字です。現在 $comment_length 文字です。");
	}
	
	if ($comment eq '') {
		&error("Error: コメントが記入されていません。");
	}
	if ($comment =~ /ON|ＯＮ|On|Ｏｎ|on|ｏｎ|殺され|狩らないで|参戦中|攻撃するな|撃破するな|やめろ|見えませんか|オン時|オン狩り|オン中|オン撃|狩るな|カモらないで|カモるな/i) {
		&error("Error: ＮＧワードがあります。伝言板・掲示板・チャットで、参戦中に攻撃されたなどと書き込むのは禁止です。<br>そんなこと書いていない場合は表\現を変えてみて下さい。");
	}
	
	open(LOG,"$logfile") || &error("Error: 書き込み保存用のログファイルが開けません。");
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
		&error("Error: 投稿コードが更新されています。リロードしてからもう一度書き込んで下さい。");
	}
	
	if ($name eq '') {
		&error("Error: HNが記入されていません。");
	}
	
	($bno, $bdate, $bname, $badmin, $bcomment, $bcolor, $baddr, $bhost, $bagent) = split(/<>/, $lines[0]);
	
	if ($name eq $bname and $comment eq $bcomment) {
		&error("Error: 二重投稿です。");
	}
	
	$no = $bno + 1;
	
	$new_random_code = int(rand(100000));
	
	while ($max <= @lines) { pop @lines; }
	
	unshift(@lines, "$new_random_code\n$no<>$date<>$name<>$admin<>$comment<>$r_color<>$addr<>$host<>$agent\n");
	
	&lock;
	open(OUT,">$logfile") || &error("Error: 書き込み保存用のログファイルが開けません。");
	print OUT @lines;
	close(OUT);
	&unlock;
	
}
#=============================================
#■ランダムカラー作成
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
#■指定ホストキック
#=============================================
sub deny_proxy {
	
	if ( $host =~/\.jp$/i ) {
		&error("Error: jpドメイン以外の書き込みは禁止されています。");
	}
}
#=============================================
#■エラー発生時はここに緊急避難
#=============================================
sub error {
	
	my $error_var = shift;
	
	&unlock;
	print "HTTP/1.1 200 OK\n";
	print "Content-Type: text/html\n";
	print "\n";
	print "<HTML>\n<BODY bgColor=#000000 text=#CFCFCF>\n$error_var\n<BR><BR>モドル<A href=\"$script\">■</A></BODY>\n</HTML>";
	exit;
}
#=============================================
#■管理モード
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
<TITLE>管理者モード</TITLE>
</HEAD>
<BODY bgColor=#000000 text=#FFFFFF>
<FORM action="$script" method="$method">
<INPUT type=hidden name=submit_code value="$submit_code">
<INPUT type=hidden name=mode value="delete_log">
<TABLE>
__HTML__
	
	open(FILE, "$logfile") || &error("Error: 書き込み保存用のログファイルが開けません。");
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
#■記事削除
#=============================================
sub delete {
	
	my($key, @lines);
	
	open(LOG,"$logfile") || &error("Error: 書き込み保存用のログファイルが開けません。");
	@lines = <LOG>;
	close(LOG);
	
	foreach $key (keys %FORM) {
		if ($key =~ /^\d+$/) { $lines[$key] = ''; }
	}
	
	&lock;
	open(OUT,">$logfile") || &error("Error: 書き込み保存用のログファイルが開けません。");
	print OUT @lines;
	close(OUT);
	&unlock;
}
#=============================================
#■アクセスログ取得
#=============================================
sub log {
	
	my(
		$count,
		@lines
	);
	
	open(IN,"$access_logfile") || &error("Error: アクセスログ保存用のログファイルが開けません。");
	@lines = <IN>;
	close(IN);
	
	$count = shift @lines;
	$count++;
	while ($max <= @lines) { pop @lines; }
	unshift(@lines, "$count\n[$date] - $referer - $host - $addr - $agent\n");
	
	&lock;
	open(OUT,">$access_logfile") || &error("Error: アクセスログ保存用のログファイルが開けません。");
	print OUT @lines;
	close(OUT);
	&unlock;
	return $count;
}
#=============================================
#■ファイルロック
#=============================================
sub lock {
	
	my $flag = 0;
	
	foreach (1..10) {
		if (-e $lockfile) {
			sleep 1;
		}
		else {
			open(LOCK, ">$lockfile") || &error("Error: ロックファイルが開けません。<BR>指定したディレクトリのパーミッションを707にして再度試してください。");
			close(LOCK);
			$flag = 1;
			last;
		}
	}
	
#	if (!$flag) { &error("Error: 現在書き込み中です。しばらくお待ちください。"); }
}
#=============================================
#■ロック解除
#=============================================
sub unlock {
	if (-e $lockfile) { unlink $lockfile; }
}
#=============================================
#■コラム記事抽出
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
		return("コラムのログファイルが見つかりません。");
	}
	
	foreach (1..$column_number) {
		if (!$lines[$_-1]) { last; }
		my($date,$com) = split(/<>/, $lines[$_-1]);
		chomp $com;
		#自動リンク
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



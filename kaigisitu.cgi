#!/usr/bin/perl
	print "Content-type: text/html\n\n";
	
$var = "1.1";
###################################################################
#
# -------���p�K��ɂ���-----------------------------------------
# ���̃X�N���v�g��NET GAME Communications�uhttp://www.ngcoms.net/�v
# �Ŕz�z���Ă���ENDLESSBATTLE2�̒ǉ��v���O�����ł��B
#
# ���̃X�N���v�g�̓t���[�\�t�g�ł������쌠�͕������Ă���܂���B
# ���̃X�N���v�g���g�p������͈ȉ��̗��p�K��Ɋ�Â��g�p���Ă��������B
#
# 1.���̃X�N���v�g���g�p�����炩�̑��Q���������Ƃ��Ă��A��ҋy�ѓ��T�C
#   �g�ɐӔC�͖������Ƃ��܂��B
# 2.�������͂����R�ɍs���܂����A�l�̐ӔC�ɂ����čs���Ă�������
# 3.�Ĕz�z�͂����R�ɍs���镨�Ƃ��܂����A���쌠�\�����폜���Ȃ���
#   ������
#
###################################################################
#
# -------var 1.1�̒ǉ��_------------------------------------------
# �P�D�N�b�L�[���擾�̓�����𒼂��܂����B
# �Q�D�Ǘ��l�������̔���������Ȃ��_�𒼂��܂����B
#
###################################################################
#
# SCRIPTNAME	EBS KAIGISITU
# HOMEPAGE 	http://melcha.zone.ne.jp/ebs/dl/
# E-MAIL 	melchaa@hotmail.com
# (C)2002 44-net FACTORY
#
###################################################################
#
#---------------ENDLESSBATTLE�X�N���v�g�ւ̒ǉ�-------------------
#
# ebs_sub3.cgi��<input type=button>�Ȃǂ̃R�}���h�{�^��������ꏊ��
# �ȉ��̍s��ǉ����Ă��������B
#
# <td><input type=button value="��c��" $STYLE_B1 onClick="parent.Sub.location.replace('./kaigisitu.cgi')"></td>
#
# ���̃X�N���v�g�̖��O�@�Ə�����Ă��镔�������̃X�N���v�g�̖��O�ɕς��Ă��������B
#
##################################################################
#�e��ݒ�
#

use lib '.';
require 'ebs_sub1.cgi';		#ebs_sub1.cgi�̖��O�ł��B
$SCRIPT = "kaigisitu.cgi";	#���̃X�N���v�g�̖��O�ł��B
$file = "./$LOG_FOLDER/kaigisitu.log";	#�����ۑ��p�t�@�C�����ł��B
$TABLE_STYLEA = "bordercolor=#404040 border=1 cellspacing=0 style=\"font-size:16pt\"";#<TABLE>�̃X�^�C���ł��B�i�������p�e�[�u���j
$TABLE_STYLEB = "bordercolor=#404040 border=0 cellspacing=0 style=\"font-size:12pt\"";#<TABLE>�̃X�^�C���ł��B�i�����\���p�e�[�u���j
$max_com = "250";		#�ő唭���������ł��B
$max_log = "250";		#�ő�ۑ����O���ł��B
$master = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$master2 = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$master3 = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$master4 = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$master5 = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$master6 = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$master7 = "�Ǘ��l304";		#�Ǘ��҂̖��O�ł��B���̖��O�̐l�͑S�Ă̔�����������悤�ɂȂ�܂��B
$mastermode = "1000";		#�Ǘ��l���{���ł���s���ł��B

#�ݒ肱���܂�
##################################################################
#�������牺�̕�����perl���g�p�����v���O�����ł��B�����o����͈͂ŕύX���Ă��������B

#if($SUB && $ENV{'HTTP_REFERER'} !~ /^$THIS_DIR/){&ERROR("���ڃ����N�͋֎~�ł��B");}

if($SUB){&$SUB;}

if(!$FORM{'pname'}){

@pair = split(/;/, $ENV{'HTTP_COOKIE'});

foreach (@pair) {
my($key, $value) = split(/=/, $_);
$key =~ s/ //g;
$DUMMY{$key} = $value;
}

@pairs = split(/,/,$DUMMY{EB});

foreach (@pairs) {
my($key, $value) = split(/:/,$_);
$COOKIE{$key} = $value;
}

$FORM{'pname'} = $COOKIE{'pname'};
$FORM{'pass'} = $COOKIE{'pass'};
}

if(!$FORM{'pname'}){&COOKIE_IN;}

&MAIN_PAGE;
exit;

sub COOKIE_IN {

&HEADER;
print<<"HTMLTAG";
<table border=0 width=100% height=90%><tr><td align=center valign=middle>
<form action=$SCRIPT method=POST>
<input type=hidden name=cmd value=MAIN_PAGE>
<table $TABLE_STYLEA>
<tr><td bgcolor=$TABLE_COLOR2 colspan=2>��c�������</td></tr>
<tr>
<td bgcolor=$TABLE_COLOR2>���O</td>
<td bgcolor=$TABLE_COLOR1><input type=text size=30 name=pname $STYLE_B1></td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR2>�p�X���[�h</td>
<td bgcolor=$TABLE_COLOR1><input type=password size=30 name=pass $STYLE_B1></td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR1 colspan=2 align=right><input type=submit value=���� $STYLE_B1></td>
</tr>
</table>
</td></tr></table>
</form>
HTMLTAG
&END_HTML;
exit;
}

sub MAIN_PAGE {

&DBM_INPORT(C);
&DBM_INPORT(P);

@VALUES = split(/\s/,$P{"$FORM{'pname'}"});
@C_VAL = split(/\s/,$C{"$VALUES[5]"});
if(!$VALUES[5]){$VALUES[5] = $NONE_NATIONALITY;$optionB = "<option>$VALUES[5]";}
else{$optionB3 = "<option>$NONE_NATIONALITY";}
if(crypt($FORM{'pass'},eb) ne $VALUES[2]){&ERROR('�p�X���[�h���Ⴂ�܂��B');}

foreach $key (sort {$a cmp $b} keys %P){
if($key ne $FORM{'pname'}){$optionA = "$optionA<option>$key";}
}

foreach $key (sort {$a cmp $b} keys %C){
if($key ne $VALUES[5]){$optionB = "$optionB<option>$key";}
else{$optionB2 = "<option>$key";}
}

if($tokutei){$optionA1 = "<option>$tokutei";}

if($FORM{'country'} && $FORM{'country'} ne $VALUES[5]){$optionB1 = "<option>$FORM{'country'}";}

open(IN,"$file");
@log = <IN>;
close(IN);

&HEADER;

print<<"HTMLTAG";
<form action=$SCRIPT method=POST>
<input type=hidden name=cmd value=OUTPUT>
<input type=hidden name=pname value=$FORM{'pname'}>
<input type=hidden name=pass value=$FORM{'pass'}>
<input type=hidden name=icon value=$VALUES[27]>
<table $TABLE_STYLEA width=100%>
<tr>
<td bgcolor=$TABLE_COLOR1>
��&nbsp;$VALUES[5]���p��c��&nbsp;&nbsp;&nbsp;&nbsp;���O�F$FORM{'pname'}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;����$C_VAL[1]�f
<div align=right><a href=$SCRIPT?SETUMEI><font style="font-size:10pt">��c���̎g�p���@</font></a></div>
</td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR2>
<table $TABLE_STYLEB cellpadding=5 width=100%>
<tr>
<td bgcolor=$TABLE_COLOR2>
�����捑�I��
<select name=country $STYLE_B1>
$optionB1
$optionB2
<option value="">�S���ɔ���
$optionB
$optionB3
</select>
&nbsp;
�����摊��I��
<select name=aiteA $STYLE_B1>
$optionA1
<option value="">���I��
$optionA
</select>
&nbsp;
��������L��
<input type=text name=aiteB $STYLE_B1>
</td></tr>
<tr>
<td bgcolor=$TABLE_COLOR2>
�������L��
<input type=text name=comment $STYLE_B1 size=50>
&nbsp;
<input type=submit value=" �@ ���� �@ " $STYLE_B1>
&nbsp;
<input type=reset value="�N���A" $STYLE_B1>
</td></tr>
<tr>
<td bgcolor=$TABLE_COLOR2>
�y�\\�������F�z
&nbsp;&nbsp;&nbsp;<font color=#ffaaaa>�l��������</font>
&nbsp;&nbsp;&nbsp;<font color=#aaaaff>�������l��</font>
&nbsp;&nbsp;&nbsp;<font color=#ffffff>�S���ւ̔���</font>
&nbsp;&nbsp;&nbsp;<font color=#ffffaa>������������</font>
&nbsp;&nbsp;&nbsp;<font color=#ff0000 size=5><b>$errcom</b></font>
</td>
</form>
</tr></table>
</td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR1>

<table $TABLE_STYLEA width=100%>
<tr>
<td bgcolor=$TABLE_COLOR1>
HTMLTAG

$l=0;

foreach(@log){
$looked = 0;
($name,$country,$comment,$date,$icon,$tokutei,$looked) = split(/<>/);
$tokutei =~ s/\n//;
$country =~ s/all//;
$jikan = &DATE_DECORD($date);

if(!$tokutei){
$hantei = 0;
if(!$country){$fcolor = "#ffffff";}
else{$fcolor = "#ffffaa";}
}

elsif($tokutei eq $FORM{'pname'}){$hantei = 0;$fcolor = "#ffaaaa";if(!$looked){$looked = 1;$LOOK = 1;}}
elsif($name eq $FORM{'pname'}){$hantei = 0;$fcolor = "#aaaaff";}
else{$hantei = 1;}

if($FORM{'pname'} eq $master || $FORM{'pname'} eq $master2 || $FORM{'pname'} eq $master3 || $FORM{'pname'} eq $master4 || $FORM{'pname'} eq $master5 || $FORM{'pname'} eq $master6 || $FORM{'pname'} eq $master7){$max_com=$mastermode;$hantei=0;}
if($max_com <= $l) {last;}

if($VALUES[5] eq $country || !$country || $name eq $FORM{'pname'} || $tokutei || $FORM{'pname'} eq $master || $FORM{'pname'} eq $master2 || $FORM{'pname'} eq $master3 || $FORM{'pname'} eq $master4 || $FORM{'pname'} eq $master5 || $FORM{'pname'} eq $master6 || $FORM{'pname'} eq $master7){
if($hantei == 0){
print<<"TABLETAG";
<table border=0 width=100% style="font-size:12pt;">
<tr>
<td align=left><font color=$fcolor>$name&nbsp;��&nbsp;$comment</font></td>
<td align=right><font style="font-size:9pt">[&nbsp;$jikan&nbsp;]</font></td>
</tr>
</table>
<hr>
TABLETAG

$l++;
}
}
}

print<<"HTMLTAG";
</td></tr></table>
</td></tr></table>
HTMLTAG

&END_HTML;
}

sub SETUMEI {

&HEADER;
print<<"SETUMEITAG";
<table $TABLE_STYLE>
<tr>
<td bgcolor=$TABLE_COLOR2 colspan=2>
��c���̎g�p���@�ɂ���
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
�����捑�I��
</td>
<td bgcolor=$TABLE_COLOR1>
�I���������ɏ������Ă���l�S���Ɍ�����悤�ɔ������܂��B<br>
�����m�̊O������z���A�푈�I�����̈��A�Ȃǂ̎��Ɏg�p���Ă��������B
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
��������I��
</td>
<td bgcolor=$TABLE_COLOR1>
����̐l�����Ɍ�����悤�ɔ������܂��B<br>
����̐l�̊��U�C�����A���̚����A�O���̎����Ɏg�p���Ă��������B
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
��������L��
</td>
<td bgcolor=$TABLE_COLOR1>
���������I������̂��߂�ǂ��ȏꍇ�A������Ƀt���l�[�����L�����ĉ������B<br>
����̐l�̊��U�C�����A���̚����A�O���̎����Ɏg�p���Ă��������B
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
��L�R��ނ̗D�揇�ʂɂ���
</td>
<td bgcolor=$TABLE_COLOR1>
��������L������������I���������捑�I���̏��ɗD��x�������Ȃ�܂��B<br>
�����捑��I��������ŁC���������I�������ꍇ�C��������ɂ̂ݔ�����������l�ɂ��܂��B<br>
���������I�����C����������L�������ꍇ�́C�L����������ɕ\\������܂��B<br>
����������L���A�������͑I�������Ĕ���������ƁC��������I���������I�ɔ�����������̖��O�ɂȂ�܂��B
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
�������̒��ӂɂ���
</td>
<td bgcolor=$TABLE_COLOR1>
��x�����������͍̂폜���邱�Ƃ��o���܂���B�I���ɂ��Ă͋C�����čs���ĉ������B<br>
�T�C�g���ɂČ��߂��Ă��������C�Öق̗����ł��錏���ɂ��Ă͎���C�ԓ����s��Ȃ��l�ɂ��܂��傤�B<br>
��c���͌����̏�ł��B���l�ւ̖\\���C�����A�����Ȃǂ͂�߂܂��傤�B
</td>
</tr>

</table>
SETUMEITAG
&END_HTML;

}


sub OUTPUT {

if(!$FORM{'comment'}){&MAIN_PAGE;}
if($FORM{'aiteA'}){$tokutei = $FORM{'aiteA'};}

if($FORM{'aiteB'}){

&DBM_INPORT(P);

while (my($key,$val) = each %P){
if($FORM{'aiteB'} eq "$key"){$tokuteikensa = 1;}
}

if(!$tokuteikensa){$errcom = "�������肪���Ȃ����߁A�������L�����Z������܂���";&MAIN_PAGE;}

$tokutei = $FORM{'aiteB'};

}

&LOCK;
open(IN,"$file");
@log = <IN>;
close(IN);

$max_line = @log;

if($max_line >= $max_log){pop(@log);}

if($tokutei){$hatugensaki = "��$tokutei";}
elsif(!$FORM{'country'}){$hatugensaki = "";}
else{$hatugensaki = "��$FORM{'country'}�̍���";}

unshift(@log,"$FORM{'pname'}<>$FORM{'country'}<>$FORM{'comment'}&nbsp;$hatugensaki<>$DATE<>$FORM{'icon'}<>$tokutei<>0<>\n");

open(OUT,"> $file");
print OUT @log;
close(OUT);
chmod(0666,"$file");
&UNLOCK;
}


sub END_HTML {

print<<"ENDHTML";
<br><br><br>
<div align=center>
<font size=2>PROGRAMING:(C) 2002 - 
<a href=http://melcha.zone.ne.jp/ebs/dl/ target=_blank>
<font size=2>44NET FACTORY</font>
</a>
 - All Right Reserved.
</font>
</div>
<div align=right><font size=2 color=#ffffff>KAIGISITU var.$var</font></div>
<p>
</body>
</html>
ENDHTML

exit;
}

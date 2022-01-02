#!/usr/bin/perl
	print "Content-type: text/html\n\n";
	
$var = "1.1";
###################################################################
#
# -------利用規定について-----------------------------------------
# このスクリプトはNET GAME Communications「http://www.ngcoms.net/」
# で配布しているENDLESSBATTLE2の追加プログラムです。
#
# このスクリプトはフリーソフトですが著作権は放棄しておりません。
# このスクリプトを使用する方は以下の利用規定に基づき使用してください。
#
# 1.このスクリプトを使用し何らかの損害があったとしても、作者及び当サイ
#   トに責任は無い物とします。
# 2.改造等はご自由に行えますが、個人の責任において行ってください
# 3.再配布はご自由に行える物としますが、著作権表示を削除しないで
#   下さい
#
###################################################################
#
# -------var 1.1の追加点------------------------------------------
# １．クッキー未取得の入り口を直しました。
# ２．管理人が国宛の発言を見れない点を直しました。
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
#---------------ENDLESSBATTLEスクリプトへの追加-------------------
#
# ebs_sub3.cgiの<input type=button>などのコマンドボタンがある場所に
# 以下の行を追加してください。
#
# <td><input type=button value="会議室" $STYLE_B1 onClick="parent.Sub.location.replace('./kaigisitu.cgi')"></td>
#
# このスクリプトの名前　と書かれている部分をこのスクリプトの名前に変えてください。
#
##################################################################
#各種設定
#

use lib '.';
require 'ebs_sub1.cgi';		#ebs_sub1.cgiの名前です。
$SCRIPT = "kaigisitu.cgi";	#このスクリプトの名前です。
$file = "./$LOG_FOLDER/kaigisitu.log";	#発言保存用ファイル名です。
$TABLE_STYLEA = "bordercolor=#404040 border=1 cellspacing=0 style=\"font-size:16pt\"";#<TABLE>のスタイルです。（発言欄用テーブル）
$TABLE_STYLEB = "bordercolor=#404040 border=0 cellspacing=0 style=\"font-size:12pt\"";#<TABLE>のスタイルです。（発言表示用テーブル）
$max_com = "250";		#最大発言文字数です。
$max_log = "250";		#最大保存ログ数です。
$master = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$master2 = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$master3 = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$master4 = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$master5 = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$master6 = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$master7 = "管理人304";		#管理者の名前です。この名前の人は全ての発言が見られるようになります。
$mastermode = "1000";		#管理人が閲覧できる行数です。

#設定ここまで
##################################################################
#ここから下の部分はperlを使用したプログラムです。改造出来る範囲で変更してください。

#if($SUB && $ENV{'HTTP_REFERER'} !~ /^$THIS_DIR/){&ERROR("直接リンクは禁止です。");}

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
<tr><td bgcolor=$TABLE_COLOR2 colspan=2>会議室入り口</td></tr>
<tr>
<td bgcolor=$TABLE_COLOR2>名前</td>
<td bgcolor=$TABLE_COLOR1><input type=text size=30 name=pname $STYLE_B1></td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR2>パスワード</td>
<td bgcolor=$TABLE_COLOR1><input type=password size=30 name=pass $STYLE_B1></td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR1 colspan=2 align=right><input type=submit value=決定 $STYLE_B1></td>
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
if(crypt($FORM{'pass'},eb) ne $VALUES[2]){&ERROR('パスワードが違います。');}

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
■&nbsp;$VALUES[5]国用会議室&nbsp;&nbsp;&nbsp;&nbsp;名前：$FORM{'pname'}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;国費$C_VAL[1]Ｇ
<div align=right><a href=$SCRIPT?SETUMEI><font style="font-size:10pt">会議室の使用方法</font></a></div>
</td>
</tr>
<tr>
<td bgcolor=$TABLE_COLOR2>
<table $TABLE_STYLEB cellpadding=5 width=100%>
<tr>
<td bgcolor=$TABLE_COLOR2>
発言先国選択
<select name=country $STYLE_B1>
$optionB1
$optionB2
<option value="">全員に発言
$optionB
$optionB3
</select>
&nbsp;
発言先相手選択
<select name=aiteA $STYLE_B1>
$optionA1
<option value="">未選択
$optionA
</select>
&nbsp;
発言相手記入
<input type=text name=aiteB $STYLE_B1>
</td></tr>
<tr>
<td bgcolor=$TABLE_COLOR2>
発言文記入
<input type=text name=comment $STYLE_B1 size=50>
&nbsp;
<input type=submit value=" 　 発言 　 " $STYLE_B1>
&nbsp;
<input type=reset value="クリア" $STYLE_B1>
</td></tr>
<tr>
<td bgcolor=$TABLE_COLOR2>
【表\示文字色】
&nbsp;&nbsp;&nbsp;<font color=#ffaaaa>個人→自分宛</font>
&nbsp;&nbsp;&nbsp;<font color=#aaaaff>自分→個人宛</font>
&nbsp;&nbsp;&nbsp;<font color=#ffffff>全員への発言</font>
&nbsp;&nbsp;&nbsp;<font color=#ffffaa>自国民宛発言</font>
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
<td align=left><font color=$fcolor>$name&nbsp;＞&nbsp;$comment</font></td>
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
会議室の使用方法について
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
発言先国選択
</td>
<td bgcolor=$TABLE_COLOR1>
選択した国に所属している人全員に見られるように発言します。<br>
国同士の外交や宣戦布告、戦争終了時の挨拶などの時に使用してください。
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
発言相手選択
</td>
<td bgcolor=$TABLE_COLOR1>
特定の人だけに見られるように発言します。<br>
特定の人の勧誘，忠告、愛の囁き、外交の時等に使用してください。
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
発言相手記入
</td>
<td bgcolor=$TABLE_COLOR1>
発言相手を選択するのがめんどうな場合、こちらにフルネームを記入して下さい。<br>
特定の人の勧誘，忠告、愛の囁き、外交の時等に使用してください。
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
上記３種類の優先順位について
</td>
<td bgcolor=$TABLE_COLOR1>
発言相手記入→発言相手選択→発言先国選択の順に優先度が高くなります。<br>
発言先国を選択した上で，発言相手を選択した場合，発言相手にのみ発言を見られる様にします。<br>
発言相手を選択し，発言相手を記入した場合は，記入した相手に表\示されます。<br>
発言相手を記入、もしくは選択をして発言をすると，発言相手選択が自動的に発言した相手の名前になります。
</td>
</tr>

<tr>
<td bgcolor=$TABLE_COLOR2>
発言時の注意について
</td>
<td bgcolor=$TABLE_COLOR1>
一度発言したものは削除することが出来ません。選択については気をつけて行って下さい。<br>
サイト内にて決められている謎解き，暗黙の了解である件等については質問，返答を行わない様にしましょう。<br>
会議室は公共の場です。他人への暴\言，中傷、吹聴などはやめましょう。
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

if(!$tokuteikensa){$errcom = "発言相手がいないため、発言がキャンセルされました";&MAIN_PAGE;}

$tokutei = $FORM{'aiteB'};

}

&LOCK;
open(IN,"$file");
@log = <IN>;
close(IN);

$max_line = @log;

if($max_line >= $max_log){pop(@log);}

if($tokutei){$hatugensaki = "＞$tokutei";}
elsif(!$FORM{'country'}){$hatugensaki = "";}
else{$hatugensaki = "＞$FORM{'country'}の国民";}

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

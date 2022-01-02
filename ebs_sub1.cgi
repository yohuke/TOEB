use AnyDBM_File;
use Fcntl;
require 'jcodeLE.pl';
		@pair = split(/;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/,/, $DUMMY{EB});
		foreach (@pairs) {my($key, $value) = split(/:/, $_);$COOKIE{$key} = $value;}

require 'config.cgi';
$STYLE_L = "style=\"height:21px; color:$FC_LIST; font-size:16px; background:$BG_LIST; border:1 solid white; border-style:solid;\"";

$DBM_P="./$LOG_FOLDER/$DB_ID1";
$DBM_C="./$LOG_FOLDER/$DB_ID2";
$DBM_H="./$LOG_FOLDER/$DB_ID3";
$DBM_L="./$LOG_FOLDER/$DB_ID4";
$DBM_R="./$LOG_FOLDER/$DB_ID5";
$DATE=time;
$ENV{'TZ'} = 'JST-9';
@TIME = localtime(time);

#自動バックアップ
if ($TIME[2] == 13 && $TIME[1] == 40 && $TIME[6] == 0){
	$TIME[5]+=1900;$TIME[4]+=1;
	$DATESTR = "$TIME[5]$TIME[4]$TIME[3]_";
	use File::Copy;
	copy("$DBM_P.db", "$LOG_FOLDER2/$DATESTR$DB_ID1.db");
	copy("$DBM_C.db", "$LOG_FOLDER2/$DATESTR$DB_ID2.db");
	copy("$DBM_H.db", "$LOG_FOLDER2/$DATESTR$DB_ID3.db");
	copy("$DBM_L.db", "$LOG_FOLDER2/$DATESTR$DB_ID4.db");
	copy("$DBM_R.db", "$LOG_FOLDER2/$DATESTR$DB_ID5.db");
}

#クリスマスメンテ
if ($CRIMENTE==1){
#	&ERROR('Maintenance',"ジングルベル♪　ジングルベル♪　鈴が鳴る♪　カップル殺して　レアゲットHEY！");exit;
	&ERROR('Maintenance',"2年間、有難う御座いました！304先生の次回作にご期待下さい。");exit;
}

#緊急メンテ
if ($MENTE==1){
	require "serifu.data";
	my$sl=@serifu;
	my$sw=@serifu[int(rand($sl))];
	&ERROR('Maintenance',"$sw");exit;
}

##世界大戦
#毎月何日の？
#if ($TIME[3] =~ /^22$|^23$|^24$|^25$|^26$|^27$|^28$/i){$HIZUK_FRAG=1;}else{$HIZUK_FRAG=0;}
use DateTime;
my $ww = DateTime->last_day_of_month(
    year  => $TIME[5] + 1900,
    month => $TIME[4] + 1
)->subtract( days => 6 );
my $dt = DateTime->now();
$HIZUK_FRAG = $ww < $dt;
#if ($TIME[3] =~ /^1$|^2$|^3$|^4$|^5$|^6$|^7$/i){$HIZUK_FRAG=1;}else{$HIZUK_FRAG=0;}
#if ($TIME[3] =~ /^16$|^17$|^18$|^19$|^20$|^21$|^22$/i){$HIZUK_FRAG=1;}else{$HIZUK_FRAG=0;}
#$HIZUK_FRAG=1;
$WW_YOUBI ='0';		#何曜日？日=0、月=1、火=2、水=3、木=4、金=5、土=6
$WW_TIME0 ='20';	#開始直前の時間（時）
$WW_TIME3 ='40';	#開始直前の時間（分）
$WW_TIME1 ='21';	#開始時間（XX:00）
$WW_TIME2 ='22';	#終了時間（XX:59）

#開始直前の臨時ログイン規制時間（分）
if ($WorldWar==1 && $HIZUK_FRAG==1 && $TIME[6]==$WW_YOUBI && ($TIME[2]==$WW_TIME1 || $TIME[2]==$WW_TIME2)){
	$WW_FRAG=1;$WW_FRAG2=1;
}else{
	$WW_FRAG=0;$WW_FRAG2=0;
}
#if ($TIME[6]==$WW_YOUBI && $TIME[2]==$WW_TIME0 && $TIME[1] >= $WW_TIME3 && $LGIN_FRAG==1 && $HIZUK_FRAG == 1){&ERROR('Regulation',"世界大戦前の準備時間中です。世界大戦は $WW_TIME1時丁度より開始になります。");exit;}
if ($TIME[6]==$WW_YOUBI && $TIME[2]==$WW_TIME0 && $TIME[1] >= $WW_TIME3 && $HIZUK_FRAG == 1 && $WorldWar == 1){&ERROR('Regulation',"世界大戦前の準備時間中です。世界大戦は $WW_TIME1時丁度より開始になります。");exit;}
#&ERROR("$TIME[2]ああ$TIME[1]");

#if (($TIME[1] >= 40) && ($TIME[1] <= 59)){$LGIN_FRAG=1;}else{$LGIN_FRAG=0;}
#if ($TIME[2]==8 && $LGIN_FRAG==1){&ERROR('Regulation','午前 8：40～8：59はメンテ中です。');exit;}

#&ERROR("$ENV{'HTTP_USER_AGENT'}");

#if ($ENV{'HTTP_USER_AGENT'} !~ m/MSIE/i){&ERROR('このゲームはIE専用です。');exit;}
#if ($ENV{'HTTP_USER_AGENT'} =~ m/Netscape|Opera|Lynx|AOL|Cuam|Gecko|Sleipnir|Ninja|WWWC|fox|FOX/i){&ERROR('このゲームはIE専用です。');exit;}
#($user_agent =~ /Mozilla|MSIE|Netscape|Opera|Lynx|AOL|Cuam|Gecko|Sleipnir|Ninja|WWWC/)

if ($ENV{'REQUEST_METHOD'} eq "POST") {
	read(STDIN, $QUERY_DATA, $ENV{'CONTENT_LENGTH'});@pairs = split(/&/,$QUERY_DATA);
	foreach (@pairs) {
		($key, $value) = split(/=/, $_);
		$value =~ tr/+/ /;$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ s/\,//g;$value =~ s/=/＝/g;$value =~ s/&/＆/g;
		$value =~ s/</&lt;/g;$value =~ s/>/&gt;/g;$value =~ s/\n//g;$value =~ s/\s//g;
		&jcode'convert(*value,'sjis');
		$FORM{$key} = $value;
	}
	$FORM{'cmd'} && ($SUB="$FORM{'cmd'}");
}elsif($ENV{'QUERY_STRING'}){$SUB="$ENV{'QUERY_STRING'}";}

#ブラウザ判別
#if ($ENV{'HTTP_USER_AGENT'} !~ m/MSIE/i){&ERROR('IEのみ');exit;}

#} elsif ($user_agent =~ /Mozilla|MSIE|Netscape|Opera|Lynx|AOL|Cuam|Gecko|Sleipnir|Ninja|WWWC/) {

if ($ENV{'REQUEST_METHOD'} eq "POST") {
	read(STDIN, $QUERY_DATA, $ENV{'CONTENT_LENGTH'});@pairs = split(/&/,$QUERY_DATA);
	foreach (@pairs) {
		($key, $value) = split(/=/, $_);
		$value =~ tr/+/ /;$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ s/</&lt;/g;$value =~ s/>/&gt;/g;$value =~ s/\n//g;$value =~ s/\s//g;
		$value =~ s/\,//g;$value =~ s/=/＝/g;$value =~ s/&/＆/g;
		&jcode'convert(*value,'sjis');
		$FORM{$key} = $value;
	}
	$FORM{'cmd'} && ($SUB="$FORM{'cmd'}");
}elsif($ENV{'QUERY_STRING'}){$SUB="$ENV{'QUERY_STRING'}";}

sub HEADER {
	$BG_MAIN="bgcolor=\"$BG_MAIN\"" if $BG_MAIN !~ /\./;
	$BG_MAIN="background=\"$BG_MAIN\"" if $BG_MAIN =~ /\./;
	print "HTTP/1.1 200 OK\n$SCKIE";
	print "Content-Type: text/html\n";
	print "\n";
	print << "	-----END-----";
	<!--美乳-->
	<!DOCTYPE HTML PUBLIC -//IETF//DTD HTML//EN>
	<html lang="ja"><head>
	<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
	<meta http-equiv="Pragma" CONTENT="no-cache">
	<title>Tactics Ogre de Endless Battle 304 Edition</title>
	-----END-----
	if($_[0] eq "Status"){
	print << "	-----END-----";
	<style type="text/css">
	a:link	{text-decoration:none; color:$LINK;}
	a:visited	{text-decoration:none; color:$LINK;}
	a:active	{text-decoration:none; color:$LINK;}
	a:hover	{text-decoration:none; color:$HOVER;}
	a img {border-style:none;}
	INPUT	{color:$FC_BUTTON; border-color:$TABLE_BORDER; background:$BG_BUTTON; height:20px; font-size:14px;}
	.td1	{background-color:$TABLE_COLOR2; font-size:10px;}
	.td2	{border:1px solid $TABLE_BORDER;}
	.td3	{background-color:$TABLE_COLOR2; font-size:13px;}
	.td4	{border:1px solid $TABLE_BORDER; font-size:12px;}
	</style>
	<script language="JavaScript">
		function showclas1(){clas1.style.visibility='visible';}
		function hideclas1(){clas1.style.visibility='hidden';}
		function showclaspl1(){claspl1.style.visibility='visible';}
		function hideclaspl1(){claspl1.style.visibility='hidden';}
	-----END-----
	$WN_sA[7] .='!2o' if $WN_sB[7] =~ m/!2q/ || $WN_sC[7] =~ m/!2q/ || $WN_sD[7] =~ m/!2q/;
	$WN_sA[7] .='!2p' if $WN_sB[7] =~ m/!2r/ || $WN_sC[7] =~ m/!2r/ || $WN_sD[7] =~ m/!2r/;
	$WN_sA[7] .='!2o' if $WN_sT[13] =~ m/!x2q/ || $WN_sU[13] =~ m/!x2q/;
	$WN_sA[7] .='!2p' if $WN_sT[13] =~ m/!x2r/ || $WN_sU[13] =~ m/!x2r/;
	@WN_sA_ef = split(/!/,$WN_sA[7]);
	foreach $j(@WN_sA_ef){
	print << "	-----END-----" if $j;
		function showclasy$j(){clas$j.style.visibility='visible';}
		function hideclasy$j(){clas$j.style.visibility='hidden';}
	-----END-----
	}
	$WN_sS[13] .='!x2o' if $WN_sT[13] =~ m/!x2q/ || $WN_sU[13] =~ m/!x2q/;
	$WN_sS[13] .='!x2p' if $WN_sT[13] =~ m/!x2r/ || $WN_sU[13] =~ m/!x2r/;
	@WN_sS_ef = split(/!/,$WN_sS[13]);
	foreach $j2(@WN_sS_ef){
	print << "	-----END-----" if $j2;
		function showclasx$j2(){clas$j2.style.visibility='visible';}
		function hideclasx$j2(){clas$j2.style.visibility='hidden';}
	-----END-----
	}
	}else{
	print << "	-----END-----";
	<style type="text/css">
	INPUT	{color:$FC_BUTTON; border-color:$TABLE_BORDER; background:$BG_BUTTON;}
	SELECT	{color:$FC_LIST; border:1 solid white; border-style:solid; background:$BG_LIST; height:21px; font-size:16px;}
	.rb1	{color:#A1C3C2;}
	.rb2	{color:#E2D0A7;}
	.rb3	{color:#C4E9BE;}
	.rb4	{color:#DDA7BC;}
	</style>
	-----END-----
	}
	print << "	-----END-----";
	</script>
	<script language="javascript"><!--
	load_tag = "Now loading...";
	function load() {
		if(document.all){
		loading.style.visibility = "hidden";
		content.style.visibility = "visible";
		return 0;
		}
	}
	function hide() {
		content.style.visibility = "hidden";
		loading.style.visibility = "visible";
	}
	function hide2() {
		content.style.visibility = "hidden";
		loading.style.visibility = "visible";
	}

	function kdown(e) {var msg =""; var flg = 1;
		switch(window.event.srcElement.tagName){case "INPUT" :if(event.srcElement.type != "text" && event.srcElement.type != "password"){return false;}flg = 0;break;case "TEXTAREA" :flg = 0;break;}
		switch(event.keyCode){case  8 :msg = "BS";break;case 27 :msg = "Esc";break;case 82 :if(event.ctrlKey){msg = "Ctrl+R";}break;case 116 :msg = "F5";break;case 122 :msg = "F11";break;}
		if (flg == 1 ) {if(event.altKey || event.shiftKey){alert("ここでShiftやAltは使用できません");return false;}}
		if (flg == 0 ) {switch(event.keyCode){case 8 :msg = "";break;}}
		if (msg != "" ) {event.keyCode = 0;return false;}else{return true;}
	}
	document.onkeydown = kdown;


	//--></script></head>
	<body $BG_MAIN text="$FONT_COLOR" style=\"margin:0px 0px 0px 0px;\" oncontextmenu="return false;" onLoad="load()">
	<script language="javascript"><!--
	if(document.all){
	document.write('<div id="loading" style="position:absolute; width:100%; height:100%; z-index:1; left: 0; top: 0; visibility: visible">'); 
	document.write('<table border="0" height="100%" align="center"><tr><td>' + load_tag + '</td></tr></table>');
	document.write('</div>');
	document.write('<div id="content" style="visibility:hidden">');
	}
	//--></script>
	-----END-----
}
sub FOOTER	{
#下記はライセンス表示なので、絶対に削除修正禁止。追加は可。

	print '<br><span style="font-size:15px;font-weight:bold;">';
	print << "	-----END-----";
	<br>
	The ENDLESS BATTLE Program Satellite 1.05<br>
	Produce By
	<a href="http://www.endlessbattle.net/" target=_blank style="font-size:15px;color:$FONT_COLOR;"><font face=\"Verdana\">&copy NET GAME Communications</font></a><br>
	All Right Reserved.<br>
	Modified By <a href="http://ogre.s1.xrea.com/" target=_blank style="font-size:15px;color:$FONT_COLOR;"><font face=\"Verdana\">Clare Harmolare & vana</font></a><br>
	
	-----END-----
	print "<br>This Site Owner is $OWNER_NAME" if $OWNER_NAME;
	print "<br>Icon &copy $COPYRIGHT_ICON All Right Reserved" if $COPYRIGHT_ICON;
	print "</span>";
	print "<script language=\"javascript\"><!--";
	print "if(document.all){document.write('</div>');}";
	print "//--></script>";
	print << "	-----END-----";
<br>
<script type="text/javascript"><!--
google_ad_client = "pub-7759470714947522";
/* 728x90, 作成済み 08/05/24 */
google_ad_slot = "8071608975";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
#src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
<noscript>
#<a href="http://www.abcoroti.com/~rent/rspace/" target="_blank">FreeServerOROTI</a>
</noscript>
<br>
	-----END-----
}
sub DBM_INPORT {
	$DBM = "DBM_$_[0]";
	$HASH=$_[0];
	tie %NOTE,AnyDBM_File,"$$DBM",O_RDONLY,0666;
		%$HASH=%NOTE;
	untie %NOTE;
}
sub DBM_CONVERT {
	$DBM = "DBM_$_[0]";
	$DBM_TYPE1="$_[0]L_VALUES";
	$DBM_KEY1="$_[1]";

	($DBM_TYPE2="$_[2]_VALUES",$DBM_KEY2="$_[3]") if $_[2];
	
	tie %NOTE,AnyDBM_File,"$$DBM",O_RDONLY,0666;
		@$DBM_TYPE1 = split(/\s/,$NOTE{"$DBM_KEY1"});
		@$DBM_TYPE2 = split(/\s/,$NOTE{"$DBM_KEY2"}) if $_[2];
	untie %NOTE;
}

sub REPAIR {
	my $DatHp=0;
	my $target = $_[0];
	my ($DatHp,$Result) = split(/\!/,$target->[1]);
	if($FORM{'yousai'} && $target->[2] eq "要塞"){
	$target->[15]+=int(($DATE-$DatHp)*$YO_REPAIR);
	}else{
	$target->[15]+=int(($DATE-$DatHp)*($target->[16]*$HP_REPAIR/100+$HP_REPAIR2));
	}
	if(($target->[15])>=($target->[16])){$target->[15]=$target->[16];$target->[25]=0;}
	$target->[17]+=int(($DATE-$DatHp)*$EN_REPAIR);
	if(($target->[17])>=($target->[18])){$target->[17]=$target->[18];}
	$target->[14]-=int(($DATE-$DatHp)*$RISK_REPAIR);
	if(($target->[14]) < 0){$target->[14]=0;}


}

sub RANK{
$r=int $_[0]/10;
$r=21 if $r > 21;$r=0 if $r < 0;
my $K_C=('#808080','#8000ff','#8000ff','#a000e5','#00518b','#00518b','#0470a5','#0470a5','#559494','#559494','#80b280','#80b280','#80b280','#2a980b','#2a980b','#2a980b','#c0c54d','#c0c54d','#c0c54d','#c0c54d','#d27880','#d27880')[$r];

my $K_N=$CLASS_NAME[$r];

	my $kaikyu="<font color=$K_C>$K_N</font>";
	if ($_[2] == -3){$kaikyu='';}
	if ($_[2] == 1){$kaikyu="<font color=#f7e957>$CLASS_NAME[22]</font>";}
	if ($_[2] == -1){$kaikyu.='<font color=#f7e957>（隊長）</font>';}
	if ($_[1] eq "$NONE_NATIONALITY" || !$_[1]){$kaikyu='';}
	return $kaikyu;
}
sub CALCTIME{
	$Dt_Calctime = time;
	return "$Dt_Calctime";
}
sub STATUS_CONVERT{
	$_[1] eq 's' && do {
		my $c=int $_[0]/5;$c=0 if $c < 0;$c=10 if $c > 10;
		my $C_C=('#5000CC','#8000ff','#a000e5','#bf00cc','#df00a6','#ff0080','#f7e957',
					'#f7e957','#f7e957','#ff0080','#ff0080')[$c];
		my $C_R=('F','E','D','C','B','A','S','SS','SSS','ACE','NT')[$c];
	return "<b style=\"color:$C_C;\">$C_R</b>";
	last STATUS_CONVERT;
	};
	$_[1] eq 'u' && do {
		my $c=$_[0];
		my $C_R=$TYPE_IMAGE[$c];
	return "<img src=\"$IMG_FOLDER5/$C_R\" width=\"64\" height=\"64\">";
	last STATUS_CONVERT;
	};
	$_[1] eq 'j' && do {
		my $c=$_[0]/100;$c=0 if $c < 0;$c=10 if $c > 10;
		my $C_C=(	'#5000CC','#8000ff','#a000e5','#bf00cc','#df00a6','#ff0080','#f7e957',
					'#f7e957','#f7e957','#ff0080','#ff0080')[$c];
		my $C_R=('F','E','D','C','B','A','S','SS','SSS','ACE','NT')[$c];
	return "<font face=\"Verdana\" color=$C_C>$C_R</font>";
	last STATUS_CONVERT;
	};
	$_[1] eq 'a' && do {
		my $c=$_[0]/12;$c=0 if $c < 0;$c=8 if $c > 8;
		my $C_C=('#567598','#667388','#757179','#846f6a','#936d5b','#ae9184','#c9b6ad','#e4dad6','#ffffff')[$c];
		my $C_R=('Chaos','Chaos','Chaos','Neutral','Neutral','Neutral','Law','Law','Law')[$c];
	return "<font face=\"Verdana\" color=$C_C>$C_R</font>";
	last STATUS_CONVERT;
	};
	$_[1] eq 'l' && do {
		my $c=$_[0]/12;$c=0 if $c < 0;$c=8 if $c > 8;
		my $C_C=('#567598','#667388','#757179','#846f6a','#936d5b','#ae9184','#c9b6ad','#e4dad6','#ffffff')[$c];
		my $C_R=('C','C','C','N','N','N','L','L','L')[$c];
	return "<font face=\"Verdana\" color=$C_C>$C_R</font>";
	last STATUS_CONVERT;
	};
	$_[1] eq 'e' && do {
		my $c=$_[0];
		my $C_R=('d0.gif','d1.gif','d2.gif','d3.gif','d4.gif','d5.gif')[$c];
	return "<img src=\"$IMG_FOLDER3/$C_R\" width=\"16\" height=\"16\">";
	last STATUS_CONVERT;
	};
	$_[1] eq 'z' && do {
		my $c=$_[0]/10;$c=0 if $c < 0;$c=10 if $c > 10;
		my $C_R=('－','★1','★2','★3','★4','★5','★6','★7','★8','★9','★10')[$c];
	return "$C_R";
	last STATUS_CONVERT;
	};
}
sub DATE_DECORD	{
	my @lt = localtime($_[0]);
	$lt[4]++;
	$lt[2] = sprintf("%02d", $lt[2]);
	$lt[1] = sprintf("%02d", $lt[1]);
	if($lt[4] == 1 && $lt[3] <= 24){$RYU="神";$ZETE=$lt[3];
	}elsif($lt[4] == 1 && $lt[3] >= 25 || $lt[4] == 2 && $lt[3] <= 18){$RYU="地";
	$ZETE=$lt[3]-24 if $lt[3] >= 25;$ZETE=$lt[3]+7 if $lt[3] <= 18;
	}elsif($lt[4] == 2 && $lt[3] >= 19 || $lt[4] == 3 && $lt[3] <= 13){$RYU="水";
	$ZETE=$lt[3]-18 if $lt[3] >= 19;$ZETE=$lt[3]+11 if $lt[3] <= 13;
	}elsif($lt[4] == 3 && $lt[3] >= 14 || $lt[4] == 4 && $lt[3] <= 6){$RYU="影";
	$ZETE=$lt[3]-13 if $lt[3] >= 14;$ZETE=$lt[3]+18 if $lt[3] <= 6;
	}elsif($lt[4] == 4 && $lt[3] >= 7 || $lt[4] == 5 && $lt[3] == 1){$RYU="白";
	$ZETE=$lt[3]-6 if $lt[3] >= 7;$ZETE=$lt[3]+24 if $lt[3] == 1;
	}elsif($lt[4] == 5 && ($lt[3] >= 2 && $lt[3] <= 25)){$RYU="炎";$ZETE=$lt[3]-1;
	}elsif($lt[4] == 5 && $lt[3] >= 26 || $lt[4] == 6 && $lt[3] <= 18){$RYU="風";
	$ZETE=$lt[3]-25 if $lt[3] >= 26;$ZETE=$lt[3]+6 if $lt[3] <= 18;
	}elsif($lt[4] == 6 && $lt[3] >= 19 || $lt[4] == 7 && $lt[3] <= 13){$RYU="金";
	$ZETE=$lt[3]-18 if $lt[3] >= 19;$ZETE=$lt[3]+12 if $lt[3] <= 13;
	}elsif($lt[4] == 7 && $lt[3] >= 14 || $lt[4] == 8 && $lt[3] <= 6){$RYU="雷";
	$ZETE=$lt[3]-13 if $lt[3] >= 14;$ZETE=$lt[3]+18 if $lt[3] <= 6;
	}elsif($lt[4] == 8 && ($lt[3] >= 7 && $lt[3] <= 30)){$RYU="闇";$ZETE=$lt[3]-6;
	}elsif($lt[4] == 8 && $lt[3] >= 31 || $lt[4] == 9 && $lt[3] <= 24){$RYU="海";
	$ZETE=$lt[3]-30 if $lt[3] >= 31;$ZETE=$lt[3]+1 if $lt[3] <= 24;
	}elsif($lt[4] == 9 && $lt[3] >= 25 || $lt[4] == 10 && $lt[3] <= 18){$RYU="黒";
	$ZETE=$lt[3]-24 if $lt[3] >= 25;$ZETE=$lt[3]+6 if $lt[3] <= 18;
	}elsif($lt[4] == 10 && $lt[3] >= 19 || $lt[4] == 11 && $lt[3] <= 11){$RYU="双";
	$ZETE=$lt[3]-18 if $lt[3] >= 19;$ZETE=$lt[3]+13 if $lt[3] <= 11;
	}elsif($lt[4] == 11 && $lt[3] >= 12 || $lt[4] == 12 && $lt[3] <= 6){$RYU="火";
	$ZETE=$lt[3]-11 if $lt[3] >= 12;$ZETE=$lt[3]+19 if $lt[3] <= 6;
	}elsif($lt[4] == 12 && $lt[3] >= 7){$RYU="光";$ZETE=$lt[3]-6;
	}
	return "$RYU竜の月$ZETE日<small>～ $lt[4]/$lt[3] ～</small>〔$lt[2]:$lt[1]〕";
}
sub ERROR		{
	if($_[0] eq "NameError"){
		SET_COOKIE:{
		my @gmt = gmtime(time + $COOKIE_KEEP*24*60*60);
		$gmt[0] = sprintf("%02d", $gmt[0]);	$gmt[1] = sprintf("%02d", $gmt[1]);
		$gmt[2] = sprintf("%02d", $gmt[2]);	$gmt[3] = sprintf("%02d", $gmt[3]);	$gmt[5] += 1900;
		$gmt[4] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$gmt[4]];
		$gmt[6] = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$gmt[6]];
		my $date_gmt = "$gmt[6], $gmt[3]\-$gmt[4]\-$gmt[5] $gmt[2]:$gmt[1]:$gmt[0] GMT";
		my $cook = "";$SCKIE="Set-Cookie: EB=$cook; expires=$date_gmt\n";
		}
	}
	if($_[0] eq "Regulation" || $_[0] eq "Maintenance"){
	&HEADER;
	print << "	-----END-----";
	<table bordercolor=\"$TABLE_BORDER\" border=1 cellspacing=0 style="font-size:10pt;">
		<tr><td bgcolor=\"$TABLE_COLOR2\"><b>ログイン規制時間中～歴史～</b></td></tr>
	-----END-----
	$c=0;
	dbmopen (%NOTE,"$DBM_H",0666);
		foreach $Key (sort {$b <=> $a} keys %NOTE){$c++;
			if ($c <= $HISTORY_MAX){
				print "<tr><td bgcolor=\"$TABLE_COLOR1\"><b>".&DATE_DECORD($Key)."</b>&nbsp;&nbsp;$NOTE{$Key}</td></tr>\n";
			}else{delete $NOTE{$Key};}
		}
	dbmclose %NOTE;
	print "</table>\n<script language=\"JavaScript\">\nalert('$_[0]\\n$_[1]')\;\n\n</script>";
	&FOOTER;exit;
	}
	&HEADER;
	print "<script language=\"JavaScript\">\nalert('$_[0]\\n$_[1]')\;\n\n</script>";
	&FOOTER;exit;
}
sub LOCK 	{open (LOCK, "eb.lock");flock(LOCK,2);}
sub UNLOCK  {flock(LOCK,8);close(LOCK);}

sub JScfm {
	$fct=$_[0];
	$msg=$_[1];
	print << "	END_OF_HTML";
	<script language="JavaScript">
	<!--
	function $fct (){
		if (confirm('$msg') == true){return true;}else{return false}
	}
	//-->
	</script>
	END_OF_HTML
}
sub LOGIN_CHECK{
my($char_name, $timer1, $timer2, @char_value, $login_flg, @log_data, %L_buff);
$char_name = $_[0];

$timer1 = 20;		#分指定（戦闘時間からの経過分）
$timer2 = 20;		#分指定（ログイン時間からの経過分）

if(!%P){ &DBM_INPORT(P); }

@char_value = split(/\s/,$P{"$char_name"});
if($char_value[26] >= time - $timer1 * 60){ $login_flg = 1; }
elsif($char_name eq '管理人304' || $char_name eq 'メルト屋304たんｖ'){ $login_flg = 1; }
else{ $login_flg = 0; }

if($login_flg == 0){
if(!%L){ &DBM_INPORT(L); }
%L_buff = %L;
foreach $login_time (sort {$b <=> $a} keys %L_buff){

if($login_time < time - $timer2 * 60){ last; }
@log_data=split(/!/, $L_buff{"$login_time"});
if($log_data[0] eq $char_name){ $login_flg = 1;}
}
}
return $login_flg;
}


1;

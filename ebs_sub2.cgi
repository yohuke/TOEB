sub LOGIN2{
	$BG_TOP="bgcolor=\"$BG_TOP\"" if $BG_TOP !~ /\./;
	$BG_TOP="background=\"$BG_TOP\"" if $BG_TOP =~ /\./;

	print "HTTP/1.1 200 OK\n";
	print "Content-Type: text/html\n";
	print "\n";
	print << "	-----END-----";
	<!--美乳-->
	<!DOCTYPE HTML PUBLIC -//IETF//DTD HTML//EN>
	<html><head>
	<script language="JavaScript">
		function showform(){login.style.visibility='visible';}
		function hideform(){login.style.visibility='hidden';}
		function showdata(){data.style.visibility='visible';}
		function hidedata(){data.style.visibility='hidden';}
	function kdown(e) {var msg =""; var flg = 1;
		switch(window.event.srcElement.tagName){case "INPUT" :flg = 0;break;case "TEXTAREA" :flg = 0;break;}
		switch(event.keyCode){case  8 :msg = "BS";break;case 27 :msg = "Esc";break;case 82 :if(event.ctrlKey){msg = "Ctrl+R";}break;case 116 :msg = "F5";break;}
		if (flg == 1 ) {if(event.altKey || event.shiftKey){alert("ここでShiftやAltは使用できません");return false;}}
		if (flg == 0 ) {switch(event.keyCode){case 8 :msg = "";break;}}
		if (msg != "" ) {event.keyCode = 0;return false;}else{return true;}
	}
	document.onkeydown = kdown;
	</script>
	<style type="text/css">
		a:link    {font-size: 17px; text-decoration:none; color:$LINK; }
		a:visited {font-size: 17px; text-decoration:none; color:$LINK; }
		a:active  {font-size: 17px; text-decoration:none; color:$LINK; }
		a:hover   {font-size: 17px; text-decoration:none; color:$HOVER; }
		td	{background-repeat:no-repeat;background-position:top;text-align: center;}
		.title{margin-top:110px;}
	</style>
	<meta http-equiv="Content-Type" content="text/html; charset=x-sjis">
	<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
	<body $BG_TOP text=#dcdcdc link=#dcdcdc style=\"margin:0px 0px 0px 0px;\" oncontextmenu="return false;">
	<body oncontextmenu="return false">
	<a name=#top>
	<table width=100% height=100% id="login" style="position:absolute;visibility:hidden;"><tr><td align=center>
		<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:16px;">
		<form action=$MAIN_SCRIPT method=POST name=frm1 style=\"margin:0px 0px 0px 0px;\">
		<tr><td style="background-color:$TABLE_COLOR2;" colspan=2>
		&nbsp;Log In</td>
		<td style="background-color:$TABLE_COLOR2;" align=right><a href="Javascript:hideform();"><b>×</b></A></td></tr>
		<tr><td align=center><input type=hidden name="cmd" value="MAIN_FRAME">
		<input type=hidden name="login" value="$DATE">
		<b>ID</b></td>
		<td><input type=text name="pname" value="$COOKIE{'pname'}" $STYLE_L></td><td>&nbsp;</td></tr>
		<tr><td align=center><b>PASS</b></td>
		<td><input type=password name="pass" value="$COOKIE{'pass'}" $STYLE_L>
		</td><td>&nbsp;<input type=submit name=lgn value=Login style="height:21px; background:#808080;color:#ffffff; font-size:15px;">
		</td></tr></form></table>
	</td></tr></table>

	<table width=100% height=100% id="data" style="position:absolute;visibility:hidden;"><tr><td align=center>
		<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:16px;">
		<tr><td style="background-color:$TABLE_COLOR2;" colspan=2>
		&nbsp;Data</td>
		<td style="background-color:$TABLE_COLOR2;" align=right><a href="Javascript:hidedata();"><b>×</b></a></td></tr>
		<tr><td><a href="$MAIN_SCRIPT?PASSCHAN2" target="_top" style="font-size:20px;"><b>PassChange</b></a></td>
			<td></td><td>&nbsp;</td></tr>
		<tr><td><a href="$MAIN_SCRIPT?DELETE2" target="_top" style="font-size:20px;"><b>DataDelete</b></a></td>
			<td></td><td>&nbsp;</td></tr>
	-----END-----
	print << "	-----END-----"if $SATELLITE_FLAG;
		<tr><td><a href="$MAIN_SCRIPT?EXPORT" target="_top" style="font-size:20px;"><b>DataExport</b></a></td>
			<td></td><td>&nbsp;</td></tr>
		<tr><td><a href="$MAIN_SCRIPT?INPORT" target="_top" style="font-size:20px;"><b>DataImport</b></a></td>
			<td></td><td>&nbsp;</td></tr>
	-----END-----
	print << "	-----END-----";
		</table>
	</td></tr></table>

	<table border=0 width=100% height=100%>
	<tr><td background="$IMG_FOLDER1/vatitle.gif">
	<div style="text-align:center;">
	<div class="title" style="margin-left:auto;margin-right:auto;text-align:left;width:130px;">
	-----END-----
		$js1="";
		if (!$COOKIE{'pname'} && !$COOKIE{'pass'}){
		print "<br><br><img src=\"$IMG_FOLDER1/stb.gif\" align=\"middle\" name=m1>&nbsp;<a href=\"$MAIN_SCRIPT?ENTRY\" target=\"_top\" onMouseOver=\"document.m1.src='$IMG_FOLDER1/sta.gif'\" align=\"middle\" onMouseOut=\"document.m1.src='$IMG_FOLDER1/stb.gif'\" style=\"font-size:13px;\"><img src=\"$IMG_FOLDER1/sa.gif\" align=\"middle\" border=\"0\">NEW GAME</a><br>";
		}else{
		print "<br><br><br>";
		}
		print "<img src=\"$IMG_FOLDER1/stb.gif\" align=\"middle\" name=m2>&nbsp;<a href=\"Javascript:showform();\" onMouseOver=\"document.m2.src='$IMG_FOLDER1/sta.gif'\" align=\"middle\" onMouseOut=\"document.m2.src='$IMG_FOLDER1/stb.gif'\" style=\"font-size:13px;\"><img src=\"$IMG_FOLDER1/sa.gif\" align=\"middle\" border=\"0\">CONTINUE</a><br>";
		print "<img src=\"$IMG_FOLDER1/stb.gif\" align=\"middle\" name=m3>&nbsp;<a href=\"$YOUR_RULES\" target=_blank onMouseOver=\"document.m3.src='$IMG_FOLDER1/sta.gif'\" align=\"middle\" onMouseOut=\"document.m3.src='$IMG_FOLDER1/stb.gif'\" style=\"font-size:13px;\"><img src=\"$IMG_FOLDER1/sa.gif\" align=\"middle\" border=\"0\">TUTORIAL</a><br>";
		print "<img src=\"$IMG_FOLDER1/stb.gif\" align=\"middle\" name=m4>&nbsp;<a href=\"Javascript:showdata();\" onMouseOver=\"document.m4.src='$IMG_FOLDER1/sta.gif'\" align=\"middle\" onMouseOut=\"document.m4.src='$IMG_FOLDER1/stb.gif'\" style=\"font-size:13px;\"><img src=\"$IMG_FOLDER1/sa.gif\" align=\"middle\" border=\"0\">TURBO FILE</a><br>";
		print "<img src=\"$IMG_FOLDER1/stb.gif\" align=\"middle\" name=m5>&nbsp;<a href=\"$YOUR_HOME\" target=_blank onMouseOver=\"document.m5.src='$IMG_FOLDER1/sta.gif'\" align=\"middle\" onMouseOut=\"document.m5.src='$IMG_FOLDER1/stb.gif'\" style=\"font-size:13px;\"><img src=\"$IMG_FOLDER1/sa.gif\" align=\"middle\" border=\"0\">HOME</a>";
	print << "	-----END-----";	
	</div>
</div>
	<p><div align=center style="font-size:18px;font-family:'細明朝体','ＭＳ Ｐ明朝';color:#ffffff;">The Endless Battle Program Satellite</div>
	<div align=center style="color:#a0a0a0;font-size:12px;">Copyright
	<a href="http://www.endlessbattle.net/" target=_blank style="font-size:12px;text-decoration:none;font-family:osaka;color:#a0a0a0;"> NET GAME Communications</font></a> All Right Reserved.</div></p>
	-----END-----

	print "<div align=right><a href=\"$MAIN_SCRIPT?MAINTE\" target=_blank>$VER</a></div>";
	print "</td></tr></table></body></html>";

	print "<script language=\"JavaScript\">location.href='#top';\n</script>\n" if $BANNER_DISPLAY;

}
sub LOG01{
	&HEADER;
&DBM_INPORT(P);
$timer = "20"; #参加者表示の時間

$COUNT=0;
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
if ( $VALS[26] >= time-$timer*60){$COUNT++;}
}

if ($CONFIG_DISPLAY){
print "<table bgcolor=$TABLE_COLOR1 style=\"border:1px solid #ffffff;font-size:15px;\">";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2 colspan=6>Site DATA</td></tr>";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>管理人</td><td nowrap>$OWNER_NAME</td>" if $OWNER_NAME && !$OWNER_EMAIL;
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>管理人</td><td nowrap><a href=\"mailto:$OWNER_EMAIL?subject=EBSについて\">$OWNER_NAME</a></td></tr>" if $OWNER_NAME && $OWNER_EMAIL;
print "<td nowrap bgcolor=$TABLE_COLOR2>ON人数</td><td nowrap align=right><b>$COUNT人</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>最大登録人数</td><td nowrap align=right><b>無限</b></td></tr>";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>アイコン数</td><td align=right><b>$ICON";
print "+α" if $SPECIAL_ICON;print "</b></td>";
dbmopen (%P,"$DBM_P",0666);	@ENTRy=keys %P;	dbmclose %P;
dbmopen (%C,"$DBM_C",0666);	@COUNTRy=keys %C;dbmclose %C;
$ENTRYS=@ENTRy;
$GENKOKU=@COUNTRy;
print "<td nowrap bgcolor=$TABLE_COLOR2>Cookie保持期間</td><td nowrap align=right><b>$COOKIE_KEEP日</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>現戦闘中人数</td><td nowrap align=right><b>$ENTRYS人</b></td>";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>HP回復</td><td nowrap align=right><b>$HP_REPAIR2+$HP_REPAIR％/秒</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>放置交代時間</td><td nowrap align=right><b>$COOKIE_KEEP3分</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>最大同時戦闘人数</td><td nowrap align=right><b>$ENTRY_MAX人</b></td></tr>";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>$STATUS_NAME[5]回復</td><td nowrap align=right><b>$EN_REPAIR/秒</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>現国数</td><td nowrap align=right><b>$GENKOKU国</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>建国費</td><td nowrap align=right><b>\$$MAKE_COUNTRY</b></td></tr>";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>RISK回復</td><td nowrap align=right><b>$RISK_REPAIR/秒</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>最大国数</td><td nowrap align=right><b>$COUNTRY_MAX国</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>部隊結成費</td><td nowrap align=right><b>\$$MAKE_TEAM</b></td></tr>";
print "<tr><td nowrap bgcolor=$TABLE_COLOR2>要塞回復</td><td nowrap align=right><b>$YO_REPAIR/秒</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>削除期限</td><td nowrap align=right><b>無し</b></td>";
print "<td nowrap bgcolor=$TABLE_COLOR2>データ移行</td><td nowrap align=right><b>";
print "許可" if $SATELLITE_FLAG;print "禁止" if !$SATELLITE_FLAG;print "</b></td></tr>";
print "</table>";
}


	print "$COMMENT_2" if $COMMENT_2;
	&FOOTER;
}
sub MY_LIST2{
#	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
#		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
#	@pairs = split(/\,/, $DUMMY{'EB'});
#		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
#	&HEADER;
#	&DBM_INPORT(P);&DBM_INPORT(C);
#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
#	&DBM_CONVERT('C',"$PL_VALUES[5]");

	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}

$CookieValue = $ENV{'HTTP_COOKIE'};
$CookieValue =~ s/\+/ /g;
$CookieValue =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C",hex($1))/eg;

	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$key =~ s/ //g;$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}

#	&ERROR("$ENV{'HTTP_COOKIE'}ああ$DUMMY{'EB'}とと@pairsええ$COOKIE{'pname'}");

#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&HEADER;


	&DBM_INPORT(P);&DBM_INPORT(C);
#	&ERROR("$FORM{pname}");

#&ERROR("$COOKIE{'pname'}と$ENV{'HTTP_COOKIE'}");

	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
#	@PL_VALUES = split(/\s/,$P{"$DUMMY{'EB'}"});
#	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
#	&DBM_CONVERT('P',"$FORM{pname}");
#	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});

	&DBM_CONVERT('C',"$PL_VALUES[5]");

	sub TR {
	$VALUES[7]='No-Comment'if !$VALUES[7];
	"<tr><td nowrap style=\"color:$VALUES[13];\">$Key</td><td>".&RANK("$VALUES[0]","$VALUES[5]","$VALUES[6]")."</td><td><img src=$IMG_FOLDER2/$VALUES[27].gif width=32 height=32></td><td style=\"color:$VALUES[13];\">$VALUES[7]</td><td style=\"color:$VALUES[13];\">".(&LOGIN_CHECK($Key) ? "<font color=#dc143c>参戦中</font>":"<font color=#143dca>休戦中</font>")
	}

	@CC=split(/!/,$CL_VALUES[46]);
	$el="";$el1="";$el2="";$el3="";
	if($CC[1] > time){

		if($CC[0] eq "1"){$el = "d0";}
		if($CC[0] eq "2"){$el = "d1";}
		if($CC[0] eq "3"){$el = "d2";}
		if($CC[0] eq "4"){$el = "d3";}

	}
	if($CC[3] > time){

		if($CC[2] eq "1"){$el1 = "d0";}
		if($CC[2] eq "2"){$el1 = "d1";}
		if($CC[2] eq "3"){$el1 = "d2";}
		if($CC[2] eq "4"){$el1 = "d3";}

	}
	if($CC[5] > time){

		if($CC[4] eq "1"){$el2 = "d0";}
		if($CC[4] eq "2"){$el2 = "d1";}
		if($CC[4] eq "3"){$el2 = "d2";}
		if($CC[4] eq "4"){$el2 = "d3";}

	}
	if($CC[7] > time){

		if($CC[6] eq "1"){$el3 = "d0";}
		if($CC[6] eq "2"){$el3 = "d1";}
		if($CC[6] eq "3"){$el3 = "d2";}
		if($CC[6] eq "4"){$el3 = "d3";}

	}

	print "<table border=1 cellspacing=1 cellpadding=1 bordercolor=#484848 style=\"font-size:15px;background:black;border:2px solid $CL_VALUES[0];\">";
	print "<tr><td colspan=5 bgcolor=$CL_VALUES[0]>";
	if($PL_VALUES[5]){
	print "<table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:35px;\"><tr><td>$PL_VALUES[5]";
	if($el eq ""){
	print "<span style=\"font-size:15px;\">&nbsp;&nbsp;&nbsp;&nbsp;国費&nbsp;<b>$CL_VALUES[1]</b>&nbsp;&nbsp;滅ぼした国&nbsp;";
	}else{
	print "<span style=\"font-size:15px;\">&nbsp;&nbsp;<img src=\"$IMG_FOLDER1/$el.gif\">&nbsp;&nbsp;国費&nbsp;<b>$CL_VALUES[1]</b>&nbsp;&nbsp;滅ぼした国&nbsp;";
	}
	$DECLT=int($CL_VALUES[13]/10);$DECL=$CL_VALUES[13]-$DECLT*10;
	for ($h=1;$h<=$DECLT;$h++){print "<img src=\"$IMG_FOLDER4/1000.gif\" width=\"32\" height=\"32\">";}
	for ($h=1;$h<=$DECL;$h++){print "<img src=\"$IMG_FOLDER4/1000.gif\" width=\"16\" height=\"16\">";}
	while (($C_Name,$C_Value) =each %C) {
		@C_VALUE2 = split(/\s/,$C_Value);
		push (@VS_COUNTRY,$C_Name) if (($C_VALUE2[6] eq $PL_VALUES[5] || $C_VALUE2[8] eq $PL_VALUES[5] || $C_VALUE2[9] eq $PL_VALUES[5] || $C_VALUE2[10] eq $PL_VALUES[5]) && $C_VALUE2[7] > time);
	}


	if(@VS_COUNTRY){
	$op="<br>&nbsp;&nbsp;現在、";
	foreach (@VS_COUNTRY) {$op.= "【$_】";}
	$op.="から侵攻を受けています。";
	}
	print "$op</span></td></tr></table>";
	}
	print "</td></tr>";
	foreach $Key (sort {$P{$b} <=> $P{$a}} keys %P){
		@VALUES = split(/\s/,$P{$Key});

#		if($PL_VALUES[39] == $VALUES[39]){
			if (!$PL_VALUES[5] && !$VALUES[5]){print &TR;}
			if ($PL_VALUES[5] && $PL_VALUES[5] eq $VALUES[5] && !$VALUES[28] && ($VALUES[6] == 1 || $VALUES[6] == 0)){print &TR;}
			if ($PL_VALUES[5] && $PL_VALUES[5] eq $VALUES[5] && $VALUES[28]){
				($UNIT_A.= &TR,$uflag_A=1) if $VALUES[28] eq $CL_VALUES[2] && $VALUES[6] != -1;
				($UNIT_B.= &TR,$uflag_B=1) if $VALUES[28] eq $CL_VALUES[3] && $VALUES[6] != -1;
				($UNIT_C.= &TR,$uflag_C=1) if $VALUES[28] eq $CL_VALUES[4] && $VALUES[6] != -1;
				($LEADER_A.= &TR,$lflag_A=1) if $VALUES[28] eq $CL_VALUES[2] && $VALUES[6] == -1;
				($LEADER_B.= &TR,$lflag_B=1) if $VALUES[28] eq $CL_VALUES[3] && $VALUES[6] == -1;
				($LEADER_C.= &TR,$lflag_C=1) if $VALUES[28] eq $CL_VALUES[4] && $VALUES[6] == -1;
			}
#		}
		$plys++;
	}
	if ($PL_VALUES[5]){
	print "<tr><td colspan=5 bgcolor=$CL_VALUES[0]><table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:25px;\">";
	if($el1 eq ""){
		print "<tr><td>&nbsp;<b>第一部隊</b>&nbsp;";
	}else{
		print "<tr><td>&nbsp;<b>第一部隊</b>&nbsp;<img src=\"$IMG_FOLDER1/$el1.gif\">&nbsp;";
	}

	print $CL_VALUES[2] ? "$CL_VALUES[2]</td></tr></table>":!$CL_VALUES[2] ? '未結成</td></tr></table>':'</td></tr></table></td></tr>';
	print $lflag_A ? "$LEADER_A":!$lflag_A ? "<tr><td colspan=6>隊長不在</td></tr>":'\n';
	print $uflag_A ? "$UNIT_A":!$uflag_A ? "<tr><td colspan=6>NoPlayer</td></tr>":'';
	print "<tr><td colspan=5 bgcolor=$CL_VALUES[0]><table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:25px;\">";
	if($el2 eq ""){
		print "<tr><td>&nbsp;<b>第二部隊</b>&nbsp;";
	}else{
		print "<tr><td>&nbsp;<b>第二部隊</b>&nbsp;<img src=\"$IMG_FOLDER1/$el2.gif\">&nbsp;";
	}

	print $CL_VALUES[3] ? "$CL_VALUES[3]</td></tr></table>":!$CL_VALUES[3] ? '未結成</td></tr></table>':'</td></tr></table></td></tr>';
	print $lflag_B ? "$LEADER_B":!$lflag_B ? "<tr><td colspan=6>隊長不在</td></tr>":'\n';
	print $uflag_B ? "$UNIT_B":!$uflag_B ? "<tr><td colspan=6>NoPlayer</td></tr>":'';
	print "<tr><td colspan=5 bgcolor=$CL_VALUES[0]><table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:25px;\">";
	if($el3 eq ""){
		print "<tr><td>&nbsp;<b>第三部隊</b>&nbsp;";
	}else{
		print "<tr><td>&nbsp;<b>第三部隊</b>&nbsp;<img src=\"$IMG_FOLDER1/$el3.gif\">&nbsp;";
	}
	print $CL_VALUES[4] ? "$CL_VALUES[4]</td></tr></table>":!$CL_VALUES[4] ? '未結成</td></tr></table>':'</td></tr></table></td></tr>';
	print $lflag_C ? "$LEADER_C":!$lflag_C ? "<tr><td colspan=6>隊長不在</td></tr>":'\n';
	print $uflag_C ? "$UNIT_C":!$uflag_C ? "<tr><td colspan=6>NoPlayer</td></tr>":'';
	}
	print "</table><br><br><br><br>";

	&FOOTER;

}
sub C_LIST2{
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&DBM_CONVERT('C',"$PL_VALUES[5]");

	&HEADER;
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT method=POST target=Sub onSubmit="">
	<input type=hidden name="cmd" value="CO_LIST">
	<b style=\"font-size:13px;\">どの国の情報を見ますか？</b><br>
	<b style="font-size:13px;">天宮シャングリラ</b><br>
	-----END-----
#	<b style="font-size:13px;">$CONTINENT_A</b><br>

		while (($C_Name,$C_Value) =each %C) {
			@C_VALUES = split(/\s/,$C_Value);

				@C_VALUE = split(/\s/,$C_Value);
#					print "<input type=hidden name=con2 value=1>";
					print "<input type=submit name=CNTRY value=\"$C_Name\"";
					print "onClick=\"\" STYLE=\" background:$C_VALUE[0];color:black\">\n";

		}
#		print "<input type=hidden name=con2 value=1>";
		print "<input type=submit name=CNTRY value=\"$NONE_NATIONALITY\"";
		print "onClick=\"\" STYLE=\" background:#808080;color:white\"></form>\n";
#ゼテギネア大陸
#		while (($C_Name,$C_Value) =each %C) {
#			@C_VALUES = split(/\s/,$C_Value);
#
#			if ($C_VALUES[39] eq "1"){
#				@C_VALUE = split(/\s/,$C_Value);
#					print "<input type=hidden name=con2 value=1>";
#					print "<input type=submit name=CNTRY value=\"$C_Name\"";
#					print "onClick=\"\" STYLE=\" background:$C_VALUE[0];color:black\">\n";
#			}

#		}
#		print "<input type=hidden name=con2 value=1>";
#		print "<input type=submit name=CNTRY value=\"$NONE_NATIONALITY\"";
#		print "onClick=\"\" STYLE=\" background:#808080;color:white\"></form>\n";
	
#ガリシア大陸
#		print "<b style=\"font-size:13px;\">$CONTINENT_B</b><br>";
#		while (($C_Name,$C_Value) =each %C) {
#			@C_VALUES = split(/\s/,$C_Value);

#			if ($C_VALUES[39] eq "2"){
#				@C_VALUE = split(/\s/,$C_Value);
#					print "<input type=hidden name=con2 value=2>";
#					print "<input type=submit name=CNTRY value=\"$C_Name\"";
#					print "onClick=\"\" STYLE=\" background:$C_VALUE[0];color:black\">\n";
#			}

#		}
#		print "<input type=hidden name=con2 value=2>";
#		print "<input type=submit name=CNTRY value=\"$NONE_NATIONALITY\"";
#		print "onClick=\"\" STYLE=\" background:#808080;color:white\"></form>\n";


}
sub ICON_LIST{
&HEADER;$c=$FORM{'start'};
print "<table width=100% height=100%><tr><td align=center><div style=\"font-size:35px;\">EB-S アイコン一覧</div><table bgcolor=#000000 cellpadding=4 cellspacing=4 style=\"border:1px solid #808080;\">";
foreach($FORM{'start'}..$ICON){$c++;
print "<tr>" if $c%10==1;
print "<td><img src=$IMG_FOLDER2/$_.gif><div align=center style=\"font-size:10px;\">No.$_</div></td>";
print "</tr>" if $c%10==0;
last if $c>=$FORM{'start'}+50;
}
print "</table><table><tr>";
$Next=$FORM{'start'}+50;
$Back=$FORM{'start'}-50;

print << "-----END-----" if $Back >= 0;
<td><form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name=cmd value="ICON">
<input type=hidden name=start value="$Back">
<input type="submit" value="<<">
</form></td>
-----END-----

print << "-----END-----" if $Next <= $ICON;
<td><form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name=cmd value="ICON">
<input type=hidden name=start value="$Next">
<input type="submit" value=">>">
</form></td>
-----END-----
print "</tr></table>";
&FOOTER;
print "</td></tr></table>";

}

1;


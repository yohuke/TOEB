sub CUSTOM_HEADER {
	$BgColor="bgcolor=\"$TABLE_COLOR1\"";
	&HEADER;
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT method=POST name=Ms target="$_[0]" onSubmit='window.location.replace("$BACKFR");'>
		<input type=hidden name=cmd value=CUSTOM>
		<input type=hidden name=CustomCheck value=$Date>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
	<table bordercolor=\"$TABLE_BORDER\" border=1 cellspacing=0 style="font-size:10pt;">
		<tr><td bgcolor=\"$TABLE_COLOR2\"><b>$FORM{'custom'}</b></td></tr>
	-----END-----
}
sub HISTORY {
	&CUSTOM_HEADER('Main');
	$c=0;
	dbmopen (%NOTE,"$DBM_H",0666);
		foreach $Key (sort {$b <=> $a} keys %NOTE){$c++;
#			if ($c <= $HISTORY_MAX && $Key <= time && "$NOTE{$Key}" ne '黒歴史'){
			if ($c <= $HISTORY_MAX && $Key <= time){
				print "<tr><td $BgColor><b>".&DATE_DECORD($Key)."</b>&nbsp;&nbsp;$NOTE{$Key}</td></tr>\n";
			}elsif($c > $HISTORY_MAX){
				delete $NOTE{$Key};
			}
		}
	dbmclose %NOTE;
	print "</table>\n";
	&FOOTER;
}
sub COMMENT {
	&CUSTOM_HEADER('Sub');
	print << "	-----END-----";
		<script language="JavaScript">
		function checkComment (){
			if(document.Ms.com.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
				window.alert("だーめっ！");return false ;
			}else{	if (confirm('コメントを変更します。よろしいですか？') == true){return true;}else{return false}	}
		}
		</script>
		<tr><td $BgColor><b>コメント変更</b><br>
		&nbsp;&nbsp;<input type="text" name="com" size="70" maxlength="50" value="" $STYLE_L><br>
		&nbsp;&nbsp;<span style="font-size:13px;">コメント入力後、必ず「変更」ボタンをクリックして下さい。
		Enterボタンでは反映されません。</span><br><input type="hidden" name="Cflag" value="ON">
		&nbsp;&nbsp;<input name="Cmode" type="submit" value="変更" onClick=\"return checkComment()\">
		&nbsp;&nbsp;<input type="reset" value="クリア"></td></tr></form></table>
	-----END-----
	&FOOTER;
}
sub SPECIAL{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	&CUSTOM_HEADER('Sub');

	require "./$LOG_FOLDER/$CLASS_DATA";
	@ALY_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

	print "<tr><td $BgColor><br>";
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"建国\" onClick=\"document.Ms.cmd.value='MAKE_C';\">" if $PL_VALUES[8] > $MAKE_COUNTRY && !$PL_VALUES[6];
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"戦略\" onClick=\"document.Ms.cmd.value='MISSION';\">" if $PL_VALUES[6] != 0 && $PL_VALUES[5] && $CL_VALUES[37] < time;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"部隊\" onClick=\"document.Ms.cmd.value='MAKE_T';\">"if $PL_VALUES[5];
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"要塞強化\" onClick=\"document.Ms.cmd.value='BOSS';\">" if ($PL_VALUES[6] != 0 || $COOKIE{'pass'} eq $MASTERPASS) && $PL_VALUES[5];
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"全体補助\" onClick=\"document.Ms.cmd.value='DEFM';\">" if $ALY_CLASS[17] =~m/!E001|!E006a|!E006b|!E006c|!E006d|!8i|!8j/;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"タロットカード\" onClick=\"document.Ms.cmd.value='CARD';\">" if ($PL_VALUES[6] != 0 && (($PL_VALUES[5] && $CL_VALUES[15] && $CL_VALUES[7] > time) || ($WW_FRAG==1 && $HIZUK_FRAG==1))) || $MENTE==1;
#	$sp.= "<input name=\"custom\" type=\"submit\" value=\"タロットカード\" onClick=\"hide();document.Ms.cmd.value='CARD';\">" if $PL_VALUES[6] != 0 && $PL_VALUES[5] && $CL_VALUES[15] && $CL_VALUES[7] > time || $MENTE==1;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"おまけ\" onClick=\"document.Ms.cmd.value='CHICON';\">" if $PL_VALUES[16] >= 80000 && $PL_VALUES[18] >= 4000;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"アイコンチェンジ！\" onClick=\"document.Ms.cmd.value='ICONEX';\">" if $PL_VALUES[8] >= 200000;
	$sp.= "<input type=\"submit\" value=\"装備図鑑\" $STYLE_B1 onClick=\"document.Ms.cmd.value='ZUKAN';\">";

	$sp.= "<input name=\"custom\" type=\"submit\" value=\"武器強化\" onClick=\"document.Ms.cmd.value='WEAPONFORCE';\">" if $WeaponReinForcement == 1;
	
#	$sp='実行できるコマンドがありません。' if !$sp;
#$WW_FRAG==1 && $HIZUK_FRAG==1
	print "&nbsp;&nbsp;$sp&nbsp;&nbsp;<br><br></td></tr></form></table>";
	&FOOTER;
}
sub WEAPONFORCE2{

	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	&CUSTOM_HEADER('Main');

	require "./$LOG_FOLDER/$HASH_DATA";
	require "./$LOG_FOLDER/$WEAPONRAIN_DATA";
	local($WN_A,$WLV_A,$WLV_AEn1,$WLV_AEn2,$WLV_AEn3,$WLV_AEn4,$WLV_AEn5) = split(/!/,$PL_VALUES[9]);

	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
	@WN_sAEn1=split(/\,/,$WEAPONRAINFORCEMENT_LIST{"$WLV_AEn1"});
	@WN_sAEn2=split(/\,/,$WEAPONRAINFORCEMENT_LIST{"$WLV_AEn2"});
	@WN_sAEn3=split(/\,/,$WEAPONRAINFORCEMENT_LIST{"$WLV_AEn3"});
	@WN_sAEn4=split(/\,/,$WEAPONRAINFORCEMENT_LIST{"$WLV_AEn4"});
	@WN_sAEn5=split(/\,/,$WEAPONRAINFORCEMENT_LIST{"$WLV_AEn5"});

##インポート
	&DBM_INPORT(P);&DBM_INPORT(C);
	print "<tr><td $BgColor>";


print<<"-----END-----";

<table style="font-size:10pt;margin-left:8px;margin-right:8px;">
<tr><td colspan=3><b>最上段にセットしている装備名：$WN_sA[0]</b></td></tr>
<tr>
<td colspan=2><input type=hidden name=yousaiCheck value=$DATE><b><span style="font-size:20px;">HP</span> $Y_HP[0]/$Y_HP[1]</b></td>
-----END-----
	#最大と最小回数を取得　両手･･･5　片手･･･4　杖・扇･･･3
	$Pl_MinCount = 0;$Pl_MaxCount = 0;
	#最小回数取得
	if($WN_sAEn1){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn2){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn3){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn4){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn5){$Pl_MinCount = $Pl_MinCount + 1;}

	#最大回数取得
	#両手武器
	if($WN_sA[7] =~ m/11/){$Pl_MinCount=5;}
	#片手武器
	elsif($WN_sA[7] =~ m/10/){$Pl_MinCount=4;}
	
	$YO_HP=int($Y_HP[1]*0.3)-37000;
	print "<td>";
	print "<br>$WN_sAEn1[0]";
	print "</td>";

	$YO_STR=int($Y_ST[0]*400)+9600;
	$YO_VIT=int($Y_ST[1]*400)+9600;
	$YO_AGI=int($Y_ST[2]*400)+9600;

	print "</tr><tr><td style=\"width:50px;\"><b>攻撃力</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[0]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"攻撃力強化\" onClick=\"return ChMn('攻撃力を強化','$YO_STR')\"></td>" if $Y_ST[0] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>防御力</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[1]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"防御力強化\" onClick=\"return ChMn('防御力を強化','$YO_VIT')\"></td>" if $Y_ST[1] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>命中力</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[2]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"命中力強化\" onClick=\"return ChMn('命中力を強化','$YO_AGI')\"></td>" if $Y_ST[2] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</td></tr></table></form>\n";
	&FOOTER;

}
sub BOSS2{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	if(($PL_VALUES[6]==0 || !$PL_VALUES[5] || !@CL_VALUES) && $COOKIE{'pass'} ne $MASTERPASS){
	require "makeserifu.data";
		my$sl=@serifu;
		my$sw=@serifu[int(rand($sl))];
		&ERROR("$FORM{pname}$sw");
	}
	&CUSTOM_HEADER('Main');

	require "./$LOG_FOLDER/$HASH_DATA";
#	local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
	local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
	local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
	local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);

#	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
	@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});


##インポート
	&DBM_INPORT(P);&DBM_INPORT(C);
##総帥指揮レベル読み込み・国民数読み込み
	while (my($key,$val) = each %P){
	@VALS = split(/\s/,$val);
		if($VALS[5] eq $PL_VALUES[5]){
			if($VALS[6] == 1){
				$SOUSUISIKI=$VALS[32];
			}
		}
	}
##総帥指揮反映時、101以上なら100にする
	$SOUSUISIKI=100 if $SOUSUISIKI > 100;
	$VSMETUCHECK=$CL_VALUES[13] if $CL_VALUES[13];
	$VSMETUCHECK=50 if $VSMETUCHECK > 50;
	$SOUSUISIKI=int($SOUSUISIKI/4)+$VSMETUCHECK;

	print "<tr><td $BgColor>";

	@Y_HP=split(/!/,$CL_VALUES[11]);
	$Y_HP[0]=$Y_HP[0]+(time-$Y_HP[2])*$YO_REPAIR;$Y_HP[0]=$Y_HP[1] if $Y_HP[0] > $Y_HP[1];
	@Y_ST=split(/!/,$CL_VALUES[12]);

print<<"-----END-----";

<table style="font-size:10pt;margin-left:8px;margin-right:8px;">
<tr><td colspan=3><b>国費：$CL_VALUES[1]</b></td></tr>
<tr>
<td colspan=2><input type=hidden name=yousaiCheck value=$DATE><b><span style="font-size:20px;">HP</span> $Y_HP[0]/$Y_HP[1]</b></td>
-----END-----
	$YO_HP=int($Y_HP[1]*0.3)-37000;
	print "<td>";
	if ($Y_HP[0] < $Y_HP[1]){
		print "<input name=\"Cmode\" type=\"submit\" value=\"回復小\" onClick=\"return ChMn('HPを回復（小）','6000')\">";
		print "<input name=\"Cmode\" type=\"submit\" value=\"回復大\" onClick=\"return ChMn('HPを回復（大）','30000')\">";
	}
	print "<input name=\"Cmode\" type=\"submit\" value=\"HP強化\" onClick=\"return ChMn('HPを強化','$YO_HP')\">" if $Y_HP[1] < $YOUSAI_MAX_HP && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));
	print "</td>";

	$YO_STR=int($Y_ST[0]*400)+9600;
	$YO_VIT=int($Y_ST[1]*400)+9600;
	$YO_AGI=int($Y_ST[2]*400)+9600;

	print "</tr><tr><td style=\"width:50px;\"><b>攻撃力</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[0]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"攻撃力強化\" onClick=\"return ChMn('攻撃力を強化','$YO_STR')\"></td>" if $Y_ST[0] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>防御力</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[1]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"防御力強化\" onClick=\"return ChMn('防御力を強化','$YO_VIT')\"></td>" if $Y_ST[1] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>命中力</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[2]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"命中力強化\" onClick=\"return ChMn('命中力を強化','$YO_AGI')\"></td>" if $Y_ST[2] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	$Zoksen="<select size=1 name=\"Zsentaku\" $STYLE_L>\n";
	$Zoksen .= "<option value=7 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "";
	$Zoksen .= ">無属性</option>";
	$Zoksen .= "<option value=0 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "0";
	$Zoksen .= ">風属性</option>";
	$Zoksen .= "<option value=1 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "1";
	$Zoksen .= ">炎属性</option>";
	$Zoksen .= "<option value=2 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "2";
	$Zoksen .= ">大地属性</option>";
	$Zoksen .= "<option value=3 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "3";
	$Zoksen .= ">水属性</option>";
	$Zoksen .= "<option value=4 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "4";
	$Zoksen .= ">神聖属性</option>";
	$Zoksen .= "<option value=5 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "5";
	$Zoksen .= ">暗黒属性</option>";
	$Zoksen .= "</select>";

	print "</tr><tr><td style=\"width:80px;\"><b>武器属性</b></td><td><b style=\"color:#ff0080;\"></b>$Zoksen</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"属性変更\" onClick=\"return ChMn('要塞武器を属性変更','50000')\"></td>" if ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 50000));

#	$a = time;
#	&ERROR("$WN_sB[7]ああ$CL_VALUES[7]いい$CL_VALUES[37]うう$a");

#	if(($WN_sB[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sC[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sD[7] =~ m/!87|!88|!89|!8a|!8b|!8c/) && ($CL_VALUES[7] > time || $CL_VALUES[37] > time)){
	if(($WN_sB[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sC[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sD[7] =~ m/!87|!88|!89|!8a|!8b|!8c/) && ($CL_VALUES[7] > time && $CL_VALUES[45] < time) && $PL_VALUES[6] ne "0" && $PL_VALUES[25] eq "0"){


		$PartofTO.="<option value=10>$CL_VALUES[6]の本隊" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=11>$CL_VALUES[6]の第一部隊" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=12>$CL_VALUES[6]の第二部隊" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=13>$CL_VALUES[6]の第三部隊" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=20>$CL_VALUES[8]の本隊" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=21>$CL_VALUES[8]の第一部隊" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=22>$CL_VALUES[8]の第二部隊" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=23>$CL_VALUES[8]の第三部隊" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=30>$CL_VALUES[9]の本隊" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=31>$CL_VALUES[9]の第一部隊" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=32>$CL_VALUES[9]の第二部隊" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=33>$CL_VALUES[9]の第三部隊" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=40>$CL_VALUES[10]の本隊" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=41>$CL_VALUES[10]の第一部隊" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=42>$CL_VALUES[10]の第二部隊" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=43>$CL_VALUES[10]の第三部隊" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);

		if($WN_sB[7] =~ m/!87/){
			$BO = "サモンイシュタル";
		}elsif($WN_sB[7] =~ m/!88/){
			$BO = "サモンアスモデ";
		}elsif($WN_sB[7] =~ m/!89/){
			$BO = "サモンゾショネル";
		}elsif($WN_sB[7] =~ m/!8a/){
			$BO = "サモングルーザ";
		}elsif($WN_sB[7] =~ m/!8b/){
			$BO = "サモンハーネラ";
		}elsif($WN_sB[7] =~ m/!8c/){
			$BO = "サモンバーサ";
		}

		if($WN_sC[7] =~ m/!87/){
			$CO = "サモンイシュタル";
		}elsif($WN_sC[7] =~ m/!88/){
			$CO = "サモンアスモデ";
		}elsif($WN_sC[7] =~ m/!89/){
			$CO = "サモンゾショネル";
		}elsif($WN_sC[7] =~ m/!8a/){
			$CO = "サモングルーザ";
		}elsif($WN_sC[7] =~ m/!8b/){
			$CO = "サモンハーネラ";
		}elsif($WN_sC[7] =~ m/!8c/){
			$CO = "サモンバーサ";
		}

		if($WN_sD[7] =~ m/!87/){
			$DO = "サモンイシュタル";
		}elsif($WN_sD[7] =~ m/!88/){
			$DO = "サモンアスモデ";
		}elsif($WN_sD[7] =~ m/!89/){
			$DO = "サモンゾショネル";
		}elsif($WN_sD[7] =~ m/!8a/){
			$DO = "サモングルーザ";
		}elsif($WN_sD[7] =~ m/!8b/){
			$DO = "サモンハーネラ";
		}elsif($WN_sD[7] =~ m/!8c/){
			$DO = "サモンバーサ";
		}

		$PartofOA.="<option value=10>$BO" if $WN_sB[7] =~ m/!87|!88|!89|!8a|!8b|!8c/;
		$PartofOA.="<option value=11>$CO" if $WN_sC[7] =~ m/!87|!88|!89|!8a|!8b|!8c/;
		$PartofOA.="<option value=38>$DO" if $WN_sD[7] =~ m/!87|!88|!89|!8a|!8b|!8c/;

		print "<SCRIPT language=\"JavaScript\">\nfunction checkSet (){\n";
		print "if (confirm('オーブを使用しますがよろしいですか？') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><b style=\"vertical-align:middle;\">オーブ解放</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=TSet>$PartofTO</select></tr><tr></td><td style=\"padding-left:20px;\"><select name=OSet>$PartofOA</select><input type=submit name=Cmode value=解放 onClick=\"return checkSet()\"></td></tr></table>\n";

		print "</td></tr>";
	
	}

	print << "	-----END-----" if ($CL_VALUES[1] >= $NAME_YOSAI && $PL_VALUES[6] == 1);
		</tr><tr><td colspan=3>要塞の名前 <input type=text name="yoname" size=25 maxlength=20 value="$Y_ST[3]" $STYLE_L></td></tr>
		<tr><td colspan=3><input name="Cmode" type=submit value="要塞改名" onClick="return checkYosai()"></td></tr>
	-----END-----

		&DBM_INPORT(C);

		$M_AITEX0="$CL_VALUES[6]";
		$M_AITEX1="$CL_VALUES[8]";
		$M_AITEX2="$CL_VALUES[9]";
		$M_AITEX3="$CL_VALUES[10]";

		$Teisen.="<option value=1>$CL_VALUES[6]" if $C{"$CL_VALUES[6]"} && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time;
		$Teisen.="<option value=2>$CL_VALUES[8]" if $C{"$CL_VALUES[8]"} && $CL_VALUES[6] ne $CL_VALUES[8] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time;
		$Teisen.="<option value=3>$CL_VALUES[9]" if $C{"$CL_VALUES[9]"} && $CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time;
		$Teisen.="<option value=4>$CL_VALUES[10]" if $C{"$CL_VALUES[10]"} && $CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time;

		print "<SCRIPT language=\"JavaScript\">\nfunction checkTeisen (){\n";
		print "if (confirm('停戦します。よろしいですか？　(※自国の停戦処理を行います。)') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor>";

		print "</td></tr>";
		if ($CL_VALUES[7] > time){
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td colspan=3><b>停戦 </b></td><td style=\"padding-left:20px;\"><select name=TeiSet>$Teisen</select></td><td style=\"padding-left:20px;\"><input type=submit name=Cmode value=停戦宣言 onClick=\"return checkTeisen()\"></td></tr></table>\n";
#			print "</td></tr>";
		}

#		<tr><td colspan=3><input name="Cmode" type=submit value="停戦" onClick="return checkTeisen()"></td>

	print "</tr></table>";

	print << "	-----END-----";
	<script language="JavaScript">
		function ChMn(msg,mny){
			if (mny > $CL_VALUES[1]){alert('資金が足りません。');return false;}
			if (confirm(msg+'します。\\n費用('+mny+')\\nよろしいですか？') == true){
				return true;}else{return false;}
		}
		function checkYosai(){
			if (document.Ms.yoname.value == ''){window.alert("要塞名が記入されていません。");return false;
			}else if(document.Ms.yoname.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
				window.alert("だーめっ！");return false;
			}else if (confirm('要塞名を変更します。費用(10000)よろしいですか') == true){return true;
			}else{return false}
		}
		function checkTeisen(){
			if (confirm('停戦します。よろしいですか？　(※自国の停戦処理を行います。)') == true){return true;
			}else{return false}
		}
	</script>
	-----END-----

	print "</td></tr></table></form>\n";
	&FOOTER;
}
sub MAHOU2{
#'
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	&ERROR if $PL_VALUES[6]==0 || !$PL_VALUES[5] || !@CL_VALUES;
	&CUSTOM_HEADER('Main');
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&DBM_CONVERT('C',"$PL_VALUES[5]");
	sub FR {"<option value=\"$Key\">$Key"}
	print << "	-----END-----";
	<script language="JavaScript">
		function checkmahou(anti1,anti2){
			if (anti2 > $CL_VALUES[1]){alert('国費が足りません。');return false;}
			if (confirm(anti1+'を使用します。\\n費用（'+anti2+'）\\nよろしいですか？') == true)
			{return true;}else{return false}
		}
	</script>
		<tr><td $BgColor><b>国費：\$ $CL_VALUES[1]</b><br><br><b>ヒーリング・ヒーリングオール・リザレクション・パラダイム使用時<br>
		対象を選択して下さい。他の補助魔法を使う場合は未選択で構\いません</b><br>
			&nbsp;&nbsp;&nbsp;&nbsp;
	-----END-----
print "<input type=hidden name=mahouCheck value=$DATE>";
	print "<select name=\"arisite\">";
	foreach $Key (sort {$P{$b} <=> $P{$a}} keys %P){
		@VALUES = split(/\s/,$P{$Key});
		if ($PL_VALUES[5] eq $VALUES[5] && $Key ne $FORM{'pname'}){print &FR;}
		$plys++;
	}
	print "</select>";
	print << "	-----END-----";
</td></tr>
		<tr><td $BgColor><b>ヒーリング：対象国民のHPを30％回復、回復中だと無効</b><br>
			&nbsp;&nbsp;\$2000<input name="Dmode" type=submit value="ヒーリング使用" onClick="return checkmahou('ヒーリング','2000')"></td></tr>
		<tr><td $BgColor><b>ヒーリングプラス：出撃可になっている国民のHPを30％回復</b><br>
			&nbsp;&nbsp;\$15000<input name="Dmode" type=submit value="ヒーリングプラス使用" onClick="return checkmahou('ヒーリングプラス','15000')"></td></tr>
		<tr><td $BgColor><b>ヒーリングオール：対象国民のHPを全回復、回復中だと無効</b><br>
			&nbsp;&nbsp;\$5000<input name="Dmode" type=submit value="ヒーリングオール使用" onClick="return checkmahou('ヒーリングオール','4000')"></td></tr>
		<tr><td $BgColor><b>リザレクション：回復中になっている対象国民をHP全回復出撃可</b><br>
			&nbsp;&nbsp;\$10000<input name="Dmode" type=submit value="リザレクション使用" onClick="return checkmahou('リザレクション','10000')"></td></tr>
		<tr><td $BgColor><b>チャージスペル：少尉未満MP+1000</b><br>
			&nbsp;&nbsp;\$50000<input name="Dmode" type=submit value="チャージスペル使用" onClick="return checkmahou('チャージスペル','50000')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] == 1);
		<tr><td $BgColor><b>マーティライズ：回復中になっている国民を現在HPそのままで出撃可にします<br>
		発動権限は総帥のみ</b><br>
			&nbsp;&nbsp;\$80000<input name="Dmode" type=submit value="マーティライズ使用" onClick="return checkmahou('マーティライズ','80000')"></td></tr>
	-----END-----
	print "</td></tr></table></form>\n";
	&FOOTER;

}
sub TAROT{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	if($PL_VALUES[6]==0 || !$PL_VALUES[5] || !@CL_VALUES){
		require "makeserifu.data";
			my$sl=@serifu;
			my$sw=@serifu[int(rand($sl))];
		&ERROR("$FORM{pname}$sw");
	}
	&CUSTOM_HEADER('Main');
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&DBM_CONVERT('C',"$PL_VALUES[5]");
#6 8 9 10
	while (my($key,$val) =each %C) {
		@CN_VALS = split(/\s/,$val);$CN_VALS[7];
		if ($PL_VALUES[5] ne "$key" && ($WW_FRAG==1 && $HIZUK_FRAG==1)){
			$op.= "<option value=\"$key\">$key\n";
#			if($CL_VALUES[6] eq "$key" || $CL_VALUES[8] eq "$key" || $CL_VALUES[9] eq "$key" || $CL_VALUES[10] eq "$key"){
#				$op.= "<option value=\"$key\">$key\n";
#			}
		}elsif ($PL_VALUES[5] ne "$key" && ($CN_VALS[6] || $CN_VALS[7] < time)){
#			$op.= "<option value=\"$key\">$key\n";
			if($CL_VALUES[6] eq "$key" || $CL_VALUES[8] eq "$key" || $CL_VALUES[9] eq "$key" || $CL_VALUES[10] eq "$key"){
				$op.= "<option value=\"$key\">$key\n";
			}
		}
	}
	#ハイエロファントの場合のみ下記エラー対象外
	&ERROR('対象がありません。') if !$op && $CL_VALUES[15] ne "f" && $MENTE!=1;
	print "<input type=hidden name=cardCheck value=$DATE>";
	print << "	-----END-----";
	<script language="JavaScript">
		function checkcard1(anti3){
			if (confirm(anti3+'を使用します。よろしいですか？') == true)
			{return true;}else{return false}
		}
		function checkcard2(anti3){
			if (confirm('カードを破棄します。よろしいですか？') == true)
			{return true;}else{return false}
		}
	</script>
		<tr><td $BgColor><b>対象選択</b><br>
			&nbsp;&nbsp;<select name="chisa">$op</select></td></tr>
	-----END-----
	require "./$LOG_FOLDER/$CARD_DATA";

	foreach $Key (sort{$a cmp $b} keys %VACARD_LIST){
		my@vcard = split(/\,/,$VACARD_LIST{$Key});
	print << "	-----END-----" if $Key eq $CL_VALUES[15] || $MENTE==1;
		<tr><td $BgColor><table style="font-size:10pt;"><tr><td>
		<img src="$IMG_FOLDER6/$vcard[3].gif"></td><td valign=top width=100% $BgColor>
		<b><font size=4>$vcard[0] $vcard[2]</font>
		<hr color="$TABLE_BORDER">$vcard[5]</b>
		<br><br><input name="Emode" type=submit value="$vcard[1]" onClick="return checkcard1('$vcard[1]')">
		<input name="Emode" type=submit value="カード破棄" onClick="return checkcard2('カード破棄')">
		</td></td></tr></table></td></tr>
	-----END-----
	}

	print << "	-----END-----" if ($MENTE==1);#管理人専用
		<tr><td $BgColor><table style="font-size:10pt;"><tr><td>
		<img src="$IMG_FOLDER6/20.gif"></td><td valign=top width=100% $BgColor>
		<b><font size=4>デバッグ1</font>
		<hr color="$TABLE_BORDER">自ユニット以外をカンストさせます</b>
		<br><br><input name="Emode" type=submit value="デバッグ1" onClick="return checkcard('デバッグ1')">
		</td></td></tr></table></td></tr>
	-----END-----
	print << "	-----END-----" if ($MENTE==1);#管理人専用
		<tr><td $BgColor><table style="font-size:10pt;"><tr><td>
		<img src="$IMG_FOLDER6/20.gif"></td><td valign=top width=100% $BgColor>
		<b><font size=4>デバッグ2</font>
		<hr color="$TABLE_BORDER">自ユニット以外の現在HPを1000にします</b>
		<br><br><input name="Emode" type=submit value="デバッグ2" onClick="return checkcard('デバッグ2')">
		</td></td></tr></table></td></tr>
	-----END-----

	print "</table></form>\n";
	&FOOTER;
}
sub CHICON2{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	&CUSTOM_HEADER('Main');
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	print << "	-----END-----";
	<script language="JavaScript">
		function checkCustom(){
			if (confirm('変更します。よろしいですか？') == true)
			{return true;}else{return false}
		}
	</script>
		<tr><td $BgColor><b>戦闘時のアイコンをクラス画像に変更します</b><br>
	-----END-----
		print "<input type=\"radio\" name=\"unitColor\" value=1";
	        print " checked" if $PL_VALUES[36] == 1;
	        print ">する\n";
		print "<input type=\"radio\" name=\"unitColor\" value=0";
	        print " checked" if $PL_VALUES[36] == 0;
	        print ">しない<input name=\"Cmode\" type=submit value=\"アイコンチェンジ\" onClick=\"return checkCustom()\"></td></tr>\n";

	if($PL_VALUES[24] > 1000){$AMA=$PL_VALUES[24]-1000;}
		print "<tr><td $BgColor>\n";
		print "現在の熟練度…".&STATUS_CONVERT("$PL_VALUES[24]",'j')."+$AMA<br>\n" if $PL_VALUES[24] > 1000;
		print "クラスチェンジ回数…$PL_VALUES[23]</td></tr>\n";

	if($COOKIE{'pass'} eq $MASTERPASS){
		my@souko=split(/,/,$PL_VALUES[38]) if $PL_VALUES[38];
		require "./$LOG_FOLDER/$HASH_DATA";
		require "./$LOG_FOLDER/$CLASS_DATA";
		my@class=split(/\,/,$VCLASS_LIST{"$souko[0]"});
		local($WN_A,$WLV_A) = split(/!/,$souko[1]);
		local($WN_B,$WLV_B) = split(/!/,$souko[2]);
		local($WN_C,$WLV_C) = split(/!/,$souko[3]);
		my@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
		my@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
		my@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
		$WEP_A=$WLV_A%$WEAPON_LVUP;
		$WEP_B=$WLV_B%$WEAPON_LVUP;
		$WEP_C=$WLV_C%$WEAPON_LVUP;
		$WLV_A=int$WLV_A/$WEAPON_LVUP;
		$WLV_B=int$WLV_B/$WEAPON_LVUP;
		$WLV_C=int$WLV_C/$WEAPON_LVUP;
		print "<tr><td $BgColor><b>現在のクラス・武器を入れ替えます</b>\n";
		print "<dl><dt>クラス</dt><dd>$class[0]</dd><dt>エレメント<dt><dd>".&STATUS_CONVERT("$souko[4]",'e')."</dd><dt>熟練度</dt><dd>$souko[5]</dd><dt>装備1</dt><dd>$WN_sA[0] Lv.$WLV_A/exp.$WEP_A</dd>";
		print "<dt>装備2</dt><dd>$WN_sB[0] Lv.$WLV_B/exp.$WEP_B</dd>" if $souko[2];
		print "<dt>装備3</dt><dd>$WN_sC[0] Lv.$WLV_C/exp.$WEP_C</dd>" if $souko[3];
		print "</dl>";
		print "<input name=\"Cmode\" type=submit value=\"倉庫入れ替え\" onClick=\"return checkCustom()\"></td></tr>\n";
	}

	print "</table></form>\n";
	&FOOTER;

}
sub DEFM2{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
#	&ERROR if $PL_VALUES[6]==0 || !$PL_VALUES[5] || !@CL_VALUES;
	require "./$LOG_FOLDER/$HASH_DATA";
#	&REPAIR(\@PL_VALUES);

	local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
	local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
	local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
	local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);
	local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
	local($WN_T,$WLV_T) = split(/!/,$PL_VALUES[42]);
	local($WN_U,$WLV_U) = split(/!/,$PL_VALUES[43]);

	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});@WN_sD2=split(/\,/,$WEAPON_LIST{"$WN_D2"});
	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});

	require "./$LOG_FOLDER/$CLASS_DATA";
	@ALY_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

	&CUSTOM_HEADER('Main');
#	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
#		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
#	@pairs = split(/\,/, $DUMMY{'EB'});
#		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};

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



	&DBM_INPORT(P);&DBM_INPORT(C);
#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

#	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
	&REPAIR(\@PL_VALUES);


	&DBM_CONVERT('C',"$PL_VALUES[5]");
#				<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[5]アップ\" $STYLE_B1 onClick='return checkEn()'></td>
#				&nbsp;&nbsp;消費MP600<input name="Cmode" type=submit value=\"$DELE[0]\" onClick="return checkmahou('デフハーネラ')"></td></tr>
	sub FR {"<option value=\"$Key\">$Key"}
	print << "	-----END-----";
	<script language="JavaScript">
		function checkmahou(anti1){
			if (confirm(anti1+'を使用します。\\nよろしいですか？') == true)
			{return true;}else{return false}
		}
	</script>
	-----END-----
print "<input type=hidden name=mahouCheck value=$DATE>";
	print << "	-----END-----";
</td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006a/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>プレイハーネラ：自身の所属する部隊全員に効果。960秒間、風属性攻撃力+20％　大地属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP400<input name="Xmode" type=submit value="プレイハーネラ" onClick="return checkmahou('プレイハーネラ')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006b/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>プレイゾショネル：自身の所属する部隊全員に効果。960秒間、炎属性攻撃力+20％　水属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP400<input name="Xmode" type=submit value="プレイゾショネル" onClick="return checkmahou('プレイゾショネル')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006c/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>プレイバーサ：自身の所属する部隊全員に効果。960秒間、大地属性攻撃力+20％　風属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP400<input name="Xmode" type=submit value="プレイバーサ" onClick="return checkmahou('プレイバーサ')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006d/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>プレイグルーザ：自身の所属する部隊全員に効果。960秒間、水属性攻撃力+20％　炎属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP400<input name="Xmode" type=submit value="プレイグルーザ" onClick="return checkmahou('プレイグルーザ')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!83/ || $WN_sT[7] =~ m/!83/ ||$WN_sU[7] =~ m/!83/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>デフハーネラ：自身の所属する部隊全員に効果。960秒間、風属性攻撃力+20％　大地属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP600<input name="Xmode" type=submit value="デフハーネラ" onClick="return checkmahou('デフハーネラ')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!84/ || $WN_sT[7] =~ m/!84/ ||$WN_sU[7] =~ m/!84/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>デフゾショネル：自身の所属する部隊全員に効果。960秒間、炎属性攻撃力+20％　水属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP600<input name="Xmode" type=submit value="デフゾショネル" onClick="return checkmahou('デフゾショネル')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!85/ || $WN_sT[7] =~ m/!85/ ||$WN_sU[7] =~ m/!85/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>デフバーサ：自身の所属する部隊全員に効果。960秒間、大地属性攻撃力+20％　風属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP600<input name="Xmode" type=submit value="デフバーサ" onClick="return checkmahou('デフバーサ')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!86/ || $WN_sT[7] =~ m/!86/ ||$WN_sU[7] =~ m/!86/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>デフグルーザ：自身の所属する部隊全員に効果。960秒間、水属性攻撃力+20％　炎属性防御力+20％</b><br>
				&nbsp;&nbsp;消費MP600<input name="Xmode" type=submit value="デフグルーザ" onClick="return checkmahou('デフグルーザ')"></td></tr>
	-----END-----
	print << "	-----END-----" if (($WN_sS[7] =~ m/!8i/ || $WN_sT[7] =~ m/!8i/ ||$WN_sU[7] =~ m/!8i/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>マーシーレイン：自身の所属する部隊全員のHPを最大ＨＰの20％分、ＨＰ回復します。(ユニットエレメントが水属性の場合は回復量+10％)</b><br>
				&nbsp;&nbsp;消費MP600<input name="Xmode" type=submit value="マーシーレイン" onClick="return checkmahou('マーシーレイン')"></td></tr>
	-----END-----
	print << "	-----END-----" if (($WN_sS[7] =~ m/!8j/ || $WN_sT[7] =~ m/!8j/ ||$WN_sU[7] =~ m/!8j/) && $PL_VALUES[17] >= 1500 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>マーティライズ：自身の所属する部隊全員の戦闘不能\回復。発動後、使用者は戦闘不能\になります。</b><br>
				&nbsp;&nbsp;消費MP1500<input name="Xmode" type=submit value="マーティライズ" onClick="return checkmahou('マーティライズ')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[25] eq "1");
			<tr><td $BgColor><b>戦闘不能\中は、補助魔法を行使できません。</b></td></tr>
	-----END-----
	print "</td></tr></table></form>\n";

	&FOOTER;



}
sub ICONEX2 {
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&UNLOCK;
	$BgColor="bgcolor=\"$TABLE_COLOR1\" style=\"padding:5px;\"";
	&HEADER;
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT method=POST name=Ms target="Main" onSubmit='window.location.replace("$BACKFR");'>
		<input type=hidden name=cmd value=CUSTOM>
		<input type=hidden name=CustomCheck value=$Date>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
	<table bordercolor=\"$TABLE_BORDER\" border=1 cellspacing=0 style="font-size:10pt;">
		<tr><td bgcolor=\"$TABLE_COLOR2\"><b>$FORM{'custom'}</b></td></tr>
	-----END-----


	if ($PL_VALUES[8] >= 100000){
	print << "	-----END-----";
	<script language="JavaScript">
	function changeImg(){
	num=document.Ms.icon.value;document.msImg.src="$IMG_FOLDER2/"+ num +".gif";
	}
	function changeImg2(){
	num2=document.Ms.icon2.value;document.msImg2.src="$IMG_FOLDER7/"+ num2 +".gif";
	}
	function checkCustom(){
	if (document.Ms.MsName.value == ''){window.alert("コードネームが未記入です。");return false;
	}else if(document.Ms.MsName.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
		window.alert("だーめっ！");return false;
	}else if (confirm('チェンジします。よろしいですか？') == true){return true;
	}else{return false}
	}
	</script>
	-----END-----
	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/classchange.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">アイコンチェンジ！</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";

	print "<tr><td style=\"padding-top:8px;\">ユニットアイコン<img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" name=\"msImg\"></td></tr>\n";
	print "<tr><td style=\"padding-left:10px;\"><select name=icon onChange=\"changeImg()\">\n";
	foreach (0..$ICON){
		print "<option value=\"$_\"";
		print " selected\n"if $_ eq $PL_VALUES[27];
		print ">No.$_\n";
	}
	if($SPECIAL_ICON == 1 && $PL_VALUES[29] >= 200 && $PL_VALUES[24] > 999){$_='';
		foreach (500..$S_ICON_NUMBER){
			print "<option value=\"$_\"";
			print " selected\n"if $_ eq $PL_VALUES[27];
			print ">No.$_\n";
		}
	}
	if($ICON_SPECIAL == 1 && $PL_VALUES[29] >= 300 && $PL_VALUES[24] > 999){$_='';
		foreach (700..$ICON_S_NUMBER){
			print "<option value=\"$_\"";
			print " selected\n"if $_ eq $PL_VALUES[27];
			print ">No.$_\n";
		}
	}

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">キャラクタアイコン<img src=\"$IMG_FOLDER7/$PL_VALUES[40].gif\" name=\"msImg2\"></td></tr>\n";
	print "<tr><td style=\"padding-left:10px;\"><select name=icon2 onChange=\"changeImg2()\">\n";
	foreach (0..$ICON2){
		print "<option value=\"$_\"";
		print " selected\n"if $_ eq $PL_VALUES[40];
		print ">No.$_\n";
	}

	if($CICON_SPECIAL == 1 && $PL_VALUES[29] >= 300 && $PL_VALUES[24] > 999){$_='';
		foreach (701..$CICON_S_NUMBER){
			print "<option value=\"$_\"";
			print " selected\n"if $_ eq $PL_VALUES[40];
			print ">No.$_\n";
		}
	}

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">コードネーム</td></tr>\n";
	print "<tr><td style=\"padding-left:10px;\"><input type=text name=MsName size=30 maxlength=15 value=$PL_VALUES[3] $STYLE_L></td></tr>\n";

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">色変更";
	print "</td></tr>\n<tr><td style=\"padding-left:10px;\"><select name=MsColor>";
	foreach (@COLOR){
		print "<option value=\"$_\"";
        	print " selected\n" if $_ =~ /$PL_VALUES[13]/i;
        	print " style=\"color:#$_\">■$_\n";
	}
	print "</select></td></tr>\n<tr align=\"right\"><td style=\"padding-left:10px;\">";
	print "<input name=\"Cmode\" type=submit value=\"チェンジ\" onClick=\"return checkCustom()\">\n";
	print "</td></tr>\n</table>\n";
	}


	print "</td></tr>\n";
	print "</form></table>\n";

	&FOOTER;
}
1;

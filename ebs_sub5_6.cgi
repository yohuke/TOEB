sub CUSTOM_HEADER {
	$BgColor="bgcolor=\"$TABLE_COLOR1\" style=\"padding:5px;\"";
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
sub SKLSET2 {
	&CUSTOM_HEADER('Main');
	require "./$LOG_FOLDER/$HASH_DATA";
	require "./$LOG_FOLDER/$CONV_DATA";
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&UNLOCK;

	@A_01=split(/!/,$PL_VALUES[60]);@A_02=split(/!/,$PL_VALUES[61]);@A_03=split(/!/,$PL_VALUES[62]);@A_04=split(/!/,$PL_VALUES[63]);
	@A_05=split(/!/,$PL_VALUES[64]);@A_06=split(/!/,$PL_VALUES[65]);@A_07=split(/!/,$PL_VALUES[66]);@A_08=split(/!/,$PL_VALUES[67]);
	@A_09=split(/!/,$PL_VALUES[68]);@A_10=split(/!/,$PL_VALUES[69]);@A_11=split(/!/,$PL_VALUES[70]);@A_12=split(/!/,$PL_VALUES[71]);
	@A_13=split(/!/,$PL_VALUES[72]);@A_14=split(/!/,$PL_VALUES[73]);@A_15=split(/!/,$PL_VALUES[74]);@A_16=split(/!/,$PL_VALUES[75]);

	local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
	local($WN_T,$WLV_T) = split(/!/,$PL_VALUES[42]);
	local($WN_U,$WLV_U) = split(/!/,$PL_VALUES[43]);
	
	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
	@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
	@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});

	$Pl_AbiNameA="$WN_sS[0]";
	$Pl_AbiNameB="$WN_sT[0]";
	$Pl_AbiNameC="$WN_sU[0]";


	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">スキル情報</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";

#		print "<tr><td>現在獲得しているAP･･･$PL_VALUES[53]&nbsp;</td></tr>\n";
		if($WN_sS[0] ne ""){
			print "<tr><td>$Pl_AbiNameA</td></tr>\n";
		}
		if($WN_sT[0] ne ""){
			print "<tr><td>$Pl_AbiNameB</td></tr>\n";
		}
		if($WN_sU[0] ne ""){
			print "<tr><td>$Pl_AbiNameC</td></tr>\n";
		}
		
	print "<tr><td style=\"padding-left:20px;\"></td></tr></table>\n";
#	print "<tr><td style=\"padding-left:20px;\">$PartofW</td></tr></table>\n";

#装備品ソート　10～38の3装備品の並び替えを行う
		if($WN_sS[0] eq ""){
			$Pl_AbiNameA = "----------";
		}
		if($WN_sT[0] eq ""){
			$Pl_AbiNameB = "----------";
		}
		if($WN_sU[0] eq ""){
			$Pl_AbiNameC = "----------";
		}
	if ($WN_sS[0] || $WN_sT[0] || $WN_sU[0]){
		&JScfm(checkAbiSort,"アビリティを並び替えます。よろしいですか？");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">スキル並び替え</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
#		print "<tr><td><input type=radio name=sortbi value=0 disabled\n";
#		print "<b>----------&nbsp;&nbsp;</b></td>\n";
#		print "<td><input type=radio name=sortab value=0 disabled\n";
#		print "<b>----------&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td><input type=radio name=sorte value=1 \n";
		print "<b>$Pl_AbiNameA&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=1 \n";
		print "<b>$Pl_AbiNameA&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td><input type=radio name=sorte value=2 \n";
		print "<b>$Pl_AbiNameB&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=2 \n";
		print "<b>$Pl_AbiNameB&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td><input type=radio name=sorte value=3 \n";
		print "<b>$Pl_AbiNameC&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=3 \n";
		print "<b>$Pl_AbiNameC&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td></td><td style=\"padding-right:10px;\"><input type=submit name=Cmode value=スキル並び替え onClick=\"return checkAbiSort()\"></td></tr></table>\n";
	}

	if ($WN_sS[0] ne "" || $WN_sT[0] ne "" || $WN_sU[0] ne ""){
		$PartofSAB.="<option value=0>";
		$PartofSAB.="<option value=1>$Pl_AbiNameA" if $WN_sS[0];
		$PartofSAB.="<option value=2>$Pl_AbiNameB" if $WN_sT[0];
		$PartofSAB.="<option value=3>$Pl_AbiNameC" if $WN_sU[0];
		print "<SCRIPT language=\"JavaScript\">\nfunction checkAPoint (){\n";
		print "num=document.Ms.sellAbi.value;\nif (num==1){var wn='$Pl_AbiNameA';}\n";
		print "else if (num ==2){var wn='$Pl_AbiNameB';}\n";
		print "else if (num ==3){var wn='$Pl_AbiNameC';}\n";
		print "else if (num ==0){return false}\n";		
		print "if (confirm(wn + 'を消去します。よろしいですか？') == true){\n";
		print "if (confirm('本当に' + wn + 'を消去してよろしいですか？') == true){return true;}else{return false}\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">スキル消去</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=sellAbi>$PartofSAB</select><input type=submit name=Cmode value=スキル消去 onClick=\"return checkAPoint()\"></td></tr></table>\n";

		print "</td></tr>";
	}
	if ($WN_sS[0] eq "" || $WN_sT[0] eq "" || $WN_sU[0] eq ""){
#		print "<tr><td $BgColor height=\"150\" background=\"$IMG_FOLDER1/shop.gif\" style=\"background-repeat:no-repeat;background-position:top;text-align: center;\"><img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" style=\"position:relative;top:20;right:22;\"></td></tr><tr><td $BgColor >\n";
		print "<tr><td></td></tr><tr><td $BgColor >\n";
		print "<table style=\"font-size:9pt;\"><img src=\"$IMG_FOLDER1/equipshop.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">スキルリスト</b>\n";
		&JScfm(checkGet,"スキルを習得します。よろしいですか？");
		local($Flag=0);
		$buy="<select name=buyskill>";
#		foreach $key (sort{$a cmp $b} keys %ABINAME_LIST){
		if($WN_sS[0] eq "" || $WN_sT[0] eq "" || $WN_sU[0] eq ""){
			$Hensu = 60;
			$Haire = 0;

			foreach $key (sort{$a cmp $b} keys %CONV_LIST){
#				my @ByW = split(/\,/,$ABINAME_LIST{$key});
				my @ByW = split(/\,/,$CONV_LIST{$key});
#				print "<tr><td>&nbsp;&nbsp;<img src=\"$IMG_FOLDER4/$ByW[9].gif\"></td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[5]</td></tr>";

				$Hensu = $ByW[1];
				@Chk_Skill=split(/!/,$PL_VALUES[$Hensu]);
				#配列の最大要素数を算出
				$HaireMax = $#Chk_Skill;
#&ERROR("$HaireMax");

				for($LngCnt = 0;$LngCnt <= $HaireMax;$LngCnt++){

#&ERROR("$Chk_Skill[$LngCnt]ああ$Hensuいい$ByW[1]うう$ByW[2]");
					if($Chk_Skill[$LngCnt] >= 1 && $LngCnt == $ByW[2] && $Hensu == $ByW[1]){
					
						#$Chk_Skill[$LngCnt] $WEP_A=$WLV_A%$WEAPON_LVUP;
						$WEP_L=int(($Chk_Skill[$LngCnt] - 1) / 100);
#						$WEP_L=34;
						print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]&nbsp;Lv.$WEP_L</td></tr>";
						$buy.="<option value=$key>$ByW[0]\n";$Flag++;
						$Hensu = 60;
						$Haire = 0;
						$LngCnt = $HaireMax;
						last;

					}else{
#						print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]</td></tr>";
#						$buy.="<option value=$key>$ByW[0]\n";$Flag++;

						$Haire = $Haire + 1;
						if($HaireMax < $Haire){
							$Haire = 0;
							$Hensu = $Hensu + 1;
						}

					}
				}

			}
		}
		if ($Flag>0){
			$buy.="</select><input name=\"Cmode\" type=submit value=スキルセット onClick=\"return checkGet()\">\n";
		}else{
			$buy="スキル枠が全て埋まっている或いは、スキルを習得していません。";$Flag++;
		}
		print "</table><div align=right>$buy</div></td></tr>\n";
	}
#	if (!$PL_VALUES[10] && !$PL_VALUES[11] && !$PL_VALUES[38] && !$PL_VALUES[41] && !$PL_VALUES[42] && !$PL_VALUES[43] && $Flag==0 && $WeCH ==0 && $JACKF==0){
	if ($WN_sS[0] eq "" && $WN_sT[0] eq "" && $WN_sU[0] eq "" && $Flag==0){
		print "<tr><td $BgColor>実行できるコマンドがありません。</td></tr>\n";}
	print "</form></table>\n";&FOOTER;
}
1;

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
sub ABISET2 {
	&CUSTOM_HEADER('Main');
	require "./$LOG_FOLDER/$ABI_DATA";
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&UNLOCK;

	local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);

	@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
	@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
	@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

	$Pl_AbiNameA="$ABI_sA[0]";
	$Pl_AbiNameB="$ABI_sB[0]";
	$Pl_AbiNameC="$ABI_sC[0]";


	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">アビリティ情報</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";

		print "<tr><td>現在獲得しているAP･･･$PL_VALUES[53]&nbsp;</td></tr>\n";
		if($ABI_sA[0] ne ""){
			print "<tr><td>$Pl_AbiNameA：$ABI_sA[3]</td></tr>\n";
		}
		if($ABI_sB[0] ne ""){
			print "<tr><td>$Pl_AbiNameB：$ABI_sB[3]</td></tr>\n";
		}
		if($ABI_sC[0] ne ""){
			print "<tr><td>$Pl_AbiNameC：$ABI_sC[3]</td></tr>\n";
		}
		
	print "<tr><td style=\"padding-left:20px;\"></td></tr></table>\n";
#	print "<tr><td style=\"padding-left:20px;\">$PartofW</td></tr></table>\n";

#装備品ソート　10～38の3装備品の並び替えを行う
		if($ABI_sA[0] eq ""){
			$Pl_AbiNameA = "----------";
		}
		if($ABI_sB[0] eq ""){
			$Pl_AbiNameB = "----------";
		}
		if($ABI_sC[0] eq ""){
			$Pl_AbiNameC = "----------";
		}
	if ($ABI_sA[0] || $ABI_sB[0] || $ABI_sC[0]){
		&JScfm(checkAbiSort,"アビリティを並び替えます。よろしいですか？");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">技術並び替え</b>\n";

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

		print "<tr><td></td><td style=\"padding-right:10px;\"><input type=submit name=Cmode value=技術並び替え onClick=\"return checkAbiSort()\"></td></tr></table>\n";
	}

	if ($ABI_sA[0] ne "" || $ABI_sB[0] ne "" || $ABI_sC[0] ne ""){
		$PartofSAB.="<option value=0>";
		$PartofSAB.="<option value=1>$Pl_AbiNameA" if $ABI_sA[0];
		$PartofSAB.="<option value=2>$Pl_AbiNameB" if $ABI_sB[0];
		$PartofSAB.="<option value=3>$Pl_AbiNameC" if $ABI_sC[0];
		print "<SCRIPT language=\"JavaScript\">\nfunction checkAPoint (){\n";
		print "num=document.Ms.sellAbi.value;\nif (num==1){var wn='$Pl_AbiNameA';}\n";
		print "else if (num ==2){var wn='$Pl_AbiNameB';}\n";
		print "else if (num ==3){var wn='$Pl_AbiNameC';}\n";
		print "else if (num ==0){return false}\n";		
		print "if (confirm(wn + 'を忘れます。よろしいですか？') == true){\n";
		print "if (confirm('本当に' + wn + 'を忘れてよろしいですか？') == true){return true;}else{return false}\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">忘れる</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=sellAbi>$PartofSAB</select><input type=submit name=Cmode value=忘れる onClick=\"return checkAPoint()\"></td></tr></table>\n";

		print "</td></tr>";
	}
	if ($ABI_sA[0] eq "" || $ABI_sB[0] eq "" || $ABI_sC[0] eq ""){
#		print "<tr><td $BgColor height=\"150\" background=\"$IMG_FOLDER1/shop.gif\" style=\"background-repeat:no-repeat;background-position:top;text-align: center;\"><img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" style=\"position:relative;top:20;right:22;\"></td></tr><tr><td $BgColor >\n";
		print "<tr><td></td></tr><tr><td $BgColor >\n";
		print "<table style=\"font-size:9pt;\"><img src=\"$IMG_FOLDER1/equipshop.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">アビリティリスト</b>\n";
		&JScfm(checkGet,"アビリティを習得します。よろしいですか？");
		local($Flag=0);
		$buy="<select name=buyabi>";
		foreach $key (sort{$a cmp $b} keys %ABINAME_LIST){
			my @ByW = split(/\,/,$ABINAME_LIST{$key});
			if($ABI_sA[0] eq "" || $ABI_sB[0] eq "" || $ABI_sC[0] eq ""){
				if($ByW[1] <= $PL_VALUES[53]){
#					print "<tr><td>&nbsp;&nbsp;<img src=\"$IMG_FOLDER4/$ByW[9].gif\"></td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[5]</td></tr>";
					print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[1]</td><td style=\"text-align:left;\">$ByW[3]</td></tr>";
					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
				}
			}
		}
		if ($Flag>0){
			$buy.="</select><input name=\"Cmode\" type=submit value=技術習得 onClick=\"return checkGet()\">\n";
		}else{
			$buy="アビリティポイントが足りません。";$Flag++;
		}
		print "</table><div align=right>$buy</div></td></tr>\n";
	}
#	if (!$PL_VALUES[10] && !$PL_VALUES[11] && !$PL_VALUES[38] && !$PL_VALUES[41] && !$PL_VALUES[42] && !$PL_VALUES[43] && $Flag==0 && $WeCH ==0 && $JACKF==0){
	if ($ABI_sA[0] eq "" && $ABI_sB[0] eq "" && $ABI_sC[0] eq "" && $Flag==0){
		print "<tr><td $BgColor>実行できるコマンドがありません。</td></tr>\n";}
	print "</form></table>\n";&FOOTER;
}
1;

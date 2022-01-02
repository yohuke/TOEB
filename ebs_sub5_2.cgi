sub CUSTOMING2 {
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
#"
$LIMIT_HP = 80000;
$LIMIT_MP = 4000;
if($AbiSys == 1){

	require "./$LOG_FOLDER/$ABI_DATA";
	local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
	@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
	@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
	@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

	if($ABI_sA[2] =~ m/!A0034/ || $ABI_sB[2] =~ m/!A0034/ || $ABI_sC[2] =~ m/!A0034/){$LIMIT_HP=90000;}
	if($ABI_sA[2] =~ m/!A0035/ || $ABI_sB[2] =~ m/!A0035/ || $ABI_sC[2] =~ m/!A0035/){$LIMIT_MP=5000;}

}
#if($PL_VALUES[16] < 80000 || $PL_VALUES[18] < 4000 || $PL_VALUES[24] >= 210){
if($PL_VALUES[16] < $LIMIT_HP || $PL_VALUES[18] < $LIMIT_MP || $PL_VALUES[24] >= 210){

#if($PL_VALUES[16] < 80000 || $PL_VALUES[18] < 4000){
if($PL_VALUES[16] < $LIMIT_HP || $PL_VALUES[18] < $LIMIT_MP){
	$HM=$PL_VALUES[16] + 5000;
	$EM=$PL_VALUES[18]*10 + 5000;
	$HM2=($PL_VALUES[16] + 5000) * 5 + 2000;
	$EM2=($PL_VALUES[18]*10 + 5000) * 5 + 500;
	$HM3=($PL_VALUES[16] + 5000) * 10 + 9000;
	$EM3=($PL_VALUES[18]*10 + 5000) * 10 + 2250;

	foreach $key (1..20){
		$OP.="<option value=$key>$key回";
	}
print<<"-----HTMLTAG-----";
	<script language="JavaScript">
	var Hp = 200;
	var En = 5;


	function checkHp(){
		if($HM > $PL_VALUES[8]){
			alert('お金が足りません');return false;
		}else if($PL_VALUES[16] >= $LIMIT_HP){
			alert('これ以上アップできません');return false;
		}else{
			if(confirm("$STATUS_NAME[4]アップ×１の$CUSTOM_NAMEをします。よろしいですか？")){return true;}else{return false;}
		}
	}
	function checkHp2(){
		if($HM2 > $PL_VALUES[8]){
			alert('お金が足りません');return false;
		}else if($PL_VALUES[16] >= $LIMIT_HP){
			alert('これ以上アップできません');return false;
		}else{
			if(confirm("$STATUS_NAME[4]アップ×５の$CUSTOM_NAMEをします。よろしいですか？")){return true;}else{return false;}
		}
	}
	function checkHp3(){
		if($HM3 > $PL_VALUES[8]){
			alert('お金が足りません');return false;
		}else if($PL_VALUES[16] >= $LIMIT_HP){
			alert('これ以上アップできません');return false;
		}else{
			if(confirm("$STATUS_NAME[4]アップ×１０の$CUSTOM_NAMEをします。よろしいですか？")){return true;}else{return false;}
		}
	}

	function checkEn(){
		if($EM > $PL_VALUES[8]){
			alert('お金が足りません');return false;
		}else if($PL_VALUES[18] >= $LIMIT_MP){
			alert('これ以上アップできません');return false;
		}else{
			if(confirm("$STATUS_NAME[5]アップ×１の$CUSTOM_NAMEをします。よろしいですか？")){return true;}else{return false;}
		}

	}
	function checkEn2(){
		if($EM2 > $PL_VALUES[8]){
			alert('お金が足りません');return false;
		}else if($PL_VALUES[18] >= $LIMIT_MP){
			alert('これ以上アップできません');return false;
		}else{
			if(confirm("$STATUS_NAME[5]アップ×５の$CUSTOM_NAMEをします。よろしいですか？")){return true;}else{return false;}
		}

	}
	function checkEn3(){
		if($EM3 > $PL_VALUES[8]){
			alert('お金が足りません');return false;
		}else if($PL_VALUES[18] >= $LIMIT_MP){
			alert('これ以上アップできません');return false;
		}else{
			if(confirm("$STATUS_NAME[5]アップ×１０の$CUSTOM_NAMEをします。よろしいですか？")){return true;}else{return false;}
		}

	}


	function checkHMn(Num){
	Chmn=0;
	Chmn = ($HM + (Num - 1) * 100) * Num;
	hm.innerHTML=Chmn;
	}

	function checkEMn(nuM){
	Cemn=0;
	Cemn = ($EM + (nuM - 1) * 25) * nuM;
	em.innerHTML=Cemn;
	}

	</script>

	<tr><td $BgColor><img src=\"$IMG_FOLDER1/training.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">トレーニング</b>

	<table style="font-size:10pt;margin-left:8px;margin-right:8px;">
	<tr>
	<td>$STATUS_NAME[4]アップ×１</td>
	<td><font id=hm>$HM</font>Goth</td>
	<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[4]アップ×１\" $STYLE_B1 onClick='return checkHp()'></td>
	</tr>
	<tr>
	<td>$STATUS_NAME[4]アップ×５</td>
	<td><font id=hm>$HM2</font>Goth</td>
	<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[4]アップ×５\" $STYLE_B1 onClick='return checkHp2()'></td>
	</tr>
	<tr>
	<td>$STATUS_NAME[4]アップ×１０</td>
	<td><font id=hm>$HM3</font>Goth</td>
	<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[4]アップ×１０\" $STYLE_B1 onClick='return checkHp3()'></td>
	</tr>
	<tr>
	<td>$STATUS_NAME[5]アップ×１</td>
	<td><font id=em>$EM</font>Goth</td>
	<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[5]アップ×１\" $STYLE_B1 onClick='return checkEn()'></td>
	</tr>
	<tr>
	<td>$STATUS_NAME[5]アップ×５</td>
	<td><font id=em>$EM2</font>Goth</td>
	<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[5]アップ×５\" $STYLE_B1 onClick='return checkEn2()'></td>
	</tr>
	<tr>
	<td>$STATUS_NAME[5]アップ×１０</td>
	<td><font id=em>$EM3</font>Goth</td>
	<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[5]アップ×１０\" $STYLE_B1 onClick='return checkEn3()'></td>
	</tr>
	</table>

	</td></tr>
-----HTMLTAG-----
}
	if ($PL_VALUES[8] >= 20000 && $PL_VALUES[24] >=210){
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
	}else if (confirm('クラスチェンジします。よろしいですか？') == true){return true;
	}else{return false}
	}
	</script>
	-----END-----
	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/classchange.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">クラスチェンジ</b>\n";

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

	print "<tr><td style=\"padding-top:8px;\">クラス</td></tr>\n<tr><td style=\"padding-left:10px;\">";

	local($PL_WN,$PL_WLV) = split(/!/,$PL_VALUES[9]);
	local($PL_WS,$PL_WLVS) = split(/!/,$PL_VALUES[41]);
	require "./$LOG_FOLDER/$HASH_DATA";
	@Pl_W=split(/\,/,$WEAPON_LIST{"$PL_WN"});
	@Pl_SW=split(/\,/,$WEAPON_LIST{"$PL_WS"});
	require "./$LOG_FOLDER/$CLASS_DATA";

	print "<select name=MsType>\n";

	while (my($key,$value) = each %VCLASS_LIST){
		my@change = split(/\,/,$value);
		if($change[5]==1){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		}elsif($change[5]==2){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && ($Pl_W[0] eq "$change[15]" || $Pl_SW[0] eq "$change[15]") && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		}elsif($change[5]==3){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && $PL_VALUES[24]<=$change[20] && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		}elsif($change[5]==4){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && ($Pl_W[7] =~ /$change[15]/i || $Pl_SW[7] =~ /$change[15]/i) && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		}elsif($change[5]==5){
		  if($TIME[2] =~ /^18$|^19$|^20$|^21$|^22$|^23$|^0$|^1$|^2$|^3$|^4$|^5$/i){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && ($Pl_W[0] eq "$change[15]" || $Pl_SW[0] eq "$change[15]") && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		  }
		}elsif($change[5]==6){
		  if($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && ($Pl_W[0] eq "$change[15]" || $Pl_SW[0] eq "$change[15]") && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		  }
		}elsif($change[5]==7){
		  if($TIME[2] =~ /^18$|^19$|^20$|^21$|^22$|^23$|^0$|^1$|^2$|^3$|^4$|^5$/i){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		  }
		}elsif($change[5]==8){
		  if($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		  }
		}elsif($change[5]==9){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && $PL_VALUES[32]>=$change[21] && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		}elsif($change[5]==10){
			if($PL_VALUES[19]>=$change[6] && $PL_VALUES[20]>=$change[7] && $PL_VALUES[21]>=$change[8] && $PL_VALUES[22]>=$change[9] && $PL_VALUES[16]>=$change[10] && $PL_VALUES[18]>=$change[11] && $PL_VALUES[12]>=$change[12] && $PL_VALUES[12]<=$change[13] && $PL_VALUES[24]>=$change[14] && $PL_VALUES[32]>=$change[21] && ($Pl_W[0] eq "$change[15]" || $Pl_SW[0] eq "$change[15]") && $PL_VALUES[4] =~ /$change[16]/i){
				print "<option value=$key";
				print " selected" if $PL_VALUES[4] == $key;
				print ">$change[0]\n";
			}
		}else{
			print "<option value=$key";
			print " selected" if $PL_VALUES[4] == $key;
			print ">$change[0]\n";		
		}
	}
	print "</select>\n";

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">エレメント選択";

	print "</td></tr>\n<tr><td style=\"padding-left:10px;\">";
	print "<select name=element>";
	print "<option value=0";
	print " selected"if $PL_VALUES[31]==0;
	print ">風";
	print "<option value=1";
	print " selected"if $PL_VALUES[31]==1;
	print ">炎";
	print "<option value=2";
	print " selected"if $PL_VALUES[31]==2;
	print ">大地";
	print "<option value=3";
	print " selected"if $PL_VALUES[31]==3;
	print ">水";
	print "</select>";

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">色変更";
	print "</td></tr>\n<tr><td style=\"padding-left:10px;\"><select name=MsColor>";
	foreach (@COLOR){
		print "<option value=\"$_\"";
        	print " selected\n" if $_ =~ /$PL_VALUES[13]/i;
        	print " style=\"color:#$_\">■$_\n";
	}
	print "</select></td></tr>\n<tr align=\"right\"><td style=\"padding-left:10px;\">";
	print "<input name=\"Cmode\" type=submit value=\"Custom\" onClick=\"return checkCustom()\">\n";
	print "</td></tr>\n</table>\n";
	}

}else{
	print "<tr><td $BgColor>鍛錬コマンドは使用できません。</td></tr>";
}

	print "</td></tr>\n";
	print "</form></table>\n";

	&FOOTER;
}
1;

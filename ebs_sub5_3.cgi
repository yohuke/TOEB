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
#			if ($c <= $HISTORY_MAX && $Key <= time && "$NOTE{$Key}" ne 'ðj'){
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
			if(document.Ms.com.value.match('[&! ?=.,*<>"\\'/¥±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜ¦Ý§¨©ª«¯~@ABCDEFGHIJKLMNOPQRSßçãÛÚæ¿¾ú\ú^ú`úbúdú~úú¡ú£úªú±ú²TUVWXYZ[]]') != null) {
				window.alert("¾[ßÁI");return false ;
			}else{	if (confirm('RgðÏXµÜ·Bæëµ¢Å·©H') == true){return true;}else{return false}	}
		}
		</script>
		<tr><td $BgColor><b>RgÏX</b><br>
		&nbsp;&nbsp;<input type="text" name="com" size="70" maxlength="50" value="" $STYLE_L><br>
		&nbsp;&nbsp;<span style="font-size:13px;">RgüÍãAK¸uÏXv{^ðNbNµÄº³¢B
		Enter{^ÅÍ½f³êÜ¹ñB</span><br><input type="hidden" name="Cflag" value="ON">
		&nbsp;&nbsp;<input name="Cmode" type="submit" value="ÏX" onClick=\"return checkComment()\">
		&nbsp;&nbsp;<input type="reset" value="NA"></td></tr></form></table>
	-----END-----
	&FOOTER;
}
sub SPECIAL{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	&CUSTOM_HEADER('Sub');

	require "./$LOG_FOLDER/$CLASS_DATA";
	@ALY_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

	print "<tr><td $BgColor><br>";
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"\" onClick=\"document.Ms.cmd.value='MAKE_C';\">" if $PL_VALUES[8] > $MAKE_COUNTRY && !$PL_VALUES[6];
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"íª\" onClick=\"document.Ms.cmd.value='MISSION';\">" if $PL_VALUES[6] != 0 && $PL_VALUES[5] && $CL_VALUES[37] < time;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"à\" onClick=\"document.Ms.cmd.value='MAKE_T';\">"if $PL_VALUES[5];
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"vÇ­»\" onClick=\"document.Ms.cmd.value='BOSS';\">" if ($PL_VALUES[6] != 0 || $COOKIE{'pass'} eq $MASTERPASS) && $PL_VALUES[5];
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"SÌâ\" onClick=\"document.Ms.cmd.value='DEFM';\">" if $ALY_CLASS[17] =~m/!E001|!E006a|!E006b|!E006c|!E006d|!8i|!8j/;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"^bgJ[h\" onClick=\"document.Ms.cmd.value='CARD';\">" if ($PL_VALUES[6] != 0 && (($PL_VALUES[5] && $CL_VALUES[15] && $CL_VALUES[7] > time) || ($WW_FRAG==1 && $HIZUK_FRAG==1))) || $MENTE==1;
#	$sp.= "<input name=\"custom\" type=\"submit\" value=\"^bgJ[h\" onClick=\"hide();document.Ms.cmd.value='CARD';\">" if $PL_VALUES[6] != 0 && $PL_VALUES[5] && $CL_VALUES[15] && $CL_VALUES[7] > time || $MENTE==1;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"¨Ü¯\" onClick=\"document.Ms.cmd.value='CHICON';\">" if $PL_VALUES[16] >= 80000 && $PL_VALUES[18] >= 4000;
	$sp.= "<input name=\"custom\" type=\"submit\" value=\"ACR`FWI\" onClick=\"document.Ms.cmd.value='ICONEX';\">" if $PL_VALUES[8] >= 200000;
	$sp.= "<input type=\"submit\" value=\"õ}Ó\" $STYLE_B1 onClick=\"document.Ms.cmd.value='ZUKAN';\">";

	$sp.= "<input name=\"custom\" type=\"submit\" value=\"í­»\" onClick=\"document.Ms.cmd.value='WEAPONFORCE';\">" if $WeaponReinForcement == 1;
	
#	$sp='ÀsÅ«éR}hª èÜ¹ñB' if !$sp;
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

##C|[g
	&DBM_INPORT(P);&DBM_INPORT(C);
	print "<tr><td $BgColor>";


print<<"-----END-----";

<table style="font-size:10pt;margin-left:8px;margin-right:8px;">
<tr><td colspan=3><b>ÅãiÉZbgµÄ¢éõ¼F$WN_sA[0]</b></td></tr>
<tr>
<td colspan=2><input type=hidden name=yousaiCheck value=$DATE><b><span style="font-size:20px;">HP</span> $Y_HP[0]/$Y_HP[1]</b></td>
-----END-----
	#ÅåÆÅ¬ñðæ¾@¼è¥¥¥5@Ðè¥¥¥4@ñEî¥¥¥3
	$Pl_MinCount = 0;$Pl_MaxCount = 0;
	#Å¬ñæ¾
	if($WN_sAEn1){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn2){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn3){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn4){$Pl_MinCount = $Pl_MinCount + 1;}
	if($WN_sAEn5){$Pl_MinCount = $Pl_MinCount + 1;}

	#Ååñæ¾
	#¼èí
	if($WN_sA[7] =~ m/11/){$Pl_MinCount=5;}
	#Ðèí
	elsif($WN_sA[7] =~ m/10/){$Pl_MinCount=4;}
	
	$YO_HP=int($Y_HP[1]*0.3)-37000;
	print "<td>";
	print "<br>$WN_sAEn1[0]";
	print "</td>";

	$YO_STR=int($Y_ST[0]*400)+9600;
	$YO_VIT=int($Y_ST[1]*400)+9600;
	$YO_AGI=int($Y_ST[2]*400)+9600;

	print "</tr><tr><td style=\"width:50px;\"><b>UÍ</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[0]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"UÍ­»\" onClick=\"return ChMn('UÍð­»','$YO_STR')\"></td>" if $Y_ST[0] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>häÍ</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[1]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"häÍ­»\" onClick=\"return ChMn('häÍð­»','$YO_VIT')\"></td>" if $Y_ST[1] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>½Í</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[2]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"½Í­»\" onClick=\"return ChMn('½Íð­»','$YO_AGI')\"></td>" if $Y_ST[2] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

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


##C|[g
	&DBM_INPORT(P);&DBM_INPORT(C);
##wöxÇÝÝE¯ÇÝÝ
	while (my($key,$val) = each %P){
	@VALS = split(/\s/,$val);
		if($VALS[5] eq $PL_VALUES[5]){
			if($VALS[6] == 1){
				$SOUSUISIKI=$VALS[32];
			}
		}
	}
##wö½fA101ÈãÈç100É·é
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
<tr><td colspan=3><b>ïF$CL_VALUES[1]</b></td></tr>
<tr>
<td colspan=2><input type=hidden name=yousaiCheck value=$DATE><b><span style="font-size:20px;">HP</span> $Y_HP[0]/$Y_HP[1]</b></td>
-----END-----
	$YO_HP=int($Y_HP[1]*0.3)-37000;
	print "<td>";
	if ($Y_HP[0] < $Y_HP[1]){
		print "<input name=\"Cmode\" type=\"submit\" value=\"ñ¬\" onClick=\"return ChMn('HPðñi¬j','6000')\">";
		print "<input name=\"Cmode\" type=\"submit\" value=\"ñå\" onClick=\"return ChMn('HPðñiåj','30000')\">";
	}
	print "<input name=\"Cmode\" type=\"submit\" value=\"HP­»\" onClick=\"return ChMn('HPð­»','$YO_HP')\">" if $Y_HP[1] < $YOUSAI_MAX_HP && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));
	print "</td>";

	$YO_STR=int($Y_ST[0]*400)+9600;
	$YO_VIT=int($Y_ST[1]*400)+9600;
	$YO_AGI=int($Y_ST[2]*400)+9600;

	print "</tr><tr><td style=\"width:50px;\"><b>UÍ</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[0]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"UÍ­»\" onClick=\"return ChMn('UÍð­»','$YO_STR')\"></td>" if $Y_ST[0] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>häÍ</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[1]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"häÍ­»\" onClick=\"return ChMn('häÍð­»','$YO_VIT')\"></td>" if $Y_ST[1] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	print "</tr><tr><td style=\"width:50px;\"><b>½Í</b></td><td><b style=\"color:#ff0080;\">NT</b>+$SOUSUISIKI+$Y_ST[2]</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"½Í­»\" onClick=\"return ChMn('½Íð­»','$YO_AGI')\"></td>" if $Y_ST[2] < $YOUSAI_MAX_ST && ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 150000));

	$Zoksen="<select size=1 name=\"Zsentaku\" $STYLE_L>\n";
	$Zoksen .= "<option value=7 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "";
	$Zoksen .= ">³®«</option>";
	$Zoksen .= "<option value=0 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "0";
	$Zoksen .= ">®«</option>";
	$Zoksen .= "<option value=1 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "1";
	$Zoksen .= ">®«</option>";
	$Zoksen .= "<option value=2 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "2";
	$Zoksen .= ">ån®«</option>";
	$Zoksen .= "<option value=3 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "3";
	$Zoksen .= ">®«</option>";
	$Zoksen .= "<option value=4 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "4";
	$Zoksen .= ">_¹®«</option>";
	$Zoksen .= "<option value=5 ";
	$Zoksen .= "selected"if $CL_VALUES[47] eq "5";
	$Zoksen .= ">Ã®«</option>";
	$Zoksen .= "</select>";

	print "</tr><tr><td style=\"width:80px;\"><b>í®«</b></td><td><b style=\"color:#ff0080;\"></b>$Zoksen</td>";
	print "<td><input name=\"Cmode\" type=\"submit\" value=\"®«ÏX\" onClick=\"return ChMn('vÇíð®«ÏX','50000')\"></td>" if ($PL_VALUES[6] == 1 || ($PL_VALUES[6] !=0 && $CL_VALUES[1] >= 50000));

#	$a = time;
#	&ERROR("$WN_sB[7]  $CL_VALUES[7]¢¢$CL_VALUES[37]¤¤$a");

#	if(($WN_sB[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sC[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sD[7] =~ m/!87|!88|!89|!8a|!8b|!8c/) && ($CL_VALUES[7] > time || $CL_VALUES[37] > time)){
	if(($WN_sB[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sC[7] =~ m/!87|!88|!89|!8a|!8b|!8c/ || $WN_sD[7] =~ m/!87|!88|!89|!8a|!8b|!8c/) && ($CL_VALUES[7] > time && $CL_VALUES[45] < time) && $PL_VALUES[6] ne "0" && $PL_VALUES[25] eq "0"){


		$PartofTO.="<option value=10>$CL_VALUES[6]Ì{à" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=11>$CL_VALUES[6]Ìæêà" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=12>$CL_VALUES[6]Ìæñà" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=13>$CL_VALUES[6]ÌæOà" if $CL_VALUES[6] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=20>$CL_VALUES[8]Ì{à" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=21>$CL_VALUES[8]Ìæêà" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=22>$CL_VALUES[8]Ìæñà" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=23>$CL_VALUES[8]ÌæOà" if $CL_VALUES[8] && $CL_VALUES[6] ne $CL_VALUES[8] && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=30>$CL_VALUES[9]Ì{à" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=31>$CL_VALUES[9]Ìæêà" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=32>$CL_VALUES[9]Ìæñà" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=33>$CL_VALUES[9]ÌæOà" if $CL_VALUES[9] && ($CL_VALUES[6] ne $CL_VALUES[9] && $CL_VALUES[8] ne $CL_VALUES[9]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=40>$CL_VALUES[10]Ì{à" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=41>$CL_VALUES[10]Ìæêà" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=42>$CL_VALUES[10]Ìæñà" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);
		$PartofTO.="<option value=43>$CL_VALUES[10]ÌæOà" if $CL_VALUES[10] && ($CL_VALUES[6] ne $CL_VALUES[10] && $CL_VALUES[8] ne $CL_VALUES[10] && $CL_VALUES[9] ne $CL_VALUES[10]) && ($CL_VALUES[7] > time);

		if($WN_sB[7] =~ m/!87/){
			$BO = "TCV^";
		}elsif($WN_sB[7] =~ m/!88/){
			$BO = "TAXf";
		}elsif($WN_sB[7] =~ m/!89/){
			$BO = "T]Vl";
		}elsif($WN_sB[7] =~ m/!8a/){
			$BO = "TO[U";
		}elsif($WN_sB[7] =~ m/!8b/){
			$BO = "Tn[l";
		}elsif($WN_sB[7] =~ m/!8c/){
			$BO = "To[T";
		}

		if($WN_sC[7] =~ m/!87/){
			$CO = "TCV^";
		}elsif($WN_sC[7] =~ m/!88/){
			$CO = "TAXf";
		}elsif($WN_sC[7] =~ m/!89/){
			$CO = "T]Vl";
		}elsif($WN_sC[7] =~ m/!8a/){
			$CO = "TO[U";
		}elsif($WN_sC[7] =~ m/!8b/){
			$CO = "Tn[l";
		}elsif($WN_sC[7] =~ m/!8c/){
			$CO = "To[T";
		}

		if($WN_sD[7] =~ m/!87/){
			$DO = "TCV^";
		}elsif($WN_sD[7] =~ m/!88/){
			$DO = "TAXf";
		}elsif($WN_sD[7] =~ m/!89/){
			$DO = "T]Vl";
		}elsif($WN_sD[7] =~ m/!8a/){
			$DO = "TO[U";
		}elsif($WN_sD[7] =~ m/!8b/){
			$DO = "Tn[l";
		}elsif($WN_sD[7] =~ m/!8c/){
			$DO = "To[T";
		}

		$PartofOA.="<option value=10>$BO" if $WN_sB[7] =~ m/!87|!88|!89|!8a|!8b|!8c/;
		$PartofOA.="<option value=11>$CO" if $WN_sC[7] =~ m/!87|!88|!89|!8a|!8b|!8c/;
		$PartofOA.="<option value=38>$DO" if $WN_sD[7] =~ m/!87|!88|!89|!8a|!8b|!8c/;

		print "<SCRIPT language=\"JavaScript\">\nfunction checkSet (){\n";
		print "if (confirm('I[uðgpµÜ·ªæëµ¢Å·©H') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><b style=\"vertical-align:middle;\">I[uðú</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=TSet>$PartofTO</select></tr><tr></td><td style=\"padding-left:20px;\"><select name=OSet>$PartofOA</select><input type=submit name=Cmode value=ðú onClick=\"return checkSet()\"></td></tr></table>\n";

		print "</td></tr>";
	
	}

	print << "	-----END-----" if ($CL_VALUES[1] >= $NAME_YOSAI && $PL_VALUES[6] == 1);
		</tr><tr><td colspan=3>vÇÌ¼O <input type=text name="yoname" size=25 maxlength=20 value="$Y_ST[3]" $STYLE_L></td></tr>
		<tr><td colspan=3><input name="Cmode" type=submit value="vÇü¼" onClick="return checkYosai()"></td></tr>
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
		print "if (confirm('âíµÜ·Bæëµ¢Å·©H@(¦©Ìâíðs¢Ü·B)') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor>";

		print "</td></tr>";
		if ($CL_VALUES[7] > time){
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td colspan=3><b>âí </b></td><td style=\"padding-left:20px;\"><select name=TeiSet>$Teisen</select></td><td style=\"padding-left:20px;\"><input type=submit name=Cmode value=âíé¾ onClick=\"return checkTeisen()\"></td></tr></table>\n";
#			print "</td></tr>";
		}

#		<tr><td colspan=3><input name="Cmode" type=submit value="âí" onClick="return checkTeisen()"></td>

	print "</tr></table>";

	print << "	-----END-----";
	<script language="JavaScript">
		function ChMn(msg,mny){
			if (mny > $CL_VALUES[1]){alert('àª«èÜ¹ñB');return false;}
			if (confirm(msg+'µÜ·B\\nïp('+mny+')\\næëµ¢Å·©H') == true){
				return true;}else{return false;}
		}
		function checkYosai(){
			if (document.Ms.yoname.value == ''){window.alert("vÇ¼ªLü³êÄ¢Ü¹ñB");return false;
			}else if(document.Ms.yoname.value.match('[&! ?=.,*<>"\\'/¥±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜ¦Ý§¨©ª«¯~@ABCDEFGHIJKLMNOPQRSßçãÛÚæ¿¾ú\ú^ú`úbúdú~úú¡ú£úªú±ú²TUVWXYZ[]]') != null) {
				window.alert("¾[ßÁI");return false;
			}else if (confirm('vÇ¼ðÏXµÜ·Bïp(10000)æëµ¢Å·©') == true){return true;
			}else{return false}
		}
		function checkTeisen(){
			if (confirm('âíµÜ·Bæëµ¢Å·©H@(¦©Ìâíðs¢Ü·B)') == true){return true;
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
	&ERROR('COOKIEª³øÉÈÁÄ¢Ü·B') if !$COOKIE{'pname'};
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&DBM_CONVERT('C',"$PL_VALUES[5]");
	sub FR {"<option value=\"$Key\">$Key"}
	print << "	-----END-----";
	<script language="JavaScript">
		function checkmahou(anti1,anti2){
			if (anti2 > $CL_VALUES[1]){alert('ïª«èÜ¹ñB');return false;}
			if (confirm(anti1+'ðgpµÜ·B\\nïpi'+anti2+'j\\næëµ¢Å·©H') == true)
			{return true;}else{return false}
		}
	</script>
		<tr><td $BgColor><b>ïF\$ $CL_VALUES[1]</b><br><br><b>q[OEq[OI[EUNVEp_Cgp<br>
		ÎÛðIðµÄº³¢B¼Ìâ@ðg¤êÍ¢IðÅ\\¢Ü¹ñ</b><br>
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
		<tr><td $BgColor><b>q[OFÎÛ¯ÌHPð30ñAñ¾Æ³ø</b><br>
			&nbsp;&nbsp;\$2000<input name="Dmode" type=submit value="q[Ogp" onClick="return checkmahou('q[O','2000')"></td></tr>
		<tr><td $BgColor><b>q[OvXFoÂÉÈÁÄ¢é¯ÌHPð30ñ</b><br>
			&nbsp;&nbsp;\$15000<input name="Dmode" type=submit value="q[OvXgp" onClick="return checkmahou('q[OvX','15000')"></td></tr>
		<tr><td $BgColor><b>q[OI[FÎÛ¯ÌHPðSñAñ¾Æ³ø</b><br>
			&nbsp;&nbsp;\$5000<input name="Dmode" type=submit value="q[OI[gp" onClick="return checkmahou('q[OI[','4000')"></td></tr>
		<tr><td $BgColor><b>UNVFñÉÈÁÄ¢éÎÛ¯ðHPSñoÂ</b><br>
			&nbsp;&nbsp;\$10000<input name="Dmode" type=submit value="UNVgp" onClick="return checkmahou('UNV','10000')"></td></tr>
		<tr><td $BgColor><b>`[WXyF­Ñ¢MP+1000</b><br>
			&nbsp;&nbsp;\$50000<input name="Dmode" type=submit value="`[WXygp" onClick="return checkmahou('`[WXy','50000')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] == 1);
		<tr><td $BgColor><b>}[eBCYFñÉÈÁÄ¢é¯ð»ÝHP»ÌÜÜÅoÂÉµÜ·<br>
		­® ÀÍÌÝ</b><br>
			&nbsp;&nbsp;\$80000<input name="Dmode" type=submit value="}[eBCYgp" onClick="return checkmahou('}[eBCY','80000')"></td></tr>
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
#	&ERROR('COOKIEª³øÉÈÁÄ¢Ü·B') if !$COOKIE{'pname'};
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
	#nCGt@gÌêÌÝºLG[ÎÛO
	&ERROR('ÎÛª èÜ¹ñB') if !$op && $CL_VALUES[15] ne "f" && $MENTE!=1;
	print "<input type=hidden name=cardCheck value=$DATE>";
	print << "	-----END-----";
	<script language="JavaScript">
		function checkcard1(anti3){
			if (confirm(anti3+'ðgpµÜ·Bæëµ¢Å·©H') == true)
			{return true;}else{return false}
		}
		function checkcard2(anti3){
			if (confirm('J[hðjüµÜ·Bæëµ¢Å·©H') == true)
			{return true;}else{return false}
		}
	</script>
		<tr><td $BgColor><b>ÎÛIð</b><br>
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
		<input name="Emode" type=submit value="J[hjü" onClick="return checkcard2('J[hjü')">
		</td></td></tr></table></td></tr>
	-----END-----
	}

	print << "	-----END-----" if ($MENTE==1);#Çlêp
		<tr><td $BgColor><table style="font-size:10pt;"><tr><td>
		<img src="$IMG_FOLDER6/20.gif"></td><td valign=top width=100% $BgColor>
		<b><font size=4>fobO1</font>
		<hr color="$TABLE_BORDER">©jbgÈOðJXg³¹Ü·</b>
		<br><br><input name="Emode" type=submit value="fobO1" onClick="return checkcard('fobO1')">
		</td></td></tr></table></td></tr>
	-----END-----
	print << "	-----END-----" if ($MENTE==1);#Çlêp
		<tr><td $BgColor><table style="font-size:10pt;"><tr><td>
		<img src="$IMG_FOLDER6/20.gif"></td><td valign=top width=100% $BgColor>
		<b><font size=4>fobO2</font>
		<hr color="$TABLE_BORDER">©jbgÈOÌ»ÝHPð1000ÉµÜ·</b>
		<br><br><input name="Emode" type=submit value="fobO2" onClick="return checkcard('fobO2')">
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
#	&ERROR('COOKIEª³øÉÈÁÄ¢Ü·B') if !$COOKIE{'pname'};
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	print << "	-----END-----";
	<script language="JavaScript">
		function checkCustom(){
			if (confirm('ÏXµÜ·Bæëµ¢Å·©H') == true)
			{return true;}else{return false}
		}
	</script>
		<tr><td $BgColor><b>í¬ÌACRðNXæÉÏXµÜ·</b><br>
	-----END-----
		print "<input type=\"radio\" name=\"unitColor\" value=1";
	        print " checked" if $PL_VALUES[36] == 1;
	        print ">·é\n";
		print "<input type=\"radio\" name=\"unitColor\" value=0";
	        print " checked" if $PL_VALUES[36] == 0;
	        print ">µÈ¢<input name=\"Cmode\" type=submit value=\"ACR`FW\" onClick=\"return checkCustom()\"></td></tr>\n";

	if($PL_VALUES[24] > 1000){$AMA=$PL_VALUES[24]-1000;}
		print "<tr><td $BgColor>\n";
		print "»ÝÌnûxc".&STATUS_CONVERT("$PL_VALUES[24]",'j')."+$AMA<br>\n" if $PL_VALUES[24] > 1000;
		print "NX`FWñc$PL_VALUES[23]</td></tr>\n";

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
		print "<tr><td $BgColor><b>»ÝÌNXEíðüêÖ¦Ü·</b>\n";
		print "<dl><dt>NX</dt><dd>$class[0]</dd><dt>Gg<dt><dd>".&STATUS_CONVERT("$souko[4]",'e')."</dd><dt>nûx</dt><dd>$souko[5]</dd><dt>õ1</dt><dd>$WN_sA[0] Lv.$WLV_A/exp.$WEP_A</dd>";
		print "<dt>õ2</dt><dd>$WN_sB[0] Lv.$WLV_B/exp.$WEP_B</dd>" if $souko[2];
		print "<dt>õ3</dt><dd>$WN_sC[0] Lv.$WLV_C/exp.$WEP_C</dd>" if $souko[3];
		print "</dl>";
		print "<input name=\"Cmode\" type=submit value=\"qÉüêÖ¦\" onClick=\"return checkCustom()\"></td></tr>\n";
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
#	&ERROR('COOKIEª³øÉÈÁÄ¢Ü·B') if !$COOKIE{'pname'};

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
#				<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[5]Abv\" $STYLE_B1 onClick='return checkEn()'></td>
#				&nbsp;&nbsp;ÁïMP600<input name="Cmode" type=submit value=\"$DELE[0]\" onClick="return checkmahou('ftn[l')"></td></tr>
	sub FR {"<option value=\"$Key\">$Key"}
	print << "	-----END-----";
	<script language="JavaScript">
		function checkmahou(anti1){
			if (confirm(anti1+'ðgpµÜ·B\\næëµ¢Å·©H') == true)
			{return true;}else{return false}
		}
	</script>
	-----END-----
print "<input type=hidden name=mahouCheck value=$DATE>";
	print << "	-----END-----";
</td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006a/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>vCn[lF©gÌ®·éàSõÉøÊB960bÔA®«UÍ+20@ån®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP400<input name="Xmode" type=submit value="vCn[l" onClick="return checkmahou('vCn[l')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006b/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>vC]VlF©gÌ®·éàSõÉøÊB960bÔA®«UÍ+20@®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP400<input name="Xmode" type=submit value="vC]Vl" onClick="return checkmahou('vC]Vl')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006c/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>vCo[TF©gÌ®·éàSõÉøÊB960bÔAån®«UÍ+20@®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP400<input name="Xmode" type=submit value="vCo[T" onClick="return checkmahou('vCo[T')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && $ALY_CLASS[17] =~ m/!E006d/ && $PL_VALUES[17] >= 400 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>vCO[UF©gÌ®·éàSõÉøÊB960bÔA®«UÍ+20@®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP400<input name="Xmode" type=submit value="vCO[U" onClick="return checkmahou('vCO[U')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!83/ || $WN_sT[7] =~ m/!83/ ||$WN_sU[7] =~ m/!83/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>ftn[lF©gÌ®·éàSõÉøÊB960bÔA®«UÍ+20@ån®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP600<input name="Xmode" type=submit value="ftn[l" onClick="return checkmahou('ftn[l')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!84/ || $WN_sT[7] =~ m/!84/ ||$WN_sU[7] =~ m/!84/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>ft]VlF©gÌ®·éàSõÉøÊB960bÔA®«UÍ+20@®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP600<input name="Xmode" type=submit value="ft]Vl" onClick="return checkmahou('ft]Vl')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!85/ || $WN_sT[7] =~ m/!85/ ||$WN_sU[7] =~ m/!85/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>fto[TF©gÌ®·éàSõÉøÊB960bÔAån®«UÍ+20@®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP600<input name="Xmode" type=submit value="fto[T" onClick="return checkmahou('fto[T')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[6] != 0 && ($WN_sS[7] =~ m/!86/ || $WN_sT[7] =~ m/!86/ ||$WN_sU[7] =~ m/!86/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>ftO[UF©gÌ®·éàSõÉøÊB960bÔA®«UÍ+20@®«häÍ+20</b><br>
				&nbsp;&nbsp;ÁïMP600<input name="Xmode" type=submit value="ftO[U" onClick="return checkmahou('ftO[U')"></td></tr>
	-----END-----
	print << "	-----END-----" if (($WN_sS[7] =~ m/!8i/ || $WN_sT[7] =~ m/!8i/ ||$WN_sU[7] =~ m/!8i/) && $PL_VALUES[17] >= 600 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>}[V[CF©gÌ®·éàSõÌHPðÅågoÌ20ªAgoñµÜ·B(jbgGgª®«ÌêÍñÊ+10)</b><br>
				&nbsp;&nbsp;ÁïMP600<input name="Xmode" type=submit value="}[V[C" onClick="return checkmahou('}[V[C')"></td></tr>
	-----END-----
	print << "	-----END-----" if (($WN_sS[7] =~ m/!8j/ || $WN_sT[7] =~ m/!8j/ ||$WN_sU[7] =~ m/!8j/) && $PL_VALUES[17] >= 1500 && $PL_VALUES[25] ne "1");
			<tr><td $BgColor><b>}[eBCYF©gÌ®·éàSõÌí¬s\\ñB­®ãAgpÒÍí¬s\\ÉÈèÜ·B</b><br>
				&nbsp;&nbsp;ÁïMP1500<input name="Xmode" type=submit value="}[eBCY" onClick="return checkmahou('}[eBCY')"></td></tr>
	-----END-----
	print << "	-----END-----" if ($PL_VALUES[25] eq "1");
			<tr><td $BgColor><b>í¬s\\ÍAâ@ðsgÅ«Ü¹ñB</b></td></tr>
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
	if (document.Ms.MsName.value == ''){window.alert("R[hl[ª¢LüÅ·B");return false;
	}else if(document.Ms.MsName.value.match('[&! ?=.,*<>"\\'/¥±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜ¦Ý§¨©ª«¯~@ABCDEFGHIJKLMNOPQRSßçãÛÚæ¿¾ú\ú^ú`úbúdú~úú¡ú£úªú±ú²TUVWXYZ[]]') != null) {
		window.alert("¾[ßÁI");return false;
	}else if (confirm('`FWµÜ·Bæëµ¢Å·©H') == true){return true;
	}else{return false}
	}
	</script>
	-----END-----
	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/classchange.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">ACR`FWI</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";

	print "<tr><td style=\"padding-top:8px;\">jbgACR<img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" name=\"msImg\"></td></tr>\n";
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

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">LN^ACR<img src=\"$IMG_FOLDER7/$PL_VALUES[40].gif\" name=\"msImg2\"></td></tr>\n";
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

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">R[hl[</td></tr>\n";
	print "<tr><td style=\"padding-left:10px;\"><input type=text name=MsName size=30 maxlength=15 value=$PL_VALUES[3] $STYLE_L></td></tr>\n";

	print "</td></tr>\n<tr><td style=\"padding-top:8px;\">FÏX";
	print "</td></tr>\n<tr><td style=\"padding-left:10px;\"><select name=MsColor>";
	foreach (@COLOR){
		print "<option value=\"$_\"";
        	print " selected\n" if $_ =~ /$PL_VALUES[13]/i;
        	print " style=\"color:#$_\">¡$_\n";
	}
	print "</select></td></tr>\n<tr align=\"right\"><td style=\"padding-left:10px;\">";
	print "<input name=\"Cmode\" type=submit value=\"`FW\" onClick=\"return checkCustom()\">\n";
	print "</td></tr>\n</table>\n";
	}


	print "</td></tr>\n";
	print "</form></table>\n";

	&FOOTER;
}
1;

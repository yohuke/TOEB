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
sub EQUIP {
	&CUSTOM_HEADER('Main');
	require "./$LOG_FOLDER/$HASH_DATA";
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&UNLOCK;
#	local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#	local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#	local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#	local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);

	local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);
	local($WN_B,$WLV_B,$WBEnt,$WB03,$WB04,$WB05,$WB06,$WB07,$WB08,$WB09,$WB10,$WB11,$WB12,$WB13,$WB14,$WB15,$WB16,$WB17,$WB18,$WB19,$WB20,$WB21,$WB22,$WB23,$WB24,$WB25,$WB26,$WB27,$WB28,$WB29,$WB30,$WB31,$WB32,$WB33,$WB34,$WB35,$WB36,$WB37,$WB38,$WB39,$WB40,$WB41,$WB42) = split(/!/,$PL_VALUES[10]);
	local($WN_C,$WLV_C,$WCEnt,$WC03,$WC04,$WC05,$WC06,$WC07,$WC08,$WC09,$WC10,$WC11,$WC12,$WC13,$WC14,$WC15,$WC16,$WC17,$WC18,$WC19,$WC20,$WC21,$WC22,$WC23,$WC24,$WC25,$WC26,$WC27,$WC28,$WC29,$WC30,$WC31,$WC32,$WC33,$WC34,$WC35,$WC36,$WC37,$WC38,$WC39,$WC40,$WC41,$WC42) = split(/!/,$PL_VALUES[11]);
	local($WN_D,$WLV_D,$WDEnt,$WD03,$WD04,$WD05,$WD06,$WD07,$WD08,$WD09,$WD10,$WD11,$WD12,$WD13,$WD14,$WD15,$WD16,$WD17,$WD18,$WD19,$WD20,$WD21,$WD22,$WD23,$WD24,$WD25,$WD26,$WD27,$WD28,$WD29,$WD30,$WD31,$WD32,$WD33,$WD34,$WD35,$WD36,$WD37,$WD38,$WD39,$WD40,$WD41,$WD42) = split(/!/,$PL_VALUES[38]);

	local($WN_S,$WLV_S,$WSEnt) = split(/!/,$PL_VALUES[41]);
	local($WN_T,$WLV_T,$WTEnt) = split(/!/,$PL_VALUES[42]);
	local($WN_U,$WLV_U,$WUEnt) = split(/!/,$PL_VALUES[43]);
#	local($WN_Y,$WLV_Y) = split(/!/,$PL_VALUES[46]);
	local($WN_Y,$WLV_Y,$WYEnt,$WY03,$WY04,$WY05,$WY06,$WY07,$WY08,$WY09,$WY10,$WY11,$WY12,$WY13,$WY14,$WY15,$WY16,$WY17,$WY18,$WY19,$WY20,$WY21,$WY22,$WY23,$WY24,$WY25,$WY26,$WY27,$WY28,$WY29,$WY30,$WY31,$WY32,$WY33,$WY34,$WY35,$WY36,$WY37,$WY38,$WY39,$WY40,$WY41,$WY42) = split(/!/,$PL_VALUES[46]);

	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
	@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
	@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
	@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});
	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
	@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
	@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});
	@WN_sY=split(/\,/,$WEAPON_LIST{"$WN_Y"});
	$WLV_A=int $WLV_A/$WEAPON_LVUP;
	$WLV_B=int $WLV_B/$WEAPON_LVUP;
	$WLV_C=int $WLV_C/$WEAPON_LVUP;
	$WLV_D=int $WLV_D/$WEAPON_LVUP;
	$WLV_S=int $WLV_S/$WEAPON_LVUP;
	$WLV_T=int $WLV_T/$WEAPON_LVUP;
	$WLV_U=int $WLV_U/$WEAPON_LVUP;
	$WLV_Y=int $WLV_Y/$WEAPON_LVUP;

##紀律の地メルフィ
if(($TIME[3]==1 && $TIME[2]>=9 && $TIME[2]<=21) || ($TIME[3]==6 && $TIME[2]>=9 && $TIME[2]<=21) || ($TIME[3]==15 && $TIME[2]>=9 && $TIME[2]<=21) || ($TIME[3]==21 && $TIME[2]>=9 && $TIME[2]<=21)){
	$merufi=1;
}else{
	$merufi=0;
	if($melchan eq "1"){$merufi=1;}
}

#	$merufi=1;


$matiname="ショップ";
if($merufi==1 && $PL_VALUES[5] eq ""){$matiname="～紀律の地メルフィ～<br>&nbsp;&nbsp;<img src=\"$IMG_FOLDER1/mel.gif\"><br><br>武器購入";}
##武器ID消失
	&JScfm(checkmiss,"該当装備欄を修復します。よろしいですか？");
	if($PL_VALUES[9]){
		unless (exists $WEAPON_LIST{"$WN_A"}){
		print "<tr><td $BgColor>装備1は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=武器修復1 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
	if($PL_VALUES[10]){
		unless (exists $WEAPON_LIST{"$WN_B"}){
		print "<tr><td $BgColor>装備2は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=武器修復2 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
	if($PL_VALUES[11]){
		unless (exists $WEAPON_LIST{"$WN_C"}){
		print "<tr><td $BgColor>装備3は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=武器修復3 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
	if($PL_VALUES[38]){
		unless (exists $WEAPON_LIST{"$WN_D"}){
		print "<tr><td $BgColor>装備4は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=武器修復4 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
	if($PL_VALUES[41]){
		unless (exists $WEAPON_LIST{"$WN_S"}){
		print "<tr><td $BgColor>特殊1は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=特殊修復1 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
	if($PL_VALUES[42]){
		unless (exists $WEAPON_LIST{"$WN_T"}){
		print "<tr><td $BgColor>特殊2は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=特殊修復2 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
	if($PL_VALUES[43]){
		unless (exists $WEAPON_LIST{"$WN_U"}){
		print "<tr><td $BgColor>特殊3は壊れているか存在しません。<br>";
		print "<input name=\"Cmode\" type=submit value=特殊修復3 onClick=\"return checkmiss()\"></td></tr>\n";
		}
	}
##装備一覧
	if($WA03 ne ""){$WN_sA[7] .= "!ENTSTR00$WA03";$WN_sA[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WA04 ne ""){$WN_sA[7] .= "!ENTVIT00$WA04";$WN_sA[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WA05 ne ""){$WN_sA[7] .= "!ENTAGI00$WA05";$WN_sA[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WA06 ne ""){$WN_sA[7] .= "!ENTDEX00$WA06";$WN_sA[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WA07 ne ""){$WN_sA[7] .= "!ENTLIF00$WA07";$WN_sA[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WA08 ne ""){$WN_sA[7] .= "!ENTMBU00$WA08";$WN_sA[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WA09 ne ""){$WN_sA[7] .= "!ENTNKI00$WA09";$WN_sA[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WA10 ne ""){$WN_sA[7] .= "!ENTNGU00$WA10";$WN_sA[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WA11 ne ""){$WN_sA[7] .= "!ENTTUP00$WA11";$WN_sA[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WA12 ne ""){$WN_sA[7] .= "!ENTMFU00$WA12";$WN_sA[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WA13 ne ""){$WN_sA[7] .= "!ENTRES00$WA13";$WN_sA[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WA14 ne ""){$WN_sA[7] .= "!ENTFIB00$WA14";$WN_sA[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WA15 ne ""){$WN_sA[7] .= "!ENTWAB00$WA15";$WN_sA[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WA16 ne ""){$WN_sA[7] .= "!ENTEAB00$WA16";$WN_sA[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WA17 ne ""){$WN_sA[7] .= "!ENTWIB00$WA17";$WN_sA[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WA18 ne ""){$WN_sA[7] .= "!ENTSAB00$WA18";$WN_sA[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WA19 ne ""){$WN_sA[7] .= "!ENTDAB00$WA19";$WN_sA[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WA20 ne ""){$WN_sA[7] .= "!ENTFIG00$WA20";$WN_sA[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WA21 ne ""){$WN_sA[7] .= "!ENTWAG00$WA21";$WN_sA[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WA22 ne ""){$WN_sA[7] .= "!ENTEAG00$WA22";$WN_sA[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WA23 ne ""){$WN_sA[7] .= "!ENTWIG00$WA23";$WN_sA[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WA24 ne ""){$WN_sA[7] .= "!ENTSAG00$WA24";$WN_sA[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WA25 ne ""){$WN_sA[7] .= "!ENTDAG00$WA25";$WN_sA[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WA26 ne ""){$WN_sA[7] .= "!ENTIMG00$WA26";$WN_sA[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WA27 ne ""){$WN_sA[7] .= "!ENTGOU00$WA27";$WN_sA[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WA28 ne ""){$WN_sA[7] .= "!ENTHHP00$WA28";$WN_sA[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WA29 ne ""){$WN_sA[7] .= "!ENTMMP00$WA29";$WN_sA[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WA30 ne ""){$WN_sA[7] .= "!ENTDAM00$WA30";$WN_sA[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WA31 ne ""){$WN_sA[7] .= "!ENTHEA00$WA31";$WN_sA[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WA32 ne ""){$WN_sA[7] .= "!ENTCRI00$WA32";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WA33 ne ""){$WN_sA[7] .= "!ENTBRK00$WA33";$WN_sA[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WB03 ne ""){$WN_sB[7] .= "!ENTSTR00$WB03";$WN_sB[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WB04 ne ""){$WN_sB[7] .= "!ENTVIT00$WB04";$WN_sB[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WB05 ne ""){$WN_sB[7] .= "!ENTAGI00$WB05";$WN_sB[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WB06 ne ""){$WN_sB[7] .= "!ENTDEX00$WB06";$WN_sB[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WB07 ne ""){$WN_sB[7] .= "!ENTLIF00$WB07";$WN_sB[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WB08 ne ""){$WN_sB[7] .= "!ENTMBU00$WB08";$WN_sB[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WB09 ne ""){$WN_sB[7] .= "!ENTNKI00$WB09";$WN_sB[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WB10 ne ""){$WN_sB[7] .= "!ENTNGU00$WB10";$WN_sB[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WB11 ne ""){$WN_sB[7] .= "!ENTTUP00$WB11";$WN_sB[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WB12 ne ""){$WN_sB[7] .= "!ENTMFU00$WB12";$WN_sB[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WB13 ne ""){$WN_sB[7] .= "!ENTRES00$WB13";$WN_sB[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WB14 ne ""){$WN_sB[7] .= "!ENTFIB00$WB14";$WN_sB[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WB15 ne ""){$WN_sB[7] .= "!ENTWAB00$WB15";$WN_sB[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WB16 ne ""){$WN_sB[7] .= "!ENTEAB00$WB16";$WN_sB[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WB17 ne ""){$WN_sB[7] .= "!ENTWIB00$WB17";$WN_sB[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WB18 ne ""){$WN_sB[7] .= "!ENTSAB00$WB18";$WN_sB[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WB19 ne ""){$WN_sB[7] .= "!ENTDAB00$WB19";$WN_sB[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WB20 ne ""){$WN_sB[7] .= "!ENTFIG00$WB20";$WN_sB[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WB21 ne ""){$WN_sB[7] .= "!ENTWAG00$WB21";$WN_sB[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WB22 ne ""){$WN_sB[7] .= "!ENTEAG00$WB22";$WN_sB[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WB23 ne ""){$WN_sB[7] .= "!ENTWIG00$WB23";$WN_sB[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WB24 ne ""){$WN_sB[7] .= "!ENTSAG00$WB24";$WN_sB[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WB25 ne ""){$WN_sB[7] .= "!ENTDAG00$WB25";$WN_sB[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WB26 ne ""){$WN_sB[7] .= "!ENTIMG00$WB26";$WN_sB[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WB27 ne ""){$WN_sB[7] .= "!ENTGOU00$WB27";$WN_sB[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WB28 ne ""){$WN_sB[7] .= "!ENTHHP00$WB28";$WN_sB[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WB29 ne ""){$WN_sB[7] .= "!ENTMMP00$WB29";$WN_sB[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WB30 ne ""){$WN_sB[7] .= "!ENTDAM00$WB30";$WN_sB[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WB31 ne ""){$WN_sB[7] .= "!ENTHEA00$WB31";$WN_sB[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WB32 ne ""){$WN_sB[7] .= "!ENTCRI00$WB32";$WN_sB[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WB33 ne ""){$WN_sB[7] .= "!ENTBRK00$WB33";$WN_sB[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WC03 ne ""){$WN_sC[7] .= "!ENTSTR00$WC03";$WN_sC[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WC04 ne ""){$WN_sC[7] .= "!ENTVIT00$WC04";$WN_sC[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WC05 ne ""){$WN_sC[7] .= "!ENTAGI00$WC05";$WN_sC[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WC06 ne ""){$WN_sC[7] .= "!ENTDEX00$WC06";$WN_sC[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WC07 ne ""){$WN_sC[7] .= "!ENTLIF00$WC07";$WN_sC[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WC08 ne ""){$WN_sC[7] .= "!ENTMBU00$WC08";$WN_sC[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WC09 ne ""){$WN_sC[7] .= "!ENTNKI00$WC09";$WN_sC[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WC10 ne ""){$WN_sC[7] .= "!ENTNGU00$WC10";$WN_sC[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WC11 ne ""){$WN_sC[7] .= "!ENTTUP00$WC11";$WN_sC[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WC12 ne ""){$WN_sC[7] .= "!ENTMFU00$WC12";$WN_sC[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WC13 ne ""){$WN_sC[7] .= "!ENTRES00$WC13";$WN_sC[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WC14 ne ""){$WN_sC[7] .= "!ENTFIB00$WC14";$WN_sC[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WC15 ne ""){$WN_sC[7] .= "!ENTWAB00$WC15";$WN_sC[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WC16 ne ""){$WN_sC[7] .= "!ENTEAB00$WC16";$WN_sC[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WC17 ne ""){$WN_sC[7] .= "!ENTWIB00$WC17";$WN_sC[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WC18 ne ""){$WN_sC[7] .= "!ENTSAB00$WC18";$WN_sC[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WC19 ne ""){$WN_sC[7] .= "!ENTDAB00$WC19";$WN_sC[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WC20 ne ""){$WN_sC[7] .= "!ENTFIG00$WC20";$WN_sC[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WC21 ne ""){$WN_sC[7] .= "!ENTWAG00$WC21";$WN_sC[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WC22 ne ""){$WN_sC[7] .= "!ENTEAG00$WC22";$WN_sC[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WC23 ne ""){$WN_sC[7] .= "!ENTWIG00$WC23";$WN_sC[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WC24 ne ""){$WN_sC[7] .= "!ENTSAG00$WC24";$WN_sC[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WC25 ne ""){$WN_sC[7] .= "!ENTDAG00$WC25";$WN_sC[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WC26 ne ""){$WN_sC[7] .= "!ENTIMG00$WC26";$WN_sC[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WC27 ne ""){$WN_sC[7] .= "!ENTGOU00$WC27";$WN_sC[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WC28 ne ""){$WN_sC[7] .= "!ENTHHP00$WC28";$WN_sC[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WC29 ne ""){$WN_sC[7] .= "!ENTMMP00$WC29";$WN_sC[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WC30 ne ""){$WN_sC[7] .= "!ENTDAM00$WC30";$WN_sC[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WC31 ne ""){$WN_sC[7] .= "!ENTHEA00$WC31";$WN_sC[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WC32 ne ""){$WN_sC[7] .= "!ENTCRI00$WC32";$WN_sC[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WC33 ne ""){$WN_sC[7] .= "!ENTBRK00$WC33";$WN_sC[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WD03 ne ""){$WN_sD[7] .= "!ENTSTR00$WD03";$WN_sD[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WD04 ne ""){$WN_sD[7] .= "!ENTVIT00$WD04";$WN_sD[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WD05 ne ""){$WN_sD[7] .= "!ENTAGI00$WD05";$WN_sD[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WD06 ne ""){$WN_sD[7] .= "!ENTDEX00$WD06";$WN_sD[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WD07 ne ""){$WN_sD[7] .= "!ENTLIF00$WD07";$WN_sD[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WD08 ne ""){$WN_sD[7] .= "!ENTMBU00$WD08";$WN_sD[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WD09 ne ""){$WN_sD[7] .= "!ENTNKI00$WD09";$WN_sD[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WD10 ne ""){$WN_sD[7] .= "!ENTNGU00$WD10";$WN_sD[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WD11 ne ""){$WN_sD[7] .= "!ENTTUP00$WD11";$WN_sD[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WD12 ne ""){$WN_sD[7] .= "!ENTMFU00$WD12";$WN_sD[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WD13 ne ""){$WN_sD[7] .= "!ENTRES00$WD13";$WN_sD[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WD14 ne ""){$WN_sD[7] .= "!ENTFIB00$WD14";$WN_sD[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WD15 ne ""){$WN_sD[7] .= "!ENTWAB00$WD15";$WN_sD[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WD16 ne ""){$WN_sD[7] .= "!ENTEAB00$WD16";$WN_sD[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WD17 ne ""){$WN_sD[7] .= "!ENTWIB00$WD17";$WN_sD[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WD18 ne ""){$WN_sD[7] .= "!ENTSAB00$WD18";$WN_sD[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WD19 ne ""){$WN_sD[7] .= "!ENTDAB00$WD19";$WN_sD[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WD20 ne ""){$WN_sD[7] .= "!ENTFIG00$WD20";$WN_sD[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WD21 ne ""){$WN_sD[7] .= "!ENTWAG00$WD21";$WN_sD[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WD22 ne ""){$WN_sD[7] .= "!ENTEAG00$WD22";$WN_sD[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WD23 ne ""){$WN_sD[7] .= "!ENTWIG00$WD23";$WN_sD[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WD24 ne ""){$WN_sD[7] .= "!ENTSAG00$WD24";$WN_sD[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WD25 ne ""){$WN_sD[7] .= "!ENTDAG00$WD25";$WN_sD[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WD26 ne ""){$WN_sD[7] .= "!ENTIMG00$WD26";$WN_sD[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WD27 ne ""){$WN_sD[7] .= "!ENTGOU00$WD27";$WN_sD[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WD28 ne ""){$WN_sD[7] .= "!ENTHHP00$WD28";$WN_sD[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WD29 ne ""){$WN_sD[7] .= "!ENTMMP00$WD29";$WN_sD[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WD30 ne ""){$WN_sD[7] .= "!ENTDAM00$WD30";$WN_sD[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WD31 ne ""){$WN_sD[7] .= "!ENTHEA00$WD31";$WN_sD[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WD32 ne ""){$WN_sD[7] .= "!ENTCRI00$WD32";$WN_sD[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WD33 ne ""){$WN_sD[7] .= "!ENTBRK00$WD33";$WN_sD[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WY03 ne ""){$WN_sY[7] .= "!ENTSTR00$WY03";$WN_sY[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WY04 ne ""){$WN_sY[7] .= "!ENTVIT00$WY04";$WN_sY[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WY05 ne ""){$WN_sY[7] .= "!ENTAGI00$WY05";$WN_sY[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WY06 ne ""){$WN_sY[7] .= "!ENTDEX00$WY06";$WN_sY[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WY07 ne ""){$WN_sY[7] .= "!ENTLIF00$WY07";$WN_sY[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WY08 ne ""){$WN_sY[7] .= "!ENTMBU00$WY08";$WN_sY[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WY09 ne ""){$WN_sY[7] .= "!ENTNKI00$WY09";$WN_sY[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WY10 ne ""){$WN_sY[7] .= "!ENTNGU00$WY10";$WN_sY[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WY11 ne ""){$WN_sY[7] .= "!ENTTUP00$WY11";$WN_sY[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WY12 ne ""){$WN_sY[7] .= "!ENTMFU00$WY12";$WN_sY[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WY13 ne ""){$WN_sY[7] .= "!ENTRES00$WY13";$WN_sY[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WY14 ne ""){$WN_sY[7] .= "!ENTFIB00$WY14";$WN_sY[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WY15 ne ""){$WN_sY[7] .= "!ENTWAB00$WY15";$WN_sY[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WY16 ne ""){$WN_sY[7] .= "!ENTEAB00$WY16";$WN_sY[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WY17 ne ""){$WN_sY[7] .= "!ENTWIB00$WY17";$WN_sY[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WY18 ne ""){$WN_sY[7] .= "!ENTSAB00$WY18";$WN_sY[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WY19 ne ""){$WN_sY[7] .= "!ENTDAB00$WY19";$WN_sY[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WY20 ne ""){$WN_sY[7] .= "!ENTFIG00$WY20";$WN_sY[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WY21 ne ""){$WN_sY[7] .= "!ENTWAG00$WY21";$WN_sY[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WY22 ne ""){$WN_sY[7] .= "!ENTEAG00$WY22";$WN_sY[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WY23 ne ""){$WN_sY[7] .= "!ENTWIG00$WY23";$WN_sY[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WY24 ne ""){$WN_sY[7] .= "!ENTSAG00$WY24";$WN_sY[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WY25 ne ""){$WN_sY[7] .= "!ENTDAG00$WY25";$WN_sY[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WY26 ne ""){$WN_sY[7] .= "!ENTIMG00$WY26";$WN_sY[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WY27 ne ""){$WN_sY[7] .= "!ENTGOU00$WY27";$WN_sY[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WY28 ne ""){$WN_sY[7] .= "!ENTHHP00$WY28";$WN_sY[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WY29 ne ""){$WN_sY[7] .= "!ENTMMP00$WY29";$WN_sY[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WY30 ne ""){$WN_sY[7] .= "!ENTDAM00$WY30";$WN_sY[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WY31 ne ""){$WN_sY[7] .= "!ENTHEA00$WY31";$WN_sY[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WY32 ne ""){$WN_sY[7] .= "!ENTCRI00$WY32";$WN_sY[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WY33 ne ""){$WN_sY[7] .= "!ENTBRK00$WY33";$WN_sY[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}


	$Pl_WeaponNameA2="$WN_sA[0](Lv$WLV_A)";
	$Pl_WeaponNameB2="$WN_sB[0](Lv$WLV_B)";
	$Pl_WeaponNameC2="$WN_sC[0](Lv$WLV_C)";
	$Pl_WeaponNameD2="$WN_sD[0](Lv$WLV_D)";
	$Pl_WeaponNameS2="$WN_sS[0](Lv$WLV_S)";
	$Pl_WeaponNameT2="$WN_sT[0](Lv$WLV_T)";
	$Pl_WeaponNameU2="$WN_sU[0](Lv$WLV_U)";
	$Pl_WeaponNameY2="$WN_sY[0](Lv$WLV_Y)";


	#エンチャントによる装備品の名称色変更
	#最上段
	@Count_A = split(/!/,$PL_VALUES[9]);
	$Ent_A = 0;
	for ($LngEntCntA = 3; $LngEntCntA <= 33; $LngEntCntA++){
		if($Count_A[$LngEntCntA] > 0){$Ent_A = $Ent_A + 1;}
	}
	if($Ent_A > 0 && $Ent_A <= 2){$WN_sA[0] = "<font color=00ff00>$WN_sA[0]</font>";}
	elsif($Ent_A > 2 && $Ent_A <= 4){$WN_sA[0] = "<font color=ffff00>$WN_sA[0]</font>";}
	elsif($Ent_A > 4){$WN_sA[0] = "<font color=ffD700>$WN_sA[0]</font>";}
	#2段目
	@Count_B = split(/!/,$PL_VALUES[10]);
	$Ent_B = 0;
	for ($LngEntCntB = 3; $LngEntCntB <= 33; $LngEntCntB++){
		if($Count_B[$LngEntCntB] > 0){$Ent_B = $Ent_B + 1;}
	}
	if($Ent_B > 0 && $Ent_B <= 2){$WN_sB[0] = "<font color=00ff00>$WN_sB[0]</font>";}
	elsif($Ent_B > 2 && $Ent_B <= 4){$WN_sB[0] = "<font color=ffff00>$WN_sB[0]</font>";}
	elsif($Ent_B > 4){$WN_sB[0] = "<font color=ffD700>$WN_sB[0]</font>";}
	#3段目
	@Count_C = split(/!/,$PL_VALUES[11]);
	$Ent_C = 0;
	for ($LngEntCntC = 3; $LngEntCntC <= 33; $LngEntCntC++){
		if($Count_C[$LngEntCntC] > 0){$Ent_C = $Ent_C + 1;}
	}
	if($Ent_C > 0 && $Ent_C <= 2){$WN_sC[0] = "<font color=00ff00>$WN_sC[0]</font>";}
	elsif($Ent_C > 2 && $Ent_C <= 4){$WN_sC[0] = "<font color=ffff00>$WN_sC[0]</font>";}
	elsif($Ent_C > 4){$WN_sC[0] = "<font color=ffD700>$WN_sC[0]</font>";}
	#4段目
	@Count_D = split(/!/,$PL_VALUES[38]);
	$Ent_D = 0;
	for ($LngEntCntD = 3; $LngEntCntD <= 33; $LngEntCntD++){
		if($Count_D[$LngEntCntD] > 0){$Ent_D = $Ent_D + 1;}
	}
	if($Ent_D > 0 && $Ent_D <= 2){$WN_sD[0] = "<font color=00ff00>$WN_sD[0]</font>";}
	elsif($Ent_D > 2 && $Ent_D <= 4){$WN_sD[0] = "<font color=ffff00>$WN_sD[0]</font>";}
	elsif($Ent_D > 4){$WN_sD[0] = "<font color=ffD700>$WN_sD[0]</font>";}

	#ストック
	@Count_Y = split(/!/,$PL_VALUES[46]);
	$Ent_Y = 0;
	for ($LngEntCntY = 3; $LngEntCntY <= 33; $LngEntCntY++){
		if($Count_Y[$LngEntCntY] > 0){$Ent_Y = $Ent_Y + 1;}
	}
	if($Ent_Y > 0 && $Ent_Y <= 2){$WN_sY[0] = "<font color=00ff00>$WN_sY[0]</font>";}
	elsif($Ent_Y > 2 && $Ent_Y <= 4){$WN_sY[0] = "<font color=ffff00>$WN_sY[0]</font>";}
	elsif($Ent_Y > 4){$WN_sY[0] = "<font color=ffD700>$WN_sY[0]</font>";}

	if($WAEnt ne "" && $WAEnt > 0){$WN_sA[0] = "＋$WAEnt $WN_sA[0]";}
	if($WBEnt ne "" && $WBEnt > 0){$WN_sB[0] = "＋$WBEnt $WN_sB[0]";}
	if($WCEnt ne "" && $WCEnt > 0){$WN_sC[0] = "＋$WCEnt $WN_sC[0]";}
	if($WDEnt ne "" && $WDEnt > 0){$WN_sD[0] = "＋$WDEnt $WN_sD[0]";}
	if($WSEnt ne "" && $WSEnt > 0){$WN_sS[0] = "＋$WSEnt $WN_sS[0]";}
	if($WTEnt ne "" && $WTEnt > 0){$WN_sT[0] = "＋$WTEnt $WN_sT[0]";}
	if($WUEnt ne "" && $WUEnt > 0){$WN_sU[0] = "＋$WUEnt $WN_sU[0]";}
	if($WYEnt ne "" && $WYEnt > 0){$WN_sY[0] = "＋$WYEnt $WN_sY[0]";}


	$Pl_WeaponNameA="$WN_sA[0](Lv$WLV_A)";
	$Pl_WeaponNameB="$WN_sB[0](Lv$WLV_B)";
	$Pl_WeaponNameC="$WN_sC[0](Lv$WLV_C)";
	$Pl_WeaponNameD="$WN_sD[0](Lv$WLV_D)";
	$Pl_WeaponNameS="$WN_sS[0](Lv$WLV_S)";
	$Pl_WeaponNameT="$WN_sT[0](Lv$WLV_T)";
	$Pl_WeaponNameU="$WN_sU[0](Lv$WLV_U)";
	$Pl_WeaponNameY="$WN_sY[0](Lv$WLV_Y)";


	$EntCnt = 0;
	@WN_sA_ef = split(/!/,$WN_sA[7]);
	foreach $j (@WN_sA_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sB_ef = split(/!/,$WN_sB[7]);
	foreach $j (@WN_sB_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq2 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq2 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu2 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sC_ef = split(/!/,$WN_sC[7]);
	foreach $j (@WN_sC_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq3 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq3 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu3 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sD_ef = split(/!/,$WN_sD[7]);
	foreach $j (@WN_sD_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq4 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq4 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu4 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sS_ef = split(/!/,$WN_sS[7]);
	foreach $j (@WN_sS_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq5 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq5 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu5 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sT_ef = split(/!/,$WN_sT[7]);
	foreach $j (@WN_sT_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq6 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq6 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu6 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sU_ef = split(/!/,$WN_sU[7]);
	foreach $j (@WN_sU_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq7 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq7 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu7 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sY_ef = split(/!/,$WN_sY[7]);
	foreach $j (@WN_sY_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq8 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq8 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu8 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">装備一覧</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
	print "<tr><td>$Pl_WeaponNameA 特性：$tokusyu $tokusyuuniq</td></tr>\n";
	if($WN_sB[0]){print "<tr><td>$Pl_WeaponNameB 特性：$tokusyu2 $tokusyuuniq2</td></tr>\n";}
	if($WN_sC[0]){print "<tr><td>$Pl_WeaponNameC 特性：$tokusyu3 $tokusyuuniq3</td></tr>\n";}
	if($WN_sD[0]){print "<tr><td>$Pl_WeaponNameD 特性：$tokusyu4 $tokusyuuniq4</td></tr>\n";}
	if($WN_sS[0]){print "<tr><td>$Pl_WeaponNameS 特性：$tokusyu5 $tokusyuuniq5</td></tr>\n";}
	if($WN_sT[0]){print "<tr><td>$Pl_WeaponNameT 特性：$tokusyu6 $tokusyuuniq6</td></tr>\n";}
	if($WN_sU[0]){print "<tr><td>$Pl_WeaponNameU 特性：$tokusyu7 $tokusyuuniq7</td></tr>\n";}
	if($WN_sY[0]){print "<tr><td>$Pl_WeaponNameY 特性：$tokusyu8 $tokusyuuniq8</td></tr>\n";}
	print "</table>\n";

##装備変更
	if ($WN_sB[0] || $WN_sC[0] || $WN_sD[0]){
		$PartofW="<select name=soubi>";
		if ($WN_sB[0] ne ""){$PartofW.="<option value=B>$Pl_WeaponNameB";}
		if ($WN_sC[0] ne ""){$PartofW.="<option value=C>$Pl_WeaponNameC";}
		if ($WN_sD[0] ne ""){$PartofW.="<option value=D>$Pl_WeaponNameD";}
		$PartofW.="</select><input type=submit name=Cmode value=装備 onClick=\"return checkEquip()\">";
		&JScfm(checkEquip,"装備を変更します。よろしいですか？");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">装備変更</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
		print "<tr><td>$Pl_WeaponNameA装備中</td></tr>\n";
		print "<tr><td style=\"padding-left:20px;\">$PartofW</td></tr></table>\n";

	}

#装備品ソート　10～38の3装備品の並び替えを行う
#		if(!$PL_VALUES[9]){
#			$Pl_WeaponNameA = "----------";
#		}
		if(!$PL_VALUES[10]){
			$Pl_WeaponNameB = "----------";
		}
		if(!$PL_VALUES[11]){
			$Pl_WeaponNameC = "----------";
		}
		if(!$PL_VALUES[38]){
			$Pl_WeaponNameD = "----------";
		}
	if ($WN_sB[0] || $WN_sC[0] || $WN_sD[0]){
		&JScfm(checkEquipSort,"装備品を並び替えます。よろしいですか？");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">装備並び替え</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
		print "<tr><td><input type=radio name=sorte value=0 disabled\n";
		print "<b>----------&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=0 disabled\n";
		print "<b>----------&nbsp;&nbsp;</b></td></tr>\n";
		print "<tr><td><input type=radio name=sorte value=1 \n";
		print "<b>$Pl_WeaponNameB&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=1 \n";
		print "<b>$Pl_WeaponNameB&nbsp;&nbsp;</b></td></tr>\n";
		print "<tr><td><input type=radio name=sorte value=2 \n";
		print "<b>$Pl_WeaponNameC&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=2 \n";
		print "<b>$Pl_WeaponNameC&nbsp;&nbsp;</b></td></tr>\n";
		print "<tr><td><input type=radio name=sorte value=3 \n";
		print "<b>$Pl_WeaponNameD&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sorter value=3 \n";
		print "<b>$Pl_WeaponNameD&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td></td><td style=\"padding-right:10px;\"><input type=submit name=Cmode value=装備並び替え onClick=\"return checkEquipSort()\"></td></tr></table>\n";
	}
#特殊ソート
		if(!$PL_VALUES[41]){
			$Pl_WeaponNameS = "----------";
		}
		if(!$PL_VALUES[42]){
			$Pl_WeaponNameT = "----------";
		}
		if(!$PL_VALUES[43]){
			$Pl_WeaponNameU = "----------";
		}
	if ($WN_sS[0] || $WN_sT[0] || $WN_sU[0]){
		&JScfm(checkSSort,"特殊攻撃を並び替えます。よろしいですか？");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">特殊並び替え</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
		print "<tr><td><input type=radio name=sorts value=1 \n";
		print "<b>$Pl_WeaponNameS&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sortsr value=1 \n";
		print "<b>$Pl_WeaponNameS&nbsp;&nbsp;</b></td></tr>\n";
		print "<tr><td><input type=radio name=sorts value=2 \n";
		print "<b>$Pl_WeaponNameT&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sortsr value=2 \n";
		print "<b>$Pl_WeaponNameT&nbsp;&nbsp;</b></td></tr>\n";
		print "<tr><td><input type=radio name=sorts value=3 \n";
		print "<b>$Pl_WeaponNameU&nbsp;&nbsp;</b></td>\n";
		print "<td><input type=radio name=sortsr value=3 \n";
		print "<b>$Pl_WeaponNameU&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td></td><td style=\"padding-right:10px;\"><input type=submit name=Cmode value=特殊並び替え onClick=\"return checkSSort()\"></td></tr></table>\n";
	}

#ストック引き出し	予備スロットからは取り出し・売却のみ可能　交換は不可！
#	if (((!$WN_sB[0] || !$WN_sC[0] || !$WN_sD[0]) && $WN_sY[11] eq "0" && $WN_sY[0]) || ((!$WN_sS[0] || !$WN_sT[0] || !$WN_sU[0]) && $WN_sY[11] ne "0" && $WN_sY[0])){

	if($WN_sY[0]){

	#エンチャントシステム
		if($WY03 ne "" && $WY03 > 0){$Pl_EntY .= "STRアップ+$WY03&nbsp;";}
		if($WY04 ne "" && $WY04 > 0){$Pl_EntY .= "VITアップ+$WY04&nbsp;";}
		if($WY05 ne "" && $WY05 > 0){$Pl_EntY .= "AGIアップ+$WY05&nbsp;";}
		if($WY06 ne "" && $WY06 > 0){$Pl_EntY .= "DEXアップ+$WY06&nbsp;";}
		if($WY07 ne "" && $WY07 > 0){$Pl_EntY .= "生命吸収+$WY07&nbsp;";}
		if($WY08 ne "" && $WY08 > 0){$Pl_EntY .= "魔法ブースト+$WY08&nbsp;";}
		if($WY09 ne "" && $WY09 > 0){$Pl_EntY .= "南瓜キラー+$WY09&nbsp;";}
		if($WY10 ne "" && $WY10 > 0){$Pl_EntY .= "南瓜ガード+$WY10&nbsp;";}
		if($WY11 ne "" && $WY11 > 0){$Pl_EntY .= "トレジャー発見率アップ+$WY11&nbsp;";}
		if($WY12 ne "" && $WY12 > 0){$Pl_EntY .= "MFアップ+$WY12&nbsp;";}
		if($WY13 ne "" && $WY13 > 0){$Pl_EntY .= "RESアップ+$WY13&nbsp;";}
		if($WY14 ne "" && $WY14 > 0){$Pl_EntY .= "火属性攻撃力アップ+$WY14&nbsp;";}
		if($WY15 ne "" && $WY15 > 0){$Pl_EntY .= "水属性攻撃力アップ+$WY15&nbsp;";}
		if($WY16 ne "" && $WY16 > 0){$Pl_EntY .= "大地属性攻撃力アップ+$WY16&nbsp;";}
		if($WY17 ne "" && $WY17 > 0){$Pl_EntY .= "風属性攻撃力アップ+$WY17&nbsp;";}
		if($WY18 ne "" && $WY18 > 0){$Pl_EntY .= "神聖属性攻撃力アップ+$WY18&nbsp;";}
		if($WY19 ne "" && $WY19 > 0){$Pl_EntY .= "暗黒属性攻撃力アップ+$WY19&nbsp;";}
		if($WY20 ne "" && $WY20 > 0){$Pl_EntY .= "火属性ダメージ軽減+$WY20&nbsp;";}
		if($WY21 ne "" && $WY21 > 0){$Pl_EntY .= "水属性ダメージ軽減+$WY21&nbsp;";}
		if($WY22 ne "" && $WY22 > 0){$Pl_EntY .= "大地属性ダメージ軽減+$WY22&nbsp;";}
		if($WY23 ne "" && $WY23 > 0){$Pl_EntY .= "風属性ダメージ軽減+$WY23&nbsp;";}
		if($WY24 ne "" && $WY24 > 0){$Pl_EntY .= "神聖属性ダメージ軽減+$WY24&nbsp;";}
		if($WY25 ne "" && $WY25 > 0){$Pl_EntY .= "暗黒属性ダメージ軽減+$WY25&nbsp;";}
		if($WY26 ne "" && $WY26 > 0){$Pl_EntY .= "無属性ダメージ軽減+$WY26&nbsp;";}
		if($WY27 ne "" && $WY27 > 0){$Pl_EntY .= "獲得Gothアップ+$WY27&nbsp;";}
#		if($WY28 ne "" && $WY28 > 0){$Pl_EntY .= "瀕死時HP回復+$WY28&nbsp;";}
		if($WY28 ne "" && $WY28 > 0){$Pl_EntY .= "戦術適性+$WY28&nbsp;";}
#		if($WY29 ne "" && $WY29 > 0){$Pl_EntY .= "戦闘不\能\時MP回復+$WY29&nbsp;";}
		if($WY29 ne "" && $WY29 > 0){$Pl_EntY .= "マナリカバリー+$WY29&nbsp;";}
		if($WY30 ne "" && $WY30 > 0){$Pl_EntY .= "ダメージ分配+$WY30&nbsp;";}
		if($WY31 ne "" && $WY31 > 0){$Pl_EntY .= "回復魔法強化+$WY31&nbsp;";}
		if($WY32 ne "" && $WY32 > 0){$Pl_EntY .= "クリティカル+$WY32&nbsp;";}
		if($WY33 ne "" && $WY33 > 0){$Pl_EntY .= "貫通攻撃+$WY33&nbsp;";}


#		@Count_Y = split(/!/,$PL_VALUES[46]);
#		$Ent_Y = 0;
#		for ($LngEntCntY = 3; $LngEntCntY <= 33; $LngEntCntY++){
#			if($Count_Y[$LngEntCntY] > 0){$Ent_Y = $Ent_Y + 1;}
#		}
#		if($Ent_Y > 0 && $Ent_Y <= 2){$Pl_WeaponNameY = "<font color=00ff00>$Pl_WeaponNameY</font>";}
#		elsif($Ent_Y > 2 && $Ent_Y <= 4){$Pl_WeaponNameY = "<font color=ffff00>$Pl_WeaponNameY</font>";}
#		elsif($Ent_Y > 4){$Pl_WeaponNameY = "<font color=ffD700>$Pl_WeaponNameY</font>";}



		&JScfm(checkGetY,"ストックからアイテムを取り出します。よろしいですか？");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">ストック</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
	if (((!$WN_sB[0] || !$WN_sC[0] || !$WN_sD[0]) && ($WN_sY[11] eq "0" || $WN_sY[11] eq "9") && $WN_sY[0]) || ((!$WN_sS[0] || !$WN_sT[0] || !$WN_sU[0]) && $WN_sY[11] ne "0" && $WN_sY[11] ne "9" && $WN_sY[0])){

		print "<tr><td>ストックアイテム：$Pl_WeaponNameY&nbsp;<font color=00ff00>$Pl_EntY</font></td><td><input type=submit name=Cmode value=取り出す onClick=\"return checkGetY()\"></td></tr>\n";
#		print "<tr><td>ストックアイテム：$WN_sY[0]</td><td><input type=submit name=Cmode value=取り出す onClick=\"return checkGetY()\"></td></tr>\n";

	}else{

		print "<tr><td>ストックアイテム：$Pl_WeaponNameY&nbsp;<font color=00ff00>$Pl_EntY</font></td></tr>\n";
#		print "<tr><td>ストックアイテム：$WN_sY[0]</td></tr>\n";

	}

#		print "<tr><td style=\"padding-left:20px;\">$PartofW</td></tr></table>\n";
#		print "<tr><input type=submit name=Cmode value=取り出す onClick=\"return checkGetY()\"></tr></table>\n";
		print "</table>\n";

	}

	if ($WLV_A >= $WEAPON_RANKUP){
		&JScfm(checkRnkup,"武器をランクアップさせます。よろしいですか？");
		while (my ($key,$val) = each %WEAPON_LIST){
			if (substr($key,0,length($WN_A)) eq $WN_A && length($key) == length($WN_A)+1){
				my @UpW = split(/\,/,$val);
				$WeCH++;
				print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/up.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">装備ランクアップ</b>\n" if $WeCH ==1;
				print "<table style=\"font-size:9pt;\"><tr><td $BgColor>&nbsp;\n";
				print "$Pl_WeaponNameA\n" if $WeCH ==1;
				print "<font color=\"$TABLE_COLOR1\">$Pl_WeaponNameA</font>\n" if $WeCH !=1;
				print "</td><td $BgColor><font color=#1e90ff><b>⇒</b></font>\n";
				print "<input type=radio name=wname value=$key\n";
				print " checked" if $WeCH ==1;
				print ">$UpW[0]</td><td $BgColor>\n";
				print "<input name=\"Cmode\" type=submit value=ランクアップ" if $WeCH ==1;
				print " onClick=\"return checkRnkup()\">\n" if $WeCH ==1;
				print "</td></tr></table>\n";
			}
		}
	}

	if ($WLV_S >= $WEAPON_RANKUP){
		&JScfm(checkSRnkup,"ランクアップさせます。よろしいですか？");
		while (my ($keys,$vals) = each %WEAPON_LIST){
			if (substr($keys,0,length($WN_S)) eq $WN_S && length($keys) == length($WN_S)+1){
				my @UpS = split(/\,/,$vals);
				$WeCHs++;
				print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/up.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">特殊ランクアップ</b>\n" if $WeCHs ==1;
				print "<table style=\"font-size:9pt;\"><tr><td $BgColor>&nbsp;\n";
				print "$Pl_WeaponNameS\n" if $WeCHs ==1;
				print "<font color=\"$TABLE_COLOR1\">$Pl_WeaponNameS</font>\n" if $WeCHs !=1;
				print "</td><td $BgColor><font color=#1e90ff><b>⇒</b></font>\n";
				print "<input type=radio name=sname value=$keys\n";
				print " checked" if $WeCHs ==1;
				print ">$UpS[0]</td><td $BgColor>\n";
				print "<input name=\"Cmode\" type=submit value=特殊ランクアップ" if $WeCHs ==1;
				print " onClick=\"return checkSRnkup()\">\n" if $WeCHs ==1;
				print "</td></tr></table>\n";
			}
		}
	}

	require "./$LOG_FOLDER/$CLASS_DATA";
	@ALY_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

	local($WN_CS,$WLV_CS) = split(/!/,$ALY_CLASS[22]);
	@WN_sCS=split(/\,/,$WEAPON_LIST{"$WN_CS"});
	local($WN_CS2,$WLV_CS2) = split(/!/,$ALY_CLASS[23]);
	@WN_sCS2=split(/\,/,$WEAPON_LIST{"$WN_CS2"});
	local($WN_CS3,$WLV_CS3) = split(/!/,$ALY_CLASS[24]);
	@WN_sCS3=split(/\,/,$WEAPON_LIST{"$WN_CS3"});
	local($WN_CS4,$WLV_CS4) = split(/!/,$ALY_CLASS[25]);
	@WN_sCS4=split(/\,/,$WEAPON_LIST{"$WN_CS4"});
	local($WN_CS5,$WLV_CS5) = split(/!/,$ALY_CLASS[26]);
	@WN_sCS5=split(/\,/,$WEAPON_LIST{"$WN_CS5"});

#迎撃時設定を追加
#		$PartofWP.="<option value=0 selected=selected>特殊を使って迎撃" if $PL_VALUES[45] ne "1";
#		$PartofWP.="<option value=0>特殊を使って迎撃" if $PL_VALUES[45] eq "1";
#		$PartofWP.="<option value=1 selected=selected>武器だけで迎撃" if $PL_VALUES[45] eq "1";
#		$PartofWP.="<option value=1>武器だけで迎撃" if $PL_VALUES[45] ne "1";

if($WN_sS[0]){
		$PartofWP.="<option value=41 selected=selected>$WN_sS[0]で迎撃" if $PL_VALUES[45] eq "41";
		$PartofWP.="<option value=41>$WN_sS[0]で迎撃" if $PL_VALUES[45] ne "41";
}
if($WN_sT[0]){
		$PartofWP.="<option value=42 selected=selected>$WN_sT[0]で迎撃" if $PL_VALUES[45] eq "42";
		$PartofWP.="<option value=42>$WN_sT[0]で迎撃" if $PL_VALUES[45] ne "42";
}
if($WN_sU[0]){
		$PartofWP.="<option value=43 selected=selected>$WN_sU[0]で迎撃" if $PL_VALUES[45] eq "43";
		$PartofWP.="<option value=43>$WN_sU[0]で迎撃" if $PL_VALUES[45] ne "43";
}
if($WN_sA[13]){
		@WN_sCalcA=split(/\,/,$WEAPON_LIST{"$WN_sA[13]"});
		$PartofWP.="<option value=90 selected=selected>$WN_sCalcA[0]で迎撃" if $PL_VALUES[45] eq "90";
		$PartofWP.="<option value=90>$WN_sCalcA[0]で迎撃" if $PL_VALUES[45] ne "90";
}
if($WN_sB[13]){
		@WN_sCalcB=split(/\,/,$WEAPON_LIST{"$WN_sB[13]"});
		$PartofWP.="<option value=100 selected=selected>$WN_sCalcB[0]で迎撃" if $PL_VALUES[45] eq "100";
		$PartofWP.="<option value=100>$WN_sCalcB[0]で迎撃" if $PL_VALUES[45] ne "100";
}
if($WN_sC[13]){
		@WN_sCalcC=split(/\,/,$WEAPON_LIST{"$WN_sC[13]"});
		$PartofWP.="<option value=110 selected=selected>$WN_sCalcC[0]で迎撃" if $PL_VALUES[45] eq "110";
		$PartofWP.="<option value=110>$WN_sCalcC[0]で迎撃" if $PL_VALUES[45] ne "110";
}
if($WN_sD[13]){
		@WN_sCalcD=split(/\,/,$WEAPON_LIST{"$WN_sD[13]"});
		$PartofWP.="<option value=380 selected=selected>$WN_sCalcD[0]で迎撃" if $PL_VALUES[45] eq "380";
		$PartofWP.="<option value=380>$WN_sCalcD[0]で迎撃" if $PL_VALUES[45] ne "380";
}
if($WN_sCS[0]){
		@WN_sCalcCS=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[22]"});
		$PartofWP.="<option value=390 selected=selected>$WN_sCalcCS[0]で迎撃" if $PL_VALUES[45] eq "390";
		$PartofWP.="<option value=390>$WN_sCalcCS[0]で迎撃" if $PL_VALUES[45] ne "390";
}
if($WN_sCS2[0]){
		@WN_sCalcCS2=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[23]"});
		$PartofWP.="<option value=391 selected=selected>$WN_sCalcCS2[0]で迎撃" if $PL_VALUES[45] eq "391";
		$PartofWP.="<option value=391>$WN_sCalcCS2[0]で迎撃" if $PL_VALUES[45] ne "391";
}
if($WN_sCS3[0]){
		@WN_sCalcCS3=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[24]"});
		$PartofWP.="<option value=392 selected=selected>$WN_sCalcCS3[0]で迎撃" if $PL_VALUES[45] eq "392";
		$PartofWP.="<option value=392>$WN_sCalcCS3[0]で迎撃" if $PL_VALUES[45] ne "392";
}
if($WN_sCS4[0]){
		@WN_sCalcCS4=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[25]"});
		$PartofWP.="<option value=393 selected=selected>$WN_sCalcCS4[0]で迎撃" if $PL_VALUES[45] eq "393";
		$PartofWP.="<option value=393>$WN_sCalcCS4[0]で迎撃" if $PL_VALUES[45] ne "393";
}
if($WN_sCS5[0]){
		@WN_sCalcCS5=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[26]"});
		$PartofWP.="<option value=394 selected=selected>$WN_sCalcCS5[0]で迎撃" if $PL_VALUES[45] eq "394";
		$PartofWP.="<option value=394>$WN_sCalcCS5[0]で迎撃" if $PL_VALUES[45] ne "394";
}
		$PartofWP.="<option value=9 selected=selected>$WN_sA[0]で迎撃" if $PL_VALUES[45] eq "9";
		$PartofWP.="<option value=9>$WN_sA[0]で迎撃" if $PL_VALUES[45] ne "9" || $PL_VALUES[45] eq "1" || $PL_VALUES[45] eq "0";

		print "<SCRIPT language=\"JavaScript\">\nfunction checkSet (){\n";
		print "if (confirm('迎撃設定を変更しますがよろしいですか？') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/up.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">迎撃設定</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=AtSet>$PartofWP</select><input type=submit name=Cmode value=設定 onClick=\"return checkSet()\"></td></tr></table>\n";

		print "</td></tr>";

#装備品強化
#		print "<SCRIPT language=\"JavaScript\">\nfunction checkkyoka (){\n";
#		print "if (confirm('装備品を強化しますがよろしいですか？') == true){\n";
#		print "}else{return false}\n";
#		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">武具強化</b>";
#		$GothCostEnt = 100000 * ($WAEnt + 1);
#		if($PL_VALUES[8] >= $GothCostEnt){
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelA$WF_A&nbsp;$Pl_WeaponNameA</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$GothCostEnt Goth消費します。<input type=submit name=Cmode value=武具強化 onClick=\"return checkkyoka()\"></td></tr></table>\n";
#		}else{
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelA$WF_A&nbsp;$Pl_WeaponNameA</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所持金が足りません。</td></tr></table>\n";		
#		}
#		print "</td></tr>";

#装備品強化解除
#		print "<SCRIPT language=\"JavaScript\">\nfunction checkrise (){\n";
#		print "if (confirm('最上段装備品の強化数をリセットしますがよろしいですか？') == true){\n";
#		print "}else{return false}\n";
#		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">武具初期化</b>";
#		if($PL_VALUES[8] >= 5000000){
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelA$WF_A&nbsp;$Pl_WeaponNameA</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5000000 Goth消費します。<input type=submit name=Cmode value=武具初期化 onClick=\"return checkrise()\"></td></tr></table>\n";
#		}else{
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelA$WF_A&nbsp;$Pl_WeaponNameA</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所持金が足りません。</td></tr></table>\n";		
#		}
#		print "</td></tr>";

#技術強化　@WN_sA
#		print "<SCRIPT language=\"JavaScript\">\nfunction checkkyoka2 (){\n";
#		print "if (confirm('最上段の技術を強化しますがよろしいですか？') == true){\n";
#		print "}else{return false}\n";
#		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">スキル強化</b>";
#		if($WLV_S >= 99 && $WN_S ne ""){
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelS$WF_S&nbsp;$Pl_WeaponNameS</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;技術EXP を消費します。（当該技術のLvは0に戻ります）<input type=submit name=Cmode value=スキル強化 onClick=\"return checkkyoka2()\"></td></tr></table>\n";
##		}elsif($WN_S == $WN_T && $WN_S ne ""){
##			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelS$WF_S&nbsp;$Pl_WeaponNameS</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同名の技術 を消費します。（当該技術のLvは0に戻ります）<input type=submit name=Cmode value=スキル強化 onClick=\"return checkkyoka2()\"></td></tr></table>\n";
##		}elsif($WN_S == $WN_U && $WN_S ne ""){
##			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelS$WF_S&nbsp;$Pl_WeaponNameS</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同名の技術 を消費します。（当該技術のLvは0に戻ります）<input type=submit name=Cmode value=スキル強化 onClick=\"return checkkyoka2()\"></td></tr></table>\n";
#		}else{
#			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$WeaponLevelS$WF_S&nbsp;$Pl_WeaponNameS</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;実行できません。</td></tr></table>\n";		
#		}
#		print "</td></tr>";
		
#エンチャント
		print "<SCRIPT language=\"JavaScript\">\nfunction checkkyokaEn (){\n";
		print "if (confirm('最上段の装備品にエンチャント付与を行いますがよろしいですか？(付与されない場合も多々あります。既存のエンチャント効果は全て破棄されます。)') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">シャッフルエンチャント</b>";

		if($PL_VALUES[8] >= 2000000){
			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$Pl_WeaponNameA</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2000000Goth消費します。<input type=submit name=Cmode value=シャッフル実行 onClick=\"return checkkyokaEn()\"></td></tr></table>\n";
		}else{
			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><b>$Pl_WeaponNameA</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;所持金が足りません。</td></tr></table>\n";		
		}
		print "</td></tr>";

#道具使用
	if ($WN_sB[7] =~ m/!E0013/ || $WN_sC[7] =~ m/!E0013/ || $WN_sD[7] =~ m/!E0013/ || $WN_sS[7] =~ m/!E0013/ || $WN_sT[7] =~ m/!E0013/ || $WN_sU[7] =~ m/!E0013/ || $WN_sY[7] =~ m/!E0013/){
		$PartofSIt.="<option value=0>";
		$PartofSIt.="<option value=1>$Pl_WeaponNameB" if $WN_sB[7] =~ m/!E0013/;
		$PartofSIt.="<option value=2>$Pl_WeaponNameC" if $WN_sC[7] =~ m/!E0013/;
		$PartofSIt.="<option value=3>$Pl_WeaponNameD" if $WN_sD[7] =~ m/!E0013/;
		$PartofSIt.="<option value=4>$Pl_WeaponNameS" if $WN_sS[7] =~ m/!E0013/;
		$PartofSIt.="<option value=5>$Pl_WeaponNameT" if $WN_sT[7] =~ m/!E0013/;
		$PartofSIt.="<option value=6>$Pl_WeaponNameU" if $WN_sU[7] =~ m/!E0013/;
		$PartofSIt.="<option value=7>$Pl_WeaponNameY" if $WN_sY[7] =~ m/!E0013/;
		print "<SCRIPT language=\"JavaScript\">\nfunction checkItemShiyo (){\n";
		print "if (confirm('道具を使用しますがよろしいですか？') == true){\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">道具使用</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=shiyoi>$PartofSIt</select><input type=submit name=Cmode value=道具使用 onClick=\"return checkItemShiyo()\"></td></tr></table>\n";

		print "</td></tr>";
	}


	if ($WN_sB[0] || $WN_sC[0] || $WN_sD[0] || $WN_sS[0] || $WN_sT[0] || $WN_sU[0] || $WN_sY[0]){
		$PartofSW.="<option value=0>";
		$PartofSW.="<option value=1>$Pl_WeaponNameB" if $WN_sB[0];
		$PartofSW.="<option value=2>$Pl_WeaponNameC" if $WN_sC[0];
		$PartofSW.="<option value=3>$Pl_WeaponNameD" if $WN_sD[0];
		$PartofSW.="<option value=4>$Pl_WeaponNameS" if $WN_sS[0];
		$PartofSW.="<option value=5>$Pl_WeaponNameT" if $WN_sT[0];
		$PartofSW.="<option value=6>$Pl_WeaponNameU" if $WN_sU[0];
		$PartofSW.="<option value=7>$WN_sY[0]" if $WN_sY[0];
		print "<SCRIPT language=\"JavaScript\">\nfunction checkMoney (){\n";
		print "num=document.Ms.sellw.value;\nif (num==1){var wn='$Pl_WeaponNameB2';var mn='".int($WN_sB[5]/2)."';}\n";
		print "else if (num ==2){var wn='$Pl_WeaponNameC2';var mn='".int($WN_sC[5]/2)."';}\n";
		print "else if (num ==3){var wn='$Pl_WeaponNameD2';var mn='".int($WN_sD[5]/2)."';}\n";
		print "else if (num ==4){var wn='$Pl_WeaponNameS2';var mn='".int($WN_sS[5]/2)."';}\n";
		print "else if (num ==5){var wn='$Pl_WeaponNameT2';var mn='".int($WN_sT[5]/2)."';}\n";
		print "else if (num ==6){var wn='$Pl_WeaponNameU2';var mn='".int($WN_sU[5]/2)."';}\n";
#		print "num=document.Ms.sellw.value;\nif (num==1){var wn='$Pl_WeaponNameB';var mn='".int($WN_sB[5]/2)."';}\n";
#		print "else if (num ==2){var wn='$Pl_WeaponNameC';var mn='".int($WN_sC[5]/2)."';}\n";
#		print "else if (num ==3){var wn='$Pl_WeaponNameD';var mn='".int($WN_sD[5]/2)."';}\n";
#		print "else if (num ==4){var wn='$Pl_WeaponNameS';var mn='".int($WN_sS[5]/2)."';}\n";
#		print "else if (num ==5){var wn='$Pl_WeaponNameT';var mn='".int($WN_sT[5]/2)."';}\n";
#		print "else if (num ==6){var wn='$Pl_WeaponNameU';var mn='".int($WN_sU[5]/2)."';}\n";
#		print "else if (num ==7){var wn='$WN_sY[0]';var mn='".int($WN_sY[5]/2)."';}\n";
		print "else if (num ==7){var wn='$Pl_WeaponNameY2';var mn='".int($WN_sY[5]/2)."';}\n";
		print "else if (num ==0){return false}\n";		
		print "if (confirm(wn + 'を\$' + mn + 'で売却します') == true){\n";
		print "if (confirm('本当に' + wn + 'を売却してよろしいですか？') == true){return true;}else{return false}\n";
		print "}else{return false}\n";
		print "}\n</script>\n<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip2.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">武器売却</b>";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\"><tr><td style=\"padding-left:20px;\"><select name=sellw>$PartofSW</select><input type=submit name=Cmode value=売却 onClick=\"return checkMoney()\"></td></tr></table>\n";

		print "</td></tr>";
	}
	if (!$WN_sB[0] || !$WN_sC[0] || !$WN_sD[0] || !$WN_sS[0] || !$WN_sT[0] || !$WN_sU[0]){
#		print "<tr><td $BgColor height=\"150\" background=\"$IMG_FOLDER1/shop.gif\" style=\"background-repeat:no-repeat;background-position:top;text-align: center;\"><img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" style=\"position:relative;top:20;right:22;\"></td></tr><tr><td $BgColor >\n";
		print "<tr></tr><tr><td $BgColor >\n";
		print "<table style=\"font-size:9pt;\"><img src=\"$IMG_FOLDER1/equipshop.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">$matiname</b>\n";
		&JScfm(checkBuy,"武器を購入します。よろしいですか？");
		local($Flag=0);
		$buy="<select name=buyw>";
		foreach $key (sort{$a cmp $b} keys %WEAPON_LIST){
			my @ByW = split(/\,/,$WEAPON_LIST{$key});
			#通常装備品
			if($ByW[11] == 0 && (!$WN_sB[0] || !$WN_sC[0] || !$WN_sD[0])){
				if($ByW[5] <= $PL_VALUES[8] && ($ByW[6] == 6 || $ByW[6] == 7)){
					print "<tr><td>&nbsp;&nbsp;<img src=\"$IMG_FOLDER4/$ByW[9].gif\"></td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[5]</td></tr>";
					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
				}
				if($ByW[5] <= $PL_VALUES[8] && $ByW[6] == 8 && $merufi == 1 && $PL_VALUES[5] eq ""){
					print "<tr><td>&nbsp;&nbsp;<img src=\"$IMG_FOLDER4/$ByW[9].gif\"></td><td><font color=#a181c0>&nbsp;&nbsp;★$ByW[0]</font></td><td style=\"text-align:right;\"><font color=#a181c0>$ByW[5]</font></td></tr>";
					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
				}
			}
			#特殊
			if($ByW[11] != 0 && (!$WN_sS[0] || !$WN_sT[0] || !$WN_sU[0])){
				if($ByW[5] <= $PL_VALUES[8] && ($ByW[6] == 6 || $ByW[6] == 7)){
					print "<tr><td>&nbsp;&nbsp;<img src=\"$IMG_FOLDER4/$ByW[9].gif\"></td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[5]</td></tr>";
					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
				}
				if($ByW[5] <= $PL_VALUES[8] && $ByW[6] == 8 && $merufi == 1 && $PL_VALUES[5] eq ""){
					print "<tr><td>&nbsp;&nbsp;<img src=\"$IMG_FOLDER4/$ByW[9].gif\"></td><td><font color=#a181c0>&nbsp;&nbsp;★$ByW[0]</font></td><td style=\"text-align:right;\"><font color=#a181c0>$ByW[5]</font></td></tr>";
					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
				}
			}
		}
		if ($Flag>0){
			$buy.="</select><input name=\"Cmode\" type=submit value=購入 onClick=\"return checkBuy()\">\n";
		}else{
			$buy="所持金が足りません。";$Flag++;
		}
		print "</table><div align=right>$buy</div></td></tr>\n";
	}
	if ($merufi == 1 && $PL_VALUES[5] eq ""){
	$JACKF++;
	&JScfm(checkJa,"アイテムを使用します。よろしいですか？");
	$TIKIM=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
	$TIKIM2=int(1000*$PL_VALUES[29]+100000);
	$TIKIM3=400000;
	print "<tr><td $BgColor><table style=\"font-size:9pt;\"><tr><td>&nbsp;&nbsp;剣の紋章</td><td>$TIKIM</td>";
	print "<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[0]アップ\" onClick='";
	print "return checkJa()'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[19] < 50;
	print "alert (\"お金が足りません\");return false;'>" if $PL_VALUES[8] < $TIKIM;
	print "alert (\"これ以上アップできません\");return false;'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[19] >= 50;
	print "</td></tr><tr><td>&nbsp;&nbsp;守護の腕輪</td><td>$TIKIM</td>";
	print "<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[1]アップ\" onClick='";
	print "return checkJa()'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[20] < 50;
	print "alert (\"お金が足りません\");return false;'>" if $PL_VALUES[8] < $TIKIM;
	print "alert (\"これ以上アップできません\");return false;'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[20] >= 50;
	print "</td></tr><tr><td>&nbsp;&nbsp;俊敏の石</td><td>$TIKIM</td>";
	print "<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[2]アップ\" onClick='";
	print "return checkJa()'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[21] < 50;
	print "alert (\"お金が足りません\");return false;'>" if $PL_VALUES[8] < $TIKIM;
	print "alert (\"これ以上アップできません\");return false;'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[21] >= 50;
	print "</td></tr><tr><td>&nbsp;&nbsp;精密の水晶</td><td>$TIKIM</td>";
	print "<td><input type=submit name=\"Cmode\" value=\"$STATUS_NAME[3]アップ\" onClick='";
	print "return checkJa()'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[22] < 50;
	print "alert (\"お金が足りません\");return false;'>" if $PL_VALUES[8] < $TIKIM;
	print "alert (\"これ以上アップできません\");return false;'>" if $PL_VALUES[8] >= $TIKIM && $PL_VALUES[22] >= 50;
	print "</td></tr><tr><td>&nbsp;&nbsp;勇者の像</td><td>$TIKIM2</td>";
	print "<td><input type=submit name=\"Cmode\" value=\"Lv.アップ\" onClick='";
	print "return checkJa()'>" if $PL_VALUES[8] >= $TIKIM2;
	print "alert (\"お金が足りません\");return false;'>" if $PL_VALUES[8] < $TIKIM2;
	print "</td></tr><tr><td>&nbsp;&nbsp;秩序の書</td><td>$TIKIM3</td>";
	print "<td><input type=submit name=\"Cmode\" value=\"ALIアップ\" onClick='";
	print "return checkJa()'>" if $PL_VALUES[8] >= $TIKIM3 && $PL_VALUES[12] < 100;
	print "alert (\"お金が足りません\");return false;'>" if $PL_VALUES[8] < $TIKIM3;
	print "alert (\"これ以上アップできません\");return false;'>" if $PL_VALUES[8] >= $TIKIM3 && $PL_VALUES[12] >= 100;
	print "</td></tr></table></td></tr>";
	}
	if (!$PL_VALUES[10] && !$PL_VALUES[11] && !$PL_VALUES[38] && !$PL_VALUES[41] && !$PL_VALUES[42] && !$PL_VALUES[43] && $Flag==0 && $WeCH ==0 && $JACKF==0){
		print "<tr><td $BgColor>実行できるコマンドがありません。</td></tr>\n";}
	print "</form></table>\n";&FOOTER;
}
sub MISSION2{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_INPORT('C');&UNLOCK;
	@C_VALUES = split(/\s/,$C{"$PL_VALUES[5]"});

	while (($C_Name,$C_Value) =each %C) {
		@C_VALUE2 = split(/\s/,$C_Value);$V_JIKANSA=$C_VALUE2[13];$V_JIKANSA=15 if $C_VALUE2[13]>14;
		push (@VS_COUNTRY,$C_Name) if (($C_VALUE2[6] eq $PL_VALUES[5] || $C_VALUE2[8] eq $PL_VALUES[5] || $C_VALUE2[9] eq $PL_VALUES[5] || $C_VALUE2[10] eq $PL_VALUES[5]) && $C_VALUE2[7] > time && ($C_VALUE2[14]+$V_JIKANSA*60) <= time);
	}
	&ERROR("世界大戦中です。") if $WW_FRAG==1;
	if ($C_VALUES[7] > time || ($PL_VALUES[6] == -1 && @VS_COUNTRY)){
	&ERROR('応戦する権限がありません。') if $PL_VALUES[6] == 0 || !$PL_VALUES[5] || !$C{"$PL_VALUES[5]"};
	&ERROR('ERROR',"現在「$C_VALUES[5]作戦」発動中です。") if !@VS_COUNTRY;
	$JIKANSA=$C_VALUES[13];$JIKANSA=15 if $C_VALUES[13]>14;
	&ERROR('現在の作戦が発動するまで応戦できません。') if ($C_VALUES[7] > time && ($C_VALUES[14]+$JIKANSA*60) > time);
	&CUSTOM_HEADER('Main');
	print "<tr><td $BgColor align=right><br>";
	$op="<option value=>応戦先 \n" if ($C_VALUES[7] > time);
	foreach (@VS_COUNTRY) {
	$op.= "<option value=\"$_\">$_\n";
	}
	if ($C_VALUES[7] <= time){$C_VALUES[5] ="応戦開始";$DOTTI="戦略";$SENPI="500";}else{$DOTTI="追加";$SENPI="5000";}
	print "<input type=hidden name=dmmy>";
	print "国費：<b>\$ $C_VALUES[1]</b><br>";
	print "戦略費：<input type=text name=sikin size=10 maxlength=10 style=\"border:none;background:#000000;color:#ffffff;text-align:right;\"><br>";
	print "作戦名：<input type=hidden name=mname value=\"$C_VALUES[5]\">$C_VALUES[5]<br>";
	print "メイン戦略：<select name=main onChange=\"YOSAN()\">$op</select><br>";

	print "第１部隊 $C_VALUES[2] 戦略：<select name=u1 onChange=\"YOSAN()\">$op</select><br>" if $C_VALUES[2];
	print "第２部隊 $C_VALUES[3] 戦略：<select name=u2 onChange=\"YOSAN()\">$op</select><br>" if $C_VALUES[3];
	print "第３部隊 $C_VALUES[4] 戦略：<select name=u3 onChange=\"YOSAN()\">$op</select><br>" if $C_VALUES[4];
	print "$DOTTI期間：<select name=kikan  onChange=\"YOSAN()\"><option value=1>30分<option value=2>1時間<option value=4>2時間</select><br>";
	print "<input name=\"Cmode\" type=\"submit\" value=\"応戦\" onClick=\"return ChMn()\">";

	if ($C_VALUES[7] > time){
	print "<script language=\"JavaScript\">\nfunction YOSAN(){\nvar mm=0;\n";
	print "if (document.Ms.main.selectedIndex != 0){mm+=$SENPI;}\n";
	print "if (document.Ms.u1.selectedIndex != 0){mm+=$SENPI;}\n" if $C_VALUES[2];
	print "if (document.Ms.u2.selectedIndex != 0){mm+=$SENPI;}\n" if $C_VALUES[3];
	print "if (document.Ms.u3.selectedIndex != 0){mm+=$SENPI;}\n" if $C_VALUES[4];
	}else{$BS_C=0;$BS_C++ if($C_VALUES[2]);$BS_C++ if($C_VALUES[3]);$BS_C++ if($C_VALUES[4]);
	if($BS_C==1){$OHSENPI=$SENPI*3;}elsif($BS_C==2){$OHSENPI=$SENPI*5;}else{$OHSENPI=$SENPI*8;}
	print "<script language=\"JavaScript\">\nfunction YOSAN(){\nvar mm=$OHSENPI;\n";
	print "if (document.Ms.main.selectedIndex == document.Ms.u1.selectedIndex){mm-=$SENPI;}\n" if $C_VALUES[2];
	print "if (document.Ms.main.selectedIndex == document.Ms.u2.selectedIndex){mm-=$SENPI;}\n" if $C_VALUES[3];
	print "if (document.Ms.main.selectedIndex == document.Ms.u3.selectedIndex){mm-=$SENPI;}\n" if $C_VALUES[4];
	print "if (document.Ms.u1.selectedIndex == document.Ms.u2.selectedIndex){mm-=$SENPI;}\n" if $C_VALUES[2] && $C_VALUES[3];
	print "if (document.Ms.u1.selectedIndex == document.Ms.u3.selectedIndex){mm-=$SENPI;}\n" if $C_VALUES[2] && $C_VALUES[4];
	print "if (document.Ms.u2.selectedIndex == document.Ms.u3.selectedIndex){mm-=$SENPI;}\n" if $C_VALUES[3] && $C_VALUES[4];
	}

	print << "	-----END-----";
		total=(eval(document.Ms.kikan.selectedIndex) + 1)*mm;
		document.Ms.sikin.value='\$'+total;
		document.Ms.dmmy.value=total;
		if (total > $C_VALUES[1]){document.Ms.sikin.style.color='#ffadac';}
		if (total <= $C_VALUES[1]){document.Ms.sikin.style.color='#ffffff';}
	}
	function ChMn(){
	if (document.Ms.dmmy.value > $C_VALUES[1]){alert('資金が足りません。');return false;}
	if (document.Ms.dmmy.value==0){alert('応戦先が指定されていません');return false;}
	if (confirm('応戦を開始します。\\nよろしいですか？') == true){return true;}else{return false;}
	}
	YOSAN();
	</script></td></tr></form></table>
	-----END-----
	}else{
	&ERROR('何処からも侵攻を受けていません。') if $PL_VALUES[6]!=1 || !$PL_VALUES[5] || !$C{"$PL_VALUES[5]"};
	&CUSTOM_HEADER('Main');
	print "<tr><td $BgColor align=right><br>";
	while (my($key,$val) =each %C) {
		@CN_VALS = split(/\s/,$val);
		if ($MENTE==0){$CN_VALS[7]+=259200;}
		if ($PL_VALUES[5] ne "$key" && ($CN_VALS[6] || $CN_VALS[7] < time)){$op.= "<option value=\"$key\">$key\n";}
	}
	&ERROR('攻略できる国がありません。') if !$op;
	print "<input type=hidden name=dmmy>";
	print "国費：<b>\$ $C_VALUES[1]</b><br>";
	print "戦略費：<input type=text name=sikin size=10 maxlength=10 style=\"border:none;background:#000000;color:#ffffff;text-align:right;\"><br>";
	print "作戦名：<input type=text name=mname size=25 maxlength=15><br>";
	print "メイン戦略：<select name=main onChange=\"YOSAN()\">$op</select><br>";

	print "第１部隊 $C_VALUES[2] 戦略：<select name=u1 onChange=\"YOSAN()\">$op</select><br>" if $C_VALUES[2];
	print "第２部隊 $C_VALUES[3] 戦略：<select name=u2 onChange=\"YOSAN()\">$op</select><br>" if $C_VALUES[3];
	print "第３部隊 $C_VALUES[4] 戦略：<select name=u3 onChange=\"YOSAN()\">$op</select><br>" if $C_VALUES[4];
	print "戦略期間：<select name=kikan onChange=\"YOSAN()\"><option value=1>3時間<option value=2>6時間<option value=4>12時間<option value=8>24時間</select><br>";
	print "<input name=\"Cmode\" type=\"submit\" value=\"発動\" onClick=\"return ChMn()\">";
	print "<script language=\"JavaScript\">\nfunction YOSAN(){\nvar mm=8000;\n";
	print "if (document.Ms.main.selectedIndex != document.Ms.u1.selectedIndex){mm+=1000;}\n" if $C_VALUES[2];
	print "if (document.Ms.main.selectedIndex != document.Ms.u2.selectedIndex){mm+=1000;}\n" if $C_VALUES[3];
	print "if (document.Ms.main.selectedIndex != document.Ms.u3.selectedIndex){mm+=1000;}\n" if $C_VALUES[4];
	print "if (document.Ms.u1.selectedIndex == document.Ms.u2.selectedIndex){mm-=1000;}\n" if $C_VALUES[2] && $C_VALUES[3];
	print "if (document.Ms.u2.selectedIndex == document.Ms.u3.selectedIndex){mm-=1000;}\n" if $C_VALUES[3] && $C_VALUES[4];
	print "if (document.Ms.u1.selectedIndex == document.Ms.u3.selectedIndex){mm-=1000;}\n" if $C_VALUES[2] && $C_VALUES[4];
	print "if (document.Ms.u1.selectedIndex != document.Ms.u2.selectedIndex && document.Ms.u1.selectedIndex != document.Ms.u3.selectedIndex){mm+=3000;}\n" if $C_VALUES[2] && $C_VALUES[3] && $C_VALUES[4];

	print << "	-----END-----";
		total=(eval(document.Ms.kikan.selectedIndex) + 1)*mm;
		document.Ms.sikin.value='\$'+total;
		document.Ms.dmmy.value=total;
		if (total > $C_VALUES[1]){document.Ms.sikin.style.color='#ffadac';}
		if (total <= $C_VALUES[1]){document.Ms.sikin.style.color='#ffffff';}
	}
	function ChMn(){
	if (document.Ms.dmmy.value > $C_VALUES[1]){alert('資金が足りません。');return false;
	}else if (document.Ms.mname.value == ''){alert('作戦名が未記入です。');return false;
	}else if(document.Ms.mname.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
				window.alert("だーめっ！");return false ;
	}else if (confirm('戦略を発動します。\\nよろしいですか？') == true){return true;}else{return false;}
	
	}
	YOSAN();
	</script></td></tr></form></table>
	-----END-----
	}
	&FOOTER;
}
sub MAKE_C2{
	&LOCK;&DBM_INPORT('C');&DBM_CONVERT('P',"$FORM{pname}");&UNLOCK;
	&CUSTOM_HEADER('Main');
	my@C=%C;my$C=@C/2;

	$CCnt = 0;
	while (($C_Name,$C_Value) =each %C) {
		@C_VALUES = split(/\s/,$C_Value);

		if ($C_VALUES[39] eq $PL_VALUES[39]){
				$CCnt = $CCnt + 1;
		}

	}


	if ($C >= $COUNTRY_MAX){print "<tr><td $BgColor>$COUNTRY_MAX国以上の建国は出来ません。</td></tr></table>\n";
#	if ($CCnt >= 6){print "<tr><td $BgColor>6国以上の建国は出来ません。</td></tr></table>\n";
	}elsif($WW_FRAG==1){print "<tr><td $BgColor>世界大戦中の建国は出来ません。</td></tr></table>\n";
	}else{
		print << "		-----END-----";
	<script language="JavaScript">
	function checkCountry(){
	if (document.Ms.cname.value == ''){window.alert("国名が記入されていません。");return false;
	}else if(document.Ms.cname.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
		window.alert("だーめっ！");return false;
	}else if (confirm('建国します。よろしいですか') == true){return true;
	}else{return false}
	}
	</script>
	<tr><td $BgColor><b>建国費用 \$$MAKE_COUNTRY</b>

	<table style="font-size:10pt;margin-left:8px;margin-right:8px;">
	<tr>
	<td>国の名前</td>
	<td><input type=text name=\"cname\" size=25 maxlength=20 $STYLE_L></td>
	</tr>
	<tr>
	<td>国の色</td><td>
		-----END-----
		print "<select name=cl>";
		foreach (@COLOR){
			print "<option value=\"$_\"";
			print " style=\"color:#$_\">■$_\n";
		}
		print "</select>";
		print << "		-----END-----";
			</td></tr></table>
			<input name="Cmode" type=submit value=建国 onClick="return checkCountry()">
			<input type=reset value=クリア></td></tr></form></table>
		-----END-----
		}
	&FOOTER;
}
sub MAKE_T2{
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&DBM_CONVERT('C',"$PL_VALUES[5]");&UNLOCK;
	&CUSTOM_HEADER('Main');&DBM_INPORT(P);
	if ($PL_VALUES[5]){
		if ($PL_VALUES[6] != 1 && !$PL_VALUES[28] && ($CL_VALUES[2] || $CL_VALUES[3] || $CL_VALUES[4])){
			&JScfm(checkInteam1,"入隊します。よろしいですか？");
			print "<tr><td $BgColor>";

			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
			print "<tr><td>部隊入隊</td><td><select name=inunit>\n";

			for ($i=2;$i <= 4; $i++){
				if ($CL_VALUES[$i]){print "<option value=\"$CL_VALUES[$i]\">$CL_VALUES[$i]\n";}
			}
			print "</select></td><td>\n";
			print "<input name=\"Cmode\" type=submit value=\"入隊\" onClick=\"return checkInteam1()\"></td></tr></table>";

		}elsif ($PL_VALUES[6] != 1 && $PL_VALUES[28]){
			&JScfm(checkOutteam,"除隊します。よろしいですか？");
			print "<tr><td $BgColor><input name=\"Cmode\" type=submit value=\"除隊\" onClick=\"return checkOutteam()\"></td></tr>\n";
		}
		if ($PL_VALUES[6] == 0 && (($CL_VALUES[2] && $CL_VALUES[2] ne "") || ($CL_VALUES[3] && $CL_VALUES[3] ne "") || ($CL_VALUES[4] && $CL_VALUES[4] ne "")) && $PL_VALUES[0] >= 100){
			&JScfm(checkInteam2,"隊長就任します。よろしいですか？");
			print "<tr><td $BgColor>";

			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
			print "<tr><td>隊長就任</td><td><select name=team>\n";

			for ($i=2;$i <= 4; $i++){
				while (my($key,$value) = each %P){
					my@VS_VALUE = split(/\s/,$value);

					if($CL_VALUES[$i] eq "$VS_VALUE[28]" && $VS_VALUE[6] == -1){
						$tflag[$i]=1;
					}
				}
				print "<option value=\"$CL_VALUES[$i]\">$CL_VALUES[$i]\n" if !$tflag[$i] && $CL_VALUES[$i];
			}
			print "</select></td><td>\n";
			print "<input name=\"Cmode\" type=submit value=\"隊長就任\" onClick=\"return checkInteam2()\"></td></tr></table>";
		}
		if (!$PL_VALUES[28] && $PL_VALUES[8] >= $MAKE_TEAM && $PL_VALUES[0] >= 150 && (!$CL_VALUES[2] || !$CL_VALUES[3] || !$CL_VALUES[4]) && $PL_VALUES[5]){
		print << "		-----END-----";
			<SCRIPT language="JavaScript">
			function checkUnit1(){
			if (document.Ms.uname.value == ''){alert("部隊名が未記入です。");return false; }
			else if (confirm('部隊作成します。よろしいですか？') == true){
					window.location.replace("$BACKFR");return true;
			}else{return false}
			}
			</script>
			<tr><td $BgColor>

			<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">
			<tr><td>部隊作成</td><td><input type=text name="uname" size=25 maxlength=15 $STYLE_L></td><td><input name="Cmode" type=submit value="部隊作成" onClick="return checkUnit1()"></td></tr></table>
		-----END-----
		}
		if ($PL_VALUES[6] == -1 && $PL_VALUES[5] && $PL_VALUES[8] >= $NAME_TEAM &&
		($CL_VALUES[2] eq $PL_VALUES[28] || $CL_VALUES[3] eq $PL_VALUES[28] || $CL_VALUES[4] eq $PL_VALUES[28])){
		print << "		-----END-----";
			<SCRIPT language="JavaScript">
			function checkUnit2(){
			if (document.Ms.uname.value == ''){alert("部隊名が未記入です。");return false; }
			else if (confirm('部隊再編成します。よろしいですか？') == true){
					window.location.replace("$BACKFR");return true;
			}else{return false}
			}
			</script>
			<tr><td $BgColor>

			<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">
			<tr><td>部隊再編成</td><td><input type=text name="suname" size=25 maxlength=15 $STYLE_L></td><td><input name="Cmode" type=submit value="部隊再編" onClick="return checkUnit2()"></td></tr></table>

		-----END-----
		}
		if ($PL_VALUES[6] == 1 && !$PL_VALUES[28] && ($CL_VALUES[2] || $CL_VALUES[3] || $CL_VALUES[4])){
			&JScfm(checkInteam,"部隊を解散します。よろしいですか？");
			print "<tr><td $BgColor>";

			print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
			print "<tr><td>部隊解散</td><td><select name=delunit>\n";

			for ($i=2;$i <= 4; $i++){
				if ($CL_VALUES[$i]){print "<option value=\"$CL_VALUES[$i]\">$CL_VALUES[$i]\n";}
			}
			print "</select></td><td>\n";
			print "<input name=\"Cmode\" type=submit value=\"解散\" onClick=\"return checkInteam()\"></td></tr></table>";
		}
	print "<tr><td $BgColor><b>部隊コマンドは使用できません。</b>" if !$CL_VALUES[2] && !$CL_VALUES[3] && !$CL_VALUES[4] && $PL_VALUES[0] < 150;
	print "</td></tr></form></table>\n";
	}

	&FOOTER;
}
1;

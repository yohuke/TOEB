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
sub KOUKENSET2 {
	&CUSTOM_HEADER('Main');
	require "./$LOG_FOLDER/$HASH_DATA";
	require "./$LOG_FOLDER/$KOUKEN_DATA";
	&LOCK;&DBM_CONVERT('P',"$FORM{pname}");&UNLOCK;
#"

#	local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#	local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#	local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#	local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);
#	local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
#	local($WN_T,$WLV_T) = split(/!/,$PL_VALUES[42]);
#	local($WN_U,$WLV_U) = split(/!/,$PL_VALUES[43]);
#	local($WN_Y,$WLV_Y) = split(/!/,$PL_VALUES[46]);
#	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
#	@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
#	@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
#	@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});
#	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
#	@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
#	@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});
#	@WN_sY=split(/\,/,$WEAPON_LIST{"$WN_Y"});
#	$WLV_A=int $WLV_A/$WEAPON_LVUP;
#	$WLV_B=int $WLV_B/$WEAPON_LVUP;
#	$WLV_C=int $WLV_C/$WEAPON_LVUP;
#	$WLV_D=int $WLV_D/$WEAPON_LVUP;
#	$WLV_S=int $WLV_S/$WEAPON_LVUP;
#	$WLV_T=int $WLV_T/$WEAPON_LVUP;
#	$WLV_U=int $WLV_U/$WEAPON_LVUP;
#	$WLV_Y=int $WLV_Y/$WEAPON_LVUP;


	local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);
	local($WN_B,$WLV_B,$WBEnt,$WB03,$WB04,$WB05,$WB06,$WB07,$WB08,$WB09,$WB10,$WB11,$WB12,$WB13,$WB14,$WB15,$WB16,$WB17,$WB18,$WB19,$WB20,$WB21,$WB22,$WB23,$WB24,$WB25,$WB26,$WB27,$WB28,$WB29,$WB30,$WB31,$WB32,$WB33,$WB34,$WB35,$WB36,$WB37,$WB38,$WB39,$WB40,$WB41,$WB42) = split(/!/,$PL_VALUES[10]);
	local($WN_C,$WLV_C,$WCEnt,$WC03,$WC04,$WC05,$WC06,$WC07,$WC08,$WC09,$WC10,$WC11,$WC12,$WC13,$WC14,$WC15,$WC16,$WC17,$WC18,$WC19,$WC20,$WC21,$WC22,$WC23,$WC24,$WC25,$WC26,$WC27,$WC28,$WC29,$WC30,$WC31,$WC32,$WC33,$WC34,$WC35,$WC36,$WC37,$WC38,$WC39,$WC40,$WC41,$WC42) = split(/!/,$PL_VALUES[11]);
	local($WN_D,$WLV_D,$WDEnt,$WD03,$WD04,$WD05,$WD06,$WD07,$WD08,$WD09,$WD10,$WD11,$WD12,$WD13,$WD14,$WD15,$WD16,$WD17,$WD18,$WD19,$WD20,$WD21,$WD22,$WD23,$WD24,$WD25,$WD26,$WD27,$WD28,$WD29,$WD30,$WD31,$WD32,$WD33,$WD34,$WD35,$WD36,$WD37,$WD38,$WD39,$WD40,$WD41,$WD42) = split(/!/,$PL_VALUES[38]);

	local($WN_S,$WLV_S,$WSEnt) = split(/!/,$PL_VALUES[41]);
	local($WN_T,$WLV_T,$WTEnt) = split(/!/,$PL_VALUES[42]);
	local($WN_U,$WLV_U,$WUEnt) = split(/!/,$PL_VALUES[43]);
	local($WN_Y,$WLV_Y,$WYEnt,$WY03,$WY04,$WY05,$WY06,$WY07,$WY08,$WY09,$WY10,$WY11,$WY12,$WY13,$WY14,$WY15,$WY16,$WY17,$WY18,$WY19,$WY20,$WY21,$WY22,$WY23,$WY24,$WY25,$WY26,$WY27,$WY28,$WY29,$WY30,$WY31,$WY32,$WY33,$WY34,$WY35,$WY36,$WY37,$WY38,$WY39,$WY40,$WY41,$WY42) = split(/!/,$PL_VALUES[46]);

	local($WN_E,$WLV_E,$WEEnt,$WE03,$WE04,$WE05,$WE06,$WE07,$WE08,$WE09,$WE10,$WE11,$WE12,$WE13,$WE14,$WE15,$WE16,$WE17,$WE18,$WE19,$WE20,$WE21,$WE22,$WE23,$WE24,$WE25,$WE26,$WE27,$WE28,$WE29,$WE30,$WE31,$WE32,$WE33,$WE34,$WE35,$WE36,$WE37,$WE38,$WE39,$WE40,$WE41,$WE42) = split(/!/,$PL_VALUES[55]);
	local($WN_F,$WLV_F,$WFEnt,$WF03,$WF04,$WF05,$WF06,$WF07,$WF08,$WF09,$WF10,$WF11,$WF12,$WF13,$WF14,$WF15,$WF16,$WF17,$WF18,$WF19,$WF20,$WF21,$WF22,$WF23,$WF24,$WF25,$WF26,$WF27,$WF28,$WF29,$WF30,$WF31,$WF32,$WF33,$WF34,$WF35,$WF36,$WF37,$WF38,$WF39,$WF40,$WF41,$WF42) = split(/!/,$PL_VALUES[56]);
	local($WN_G,$WLV_G,$WGEnt,$WG03,$WG04,$WG05,$WG06,$WG07,$WG08,$WG09,$WG10,$WG11,$WG12,$WG13,$WG14,$WG15,$WG16,$WG17,$WG18,$WG19,$WG20,$WG21,$WG22,$WG23,$WG24,$WG25,$WG26,$WG27,$WG28,$WG29,$WG30,$WG31,$WG32,$WG33,$WG34,$WG35,$WG36,$WG37,$WG38,$WG39,$WG40,$WG41,$WG42) = split(/!/,$PL_VALUES[57]);
	local($WN_H,$WLV_H,$WHEnt,$WH03,$WH04,$WH05,$WH06,$WH07,$WH08,$WH09,$WH10,$WH11,$WH12,$WH13,$WH14,$WH15,$WH16,$WH17,$WH18,$WH19,$WH20,$WH21,$WH22,$WH23,$WH24,$WH25,$WH26,$WH27,$WH28,$WH29,$WH30,$WH31,$WH32,$WH33,$WH34,$WH35,$WH36,$WH37,$WH38,$WH39,$WH40,$WH41,$WH42) = split(/!/,$PL_VALUES[58]);
	local($WN_I,$WLV_I,$WIEnt,$WI03,$WI04,$WI05,$WI06,$WI07,$WI08,$WI09,$WI10,$WI11,$WI12,$WI13,$WI14,$WI15,$WI16,$WI17,$WI18,$WI19,$WI20,$WI21,$WI22,$WI23,$WI24,$WI25,$WI26,$WI27,$WI28,$WI29,$WI30,$WI31,$WI32,$WI33,$WI34,$WI35,$WI36,$WI37,$WI38,$WI39,$WI40,$WI41,$WI42) = split(/!/,$PL_VALUES[59]);
	local($WN_J,$WLV_J,$WJEnt,$WJ03,$WJ04,$WJ05,$WJ06,$WJ07,$WJ08,$WJ09,$WJ10,$WJ11,$WJ12,$WJ13,$WJ14,$WJ15,$WJ16,$WJ17,$WJ18,$WJ19,$WJ20,$WJ21,$WJ22,$WJ23,$WJ24,$WJ25,$WJ26,$WJ27,$WJ28,$WJ29,$WJ30,$WJ31,$WJ32,$WJ33,$WJ34,$WJ35,$WJ36,$WJ37,$WJ38,$WJ39,$WJ40,$WJ41,$WJ42) = split(/!/,$PL_VALUES[60]);

	local($WN_K,$WLV_K,$WKEnt) = split(/!/,$PL_VALUES[61]);
	local($WN_L,$WLV_L,$WLEnt) = split(/!/,$PL_VALUES[62]);
	local($WN_M,$WLV_M,$WMEnt) = split(/!/,$PL_VALUES[63]);




	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
	@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
	@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
	@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});
	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
	@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
	@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});
	@WN_sY=split(/\,/,$WEAPON_LIST{"$WN_Y"});

	@WN_sE=split(/\,/,$WEAPON_LIST{"$WN_E"});
	@WN_sF=split(/\,/,$WEAPON_LIST{"$WN_F"});
	@WN_sG=split(/\,/,$WEAPON_LIST{"$WN_G"});
	@WN_sH=split(/\,/,$WEAPON_LIST{"$WN_H"});
	@WN_sI=split(/\,/,$WEAPON_LIST{"$WN_I"});
	@WN_sJ=split(/\,/,$WEAPON_LIST{"$WN_J"});

	@WN_sK=split(/\,/,$WEAPON_LIST{"$WN_K"});
	@WN_sL=split(/\,/,$WEAPON_LIST{"$WN_L"});
	@WN_sM=split(/\,/,$WEAPON_LIST{"$WN_M"});



	$WLV_A=int $WLV_A/$WEAPON_LVUP;
	$WLV_B=int $WLV_B/$WEAPON_LVUP;
	$WLV_C=int $WLV_C/$WEAPON_LVUP;
	$WLV_D=int $WLV_D/$WEAPON_LVUP;
	$WLV_S=int $WLV_S/$WEAPON_LVUP;
	$WLV_T=int $WLV_T/$WEAPON_LVUP;
	$WLV_U=int $WLV_U/$WEAPON_LVUP;
	$WLV_Y=int $WLV_Y/$WEAPON_LVUP;

	$WLV_E=int $WLV_E/$WEAPON_LVUP;
	$WLV_F=int $WLV_F/$WEAPON_LVUP;
	$WLV_G=int $WLV_G/$WEAPON_LVUP;
	$WLV_H=int $WLV_H/$WEAPON_LVUP;
	$WLV_I=int $WLV_I/$WEAPON_LVUP;
	$WLV_J=int $WLV_J/$WEAPON_LVUP;

	$WLV_K=int $WLV_K/$WEAPON_LVUP;
	$WLV_L=int $WLV_L/$WEAPON_LVUP;
	$WLV_M=int $WLV_M/$WEAPON_LVUP;


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

	if($WE03 ne ""){$WN_sE[7] .= "!ENTSTR00$WE03";$WN_sE[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WE04 ne ""){$WN_sE[7] .= "!ENTVIT00$WE04";$WN_sE[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WE05 ne ""){$WN_sE[7] .= "!ENTAGI00$WE05";$WN_sE[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WE06 ne ""){$WN_sE[7] .= "!ENTDEX00$WE06";$WN_sE[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WE07 ne ""){$WN_sE[7] .= "!ENTLIF00$WE07";$WN_sE[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WE08 ne ""){$WN_sE[7] .= "!ENTMBU00$WE08";$WN_sE[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WE09 ne ""){$WN_sE[7] .= "!ENTNKI00$WE09";$WN_sE[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WE10 ne ""){$WN_sE[7] .= "!ENTNGU00$WE10";$WN_sE[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WE11 ne ""){$WN_sE[7] .= "!ENTTUP00$WE11";$WN_sE[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WE12 ne ""){$WN_sE[7] .= "!ENTMFU00$WE12";$WN_sE[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WE13 ne ""){$WN_sE[7] .= "!ENTRES00$WE13";$WN_sE[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WE14 ne ""){$WN_sE[7] .= "!ENTFIB00$WE14";$WN_sE[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WE15 ne ""){$WN_sE[7] .= "!ENTWAB00$WE15";$WN_sE[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WE16 ne ""){$WN_sE[7] .= "!ENTEAB00$WE16";$WN_sE[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WE17 ne ""){$WN_sE[7] .= "!ENTWIB00$WE17";$WN_sE[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WE18 ne ""){$WN_sE[7] .= "!ENTSAB00$WE18";$WN_sE[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WE19 ne ""){$WN_sE[7] .= "!ENTDAB00$WE19";$WN_sE[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WE20 ne ""){$WN_sE[7] .= "!ENTFIG00$WE20";$WN_sE[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WE21 ne ""){$WN_sE[7] .= "!ENTWAG00$WE21";$WN_sE[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WE22 ne ""){$WN_sE[7] .= "!ENTEAG00$WE22";$WN_sE[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WE23 ne ""){$WN_sE[7] .= "!ENTWIG00$WE23";$WN_sE[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WE24 ne ""){$WN_sE[7] .= "!ENTSAG00$WE24";$WN_sE[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WE25 ne ""){$WN_sE[7] .= "!ENTDAG00$WE25";$WN_sE[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WE26 ne ""){$WN_sE[7] .= "!ENTIMG00$WE26";$WN_sE[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WE27 ne ""){$WN_sE[7] .= "!ENTGOU00$WE27";$WN_sE[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WE28 ne ""){$WN_sE[7] .= "!ENTHHP00$WE28";$WN_sE[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WE29 ne ""){$WN_sE[7] .= "!ENTMMP00$WE29";$WN_sE[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WE30 ne ""){$WN_sE[7] .= "!ENTDAM00$WE30";$WN_sE[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WE31 ne ""){$WN_sE[7] .= "!ENTHEA00$WE31";$WN_sE[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WE32 ne ""){$WN_sE[7] .= "!ENTCRI00$WE32";$WN_sE[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WE33 ne ""){$WN_sE[7] .= "!ENTBRK00$WE33";$WN_sE[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WF03 ne ""){$WN_sF[7] .= "!ENTSTR00$WF03";$WN_sF[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WF04 ne ""){$WN_sF[7] .= "!ENTVIT00$WF04";$WN_sF[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WF05 ne ""){$WN_sF[7] .= "!ENTAGI00$WF05";$WN_sF[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WF06 ne ""){$WN_sF[7] .= "!ENTDEX00$WF06";$WN_sF[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WF07 ne ""){$WN_sF[7] .= "!ENTLIF00$WF07";$WN_sF[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WF08 ne ""){$WN_sF[7] .= "!ENTMBU00$WF08";$WN_sF[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WF09 ne ""){$WN_sF[7] .= "!ENTNKI00$WF09";$WN_sF[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WF10 ne ""){$WN_sF[7] .= "!ENTNGU00$WF10";$WN_sF[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WF11 ne ""){$WN_sF[7] .= "!ENTTUP00$WF11";$WN_sF[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WF12 ne ""){$WN_sF[7] .= "!ENTMFU00$WF12";$WN_sF[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WF13 ne ""){$WN_sF[7] .= "!ENTRES00$WF13";$WN_sF[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WF14 ne ""){$WN_sF[7] .= "!ENTFIB00$WF14";$WN_sF[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WF15 ne ""){$WN_sF[7] .= "!ENTWAB00$WF15";$WN_sF[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WF16 ne ""){$WN_sF[7] .= "!ENTEAB00$WF16";$WN_sF[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WF17 ne ""){$WN_sF[7] .= "!ENTWIB00$WF17";$WN_sF[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WF18 ne ""){$WN_sF[7] .= "!ENTSAB00$WF18";$WN_sF[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WF19 ne ""){$WN_sF[7] .= "!ENTDAB00$WF19";$WN_sF[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WF20 ne ""){$WN_sF[7] .= "!ENTFIG00$WF20";$WN_sF[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WF21 ne ""){$WN_sF[7] .= "!ENTWAG00$WF21";$WN_sF[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WF22 ne ""){$WN_sF[7] .= "!ENTEAG00$WF22";$WN_sF[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WF23 ne ""){$WN_sF[7] .= "!ENTWIG00$WF23";$WN_sF[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WF24 ne ""){$WN_sF[7] .= "!ENTSAG00$WF24";$WN_sF[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WF25 ne ""){$WN_sF[7] .= "!ENTDAG00$WF25";$WN_sF[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WF26 ne ""){$WN_sF[7] .= "!ENTIMG00$WF26";$WN_sF[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WF27 ne ""){$WN_sF[7] .= "!ENTGOU00$WF27";$WN_sF[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WF28 ne ""){$WN_sF[7] .= "!ENTHHP00$WF28";$WN_sF[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WF29 ne ""){$WN_sF[7] .= "!ENTMMP00$WF29";$WN_sF[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WF30 ne ""){$WN_sF[7] .= "!ENTDAM00$WF30";$WN_sF[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WF31 ne ""){$WN_sF[7] .= "!ENTHEA00$WF31";$WN_sF[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WF32 ne ""){$WN_sF[7] .= "!ENTCRI00$WF32";$WN_sF[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WF33 ne ""){$WN_sF[7] .= "!ENTBRK00$WF33";$WN_sF[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WG03 ne ""){$WN_sG[7] .= "!ENTSTR00$WG03";$WN_sG[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WG04 ne ""){$WN_sG[7] .= "!ENTVIT00$WG04";$WN_sG[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WG05 ne ""){$WN_sG[7] .= "!ENTAGI00$WG05";$WN_sG[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WG06 ne ""){$WN_sG[7] .= "!ENTDEX00$WG06";$WN_sG[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WG07 ne ""){$WN_sG[7] .= "!ENTLIF00$WG07";$WN_sG[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WG08 ne ""){$WN_sG[7] .= "!ENTMBU00$WG08";$WN_sG[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WG09 ne ""){$WN_sG[7] .= "!ENTNKI00$WG09";$WN_sG[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WG10 ne ""){$WN_sG[7] .= "!ENTNGU00$WG10";$WN_sG[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WG11 ne ""){$WN_sG[7] .= "!ENTTUP00$WG11";$WN_sG[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WG12 ne ""){$WN_sG[7] .= "!ENTMFU00$WG12";$WN_sG[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WG13 ne ""){$WN_sG[7] .= "!ENTRES00$WG13";$WN_sG[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WG14 ne ""){$WN_sG[7] .= "!ENTFIB00$WG14";$WN_sG[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WG15 ne ""){$WN_sG[7] .= "!ENTWAB00$WG15";$WN_sG[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WG16 ne ""){$WN_sG[7] .= "!ENTEAB00$WG16";$WN_sG[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WG17 ne ""){$WN_sG[7] .= "!ENTWIB00$WG17";$WN_sG[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WG18 ne ""){$WN_sG[7] .= "!ENTSAB00$WG18";$WN_sG[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WG19 ne ""){$WN_sG[7] .= "!ENTDAB00$WG19";$WN_sG[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WG20 ne ""){$WN_sG[7] .= "!ENTFIG00$WG20";$WN_sG[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WG21 ne ""){$WN_sG[7] .= "!ENTWAG00$WG21";$WN_sG[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WG22 ne ""){$WN_sG[7] .= "!ENTEAG00$WG22";$WN_sG[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WG23 ne ""){$WN_sG[7] .= "!ENTWIG00$WG23";$WN_sG[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WG24 ne ""){$WN_sG[7] .= "!ENTSAG00$WG24";$WN_sG[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WG25 ne ""){$WN_sG[7] .= "!ENTDAG00$WG25";$WN_sG[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WG26 ne ""){$WN_sG[7] .= "!ENTIMG00$WG26";$WN_sG[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WG27 ne ""){$WN_sG[7] .= "!ENTGOU00$WG27";$WN_sG[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WG28 ne ""){$WN_sG[7] .= "!ENTHHP00$WG28";$WN_sG[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WG29 ne ""){$WN_sG[7] .= "!ENTMMP00$WG29";$WN_sG[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WG30 ne ""){$WN_sG[7] .= "!ENTDAM00$WG30";$WN_sG[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WG31 ne ""){$WN_sG[7] .= "!ENTHEA00$WG31";$WN_sG[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WG32 ne ""){$WN_sG[7] .= "!ENTCRI00$WG32";$WN_sG[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WG33 ne ""){$WN_sG[7] .= "!ENTBRK00$WG33";$WN_sG[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WH03 ne ""){$WN_sH[7] .= "!ENTSTR00$WH03";$WN_sH[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WH04 ne ""){$WN_sH[7] .= "!ENTVIT00$WH04";$WN_sH[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WH05 ne ""){$WN_sH[7] .= "!ENTAGI00$WH05";$WN_sH[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WH06 ne ""){$WN_sH[7] .= "!ENTDEX00$WH06";$WN_sH[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WH07 ne ""){$WN_sH[7] .= "!ENTLIF00$WH07";$WN_sH[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WH08 ne ""){$WN_sH[7] .= "!ENTMBU00$WH08";$WN_sH[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WH09 ne ""){$WN_sH[7] .= "!ENTNKI00$WH09";$WN_sH[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WH10 ne ""){$WN_sH[7] .= "!ENTNGU00$WH10";$WN_sH[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WH11 ne ""){$WN_sH[7] .= "!ENTTUP00$WH11";$WN_sH[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WH12 ne ""){$WN_sH[7] .= "!ENTMFU00$WH12";$WN_sH[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WH13 ne ""){$WN_sH[7] .= "!ENTRES00$WH13";$WN_sH[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WH14 ne ""){$WN_sH[7] .= "!ENTFIB00$WH14";$WN_sH[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WH15 ne ""){$WN_sH[7] .= "!ENTWAB00$WH15";$WN_sH[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WH16 ne ""){$WN_sH[7] .= "!ENTEAB00$WH16";$WN_sH[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WH17 ne ""){$WN_sH[7] .= "!ENTWIB00$WH17";$WN_sH[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WH18 ne ""){$WN_sH[7] .= "!ENTSAB00$WH18";$WN_sH[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WH19 ne ""){$WN_sH[7] .= "!ENTDAB00$WH19";$WN_sH[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WH20 ne ""){$WN_sH[7] .= "!ENTFIG00$WH20";$WN_sH[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WH21 ne ""){$WN_sH[7] .= "!ENTWAG00$WH21";$WN_sH[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WH22 ne ""){$WN_sH[7] .= "!ENTEAG00$WH22";$WN_sH[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WH23 ne ""){$WN_sH[7] .= "!ENTWIG00$WH23";$WN_sH[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WH24 ne ""){$WN_sH[7] .= "!ENTSAG00$WH24";$WN_sH[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WH25 ne ""){$WN_sH[7] .= "!ENTDAG00$WH25";$WN_sH[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WH26 ne ""){$WN_sH[7] .= "!ENTIMG00$WH26";$WN_sH[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WH27 ne ""){$WN_sH[7] .= "!ENTGOU00$WH27";$WN_sH[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WH28 ne ""){$WN_sH[7] .= "!ENTHHP00$WH28";$WN_sH[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WH29 ne ""){$WN_sH[7] .= "!ENTMMP00$WH29";$WN_sH[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WH30 ne ""){$WN_sH[7] .= "!ENTDAM00$WH30";$WN_sH[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WH31 ne ""){$WN_sH[7] .= "!ENTHEA00$WH31";$WN_sH[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WH32 ne ""){$WN_sH[7] .= "!ENTCRI00$WH32";$WN_sH[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WH33 ne ""){$WN_sH[7] .= "!ENTBRK00$WH33";$WN_sH[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WI03 ne ""){$WN_sI[7] .= "!ENTSTR00$WI03";$WN_sI[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WI04 ne ""){$WN_sI[7] .= "!ENTVIT00$WI04";$WN_sI[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WI05 ne ""){$WN_sI[7] .= "!ENTAGI00$WI05";$WN_sI[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WI06 ne ""){$WN_sI[7] .= "!ENTDEX00$WI06";$WN_sI[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WI07 ne ""){$WN_sI[7] .= "!ENTLIF00$WI07";$WN_sI[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WI08 ne ""){$WN_sI[7] .= "!ENTMBU00$WI08";$WN_sI[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WI09 ne ""){$WN_sI[7] .= "!ENTNKI00$WI09";$WN_sI[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WI10 ne ""){$WN_sI[7] .= "!ENTNGU00$WI10";$WN_sI[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WI11 ne ""){$WN_sI[7] .= "!ENTTUP00$WI11";$WN_sI[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WI12 ne ""){$WN_sI[7] .= "!ENTMFU00$WI12";$WN_sI[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WI13 ne ""){$WN_sI[7] .= "!ENTRES00$WI13";$WN_sI[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WI14 ne ""){$WN_sI[7] .= "!ENTFIB00$WI14";$WN_sI[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WI15 ne ""){$WN_sI[7] .= "!ENTWAB00$WI15";$WN_sI[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WI16 ne ""){$WN_sI[7] .= "!ENTEAB00$WI16";$WN_sI[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WI17 ne ""){$WN_sI[7] .= "!ENTWIB00$WI17";$WN_sI[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WI18 ne ""){$WN_sI[7] .= "!ENTSAB00$WI18";$WN_sI[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WI19 ne ""){$WN_sI[7] .= "!ENTDAB00$WI19";$WN_sI[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WI20 ne ""){$WN_sI[7] .= "!ENTFIG00$WI20";$WN_sI[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WI21 ne ""){$WN_sI[7] .= "!ENTWAG00$WI21";$WN_sI[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WI22 ne ""){$WN_sI[7] .= "!ENTEAG00$WI22";$WN_sI[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WI23 ne ""){$WN_sI[7] .= "!ENTWIG00$WI23";$WN_sI[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WI24 ne ""){$WN_sI[7] .= "!ENTSAG00$WI24";$WN_sI[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WI25 ne ""){$WN_sI[7] .= "!ENTDAG00$WI25";$WN_sI[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WI26 ne ""){$WN_sI[7] .= "!ENTIMG00$WI26";$WN_sI[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WI27 ne ""){$WN_sI[7] .= "!ENTGOU00$WI27";$WN_sI[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WI28 ne ""){$WN_sI[7] .= "!ENTHHP00$WI28";$WN_sI[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WI29 ne ""){$WN_sI[7] .= "!ENTMMP00$WI29";$WN_sI[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WI30 ne ""){$WN_sI[7] .= "!ENTDAM00$WI30";$WN_sI[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WI31 ne ""){$WN_sI[7] .= "!ENTHEA00$WI31";$WN_sI[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WI32 ne ""){$WN_sI[7] .= "!ENTCRI00$WI32";$WN_sI[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WI33 ne ""){$WN_sI[7] .= "!ENTBRK00$WI33";$WN_sI[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	if($WJ03 ne ""){$WN_sJ[7] .= "!ENTSTR00$WJ03";$WN_sJ[7] =~ s/!ENTSTR0010/!ENTSTR010/g;}
	if($WJ04 ne ""){$WN_sJ[7] .= "!ENTVIT00$WJ04";$WN_sJ[7] =~ s/!ENTVIT0010/!ENTVIT010/g;}
	if($WJ05 ne ""){$WN_sJ[7] .= "!ENTAGI00$WJ05";$WN_sJ[7] =~ s/!ENTAGI0010/!ENTAGI010/g;}
	if($WJ06 ne ""){$WN_sJ[7] .= "!ENTDEX00$WJ06";$WN_sJ[7] =~ s/!ENTDEX0010/!ENTDEX010/g;}
	if($WJ07 ne ""){$WN_sJ[7] .= "!ENTLIF00$WJ07";$WN_sJ[7] =~ s/!ENTLIF0010/!ENTLIF010/g;}
	if($WJ08 ne ""){$WN_sJ[7] .= "!ENTMBU00$WJ08";$WN_sJ[7] =~ s/!ENTMBU0010/!ENTMBU010/g;}
	if($WJ09 ne ""){$WN_sJ[7] .= "!ENTNKI00$WJ09";$WN_sJ[7] =~ s/!ENTNKI0010/!ENTNKI010/g;}
	if($WJ10 ne ""){$WN_sJ[7] .= "!ENTNGU00$WJ10";$WN_sJ[7] =~ s/!ENTNGU0010/!ENTNGU010/g;}
	if($WJ11 ne ""){$WN_sJ[7] .= "!ENTTUP00$WJ11";$WN_sJ[7] =~ s/!ENTTUP0010/!ENTTUP010/g;}
	if($WJ12 ne ""){$WN_sJ[7] .= "!ENTMFU00$WJ12";$WN_sJ[7] =~ s/!ENTMFU0010/!ENTMFU010/g;}
	if($WJ13 ne ""){$WN_sJ[7] .= "!ENTRES00$WJ13";$WN_sJ[7] =~ s/!ENTRES0010/!ENTRES010/g;}
	if($WJ14 ne ""){$WN_sJ[7] .= "!ENTFIB00$WJ14";$WN_sJ[7] =~ s/!ENTFIB0010/!ENTFIB010/g;}
	if($WJ15 ne ""){$WN_sJ[7] .= "!ENTWAB00$WJ15";$WN_sJ[7] =~ s/!ENTWAB0010/!ENTWAB010/g;}
	if($WJ16 ne ""){$WN_sJ[7] .= "!ENTEAB00$WJ16";$WN_sJ[7] =~ s/!ENTEAB0010/!ENTEAB010/g;}
	if($WJ17 ne ""){$WN_sJ[7] .= "!ENTWIB00$WJ17";$WN_sJ[7] =~ s/!ENTWIB0010/!ENTWIB010/g;}
	if($WJ18 ne ""){$WN_sJ[7] .= "!ENTSAB00$WJ18";$WN_sJ[7] =~ s/!ENTSAB0010/!ENTSAB010/g;}
	if($WJ19 ne ""){$WN_sJ[7] .= "!ENTDAB00$WJ19";$WN_sJ[7] =~ s/!ENTDAB0010/!ENTDAB010/g;}
	if($WJ20 ne ""){$WN_sJ[7] .= "!ENTFIG00$WJ20";$WN_sJ[7] =~ s/!ENTFIG0010/!ENTFIG010/g;}
	if($WJ21 ne ""){$WN_sJ[7] .= "!ENTWAG00$WJ21";$WN_sJ[7] =~ s/!ENTWAG0010/!ENTWAG010/g;}
	if($WJ22 ne ""){$WN_sJ[7] .= "!ENTEAG00$WJ22";$WN_sJ[7] =~ s/!ENTEAG0010/!ENTEAG010/g;}
	if($WJ23 ne ""){$WN_sJ[7] .= "!ENTWIG00$WJ23";$WN_sJ[7] =~ s/!ENTWIG0010/!ENTWIG010/g;}
	if($WJ24 ne ""){$WN_sJ[7] .= "!ENTSAG00$WJ24";$WN_sJ[7] =~ s/!ENTSAG0010/!ENTSAG010/g;}
	if($WJ25 ne ""){$WN_sJ[7] .= "!ENTDAG00$WJ25";$WN_sJ[7] =~ s/!ENTDAG0010/!ENTDAG010/g;}
	if($WJ26 ne ""){$WN_sJ[7] .= "!ENTIMG00$WJ26";$WN_sJ[7] =~ s/!ENTIMG0010/!ENTIMG010/g;}
	if($WJ27 ne ""){$WN_sJ[7] .= "!ENTGOU00$WJ27";$WN_sJ[7] =~ s/!ENTGOU0010/!ENTGOU010/g;}
	if($WJ28 ne ""){$WN_sJ[7] .= "!ENTHHP00$WJ28";$WN_sJ[7] =~ s/!ENTHHP0010/!ENTHHP010/g;}
	if($WJ29 ne ""){$WN_sJ[7] .= "!ENTMMP00$WJ29";$WN_sJ[7] =~ s/!ENTMMP0010/!ENTMMP010/g;}
	if($WJ30 ne ""){$WN_sJ[7] .= "!ENTDAM00$WJ30";$WN_sJ[7] =~ s/!ENTDAM0010/!ENTDAM010/g;}
	if($WJ31 ne ""){$WN_sJ[7] .= "!ENTHEA00$WJ31";$WN_sJ[7] =~ s/!ENTHEA0010/!ENTHEA010/g;}
	if($WJ32 ne ""){$WN_sJ[7] .= "!ENTCRI00$WJ32";$WN_sJ[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
	if($WJ33 ne ""){$WN_sJ[7] .= "!ENTBRK00$WJ33";$WN_sJ[7] =~ s/!ENTBRK0010/!ENTBRK010/g;}

	$Pl_WeaponNameA2="$WN_sA[0](Lv$WLV_A)";
	$Pl_WeaponNameB2="$WN_sB[0](Lv$WLV_B)";
	$Pl_WeaponNameC2="$WN_sC[0](Lv$WLV_C)";
	$Pl_WeaponNameD2="$WN_sD[0](Lv$WLV_D)";
	$Pl_WeaponNameS2="$WN_sS[0](Lv$WLV_S)";
	$Pl_WeaponNameT2="$WN_sT[0](Lv$WLV_T)";
	$Pl_WeaponNameU2="$WN_sU[0](Lv$WLV_U)";
	$Pl_WeaponNameY2="$WN_sY[0](Lv$WLV_Y)";

	$Pl_WeaponNameE2="$WN_sE[0](Lv$WLV_E)";
	$Pl_WeaponNameF2="$WN_sF[0](Lv$WLV_F)";
	$Pl_WeaponNameG2="$WN_sG[0](Lv$WLV_G)";
	$Pl_WeaponNameH2="$WN_sH[0](Lv$WLV_H)";
	$Pl_WeaponNameI2="$WN_sI[0](Lv$WLV_I)";
	$Pl_WeaponNameJ2="$WN_sJ[0](Lv$WLV_J)";

	$Pl_WeaponNameK2="$WN_sK[0](Lv$WLV_K)";
	$Pl_WeaponNameL2="$WN_sL[0](Lv$WLV_L)";
	$Pl_WeaponNameM2="$WN_sM[0](Lv$WLV_M)";


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

	#予備倉庫
	@Count_E = split(/!/,$PL_VALUES[55]);
	$Ent_E = 0;
	for ($LngEntCntE = 3; $LngEntCntE <= 33; $LngEntCntE++){
		if($Count_E[$LngEntCntE] > 0){$Ent_E = $Ent_E + 1;}
	}
	if($Ent_E > 0 && $Ent_E <= 2){$WN_sE[0] = "<font color=00ff00>$WN_sE[0]</font>";}
	elsif($Ent_E > 2 && $Ent_E <= 4){$WN_sE[0] = "<font color=ffff00>$WN_sE[0]</font>";}
	elsif($Ent_E > 4){$WN_sE[0] = "<font color=ffD700>$WN_sE[0]</font>";}

	@Count_F = split(/!/,$PL_VALUES[56]);
	$Ent_F = 0;
	for ($LngEntCntF = 3; $LngEntCntF <= 33; $LngEntCntF++){
		if($Count_F[$LngEntCntF] > 0){$Ent_F = $Ent_F + 1;}
	}
	if($Ent_F > 0 && $Ent_F <= 2){$WN_sF[0] = "<font color=00ff00>$WN_sF[0]</font>";}
	elsif($Ent_F > 2 && $Ent_F <= 4){$WN_sF[0] = "<font color=ffff00>$WN_sF[0]</font>";}
	elsif($Ent_F > 4){$WN_sF[0] = "<font color=ffD700>$WN_sF[0]</font>";}

	@Count_G = split(/!/,$PL_VALUES[57]);
	$Ent_G = 0;
	for ($LngEntCntG = 3; $LngEntCntG <= 33; $LngEntCntG++){
		if($Count_G[$LngEntCntG] > 0){$Ent_G = $Ent_G + 1;}
	}
	if($Ent_G > 0 && $Ent_G <= 2){$WN_sG[0] = "<font color=00ff00>$WN_sG[0]</font>";}
	elsif($Ent_G > 2 && $Ent_G <= 4){$WN_sG[0] = "<font color=ffff00>$WN_sG[0]</font>";}
	elsif($Ent_G > 4){$WN_sG[0] = "<font color=ffD700>$WN_sG[0]</font>";}

	@Count_H = split(/!/,$PL_VALUES[58]);
	$Ent_H = 0;
	for ($LngEntCntH = 3; $LngEntCntH <= 33; $LngEntCntH++){
		if($Count_H[$LngEntCntH] > 0){$Ent_H = $Ent_H + 1;}
	}
	if($Ent_H > 0 && $Ent_H <= 2){$WN_sH[0] = "<font color=00ff00>$WN_sH[0]</font>";}
	elsif($Ent_H > 2 && $Ent_H <= 4){$WN_sH[0] = "<font color=ffff00>$WN_sH[0]</font>";}
	elsif($Ent_H > 4){$WN_sH[0] = "<font color=ffD700>$WN_sH[0]</font>";}

	@Count_I = split(/!/,$PL_VALUES[59]);
	$Ent_I = 0;
	for ($LngEntCntI = 3; $LngEntCntI <= 33; $LngEntCntI++){
		if($Count_I[$LngEntCntI] > 0){$Ent_I = $Ent_I + 1;}
	}
	if($Ent_I > 0 && $Ent_I <= 2){$WN_sI[0] = "<font color=00ff00>$WN_sI[0]</font>";}
	elsif($Ent_I > 2 && $Ent_I <= 4){$WN_sI[0] = "<font color=ffff00>$WN_sI[0]</font>";}
	elsif($Ent_I > 4){$WN_sI[0] = "<font color=ffD700>$WN_sI[0]</font>";}

	@Count_J = split(/!/,$PL_VALUES[60]);
	$Ent_J = 0;
	for ($LngEntCntJ = 3; $LngEntCntJ <= 33; $LngEntCntJ++){
		if($Count_J[$LngEntCntJ] > 0){$Ent_J = $Ent_J + 1;}
	}
	if($Ent_J > 0 && $Ent_J <= 2){$WN_sJ[0] = "<font color=00ff00>$WN_sJ[0]</font>";}
	elsif($Ent_J > 2 && $Ent_J <= 4){$WN_sJ[0] = "<font color=ffff00>$WN_sJ[0]</font>";}
	elsif($Ent_J > 4){$WN_sJ[0] = "<font color=ffD700>$WN_sJ[0]</font>";}


	if($WAEnt ne "" && $WAEnt > 0){$WN_sA[0] = "＋$WAEnt $WN_sA[0]";}
	if($WBEnt ne "" && $WBEnt > 0){$WN_sB[0] = "＋$WBEnt $WN_sB[0]";}
	if($WCEnt ne "" && $WCEnt > 0){$WN_sC[0] = "＋$WCEnt $WN_sC[0]";}
	if($WDEnt ne "" && $WDEnt > 0){$WN_sD[0] = "＋$WDEnt $WN_sD[0]";}
	if($WSEnt ne "" && $WSEnt > 0){$WN_sS[0] = "＋$WSEnt $WN_sS[0]";}
	if($WTEnt ne "" && $WTEnt > 0){$WN_sT[0] = "＋$WTEnt $WN_sT[0]";}
	if($WUEnt ne "" && $WUEnt > 0){$WN_sU[0] = "＋$WUEnt $WN_sU[0]";}
	if($WYEnt ne "" && $WYEnt > 0){$WN_sY[0] = "＋$WYEnt $WN_sY[0]";}

	if($WEEnt ne "" && $WEEnt > 0){$WN_sE[0] = "＋$WEEnt $WN_sE[0]";}
	if($WFEnt ne "" && $WFEnt > 0){$WN_sF[0] = "＋$WFEnt $WN_sF[0]";}
	if($WGEnt ne "" && $WGEnt > 0){$WN_sG[0] = "＋$WGEnt $WN_sG[0]";}
	if($WHEnt ne "" && $WHEnt > 0){$WN_sH[0] = "＋$WHEnt $WN_sH[0]";}
	if($WIEnt ne "" && $WIEnt > 0){$WN_sI[0] = "＋$WIEnt $WN_sI[0]";}
	if($WJEnt ne "" && $WJEnt > 0){$WN_sJ[0] = "＋$WJEnt $WN_sJ[0]";}
	if($WKEnt ne "" && $WKEnt > 0){$WN_sK[0] = "＋$WKEnt $WN_sK[0]";}
	if($WLEnt ne "" && $WLEnt > 0){$WN_sL[0] = "＋$WLEnt $WN_sL[0]";}
	if($WMEnt ne "" && $WMEnt > 0){$WN_sM[0] = "＋$WMEnt $WN_sM[0]";}



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

	$EntCnt = 0;
	@WN_sE_ef = split(/!/,$WN_sE[7]);
	foreach $j (@WN_sE_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq9 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq9 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu9 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sF_ef = split(/!/,$WN_sF[7]);
	foreach $j (@WN_sF_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq10 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq10 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu10 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sG_ef = split(/!/,$WN_sG[7]);
	foreach $j (@WN_sG_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq11 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq11 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu11 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sH_ef = split(/!/,$WN_sH[7]);
	foreach $j (@WN_sH_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq12 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq12 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu12 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sI_ef = split(/!/,$WN_sI[7]);
	foreach $j (@WN_sI_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq13 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq13 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu13 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sJ_ef = split(/!/,$WN_sJ[7]);
	foreach $j (@WN_sJ_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq14 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq14 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu14 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}


	$EntCnt = 0;
	@WN_sK_ef = split(/!/,$WN_sK[7]);
	foreach $j (@WN_sK_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq15 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq15 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu15 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sL_ef = split(/!/,$WN_sL[7]);
	foreach $j (@WN_sL_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq16 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq16 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu16 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$EntCnt = 0;
	@WN_sM_ef = split(/!/,$WN_sM[7]);
	foreach $j (@WN_sM_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
			if($vijunu[0] ne ""){
				$tokusyuuniq17 .= "<font color=00ff00>$vijunu[0]</font>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
#					$tokusyuuniq2 .= "固有：";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq17 .= "<font color=00ff00>$vijunu[0]</font>"if $j;		
			}
		}else{
			$tokusyu17 .= "$vijunu[0]&nbsp;"if $j;				
		}
	}

	$Pl_WeaponNameA="$WN_sA[0](Lv$WLV_A)";
	$Pl_WeaponNameB="$WN_sB[0](Lv$WLV_B)";
	$Pl_WeaponNameC="$WN_sC[0](Lv$WLV_C)";
	$Pl_WeaponNameD="$WN_sD[0](Lv$WLV_D)";
	$Pl_WeaponNameS="$WN_sS[0](Lv$WLV_S)";
	$Pl_WeaponNameT="$WN_sT[0](Lv$WLV_T)";
	$Pl_WeaponNameU="$WN_sU[0](Lv$WLV_U)";
	$Pl_WeaponNameY="$WN_sY[0](Lv$WLV_Y)";

	$Pl_WeaponNameE="$WN_sE[0](Lv$WLV_E)";
	$Pl_WeaponNameF="$WN_sF[0](Lv$WLV_F)";
	$Pl_WeaponNameG="$WN_sG[0](Lv$WLV_G)";
	$Pl_WeaponNameH="$WN_sH[0](Lv$WLV_H)";
	$Pl_WeaponNameI="$WN_sI[0](Lv$WLV_I)";
	$Pl_WeaponNameJ="$WN_sJ[0](Lv$WLV_J)";

	$Pl_WeaponNameK="$WN_sK[0](Lv$WLV_K)";
	$Pl_WeaponNameL="$WN_sL[0](Lv$WLV_L)";
	$Pl_WeaponNameM="$WN_sM[0](Lv$WLV_M)";


	@HC=split(/!/,$PL_VALUES[50]);
	if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
	if($HC[1] eq ""){$HC[1] = 0;}
	if($HC[2] eq ""){$HC[2] = 0;}

	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">装備一覧</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
	print "<tr><td>$Pl_WeaponNameA 特性：$tokusyu $tokusyuuniq</td></tr>\n";
	if($WN_sB[0]){print "<tr><td>$Pl_WeaponNameB 特性：$tokusyu2 $tokusyuuniq2</td></tr>\n";}
	if($WN_sC[0]){print "<tr><td>$Pl_WeaponNameC 特性：$tokusyu3 $tokusyuuniq3</td></tr>\n";}
	if($WN_sD[0]){print "<tr><td>$Pl_WeaponNameD 特性：$tokusyu4 $tokusyuuniq4</td></tr>\n";}
	if($WN_sS[0]){print "<tr><td>$Pl_WeaponNameS 特性：$tokusyu5 $tokusyuuniq5</td></tr>\n";}
	if($WN_sT[0]){print "<tr><td>$Pl_WeaponNameT 特性：$tokusyu6 $tokusyuuniq6</td></tr>\n";}
	if($WN_sU[0]){print "<tr><td>$Pl_WeaponNameU 特性：$tokusyu7 $tokusyuuniq7</td></tr>\n";}
#	if($WN_sY[0]){print "<tr><td>$Pl_WeaponNameY 特性：$tokusyu8 $tokusyuuniq8</td></tr>\n";}

	print "</table>\n";

	if ($WN_sE[0] || $WN_sF[0] || $WN_sG[0] || $WN_sH[0] || $WN_sI[0] || $WN_sJ[0]){
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">倉庫一覧</b>\n";
		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";

		if($WN_sE[0]){print "<tr><td>$Pl_WeaponNameE 特性：$tokusyu9 $tokusyuuniq9</td></tr>\n";}
		if($WN_sF[0]){print "<tr><td>$Pl_WeaponNameF 特性：$tokusyu10 $tokusyuuniq10</td></tr>\n";}
		if($WN_sG[0]){print "<tr><td>$Pl_WeaponNameG 特性：$tokusyu11 $tokusyuuniq11</td></tr>\n";}
		if($WN_sH[0]){print "<tr><td>$Pl_WeaponNameH 特性：$tokusyu12 $tokusyuuniq12</td></tr>\n";}
		if($WN_sI[0]){print "<tr><td>$Pl_WeaponNameI 特性：$tokusyu13 $tokusyuuniq13</td></tr>\n";}
		if($WN_sJ[0]){print "<tr><td>$Pl_WeaponNameJ 特性：$tokusyu14 $tokusyuuniq14</td></tr>\n";}

		if($WN_sK[0]){print "<tr><td>$Pl_WeaponNameK 特性：$tokusyu15 $tokusyuuniq15</td></tr>\n";}
		if($WN_sL[0]){print "<tr><td>$Pl_WeaponNameL 特性：$tokusyu16 $tokusyuuniq16</td></tr>\n";}
		if($WN_sM[0]){print "<tr><td>$Pl_WeaponNameM 特性：$tokusyu17 $tokusyuuniq17</td></tr>\n";}

		print "</table>\n";
	}
#褒章倉庫
		if(!$PL_VALUES[9]){
			$Pl_WeaponNameA = "----------";
		}
		if(!$PL_VALUES[10]){
			$Pl_WeaponNameB = "----------";
		}
		if(!$PL_VALUES[11]){
			$Pl_WeaponNameC = "----------";
		}
		if(!$PL_VALUES[38]){
			$Pl_WeaponNameD = "----------";
		}
		if(!$PL_VALUES[41]){
			$Pl_WeaponNameS = "----------";
		}
		if(!$PL_VALUES[42]){
			$Pl_WeaponNameT = "----------";
		}
		if(!$PL_VALUES[43]){
			$Pl_WeaponNameU = "----------";
		}
		if(!$PL_VALUES[55]){
			$Pl_WeaponNameE = "----------";
		}
		if(!$PL_VALUES[56]){
			$Pl_WeaponNameF = "----------";
		}
		if(!$PL_VALUES[57]){
			$Pl_WeaponNameG = "----------";
		}
		if(!$PL_VALUES[58]){
			$Pl_WeaponNameH = "----------";
		}
		if(!$PL_VALUES[59]){
			$Pl_WeaponNameI = "----------";
		}
		if(!$PL_VALUES[60]){
			$Pl_WeaponNameJ = "----------";
		}
		if(!$PL_VALUES[61]){
			$Pl_WeaponNameK = "----------";
		}
		if(!$PL_VALUES[62]){
			$Pl_WeaponNameL = "----------";
		}
		if(!$PL_VALUES[63]){
			$Pl_WeaponNameM = "----------";
		}		
	if ($HC[1] >= 2){
		&JScfm(checkEquipSort,"\装\備倉庫を使用します。よろしいですか？※貢献値を2ポイント消費します。");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">\装\備倉庫</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
		print "<tr><td><input type=radio name=sorte value=0 disabled\n";
		print "<b>$Pl_WeaponNameA&nbsp;&nbsp;</b></td>\n";
		
		if($WN_sE[11] == 0 || $WN_sE[11] == 9){
			print "<td><input type=radio name=sorter value=0 \n";
			print "<b>$Pl_WeaponNameE&nbsp;&nbsp;</b></td></tr>\n";
		}else{
			print "<td><input type=radio name=sorter value=0 disabled\n";
			print "<b>$Pl_WeaponNameE&nbsp;&nbsp;</b></td></tr>\n";		
		}
		
		print "<tr><td><input type=radio name=sorte value=1 \n";
		print "<b>$Pl_WeaponNameB&nbsp;&nbsp;</b></td>\n";
		
		if($WN_sF[11] == 0 || $WN_sF[11] == 9){
			print "<td><input type=radio name=sorter value=1 \n";
			print "<b>$Pl_WeaponNameF&nbsp;&nbsp;</b></td></tr>\n";
		}else{
			print "<td><input type=radio name=sorter value=1 disabled\n";
			print "<b>$Pl_WeaponNameF&nbsp;&nbsp;</b></td></tr>\n";		
		}
		
		print "<tr><td><input type=radio name=sorte value=2 \n";
		print "<b>$Pl_WeaponNameC&nbsp;&nbsp;</b></td>\n";
		
		if($WN_sG[11] == 0 || $WN_sG[11] == 9){
			print "<td><input type=radio name=sorter value=2 \n";
			print "<b>$Pl_WeaponNameG&nbsp;&nbsp;</b></td></tr>\n";
		}else{
			print "<td><input type=radio name=sorter value=2 disabled\n";
			print "<b>$Pl_WeaponNameG&nbsp;&nbsp;</b></td></tr>\n";		
		}
		
		print "<tr><td><input type=radio name=sorte value=3 \n";
		print "<b>$Pl_WeaponNameD&nbsp;&nbsp;</b></td>\n";

		if($PL_VALUES[29] >= 200){
			if($WN_sH[11] == 0 || $WN_sH[11] == 9){
				print "<td><input type=radio name=sorter value=3 \n";
				print "<b>$Pl_WeaponNameH&nbsp;&nbsp;</b></td></tr>\n";
			}else{
				print "<td><input type=radio name=sorter value=3 disabled\n";
				print "<b>$Pl_WeaponNameH&nbsp;&nbsp;</b></td></tr>\n";		
			}
		}else{
			print "<td><input type=radio name=sorter value=3 disabled\n";
			print "<b>Lv200以上で解放&nbsp;&nbsp;</b></td></tr>\n";
		}
		
		print "<tr><td></td>\n";
		
		if($PL_VALUES[29] >= 500){
			if($WN_sI[11] == 0 || $WN_sI[11] == 9){
				print "<td><input type=radio name=sorter value=4 \n";
				print "<b>$Pl_WeaponNameI&nbsp;&nbsp;</b></td></tr>\n";
			}else{
				print "<td><input type=radio name=sorter value=4 disabled\n";
				print "<b>$Pl_WeaponNameI&nbsp;&nbsp;</b></td></tr>\n";		
			}
		}else{
			print "<td><input type=radio name=sorter value=4 disabled\n";
			print "<b>Lv500以上で解放&nbsp;&nbsp;</b></td></tr>\n";
		}

		print "<tr><td></td>\n";
		
		if($PL_VALUES[29] >= 1000){
			if($WN_sJ[11] == 0 || $WN_sJ[11] == 9){
				print "<td><input type=radio name=sorter value=5 \n";
				print "<b>$Pl_WeaponNameJ&nbsp;&nbsp;</b></td></tr>\n";
			}else{
				print "<td><input type=radio name=sorter value=5 disabled\n";
				print "<b>$Pl_WeaponNameJ&nbsp;&nbsp;</b></td></tr>\n";		
			}
		}else{
			print "<td><input type=radio name=sorter value=5 disabled\n";
			print "<b>Lv1000以上で解放&nbsp;&nbsp;</b></td></tr>\n";
		}
		
#		print "<td><input type=radio name=sorter value=6 \n";
#		print "<b>$Pl_WeaponNameU&nbsp;&nbsp;</b></td></tr>\n";



		print "<tr><td></td><td style=\"padding-right:10px;\"><input type=submit name=Cmode value=\装\備倉庫使用 onClick=\"return checkEquipSort()\"></td></tr></table>\n";
	}



	if ($HC[1] >= 2){
		&JScfm(checkEquipSort2,"特殊倉庫を使用します。よろしいですか？※貢献値を2ポイント消費します。");
		print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">特殊倉庫</b>\n";

		print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";
		print "<tr><td><input type=radio name=sorts value=1 \n";
		print "<b>$Pl_WeaponNameS&nbsp;&nbsp;</b></td>\n";

		print "<td><input type=radio name=sortsr value=1 \n";
		print "<b>$Pl_WeaponNameK&nbsp;&nbsp;</b></td></tr>\n";

		print "<tr><td><input type=radio name=sorts value=2 \n";
		print "<b>$Pl_WeaponNameT&nbsp;&nbsp;</b></td>\n";

		if($PL_VALUES[29] >= 300){
			print "<td><input type=radio name=sortsr value=2 \n";
			print "<b>$Pl_WeaponNameL&nbsp;&nbsp;</b></td></tr>\n";
		}else{
			print "<td><input type=radio name=sortsr value=2 disabled\n";
			print "<b>Lv300以上で解放&nbsp;&nbsp;</b></td></tr>\n";
		}


		print "<tr><td><input type=radio name=sorts value=3 \n";
		print "<b>$Pl_WeaponNameU&nbsp;&nbsp;</b></td>\n";

		if($PL_VALUES[29] >= 800){
			print "<td><input type=radio name=sortsr value=3 \n";
			print "<b>$Pl_WeaponNameM&nbsp;&nbsp;</b></td></tr>\n";
		}else{
			print "<td><input type=radio name=sortsr value=3 disabled\n";
			print "<b>Lv800以上で解放&nbsp;&nbsp;</b></td></tr>\n";
		}

		print "<tr><td></td><td style=\"padding-right:10px;\"><input type=submit name=Cmode value=特殊倉庫使用 onClick=\"return checkEquipSort2()\"></td></tr></table>\n";
	}


	print "<tr><td $BgColor><img src=\"$IMG_FOLDER1/equip1.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">褒章交換</b>\n";

	print "<table style=\"font-size:10pt;margin-left:8px;margin-right:8px;\">\n";

		print "<tr><td>現在獲得している貢献値･･･$HC[1]&nbsp;</td></tr>\n";
		
	print "<tr><td style=\"padding-left:20px;\"></td></tr></table>\n";
#	print "<tr><td style=\"padding-left:20px;\">$PartofW</td></tr></table>\n";


#	if (!$WN_sB[0] || !$WN_sC[0] || !$WN_sD[0] || !$WN_sS[0] || !$WN_sT[0] || !$WN_sU[0]){
#	if ($WN_sB[0] eq "" || $WN_sC[0] eq "" || $WN_sD[0] eq "" || $WN_sS[0] eq "" || $WN_sT[0] eq "" || $WN_sU[0] eq ""){
#	if (!$PL_VALUES[10] || !$PL_VALUES[11] || !$PL_VALUES[38] || !$PL_VALUES[41] || !$PL_VALUES[42] || !$PL_VALUES[43]){

	if(($WW_FRAG==1 && $HIZUK_FRAG==1) || ($CL_VALUES[7] > time || $CL_VALUES[37] > time)){
		print "<tr><td $BgColor>戦略中は、褒章交換できません。</td></tr>\n";
	}elsif (!$PL_VALUES[46]){
#		print "<tr><td $BgColor height=\"150\" background=\"$IMG_FOLDER1/shop.gif\" style=\"background-repeat:no-repeat;background-position:top;text-align: center;\"><img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" style=\"position:relative;top:20;right:22;\"></td></tr><tr><td $BgColor >\n";
		print "<table style=\"font-size:9pt;\"><img src=\"$IMG_FOLDER1/equipshop.gif\" align=\"middle\" style=\"margin-right:5px;\"><b style=\"vertical-align:middle;\">褒章リスト</b>\n";
		&JScfm(checkBuy,"褒章交換します。よろしいですか？");
		local($Flag=0);
		$buy="<select name=buyw>";
		foreach $key (sort{$a cmp $b} keys %KOUKEN_LIST){
			my @ByW = split(/\,/,$KOUKEN_LIST{$key});

			if(!$PL_VALUES[46]){
				if($ByW[1] <= $HC[1]){
					print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[1]</td></tr>";
					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
				}
			}
			
#			#通常装備品
#			if($ByW[3] == 0 && (!$PL_VALUES[10] || !$PL_VALUES[11] || !$PL_VALUES[38])){
#				if($ByW[1] <= $HC[1]){
#					print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[1]</td></tr>";
#					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
#				}
#			}
#			#特殊
#			if($ByW[3] == 1 && (!$PL_VALUES[41] || !$PL_VALUES[42] || !$PL_VALUES[43])){
#				if($ByW[1] <= $HC[1]){
#					print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[1]</td></tr>";
#					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
#				}
#			}
#			#トレジャー袋
#			if($ByW[3] == 3 && (!$PL_VALUES[10] || !$PL_VALUES[11] || !$PL_VALUES[38] || !$PL_VALUES[41] || !$PL_VALUES[42] || !$PL_VALUES[43])){
#				if($ByW[1] <= $HC[1]){
#					print "<tr><td>&nbsp;&nbsp;</td><td>&nbsp;&nbsp;$ByW[0]</td><td style=\"text-align:right;\">$ByW[1]</td></tr>";
#					$buy.="<option value=$key>$ByW[0]\n";$Flag++;
#				}
#			}
		}
		if ($Flag>0){
			$buy.="</select><input name=\"Cmode\" type=submit value=褒章交換 onClick=\"return checkBuy()\">\n";
		}else{
			$buy="貢献値が足りません。";$Flag++;
		}
		print "</table><div align=right>$buy</div></td></tr>\n";
	}

#	if (!$PL_VALUES[10] && !$PL_VALUES[11] && !$PL_VALUES[38] && !$PL_VALUES[41] && !$PL_VALUES[42] && !$PL_VALUES[43]){
	if ($PL_VALUES[46]){
#	if ($ABI_sA[0] eq "" && $ABI_sB[0] eq "" && $ABI_sC[0] eq "" && $Flag==0){
		print "<tr><td $BgColor>実行できるコマンドがありません。</td></tr>\n";}
	print "</form></table>\n";&FOOTER;
}
1;

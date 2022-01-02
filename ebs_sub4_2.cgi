sub BATTLE2{
	require './vabattle.pl';
	&vabattleheader;

	&LOCK;
		&DBM_CONVERT('P',"$FORM{pname}",'VS',"$FORM{vsname}");
		&DBM_CONVERT('C',"$PL_VALUES[5]",'VC',"$VS_VALUES[5]");

	&vabattle1;

	&ERROR('Repair','直前に戦闘の割り込みが入りました。戦闘を中止します。') if ($PL_VALUES[25] || $VS_VALUES[25]);
	&ERROR("世界大戦中は無国籍のプレイヤーは他国の国民と戦闘することは出来ません。") if (!$PL_VALUES[5] && $VS_VALUES[5] && $WW_FRAG==1 && $HIZUK_FRAG==1);

#	local($PL_WN,$PL_WLV) = split(/!/,$PL_VALUES[9]);local($PL_WB,$PL_LVB) = split(/!/,$PL_VALUES[10]);local($PL_WC,$PL_LVC) = split(/!/,$PL_VALUES[11]);local($PL_WD,$PL_LVD) = split(/!/,$PL_VALUES[38]);
#	local($VS_WN,$VS_WLV) = split(/!/,$VS_VALUES[9]);local($VS_WB,$VS_LVB) = split(/!/,$VS_VALUES[10]);local($VS_WC,$VS_LVC) = split(/!/,$VS_VALUES[11]);local($VS_WD,$VS_LVD) = split(/!/,$VS_VALUES[38]);
#         haaa!   207!   0!        1!       0!       0!        0!      0!       0!        6!          5!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!2!0!0!0!0!0!!!!!!!!!!
#			4gbac!2484!		0!		0!		0!			0!		0!		0!		0!			0!		0!		3!			0!		5!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!0!!!!!!0!0!!!
	local($PL_WN,$PL_WLV,$PL_WAEnt,$PL_WA03,$PL_WA04,$PL_WA05,$PL_WA06,$PL_WA07,$PL_WA08,$PL_WA09,$PL_WA10,$PL_WA11,$PL_WA12,$PL_WA13,$PL_WA14,$PL_WA15,$PL_WA16,$PL_WA17,$PL_WA18,$PL_WA19,$PL_WA20,$PL_WA21,$PL_WA22,$PL_WA23,$PL_WA24,$PL_WA25,$PL_WA26,$PL_WA27,$PL_WA28,$PL_WA29,$PL_WA30,$PL_WA31,$PL_WA32,$PL_WA33,$PL_WA34,$PL_WA35,$PL_WA36,$PL_WA37,$PL_WA38,$PL_WA39,$PL_WA40,$PL_WA41,$PL_WA42) = split(/!/,$PL_VALUES[9]);
	local($PL_WB,$PL_LVB,$PL_WBEnt,$PL_WB03,$PL_WB04,$PL_WB05,$PL_WB06,$PL_WB07,$PL_WB08,$PL_WB09,$PL_WB10,$PL_WB11,$PL_WB12,$PL_WB13,$PL_WB14,$PL_WB15,$PL_WB16,$PL_WB17,$PL_WB18,$PL_WB19,$PL_WB20,$PL_WB21,$PL_WB22,$PL_WB23,$PL_WB24,$PL_WB25,$PL_WB26,$PL_WB27,$PL_WB28,$PL_WB29,$PL_WB30,$PL_WB31,$PL_WB32,$PL_WB33,$PL_WB34,$PL_WB35,$PL_WB36,$PL_WB37,$PL_WB38,$PL_WB39,$PL_WB40,$PL_WB41,$PL_WB42) = split(/!/,$PL_VALUES[10]);
	local($PL_WC,$PL_LVC,$PL_WCEnt,$PL_WC03,$PL_WC04,$PL_WC05,$PL_WC06,$PL_WC07,$PL_WC08,$PL_WC09,$PL_WC10,$PL_WC11,$PL_WC12,$PL_WC13,$PL_WC14,$PL_WC15,$PL_WC16,$PL_WC17,$PL_WC18,$PL_WC19,$PL_WC20,$PL_WC21,$PL_WC22,$PL_WC23,$PL_WC24,$PL_WC25,$PL_WC26,$PL_WC27,$PL_WC28,$PL_WC29,$PL_WC30,$PL_WC31,$PL_WC32,$PL_WC33,$PL_WC34,$PL_WC35,$PL_WC36,$PL_WC37,$PL_WC38,$PL_WC39,$PL_WC40,$PL_WC41,$PL_WC42) = split(/!/,$PL_VALUES[11]);
	local($PL_WD,$PL_LVD,$PL_WDEnt,$PL_WD03,$PL_WD04,$PL_WD05,$PL_WD06,$PL_WD07,$PL_WD08,$PL_WD09,$PL_WD10,$PL_WD11,$PL_WD12,$PL_WD13,$PL_WD14,$PL_WD15,$PL_WD16,$PL_WD17,$PL_WD18,$PL_WD19,$PL_WD20,$PL_WD21,$PL_WD22,$PL_WD23,$PL_WD24,$PL_WD25,$PL_WD26,$PL_WD27,$PL_WD28,$PL_WD29,$PL_WD30,$PL_WD31,$PL_WD32,$PL_WD33,$PL_WD34,$PL_WD35,$PL_WD36,$PL_WD37,$PL_WD38,$PL_WD39,$PL_WD40,$PL_WD41,$PL_WD42) = split(/!/,$PL_VALUES[38]);
	
	local($VS_WN,$VS_WLV,$VS_WAEnt,$VS_WA03,$VS_WA04,$VS_WA05,$VS_WA06,$VS_WA07,$VS_WA08,$VS_WA09,$VS_WA10,$VS_WA11,$VS_WA12,$VS_WA13,$VS_WA14,$VS_WA15,$VS_WA16,$VS_WA17,$VS_WA18,$VS_WA19,$VS_WA20,$VS_WA21,$VS_WA22,$VS_WA23,$VS_WA24,$VS_WA25,$VS_WA26,$VS_WA27,$VS_WA28,$VS_WA29,$VS_WA30,$VS_WA31,$VS_WA32,$VS_WA33,$VS_WA34,$VS_WA35,$VS_WA36,$VS_WA37,$VS_WA38,$VS_WA39,$VS_WA40,$VS_WA41,$VS_WA42) = split(/!/,$VS_VALUES[9]);
	local($VS_WB,$VS_LVB,$VS_WBEnt,$VS_WB03,$VS_WB04,$VS_WB05,$VS_WB06,$VS_WB07,$VS_WB08,$VS_WB09,$VS_WB10,$VS_WB11,$VS_WB12,$VS_WB13,$VS_WB14,$VS_WB15,$VS_WB16,$VS_WB17,$VS_WB18,$VS_WB19,$VS_WB20,$VS_WB21,$VS_WB22,$VS_WB23,$VS_WB24,$VS_WB25,$VS_WB26,$VS_WB27,$VS_WB28,$VS_WB29,$VS_WB30,$VS_WB31,$VS_WB32,$VS_WB33,$VS_WB34,$VS_WB35,$VS_WB36,$VS_WB37,$VS_WB38,$VS_WB39,$VS_WB40,$VS_WB41,$VS_WB42) = split(/!/,$VS_VALUES[10]);
	local($VS_WC,$VS_LVC,$VS_WCEnt,$VS_WC03,$VS_WC04,$VS_WC05,$VS_WC06,$VS_WC07,$VS_WC08,$VS_WC09,$VS_WC10,$VS_WC11,$VS_WC12,$VS_WC13,$VS_WC14,$VS_WC15,$VS_WC16,$VS_WC17,$VS_WC18,$VS_WC19,$VS_WC20,$VS_WC21,$VS_WC22,$VS_WC23,$VS_WC24,$VS_WC25,$VS_WC26,$VS_WC27,$VS_WC28,$VS_WC29,$VS_WC30,$VS_WC31,$VS_WC32,$VS_WC33,$VS_WC34,$VS_WC35,$VS_WC36,$VS_WC37,$VS_WC38,$VS_WC39,$VS_WC40,$VS_WC41,$VS_WC42) = split(/!/,$VS_VALUES[11]);
	local($VS_WD,$VS_LVD,$VS_WDEnt,$VS_WD03,$VS_WD04,$VS_WD05,$VS_WD06,$VS_WD07,$VS_WD08,$VS_WD09,$VS_WD10,$VS_WD11,$VS_WD12,$VS_WD13,$VS_WD14,$VS_WD15,$VS_WD16,$VS_WD17,$VS_WD18,$VS_WD19,$VS_WD20,$VS_WD21,$VS_WD22,$VS_WD23,$VS_WD24,$VS_WD25,$VS_WD26,$VS_WD27,$VS_WD28,$VS_WD29,$VS_WD30,$VS_WD31,$VS_WD32,$VS_WD33,$VS_WD34,$VS_WD35,$VS_WD36,$VS_WD37,$VS_WD38,$VS_WD39,$VS_WD40,$VS_WD41,$VS_WD42) = split(/!/,$VS_VALUES[38]);

	local($PL_WS,$PL_LVS,$PL_WSEnt) = split(/!/,$PL_VALUES[$FORM{"sentaku"}]);
	local($PL_WH,$PL_LVH,$PL_WHEnt) = split(/!/,$PL_VALUES[$FORM{"Hosentaku"}]);

	@VS_ChW=split(/\,/,$WEAPON_LIST{"$VS_WN"});

#ヒート、メルト用
	local($PL_WSS1,$PL_LVSS1,$PL_WSS1Ent) = split(/!/,$PL_VALUES[41]);
	local($PL_WSS2,$PL_LVSS2,$PL_WSS2Ent) = split(/!/,$PL_VALUES[42]);
	local($PL_WSS3,$PL_LVSS3,$PL_WSS3Ent) = split(/!/,$PL_VALUES[43]);
	local($VS_WSS1,$VS_LVSS1,$VS_WSS1Ent) = split(/!/,$VS_VALUES[41]);
	local($VS_WSS2,$VS_LVSS2,$VS_WSS2Ent) = split(/!/,$VS_VALUES[42]);
	local($VS_WSS3,$VS_LVSS3,$VS_WSS3Ent) = split(/!/,$VS_VALUES[43]);

#	local($PL_WSS1,$PL_LVSS1,$PL_WSEnt,$PL_WS03,$PL_WS04,$PL_WS05,$PL_WS06,$PL_WS07,$PL_WS08,$PL_WS09,$PL_WS10,$PL_WS11,$PL_WS12,$PL_WS13,$PL_WS14,$PL_WS15,$PL_WS16,$PL_WS17,$PL_WS18,$PL_WS19,$PL_WS20,$PL_WS21,$PL_WS22,$PL_WS23,$PL_WS24,$PL_WS25,$PL_WS26,$PL_WS27,$PL_WS28,$PL_WS29,$PL_WS30,$PL_WS31,$PL_WS32,$PL_WS33,$PL_WS34,$PL_WS35,$PL_WS36,$PL_WS37,$PL_WS38,$PL_WS39,$PL_WS40,$PL_WS41,$PL_WS42) = split(/!/,$PL_VALUES[41]);
#	local($PL_WSS2,$PL_LVSS2,$PL_WTEnt,$PL_WT03,$PL_WT04,$PL_WT05,$PL_WT06,$PL_WT07,$PL_WT08,$PL_WT09,$PL_WT10,$PL_WT11,$PL_WT12,$PL_WT13,$PL_WT14,$PL_WT15,$PL_WT16,$PL_WT17,$PL_WT18,$PL_WT19,$PL_WT20,$PL_WT21,$PL_WT22,$PL_WT23,$PL_WT24,$PL_WT25,$PL_WT26,$PL_WT27,$PL_WT28,$PL_WT29,$PL_WT30,$PL_WT31,$PL_WT32,$PL_WT33,$PL_WT34,$PL_WT35,$PL_WT36,$PL_WT37,$PL_WT38,$PL_WT39,$PL_WT40,$PL_WT41,$PL_WT42) = split(/!/,$PL_VALUES[42]);
#	local($PL_WSS3,$PL_LVSS3,$PL_WUEnt,$PL_WU03,$PL_WU04,$PL_WU05,$PL_WU06,$PL_WU07,$PL_WU08,$PL_WU09,$PL_WU10,$PL_WU11,$PL_WU12,$PL_WU13,$PL_WU14,$PL_WU15,$PL_WU16,$PL_WU17,$PL_WU18,$PL_WU19,$PL_WU20,$PL_WU21,$PL_WU22,$PL_WU23,$PL_WU24,$PL_WU25,$PL_WU26,$PL_WU27,$PL_WU28,$PL_WU29,$PL_WU30,$PL_WU31,$PL_WU32,$PL_WU33,$PL_WU34,$PL_WU35,$PL_WU36,$PL_WU37,$PL_WU38,$PL_WU39,$PL_WU40,$PL_WU41,$PL_WU42) = split(/!/,$PL_VALUES[43]);
#	local($VS_WSS1,$VS_LVSS1,$VS_WSEnt,$VS_WS03,$VS_WS04,$VS_WS05,$VS_WS06,$VS_WS07,$VS_WS08,$VS_WS09,$VS_WS10,$VS_WS11,$VS_WS12,$VS_WS13,$VS_WS14,$VS_WS15,$VS_WS16,$VS_WS17,$VS_WS18,$VS_WS19,$VS_WS20,$VS_WS21,$VS_WS22,$VS_WS23,$VS_WS24,$VS_WS25,$VS_WS26,$VS_WS27,$VS_WS28,$VS_WS29,$VS_WS30,$VS_WS31,$VS_WS32,$VS_WS33,$VS_WS34,$VS_WS35,$VS_WS36,$VS_WS37,$VS_WS38,$VS_WS39,$VS_WS40,$VS_WS41,$VS_WS42) = split(/!/,$VS_VALUES[41]);
#	local($VS_WSS2,$VS_LVSS2,$VS_WTEnt,$VS_WT03,$VS_WT04,$VS_WT05,$VS_WT06,$VS_WT07,$VS_WT08,$VS_WT09,$VS_WT10,$VS_WT11,$VS_WT12,$VS_WT13,$VS_WT14,$VS_WT15,$VS_WT16,$VS_WT17,$VS_WT18,$VS_WT19,$VS_WT20,$VS_WT21,$VS_WT22,$VS_WT23,$VS_WT24,$VS_WT25,$VS_WT26,$VS_WT27,$VS_WT28,$VS_WT29,$VS_WT30,$VS_WT31,$VS_WT32,$VS_WT33,$VS_WT34,$VS_WT35,$VS_WT36,$VS_WT37,$VS_WT38,$VS_WT39,$VS_WT40,$VS_WT41,$VS_WT42) = split(/!/,$VS_VALUES[42]);
#	local($VS_WSS3,$VS_LVSS3,$VS_WUEnt,$VS_WU03,$VS_WU04,$VS_WU05,$VS_WU06,$VS_WU07,$VS_WU08,$VS_WU09,$VS_WU10,$VS_WU11,$VS_WU12,$VS_WU13,$VS_WU14,$VS_WU15,$VS_WU16,$VS_WU17,$VS_WU18,$VS_WU19,$VS_WU20,$VS_WU21,$VS_WU22,$VS_WU23,$VS_WU24,$VS_WU25,$VS_WU26,$VS_WU27,$VS_WU28,$VS_WU29,$VS_WU30,$VS_WU31,$VS_WU32,$VS_WU33,$VS_WU34,$VS_WU35,$VS_WU36,$VS_WU37,$VS_WU38,$VS_WU39,$VS_WU40,$VS_WU41,$VS_WU42) = split(/!/,$VS_VALUES[43]);

#	local($VS_WS,$VS_LVS) = split(/!/,$VS_VALUES[41]);
#	if($VS_VALUES[45] eq "1"){
#		$VS_WS="";
#		$VS_LVS="";
#	}
	require "./$LOG_FOLDER/$HASH_DATA";
	require "./$LOG_FOLDER/$ABI_DATA";
	if($AbiSys == 1){
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		local($VABI_FLG,$VABI_A,$VABI_B,$VABI_C) = split(/!/,$VS_VALUES[52]);
	}
#	@VS_WX=split(/\,/,$WEAPON_LIST{"$VS_WS"});

	if($VS_VALUES[45] eq "41"){
		$VS_X = $VS_VALUES[41];
		$VS_LVSET = 41;
	}elsif($VS_VALUES[45] eq "42"){
		$VS_X = $VS_VALUES[42];
		$VS_LVSET = 42;
	}elsif($VS_VALUES[45] eq "43"){
		$VS_X = $VS_VALUES[43];
		$VS_LVSET = 43;
	}elsif($VS_VALUES[45] eq "90"){
		$VS_X1 = $VS_VALUES[9];
		local($VS_X2,$VS_X2S) = split(/!/,$VS_X1);
		@VS_X3 = split(/\,/,$WEAPON_LIST{"$VS_X2"});

		if($VS_X3[13]){
			$VS_X = $VS_X3[13];
		}

		$VS_LVSET = 9;

	}elsif($VS_VALUES[45] eq "100"){
		$VS_X1 = $VS_VALUES[10];
		local($VS_X2,$VS_X2S) = split(/!/,$VS_X1);
		@VS_X3 = split(/\,/,$WEAPON_LIST{"$VS_X2"});

		if($VS_X3[13]){
			$VS_X = $VS_X3[13];
		}

		$VS_LVSET = 10;

	}elsif($VS_VALUES[45] eq "110"){
		$VS_X1 = $VS_VALUES[11];
		local($VS_X2,$VS_X2S) = split(/!/,$VS_X1);
		@VS_X3 = split(/\,/,$WEAPON_LIST{"$VS_X2"});

		if($VS_X3[13]){
			$VS_X = $VS_X3[13];
		}

		$VS_LVSET = 11;

	}elsif($VS_VALUES[45] eq "380"){
		$VS_X1 = $VS_VALUES[38];
		local($VS_X2,$VS_X2S) = split(/!/,$VS_X1);
		@VS_X3 = split(/\,/,$WEAPON_LIST{"$VS_X2"});

		if($VS_X3[13]){
			$VS_X = $VS_X3[13];
		}

#	&ERROR("$VS_VALUES[45]おおあ$VS_X3あああ$VS_X3[13]");
		$VS_LVSET = 38;

	}elsif($VS_VALUES[45] eq "390"){
		require "./$LOG_FOLDER/$CLASS_DATA";
		@VSALY_CLASS=split(/\,/,$VCLASS_LIST{"$VS_VALUES[4]"});

		$VS_X = $VSALY_CLASS[22];

		$VS_LVSET = 44;

	}
#&ERROR("$VS_WSEntと$VS_X");
	local($VS_WS,$VS_LVS,$VS_WSEnt) = split(/!/,$VS_X);


	if($VS_VALUES[45] eq "90"){
		@VS_LVCOUNT = split(/!/,$VS_VALUES[9]);
		$VS_LVS = $VS_LVCOUNT[1]
	}elsif($VS_VALUES[45] eq "100"){
		@VS_LVCOUNT = split(/!/,$VS_VALUES[10]);
		$VS_LVS = $VS_LVCOUNT[1]
	}elsif($VS_VALUES[45] eq "110"){
		@VS_LVCOUNT = split(/!/,$VS_VALUES[11]);
		$VS_LVS = $VS_LVCOUNT[1]
	}elsif($VS_VALUES[45] eq "380"){
		@VS_LVCOUNT = split(/!/,$VS_VALUES[38]);
		$VS_LVS = $VS_LVCOUNT[1]
	}elsif($VS_VALUES[45] eq "390"){
		@VS_LVCOUNT = split(/!/,$VS_VALUES[44]);
		$VS_LVS = $VS_LVCOUNT[1]
#		&ERROR("$VS_LVSああ");
	}

#	if($VS_VALUES[45] eq ""){
#		$VS_LVS = split(/!/,$VS_VALUES[44]);
#	}

	if($VS_VALUES[45] eq "" || $VS_VALUES[45] eq "1" || $VS_VALUES[45] eq "0" || $VS_VALUES[45] eq "9" || ($VS_ChW <= 40 && $VS_ChW > 0)){
		$VS_WS="";
		$VS_LVS="";
		$VS_LVSET = 9;

	}
#		&ERROR("$VS_VALUES[45]ああ$VS_WS");

#	&ERROR("$VS_VALUES[45]おおあ$VS_WSあああ$VS_WS[0]");

#	&ERROR("$VS_WS[0]");

#		&ERROR("$FORM{'sentaku'}","$PL_WS");

	&vabattle2;

#アビリティシステム
	$CriHosei = 0;
	$CriHosei2 = 0;
	if($AbiSys == 1 && $AbiMukou == 0){

		#必殺攻撃
		if($ABI_sA[2] =~ m/!A0016/ || $ABI_sB[2] =~ m/!A0016/ || $ABI_sC[2] =~ m/!A0016/){$CriHosei = 5;}

		#ストライカー
		if($PL_VALUES[14] >= 40 && ($ABI_sA[2] =~ m/!A0013/ || $ABI_sB[2] =~ m/!A0013/ || $ABI_sC[2] =~ m/!A0013/)){$CriHosei = 20;}

		#必殺修練
		if($ABI_sA[2] =~ m/!A0015/ || $ABI_sB[2] =~ m/!A0015/ || $ABI_sC[2] =~ m/!A0015/){$CriHosei2 = 1;}
		
	}

##クリティカル！！


#$PL_WA32
#	print "<font color=\"#f7e957\">試験$PL_WA32</font><br>\n";
	$PL_CRIP=0;
	if($PL_WA32 eq ""){$PL_WA32=0;}
	$PL_CRIP = $PL_CRIP + $PL_WA32;

#	if(int($PL_VALUES[18]/$PL_W[4]/10-10+$PL_VALUES[14]) > rand($PL_W[4])){
	if(int($PL_VALUES[18]/$PL_W[4]/10-10+$PL_VALUES[14]+$CriHosei+$PL_CRIP) > rand($PL_W[4])){
	$Pl_AttPoint*=3;
	$PL_CRITICAL=1;$R_VALUES[100]++;
	}else{$PL_W[4]+=$PL_VALUES[14] if $PL_VALUES[14];}
	$PL_W[4]*=5 if $PL_CRITICAL;

#アビリティシステム
	#必殺修練　クリティカル時のMP5倍補正を2.5倍補正に変更する
	if($PL_CRITICAL && $CriHosei2 eq "1"){$PL_W[4]=int($PL_W[4]/5*2.5);}

	if($PL_CRITICAL && $PL_CLASS[17] =~ m/!W024/){$PL_W[4]=int($PL_W[4]/5*2);}
	elsif($PL_CRITICAL && $PL_WA32 > 0){$PL_W[4]=int($PL_W[4]/5*(5 - $PL_WA32*0.2));}

	&vabattle3;

	&vabattle3_1;

	&vabattle4;

	&vabattle4_1;

###ルーチン
	&vabattle5;

	&vabattle5_1;

#濁鯖の魂
	if($PL_W[7] =~ m/!6u/ || $VS_W[7] =~ m/!6u/){
		$Vs_AtPoint=0;$R_VALUES[25]++;
	}
#アシェルム
	if ($PL_W[7] =~ m/!68/ && $PL_CLASS[17] !~ m/!x/ && $PL_VALUES[31]<4 && $VS_VALUES[31]<4){
		$PL_VALUES[31]=$VS_VALUES[31];$PLCONFORM=1;$R_VALUES[12]++;
	}
#ストライクノヴァ
	if ($PL_W[7] =~ m/!60/ && $PL_CLASS[17] =~ m/!1|!E007|!E008/ && $Pl_Times){
		$PL_message.='p';$R_VALUES[101]++;
	}

	$Pl_AtPoint=0 if $Pl_AtPoint < 0;
	$Vs_AtPoint=0 if $Vs_AtPoint < 0;
	
	#貢献値用
	$PL_DAM = $Pl_AtPoint;

	$dmgStyl="style=\"font-size:21px;color:#9acd32;\"";
	$chaStyl="style=\"font-size:12px;color:#dc143c;\"";
	$PlsumDmg="<b $dmgStyl>$PL_W[3]</b> <b $chaStyl>Attack</b> <b $dmgStyl>$Pl_Times</b> <b $chaStyl>hit</b> 
		<b $dmgStyl>$Pl_AtPoint</b><b $chaStyl> Damage</b>" if $Pl_Times > 0;
	$PlsumDmg='<font color=#6a5acd>Miss</font>' if $Pl_Times == 0;
	$VssumDmg="<b $dmgStyl>$VS_W[3]</b> <b $chaStyl>Attack</b> <b $dmgStyl>$Vs_Times</b> <b $chaStyl>hit</b> 
		<b $dmgStyl>$Vs_AtPoint</b><b $chaStyl> Damage</b>" if $Vs_Times > 0;
	$VssumDmg='<font color=#6a5acd>Miss</font>' if $Vs_Times == 0;

		$hpcolor="$IMG_FOLDER1/hp.gif";
		$dmgcolor="$IMG_FOLDER1/dmg.gif";
		$zencolor="$IMG_FOLDER1/zen.gif";

	if($MENTE==1){
		$hpcolor="$IMG_FOLDER1/hp1.gif";
		$dmgcolor="$IMG_FOLDER1/dmg1.gif";
		$zencolor="$IMG_FOLDER1/zen1.gif";
	}

	$Pl_BfrHP=$PL_VALUES[15];
	$Vs_AtPoint=$PL_VALUES[15] if $PL_VALUES[15] < $Vs_AtPoint;
	$PL_VALUES[15]=$PL_VALUES[15]-$Vs_AtPoint;
	$Pl_width_per=$PL_VALUES[16]/150;
	$Pl_width_hp=int($PL_VALUES[15]/$Pl_width_per);
	$Pl_width_zen=int(($PL_VALUES[16]-$Pl_BfrHP)/$Pl_width_per);
	$Pl_width_dmg=int($Vs_AtPoint/$Pl_width_per);
	$PL_HPTAG="<img src=\"$hpcolor\" hspace=0 height=7 width=$Pl_width_hp>" if $Pl_width_hp;
	$PL_HPTAG.="<img src=\"$dmgcolor\" hspace=0 height=7 width=$Pl_width_dmg>" if $Pl_width_dmg;
	$PL_HPTAG.="<img src=\"$zencolor\" hspace=0 height=7 width=$Pl_width_zen>" if $Pl_width_zen;
	$Vs_BfrHP=$VS_VALUES[15];
	$Pl_AtPoint=$VS_VALUES[15] if $VS_VALUES[15] < $Pl_AtPoint;
	$VS_VALUES[15]=$VS_VALUES[15]-$Pl_AtPoint;
	$Vs_width_per=$VS_VALUES[16]/150;
	$Vs_width_hp=int($VS_VALUES[15]/$Vs_width_per);
	$Vs_width_zen=int(($VS_VALUES[16]-$Vs_BfrHP)/$Vs_width_per);
	$Vs_width_dmg=int($Pl_AtPoint/$Vs_width_per);
	$VS_HPTAG="<img src=\"$hpcolor\" hspace=0 height=7 width=$Vs_width_hp>" if $Vs_width_hp;
	$VS_HPTAG.="<img src=\"$dmgcolor\" hspace=0 height=7 width=$Vs_width_dmg>" if $Vs_width_dmg;
	$VS_HPTAG.="<img src=\"$zencolor\" hspace=0 height=7 width=$Vs_width_zen>" if $Vs_width_zen;

	&vabattle6_1;

#恨みプレイヤーサイド
	if ($PL_W[7] =~ m/!29/ && $VS_W[7] !~ m/!43/ && $VS_sB[7] !~ m/!43/ && $VS_sC[7] !~ m/!43/ && $VS_sD[7] !~ m/!43/ && $ResultBattle==1){
		if(rand(100) > 78){$VS_VALUES[15]=0;$VS_VALUES[25]=1;$PLURAMI=1;$R_VALUES[77]++;}
	$R_VALUES[109]++;}
#トランスファー！
	if (($PL_W[7] =~ m/!6t/ || $PL_sB[7] =~ m/!6t/ || $PL_sC[7] =~ m/!6t/ || $PL_sD[7] =~ m/!6t/) && $ResultBattle==1){
		if($PL_VALUES[6]==1){
			$sousui='デニム';
		}else{
			while (my($key,$val) = each %P){
				my@VALS = split(/\s/,$val);
				if($VALS[5] eq $PL_VALUES[5]){
					if($VALS[6] == 1){
						$sousui=$key;
					}
				}
			}
		}
		$PL_VALUES[5]="";$PL_VALUES[28]='';$PL_VALUES[0]=$PL_VALUES[6]=0;
		$PLTRANS=1;$R_VALUES[19]++;
#		$PL_VALUES[10]='1oa!0' if $PL_sB[7] =~ m/!6t/;
#		$PL_VALUES[11]='1oa!0' if $PL_sC[7] =~ m/!6t/;
#		$PL_VALUES[38]='1oa!0' if $PL_sD[7] =~ m/!6t/;
		$PL_VALUES[10]='1024a!0' if $PL_sB[7] =~ m/!6t/;
		$PL_VALUES[11]='1024a!0' if $PL_sC[7] =~ m/!6t/;
		$PL_VALUES[38]='1024a!0' if $PL_sD[7] =~ m/!6t/;
	}
#リバイバル！
	if ($VS_sB[7] =~ m/!6v/ && $ResultBattle==0){
		$VS_VALUES[15]=$VS_VALUES[16];$VS_VALUES[25]=0;$VSMIGAWARI=1;$R_VALUES[20]++;
	}

	&vabattle6_2;

#&ERROR("$PL_STF");

	&MESSAGE('m','PL','VS') if $PL_message;
	&MESSAGE('m','VS','PL') if $VS_message;

#アビリティシステム
	#トレジャー発見率アップ
	$toretore = 1;$yokubou = 0;

	#チェインシステム
	if($ChainSys == 1){
		local($Chain_FLG,$Chain_Cnt,$Chain_Country,$Chain_time) = split(/!/,$PL_VALUES[54]);
		#チェインキー処理
		if($Chain_FLG ne $ChainKey){$PL_VALUES[54]="";$Chain_Cnt="0";$Chain_Country="";$Chain_FLG=$ChainKey;}

		#Chain_timeが空の場合は、time関数を設定する
		if($Chain_time eq ""){$Chain_time = time;}

		#Chain_timeから10分経過している場合はリセットする
		if($Chain_time + 600 < time){$Chain_Cnt="0";$Chain_Country="";$Chain_FLG=$ChainKey;}
		$Chain_time = time;
		#最終戦闘時間から10分以上経過した場合もリセット
#			if($PL_VALUES[26] < time - 600){$Chain_Cnt="0";$Chain_Country="";$Chain_FLG=$ChainKey;}

		#チェインキー設定
		$Chain_FLG=$ChainKey;$Chain_Msgflg=0;
		#チェイン国と撃破プレイヤーの国が異なる場合はカウントをリセット
		if($Chain_Country ne $VS_VALUES[5]){$Chain_Cnt = "0";print "<font color=\"#f7e957\">ChainRESET！！</font><br>\n";$Chain_Msgflg=1;}
		#チェイン国設定
		$Chain_Country = $VS_VALUES[5];
		#撃破時チェイン加算　撃破できなかった場合はカウントリセット
		if($Chain_Cnt eq ""){$Chain_Cnt = "0";}
		if($ResultBattle==0){$Chain_Cnt = $Chain_Cnt + 1;}else{$Chain_Cnt = "0";if($Chain_Msgflg eq "0"){print "<font color=\"#f7e957\">ChainRESET！！</font><br>\n";}}

		$PL_VALUES[54] = "$Chain_FLG!$Chain_Cnt!$Chain_Country!$Chain_time";

		if($Chain_Cnt > 1){print "<font color=\"#f7e957\">$Chain_Cnt Chain！！</font><br>\n";}
		
		#チェインボーナス　10カウント以降
		if($Chain_Cnt > 9){

			$PL_VALUES[53] = $PL_VALUES[53]+7;
			if($PL_VALUES[53] > 9999){$PL_VALUES[53] = 9999;}
			print "<font color=\"#f7e957\">ChainBonus！！7APを獲得。</font><br>\n";
			$toretore = $toretore - ($Chain_Cnt - 9) * 0.01;
			if($toretore < 0.5){$toretore = 0.5;}

		}
		#チェインボーナス　5カウント以降
		elsif($Chain_Cnt > 4){
		
			$PL_VALUES[53] = $PL_VALUES[53]+5;
			if($PL_VALUES[53] > 9999){$PL_VALUES[53] = 9999;}
			print "<font color=\"#f7e957\">ChainBonus！！5APを獲得。</font><br>\n";
		
		}
		elsif($Chain_Cnt eq "3"){
		
			$PL_VALUES[53] = $PL_VALUES[53]+3;
			if($PL_VALUES[53] > 9999){$PL_VALUES[53] = 9999;}
			print "<font color=\"#f7e957\">ChainBonus！！3APを獲得。</font><br>\n";
		
		}			
	}
		
	if($AbiSys == 1 && $AbiMukou == 0){
		if($ABI_sA[2] =~ m/!A0006/ || $ABI_sB[2] =~ m/!A0006/ || $ABI_sC[2] =~ m/!A0006/){$toretore=0.8;}
	}

#エンチャント　MF
	$MFUP=0;
#	if($PL_WA12 ne "" && $PL_WA12 > 0 && $PL_flgEnt > 0){$MFUP = $MFUP + $PL_WA12 * 2;}
#	if($PL_WB12 ne "" && $PL_WB12 > 0 && $PL_flgEnt2 > 0){$MFUP = $MFUP + $PL_WB12 * 2;}
#	if($PL_WC12 ne "" && $PL_WC12 > 0 && $PL_flgEnt3 > 0){$MFUP = $MFUP + $PL_WC12 * 2;}
#	if($PL_WD12 ne "" && $PL_WD12 > 0 && $PL_flgEnt4 > 0){$MFUP = $MFUP + $PL_WD12 * 2;}

	if($PL_WA12 ne "" && $PL_WA12 > 0){$MFUP = $MFUP + $PL_WA12 * 2;}
	if($PL_WB12 ne "" && $PL_WB12 > 0){$MFUP = $MFUP + $PL_WB12 * 2;}
	if($PL_WC12 ne "" && $PL_WC12 > 0){$MFUP = $MFUP + $PL_WC12 * 2;}
	if($PL_WD12 ne "" && $PL_WD12 > 0){$MFUP = $MFUP + $PL_WD12 * 2;}

	
	#トレジャー発見率アップ
	$toreho = 1;
#	if($PL_WA11 ne "" && $PL_WA11 > 0 && $PL_flgEnt > 0){$toreho = $toreho - ($PL_WA11 * 0.04);}
#	if($PL_WB11 ne "" && $PL_WB11 > 0 && $PL_flgEnt2 > 0){$toreho = $toreho - ($PL_WB11 * 0.04);}
#	if($PL_WC11 ne "" && $PL_WC11 > 0 && $PL_flgEnt3 > 0){$toreho = $toreho - ($PL_WC11 * 0.04);}
#	if($PL_WD11 ne "" && $PL_WD11 > 0 && $PL_flgEnt4 > 0){$toreho = $toreho - ($PL_WD11 * 0.04);}

	if($PL_WA11 ne "" && $PL_WA11 > 0){$toreho = $toreho - ($PL_WA11 * 0.04);}
	if($PL_WB11 ne "" && $PL_WB11 > 0){$toreho = $toreho - ($PL_WB11 * 0.04);}
	if($PL_WC11 ne "" && $PL_WC11 > 0){$toreho = $toreho - ($PL_WC11 * 0.04);}
	if($PL_WD11 ne "" && $PL_WD11 > 0){$toreho = $toreho - ($PL_WD11 * 0.04);}

#装備強化システム
	$PL_ToreEntPoint = 0;
	$VS_ToreEntPoint = 0;

	$PL_MFEntPoint = 0;
	$VS_MFEntPoint = 0;


	require "./$LOG_FOLDER/$HASH_DATA";
	@PL_W=split(/\,/,$WEAPON_LIST{"$PL_WN"}); @PL_sB=split(/\,/,$WEAPON_LIST{"$PL_WB"}); @PL_sC=split(/\,/,$WEAPON_LIST{"$PL_WC"}); @PL_sD=split(/\,/,$WEAPON_LIST{"$PL_WD"});


	if($PL_WAEnt ne "" & $PL_WAEnt > 0){
		if($PL_W[14] =~ m/A27/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WAEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WAEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WAEnt / 10);
		#装飾品
		}elsif($PL_W[14] =~ m/A30/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WAEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WAEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WAEnt / 10);
		}
	}
	if($PL_WBEnt ne "" & $PL_WBEnt > 0){

		#頭防具
		if($PL_sB[14] =~ m/A27/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WBEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WBEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WBEnt / 10);
		#装飾品
		}elsif($PL_sB[14] =~ m/A30/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WBEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WBEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WBEnt / 10);
		}

	}

	if($PL_WCEnt ne "" & $PL_WCEnt > 0){

		#頭防具
		if($PL_sC[14] =~ m/A27/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WCEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WCEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WCEnt / 10);
		#装飾品
		}elsif($PL_sC[14] =~ m/A30/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WCEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WCEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WCEnt / 10);
		}

	}

	if($PL_WDEnt ne "" & $PL_WDEnt > 0){

		#頭防具
		if($PL_sD[14] =~ m/A27/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WDEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WDEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WDEnt / 10);
		#装飾品
		}elsif($PL_sD[14] =~ m/A30/){
#			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WDEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WDEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WDEnt / 10);
		}

	}

	$toreho = $toreho - ($PL_ToreEntPoint * 0.01);
	$MFUP = $MFUP + $PL_MFEntPoint * 1;

#20181206 MF・トレジャーアップ
#	$MFUP = $MFUP + 4;
#	$toreho = $toreho - (5 * 0.04);

	if($toreho <= 0){$toreho = 0.01;}

#試験
#if($PL_VALUES[4] == 170){$PL_VALUES[17] = $PL_VALUES[18];$toreho = $toreho * 0.1;}








	$buki=0;
	



	
	

	if (!$ResultBattle && (!$PL_VALUES[10] || !$PL_VALUES[11] || !$PL_VALUES[38] || !$PL_VALUES[41] || !$PL_VALUES[42] || !$PL_VALUES[43] || !$PL_VALUES[46])){
		my@al=keys %WEAPON_LIST;$alw=@al;
		$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
			@q=split(/\,/,$WEAPON_LIST{"$gw"});
	  if ($PL_W[7] =~ m/!1d/ && ($PL_sB[7] =~ m/!1c/ || $PL_sC[7] =~ m/!1c/ || $PL_sD[7] =~ m/!1c/)){
		#属性魔法書の獲得処理　今は触らない
		if($q[8] > rand(80) && $q[7] !~ m/!1c/){
			if(!$PL_VALUES[10]){$PL_VALUES[10]=$gw;}
			elsif(!$PL_VALUES[11]){$PL_VALUES[11]=$gw;}
			elsif(!$PL_VALUES[38]){$PL_VALUES[38]=$gw;}
#			print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";
			print "<font color=\"#0086ad\">トレジャーを獲得。</font><br>\n";
		}
	  }else{
	  	if($q[8] eq ""){$q[8] = 0;}
#		if ($q[8] > rand(60) && ($q[7] !~ m/!71|!72/ || ($q[7] =~ m/!71/ && $PL_VALUES[39] eq "1") || ($q[7] =~ m/!72/ && $PL_VALUES[39] eq "2"))){
		if ($q[8] > (rand(20) * $toretore * $toreho)){
#		if ($q[8] >= 0){

			#装備品の場合、エンチャント付与を行う
			$ent="!0!0";
			if($q[11] eq "0"){

				#STRボーナス
				$ent_str="!0";
				if(rand(100) < 5 + $MFUP){

					if(rand(1000) < 2){$ent_str = "!10";}
					elsif(rand(1000) < 7){$ent_str = "!9";}
					elsif(rand(1000) < 14){$ent_str = "!8";}
					elsif(rand(1000) < 28){$ent_str = "!7";}
					elsif(rand(1000) < 36){$ent_str = "!6";}
					elsif(rand(1000) < 51){$ent_str = "!5";}
					elsif(rand(1000) < 78){$ent_str = "!4";}
					elsif(rand(1000) < 99){$ent_str = "!3";}
					elsif(rand(1000) < 152){$ent_str = "!2";}
					else{$ent_str = "!1";}
				
				}

				#VITボーナス
				$ent_vit="!0";
				if(rand(100) < 5 + $MFUP){

					if(rand(1000) < 2){$ent_vit = "!10";}
					elsif(rand(1000) < 7){$ent_vit = "!9";}
					elsif(rand(1000) < 14){$ent_vit = "!8";}
					elsif(rand(1000) < 28){$ent_vit = "!7";}
					elsif(rand(1000) < 36){$ent_vit = "!6";}
					elsif(rand(1000) < 51){$ent_vit = "!5";}
					elsif(rand(1000) < 78){$ent_vit = "!4";}
					elsif(rand(1000) < 99){$ent_vit = "!3";}
					elsif(rand(1000) < 152){$ent_vit = "!2";}
					else{$ent_vit = "!1";}
				
				}

				#DEXボーナス
				$ent_dex="!0";
				if(rand(100) < 5 + $MFUP){

					if(rand(1000) < 2){$ent_dex = "!10";}
					elsif(rand(1000) < 7){$ent_dex = "!9";}
					elsif(rand(1000) < 14){$ent_dex = "!8";}
					elsif(rand(1000) < 28){$ent_dex = "!7";}
					elsif(rand(1000) < 36){$ent_dex = "!6";}
					elsif(rand(1000) < 51){$ent_dex = "!5";}
					elsif(rand(1000) < 78){$ent_dex = "!4";}
					elsif(rand(1000) < 99){$ent_dex = "!3";}
					elsif(rand(1000) < 152){$ent_dex = "!2";}
					else{$ent_dex = "!1";}
				
				}

				#AGIボーナス
				$ent_agi="!0";
				if(rand(100) < 5 + $MFUP){

					if(rand(1000) < 2){$ent_agi = "!10";}
					elsif(rand(1000) < 7){$ent_agi = "!9";}
					elsif(rand(1000) < 14){$ent_agi = "!8";}
					elsif(rand(1000) < 28){$ent_agi = "!7";}
					elsif(rand(1000) < 36){$ent_agi = "!6";}
					elsif(rand(1000) < 51){$ent_agi = "!5";}
					elsif(rand(1000) < 78){$ent_agi = "!4";}
					elsif(rand(1000) < 99){$ent_agi = "!3";}
					elsif(rand(1000) < 152){$ent_agi = "!2";}
					else{$ent_agi = "!1";}
				
				}
				
				#マジックファインド　頭防具限定
				$ent_mf="!0";
				if($q[14] =~ m/A27|A30/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_mf = "!10";}
					elsif(rand(1000) < 7){$ent_mf = "!9";}
					elsif(rand(1000) < 14){$ent_mf = "!8";}
					elsif(rand(1000) < 28){$ent_mf = "!7";}
					elsif(rand(1000) < 36){$ent_mf = "!6";}
					elsif(rand(1000) < 51){$ent_mf = "!5";}
					elsif(rand(1000) < 78){$ent_mf = "!4";}
					elsif(rand(1000) < 99){$ent_mf = "!3";}
					elsif(rand(1000) < 152){$ent_mf = "!2";}
					else{$ent_mf = "!1";}
				
				}

				#生命吸収　武器限定
				$ent_dl="!0";
				if($q[14] =~ m/A02/ && $q[7] =~ m/!11/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 4){$ent_dl = "!10";}
					elsif(rand(1000) < 14){$ent_dl = "!9";}
					elsif(rand(1000) < 28){$ent_dl = "!8";}
					elsif(rand(1000) < 56){$ent_dl = "!7";}
					elsif(rand(1000) < 72){$ent_dl = "!6";}
					elsif(rand(1000) < 102){$ent_dl = "!5";}
					elsif(rand(1000) < 156){$ent_dl = "!4";}
					elsif(rand(1000) < 198){$ent_dl = "!3";}
					elsif(rand(1000) < 304){$ent_dl = "!2";}
					else{$ent_dl = "!1";}

				}elsif($q[14] =~ m/A02/ && $q[7] =~ m/!10/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_dl = "!10";}
					elsif(rand(1000) < 7){$ent_dl = "!9";}
					elsif(rand(1000) < 14){$ent_dl = "!8";}
					elsif(rand(1000) < 28){$ent_dl = "!7";}
					elsif(rand(1000) < 36){$ent_dl = "!6";}
					elsif(rand(1000) < 51){$ent_dl = "!5";}
					elsif(rand(1000) < 78){$ent_dl = "!4";}
					elsif(rand(1000) < 99){$ent_dl = "!3";}
					elsif(rand(1000) < 152){$ent_dl = "!2";}
					else{$ent_dl = "!1";}
				
				}				

				#マナブースト　杖・扇限定
				$ent_mnb="!0";
				if($q[14] =~ m/A14|A15/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_mnb = "!10";}
					elsif(rand(1000) < 7){$ent_mnb = "!9";}
					elsif(rand(1000) < 14){$ent_mnb = "!8";}
					elsif(rand(1000) < 28){$ent_mnb = "!7";}
					elsif(rand(1000) < 36){$ent_mnb = "!6";}
					elsif(rand(1000) < 51){$ent_mnb = "!5";}
					elsif(rand(1000) < 78){$ent_mnb = "!4";}
					elsif(rand(1000) < 99){$ent_mnb = "!3";}
					elsif(rand(1000) < 152){$ent_mnb = "!2";}
					else{$ent_mnb = "!1";}
				
				}

				#南瓜キラー
				$ent_kabok="!0";
				if(($q[14] =~ m/A02/ && $q[7] =~ m/!11/ || $q[14] =~ m/A14|A15/) && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_kabok = "!10";}
					elsif(rand(1000) < 7){$ent_kabok = "!9";}
					elsif(rand(1000) < 14){$ent_kabok = "!8";}
					elsif(rand(1000) < 28){$ent_kabok = "!7";}
					elsif(rand(1000) < 36){$ent_kabok = "!6";}
					elsif(rand(1000) < 51){$ent_kabok = "!5";}
					elsif(rand(1000) < 78){$ent_kabok = "!4";}
					elsif(rand(1000) < 99){$ent_kabok = "!3";}
					elsif(rand(1000) < 152){$ent_kabok = "!2";}
					else{$ent_kabok = "!1";}
				
				}
				
				#南瓜ガード
				$ent_kabog="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_kabog = "!10";}
					elsif(rand(1000) < 7){$ent_kabog = "!9";}
					elsif(rand(1000) < 14){$ent_kabog = "!8";}
					elsif(rand(1000) < 28){$ent_kabog = "!7";}
					elsif(rand(1000) < 36){$ent_kabog = "!6";}
					elsif(rand(1000) < 51){$ent_kabog = "!5";}
					elsif(rand(1000) < 78){$ent_kabog = "!4";}
					elsif(rand(1000) < 99){$ent_kabog = "!3";}
					elsif(rand(1000) < 152){$ent_kabog = "!2";}
					else{$ent_kabog = "!1";}
				
				}

				#トレジャー発見率アップ
				$ent_tore="!0";
				if($q[14] =~ m/A27|A30/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_tore = "!10";}
					elsif(rand(1000) < 7){$ent_tore = "!9";}
					elsif(rand(1000) < 14){$ent_tore = "!8";}
					elsif(rand(1000) < 28){$ent_tore = "!7";}
					elsif(rand(1000) < 36){$ent_tore = "!6";}
					elsif(rand(1000) < 51){$ent_tore = "!5";}
					elsif(rand(1000) < 78){$ent_tore = "!4";}
					elsif(rand(1000) < 99){$ent_tore = "!3";}
					elsif(rand(1000) < 152){$ent_tore = "!2";}
					else{$ent_tore = "!1";}
				
				}
				
				#RESアップ
				$ent_res="!0";
				if($q[14] =~ m/A27|A28|A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_res = "!10";}
					elsif(rand(1000) < 7){$ent_res = "!9";}
					elsif(rand(1000) < 14){$ent_res = "!8";}
					elsif(rand(1000) < 28){$ent_res = "!7";}
					elsif(rand(1000) < 36){$ent_res = "!6";}
					elsif(rand(1000) < 51){$ent_res = "!5";}
					elsif(rand(1000) < 78){$ent_res = "!4";}
					elsif(rand(1000) < 99){$ent_res = "!3";}
					elsif(rand(1000) < 152){$ent_res = "!2";}
					else{$ent_res = "!1";}
				
				}

				#火属性攻撃力アップ
				$ent_fireb="!0";
				$flg_EntSetOk = 0;
				if($q[7] =~ m/!01/){$flg_EntSetOk = 1;}
				elsif($q[7] !~ m/!00|!01|!02|!03|!04|!05/){$flg_EntSetOk = 1;}
				if($q[14] =~ m/A02|A14|A15/ && (rand(100) < 5 + $MFUP) && $flg_EntSetOk == 1){

					if(rand(1000) < 2){$ent_fireb = "!10";}
					elsif(rand(1000) < 7){$ent_fireb = "!9";}
					elsif(rand(1000) < 14){$ent_fireb = "!8";}
					elsif(rand(1000) < 28){$ent_fireb = "!7";}
					elsif(rand(1000) < 36){$ent_fireb = "!6";}
					elsif(rand(1000) < 51){$ent_fireb = "!5";}
					elsif(rand(1000) < 78){$ent_fireb = "!4";}
					elsif(rand(1000) < 99){$ent_fireb = "!3";}
					elsif(rand(1000) < 152){$ent_fireb = "!2";}
					else{$ent_fireb = "!1";}
					
				}

				#水属性攻撃力アップ
				$ent_waterb="!0";
				$flg_EntSetOk = 0;
				if($q[7] =~ m/!03/){$flg_EntSetOk = 1;}
				elsif($q[7] !~ m/!00|!01|!02|!03|!04|!05/){$flg_EntSetOk = 1;}
				if($q[14] =~ m/A02|A14|A15/ && (rand(100) < 5 + $MFUP) && $flg_EntSetOk == 1){

					if(rand(1000) < 2){$ent_waterb = "!10";}
					elsif(rand(1000) < 7){$ent_waterb = "!9";}
					elsif(rand(1000) < 14){$ent_waterb = "!8";}
					elsif(rand(1000) < 28){$ent_waterb = "!7";}
					elsif(rand(1000) < 36){$ent_waterb = "!6";}
					elsif(rand(1000) < 51){$ent_waterb = "!5";}
					elsif(rand(1000) < 78){$ent_waterb = "!4";}
					elsif(rand(1000) < 99){$ent_waterb = "!3";}
					elsif(rand(1000) < 152){$ent_waterb = "!2";}
					else{$ent_waterb = "!1";}
					
				}

				#大地属性攻撃力アップ
				$ent_earthb="!0";
				$flg_EntSetOk = 0;
				if($q[7] =~ m/!02/){$flg_EntSetOk = 1;}
				elsif($q[7] !~ m/!00|!01|!02|!03|!04|!05/){$flg_EntSetOk = 1;}
				if($q[14] =~ m/A02|A14|A15/ && (rand(100) < 5 + $MFUP) && $flg_EntSetOk == 1){

					if(rand(1000) < 2){$ent_earthb = "!10";}
					elsif(rand(1000) < 7){$ent_earthb = "!9";}
					elsif(rand(1000) < 14){$ent_earthb = "!8";}
					elsif(rand(1000) < 28){$ent_earthb = "!7";}
					elsif(rand(1000) < 36){$ent_earthb = "!6";}
					elsif(rand(1000) < 51){$ent_earthb = "!5";}
					elsif(rand(1000) < 78){$ent_earthb = "!4";}
					elsif(rand(1000) < 99){$ent_earthb = "!3";}
					elsif(rand(1000) < 152){$ent_earthb = "!2";}
					else{$ent_earthb = "!1";}
					
				}

				#風属性攻撃力アップ
				$ent_windb="!0";
				$flg_EntSetOk = 0;
				if($q[7] =~ m/!00/){$flg_EntSetOk = 1;}
				elsif($q[7] !~ m/!00|!01|!02|!03|!04|!05/){$flg_EntSetOk = 1;}
				if($q[14] =~ m/A02|A14|A15/ && (rand(100) < 5 + $MFUP) && $flg_EntSetOk == 1){

					if(rand(1000) < 2){$ent_windb = "!10";}
					elsif(rand(1000) < 7){$ent_windb = "!9";}
					elsif(rand(1000) < 14){$ent_windb = "!8";}
					elsif(rand(1000) < 28){$ent_windb = "!7";}
					elsif(rand(1000) < 36){$ent_windb = "!6";}
					elsif(rand(1000) < 51){$ent_windb = "!5";}
					elsif(rand(1000) < 78){$ent_windb = "!4";}
					elsif(rand(1000) < 99){$ent_windb = "!3";}
					elsif(rand(1000) < 152){$ent_windb = "!2";}
					else{$ent_windb = "!1";}
					
				}

				#神聖属性攻撃力アップ
				$ent_saintb="!0";
				$flg_EntSetOk = 0;
				if($q[7] =~ m/!04/){$flg_EntSetOk = 1;}
				elsif($q[7] !~ m/!00|!01|!02|!03|!04|!05/){$flg_EntSetOk = 1;}
				if($q[14] =~ m/A02|A14|A15/ && (rand(100) < 5 + $MFUP) && $flg_EntSetOk == 1){

					if(rand(1000) < 2){$ent_saintb = "!10";}
					elsif(rand(1000) < 7){$ent_saintb = "!9";}
					elsif(rand(1000) < 14){$ent_saintb = "!8";}
					elsif(rand(1000) < 28){$ent_saintb = "!7";}
					elsif(rand(1000) < 36){$ent_saintb = "!6";}
					elsif(rand(1000) < 51){$ent_saintb = "!5";}
					elsif(rand(1000) < 78){$ent_saintb = "!4";}
					elsif(rand(1000) < 99){$ent_saintb = "!3";}
					elsif(rand(1000) < 152){$ent_saintb = "!2";}
					else{$ent_saintb = "!1";}
					
				}
				
				#暗黒属性攻撃力アップ
				$ent_darkb="!0";
				$flg_EntSetOk = 0;
				if($q[7] =~ m/!05/){$flg_EntSetOk = 1;}
				elsif($q[7] !~ m/!00|!01|!02|!03|!04|!05/){$flg_EntSetOk = 1;}
				if($q[14] =~ m/A02|A14|A15/ && (rand(100) < 5 + $MFUP) && $flg_EntSetOk == 1){

					if(rand(1000) < 2){$ent_darkb = "!10";}
					elsif(rand(1000) < 7){$ent_darkb = "!9";}
					elsif(rand(1000) < 14){$ent_darkb = "!8";}
					elsif(rand(1000) < 28){$ent_darkb = "!7";}
					elsif(rand(1000) < 36){$ent_darkb = "!6";}
					elsif(rand(1000) < 51){$ent_darkb = "!5";}
					elsif(rand(1000) < 78){$ent_darkb = "!4";}
					elsif(rand(1000) < 99){$ent_darkb = "!3";}
					elsif(rand(1000) < 152){$ent_darkb = "!2";}
					else{$ent_darkb = "!1";}
					
				}

				#火属性ダメージ軽減
				$ent_fireg="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_fireg = "!10";}
					elsif(rand(1000) < 7){$ent_fireg = "!9";}
					elsif(rand(1000) < 14){$ent_fireg = "!8";}
					elsif(rand(1000) < 28){$ent_fireg = "!7";}
					elsif(rand(1000) < 36){$ent_fireg = "!6";}
					elsif(rand(1000) < 51){$ent_fireg = "!5";}
					elsif(rand(1000) < 78){$ent_fireg = "!4";}
					elsif(rand(1000) < 99){$ent_fireg = "!3";}
					elsif(rand(1000) < 152){$ent_fireg = "!2";}
					else{$ent_fireg = "!1";}
					
				}
				
				#水属性ダメージ軽減
				$ent_waterg="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_waterg = "!10";}
					elsif(rand(1000) < 7){$ent_waterg = "!9";}
					elsif(rand(1000) < 14){$ent_waterg = "!8";}
					elsif(rand(1000) < 28){$ent_waterg = "!7";}
					elsif(rand(1000) < 36){$ent_waterg = "!6";}
					elsif(rand(1000) < 51){$ent_waterg = "!5";}
					elsif(rand(1000) < 78){$ent_waterg = "!4";}
					elsif(rand(1000) < 99){$ent_waterg = "!3";}
					elsif(rand(1000) < 152){$ent_waterg = "!2";}
					else{$ent_waterg = "!1";}
					
				}

				#大地属性ダメージ軽減
				$ent_earthg="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_earthg = "!10";}
					elsif(rand(1000) < 7){$ent_earthg = "!9";}
					elsif(rand(1000) < 14){$ent_earthg = "!8";}
					elsif(rand(1000) < 28){$ent_earthg = "!7";}
					elsif(rand(1000) < 36){$ent_earthg = "!6";}
					elsif(rand(1000) < 51){$ent_earthg = "!5";}
					elsif(rand(1000) < 78){$ent_earthg = "!4";}
					elsif(rand(1000) < 99){$ent_earthg = "!3";}
					elsif(rand(1000) < 152){$ent_earthg = "!2";}
					else{$ent_earthg = "!1";}
					
				}

				#風属性ダメージ軽減
				$ent_windg="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_windg = "!10";}
					elsif(rand(1000) < 7){$ent_windg = "!9";}
					elsif(rand(1000) < 14){$ent_windg = "!8";}
					elsif(rand(1000) < 28){$ent_windg = "!7";}
					elsif(rand(1000) < 36){$ent_windg = "!6";}
					elsif(rand(1000) < 51){$ent_windg = "!5";}
					elsif(rand(1000) < 78){$ent_windg = "!4";}
					elsif(rand(1000) < 99){$ent_windg = "!3";}
					elsif(rand(1000) < 152){$ent_windg = "!2";}
					else{$ent_windg = "!1";}
					
				}

				#神聖属性ダメージ軽減
				$ent_saintg="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_saintg = "!10";}
					elsif(rand(1000) < 7){$ent_saintg = "!9";}
					elsif(rand(1000) < 14){$ent_saintg = "!8";}
					elsif(rand(1000) < 28){$ent_saintg = "!7";}
					elsif(rand(1000) < 36){$ent_saintg = "!6";}
					elsif(rand(1000) < 51){$ent_saintg = "!5";}
					elsif(rand(1000) < 78){$ent_saintg = "!4";}
					elsif(rand(1000) < 99){$ent_saintg = "!3";}
					elsif(rand(1000) < 152){$ent_saintg = "!2";}
					else{$ent_saintg = "!1";}
					
				}

				#暗黒属性ダメージ軽減
				$ent_darkg="!0";
				if($q[14] =~ m/A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_darkg = "!10";}
					elsif(rand(1000) < 7){$ent_darkg = "!9";}
					elsif(rand(1000) < 14){$ent_darkg = "!8";}
					elsif(rand(1000) < 28){$ent_darkg = "!7";}
					elsif(rand(1000) < 36){$ent_darkg = "!6";}
					elsif(rand(1000) < 51){$ent_darkg = "!5";}
					elsif(rand(1000) < 78){$ent_darkg = "!4";}
					elsif(rand(1000) < 99){$ent_darkg = "!3";}
					elsif(rand(1000) < 152){$ent_darkg = "!2";}
					else{$ent_darkg = "!1";}
					
				}

				#無属性ダメージ軽減
				$ent_img="!0";
				if($q[14] =~ m/A28|A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_img = "!10";}
					elsif(rand(1000) < 7){$ent_img = "!9";}
					elsif(rand(1000) < 14){$ent_img = "!8";}
					elsif(rand(1000) < 28){$ent_img = "!7";}
					elsif(rand(1000) < 36){$ent_img = "!6";}
					elsif(rand(1000) < 51){$ent_img = "!5";}
					elsif(rand(1000) < 78){$ent_img = "!4";}
					elsif(rand(1000) < 99){$ent_img = "!3";}
					elsif(rand(1000) < 152){$ent_img = "!2";}
					else{$ent_img = "!1";}
					
				}

				#獲得Gothアップ
				$ent_gou="!0";
				if($q[14] =~ m/A02|A30/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_gou = "!10";}
					elsif(rand(1000) < 7){$ent_gou = "!9";}
					elsif(rand(1000) < 14){$ent_gou = "!8";}
					elsif(rand(1000) < 28){$ent_gou = "!7";}
					elsif(rand(1000) < 36){$ent_gou = "!6";}
					elsif(rand(1000) < 51){$ent_gou = "!5";}
					elsif(rand(1000) < 78){$ent_gou = "!4";}
					elsif(rand(1000) < 99){$ent_gou = "!3";}
					elsif(rand(1000) < 152){$ent_gou = "!2";}
					else{$ent_gou = "!1";}
					
				}

				#瀕死時HP回復 →戦術適性
				$ent_hhp="!0";
				if($q[14] =~ m/A28/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_hhp = "!10";}
					elsif(rand(1000) < 7){$ent_hhp = "!9";}
					elsif(rand(1000) < 14){$ent_hhp = "!8";}
					elsif(rand(1000) < 28){$ent_hhp = "!7";}
					elsif(rand(1000) < 36){$ent_hhp = "!6";}
					elsif(rand(1000) < 51){$ent_hhp = "!5";}
					elsif(rand(1000) < 78){$ent_hhp = "!4";}
					elsif(rand(1000) < 99){$ent_hhp = "!3";}
					elsif(rand(1000) < 152){$ent_hhp = "!2";}
					else{$ent_hhp = "!1";}
					
				}
				
				#戦闘不能時MP回復 →マナリカバリー
				$ent_mmp="!0";
				if($q[14] =~ m/A27|A28|A30/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_mmp = "!10";}
					elsif(rand(1000) < 7){$ent_mmp = "!9";}
					elsif(rand(1000) < 14){$ent_mmp = "!8";}
					elsif(rand(1000) < 28){$ent_mmp = "!7";}
					elsif(rand(1000) < 36){$ent_mmp = "!6";}
					elsif(rand(1000) < 51){$ent_mmp = "!5";}
					elsif(rand(1000) < 78){$ent_mmp = "!4";}
					elsif(rand(1000) < 99){$ent_mmp = "!3";}
					elsif(rand(1000) < 152){$ent_mmp = "!2";}
					else{$ent_mmp = "!1";}
					
				}
				
				#ダメージ分配
				$ent_dam="!0";
				if($q[14] =~ m/A27|A28|A29/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_dam = "!10";}
					elsif(rand(1000) < 7){$ent_dam = "!9";}
					elsif(rand(1000) < 14){$ent_dam = "!8";}
					elsif(rand(1000) < 28){$ent_dam = "!7";}
					elsif(rand(1000) < 36){$ent_dam = "!6";}
					elsif(rand(1000) < 51){$ent_dam = "!5";}
					elsif(rand(1000) < 78){$ent_dam = "!4";}
					elsif(rand(1000) < 99){$ent_dam = "!3";}
					elsif(rand(1000) < 152){$ent_dam = "!2";}
					else{$ent_dam = "!1";}
					
				}

				#回復魔法強化
				$ent_hea="!0";
				if($q[14] =~ m/A14|A15|A30/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_hea = "!10";}
					elsif(rand(1000) < 7){$ent_hea = "!9";}
					elsif(rand(1000) < 14){$ent_hea = "!8";}
					elsif(rand(1000) < 28){$ent_hea = "!7";}
					elsif(rand(1000) < 36){$ent_hea = "!6";}
					elsif(rand(1000) < 51){$ent_hea = "!5";}
					elsif(rand(1000) < 78){$ent_hea = "!4";}
					elsif(rand(1000) < 99){$ent_hea = "!3";}
					elsif(rand(1000) < 152){$ent_hea = "!2";}
					else{$ent_hea = "!1";}
					
				}

				#クリティカル
				$ent_cri="!0";
				if($q[14] =~ m/A02/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_cri = "!10";}
					elsif(rand(1000) < 7){$ent_cri = "!9";}
					elsif(rand(1000) < 14){$ent_cri = "!8";}
					elsif(rand(1000) < 28){$ent_cri = "!7";}
					elsif(rand(1000) < 36){$ent_cri = "!6";}
					elsif(rand(1000) < 51){$ent_cri = "!5";}
					elsif(rand(1000) < 78){$ent_cri = "!4";}
					elsif(rand(1000) < 99){$ent_cri = "!3";}
					elsif(rand(1000) < 152){$ent_cri = "!2";}
					else{$ent_cri = "!1";}
					
				}

				#貫通攻撃
				$ent_brk="!0";
				if($q[14] =~ m/A02/ && (rand(100) < 5 + $MFUP)){

					if(rand(1000) < 2){$ent_brk = "!10";}
					elsif(rand(1000) < 7){$ent_brk = "!9";}
					elsif(rand(1000) < 14){$ent_brk = "!8";}
					elsif(rand(1000) < 28){$ent_brk = "!7";}
					elsif(rand(1000) < 36){$ent_brk = "!6";}
					elsif(rand(1000) < 51){$ent_brk = "!5";}
					elsif(rand(1000) < 78){$ent_brk = "!4";}
					elsif(rand(1000) < 99){$ent_brk = "!3";}
					elsif(rand(1000) < 152){$ent_brk = "!2";}
					else{$ent_brk = "!1";}
					
				}
				
				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi$ent_dl$ent_mnb$ent_kabok$ent_kabog$ent_tore$ent_mf$ent_res$ent_fireb$ent_waterb$ent_earthb$ent_windb$ent_saintb$ent_darkb$ent_fireg$ent_waterg$ent_earthg$ent_windg$ent_saintg$ent_darkg$ent_img$ent_gou$ent_hhp$ent_mmp$ent_dam$ent_hea$ent_cri$ent_brk";

			}

			if (!$PL_VALUES[10] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[10]=$gw;$PL_VALUES[10].=$ent;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
			elsif(!$PL_VALUES[11] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[11]=$gw;$PL_VALUES[11].=$ent;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
			elsif(!$PL_VALUES[38] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[38]=$gw;$PL_VALUES[38].=$ent;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
			elsif(!$PL_VALUES[41] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[41]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
			elsif(!$PL_VALUES[42] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[42]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
			elsif(!$PL_VALUES[43] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[43]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
#			elsif(!$PL_VALUES[46]){$PL_VALUES[46]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。ストックに格納されました。</font><br>\n";}
#			elsif(!$PL_VALUES[46] && $PL_STF eq "1"){$PL_VALUES[46]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。ストックに格納されました。</font><br>\n";}
			elsif(!$PL_VALUES[46] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[46]=$gw;$PL_VALUES[46].=$ent;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。ストックに格納されました。</font><br>\n";}
			elsif(!$PL_VALUES[46] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[46]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。ストックに格納されました。</font><br>\n";}

			$ItemChk=$gw;
		}
	  }

		#アビリティシステム
		if($AbiSys == 1 && $AbiMukou == 0){	
			#欲望の権化
			if($ABI_sA[2] =~ m/!A0078/ || $ABI_sB[2] =~ m/!A0078/ || $ABI_sC[2] =~ m/!A0078/){

				my@al=keys %WEAPON_LIST;$alw=@al;
				$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
				@q=split(/\,/,$WEAPON_LIST{"$gw"});

			  if ($PL_W[7] =~ m/!1d/ && ($PL_sB[7] =~ m/!1c/ || $PL_sC[7] =~ m/!1c/ || $PL_sD[7] =~ m/!1c/)){
				#属性魔法書の獲得処理　今は触らない
				if($q[8] > rand(80) && $q[7] !~ m/!1c/){
					if(!$PL_VALUES[10]){$PL_VALUES[10]=$gw;}
					elsif(!$PL_VALUES[11]){$PL_VALUES[11]=$gw;}
					elsif(!$PL_VALUES[38]){$PL_VALUES[38]=$gw;}
					print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";
				}
			  }else{
				if ($q[8] > rand(60) && ($q[7] !~ m/!71|!72/ || ($q[7] =~ m/!71/ && $PL_VALUES[39] eq "1") || ($q[7] =~ m/!72/ && $PL_VALUES[39] eq "2"))){
		#		if ($q[8] > (rand(50) * $toretore)){
					if (!$PL_VALUES[10] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[10]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
					elsif(!$PL_VALUES[11] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[11]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
					elsif(!$PL_VALUES[38] && ($q[11] == 0 || $q[11] == 9)){$PL_VALUES[38]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
					elsif(!$PL_VALUES[41] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[41]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
					elsif(!$PL_VALUES[42] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[42]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
					elsif(!$PL_VALUES[43] && $q[11] != 0 && $q[11] != 9){$PL_VALUES[43]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。</font><br>\n";}
					elsif(!$PL_VALUES[46]){$PL_VALUES[46]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。ストックに格納されました。</font><br>\n";}
		#			elsif(!$PL_VALUES[46] && $PL_STF eq "1"){$PL_VALUES[46]=$gw;$buki=1;print "<font color=\"#f7e957\">トレジャーを獲得。ストックに格納されました。</font><br>\n";}
					$ItemChk=$gw;
				}
			  }

			}
		}
		
	}

#褒章
#$ResultBattle==0 勝利　$ResultBattle==1 負け　$ResultBattle==2　引分け
	if($PL_VALUES[5] && !$PL_VALUES[28]){
		$M_AITEX0="$CL_VALUES[6]";
	}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUES[2]" && $CL_VALUE2[2]){
		$M_AITEX1="$CL_VALUES[8]";
	}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUES[3]" && $CL_VALUE2[3]){
		$M_AITEX2="$CL_VALUES[9]";
	}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUES[4]" && $CL_VALUE2[4]){
		$M_AITEX3="$CL_VALUES[10]";
	}

	if($HoushoFlg == 1 && ($CL_VALUES[7] > time || $CL_VALUES[37] > time) && $VS_VALUES[5] ne "" && ($VS_VALUES[5] eq "$M_AITEX0" || $VS_VALUES[5] eq "$M_AITEX1" || $VS_VALUES[5] eq "$M_AITEX2" || $VS_VALUES[5] eq "$M_AITEX3")){

		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] eq ""){$HC[0] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}
		@VHC=split(/!/,$VS_VALUES[50]);
		if($VHC[0] eq ""){$VHC[0] = 0;}
		if($VHC[1] eq ""){$VHC[1] = 0;}
		if($VHC[2] eq ""){$VHC[2] = 0;}

		#勝利
		if($ResultBattle==0){

			#相手が総帥の場合
			if($VS_VALUES[6] eq "1"){
				#現在貢献点+75
				$HC[0] = $HC[0] + 75;
				$HC[2] = $HC[2] + 75;
				#自身も総帥の場合+35
				if($PL_VALUES[6] eq "1"){
					#現在貢献点+35
					$HC[0] = $HC[0] + 35;
					$HC[2] = $HC[2] + 35;
				}elsif($PL_VALUES[6] eq "-1"){
				#自身も隊長の場合+20
					#現在貢献点+20
					$HC[0] = $HC[0] + 20;
					$HC[2] = $HC[2] + 20;
				}

				$VHC[0] = $VHC[0] + 5;
				$VHC[2] = $VHC[2] + 5;

			#相手が隊長の場合
			}elsif($VS_VALUES[6] eq "-1"){

				#現在貢献点+50
				$HC[0] = $HC[0] + 50;
				$HC[2] = $HC[2] + 50;
				#自身も総帥の場合+25
				if($PL_VALUES[6] eq "1"){
					#現在貢献点+25
					$HC[0] = $HC[0] + 25;
					$HC[2] = $HC[2] + 25;
				}elsif($PL_VALUES[6] eq "-1"){
				#自身も隊長の場合+15
					#現在貢献点+15
					$HC[0] = $HC[0] + 15;
					$HC[2] = $HC[2] + 15;
				}

				$VHC[0] = $VHC[0] + 3;
				$VHC[2] = $VHC[2] + 3;

			#隊長・総帥ではない場合
			}else{

				#現在貢献点+30
				$HC[0] = $HC[0] + 30;
				$HC[2] = $HC[2] + 30;
				#自身も総帥の場合+15
				if($PL_VALUES[6] eq "1"){
					#現在貢献点+15
					$HC[0] = $HC[0] + 15;
					$HC[2] = $HC[2] + 15;
				}elsif($PL_VALUES[6] eq "-1"){
				#自身も隊長の場合+10
					#現在貢献点+10
					$HC[0] = $HC[0] + 10;
					$HC[2] = $HC[2] + 10;
				}

			}

			$VHC[0] = $VHC[0] + 10;
			$VHC[2] = $VHC[2] + 10;

		#引分け
		}elsif($ResultBattle==2){

			#現在貢献点+5
			$HC[0] = $HC[0] + 5;
			$HC[2] = $HC[2] + 5;
			#自身も総帥の場合+3
			if($PL_VALUES[6] eq "1"){
				#現在貢献点+3
				$HC[0] = $HC[0] + 3;
				$HC[2] = $HC[2] + 3;
			}elsif($PL_VALUES[6] eq "-1"){
			#自身も隊長の場合+1
				#現在貢献点+1
				$HC[0] = $HC[0] + 1;
				$HC[2] = $HC[2] + 1;
			}

			$VHC[0] = $VHC[0] + 5;
			$VHC[2] = $VHC[2] + 5;

		#敗北
		}else{

			#自分が総帥の場合
			if($PL_VALUES[6] eq "1"){
				#現在貢献点+75
				$VHC[0] = $VHC[0] + 75;
				$VHC[2] = $VHC[2] + 75;
				#相手も総帥の場合+35
				if($VS_VALUES[6] eq "1"){
					#現在貢献点+35
					$VHC[0] = $VHC[0] + 35;
					$VHC[2] = $VHC[2] + 35;
				}elsif($VS_VALUES[6] eq "-1"){
				#相手も隊長の場合+20
					#現在貢献点+20
					$VHC[0] = $VHC[0] + 20;
					$VHC[2] = $VHC[2] + 20;
				}

				$HC[0] = $HC[0] + 5;
				$HC[2] = $HC[2] + 5;

			#自分が隊長の場合
			}elsif($PL_VALUES[6] eq "-1"){

				#現在貢献点+50
				$VHC[0] = $VHC[0] + 50;
				$VHC[2] = $VHC[2] + 50;
				#相手も総帥の場合+25
				if($VS_VALUES[6] eq "1"){
					#現在貢献点+25
					$VHC[0] = $VHC[0] + 25;
					$VHC[2] = $VHC[2] + 25;
				}elsif($VS_VALUES[6] eq "-1"){
				#相手も隊長の場合+15
					#現在貢献点+15
					$VHC[0] = $VHC[0] + 15;
					$VHC[2] = $VHC[2] + 15;
				}

				$HC[0] = $HC[0] + 3;
				$HC[2] = $HC[2] + 3;

			#隊長・総帥ではない場合
			}else{

				#現在貢献点+30
				$VHC[0] = $VHC[0] + 30;
				$VHC[2] = $VHC[2] + 30;
				#相手も総帥の場合+15
				if($VS_VALUES[6] eq "1"){
					#現在貢献点+15
					$VHC[0] = $VHC[0] + 15;
					$VHC[2] = $VHC[2] + 15;
				}elsif($PVS_VALUES[6] eq "-1"){
				#相手も隊長の場合+10
					#現在貢献点+10
					$VHC[0] = $VHC[0] + 10;
					$VHC[2] = $VHC[2] + 10;
				}

			}

			$HC[0] = $HC[0] + 10;
			$HC[2] = $HC[2] + 10;

		}

		#現在貢献点＞最大貢献点の場合は記録
		if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
		if($VHC[0] > $VHC[1]){$VHC[1] = $VHC[0];}

		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		$VS_VALUES[50] = "$VHC[0]!$VHC[1]!$VHC[2]!";

	}

#テレポート処理
#ジャンプウォール･･･　消費MP4000で相手の国に移動　テレポート･･･　消費MP1000で相手の国に移動

	$PL_TE = 0;
	if($PL_W[7] =~ m/!8e|!8f/ && $VS_VALUES[5] ne "メルト屋愛好会" && $VS_VALUES[5] ne "バルダー装備を崇める会" && $C_VALUES[7] < time && $VC_VALUES[7] < time){

		$PL_VALUES[5]=$VS_VALUES[5];$PL_VALUES[28]='';$PL_VALUES[0]=$PL_VALUES[6]=0;$PL_VALUES[39]=$VS_VALUES[39];
		
		if($PL_VALUES[39] eq "1"){$Conh="ゼテギネア大陸";}else{$Conh="ガリシア大陸";}

		if($PL_W[7] =~ m/!8e/){
			$PL_VALUES[17] = $PL_VALUES[17] - 4000;
			if($PL_VALUES[17] < 0){$PL_VALUES[17] = 0;}
			$PL_VALUES[8] = int($PL_VALUES[8] * 0.67);
			print "<font color=\"#f7e957\">ジャンプウォール発動！$Conhの$VS_VALUES[5]の国に移動しました。</font><br>\n";
#			print "<font color=\"#f7e957\">ジャンプウォール発動！$VS_VALUES[5]の国に移動しました。</font><br>\n";
		}else{
			$PL_VALUES[17] = $PL_VALUES[17] - 1000;
			if($PL_VALUES[17] < 0){$PL_VALUES[17] = 0;}
			print "<font color=\"#f7e957\">テレポート発動！$Conhの$VS_VALUES[5]の国に移動しました。</font><br>\n";
#			print "<font color=\"#f7e957\">テレポート発動！$VS_VALUES[5]の国に移動しました。</font><br>\n";
		}

		$PL_TE = 1;

	}

	#生命吸収
	if($Pl_WOnly eq "1" && $PL_WA07 > 0 && $PL_WA07 ne ""){
		$PL_VALUES[15] = $PL_VALUES[15] + int($PL_WA07*500);
		if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
		print "<font color=\"#f7e957\">生命吸収発動！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
	}

#戦術適性
#	if($PL_VALUES[25] ne "1" && $PL_WA28 ne "" && $PL_WA28 > 0 && $PL_flgEnt > 0){
	if($PL_VALUES[25] ne "1" && $PL_WA28 ne "" && $PL_WA28 > 0){
		$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * $PL_WA28 * 0.01);
		if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$PL_VALUES[3]のHPが回復しました。</font><br>\n";
#	}elsif($PL_VALUES[25] ne "1" && $PL_WB28 ne "" && $PL_WB28 > 0 && $PL_flgEnt2 > 0){
	}elsif($PL_VALUES[25] ne "1" && $PL_WB28 ne "" && $PL_WB28 > 0){
		$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * $PL_WB28 * 0.01);
		if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$PL_VALUES[3]のHPが回復しました。</font><br>\n";
#	}elsif($PL_VALUES[25] ne "1" && $PL_WC28 ne "" && $PL_WC28 > 0 && $PL_flgEnt3 > 0){
	}elsif($PL_VALUES[25] ne "1" && $PL_WC28 ne "" && $PL_WC28 > 0){
		$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * $PL_WC28 * 0.01);
		if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$PL_VALUES[3]のHPが回復しました。</font><br>\n";
#	}elsif($PL_VALUES[25] ne "1" && $PL_WD28 ne "" && $PL_WD28 > 0 && $PL_flgEnt4 > 0){
	}elsif($PL_VALUES[25] ne "1" && $PL_WD28 ne "" && $PL_WD28 > 0){
		$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * $PL_WD28 * 0.01);
		if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$PL_VALUES[3]のHPが回復しました。</font><br>\n";
	}
	
#	if($VS_VALUES[25] ne "1" && $VS_WA28 ne "" && $VS_WA28 > 0 && $VS_flgEnt > 0){
	if($VS_VALUES[25] ne "1" && $VS_WA28 ne "" && $VS_WA28 > 0){
		$VS_VALUES[15] = $VS_VALUES[15] + int($VS_VALUES[16] * $VS_WA28 * 0.01);
		if($VS_VALUES[15] > $VS_VALUES[16]){$VS_VALUES[15]=$VS_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$VS_VALUES[3]のHPが回復しました。</font><br>\n";
#	}elsif($VS_VALUES[25] ne "1" && $VS_WB28 ne "" && $VS_WB28 > 0 && $VS_flgEnt2 > 0){
	}elsif($VS_VALUES[25] ne "1" && $VS_WB28 ne "" && $VS_WB28 > 0){
		$VS_VALUES[15] = $VS_VALUES[15] + int($VS_VALUES[16] * $VS_WB28 * 0.01);
		if($VS_VALUES[15] > $VS_VALUES[16]){$VS_VALUES[15]=$VS_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$VS_VALUES[3]のHPが回復しました。</font><br>\n";
#	}elsif($VS_VALUES[25] ne "1" && $VS_WC28 ne "" && $VS_WC28 > 0 && $VS_flgEnt3 > 0){
	}elsif($VS_VALUES[25] ne "1" && $VS_WC28 ne "" && $VS_WC28 > 0){
		$VS_VALUES[15] = $VS_VALUES[15] + int($VS_VALUES[16] * $VS_WC28 * 0.01);
		if($VS_VALUES[15] > $VS_VALUES[16]){$VS_VALUES[15]=$VS_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$VS_VALUES[3]のHPが回復しました。</font><br>\n";
#	}elsif($VS_VALUES[25] ne "1" && $VS_WD28 ne "" && $VS_WD28 > 0 && $VS_flgEnt4 > 0){
	}elsif($VS_VALUES[25] ne "1" && $VS_WD28 ne "" && $VS_WD28 > 0){
		$VS_VALUES[15] = $VS_VALUES[15] + int($VS_VALUES[16] * $VS_WD28 * 0.01);
		if($VS_VALUES[15] > $VS_VALUES[16]){$VS_VALUES[15]=$VS_VALUES[16];}
		print "<font color=\"#f7e957\">戦術適性の効果により、$VS_VALUES[3]のHPが回復しました。</font><br>\n";
	}

#マナリカバリー
	$PL_ManaR = 0;

#	if($PL_WA29 ne "" && $PL_WA29 > 0 && $PL_flgEnt > 0){$PL_ManaR = $PL_ManaR + $PL_WA29;}
#	if($PL_WB29 ne "" && $PL_WB29 > 0 && $PL_flgEnt2 > 0){$PL_ManaR = $PL_ManaR + $PL_WB29;}
#	if($PL_WC29 ne "" && $PL_WC29 > 0 && $PL_flgEnt3 > 0){$PL_ManaR = $PL_ManaR + $PL_WC29;}
#	if($PL_WD29 ne "" && $PL_WD29 > 0 && $PL_flgEnt4 > 0){$PL_ManaR = $PL_ManaR + $PL_WD29;}
	if($PL_WA29 ne "" && $PL_WA29 > 0){$PL_ManaR = $PL_ManaR + $PL_WA29;}
	if($PL_WB29 ne "" && $PL_WB29 > 0){$PL_ManaR = $PL_ManaR + $PL_WB29;}
	if($PL_WC29 ne "" && $PL_WC29 > 0){$PL_ManaR = $PL_ManaR + $PL_WC29;}
	if($PL_WD29 ne "" && $PL_WD29 > 0){$PL_ManaR = $PL_ManaR + $PL_WD29;}
	
	if(rand(100) <= $PL_ManaR && $PL_ManaR > 0){
		$PL_VALUES[17] = $PL_VALUES[17] + $PL_ManaR * 20;
		if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}
		print "<font color=\"#f7e957\">マナリカバリー発動！$PL_VALUES[3]のMPが回復しました。</font><br>\n";
	}
#print "<font color=\"#f7e957\">テスト $PL_ManaR $PL_WA29 $PL_WB29 $PL_WC29 $PL_WD29</font><br>\n";
	#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0){	
	
		#ブラッドウエポン
#		if(($ABI_sA[2] =~ m/!A0076/ || $ABI_sB[2] =~ m/!A0076/ || $ABI_sC[2] =~ m/!A0076/) && $ResultBattle ne "1" && ($Pl_WOnly eq "1" || $PL_sS[0] eq "怒号魔破拳")){
		if(($ABI_sA[2] =~ m/!A0076/ || $ABI_sB[2] =~ m/!A0076/ || $ABI_sC[2] =~ m/!A0076/) && $PL_VALUES[25] ne "1" && $PL_W[7] =~ m/!11/ && ($Pl_WOnly eq "1" || $PL_sS[0] eq "怒号魔破拳")){
		
			$PL_VALUES[15] = $PL_VALUES[15] + int($Pl_AtPoint*0.2);
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
			print "<font color=\"#f7e957\">ブラッドウエポン発動！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
			
		}

		#一撃の刃
		if(($ABI_sA[2] =~ m/!A0057/ || $ABI_sB[2] =~ m/!A0057/ || $ABI_sC[2] =~ m/!A0057/) && rand(100) < 8 && $ResultBattle==2){

			$VS_VALUES[15]=0;$VS_VALUES[25]=1;
			print "<font color=\"#00FF00\">一撃の刃発動！$VS_VALUES[3]は戦闘不\能\！！</font><br>\n";

		}

		if(($VABI_sA[2] =~ m/!A0057/ || $VABI_sB[2] =~ m/!A0057/ || $VABI_sC[2] =~ m/!A0057/) && rand(100) < 8 && $ResultBattle==2){

			$PL_VALUES[15]=0;$PL_VALUES[25]=1;
			print "<font color=\"#00FF00\">一撃の刃発動！$PL_VALUES[3]は戦闘不\能\！！</font><br>\n";

		}
	
		#武士道精神
		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0072/ || $ABI_sB[2] =~ m/!A0072/ || $ABI_sC[2] =~ m/!A0072/ || $VABI_sA[2] =~ m/!A0072/ || $VABI_sB[2] =~ m/!A0072/ || $VABI_sC[2] =~ m/!A0072/)){
		
			if($PL_VALUES[15] < int($PL_VALUES[16]*0.2)){
				$PL_VALUES[15]=0;$PL_VALUES[25]=1;
				print "<font color=\"#00FF00\">武士道精神発動！$PL_VALUES[3]は戦闘不\能\！！</font><br>\n";			
			}

			if($VS_VALUES[15] < int($VS_VALUES[16]*0.2)){
				$VS_VALUES[15]=0;$VS_VALUES[25]=1;
				print "<font color=\"#00FF00\">武士道精神発動！$VS_VALUES[3]は戦闘不\能\！！</font><br>\n";			
			}
		
		}

		#ラーニング「アトロポス」
		if(($ABI_sA[2] =~ m/!A0079/ || $ABI_sB[2] =~ m/!A0079/ || $ABI_sC[2] =~ m/!A0079/) && $Pl_WOnly eq "1" && $PL_W[12] =~ m/e001|e012/ && rand(255) > 253 && $PL_VALUES[25] ne "1"){

			if(!$PL_VALUES[41]){$PL_VALUES[41]="2da";print "<font color=\"#f7e957\">アトロポスを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[42]){$PL_VALUES[42]="2da";print "<font color=\"#f7e957\">アトロポスを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[43]){$PL_VALUES[43]="2da";print "<font color=\"#f7e957\">アトロポスを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[46]){$PL_VALUES[46]="2da";print "<font color=\"#f7e957\">アトロポスを習得した！！ストックに格納されました。</font><br>\n";}

		}
		#ラーニング「ラケシス」
		if(($ABI_sA[2] =~ m/!A0080/ || $ABI_sB[2] =~ m/!A0080/ || $ABI_sC[2] =~ m/!A0080/) && $Pl_WOnly eq "1" && $PL_W[12] =~ m/e009|e011/ && rand(255) > 253 && $PL_VALUES[25] ne "1"){

			if(!$PL_VALUES[41]){$PL_VALUES[41]="2db";print "<font color=\"#f7e957\">ラケシスを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[42]){$PL_VALUES[42]="2db";print "<font color=\"#f7e957\">ラケシスを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[43]){$PL_VALUES[43]="2db";print "<font color=\"#f7e957\">ラケシスを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[46]){$PL_VALUES[46]="2db";print "<font color=\"#f7e957\">ラケシスを習得した！！ストックに格納されました。</font><br>\n";}

		}
		#ラーニング「クロト」
		if(($ABI_sA[2] =~ m/!A0081/ || $ABI_sB[2] =~ m/!A0081/ || $ABI_sC[2] =~ m/!A0081/) && $Pl_WOnly eq "1" && $PL_W[12] =~ m/e007|e013/ && rand(255) > 253 && $PL_VALUES[25] ne "1"){

			if(!$PL_VALUES[41]){$PL_VALUES[41]="2dc";print "<font color=\"#f7e957\">クロトを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[42]){$PL_VALUES[42]="2dc";print "<font color=\"#f7e957\">クロトを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[43]){$PL_VALUES[43]="2dc";print "<font color=\"#f7e957\">クロトを習得した！！</font><br>\n";}
			elsif(!$PL_VALUES[46]){$PL_VALUES[46]="2dc";print "<font color=\"#f7e957\">クロトを習得した！！ストックに格納されました。</font><br>\n";}

		}

	}

#エンチャント　ダメージ分配
	$PL_DamR = 0;
	$VS_DamR = 0;

#	if($PL_WA30 ne "" && $PL_WA30 > 0 && $PL_flgEnt > 0){$PL_DamR = $PL_DamR + $PL_WA30;}
#	if($PL_WB30 ne "" && $PL_WB30 > 0 && $PL_flgEnt2 > 0){$PL_DamR = $PL_DamR + $PL_WB30;}
#	if($PL_WC30 ne "" && $PL_WC30 > 0 && $PL_flgEnt3 > 0){$PL_DamR = $PL_DamR + $PL_WC30;}
#	if($PL_WD30 ne "" && $PL_WD30 > 0 && $PL_flgEnt4 > 0){$PL_DamR = $PL_DamR + $PL_WD30;}

#	if($VS_WA30 ne "" && $VS_WA30 > 0 && $VS_flgEnt > 0){$VS_DamR = $VS_DamR + $VS_WA30;}
#	if($VS_WB30 ne "" && $VS_WB30 > 0 && $VS_flgEnt2 > 0){$VS_DamR = $VS_DamR + $VS_WB30;}
#	if($VS_WC30 ne "" && $VS_WC30 > 0 && $VS_flgEnt3 > 0){$VS_DamR = $VS_DamR + $VS_WC30;}
#	if($VS_WD30 ne "" && $VS_WD30 > 0 && $VS_flgEnt4 > 0){$VS_DamR = $VS_DamR + $VS_WD30;}

	if($PL_WA30 ne "" && $PL_WA30 > 0){$PL_DamR = $PL_DamR + $PL_WA30;}
	if($PL_WB30 ne "" && $PL_WB30 > 0){$PL_DamR = $PL_DamR + $PL_WB30;}
	if($PL_WC30 ne "" && $PL_WC30 > 0){$PL_DamR = $PL_DamR + $PL_WC30;}
	if($PL_WD30 ne "" && $PL_WD30 > 0){$PL_DamR = $PL_DamR + $PL_WD30;}

	if($VS_WA30 ne "" && $VS_WA30 > 0){$VS_DamR = $VS_DamR + $VS_WA30;}
	if($VS_WB30 ne "" && $VS_WB30 > 0){$VS_DamR = $VS_DamR + $VS_WB30;}
	if($VS_WC30 ne "" && $VS_WC30 > 0){$VS_DamR = $VS_DamR + $VS_WC30;}
	if($VS_WD30 ne "" && $VS_WD30 > 0){$VS_DamR = $VS_DamR + $VS_WD30;}
	
	
	if($PL_DamR > 0 && rand(100) <= 40 && $Vs_AtPoint > 0){
		$VS_VALUES[15] = $VS_VALUES[15] - int($Vs_AtPoint * $PL_DamR * 0.04);
		if($VS_VALUES[15] <= 0){$VS_VALUES[15] = 0;$VS_VALUES[25] = 1;}
		print "<font color=\"#00FF00\">ダメージ分配発動！！</font><br>\n";
	}
	if($VS_DamR > 0 && rand(100) <= 40 && $Pl_AtPoint > 0){
		$PL_VALUES[15] = $PL_VALUES[15] - int($Pl_AtPoint * $VS_DamR * 0.04);
		if($PL_VALUES[15] <= 0){$PL_VALUES[15] = 0;$PL_VALUES[25] = 1;}
		print "<font color=\"#f7e957\">ダメージ分配発動！！</font><br>\n";
	}

#リジェネ
#	if($PL_W[7] !~ m/!1s|!1u|!1w/ && ($PL_sB[7] =~ m/!E0004/ && $PL_sC[7] !~ m/!1s|!1u|!1w/ && $PL_sD[7] !~ m/!1s|!1u|!1w/) || ($PL_sC[7] =~ m/!E0004/ && $PL_sB[7] !~ m/!1s|!1u|!1w/ && $PL_sD[7] !~ m/!1s|!1u|!1w/) || ($PL_sD[7] =~ m/!E0004/ && $PL_sB[7] !~ m/!1s|!1u|!1w/ && $PL_sC[7] !~ m/!1s|!1u|!1w/)){
#
#		if ($PL_VALUES[25] eq "0" && $VS_ELWEA != 5){
#			$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * 0.1);
#			if ($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
##			print "<font color=\"#f7e957\">リジェネレイト！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
#			print "<font color=\"#00FF00\">リジェネレイト！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
#		}
#	}

	if($PL_W[7] !~ m/!1s|!1u|!1w/ && (($PL_BFLAG && $PL_sB[7] =~ m/!E0004/) || ($PL_CFLAG && $PL_sC[7] =~ m/!E0004/) || ($PL_DFLAG && $PL_sD[7] =~ m/!E0004/))){
		$HPR = 0;
		$HPR = int($PL_CLASS[2]/2-0.5);

#		if ($PL_VALUES[25] eq "0" && $VS_ELWEA != 5){
		if ($PL_VALUES[25] eq "0" && $VS_W[7] !~ m/!05/){
#			$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * 0.1);
			$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * (0.07 + $HPR / 100));
			if ($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
			print "<font color=\"#00FF00\">リジェネレイト！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
		}

	}
##00FF00
#ドレインライフ
	if($PL_W[7] =~ m/!E0009/ || $PL_sS[7] =~ m/!E0009/){
		if ($PL_VALUES[25] eq "0" && $Pl_AtPoint > 0){
			$PL_VALUES[15] = $PL_VALUES[15] + int($Pl_AtPoint * 0.3);
			if ($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
			print "<font color=\"#f7e957\">HP吸収攻撃！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
		}
	}

#メディテ
	if(($PL_H[7] =~ m/!8q|!x8q/ || $PL_W[7] =~ m/!8q|!x8q/) && $PL_CLASS[17] =~ m/!E001/ && $Pl_AntiEl eq "0"){

		$PL_MP = 35;
		if($PL_CLASS[17] =~ m/!E002/){$PL_MP+=10;}
		$PL_MP = $PL_MP + int($PL_LVH/1000);
		$PL_MPD = int(rand(30)+30)/100;

		if(rand(100) <= $PL_MP){
			if ($PL_VALUES[25] eq "0"){
				$PL_MPKAIHUKU = int($VS_W[4] * $PL_MPD);
				if($PL_MPKAIHUKU>300){$PL_MPKAIHUKU = 300;}
				
				if($VS_W[4] > 1000){$PL_MPKAIHUKU = 0;}
				
				$PL_VALUES[17] = $PL_VALUES[17] + $PL_MPKAIHUKU + 20;
				
				if ($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}
				print "<font color=\"#f7e957\">クレイブマインド発動！$PL_VALUES[3]のMPが回復しました。</font><br>\n";
			}
		}

	}
	#オートリレイズ
	if($PL_CLASS[17] =~ m/!W021/ && $PL_VALUES[25] eq "1" && rand(100) < 15){
		$PL_VALUES[25]=0;
		print "<font color=\"#00FF00\">オートリレイズ発動！$PL_VALUES[3]の戦闘不\能\が回復しました。</font><br>\n";
	}
	if($VS_CLASS[17] =~ m/!W021/ && $VS_VALUES[25] eq "1" && rand(100) < 15){
		$VS_VALUES[25]=0;
		print "<font color=\"#00FF00\">オートリレイズ発動！$VS_VALUES[3]の戦闘不\能\が回復しました。</font><br>\n";
	}

	#アンデッドクラスのHP回復速度アップ　※対戦相手が神聖属性の場合は無効
	if($PL_CLASS[17] =~ m/!E004/ && $PL_VALUES[25] eq "1" && $VS_W[7] !~ m/!04/){
		$PL_VALUES[15] = int($PL_VALUES[16] * 0.4);
	}
	if($VS_CLASS[17] =~ m/!E004/ && $VS_VALUES[25] eq "1" && $PL_W[7] !~ m/!04/){
		$VS_VALUES[15] = int($VS_VALUES[16] * 0.4);
	}


	#生命吸収　クレシダ
	if($PL_CLASS[17] =~ m/!W022/ && $PL_VALUES[25] eq "1"){
		$PL_VALUES[15] = $PL_VALUES[15] + int(500 + rand(4500));
		if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
		print "<font color=\"#f7e957\">生命吸収発動！$PL_VALUES[3]のHPが回復しました。</font><br>\n";
	}

##アビリティシステム
	 	if($AbiSys == 1 && $AbiMukou == 0){
	 	
			#不屈の闘志
			if(($ABI_sA[2] =~ m/!A0071/ || $ABI_sB[2] =~ m/!A0071/ || $ABI_sC[2] =~ m/!A0071/) && $PL_VALUES[25] eq "1" && rand(100) < 10){
				$PL_VALUES[25]=0;
				print "<font color=\"#00FF00\">不屈の闘志発動！$PL_VALUES[3]の戦闘不\能\が回復しました。</font><br>\n";
			}
			if(($VABI_sA[2] =~ m/!A0071/ || $VABI_sB[2] =~ m/!A0071/ || $VABI_sC[2] =~ m/!A0071/) && $VS_VALUES[25] eq "1" && rand(100) < 10){
				$VS_VALUES[25]=0;
				print "<font color=\"#00FF00\">不屈の闘志発動！$VS_VALUES[3]の戦闘不\能\が回復しました。</font><br>\n";
			}

			#瀕死時HP回復
			if(($ABI_sA[2] =~ m/!A0036/ || $ABI_sB[2] =~ m/!A0036/ || $ABI_sC[2] =~ m/!A0036/) && int($PL_VALUES[16]*0.1) > $PL_VALUES[15] && $PL_VALUES[25] ne "1"){
				$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * 0.25);
			}
			if(($VABI_sA[2] =~ m/!A0036/ || $VABI_sB[2] =~ m/!A0036/ || $VABI_sC[2] =~ m/!A0036/) && int($VS_VALUES[16]*0.1) > $VS_VALUES[15] && $VS_VALUES[25] ne "1"){
				$VS_VALUES[15] = $VS_VALUES[15] + int($VS_VALUES[16] * 0.25);
			}

			#戦闘不能時MP回復
#			if(($ABI_sA[2] =~ m/!A0037/ || $ABI_sB[2] =~ m/!A0037/ || $ABI_sC[2] =~ m/!A0037/) && int($PL_VALUES[16]*0.1) > $PL_VALUES[15] && $PL_VALUES[25] ne "1"){
			if(($ABI_sA[2] =~ m/!A0037/ || $ABI_sB[2] =~ m/!A0037/ || $ABI_sC[2] =~ m/!A0037/) && $PL_VALUES[25] eq "1"){
				$PL_VALUES[17] = $PL_VALUES[17] + int($PL_VALUES[18] * 0.20);
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}
				print "<font color=\"#00FF00\">戦闘不\能\時MP回復発動！$PL_VALUES[3]のMPが回復しました。</font><br>\n";
			}
#			if(($VABI_sA[2] =~ m/!A0037/ || $VABI_sB[2] =~ m/!A0037/ || $VABI_sC[2] =~ m/!A0037/) && int($VS_VALUES[16]*0.1) > $VS_VALUES[15] && $VS_VALUES[25] ne "1"){
#				$VS_VALUES[17] = $VS_VALUES[17] + int($VS_VALUES[18] * 0.07);
#			}

	 	}

#39MP 38HP $PL_WA38,$PL_WA39
		$PL_HHPCOUNT=0;
		$VS_HHPCOUNT=0;
		if($PL_WA38 eq ""){$PL_WA38=0;}
		if($PL_WB38 eq ""){$PL_WB38=0;}
		if($PL_WC38 eq ""){$PL_WC38=0;}
		if($PL_WD38 eq ""){$PL_WD38=0;}

		if($VS_WA38 eq ""){$VS_WA38=0;}
		if($VS_WB38 eq ""){$VS_WB38=0;}
		if($VS_WC38 eq ""){$VS_WC38=0;}
		if($VS_WD38 eq ""){$VS_WD38=0;}
		
		$PL_HHPCOUNT=$PL_WA38 + $PL_WB38 + $PL_WC38 + $PL_WD38;
		$VS_HHPCOUNT=$VS_WA38 + $VS_WB38 + $VS_WC38 + $VS_WD38;


		$PL_HMPCOUNT=0;
		$VS_HMPCOUNT=0;

		if($PL_WA39 eq ""){$PL_WA39=0;}
		if($PL_WB39 eq ""){$PL_WB39=0;}
		if($PL_WC39 eq ""){$PL_WC39=0;}
		if($PL_WD39 eq ""){$PL_WD39=0;}

		if($VS_WA39 eq ""){$VS_WA39=0;}
		if($VS_WB39 eq ""){$VS_WB39=0;}
		if($VS_WC39 eq ""){$VS_WC39=0;}
		if($VS_WD39 eq ""){$VS_WD39=0;}

		$PL_HMPCOUNT=$PL_WA39 + $PL_WB39 + $PL_WC39 + $PL_WD39;
		$VS_HMPCOUNT=$VS_WA39 + $VS_WB39 + $VS_WC39 + $VS_WD39;



		$seiseki1 = 0;
		$seiseki2 = 0;
#至福の聖石
	if($PL_VALUES[25] eq "1" && ($PL_sB[7] =~ m/!E0036/ || $PL_sC[7] =~ m/!E0036/ || $PL_sD[7] =~ m/!E0036/)){

		$seiseki2 = 1;
		$PL_VALUES[25] = 0;
		$PL_VALUES[15] = $PL_VALUES[16];
		$PL_VALUES[17] = $PL_VALUES[18];
		print "<font color=\"#00FF00\">至福の聖石発動！$PL_VALUES[3]の戦闘不\能\状態が完全に回復しました。</font><br>\n";

	}
#祝福の聖石
	elsif($PL_VALUES[25] eq "1" && ($PL_sB[7] =~ m/!E0035/ || $PL_sC[7] =~ m/!E0035/ || $PL_sD[7] =~ m/!E0035/)){

		$seiseki1 = 1;
		$PL_VALUES[25] = 0;
		$PL_VALUES[15] = int($PL_VALUES[16]/2);
		print "<font color=\"#00FF00\">祝福の聖石発動！$PL_VALUES[3]の戦闘不\能\状態が回復しました。</font><br>\n";

	}

#カードシステム 自分が無国籍は対象外　対戦相手がNPCは対象外
	if (!$ResultBattle && $VS_VALUES[5] ne "バランスの集い" && $PL_VALUES[5] ne ""){
		@Y_HP=split(/!/,$CL_VALUES[11]);
		@Y_ST=split(/!/,$CL_VALUES[12]);

		$CardHosei=0;
		#対戦相手の熟練度100ごとに+0.1％の補正
		$VS_Jyuku = int($VS_VALUES[24] / 10);
		if($VS_Jyuku >= 100){$VS_Jyuku = 100;}
		$CardHosei = $CardHosei + $VS_Jyuku;
		#対戦相手の最大HP10000ごとに+0.1％の補正
		$CardHosei = $CardHosei + int($VS_VALUES[16] / 1000);
		#対戦相手のLv100ごとに+0.1％の補正
		$CardHosei = $CardHosei + int($VS_VALUES[29] / 10);
		#自身のLv100ごとにも補正
		$CardHosei = $CardHosei + int($PL_VALUES[29] / 10);
#		print "<font color=\"#00FF00\">試験$CardHosei</font><br>\n";
#$CardHosei=0;
		#STRのカード
		if(rand(100000) <= 10 + $CardHosei){
			$Y_ST[0]++;
			if($Y_ST[0] > 200){$Y_ST[0] = 200;print "<font color=\"#00FF00\">STRのカードを取得。要塞の攻撃力がMAXの為、破棄されました。</font><br>\n";}
			else{print "<font color=\"#00FF00\">STRのカードを取得。要塞の攻撃力がアップ。</font><br>\n";}
		#VITのカード
		}elsif(rand(100000) <= 10 + $CardHosei){
			$Y_ST[1]++;
			if($Y_ST[1] > 200){$Y_ST[1] = 200;print "<font color=\"#00FF00\">VITのカードを取得。要塞の攻撃力がMAXの為、破棄されました。</font><br>\n";}
			else{print "<font color=\"#00FF00\">VITのカードを取得。要塞の防御力がアップ。</font><br>\n";}
		#DEXのカード
		}elsif(rand(100000) <= 10 + $CardHosei){
			$Y_ST[2]++;
			if($Y_ST[2] > 200){$Y_ST[2] = 200;print "<font color=\"#00FF00\">DEXのカードを取得。要塞の命中力がMAXの為、破棄されました。</font><br>\n";}
			else{print "<font color=\"#00FF00\">DEXのカードを取得。要塞の命中力がアップ。</font><br>\n";}
		#HPのカード
		}elsif(rand(100000) <= 10 + $CardHosei){
			$Y_HP[1]+=5000;
			if($Y_HP[1] > 600000){$Y_HP[1] = 600000;print "<font color=\"#00FF00\">HPのカードを取得。要塞の最大HPがMAXの為、破棄されました。</font><br>\n";}
			else{print "<font color=\"#00FF00\">HPのカードを取得。要塞の最大HPがアップ。</font><br>\n";}
		#HP回復のカード
#		}elsif(rand(10000) <= 300 + $CardHosei){
		}elsif(rand(10000) <= 900 + $CardHosei){
			$HealCard = 1000 + int(rand(79001));
			$PL_VALUES[15] = $PL_VALUES[15] + $HealCard;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
			print "<font color=\"#00FF00\">HP回復のカードを取得。$PL_VALUES[3]のHPが $HealCard 回復しました。</font><br>\n";
		#MP回復のカード
#		}elsif(rand(10000) <= 200 + $CardHosei){
		}elsif(rand(10000) <= 600 + $CardHosei){
			$HealMPCard = 100 + int(rand(3901));
			$PL_VALUES[17] = $PL_VALUES[17] + $HealMPCard;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}
			print "<font color=\"#00FF00\">MP回復のカードを取得。$PL_VALUES[3]のMPが $HealMPCard 回復しました。</font><br>\n";
		#装備経験値のカード
#		}elsif(rand(10000) <= 300 + $CardHosei){
		}elsif(rand(10000) <= 600 + $CardHosei){
			$PL_In[0] = $PL_In[0] + int(10 + rand(290));
			print "<font color=\"#00FF00\">装備経験値のカードを取得。$PL_VALUES[3]の装備経験値が追加でアップ。</font><br>\n";
#		#褒章のカード
#		}elsif(rand(10000) <= 100 + $CardHosei){
		}elsif(rand(10000) <= 200 + $CardHosei){
			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}

			$HoshouP = 1 + int(rand(100));
			print "<font color=\"#00FF00\">褒章のカードを取得。$PL_VALUES[3]の貢献値が $HoshouP ポイントアップ。</font><br>\n";

			$HC[1] = $HC[1] + $HoshouP;
			$HC[2] = $HC[2] + $HoshouP;
			
			if($HC[1] > 9999){$HC[1] = 9999;}
		
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
#		#熟練度+5　これはなし。クレリック系のチェンジが逆に難しくなるｗ
#		#Riskクリア
#		}elsif(rand(10000) <= 500 + $CardHosei){
		}elsif(rand(10000) <= 1000 + $CardHosei){
			$PL_VALUES[14] = 0;
			print "<font color=\"#00FF00\">Riskのカードを取得。$PL_VALUES[3]のRiskが 大幅に軽減されました。</font><br>\n";

		}
		
#print "<font color=\"#00FF00\">テスト$PL_In[0]</font><br>\n";
		$CL_VALUES[11]="$Y_HP[0]!$Y_HP[1]!$Y_HP[2]";
		$CL_VALUES[12]="$Y_ST[0]!$Y_ST[1]!$Y_ST[2]!$Y_ST[3]";

	}


##アビリティシステム
 	if($AbiSys == 1 && $AbiMukou == 0){

		#リーンカーネイト
		if(($ABI_sA[2] =~ m/!A0069/ || $ABI_sB[2] =~ m/!A0069/ || $ABI_sC[2] =~ m/!A0069/) && $ResultBattle==0 && $VS_VALUES[24] > 1000 && rand(100) < 4){
			if(rand(100) > 50){$VS_VALUES[40]=0;}else{$VS_VALUES[40]=13;}
			print "<font color=\"#00FF00\">リーンカーネイト発動！</font><br>\n";
		}
		if(($VABI_sA[2] =~ m/!A0069/ || $VABI_sB[2] =~ m/!A0069/ || $VABI_sC[2] =~ m/!A0069/) && $ResultBattle==1 && $PL_VALUES[24] > 1000 && rand(100) < 4){
			if(rand(100) > 50){$PL_VALUES[40]=0;}else{$PL_VALUES[40]=13;}
			print "<font color=\"#00FF00\">リーンカーネイト発動！</font><br>\n";
		}

		#死者の指輪
		if(($ABI_sA[2] =~ m/!A0070/ || $ABI_sB[2] =~ m/!A0070/ || $ABI_sC[2] =~ m/!A0070/) && $ResultBattle==0 && $VS_VALUES[24] > 1000 && rand(100) < 4){
			$VS_VALUES[40]=11;
			print "<font color=\"#00FF00\">死者の指輪発動！</font><br>\n";
		}
		if(($VABI_sA[2] =~ m/!A0070/ || $VABI_sB[2] =~ m/!A0070/ || $VABI_sC[2] =~ m/!A0070/) && $ResultBattle==1 && $PL_VALUES[24] > 1000 && rand(100) < 4){
			$PL_VALUES[40]=11;
			print "<font color=\"#00FF00\">死者の指輪発動！</font><br>\n";
		}

	}
#イクソシズム　
	if($PL_CLASS[17] =~ m/!E013/ && ($PL_W[7] =~ m/!8u/ || $PL_sS[7] =~ m/!8u/ || $PL_H[7] =~ m/!8u/)){
		$flg_ik=0;
#		if($VS_CLASS[17] =~ m/!E004/ && rand(100) < 35){
		if($VS_CLASS[17] =~ m/!E004/){
			$VS_VALUES[15]=0;
			$VS_VALUES[25]=1;
			$flg_ik=1;
		}

		if($PL_VALUES[28] ne ''){
	  			if($PL_VALUES[28] eq $CL_VALUES[2]){
				$MOKUHYO4="$CL_VALUES[8]";
			}elsif($PL_VALUES[28] eq $CL_VALUES[3]){
				$MOKUHYO4="$CL_VALUES[9]";
			}elsif($PL_VALUES[28] eq $CL_VALUES[4]){
				$MOKUHYO4="$CL_VALUES[10]";
			}
		}else{
			$MOKUHYO4="$CL_VALUES[6]";
		}
	
		if($MOKUHYO4 eq "バルダー装備を崇める会かも"){$MOKUHYO4="";}

		#プレザンス先生専用戦略時のみ全体化
		if($PL_CLASS[17] =~ m/!E014/ && (($WW_FRAG==1 && $HIZUK_FRAG==1) || (($CL_VALUES[7] > time || $CL_VALUES[37] > time) && $MOKUHYO ne ""))){
			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				@NP_CLASS=split(/\,/,$VCLASS_LIST{"$NP_VALS[4]"});
	
				if($VS_VALUES[5] eq $NP_VALS[5] && ($VS_CLASS[17] =~ m/!E004/ && $NP_CLASS[17] =~ m/!E004/)){
#				if($VS_VALUES[5] eq $NP_VALS[5] && ($NP_CLASS[17] =~ m/!E004/) && $VS_VALUES[28] eq $NP_VALS[28] && rand(100) < 35){
					$NP_VALS[15]=0;
					$NP_VALS[25]=1;
	
					dbmopen (%P,"$DBM_P",0666);
						$P{"$key"}="@NP_VALS";
						$V{"$key"}="@NP_VALS" if !$FORM{'yousai'};
					dbmclose %P;
	
				}
	
			}

			print "<font color=\"#00FF00\">イクソ\シズム発動！$VS_VALUES[3]の所属する国の全てのアンデッドクラスプレイヤーに浄化攻撃！</font><br>\n";
		}else{
			if($flg_ik eq "1"){
				print "<font color=\"#00FF00\">イクソ\シズム発動！$VS_VALUES[3]に浄化攻撃！</font><br>\n";
			}
		}

	}


#			&DBM_INPORT(P);
#			foreach $key (keys %P){
#				@NP_VALS = split(/\s/,$P{$key});
#				@NP_CLASS=split(/\,/,$VCLASS_LIST{"$NP_VALS[4]"});
	
#				if($VS_VALUES[5] eq $NP_VALS[5] && ($VS_CLASS[17] =~ m/!E004/ && $NP_CLASS[17] =~ m/!E004/)){
#				if($VS_VALUES[5] eq $NP_VALS[5] && ($NP_CLASS[17] =~ m/!E004/) && $VS_VALUES[28] eq $NP_VALS[28] && rand(100) < 35){
#					$NP_VALS[55]="";
#					$NP_VALS[56]="";
#					$NP_VALS[57]="";
#					$NP_VALS[58]="";
#					$NP_VALS[59]="";
#					$NP_VALS[60]="";
	
#					&LOCK;
#					dbmopen (%P,"$DBM_P",0666);
#						$P{"$key"}="@NP_VALS";
#						$V{"$key"}="@NP_VALS" if !$FORM{'yousai'};
#					dbmclose %P;
#					&UNLOCK;
	
#				}
	
#			}

#お菓子セット	魔法＆盾の問題があるので、こいつに限り特殊処理
	$okasi = 0;
	if($PL_WDu[0] eq "シュガーケーン" || $PL_sB[0] eq "シュガーケーン" || $PL_sC[0] eq "シュガーケーン" || $PL_sD[0] eq "シュガーケーン"){

		if($PL_WN eq "4caaaa" || $PL_WB eq "4caaaa" || $PL_WC eq "4caaaa" || $PL_WD eq "4caaaa"){

			$okasi = 1;

			if($PL_WDu[0] eq "キャンディヘルム" || $PL_sB[0] eq "キャンディヘルム" || $PL_sC[0] eq "キャンディヘルム" || $PL_sD[0] eq "キャンディヘルム"){

				$okasi = 2;

				if($PL_WDu[0] eq "砂糖菓子のヨロイ" || $PL_sB[0] eq "砂糖菓子のヨロイ" || $PL_sC[0] eq "砂糖菓子のヨロイ" || $PL_sD[0] eq "砂糖菓子のヨロイ"){
	
					$okasi = 3;
	
				}

			}

			if($okasi == 1){

				print "<font color=\"#f7e957\">お菓子セットの効果発動！$PL_VALUES[3]のHPが回復しました。</font><br>\n";

				if ($PL_VALUES[25] eq "0"){
					$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * 0.15);
					if ($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
				}

			}elsif($okasi == 2){

				print "<font color=\"#f7e957\">お菓子セットの効果発動！$PL_VALUES[3]のHPが回復しました。</font><br>\n";

				if ($PL_VALUES[25] eq "0"){
					$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * 0.2);
					if ($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
#					$PL_VALUES[17] = $PL_VALUES[17] + int($PL_VALUES[18] * 0.01);
#					if ($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}
				}

			}elsif($okasi == 3){

				print "<font color=\"#f7e957\">お菓子セットの効果発動！$PL_VALUES[3]のHPとMPが回復しました。</font><br>\n";

				if ($PL_VALUES[25] eq "0"){
					$PL_VALUES[15] = $PL_VALUES[15] + int($PL_VALUES[16] * 0.25);
					if ($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}
					$PL_VALUES[17] = $PL_VALUES[17] + int($PL_VALUES[18] * 0.01);
					if ($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}
				}

			}

		}

	}


#シャングリラ跡
#ゼテギネアのリセット　ガリシア国にいるゼテギネア民を無国籍に
	if($PL_W[7] =~ m/!9998/){

		&DBM_INPORT(P);
		foreach $key (keys %P){
			@NP_VALS = split(/\s/,$P{$key});

			#$NP_VALS[5] 所属国

			while (($NC_Name,$NC_Value) =each %C) {

				if($NC_Name eq $NP_VALS[5]){

					@NC_VALUES = split(/\s/,$NC_Value);
					if ($NC_VALUES[39] ne $NP_VALS[39]){

						$NP_VALS[5] = "";$NP_VALS[28]='';$NP_VALS[0]=$NP_VALS[6]=0;
#						if($NP_VALS[39] eq "1"){$NP_VALS[39] = 2;}else{$NP_VALS[39] = 1;}
						dbmopen (%P,"$DBM_P",0666);
							$P{"$key"}="@NP_VALS";
						dbmclose %P;
	
					}

				}
	
			}

		}
		print "<font color=\"#f7e957\">？？？</font><br>\n";

	}

#貢献値加算
	if($NewHoushoFlg == 1 && $PL_VALUES[25] ne "1" && $PL_VALUES[5] ne "" && $VS_VALUES[25] eq "1"){

		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}

		$HC[1] = $HC[1] + 1;
		$HC[2] = $HC[2] + 1;
		#総帥の場合、貢献点+1
		if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 1;}

		#OVERKILL	貢献値+10　総帥は貢献値+20
		if($PL_DAM >= 80000){
			$HC[1] = $HC[1] + 10;
			$HC[2] = $HC[2] + 10;
		
			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 10;$HC[2] = $HC[2] + 10;}
			print "<font color=\"#f7e957\"><b>OVERKILL！！</b></font><br>\n";
		}

		#強者必衰　対戦相手の最大HPで貢献値ボーナス
		if($VS_VALUES[16] >= 70000){
			$HC[1] = $HC[1] + 5;
			$HC[2] = $HC[2] + 5;
		
			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 5;$HC[2] = $HC[2] + 5;print "<font color=\"#f7e957\"><b>貢献値加算ボーナス･･･+10</b></font><br>\n";}else{print "<font color=\"#f7e957\"><b>貢献値加算ボーナス･･･+5</b></font><br>\n";}
			
		}elsif($VS_VALUES[16] >= 50000){
			$HC[1] = $HC[1] + 3;
			$HC[2] = $HC[2] + 3;
		
			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 3;$HC[2] = $HC[2] + 3;print "<font color=\"#f7e957\"><b>貢献値加算ボーナス･･･+6</b></font><br>\n";}else{print "<font color=\"#f7e957\"><b>貢献値加算ボーナス･･･+3</b></font><br>\n";}

		}elsif($VS_VALUES[16] >= 30000){
			$HC[1] = $HC[1] + 1;
			$HC[2] = $HC[2] + 1;
		
			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 1;print "<font color=\"#f7e957\"><b>貢献値加算ボーナス･･･+2</b></font><br>\n";}else{print "<font color=\"#f7e957\"><b>貢献値加算ボーナス･･･+1</b></font><br>\n";}

		}

		
		if($HC[1] > 9999){$HC[1] = 9999;}
		
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

	}

#貢献値改正
	if($PL_W[7] =~ m/!9999/){
		
		$KoukenP = 2 * int(rand(120)+30);
		&DBM_INPORT(P);
		foreach $key (keys %P){
			@NP_VALS = split(/\s/,$P{$key});

			#$NP_VALS[5] 所属国
#			$TarCon = "機甲界ガリシアン";
$TarCon="sadasdasdasd";
			if($NP_VALS[5] eq $TarCon){

#				&ERROR("$NP_VALS[5]ああ$NP_VALS[3]");
				@HC=split(/!/,$NP_VALS[50]);
				if($HC[0] ne $HoushoKey){$NP_VALS[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

#				$KoukenP = (1 + $VC_VALUES[13]) * int(rand(120)+30);
				$HC[1] = $HC[1] + $KoukenP;
				if($HC[1] > 3000){$HC[1] = 3000;}
				$HC[2] = $HC[2] + $KoukenP;
				
				$NP_VALS[50] = "$HC[0]!$HC[1]!$HC[2]!";
			
#				&ERROR("$NP_VALS[5]ああ$NP_VALS[3]と$NP_VALS[50]");
				dbmopen (%P,"$DBM_P",0666);
					$P{"$key"}="@NP_VALS";
				dbmclose %P;
			
			}

		}
		print "<font color=\"#f7e957\">？？？？$KoukenP</font><br>\n";

	}
#STD

	if ($PLURAMI){print "<font color=#4aa1af>$PL_VALUES[3]が恨みの一撃！$VS_VALUES[3]を道連れにした！！</font><br>\n";}
	if ($PLCONFORM){print "<font color=#ff4d4d>アシェルム！！相手のエレメントを使用者のエレメントに写した！！</font><br>\n";}
	if ($PLTRANS){
		print "<font color=#ff4d4d>トランスファー！</font><br>\n";
		require "boserifu.data";
		my$sl=@teniseki;
		my$sw=@teniseki[int(rand($sl))];			
		print "$FORM{'pname'}$sw<br>\n";
	}
	if ($VSMIGAWARI){
		print "<font color=#ffffbb>リバイバル！！命を落とした者の魂を即座に呼び戻す・・・</font><br>\n";
	}

	$hatustd=0;

	$STDN=20;

	if($VS_VALUES[5] eq "バルダー装備を崇める会" || $VS_VALUES[5] eq "メルト屋愛好会"){$STDN=60;}

	if($VS_W[7] =~ m/!6u/){$STDN+=$Vswl;}

#20190322 ダウン攻撃凍結
	$STDN = 0;
	

# && $COOKIE{'pass'} ne $MASTERPASS
	if ($PL_VALUES[29] > 102 && $VS_VALUES[15] > 0 && $PL_CLASS[17] !~ m/E009/ && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/ && $PL_sD[7] !~ m/!4b/){
		if($VS_W[7] =~ m/!22/ && $PL_VALUES[19] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>！！敵兵の$STATUS_NAME[0]ダウン攻撃！！<br>$PL_VALUES[3]は攻撃力低下</font><br>\n";
			$PL_VALUES[19]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[67]++;}$R_VALUES[126]++;
		}
		if($VS_W[7] =~ m/!23/ && $PL_VALUES[20] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>！！敵兵の$STATUS_NAME[1]ダウン攻撃！！<br>$PL_VALUES[3]は防御力低下</font><br>\n";
			$PL_VALUES[20]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[68]++;}$R_VALUES[127]++;
		}
		if($VS_W[7] =~ m/!24/ && $PL_VALUES[21] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>！！敵兵の$STATUS_NAME[2]ダウン攻撃！！<br>$PL_VALUES[3]は回避力低下</font><br>\n";
			$PL_VALUES[21]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[69]++;}$R_VALUES[128]++;
		}
		if($VS_W[7] =~ m/!25/ && $PL_VALUES[22] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>！！敵兵の$STATUS_NAME[3]ダウン攻撃！！<br>$PL_VALUES[3]は命中力低下</font><br>\n";
			$PL_VALUES[22]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[70]++;}$R_VALUES[129]++;
		}
	}

	if ($PL_VALUES[29] > 102 && $VS_W[7] =~ m/!2j/ && $PL_VALUES[16]==80000){
		if(rand(100) > 98){print "<font color=#8000ff>！！敵兵のHPダウン攻撃！！<br>$PL_VALUES[3]は最大HP低下</font><br>\n";
		$PL_VALUES[16]=int($PL_VALUES[16]*0.99);$PL_VALUES[29]=$PL_VALUES[29]-3;$PL_VALUES[30]=int($PL_VALUES[30]/2);$R_VALUES[130]++;
		}$R_VALUES[131]++;
	}
	if($hatustd == 1){print "<font color=#8000ff>レベル低下</font><br>\n";
		$PL_VALUES[30]=int($PL_VALUES[30]/3);
		if($PL_VALUES[29] < 100){$PL_VALUES[29]=100;}
	}

	if ($PL_CRITICAL && $Pl_Times){
		print "<font color=#ff0080>！！クリティカルヒット！！</font><br>\n";
	}

	&vabattle7;

	&vabattle8;

#石を消す
	if($seiseki1 == 1){
		if($PL_sB[7] =~ m/!E0035/){$PL_VALUES[10] ="";}
		elsif($PL_sC[7] =~ m/!E0035/){$PL_VALUES[11] ="";}
		elsif($PL_sD[7] =~ m/!E0035/){$PL_VALUES[38] ="";}	
	}elsif($seiseki2 == 1){
		if($PL_sB[7] =~ m/!E0036/){$PL_VALUES[10] ="";}
		elsif($PL_sC[7] =~ m/!E0036/){$PL_VALUES[11] ="";}
		elsif($PL_sD[7] =~ m/!E0036/){$PL_VALUES[38] ="";}	
	}

#武器獲得数
	if($buki == 1){
		$R_VALUES[7]++;
		my@kakutoku=("18a","19a","1aa","1ba","1ca","1da","1ea","1fa","1ga","1ha","1ia","2hm","2ch","2ci","2cj","2ck","2cl","2cm","4ba","4ca","4da","4ga","4gb","4gc","4gd","4ge","4gf","4gg","4gh","4gi","4ha","4hb","4hc","4hd","4he","4hf","4hg","4hi","4ia","6aa","6ba","6ca","6da","6ea","6fa","6ga","71a","71b","71c","71d","1oa","1od","1oe","1of","4ea","4fa","2hn");
			for($i=0; $i < @kakutoku; $i++){
				if($kakutoku[$i] eq "$gw"){
					$ban=$i+159;last;
				}
			}
		$R_VALUES[$ban]++;

		#ランキング用 アイテム獲得数　0はアイテム獲得　1はMVP 2は図鑑登録 3は不正カウント 4は剣道具監視
		@RC=split(/!/,$PL_VALUES[47]);
		if($RC[0] eq ""){$RC[0] = 0;}
		$RC[0] = $RC[0] + 1;

		#剣道具シリーズは、不正防止用に監視する
		if ($ItemChk eq "1ha" || $ItemChk eq "4da" || $ItemChk eq "0011a" || $ItemChk eq "0017a"){
			if($RC[4] eq ""){$RC[4] = 0;}
			$RC[4] = $RC[4] + 1;
		}

		$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";

	}

	#テレポート系発動時は消去
	if ($PL_TE eq "1"){$PL_VALUES[$FORM{"sentaku"}] = "";}

	&vabattle9;


}

1;

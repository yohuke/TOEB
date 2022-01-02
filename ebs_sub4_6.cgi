sub BATTLE6{
	require './vabattle.pl';
	&vabattleheader;

	&LOCK;
		&DBM_CONVERT('P',"$FORM{pname}",'VS',"$FORM{vsname}");
		&DBM_CONVERT('C',"$PL_VALUES[5]",'VC',"$VS_VALUES[5]");

	&vabattle1;

	&ERROR('Repair','直前に戦闘の割り込みが入りました。戦闘を中止します。') if ($PL_VALUES[25] || $VS_VALUES[25]);

#	local($PL_WN,$PL_WLV) = split(/!/,$PL_VALUES[9]);local($PL_WB,$PL_LVB) = split(/!/,$PL_VALUES[10]);local($PL_WC,$PL_LVC) = split(/!/,$PL_VALUES[11]); local($PL_WD,$PL_LVD) = split(/!/,$PL_VALUES[38]);
#	local($VS_WN,$VS_WLV) = split(/!/,$VS_VALUES[9]);local($VS_WB,$VS_LVB) = split(/!/,$VS_VALUES[10]);local($VS_WC,$VS_LVC) = split(/!/,$VS_VALUES[11]); local($VS_WD,$VS_LVD) = split(/!/,$VS_VALUES[38]);

	local($PL_WN,$PL_WLV,$PL_WAEnt,$PL_WA03,$PL_WA04,$PL_WA05,$PL_WA06,$PL_WA07,$PL_WA08,$PL_WA09,$PL_WA10,$PL_WA11,$PL_WA12,$PL_WA13,$PL_WA14,$PL_WA15,$PL_WA16,$PL_WA17,$PL_WA18,$PL_WA19,$PL_WA20,$PL_WA21,$PL_WA22,$PL_WA23,$PL_WA24,$PL_WA25,$PL_WA26,$PL_WA27,$PL_WA28,$PL_WA29,$PL_WA30,$PL_WA31,$PL_WA32,$PL_WA33,$PL_WA34,$PL_WA35,$PL_WA36,$PL_WA37,$PL_WA38,$PL_WA39,$PL_WA40,$PL_WA41,$PL_WA42) = split(/!/,$PL_VALUES[9]);
	local($PL_WB,$PL_LVB,$PL_WBEnt,$PL_WB03,$PL_WB04,$PL_WB05,$PL_WB06,$PL_WB07,$PL_WB08,$PL_WB09,$PL_WB10,$PL_WB11,$PL_WB12,$PL_WB13,$PL_WB14,$PL_WB15,$PL_WB16,$PL_WB17,$PL_WB18,$PL_WB19,$PL_WB20,$PL_WB21,$PL_WB22,$PL_WB23,$PL_WB24,$PL_WB25,$PL_WB26,$PL_WB27,$PL_WB28,$PL_WB29,$PL_WB30,$PL_WB31,$PL_WB32,$PL_WB33,$PL_WB34,$PL_WB35,$PL_WB36,$PL_WB37,$PL_WB38,$PL_WB39,$PL_WB40,$PL_WB41,$PL_WB42) = split(/!/,$PL_VALUES[10]);
	local($PL_WC,$PL_LVC,$PL_WCEnt,$PL_WC03,$PL_WC04,$PL_WC05,$PL_WC06,$PL_WC07,$PL_WC08,$PL_WC09,$PL_WC10,$PL_WC11,$PL_WC12,$PL_WC13,$PL_WC14,$PL_WC15,$PL_WC16,$PL_WC17,$PL_WC18,$PL_WC19,$PL_WC20,$PL_WC21,$PL_WC22,$PL_WC23,$PL_WC24,$PL_WC25,$PL_WC26,$PL_WC27,$PL_WC28,$PL_WC29,$PL_WC30,$PL_WC31,$PL_WC32,$PL_WC33,$PL_WC34,$PL_WC35,$PL_WC36,$PL_WC37,$PL_WC38,$PL_WC39,$PL_WC40,$PL_WC41,$PL_WC42) = split(/!/,$PL_VALUES[11]);
	local($PL_WD,$PL_LVD,$PL_WDEnt,$PL_WD03,$PL_WD04,$PL_WD05,$PL_WD06,$PL_WD07,$PL_WD08,$PL_WD09,$PL_WD10,$PL_WD11,$PL_WD12,$PL_WD13,$PL_WD14,$PL_WD15,$PL_WD16,$PL_WD17,$PL_WD18,$PL_WD19,$PL_WD20,$PL_WD21,$PL_WD22,$PL_WD23,$PL_WD24,$PL_WD25,$PL_WD26,$PL_WD27,$PL_WD28,$PL_WD29,$PL_WD30,$PL_WD31,$PL_WD32,$PL_WD33,$PL_WD34,$PL_WD35,$PL_WD36,$PL_WD37,$PL_WD38,$PL_WD39,$PL_WD40,$PL_WD41,$PL_WD42) = split(/!/,$PL_VALUES[38]);
	
	local($VS_WN,$VS_WLV,$VS_WAEnt,$VS_WA03,$VS_WA04,$VS_WA05,$VS_WA06,$VS_WA07,$VS_WA08,$VS_WA09,$VS_WA10,$VS_WA11,$VS_WA12,$VS_WA13,$VS_WA14,$VS_WA15,$VS_WA16,$VS_WA17,$VS_WA18,$VS_WA19,$VS_WA20,$VS_WA21,$VS_WA22,$VS_WA23,$VS_WA24,$VS_WA25,$VS_WA26,$VS_WA27,$VS_WA28,$VS_WA29,$VS_WA30,$VS_WA31,$VS_WA32,$VS_WA33,$VS_WA34,$VS_WA35,$VS_WA36,$VS_WA37,$VS_WA38,$VS_WA39,$VS_WA40,$VS_WA41,$VS_WA42) = split(/!/,$VS_VALUES[9]);
	local($VS_WB,$VS_LVB,$VS_WBEnt,$VS_WB03,$VS_WB04,$VS_WB05,$VS_WB06,$VS_WB07,$VS_WB08,$VS_WB09,$VS_WB10,$VS_WB11,$VS_WB12,$VS_WB13,$VS_WB14,$VS_WB15,$VS_WB16,$VS_WB17,$VS_WB18,$VS_WB19,$VS_WB20,$VS_WB21,$VS_WB22,$VS_WB23,$VS_WB24,$VS_WB25,$VS_WB26,$VS_WB27,$VS_WB28,$VS_WB29,$VS_WB30,$VS_WB31,$VS_WB32,$VS_WB33,$VS_WB34,$VS_WB35,$VS_WB36,$VS_WB37,$VS_WB38,$VS_WB39,$VS_WB40,$VS_WB41,$VS_WB42) = split(/!/,$VS_VALUES[10]);
	local($VS_WC,$VS_LVC,$VS_WCEnt,$VS_WC03,$VS_WC04,$VS_WC05,$VS_WC06,$VS_WC07,$VS_WC08,$VS_WC09,$VS_WC10,$VS_WC11,$VS_WC12,$VS_WC13,$VS_WC14,$VS_WC15,$VS_WC16,$VS_WC17,$VS_WC18,$VS_WC19,$VS_WC20,$VS_WC21,$VS_WC22,$VS_WC23,$VS_WC24,$VS_WC25,$VS_WC26,$VS_WC27,$VS_WC28,$VS_WC29,$VS_WC30,$VS_WC31,$VS_WC32,$VS_WC33,$VS_WC34,$VS_WC35,$VS_WC36,$VS_WC37,$VS_WC38,$VS_WC39,$VS_WC40,$VS_WC41,$VS_WC42) = split(/!/,$VS_VALUES[11]);
	local($VS_WD,$VS_LVD,$VS_WDEnt,$VS_WD03,$VS_WD04,$VS_WD05,$VS_WD06,$VS_WD07,$VS_WD08,$VS_WD09,$VS_WD10,$VS_WD11,$VS_WD12,$VS_WD13,$VS_WD14,$VS_WD15,$VS_WD16,$VS_WD17,$VS_WD18,$VS_WD19,$VS_WD20,$VS_WD21,$VS_WD22,$VS_WD23,$VS_WD24,$VS_WD25,$VS_WD26,$VS_WD27,$VS_WD28,$VS_WD29,$VS_WD30,$VS_WD31,$VS_WD32,$VS_WD33,$VS_WD34,$VS_WD35,$VS_WD36,$VS_WD37,$VS_WD38,$VS_WD39,$VS_WD40,$VS_WD41,$VS_WD42) = split(/!/,$VS_VALUES[38]);

#	if($FORM{"sentaku"} =~ m/41|42|43/){
		local($PL_WS,$PL_LVS,$PL_WSEnt) = split(/!/,$PL_VALUES[$FORM{"sentaku"}]);
		local($PL_WH,$PL_LVH,$PL_WHEnt) = split(/!/,$PL_VALUES[$FORM{"Hosentaku"}]);
#	}

#ヒート、メルト用
#	local($PL_WSS1,$PL_LVSS1) = split(/!/,$PL_VALUES[41]);
#	local($PL_WSS2,$PL_LVSS2) = split(/!/,$PL_VALUES[42]);
#	local($PL_WSS3,$PL_LVSS3) = split(/!/,$PL_VALUES[43]);
#	local($VS_WSS1,$VS_LVSS1) = split(/!/,$VS_VALUES[41]);
#	local($VS_WSS2,$VS_LVSS2) = split(/!/,$VS_VALUES[42]);
#	local($VS_WSS3,$VS_LVSS3) = split(/!/,$VS_VALUES[43]);

	local($PL_WSS1,$PL_LVSS1,$PL_WSS1Ent) = split(/!/,$PL_VALUES[41]);
	local($PL_WSS2,$PL_LVSS2,$PL_WSS2Ent) = split(/!/,$PL_VALUES[42]);
	local($PL_WSS3,$PL_LVSS3,$PL_WSS3Ent) = split(/!/,$PL_VALUES[43]);
	local($VS_WSS1,$VS_LVSS1,$VS_WSS1Ent) = split(/!/,$VS_VALUES[41]);
	local($VS_WSS2,$VS_LVSS2,$VS_WSS2Ent) = split(/!/,$VS_VALUES[42]);
	local($VS_WSS3,$VS_LVSS3,$VS_WSS3Ent) = split(/!/,$VS_VALUES[43]);

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
#		&ERROR("$VS_LVSああ");

#	if($VS_VALUES[45] eq ""){
#		$VS_LVS = split(/!/,$VS_VALUES[44]);
#	}

	if($VS_VALUES[45] eq "" || $VS_VALUES[45] eq "1" || $VS_VALUES[45] eq "0" || $VS_VALUES[45] eq "9"){
		$VS_WS="";
		$VS_LVS="";
		$VS_LVSET = 9;

	}

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

	$PL_CRIP=0;
	if($PL_WA32 eq ""){$PL_WA32=0;}
	$PL_CRIP = $PL_CRIP + $PL_WA32;

#	if(int($PL_VALUES[18]/$PL_W[4]/10-10+$PL_VALUES[14]) > rand($PL_W[4])){
	if(int($PL_VALUES[18]/$PL_W[4]/10-10+$PL_VALUES[14]+$CriHosei) > rand($PL_W[4])){
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

	$Pl_AtPoint=0 if $Pl_AtPoint < 0;
	$Vs_AtPoint=0 if $Vs_AtPoint < 0;

	$dmgStyl="style=\"font-size:21px;color:#9acd32;\"";
	$chaStyl="style=\"font-size:12px;color:#dc143c;\"";
	$PlsumDmg="<b $dmgStyl>$PL_W[3]</b> <b $chaStyl>Attack</b> <b $dmgStyl>$Pl_Times</b> <b $chaStyl>hit</b> 
		<b $dmgStyl>$Pl_AtPoint</b><b $chaStyl> Damage</b>" if $Pl_Times > 0;
	$PlsumDmg='<font color=#6a5acd>Miss</font>' if $Pl_Times == 0;
	$VssumDmg="<b $dmgStyl>$VS_W[3]</b> <b $chaStyl>Attack</b> <b $dmgStyl>$Vs_Times</b> <b $chaStyl>hit</b> 
		<b $dmgStyl>$Vs_AtPoint</b><b $chaStyl> Damage</b>" if $Vs_Times > 0;
	$VssumDmg='<font color=#6a5acd>Miss</font>' if $Vs_Times == 0;

	$Pl_BfrHP=$PL_VALUES[15];
	$Vs_AtPoint=$PL_VALUES[15] if $PL_VALUES[15] < $Vs_AtPoint;
	$PL_VALUES[15]=$PL_VALUES[15]-$Vs_AtPoint;
	$Pl_width_per=$PL_VALUES[16]/150;
	$Pl_width_hp=int($PL_VALUES[15]/$Pl_width_per);
	$Pl_width_zen=int(($PL_VALUES[16]-$Pl_BfrHP)/$Pl_width_per);
	$Pl_width_dmg=int($Vs_AtPoint/$Pl_width_per);
	$PL_HPTAG="<img src=\"$IMG_FOLDER1/hp.gif\" hspace=0 height=7 width=$Pl_width_hp>" if $Pl_width_hp;
	$PL_HPTAG.="<img src=\"$IMG_FOLDER1/dmg.gif\" hspace=0 height=7 width=$Pl_width_dmg>" if $Pl_width_dmg;
	$PL_HPTAG.="<img src=\"$IMG_FOLDER1/zen.gif\" hspace=0 height=7 width=$Pl_width_zen>" if $Pl_width_zen;
	$Vs_BfrHP=$VS_VALUES[15];
	$Pl_AtPoint=$VS_VALUES[15] if $VS_VALUES[15] < $Pl_AtPoint;
	$VS_VALUES[15]=$VS_VALUES[15]-$Pl_AtPoint;
	$Vs_width_per=$VS_VALUES[16]/150;
	$Vs_width_hp=int($VS_VALUES[15]/$Vs_width_per);
	$Vs_width_zen=int(($VS_VALUES[16]-$Vs_BfrHP)/$Vs_width_per);
	$Vs_width_dmg=int($Pl_AtPoint/$Vs_width_per);
	$VS_HPTAG="<img src=\"$IMG_FOLDER1/hp.gif\" hspace=0 height=7 width=$Vs_width_hp>" if $Vs_width_hp;
	$VS_HPTAG.="<img src=\"$IMG_FOLDER1/dmg.gif\" hspace=0 height=7 width=$Vs_width_dmg>" if $Vs_width_dmg;
	$VS_HPTAG.="<img src=\"$IMG_FOLDER1/zen.gif\" hspace=0 height=7 width=$Vs_width_zen>" if $Vs_width_zen;

	&vabattle6_1;

	&vabattle6_2;

	&MESSAGE('m','PL','VS');
	&MESSAGE('m','VS','PL');

	if ($PL_CRITICAL && $Pl_Times){
		print "<font color=#ff0080>！！クリティカルヒット！！</font><br>\n";
	}

	&vabattle7;

	if ($FORM{'b_mode'} eq '亡命'){
		if($B_Com eq '成功'){
			require "boserifu.data";
			my$sl=@disaffectionserifu;
			my$sw=@disaffectionserifu[int(rand($sl))];
			print "<font color=#ff0080>DISAFFECTION！！</font><br>\n";
			print "$FORM{'pname'}$sw<br>\n";
			$R_VALUES[31]++;
		}else{
			require "boserifu.data";
			my$sl=@cautionserifu;
			my$sw=@cautionserifu[int(rand($sl))];
			print "<font color=#ff0080>CAUTION！</font><br>\n";
			print "$FORM{'pname'}$sw<br>\n";
			$R_VALUES[32]++;
		}
		print "$FORM{'b_mode'}$B_Com<br>\n";
	}

	if ($FORM{'b_mode'} eq '内乱'){
		if($B_Com eq '成功'){
			my@C=%C;
			my$C=@C/2;

			if($VS_VALUES[6] == 1 && $C < $COUNTRY_MAX){
				$AGAKI_FLAG=1;
				$PL_VALUES[37]++;
			}
			print "$FORM{'vsname'}「ほんのわずかでいいから、気を使って欲しいな・・・。<br>\n";
			$R_VALUES[33]++;
		}else{
			$AGAKI_FLAG=2;$R_VALUES[34]++;
		}
		if($AGAKI_FLAG==1){
			if($PL_VALUES[37] < 2){
				print "<font color=#8000ff>むー・・・</font><br>\n";
			}elsif($PL_VALUES[37]==2){
				print "<font color=#8000ff>建国枠、空いてませんでしたか？・・・警告。</font><br>\n";
			}elsif($PL_VALUES[37]==3){
				$PL_VALUES[18]=0;
				print "<font color=#8000ff>game over</font><br>\n";
			}
		}elsif($AGAKI_FLAG==2){
			print "$FORM{'vsname'}「おいおい、いいのかい？そんなわけないよなぁ？マジな話？<br>\n";
		}
		print "$FORM{'b_mode'}$B_Com<br>\n";
	}

	&vabattle8;

	&vabattle9;
}

1;

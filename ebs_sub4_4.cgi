sub BATTLE4{
	require './vabattle.pl';
	&vabattleheader;

	&LOCK;
		&DBM_CONVERT('P',"$FORM{pname}");
		&DBM_CONVERT('C',"$PL_VALUES[5]",'VC',"$FORM{'vsname'}");

	if(!$PL_VALUES[28]){
		$M_AITE="$CL_VALUES[6]";
	}elsif($PL_VALUES[28] eq "$CL_VALUES[2]" && $CL_VALUES[2]){
		$M_AITE="$CL_VALUES[8]";
	}elsif($PL_VALUES[28] eq "$CL_VALUES[3]" && $CL_VALUES[3]){
		$M_AITE="$CL_VALUES[9]";
	}elsif($PL_VALUES[28] eq "$CL_VALUES[4]" && $CL_VALUES[4]){
		$M_AITE="$CL_VALUES[10]";
	}
#	&ERROR('�U���悪�Ⴂ�܂��B') if $M_AITE ne "$FORM{'vsname'}";
	&ERROR('�U���悪�Ⴂ�܂��B') if ($M_AITE ne "$FORM{'vsname'}" && $WW_FRAG==0);
#	&ERROR('���������؂�Ă��܂��B') if time > $CL_VALUES[7];
	&ERROR('���������؂�Ă��܂��B') if (time > $CL_VALUES[7] && $WW_FRAG==0);
	&ERROR('���ɖŖS���Ă��܂��B') if !@VC_VALUES;

	&ERROR("���E��풆�͖����Ђ̃v���C���[�͑����̗v�ǂƐ퓬���邱�Ƃ͏o���܂���B") if (!$PL_VALUES[5] && $VS_VALUES[5] && $WW_FRAG==0 && $HIZUK_FRAG==0);

##�C���|�[�g
	&DBM_INPORT(P);&DBM_INPORT(C);
##�����w�����x���ǂݍ��݁E�������ǂݍ���
	while (my($key,$val) = each %P){
		@VALS = split(/\s/,$val);
			if($VALS[5] eq "$M_AITE"){
				if($VALS[6]==1){$SOUSUISIKI=$VALS[32];}
				if($VALS[15] > 40000){$SINMIN++;}
			}
	}
##�����w�����f���A101�ȏ�Ȃ�100�ɂ���
	$SOUSUISIKI=100 if $SOUSUISIKI > 100;
	$VSMETUCHECK=$VC_VALUES[13] if $VC_VALUES[13];
	$VSMETUCHECK=50 if $VSMETUCHECK > 50;
	$SOUSUISIKI=int($SOUSUISIKI/4)+$VSMETUCHECK;
##�v�ǔ\��
	@Y_HP=split(/!/,$VC_VALUES[11]);
	@Y_ST=split(/!/,$VC_VALUES[12]);
	$Y_STR=$Y_ST[0];$Y_VIT=$Y_ST[1];$Y_DEX=$Y_ST[2];
	$Y_ST[0]+=(50+$SOUSUISIKI);$Y_ST[1]+=(50+$SOUSUISIKI);$Y_ST[2]+=(60+$SOUSUISIKI);
	$YSTR=$Y_ST[0];$YSTR*=6;
	@VS_VALUES=("300","$Y_HP[2]!0","�v��","$Y_ST[3]","AL","$FORM{'vsname'}","99","","0","zzzz","zzzz","zzzz","6","$VC_VALUES[0]","0","$Y_HP[0]","$Y_HP[1]","9999","9999","$YSTR","$Y_ST[1]","-50","$Y_ST[2]","99","999","0","$DATE","1000","0","99","0");
	$world=1 if $VC_VALUES[38] > time;

#�������ɂ�鋭���{�[�i�X�@����1�l�ɂ��A�U�E�h�E��+1
	$MyCountryCount = 0;
#	while (my($key,$val) = each %P){
#		@VALS = split(/\s/,$val);
#		if($PL_VALUES[5] eq $VALS[5]){
#			$MyCountryCount = $MyCountryCount + 1;
#		}
#	}

#	$Y_STR=$Y_STR + $MyCountryCount;
#	$Y_VIT=$Y_VIT + int($MyCountryCount * 0.5);
#	$Y_DEX=$Y_DEX + $MyCountryCount;

#20180528�@�U���͒���
	$Y_STR = int($Y_STR * 0.6);

#�����␳�̒ǉ�����
	$YousaiKaihi = 0;
	$YousaiKaihi = int($Y_DEX / 4);
	
	if($YousaiKaihi >= 10){$YousaiKaihi = 10;}

	&vabattle1;

	&ERROR('Repair','���O�ɐ퓬�̊��荞�݂�����܂����B�퓬�𒆎~���܂��B') if ($PL_VALUES[25] || $VS_VALUES[25]);

#�v�Ǖ���ύX
	if($VS_VALUES[47] eq "0"){$VS_VALUES[9] = "zzzza";}
	elsif($VS_VALUES[47] eq "1"){$VS_VALUES[9] = "zzzzb";}
	elsif($VS_VALUES[47] eq "2"){$VS_VALUES[9] = "zzzzc";}
	elsif($VS_VALUES[47] eq "3"){$VS_VALUES[9] = "zzzzd";}
	elsif($VS_VALUES[47] eq "4"){$VS_VALUES[9] = "zzzze";}
	elsif($VS_VALUES[47] eq "5"){$VS_VALUES[9] = "zzzzf";}
	else{$VS_VALUES[9] = "zzzz";}

#	local($PL_WN,$PL_WLV) = split(/!/,$PL_VALUES[9]); local($PL_WB,$PL_LVB) = split(/!/,$PL_VALUES[10]); local($PL_WC,$PL_LVC) = split(/!/,$PL_VALUES[11]); local($PL_WD,$PL_LVD) = split(/!/,$PL_VALUES[38]);
#	local($VS_WN,$VS_WLV) = split(/!/,$VS_VALUES[9]); local($VS_WB,$VS_LVB) = split(/!/,$VS_VALUES[10]); local($VS_WC,$VS_LVC) = split(/!/,$VS_VALUES[11]); local($VS_WD,$VS_LVD) = split(/!/,$VS_VALUES[38]);

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
	local($VS_WS,$VS_LVS,$VS_WSEnt) = split(/!/,$VS_VALUES[41]);
	if($VS_VALUES[45] eq "1"){
		$VS_WS="";
		$VS_LVS="";
	}

	require "./$LOG_FOLDER/$ABI_DATA";
	if($AbiSys == 1){
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		local($VABI_FLG,$VABI_A,$VABI_B,$VABI_C) = split(/!/,$VS_VALUES[52]);
	}

	&vabattle2;

#�A�r���e�B�V�X�e��
	$CriHosei = 0;
	$CriHosei2 = 0;
	if($AbiSys == 1 && $AbiMukou == 0){

		#�K�E�U��
		if($ABI_sA[2] =~ m/!A0016/ || $ABI_sB[2] =~ m/!A0016/ || $ABI_sC[2] =~ m/!A0016/){$CriHosei = 5;}

		#�X�g���C�J�[
		if($PL_VALUES[14] >= 40 && ($ABI_sA[2] =~ m/!A0013/ || $ABI_sB[2] =~ m/!A0013/ || $ABI_sC[2] =~ m/!A0013/)){$CriHosei = 20;}

		#�K�E�C��
		if($ABI_sA[2] =~ m/!A0015/ || $ABI_sB[2] =~ m/!A0015/ || $ABI_sC[2] =~ m/!A0015/){$CriHosei2 = 1;}
		
	}

##�N���e�B�J���I�I
#	if(int($PL_VALUES[18]/$PL_W[4]/10-10+$PL_VALUES[14]) > rand($PL_W[4])){
	if(int($PL_VALUES[18]/$PL_W[4]/10-10+$PL_VALUES[14]+$CriHosei) > rand($PL_W[4])){
		$CRITICAL=1;$R_VALUES[100]++;
	}else{
		$PL_W[4]+=$PL_VALUES[14] if $PL_VALUES[14];
	}
	$PL_W[4]*=5 if $CRITICAL;

#�A�r���e�B�V�X�e��
	#�K�E�C���@�N���e�B�J������MP5�{�␳��1.5�{�␳�ɕύX����
	if($PL_CRITICAL && $CriHosei2 eq "1"){$PL_W[4]=int($PL_W[4]/5*2.5);}

	if($CRITICAL && $PL_CLASS[17] =~ m/!W024/){$PL_W[4]=int($PL_W[4]/5*2);}
	elsif($CRITICAL && $PL_WA32 > 0){$PL_W[4]=int($PL_W[4]/5*(5 - $PL_WA32*0.2));}

	&vabattle3;

##�{��̈ꌂ�I
	if($PL_W[7] =~ m/!28/ && $VS_W[7] !~ m/!42/ && $VS_sB[7] !~ m/!42/ && $VS_sC[7] !~ m/!42/ && $VS_sD[7] !~ m/!42/){$Vs_DefPoint*=0.8;$PLIKARI=1;}
	&vabattle4;

	&vabattle5;


#��Z�n�G���`�����g
#�L���[
	if($PL_WA09 ne "" && $PL_WA09 > 0){$Pl_AtPoint = int($Pl_AtPoint * (1 + $PL_WA09 * 0.03));}
	if($PL_WB09 ne "" && $PL_WB09 > 0){$Pl_AtPoint = int($Pl_AtPoint * (1 + $PL_WB09 * 0.03));}
	if($PL_WC09 ne "" && $PL_WC09 > 0){$Pl_AtPoint = int($Pl_AtPoint * (1 + $PL_WC09 * 0.03));}
	if($PL_WD09 ne "" && $PL_WD09 > 0){$Pl_AtPoint = int($Pl_AtPoint * (1 + $PL_WD09 * 0.03));}
#�K�[�h
	if($PL_WA10 ne "" && $PL_WA10 > 0){$Vs_AtPoint = int($Vs_AtPoint * (1 - $PL_WA10 * 0.03));}
	if($PL_WB10 ne "" && $PL_WB10 > 0){$Vs_AtPoint = int($Vs_AtPoint * (1 - $PL_WB10 * 0.03));}
	if($PL_WC10 ne "" && $PL_WC10 > 0){$Vs_AtPoint = int($Vs_AtPoint * (1 - $PL_WC10 * 0.03));}
	if($PL_WD10 ne "" && $PL_WD10 > 0){$Vs_AtPoint = int($Vs_AtPoint * (1 - $PL_WD10 * 0.03));}

#�v�ǂ̖h��͂��ꗥ�����@�ΐ푊��̍U����35������
#20100612�@���������@45����35�� 20110327
#$Pl_AtPoint=int($Pl_AtPoint*0.5);
#20180528 �Ē���
#20190523 �Ē��� 0.8��0.6
$Pl_AtPoint=int($Pl_AtPoint*0.6);


#���[���h
	if($world){
		if($PL_W[7] =~ m/!18/){
			$Pl_AtPoint=int($Pl_AtPoint*0.7);
		}else{
			$Pl_AtPoint=int($Pl_AtPoint*0.8);
		}
	}

#�[�e�M�l�A�~�ρ@�K���V�A6���܂Ł@20100905���{ 0906����
#	if($VC_VALUES[39] eq "1"){
#			$Pl_AtPoint=int($Pl_AtPoint*0.5);
#			$Vs_AtPoint=int($Vs_AtPoint*1.5);
#	}


#���E��펞�͍X�ɖh�䋭�� 20180528����
#	if($WorldWar eq "1" && $WW_FRAG2 eq "1"){
#			$Pl_AtPoint=int($Pl_AtPoint*0.65);
#	}

#	if($COOKIE{'pass'} eq $MASTERPASS){$Pl_AtPoint=int($Pl_AtPoint*1.8);}

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

#	if($VS_VALUES[15] > 99999){
#		$Vs_HyoHP="�H�H�H";
#	}else{
		$Vs_HyoHP=$VS_VALUES[15];
#	}
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

	if ($world){print "<font color=#ff4d4d>���[���h�I�I�_���[�W�y���I�I</font><br>\n";}

	$seikou = 0;

	if($PL_WA33 ne "" && $PL_WA33 > 0 && rand(100) <= ($PL_WA33 * 2)){
		$PL_W[7] .= "!6x";
	}

	if ($PL_W[7] =~ m/!6b/ && $VS_VALUES[16] > 240000){
		if(rand(255) > 36){
		print "<font color=#ff0080>�G�v�ǂ̍ő�HP�Ƀ_���[�W�I�I</font><br>\n";

		$seikou = 1;

#		$PL_VALUES[17]=0;
		$lb+=10000 if ($VS_VALUES[16] > 245000);
		$lb+=5000 if ($VS_VALUES[16] > 300000);
		$lb+=5000 if ($VS_VALUES[16] > 400000);
		$lb/=2 if $world;
		$lb/=2 if $WorldWar eq "1" && $WW_FRAG2 eq "1";
		$Y_HP[1]-=$lb;
		$R_VALUES[132]+=1;
		}
	$R_VALUES[133]+=1;
	}

	$md=4;
	$md/=2 if $world;
	$md/=2 if $WorldWar eq "1" && $WW_FRAG2 eq "1";

	if ($PL_W[7] =~ m/!6x/ && $Y_STR > 7 && rand(255) > 46){
		print "<font color=#bb7a7d>�G�v�ǂ̍U���͂Ƀ_���[�W�I�I</font><br>\n";
		$Y_ST[0]-=$md+int(rand(2));$R_VALUES[27]++;
		#$PL_VALUES[17]=0;
		$seikou = 1;
	}
	if ($PL_W[7] =~ m/!6x/ && $Y_VIT > 7 && rand(255) > 46){
		print "<font color=#bb7a7d>�G�v�ǂ̖h��͂Ƀ_���[�W�I�I</font><br>\n";
		$Y_ST[1]-=$md+int(rand(2));$R_VALUES[27]++;
		#$PL_VALUES[17]=0;
		$seikou = 1;
	}
	if ($PL_W[7] =~ m/!6x/ && $Y_DEX > 7 && rand(255) > 46){
		print "<font color=#bb7a7d>�G�v�ǂ̖����͂Ƀ_���[�W�I�I</font><br>\n";
		$Y_ST[2]-=$md+int(rand(2));$R_VALUES[27]++;
		#$PL_VALUES[17]=0;
		$seikou = 1;
	}
	if ($Y_VIT > 40 && rand(255) > 46){
		print "<font color=#ff0080>�G�v�ǂ̖h��͂Ƀ_���[�W�I�I</font><br>\n";
		$Y_ST[1]--;
	}

	if($HoushoFlg == 1 && $WW_FRAG==0){

		if($PL_W[7] =~ m/!6b|!6x/){
			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			#���ݍv���_+40
			$HC[0] = $HC[0] + 40;
			$HC[2] = $HC[2] + 40;

			#�����ōX��+20
			if($seikou eq "1"){
				$HC[0] = $HC[0] + 20;
				$HC[2] = $HC[2] + 20;

				#���g�������̏ꍇ+20
				if($PL_VALUES[6] eq "1"){
					#���ݍv���_+20
					$HC[0] = $HC[0] + 20;
					$HC[2] = $HC[2] + 20;
				}elsif($PL_VALUES[6] eq "-1"){
				#���g�������̏ꍇ+7
					#���ݍv���_+7
					$HC[0] = $HC[0] + 7;
					$HC[2] = $HC[2] + 7;
				}
			}

			#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
	
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

	}

	&vabattle7;

#	&ERROR('���ɖŖS���Ă��܂��B') if !@VC_VALUES;

##����
	$TheEnd=1 if !$ResultBattle;
		$VC_VALUES[11]="$VS_VALUES[15]!$Y_HP[1]!$DATE";
		$Y_ST[0]-=(50+$SOUSUISIKI);
		$Y_ST[1]-=(50+$SOUSUISIKI);
		$Y_ST[2]-=(60+$SOUSUISIKI);
		$VC_VALUES[12]="$Y_ST[0]!$Y_ST[1]!$Y_ST[2]!$Y_ST[3]";

	if(!$ResultBattle && $PL_VALUES[5]){
		$CL_VALUES[1]+=$VS_VALUES[0]+20;
		if ($TheEnd==1){
			$CL_VALUES[1]+=50000;$CL_VALUES[13]++;$R_VALUES[4]+=1;
			if($PL_VALUES[6] != 0){$CL_VALUES[1]+=10000;}
		}
	}elsif($ResultBattle && $PL_VALUES[5]){
		$CL_VALUES[1]+=int(($VS_VALUES[0]+20)/3);
	}

	if (!$ResultBattle && $TheEnd == 1){
	$B_MONE=int(($CL_VALUES[13]*10000+50000)*$VC_VALUES[13]+rand(10000));
	$B_MONE=int(($CL_VALUES[13]*10000)+10000+rand(10000)) if !$VC_VALUES[13];
	$PL_VALUES[8]+=$B_MONE;
	$Mone="<img src=$IMG_FOLDER3/money.gif> Bonus Money $B_MONE goth";
	$CL_VALUES[1]+=($VC_VALUES[13]*5000+$CL_VALUES[13]*1000+int(rand(1000)));
##�^���b�g�J�[�h�擾
#	if(!$CL_VALUES[15]){
#		require "./$LOG_FOLDER/$CARD_DATA";
#		my@al=keys %VACARD_LIST;
#		my$length=@al;
#		$gcard=$al[int(rand($length))];
#		@q=split(/\,/,$VACARD_LIST{"$gcard"});
#		$Getcard="<img src=$IMG_FOLDER6/card.gif> �w$q[1]�x�̃J�[�h�������܂����B";
#		$CL_VALUES[15]=$gcard;
#	}

#	&ERROR('���ɖŖS���Ă��܂��B') if !@VC_VALUES;
	
	
	#�����y�ѓG���̍��������J�E���g����
	$JiCount = 0;
	$EnCount = 0;
	while (my($key,$val) = each %P){
		@VALS = split(/\s/,$val);
		if($PL_VALUES[5] eq $VALS[5]){
			$JiCount = $JiCount + 1;
		}
		if($VS_VALUES[5] eq $VALS[5]){
			$EnCount = $EnCount + 1;
		}
	}

#	if($NewHoushoFlg == 1){
	
#		$KoukenHosei = 1;
#		#��������25�l�ȏ�̏ꍇ�A�v���l�ቺ�␳
#		if($JiCount >= 25){$KoukenHosei = ((85 - $JiCount + 25)*0.01);}
#		#�G������30�l�ȏ�̏ꍇ�A�v���l�㏸�␳
#		if($EnCount >= 30){$KoukenHosei = $KoukenHosei * ((105 + $EnCount - 30)*0.01);}
	
#		$KoukenP = int((1 + $VC_VALUES[13]) * int(rand(120)+30) * $KoukenHosei);
#		if($KoukenP < 0){$KoukenP = 1;}

#	}

	#�����Ђ֔�΂��́A���������Ƃ����ꍇ���������̎w�����E�㏸
		while (my($key,$val) = each %P){
			@VALS = split(/\s/,$val);
			if($VS_VALUES[5] eq $VALS[5]){
				$VALS[5]=$VALS[28]='';
				$VALS[0]=$VALS[6]=0;

				#�J�̓V�X�e���@�v���_���N���A����
				if($HoushoFlg == 1){
					@HC=split(/!/,$VALS[50]);
					if($HC[0] eq ""){$HC[0] = 0;}
					if($HC[1] eq ""){$HC[1] = 0;}
					if($HC[2] eq ""){$HC[2] = 0;}
					
					#���ݍv���_0
					$HC[0] = 0;
		
					$VALS[50] = "$HC[0]!$HC[1]!$HC[2]!";
				}

#				#�V�^�J�̓V�X�e��
#				if($NewHoushoFlg == 1){
				
#					@HC=split(/!/,$VALS[50]);
#					if($HC[0] ne $HoushoKey){$VALS[50] = "";$HC[1]=0;$HC[2] = 0;}
#					if($HC[1] eq ""){$HC[1] = 0;}
#					if($HC[2] eq ""){$HC[2] = 0;}

#					$HC[1] = 0;
					
#					$VALS[50] = "$HC[0]!$HC[1]!$HC[2]!";
				
#				}

#				@TeRC=split(/!/,$VALS[47]);
#				if($TeRC[5] eq ""){$TeRC[5] = 0;}
#				$TeRC[5] = "0;
#				$VALS[47] = "$TeRC[0]!$TeRC[1]!$TeRC[2]!$TeRC[3]!$TeRC[4]!$TeRC[5]!$TeRC[6]!$TeRC[7]!$TeRC[8]!$TeRC[9]!$TeRC[10]!";

			}
			if($PL_VALUES[5] eq $VALS[5] && $VALS[6]==1){
				$VALS[35]++;
				$VALS[32]++;
			}
#			#�A�r���e�B�V�X�e���@�����S����AP�{�[�i�X
#			if($AbiSys == 1 && $PL_VALUES[5] eq $VALS[5]){
#				$PL_VALUES[53] = $PL_VALUES[53] + (1 + $VC_VALUES[13] + $CL_VALUES[13]) * 30;
#				if($PL_VALUES[53] > 9999){$PL_VALUES[53] = 9999;}
#			}

			#�V�^�J�̓V�X�e�� 20100519 ����
#			if($NewHoushoFlg == 1 && $PL_VALUES[5] eq $VALS[5]){
			
#				@HC=split(/!/,$VALS[50]);
#				if($HC[0] ne $HoushoKey){$VALS[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
#				if($HC[1] eq ""){$HC[1] = 0;}
#				if($HC[2] eq ""){$HC[2] = 0;}

##				$KoukenP = (1 + $VC_VALUES[13]) * int(rand(120)+30);

#				$HC[1] = $HC[1] + $KoukenP;
#				#�����̏ꍇ�A�v���_+50��
#				if($VALS[6] == 1){$HC[1] = $HC[1] + int($KoukenP * 0.5);}
				
#				if($HC[1] > 3000){$HC[1] = 3000;}
#				$HC[2] = $HC[2] + $KoukenP;
				
#				$VALS[50] = "$HC[0]!$HC[1]!$HC[2]!";
			
#			}

			dbmopen (%PL,"$DBM_P",0666);
			$PL{"$key"}="@VALS";
			dbmclose %PL;
		}
	#�����ŗ��Ƃ����ꍇ�w�����E�㏸
		if($PL_VALUES[6]==1){
			$PL_VALUES[35]++;
			$PL_VALUES[32]++;
		}
		
		#�V�^�J�̓V�X�e��
#		if($NewHoushoFlg == 1){
		
#			@HC=split(/!/,$PL_VALUES[50]);
#			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
#			if($HC[1] eq ""){$HC[1] = 0;}
#			if($HC[2] eq ""){$HC[2] = 0;}

#			$HC[1] = $HC[1] + $KoukenP;
#			#�����̏ꍇ�A�v���_+50��
#			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + int($KoukenP * 0.5);}

#			if($HC[1] > 3000){$HC[1] = 3000;}
#			$HC[2] = $HC[2] + $KoukenP;
			
#			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		
#		}

		if($HoushoFlg == 1 && $WW_FRAG==0){
	
			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			#���ݍv���_+150
			$HC[0] = $HC[0] + 150;
			$HC[2] = $HC[2] + 150;

			#���g�������̏ꍇ+75
			if($PL_VALUES[6] eq "1"){
				#���ݍv���_+75
				$HC[0] = $HC[0] + 75;
				$HC[2] = $HC[2] + 75;
			}elsif($PL_VALUES[6] eq "-1"){
			#���g�������̏ꍇ+40
				#���ݍv���_+40
				$HC[0] = $HC[0] + 40;
				$HC[2] = $HC[2] + 40;
			}

			#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
	
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
	
		}


#MVP�����L���O�p
		#�����L���O�p MVP�l�����@0�̓A�C�e���l���@1��MVP
		@RC=split(/!/,$PL_VALUES[47]);
		if($RC[1] eq ""){$RC[1] = 0;}
		$RC[1] = $RC[1] + 1;
		$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";

#	&ERROR('���ɖŖS���Ă��܂��B') if !@VC_VALUES;


#304�Ńg���t�B�[\vvvvvvv
		if (!$PL_VALUES[10] || !$PL_VALUES[11] || !$PL_VALUES[38] || !$PL_VALUES[41] || !$PL_VALUES[42] || !$PL_VALUES[43] || !$PL_VALUES[46]){
#			$arisia=($VC_VALUES[13]*40);
			$arisia=($VC_VALUES[13]*115);
#			$VC_VALUES[13]=$VC_VALUES[13]+15;
			$R_VALUES[154]=$arisia;
#			$Rams =
#			if(rand(4000) < $arisia){
			$flg_MV = 0;

			#�Ίݕ␳
			if($PL_VALUES[10] ne $VS_VALUES[39]){$VC_VALUES[13] = $VC_VALUES[13] + 0.5;}

#20180626 MVP�o�₷��
			$VC_VALUES[13] = $VC_VALUES[13] + 1;

			use List::Util qw(max min);
			$VC_VALUES[13] += max( $JiCount - 15, 0 ) * 0.05 + min( $JiCount, 15 ) * 0.5;
			$VC_VALUES[13] += max( $EnCount - 15, 0 ) * 0.2 + min( $EnCount, 15 ) * 0.5;

#�A�r���e�B�V�X�e��
			if($AbiSys == 1){
				#���b�L�[�@��Z+2�Ōv�Z����
				if($ABI_sA[2] =~ m/!A0014/ || $ABI_sB[2] =~ m/!A0014/ || $ABI_sC[2] =~ m/!A0014/){$VC_VALUES[13]+=2;}
			}

				if($MVPCALC eq "1"){

#					print "<font color=#ff0080>��Z�J�E���g�I$VC_VALUES[13]</font><br>\n";
					srand(time ^ ($$ + ($$ << 15)));	#����������
					$DropCount = int($VC_VALUES[13]);
					$DropGet = 0;

					#��Z20�ȏ��33���̊m���Ńt�@�C�A�N���X�g
#					if($VC_VALUES[13] >= 20 && rand(100) < 33){$tw = "2fq";$flg_MV = 1;}	#�t�@�C�A�N���X�g
					if($DropCount >= 20){

						if(33 >= rand(100)){$tw = "2fq";$flg_MV = 1;$DropGet = 1;}	#�t�@�C�A�N���X�g
						elsif(33 >= rand(100)){$tw = "2ga";$flg_MV = 1;$DropGet = 1;}	#�G�N�X�n���e�B�I

					}
					#12�ȏ�ŇU���@�]�[������
					if($DropGet eq "0" && $DropCount >= 10 && ((48 + ($DropCount - 11) * 4) >= rand(100))){

						if(rand(100) < 5){$tw = "0307a";$flg_MV = 1;$DropGet = 1;}	#�e���y�X�g�U
						elsif(rand(100) < 5){$tw = "0308a";$flg_MV = 1;$DropGet = 1;}	#�A�j�q���[�V�����U
						elsif(rand(100) < 5){$tw = "0309a";$flg_MV = 1;$DropGet = 1;}	#���e�I�X�g���C�N�U
						elsif(rand(100) < 5){$tw = "0310a";$flg_MV = 1;$DropGet = 1;}	#�z���C�g�~���[�g�U
						elsif(rand(100) < 5){$tw = "0311a";$flg_MV = 1;$DropGet = 1;}	#�G�A���A���N���C�U
						elsif(rand(100) < 5){$tw = "0312a";$flg_MV = 1;$DropGet = 1;}	#�X�[�p�[�m���@�U
						elsif(rand(100) < 5){$tw = "0313a";$flg_MV = 1;$DropGet = 1;}	#�A�[�X�N�G�C�N�U
						elsif(rand(100) < 5){$tw = "0314a";$flg_MV = 1;$DropGet = 1;}	#�A�C�X���N�C�G���U
						elsif(rand(100) < 5){$tw = "0315a";$flg_MV = 1;$DropGet = 1;}	#�X�^�[�e�B�A���U
						elsif(rand(100) < 5){$tw = "0316a";$flg_MV = 1;$DropGet = 1;}	#�f�b�h�X�N���[���U

					}
					#10�ȏ�ŃJ�i�Z�]�[������
#					elsif($VC_VALUES[13] >= 8 && (rand(100) < (48+($VC_VALUES[13]-9)*4))){
					if($DropGet eq "0" && $DropCount >= 8 && ((48 + ($DropCount - 9) * 4) >= rand(100))){
	
						if(rand(100) < 5){$tw = "2aa";$flg_MV = 1;$DropGet = 1;}	#�A�|�J���v�X
						elsif(rand(100) < 5){$tw = "2ab";$flg_MV = 1;$DropGet = 1;}	#�T���_�[�u���C�h
						elsif(rand(100) < 5){$tw = "2ac";$flg_MV = 1;$DropGet = 1;}	#�f�X�A�x���W���[
						elsif(rand(100) < 5){$tw = "2ad";$flg_MV = 1;$DropGet = 1;}	#�u���b�N�v���Y��
						elsif(rand(100) < 5){$tw = "2ae";$flg_MV = 1;$DropGet = 1;}	#�t���[���F�m��
						elsif(rand(100) < 5){$tw = "2af";$flg_MV = 1;$DropGet = 1;}	#�f�[�������[�Y
						elsif(rand(100) < 5){$tw = "2ag";$flg_MV = 1;$DropGet = 1;}	#�t���C�~���O�f�X
						elsif(rand(100) < 5){$tw = "2ah";$flg_MV = 1;$DropGet = 1;}	#���C�A�b�g�o�[��

					}

					#8�ȏ�ŗ�����]�[������
					if($DropGet eq "0" && $DropCount >= 6 && ((48 + ($DropCount - 7) * 4) >= rand(100))){
	
						if(rand(100) < 5){$tw = "0025a";$flg_MV = 1;$DropGet = 1;}	#�}�[�e�B���C�Y
						elsif(rand(100) < 5){$tw = "2ca";$flg_MV = 1;$DropGet = 1;}	#�e���y�X�g
						elsif(rand(100) < 5){$tw = "2cb";$flg_MV = 1;$DropGet = 1;}	#�A�j�q���[�V����
						elsif(rand(100) < 5){$tw = "2cc";$flg_MV = 1;$DropGet = 1;}	#���e�I�X�g���C�N
						elsif(rand(100) < 5){$tw = "2cd";$flg_MV = 1;$DropGet = 1;}	#�z���C�g�~���[�g
	
					}
					#6�ȏ�œ`�����O�`�Z�]�[������
#					elsif($VC_VALUES[13] >= 6 && rand(100) < 10+$VC_VALUES[13]-6){
					if($DropGet eq "0" && $DropCount >= 4 && ((48 + ($DropCount - 5) * 4) >= rand(100))){
	
						if(rand(100) < 2){$tw = "1034a";$flg_MV = 1;$DropGet = 1;}	#�\�j�b�N�u�[��
						elsif(rand(100) < 5){$tw = "2cg";$flg_MV = 1;$DropGet = 1;}	#�f�B�Z���g
						elsif(rand(100) < 5){$tw = "2dd";$flg_MV = 1;$DropGet = 1;}	#�w���Y�Q�[�g
						elsif(rand(100) < 5){$tw = "2ea";$flg_MV = 1;$DropGet = 1;}	#�_�E���N���E�Y
						elsif(rand(100) < 5){$tw = "2fa";$flg_MV = 1;$DropGet = 1;}	#�\�j�b�N�u���C�h
						elsif(rand(100) < 5){$tw = "2da";$flg_MV = 1;$DropGet = 1;}	#�A�g���|�X
						elsif(rand(100) < 5){$tw = "2db";$flg_MV = 1;$DropGet = 1;}	#���P�V�X
						elsif(rand(100) < 5){$tw = "2dc";$flg_MV = 1;$DropGet = 1;}	#�N���g
						elsif(rand(100) < 5){$tw = "2eb";$flg_MV = 1;$DropGet = 1;}	#�C�N�X�e�B���N
	
					}

					#5�ȏ�ŇU�������@�]�[������
					if($DropGet eq "0" && $DropCount >= 3 && ((48 + ($DropCount - 4) * 4) >= rand(100))){

						if(rand(100) < 5){$tw = "0301a";$flg_MV = 1;$DropGet = 1;}	#�T���_�[�o�[�h�U
						elsif(rand(100) < 5){$tw = "0302a";$flg_MV = 1;$DropGet = 1;}	#�T���}���_�[�U
						elsif(rand(100) < 5){$tw = "0303a";$flg_MV = 1;$DropGet = 1;}	#�m�[���U
						elsif(rand(100) < 5){$tw = "0304a";$flg_MV = 1;$DropGet = 1;}	#�t�F�������U
						elsif(rand(100) < 5){$tw = "0305a";$flg_MV = 1;$DropGet = 1;}	#�_�[�N���A�U
						elsif(rand(100) < 5){$tw = "0306a";$flg_MV = 1;$DropGet = 1;}	#�C�O�j�X�t�@�^�X�U

					}

					#4�ȏ�Ŋ����Z�]�[������
#					elsif($VC_VALUES[13] >= 4 && rand(100) < 10+$VC_VALUES[13]-4){
					if($DropGet eq "0" && $DropCount >= 3 && ((48 + ($DropCount - 3) * 4) >= rand(100))){
	
						if(rand(100) < 5){$tw = "2ba";$flg_MV = 1;$DropGet = 1;}	#�_������
						elsif(rand(100) < 5){$tw = "2bb";$flg_MV = 1;$DropGet = 1;}	#�o���׉���
						elsif(rand(100) < 5){$tw = "2bc";$flg_MV = 1;$DropGet = 1;}	#�V�������g
						elsif(rand(100) < 5){$tw = "2bd";$flg_MV = 1;$DropGet = 1;}	#�{�����j��
						elsif(rand(100) < 5){$tw = "2be";$flg_MV = 1;$DropGet = 1;}	#�e�������g
						elsif(rand(100) < 5){$tw = "2bf";$flg_MV = 1;$DropGet = 1;}	#�g�������a
						elsif(rand(100) < 5){$tw = "2bg";$flg_MV = 1;$DropGet = 1;}	#�����V�j�a
						elsif(rand(100) < 5){$tw = "2bh";$flg_MV = 1;$DropGet = 1;}	#����󕗌�
						elsif(rand(100) < 5){$tw = "2bi";$flg_MV = 1;$DropGet = 1;}	#�S�L���U�a
						elsif(rand(100) < 5){$tw = "2bj";$flg_MV = 1;$DropGet = 1;}	#���Ԓn��a
	
					}
					#3�ȏ�Ńu���X�g�Z�]�[������
#					elsif($VC_VALUES[13] >= 3 && rand(100) < 10+$VC_VALUES[13]-3){
					if($DropGet eq "0" && $DropCount >= 2 && ((48 + ($DropCount - 2) * 4) >= rand(100))){
	
						if(rand(100) < 5){$tw = "2fc";$flg_MV = 1;$DropGet = 1;}	#�E�B���h�u���X�g
						elsif(rand(100) < 5){$tw = "2fd";$flg_MV = 1;$DropGet = 1;}	#�t�@�C�A�u���X�g
						elsif(rand(100) < 5){$tw = "2fe";$flg_MV = 1;$DropGet = 1;}	#�A�[�X�u���X�g
						elsif(rand(100) < 5){$tw = "2ff";$flg_MV = 1;$DropGet = 1;}	#�A�N�A�u���X�g
						elsif(rand(100) < 5){$tw = "2fg";$flg_MV = 1;$DropGet = 1;}	#�z�[���[�u���X�g
						elsif(rand(100) < 5){$tw = "2fh";$flg_MV = 1;$DropGet = 1;}	#�_�[�N�u���X�g
						elsif(rand(100) < 5){$tw = "2fb";$flg_MV = 1;$DropGet = 1;}	#�\�j�b�N�u���X�g
	
					}
					#1�ȏ�ł��̑��FA�]�[������
					if($DropGet eq "0" && $DropCount >= 1 && ((48 + $DropCount - 2) >= rand(100))){
	
						if(rand(100) < 6){$tw = "2fo";$flg_MV = 1;$DropGet = 1;}		#�K�����g�N�@���]���낗��
						elsif(rand(100) < 2){$tw = "2fv";$flg_MV = 1;$DropGet = 1;}	#���[���@���e�C��
						elsif(rand(100) < 2){$tw = "2de";$flg_MV = 1;$DropGet = 1;}	#�����M�R���j�X
						elsif(rand(100) < 4){$tw = "71c";$flg_MV = 1;$DropGet = 1;}	#���U���I
#						elsif(rand(100) < 6){$tw = "2gb";$flg_MV = 1;$DropGet = 1;}	#�W�B���K�̖��|
#						elsif(rand(100) < 6){$tw = "2gc";$flg_MV = 1;$DropGet = 1;}	#�N���V�F���e
						elsif(rand(100) < 6){$tw = "ub2gb";$flg_MV = 1;$DropGet = 1;}	#�W�B���K�̖��|
						elsif(rand(100) < 6){$tw = "ub2gc";$flg_MV = 1;$DropGet = 1;}	#�N���V�F���e
						elsif(rand(100) < 6){$tw = "2000a";$flg_MV = 1;$DropGet = 1;}	#�K���[�_�̋|
						elsif(rand(100) < 6){$tw = "2000b";$flg_MV = 1;$DropGet = 1;}	#�C�V���L�~���̋|
						elsif(rand(100) < 6){$tw = "2000c";$flg_MV = 1;$DropGet = 1;}	#�N�s�h�̋|
						elsif(rand(100) < 6){$tw = "2000d";$flg_MV = 1;$DropGet = 1;}	#�g�Η��̋|
						elsif(rand(100) < 6){$tw = "2000e";$flg_MV = 1;$DropGet = 1;}	#�Z���e�I�g���̋|

						elsif(rand(100) < 6){$tw = "����";$flg_MV = 1;$DropGet = 1;}	#����
						elsif(rand(100) < 6){$tw = "������";$flg_MV = 1;$DropGet = 1;}	#������
						elsif(rand(100) < 6){$tw = "�Ɏɓ�";$flg_MV = 1;$DropGet = 1;}	#�Ɏɓ�
						elsif(rand(100) < 6){$tw = "����";$flg_MV = 1;$DropGet = 1;}	#����
						elsif(rand(100) < 6){$tw = "���C��";$flg_MV = 1;$DropGet = 1;}	#���C��
						elsif(rand(100) < 6){$tw = "������";$flg_MV = 1;$DropGet = 1;}	#������
						elsif(rand(100) < 6){$tw = "��旅";$flg_MV = 1;$DropGet = 1;}	#��旅
						elsif(rand(100) < 6){$tw = "���ܗ�";$flg_MV = 1;$DropGet = 1;}	#���ܗ�
						elsif(rand(100) < 6){$tw = "�����n";$flg_MV = 1;$DropGet = 1;}	#�����n
						elsif(rand(100) < 6){$tw = "�O����";$flg_MV = 1;$DropGet = 1;}	#�O����
						elsif(rand(100) < 6){$tw = "����";$flg_MV = 1;$DropGet = 1;}	#����


						elsif(rand(100) < 8){$tw = "6ba";$flg_MV = 1;$DropGet = 1;}	#���v���Y���b�h
						elsif(rand(100) < 8){$tw = "6ca";$flg_MV = 1;$DropGet = 1;}	#�K���o���e�C��
						elsif(rand(100) < 14){$tw = "0020a";$flg_MV = 1;$DropGet = 1;}	#���_�̍b�h�@�[�e�M�l�A���Ƃ𗎂Ƃ�
						elsif(rand(100) < 8){$tw = "2ce";$flg_MV = 1;$DropGet = 1;}	#�C�O�j�X�t�@�^�X
						elsif(rand(100) < 14){$tw = "2ha";$flg_MV = 1;$DropGet = 1;}	#�m�g�X
						elsif(rand(100) < 14){$tw = "2hb";$flg_MV = 1;$DropGet = 1;}	#�{���A�X
						elsif(rand(100) < 14){$tw = "2hc";$flg_MV = 1;$DropGet = 1;}	#�G�E���X
						elsif(rand(100) < 14){$tw = "2hd";$flg_MV = 1;$DropGet = 1;}	#�[�s�����X
						elsif(rand(100) < 14){$tw = "2cf";$flg_MV = 1;$DropGet = 1;}	#�T�o�g
						elsif(rand(100) < 14){$tw = "2gf";$flg_MV = 1;$DropGet = 1;}	#�I�Y���b�N�X�s�A
						elsif(rand(100) < 14){$tw = "2gh";$flg_MV = 1;$DropGet = 1;}	#�����O�I�u�p���[
						elsif(rand(100) < 14){$tw = "2gi";$flg_MV = 1;$DropGet = 1;}	#���V�t�@�[�����O
						elsif(rand(100) < 14){$tw = "2gm";$flg_MV = 1;$DropGet = 1;}	#�m�C�b�V���̐���
						elsif(rand(100) < 14){$tw = "2gq";$flg_MV = 1;$DropGet = 1;}	#�V���K�[�P�[��
						elsif(rand(100) < 14){$tw = "2gr";$flg_MV = 1;$DropGet = 1;}	#�P�[�����P�C�I��
						elsif(rand(100) < 14){$tw = "2gs";$flg_MV = 1;$DropGet = 1;}	#�W�v�V�[�N�C�[��
						elsif(rand(100) < 14){$tw = "0012a";$flg_MV = 1;$DropGet = 1;}	#���Ђ̊O��
						elsif(rand(100) < 14){$tw = "0019a";$flg_MV = 1;$DropGet = 1;}	#�l�N���}���V�[
						elsif(rand(100) < 14){$tw = "2fn";$flg_MV = 1;$DropGet = 1;}	#����
						elsif(rand(100) < 14){$tw = "2gg";$flg_MV = 1;$DropGet = 1;}	#�����̑匕
						elsif(rand(100) < 14){$tw = "2gj";$flg_MV = 1;$DropGet = 1;}	#���[���A�b�N�X
						elsif(rand(100) < 14){$tw = "2gk";$flg_MV = 1;$DropGet = 1;}	#�T�^���u���[�o�[
						elsif(rand(100) < 14){$tw = "0009a";$flg_MV = 1;$DropGet = 1;}	#�����َq�̃����C
						elsif(rand(100) < 14){$tw = "0010a";$flg_MV = 1;$DropGet = 1;}	#�O�����T�[�R�[�g
						elsif(rand(100) < 14){$tw = "0015a";$flg_MV = 1;$DropGet = 1;}	#�L�����f�B�w����
						elsif(rand(100) < 14){$tw = "0016a";$flg_MV = 1;$DropGet = 1;}	#�z�[���[�N���E��
						elsif(rand(100) < 14){$tw = "0005a";$flg_MV = 1;$DropGet = 1;}	#�_�[�N���A
						elsif(rand(100) < 14){$tw = "2fk";$flg_MV = 1;$DropGet = 1;}	#�y���_�[�g�\�[�h
						elsif(rand(100) < 14){$tw = "2fl";$flg_MV = 1;$DropGet = 1;}	#�j�t���[�g�\�[�h
						elsif(rand(100) < 14){$tw = "2fm";$flg_MV = 1;$DropGet = 1;}	#������
						elsif(rand(100) < 14){$tw = "2gp";$flg_MV = 1;$DropGet = 1;}	#�K���X�̃J�{�`��
						elsif(rand(100) < 14){$tw = "1oe";$flg_MV = 1;$DropGet = 1;}	#�����̐�
						elsif(rand(100) < 14){$tw = "1of";$flg_MV = 1;$DropGet = 1;}	#�u���b�h�X�y��
						else{$tw = "0013a";$flg_MV = 1;$DropGet = 1;}	#�����̃h���X
	
					}
					if($DropGet eq "0" && $VC_VALUES[13] >= 0 && rand(700) < $arisia){$tw = "1";$flg_MV = 1;}	#��������


				}else{

					if($VC_VALUES[13] >= 30 && rand(6000) < $arisia){$tw = "2fo";$flg_MV = 1;}		#�K�����g�N�@���]���낗��
					elsif($VC_VALUES[13] >= 30 && rand(6000) < $arisia){$tw = "2fq";$flg_MV = 1;}	#�t�@�C�A�N���X�g
					elsif($VC_VALUES[13] >= 20 && rand(6000) < $arisia){$tw = "2fv";$flg_MV = 1;}	#���[���@���e�C��
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2ab";$flg_MV = 1;}	#�T���_�[�u���C�h
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2ac";$flg_MV = 1;}	#�f�X�A�x���W���[
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2ad";$flg_MV = 1;}	#�u���b�N�v���Y��
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2ae";$flg_MV = 1;}	#�t���[���F�m��
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2af";$flg_MV = 1;}	#�f�[�������[�Y
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2ag";$flg_MV = 1;}	#�t���C�~���O�f�X
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2ah";$flg_MV = 1;}	#���C�A�b�g�o�[��
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2aa";$flg_MV = 1;}	#�A�|�J���v�X
					elsif($VC_VALUES[13] >= 20 && rand(5000) < $arisia){$tw = "2de";$flg_MV = 1;}	#�����M�R���j�X
					elsif($VC_VALUES[13] >= 20 && rand(4000) < $arisia){$tw = "1034a";$flg_MV = 1;}	#�\�j�b�N�u�[��
					elsif($VC_VALUES[13] >= 15 && rand(4000) < $arisia){$tw = "71c";$flg_MV = 1;}	#���U���I
					elsif($VC_VALUES[13] >= 15 && rand(4000) < $arisia){$tw = "2cg";$flg_MV = 1;}	#�f�B�Z���g
					elsif($VC_VALUES[13] >= 15 && rand(4000) < $arisia){$tw = "2dd";$flg_MV = 1;}	#�w���Y�Q�[�g
					elsif($VC_VALUES[13] >= 15 && rand(4000) < $arisia){$tw = "2ea";$flg_MV = 1;}	#�_�E���N���E�Y
					elsif($VC_VALUES[13] >= 15 && rand(4000) < $arisia){$tw = "2fa";$flg_MV = 1;}	#�\�j�b�N�u���C�h
					elsif($VC_VALUES[13] >= 12 && rand(4000) < $arisia){$tw = "2ca";$flg_MV = 1;}	#�e���y�X�g
					elsif($VC_VALUES[13] >= 12 && rand(4000) < $arisia){$tw = "2cb";$flg_MV = 1;}	#�A�j�q���[�V����
					elsif($VC_VALUES[13] >= 12 && rand(4000) < $arisia){$tw = "2cc";$flg_MV = 1;}	#���e�I�X�g���C�N
					elsif($VC_VALUES[13] >= 12 && rand(4000) < $arisia){$tw = "2cd";$flg_MV = 1;}	#�z���C�g�~���[�g
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2gb";$flg_MV = 1;}	#�W�B���K�̖��|
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2gc";$flg_MV = 1;}	#�N���V�F���e
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "6ba";$flg_MV = 1;}	#���v���Y���b�h
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "6ca";$flg_MV = 1;}	#�K���o���e�C��
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia && $VC_VALUES[39] eq "1"){$tw = "0020a";$flg_MV = 1;}	#���_�̍b�h�@�[�e�M�l�A���Ƃ𗎂Ƃ�
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2ce";$flg_MV = 1;}	#�C�O�j�X�t�@�^�X
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2da";$flg_MV = 1;}	#�A�g���|�X
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2db";$flg_MV = 1;}	#���P�V�X
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2dc";$flg_MV = 1;}	#�N���g
					elsif($VC_VALUES[13] >= 10 && rand(3000) < $arisia){$tw = "2eb";$flg_MV = 1;}	#�C�N�X�e�B���N
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2ba";$flg_MV = 1;}	#�_������
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bb";$flg_MV = 1;}	#�o���׉���
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bc";$flg_MV = 1;}	#�V�������g
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bd";$flg_MV = 1;}	#�{�����j��
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2be";$flg_MV = 1;}	#�e�������g
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bf";$flg_MV = 1;}	#�g�������a
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bg";$flg_MV = 1;}	#�����V�j�a
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bh";$flg_MV = 1;}	#����󕗌�
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bi";$flg_MV = 1;}	#�S�L���U�a
					elsif($VC_VALUES[13] >= 8 && rand(2700) < $arisia){$tw = "2bj";$flg_MV = 1;}	#���Ԓn��a
					elsif($VC_VALUES[13] >= 7 && rand(2200) < $arisia){$tw = "2ha";$flg_MV = 1;}	#�m�g�X
					elsif($VC_VALUES[13] >= 7 && rand(2200) < $arisia){$tw = "2hb";$flg_MV = 1;}	#�{���A�X
					elsif($VC_VALUES[13] >= 7 && rand(2200) < $arisia){$tw = "2hc";$flg_MV = 1;}	#�G�E���X
					elsif($VC_VALUES[13] >= 7 && rand(2200) < $arisia){$tw = "2hd";$flg_MV = 1;}	#�[�s�����X
					elsif($VC_VALUES[13] >= 7 && rand(2200) < $arisia){$tw = "2cf";$flg_MV = 1;}	#�T�o�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gf";$flg_MV = 1;}	#�I�Y���b�N�X�s�A
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gh";$flg_MV = 1;}	#�����O�I�u�p���[
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gi";$flg_MV = 1;}	#���V�t�@�[�����O
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gm";$flg_MV = 1;}	#�m�C�b�V���̐���
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gq";$flg_MV = 1;}	#�V���K�[�P�[��
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gr";$flg_MV = 1;}	#�P�[�����P�C�I��
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2gs";$flg_MV = 1;}	#�W�v�V�[�N�C�[��
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "0012a";$flg_MV = 1;}	#���Ђ̊O��
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "0019a";$flg_MV = 1;}	#�l�N���}���V�[
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2fb";$flg_MV = 1;}	#�\�j�b�N�u���X�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2fc";$flg_MV = 1;}	#�E�B���h�u���X�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2fd";$flg_MV = 1;}	#�t�@�C�A�u���X�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2fe";$flg_MV = 1;}	#�A�[�X�u���X�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2ff";$flg_MV = 1;}	#�A�N�A�u���X�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2fg";$flg_MV = 1;}	#�z�[���[�u���X�g
					elsif($VC_VALUES[13] >= 5 && rand(1800) < $arisia){$tw = "2fh";$flg_MV = 1;}	#�_�[�N�u���X�g
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "2fn";$flg_MV = 1;}	#����
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "2gg";$flg_MV = 1;}	#�����̑匕
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "2gj";$flg_MV = 1;}	#���[���A�b�N�X
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "2gk";$flg_MV = 1;}	#�T�^���u���[�o�[
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "0009a";$flg_MV = 1;}	#�����َq�̃����C
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "0010a";$flg_MV = 1;}	#�O�����T�[�R�[�g
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia && $VC_VALUES[39] eq "2"){$tw = "0015a";$flg_MV = 1;}	#�L�����f�B�w����
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "0016a";$flg_MV = 1;}	#�z�[���[�N���E��
					elsif($VC_VALUES[13] >= 3 && rand(1000) < $arisia){$tw = "0005a";$flg_MV = 1;}	#�_�[�N���A
					elsif($VC_VALUES[13] >= 1 && rand(2400) < $arisia){$tw = "2fk";$flg_MV = 1;}	#�y���_�[�g�\�[�h
					elsif($VC_VALUES[13] >= 1 && rand(2400) < $arisia){$tw = "2fl";$flg_MV = 1;}	#�j�t���[�g�\�[�h
					elsif($VC_VALUES[13] >= 1 && rand(2400) < $arisia){$tw = "2fm";$flg_MV = 1;}	#������
					elsif($VC_VALUES[13] >= 1 && rand(3200) < $arisia){$tw = "2gp";$flg_MV = 1;}	#�K���X�̃J�{�`��
					elsif($VC_VALUES[13] >= 1 && rand(700) < $arisia){$tw = "1oe";$flg_MV = 1;}	#�����̐�
					elsif($VC_VALUES[13] >= 1 && rand(700) < $arisia){$tw = "1of";$flg_MV = 1;}	#�u���b�h�X�y��
					elsif($VC_VALUES[13] >= 1 && rand(700) < $arisia && $VC_VALUES[39] eq "1"){$tw = "0013a";$flg_MV = 1;}	#�����̃h���X
					elsif($VC_VALUES[13] >= 1 && rand(700) < $arisia){$tw = "1";$flg_MV = 1;}	#��������

				}

#	&ERROR('���ɖŖS���Ă��܂��B') if !@VC_VALUES;

				if($flg_MV eq "1"){
					@q=split(/\,/,$WEAPON_LIST{"$tw"});
#20180626 �헪��MFUP��␳�{�[�i�X�@0��10
					$MFUP=10;
					if($PL_WA12 ne "" && $PL_WA12 > 0 && $PL_flgEnt > 0){$MFUP = $MFUP + $PL_WA12 * 2;}
					if($PL_WB12 ne "" && $PL_WB12 > 0 && $PL_flgEnt2 > 0){$MFUP = $MFUP + $PL_WB12 * 2;}
					if($PL_WC12 ne "" && $PL_WC12 > 0 && $PL_flgEnt3 > 0){$MFUP = $MFUP + $PL_WC12 * 2;}
					if($PL_WD12 ne "" && $PL_WD12 > 0 && $PL_flgEnt4 > 0){$MFUP = $MFUP + $PL_WD12 * 2;}

					$ent="!0!0";
					if($q[11] eq "0"){

						#STR�{�[�i�X
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

						#VIT�{�[�i�X
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

						#DEX�{�[�i�X
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

						#AGI�{�[�i�X
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
						
						#�}�W�b�N�t�@�C���h�@���h�����
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

						#�����z���@�������
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

						#�}�i�u�[�X�g�@��E�����
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

						#��Z�L���[
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
						
						#��Z�K�[�h
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

						#�g���W���[�������A�b�v
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
						
						#RES�A�b�v
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

						#�Α����U���̓A�b�v
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

						#�������U���̓A�b�v
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

						#��n�����U���̓A�b�v
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

						#�������U���̓A�b�v
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

						#�_�������U���̓A�b�v
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
						
						#�Í������U���̓A�b�v
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

						#�Α����_���[�W�y��
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
						
						#�������_���[�W�y��
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

						#��n�����_���[�W�y��
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

						#�������_���[�W�y��
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

						#�_�������_���[�W�y��
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

						#�Í������_���[�W�y��
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

						#�������_���[�W�y��
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

						#�l��Goth�A�b�v
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

						#�m����HP�� ����p�K��
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
						
						#�퓬�s�\��MP�� ���}�i���J�o���[
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
						
						#�_���[�W���z
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

						#�񕜖��@����
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

						#�N���e�B�J��
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

						#�ђʍU��
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
						
#						$ent .= "$ent_str$ent_vit$ent_dex$ent_agi!$ent_dl!$ent_mnb!$ent_kabok!$ent_kabog!$ent_tore!$ent_mf!$ent_res!$ent_fireb!$ent_waterb!$ent_earthb!$ent_windb!$ent_saintb!$ent_darkb!$ent_fireg!$ent_waterg!$ent_earthg!$ent_windg!$ent_saintg!$ent_darkg!$ent_img!$ent_gou!$ent_hhp!$ent_mmp!$ent_dam!$ent_hea!$ent_cri";
						$ent .= "$ent_str$ent_vit$ent_dex$ent_agi$ent_dl$ent_mnb$ent_kabok$ent_kabog$ent_tore$ent_mf$ent_res$ent_fireb$ent_waterb$ent_earthb$ent_windb$ent_saintb$ent_darkb$ent_fireg$ent_waterg$ent_earthg$ent_windg$ent_saintg$ent_darkg$ent_img$ent_gou$ent_hhp$ent_mmp$ent_dam$ent_hea$ent_cri$ent_brk";

					}


					if(!$PL_VALUES[10] && $q[11] == 0){
						$PL_VALUES[10]=$tw;$PL_VALUES[10].=$ent;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
					}elsif(!$PL_VALUES[11] && $q[11] == 0){
						$PL_VALUES[11]=$tw;$PL_VALUES[11].=$ent;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
					}elsif(!$PL_VALUES[38] && $q[11] == 0){
						$PL_VALUES[38]=$tw;$PL_VALUES[38].=$ent;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
					}elsif(!$PL_VALUES[41] && $q[11] != 0){
						$PL_VALUES[41]=$tw;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
					}elsif(!$PL_VALUES[42] && $q[11] != 0){
						$PL_VALUES[42]=$tw;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
					}elsif(!$PL_VALUES[43] && $q[11] != 0){
						$PL_VALUES[43]=$tw;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
#					}elsif(!$PL_VALUES[46] && $PL_STF eq "1"){
					}elsif(!$PL_VALUES[46]){
						$PL_VALUES[46]=$tw;$PL_VALUES[46].=$ent;$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
					}

				}

#			}
		}

#�^���b�g�J�[�h�擾
	if(!$CL_VALUES[15]){
		require "./$LOG_FOLDER/$CARD_DATA";
		my@al=keys %VACARD_LIST;
		my$length=@al;
		$gcard=$al[int(rand($length))];
		@q=split(/\,/,$VACARD_LIST{"$gcard"});
		$Getcard="<img src=$IMG_FOLDER6/card.gif> �w$q[1]�x�̃J�[�h�������܂����B";
		$CL_VALUES[15]=$gcard;
	}


#�g���t�B�[
#		if (!$PL_VALUES[10] || !$PL_VALUES[11] || !$PL_VALUES[38]){
#			$arisia=($VC_VALUES[13]*110);
#			$R_VALUES[154]=$arisia;
#			if(rand(4000) < $arisia){
##-----------------���͂܂����܂��Ă���܂���(��-------------------
#				if(!$PL_VALUES[10]){
#					$PL_VALUES[10]=$tw;
#				}elsif(!$PL_VALUES[11]){
#					$PL_VALUES[11]=$tw;
#				}elsif(!$PL_VALUES[38]){
#					$PL_VALUES[38]=$tw;
#				}
#			$TROPHIES=" <img src=$IMG_FOLDER3/trophy.gif> War Trophies $q[0]";
#			}
#		}
	}

	&vabattle8;

	&vabattle9;

}

1;

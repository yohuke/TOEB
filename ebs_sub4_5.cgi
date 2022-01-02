sub BATTLE5{
	require './vabattle.pl';
	&vabattleheader;

	&LOCK;
		&DBM_CONVERT('P',"$FORM{pname}",'VS',"$FORM{vsname}");
		&DBM_CONVERT('C',"$PL_VALUES[5]",'VC',"$VS_VALUES[5]");

	&vabattle1;

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

##回復モードの場合、プレイヤーが回復・蘇生魔法をセットしていない場合は戦闘不可とする
	if($FORM{"sentaku"} eq ""){&ERROR("回復コマンドでは、回復・蘇生・補助魔法を選択してくださ～い。選択できない場合は使用できません。");}

	&vabattle2;

	$R_VALUES[28]++ if $PL_W[7]=~ m/!6j/;
	$R_VALUES[29]++ if $PL_W[7]=~ m/!6k/;
	$R_VALUES[30]++ if $PL_W[7]=~ m/!6l/;
	$R_VALUES[28]++ if $PL_W[7]=~ m/!76/;#ヒーリングプラス

	&vabattle3;

	&vabattle4;
##回復・エネミーサイド攻撃力0
	$Pl_AttPoint*=(rand(20)+90)/100;
	$Pl_AttPoint*=-1 if $PL_W[7] !~ m/!6o/;
	if($VS_VALUES[25]==1 && $PL_W[7] !~ m/!6l/){
		$Pl_AttPoint=0;
	}
	if($VS_VALUES[25]==0 && $PL_W[7] =~ m/!6l/){
		$Pl_AttPoint=0;
	}

#エンチャント　回復魔法強化$PL_WA31
	$PL_HealUP = 0;
	$PL_HealUPMP = 0;
	if($PL_WA31 eq ""){$PL_WA31=0;}
	if($PL_WB31 eq ""){$PL_WB31=0;}
	if($PL_WC31 eq ""){$PL_WC31=0;}
	if($PL_WD31 eq ""){$PL_WD31=0;}
	$PL_HealUP = $PL_WA31 + $PL_WB31 + $PL_WC31 + $PL_WD31;
	$PL_HealUPMP = $PL_WA31 + $PL_WB31 + $PL_WC31 + $PL_WD31;
	$Pl_AttPoint = int($Pl_AttPoint * (1 + $PL_HealUP*0.03));
	$PL_W[4] = int($PL_W[4] * (1 - $PL_HealUP*0.01));

	$Vs_AttPoint=0;
	$Vs_DefPoint=0;
	&vabattle5;

#	if($PL_W[7]=~ m/!6k|!6l|!77/ || $PL_sS[7]=~ m/!6k|!6l|!77/){$Pl_AtPoint=$VS_VALUES[16];}
	#ヒーリングオール
	if(($PL_W[7]=~ m/!6k/ || $PL_sS[7]=~ m/!6k/) && ($VS_VALUES[25]==0)){$Pl_AtPoint=$VS_VALUES[16];}
	#リザレクション
	if(($PL_W[7]=~ m/!6l0/ || $PL_sS[7]=~ m/!6l0/) && ($VS_VALUES[25]==1)){$Pl_AtPoint=int $VS_VALUES[16]/10;$VS_VALUES[25]=0;}
	if(($PL_W[7]=~ m/!6l1/ || $PL_sS[7]=~ m/!6l1/) && ($VS_VALUES[25]==1)){$Pl_AtPoint=int $VS_VALUES[16]/2;$VS_VALUES[25]=0;}
	if(($PL_W[7]=~ m/!77/ || $PL_sS[7]=~ m/!77/) && $VS_CLASS[17] =~ m/!E004/){$Pl_AtPoint=$VS_VALUES[16];}

	$Pl_AtPoint=0 if $Pl_AtPoint < 0;
	$Vs_AtPoint=0;
	$dmgStyl="style=\"font-size:21px;color:#a8e69a;\"";
	$chaStyl="style=\"font-size:12px;color:#78b69a;\"";
	$PlsumDmg="<b $dmgStyl>$Pl_AtPoint</b><b $chaStyl> heal</b>";
	$VssumDmg='<font color=#6a5acd>wait</font>';
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
	$Vs_BfrHP=$VS_VALUES[15]+$Pl_AtPoint;
	$Vs_BfrHP=$VS_VALUES[16] if $VS_VALUES[16] < $Vs_BfrHP;
	$Pl_AtPoint=$VS_VALUES[16]-$VS_VALUES[15] if $VS_VALUES[16]-$VS_VALUES[15] < $Pl_AtPoint;
	$Vs_width_per=$VS_VALUES[16]/150;
	$Vs_width_hp=int($VS_VALUES[15]/$Vs_width_per);


#相手がアンデッドクラスの場合は、回復量を0にする
	if($VS_CLASS[17] !~ m/!E004/){
		$VS_VALUES[15]=$VS_VALUES[15]+$Pl_AtPoint;
	}


	$Vs_width_dmg=int($Pl_AtPoint/$Vs_width_per);
	$Vs_width_zen=int(($VS_VALUES[16]-$Vs_BfrHP)/$Vs_width_per);
	$VS_HPTAG="<img src=\"$IMG_FOLDER1/hp.gif\" hspace=0 height=7 width=$Vs_width_hp>" if $Vs_width_hp;
	$VS_HPTAG.="<img src=\"$IMG_FOLDER1/heal.gif\" hspace=0 height=7 width=$Vs_width_dmg>" if $Vs_width_dmg;
	$VS_HPTAG.="<img src=\"$IMG_FOLDER1/zen.gif\" hspace=0 height=7 width=$Vs_width_zen>" if $Vs_width_zen;
	if(!$PL_VALUES[5]){$PL_VALUES[0]='0';}
	if(!$VS_VALUES[5]){$VS_VALUES[0]='0';}
	if($PL_VALUES[29] > 100){$PLLVKYU=100;}else{$PLLVKYU=$PL_VALUES[29];}
	if($VS_VALUES[29] > 100){$VSLVKYU=100;}else{$VSLVKYU=$VS_VALUES[29];}

	&vabattle6_1;

#レベルによる補助、お金減算
	$PL_In[2]=int($PL_In[2]*1.5) if $PL_VALUES[29] < 100;
	$VS_In[2]=int($VS_In[2]*1.5) if $VS_VALUES[29] < 100;
#ダウジングロッド
	if (($PL_sB[7] =~ m/!6n/ || $PL_sC[7] =~ m/!6n/ || $PL_sD[7] =~ m/!6n/) && $PL_CLASS[17] =~ m/!1|!E007|!E008/){
		$PL_In[2]=int($PL_In[2]*2);
	}

#ヒーリングプラス
	if($PL_W[7] =~ m/!76/ && $PL_CLASS[17] =~ m/!p/){

#			#対象人数によって、回復量を変動
#			#カウントする
#			$HealerCount = 0;
#			&DBM_INPORT(P);
#			while (my($key,$val) = each %P){
#				@VALS = split(/\s/,$val);
#				if($VS_VALUES[5] eq $VALS[5] && $VS_VALUES[28] eq $VALS[28]){
#					$HealerCount = $HealerCount + 1;
#				}
#			}

#			if($HealerCount >= 21){
#				$Pl_AttPoint = int($Pl_AttPoint * 0.1);
#			}elsif($HealerCount <= 20 && $HealerCount >= 16){
#				$Pl_AttPoint = int($Pl_AttPoint * 0.2);
#			}elsif($HealerCount <= 15 && $HealerCount >= 11){
#				$Pl_AttPoint = int($Pl_AttPoint * 0.4);
#			}elsif($HealerCount <= 10 && $HealerCount >= 6){
#				$Pl_AttPoint = int($Pl_AttPoint * 0.7);
#			}

			#自分と選択相手はここで回復
			if($PL_VALUES[25] ne "1"){
				$PL_VALUES[15]+=int($Pl_AttPoint);
				if($PL_VALUES[15] >= $PL_VALUES[16]){
					$PL_VALUES[15] = $PL_VALUES[16];
				}
			}
##			if($VS_VALUES[25] ne "1"){
#				$VS_VALUES[15]+=int($Pl_AttPoint);
#				if($VS_VALUES[15] >= $VS_VALUES[16]){
#					$VS_VALUES[15] = $VS_VALUES[16];
#				}
#			}
			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				@NP_CLASS=split(/\,/,$VCLASS_LIST{"$NP_VALS[4]"});
				if($VS_VALUES[5] eq $NP_VALS[5] && ($VS_VALUES[28] eq $NP_VALS[28])){

					&REPAIR(\@NP_VALS);

					if($NP_VALS[25] ne "1" && $NP_CLASS[17] !~ m/!E004/){

						$NP_VALS[15]+=int($Pl_AttPoint);
						$NP_VALS[1]="$DATE!$PL_VALUES[3]はヒーリングプラスを行使！";

						if($NP_VALS[15] >= $NP_VALS[16]){
							$NP_VALS[15] = $NP_VALS[16];
						}

						dbmopen (%P,"$DBM_P",0666);
							$P{"$key"}="@NP_VALS";
#							$V{"$key"}="@NP_VALS" if !$FORM{'yousai'};
						dbmclose %P;

					}
				}

			}

		$ResultTag.="ヒーリングプラス！$VS_VALUES[3]の所属する部隊全員のHPが回復します<br>";
#		$PL_VALUES[17] = $PL_VALUES[18];
	}

#ネクロマンシー
	require "./$LOG_FOLDER/$CLASS_DATA";

	if($PL_W[7] =~ m/!77/ && $PL_CLASS[17] =~ m/!E003/){
			#自分と選択相手はここで復活
			if($PL_CLASS[17] =~ m/!E004/){
#				$PL_VALUES[15]=$PL_VALUES[16];
#				$PL_VALUES[25]=0;
			}
			if($VS_CLASS[17] =~ m/!E004/){
				$VS_VALUES[15]=$VS_VALUES[16];
				$VS_VALUES[25]=0;
			}


			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				@NP_CLASS=split(/\,/,$VCLASS_LIST{"$NP_VALS[4]"});

#				if($VS_VALUES[5] eq $NP_VALS[5] && ($VS_CLASS[17] =~ m/!E004/ && $NP_CLASS[17] =~ m/!E004/)){
				if($VS_VALUES[5] eq $NP_VALS[5] && ($NP_CLASS[17] =~ m/!E004/)){
					$NP_VALS[15]=$NP_VALS[16];
					$NP_VALS[25]=0;

					dbmopen (%P,"$DBM_P",0666);
						$P{"$key"}="@NP_VALS";
						$V{"$key"}="@NP_VALS" if !$FORM{'yousai'};
					dbmclose %P;

				}

			}

		$ResultTag.="ネクロマンシー！$VS_VALUES[3]の所属する国の全てのアンデッドクラスユニットのHPが全回復します<br>"
	}

#貢献値加算
	if($NewHoushoFlg == 1){

		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}

		$HC[1] = $HC[1] + 1;
		$HC[2] = $HC[2] + 1;
		#総帥の場合、貢献点+1
		if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 1;}
		
		if($HC[1] > 9999){$HC[1] = 9999;}
		
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

	}

	if($PL_W[7] =~ m/!6s/ || $VS_W[7] =~ m/!6s/){
		$PL_In[2]=int($PL_In[2]/3);
		$VS_In[2]=int($VS_In[2]/3);
	}


	if($HoushoFlg == 1 && ($CL_VALUES[7] > time || $CL_VALUES[37] > time)){

#国チェックが必要
#		if($PL_VALUES[5] && !$PL_VALUES[28]){
			$M_AITEX="$CL_VALUES[6]";
#		}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUES[2]" && $CL_VALUE2[2]){
			$M_AITEX="$CL_VALUES[8]";
#		}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUES[3]" && $CL_VALUE2[3]){
			$M_AITEX="$CL_VALUES[9]";
#		}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUES[4]" && $CL_VALUE2[4]){
			$M_AITEX="$CL_VALUES[10]";
#		}

		&DBM_INPORT(C);
		if (!$C{"$M_AITEX"} || $M_AITEX eq "" || $M_AITEX eq "バルダー装備を崇める会かも"){


		}else{

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
	
			#ヒーリング、ヒーリングオール
			if($PL_W[7] =~ m/!6j|!6k/){
				#現在貢献点+20
				$HC[0] = $HC[0] + 20;
				$HC[2] = $HC[2] + 20;
	
				#自身も総帥の場合+10
				if($PL_VALUES[6] eq "1"){
					#現在貢献点+10
					$HC[0] = $HC[0] + 10;
					$HC[2] = $HC[2] + 10;
				}elsif($PL_VALUES[6] eq "-1"){
				#自身も隊長の場合+5
					#現在貢献点+5
					$HC[0] = $HC[0] + 5;
					$HC[2] = $HC[2] + 5;
				}
	
			#ヒーリングプラス
			}elsif($PL_W[7] =~ m/!76/){
				#現在貢献点+45
				$HC[0] = $HC[0] + 45;
				$HC[2] = $HC[2] + 45;
	
				#自身も総帥の場合+20
				if($PL_VALUES[6] eq "1"){
					#現在貢献点+20
					$HC[0] = $HC[0] + 20;
					$HC[2] = $HC[2] + 20;
				}elsif($PL_VALUES[6] eq "-1"){
				#自身も隊長の場合+12
					#現在貢献点+12
					$HC[0] = $HC[0] + 12;
					$HC[2] = $HC[2] + 12;
				}
	
			#リザレクション
			}elsif($PL_W[7] =~ m/!6l/){
				#現在貢献点+45
				$HC[0] = $HC[0] + 80;
				$HC[2] = $HC[2] + 80;
	
				#自身も総帥の場合+40
				if($PL_VALUES[6] eq "1"){
					#現在貢献点+40
					$HC[0] = $HC[0] + 40;
					$HC[2] = $HC[2] + 40;
				}elsif($PL_VALUES[6] eq "-1"){
				#自身も隊長の場合+20
					#現在貢献点+20
					$HC[0] = $HC[0] + 20;
					$HC[2] = $HC[2] + 20;
				}
			#ネクロマンシー
			}elsif($PL_W[7] =~ m/!77/){
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
	
			#現在貢献点＞最大貢献点の場合は記録
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
	
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

	}

	$PL_In[2]=10 if $PL_In[2]<10;
	$VS_In[2]=10 if $VS_In[2]<10;
	$PL_VALUES[0]+=$PL_In[1];
	$VS_VALUES[0]+=$VS_In[1];
	$PL_VALUES[8]+=$PL_In[2];
	$VS_VALUES[8]+=$VS_In[2];
	$PL_VALUES[14]=100 if $PL_VALUES[14]>100;
	$PL_VALUES[0]=0   if $PL_VALUES[0] < 0;
	$PL_VALUES[0]=215 if $PL_VALUES[0] >= 215;
	$PL_VALUES[0]=220 if $PL_VALUES[6] == 1;
	$VS_VALUES[0]=0   if $VS_VALUES[0] < 0;
	$VS_VALUES[0]=215 if $VS_VALUES[0] >= 215;
	$VS_VALUES[0]=220 if $VS_VALUES[6] == 1;
	$PL_VALUES[17]-=$PL_W[4] if $Pl_Times;
	$PL_VALUES[17]-=int($PL_W[4]/5) if $Pl_Times == 0;
	$PL_VALUES[17]=0 if $PL_VALUES[17] < 0;
	$Pl_vs="$VS_VALUES[5]の"if $VS_VALUES[5];$Pl_vs="$NONE_NATIONALITYの"if !$VS_VALUES[5];
	$Vs_vs="$PL_VALUES[5]の"if $PL_VALUES[5];$Vs_vs="$NONE_NATIONALITYの"if !$PL_VALUES[5];
	$PL_VALUES[1]="$DATE!$Pl_vs$FORM{'vsname'}と交戦。";$PL_VALUES[26]=time;
	$VS_VALUES[1]="$DATE!$Vs_vs$FORM{'pname'}と交戦。";
	($ResultTag.="$VS_VALUES[3]&nbsp;撃破。<br>",$PL_VALUES[1].="$VS_VALUES[3]&nbsp;撃破。",$VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。")	if $ResultBattle==0;
	($ResultTag.="$PL_VALUES[3]&nbsp;戦闘不\能\。<br>",$PL_VALUES[1].="$PL_VALUES[3]&nbsp;戦闘不\能\。",$VS_VALUES[1].="$PL_VALUES[3]&nbsp;撃破。")	if $ResultBattle==1;
	($PL_VALUES[1].="[ON狩り]",$VS_VALUES[1].="[被ON狩り]")if $PONGARI==1;

	&HEADER;

	if($PL_VALUES[27]>=700){$PSIZE='72';}else{$PSIZE='64';}
	if($VS_VALUES[27]>=700){$VSIZE='72';}else{$VSIZE='64';}
	$PIMAGE="$IMG_FOLDER2/$PL_VALUES[27].gif";
	$VIMAGE="$IMG_FOLDER2/$VS_VALUES[27].gif";
	if($PL_VALUES[36]==1){$PIMAGE="$IMG_FOLDER5/$PL_CLASS[18]";$PSIZE='64';}
	if($VS_VALUES[36]==1){$VIMAGE="$IMG_FOLDER5/$VS_CLASS[18]";$VSIZE='64';}

#メンテ時は詳細表示
	if($MENTE==1){
		$phyouji="<br><font color=#73652b>ATK=$test_Pl_AtPoint(STR1+$PL_agD STR2+$PL_agD2 STR3+$PL_agDD3) DEF=$Pl_DefPoint(RES1+$PLCSS RES2+$PLBSS RES3+$PLDDSS) AGI=$Pl_SpPoint(AGI1+$PLFP AGI2+$PLGP AGI3+$PLDDP) DEX=$test_Pl_Check(DEX1+$PL_mei DEX2+$PL_mei2 DEX3+$PL_mei3) Ini=$Pl_Ini</font>";
		$vhyouji="<br><font color=#73652b>ATK=$test_Vs_AtPoint(STR1+$VS_agD STR2+$VS_agD2 STR3+$VS_agDD3) DEF=$Vs_DefPoint(RES1+$VSCSS RES2+$VSBSS RES3+$VSDDSS) AGI=$Vs_SpPoint(AGI1+$VSFP AGI2+$VSGP AGI3+$VSDDP) DEX=$test_Vs_Check(DEX1+$VS_mei DEX2+$VS_mei2 DEX3+$VS_mei3) Ini=$Vs_Ini</font>";
	}

	print << "	-----END-----";
	<div align=center>

	<table border=0 bgcolor=#000000 width=100% cellspacing=0 cellpadding=0>
	<tr><td align=center width=50% bgcolor="$CL_VALUES[0]" style="color:#000000;font-size:25pt;">
		<b>$PL_Country</b></td>
		<td align=center width=50% bgcolor="$VC_VALUES[0]" style="color:#000000;font-size:25pt;">
		<b>$VS_Country</b></td></tr>
	<tr><td align=center width=50%><font color=$PL_VALUES[13] style="font-size:18pt;">$PL_VALUES[3]</font><br>
		<div style="font-size:15px;">（$FORM{'pname'}$Pl_Kaikyu）</div></td>
		<td align=center width=50%><font color=$VS_VALUES[13] style="font-size:18pt;">$VS_VALUES[3]</font><br>
		<div style="font-size:15px;">（$FORM{'vsname'}$Vs_Kaikyu）</div></td></tr>
	<tr><td align=center width=50% height=100 valign=bottom>
		<div align=center><img src=\"$PIMAGE\" width=\"$PSIZE\" height=\"$PSIZE\"></div>
		<font color=#997788 style="font-size:12px;">$PL_CLASS[0]</font>
		<div style="font-size:15px;">【$Pl_MsnStyle】</div>
		<table $TBL_TAG1><tr><td style="font-size:15px;"><b>HP</b>&nbsp;</td>
			<td>$PL_HPTAG</td><td width=50 align=right style="font-size:14px;"><span id=cplhp>$Pl_BfrHP</span></td>
			<td style="font-size:14px;">/<b>$PL_VALUES[16]</b></td></tr></table></td>
	<td align=center width=50% height=100 valign=bottom>
		<div align=center><img src=\"$VIMAGE\" style=\"filter:fliph();\" width=\"$VSIZE\" height=\"$VSIZE\"></div>
		<font color=#997788 style="font-size:12px;">$VS_CLASS[0]</font>
		<div style="font-size:15px;">【待機中】</div>
		<table $TBL_TAG1><tr><td style="font-size:15px;"><b>HP</b>&nbsp;</td>
			<td>$VS_HPTAG</td><td width=50 align=right style="font-size:14px;"><span id=cvshp>$Vs_BfrHP</span></td>
			<td style="font-size:14px;">/<b>$VS_VALUES[16]</b></td></tr></table></td></tr>
	<tr><td align=center valign=top width=40%><font color=#778899 style="font-size:16px;"><b>$PL_WeaponNameA</b>
			<font style="font-size:12px;"><b>$PL_ShieldNameA</b></font></font><div align=center>$PlsumDmg<br>
			<b style="font-size:12px;color:#dc143c;">$STATUS_NAME[5]:-$PL_W[4]$phyouji</b></div></td>
			<td align=center valign=top width=40%><font color=#778899 style="font-size:16px;"><b>$VS_WeaponNameA</b>
			<font style="font-size:12px;"><b>$VS_ShieldNameA</b></font></font><div align=center>$VssumDmg<br>
			</div></td></tr></table>
	<div style="line-height:4pt;">&nbsp;</div>
		<table><tr><td bgcolor=#000000 style="line-height:18px;font-size:14px;">
	-----END-----
		if ($PONGARI){
		print "<table><tr><td><font color=#cb0881><b>从‘　。‘从☆ <font size=150%>ON狩り</font> （‘◇‘☆彡</b><br>！！カウント$PL_VALUES[33]！！</font></td></tr></table><br>\n";
		}
		print "$ResultTag";
##battle_result
	print << "	-----END-----";
	<script language="JavaScript">
	timeID=10;var timID;
		cdplhp=Math.round(($Pl_BfrHP-$PL_VALUES[15])*0.1);
		cdvshp=Math.round(($Vs_BfrHP-$VS_VALUES[15])*0.1);
		flaga=flagb=flagc=0;
		setTimeout(\"HEcount()\",2500);
	function HEcount(){
		cplhp.innerText-=cdplhp;
		cvshp.innerText-=cdvshp;
		if (eval(cplhp.innerText) <= $PL_VALUES[15]){cplhp.innerText='$PL_VALUES[15]';flaga=1;}
		if (eval(cvshp.innerText) <= $VS_VALUES[15]){cvshp.innerText='$VS_VALUES[15]';flagb=1;}
		clearTimeout(timeID);
		if (!flaga || !flagb){timeID = setTimeout(\"HEcount()\",1);}
	}
	function kikan(ms){s = ms;clearTimeout(timID);
		if(s>0){s--;timID=setTimeout('kikan(s)',1000);}else{go.gogo.click();}
	}
	</script>
	-----END-----
	$Ch_rank=&RANK($PL_VALUES[0],$PL_VALUES[5],$PL_VALUES[6]);
	if($Ch_rank ne $Pl_Kaikyu && $Ch_rank){
		print "$FORM{'pname'}は、$Ch_rankに";
		print $PL_In[1] > 0 ? "昇格<br>":$PL_In[1] < 0 ? "降格<br>":"<br>";
	}
	$Ch_rank=&RANK($VS_VALUES[0],$VS_VALUES[5],$VS_VALUES[6]);
	if($Ch_rank ne $Vs_Kaikyu && $Ch_rank){
		print "$FORM{'vsname'}は、$Ch_rankに";
		print $VS_In[1] > 0 ? "昇格<br>":$VS_In[1] < 0 ? "降格<br>":"<br>";
	}

	if($PL_VALUES[5] ne ""){$PL_In[4]=$PL_In[0]*($VS_VALUES[0]+1)+($PL_VALUES[0]*2+1);}else{$PL_In[4]=$PL_In[0]*($VS_VALUES[0]+1);}
	if($PL_W[7] =~ m/!12|!13|!14|!15|!16|!17|!1c|!1m|!1n|!1s|!1t|!1u|!1v|!1w|!1x|!64|!65|!66|!67|!68|!69|!6b|!6c|!za|!zb/ || $VS_W[7] =~ m/!12|!13|!14|!15|!16|!17|!1c|!1m|!1n|!1s|!1t|!1u|!1v|!1w|!1x|!6b|!6c|!za|!zb/){$PL_In[4]=int($PL_In[4]/2);}
	$PL_VALUES[30]+=$PL_In[4];
	print "$FORM{'pname'} は $PL_In[4] の経験値を獲得<br>";
#	$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
#	$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;

	if (($PL_VALUES[29]+1)*200 <= $PL_VALUES[30]){&BATTLE_3;}
#	&BATTLE_3;

	&vabattle7;

	&vabattle8;

	&vabattle9;
}

1;

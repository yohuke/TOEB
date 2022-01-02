sub BATTLE1{
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
	&REPAIR(\@PL_VALUES);
	&ERROR("$NONE_NATIONALITYでは内乱できません。") if $FORM{'b_mode'} eq '内乱' && !$PL_VALUES[5];
#	&ERROR("レベル50以上のユニットは$NONE_NATIONALITYでは戦闘できません。国を興すかどこかに亡命しましょう！") if ($FORM{'b_mode'} eq '戦闘' && !$PL_VALUES[5] && $PL_VALUES[29]>49 && ($WW_FRAG==0 && $HIZUK_FRAG==0));
#	&ERROR("レベル50以上のユニットは$NONE_NATIONALITYでは戦闘できません。国を興すかどこかに亡命しましょう！") if ($FORM{'b_mode'} eq '戦闘' && !$PL_VALUES[5] && $PL_VALUES[29]>49);
	&ERROR('隊長、総帥ランクは内乱できません。') if $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6]!=0;
	&ERROR('すいみんちゅう') if($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i) && ($PL_VALUES[4] =~ /^64$|^65$/i);

	&HEADER;
	require "./$LOG_FOLDER/$HASH_DATA";
	require "./$LOG_FOLDER/$ABI_DATA";
	if($AbiSys == 1){
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});
	}
	
#	local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
#	local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#	@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
#	local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#	@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
#	local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);
#	@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});
#	local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
#	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
#	local($WN_T,$WLV_T) = split(/!/,$PL_VALUES[42]);
#	@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
#	local($WN_U,$WLV_U) = split(/!/,$PL_VALUES[43]);
#	@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});

	local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);
	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
	local($WN_B,$WLV_B,$WBEnt,$WB03,$WB04,$WB05,$WB06,$WB07,$WB08,$WB09,$WB10,$WB11,$WB12,$WB13,$WB14,$WB15,$WB16,$WB17,$WB18,$WB19,$WB20,$WB21,$WB22,$WB23,$WB24,$WB25,$WB26,$WB27,$WB28,$WB29,$WB30,$WB31,$WB32,$WB33,$WB34,$WB35,$WB36,$WB37,$WB38,$WB39,$WB40,$WB41,$WB42) = split(/!/,$PL_VALUES[10]);
	@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
	local($WN_C,$WLV_C,$WCEnt,$WC03,$WC04,$WC05,$WC06,$WC07,$WC08,$WC09,$WC10,$WC11,$WC12,$WC13,$WC14,$WC15,$WC16,$WC17,$WC18,$WC19,$WC20,$WC21,$WC22,$WC23,$WC24,$WC25,$WC26,$WC27,$WC28,$WC29,$WC30,$WC31,$WC32,$WC33,$WC34,$WC35,$WC36,$WC37,$WC38,$WC39,$WC40,$WC41,$WC42) = split(/!/,$PL_VALUES[11]);
	@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
	local($WN_D,$WLV_D,$WDEnt,$WD03,$WD04,$WD05,$WD06,$WD07,$WD08,$WD09,$WD10,$WD11,$WD12,$WD13,$WD14,$WD15,$WD16,$WD17,$WD18,$WD19,$WD20,$WD21,$WD22,$WD23,$WD24,$WD25,$WD26,$WD27,$WD28,$WD29,$WD30,$WD31,$WD32,$WD33,$WD34,$WD35,$WD36,$WD37,$WD38,$WD39,$WD40,$WD41,$WD42) = split(/!/,$PL_VALUES[38]);
	@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});
	local($WN_S,$WLV_S,$WSEnt) = split(/!/,$PL_VALUES[41]);
	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
	local($WN_T,$WLV_T,$WTEnt) = split(/!/,$PL_VALUES[42]);
	@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
	local($WN_U,$WLV_U,$WUEnt) = split(/!/,$PL_VALUES[43]);
	@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});
##クラス読み込み
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

	if($FORM{'nowt'} eq ""){$FORM{'nowt'}=$FORM{'ntim'};}
	$NowTime = $FORM{'nowt'};
#	$mod=$FORM{'b_mode'};
	($PL_VALUES[17] < $WN_sA[4] || $PL_VALUES[25]==1 || (!$C{"$PL_VALUES[5]"} && $PL_VALUES[5] ne "")) && do{print "$STATUS_NAME[5]が足りないか、戦闘不\能\中です。\n";
	print "<table border=1 bordercolor=#333333 cellspacing=0>\n";
	print "<form action=$MAIN_SCRIPT method=POST target=Main>\n";
	print "<input type=hidden name=cmd value=MAIN_FRAME>\n";
	print "<input type=hidden name=pname value=$FORM{'pname'}>\n";
	print "<input type=hidden name=pass value=$FORM{'pass'}><tr><td bgcolor=#000000>\n";
	print "<b $chaStyl>&nbsp;</b><br>\n";
	print "<input type=submit value=\"更新\" onClick=\"parent.Sub.location.replace(\'$BACKFR\');\">\n";
	print "</td></form></table>\n";exit;};


	@pair = split(/;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	if($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復'){
#		@MISSION=('通常攻撃,0','ダブルアタック,70');
		@MISSION=('通常攻撃,0,1','突撃,99999,1','防御,99999,1','ヒットアンドアウェイ,99999,1',
					'狙撃,99999,1','捨て身,99999,1','見切り,99999,1','ダブルアタック,70,1','速攻,99999,80','大防御,99999,50','大防御,99999,51','大防御,99999,216');
	}else{
		@MISSION=('通常攻撃,0,1','突撃,5,1','防御,18,1','ヒットアンドアウェイ,25,1',
					'狙撃,30,1','捨て身,40,1','見切り,50,1','ダブルアタック,70,1','速攻,99999,80','大防御,99999,50','大防御,99999,51','大防御,99999,216');
	}
	$Sakusen="作戦<select size=1 name=\"mode\">\n";
	foreach (@MISSION){$c++;
		my($M,$R,$R2)=split(/\,/,$_);
		if($PL_VALUES[29] >= $R){
			$Sakusen .= "<option value=\"$c\"";
			$Sakusen .= "selected"if $c ==  $DUMMY{' EBMISSON'};
			$Sakusen .= ">$M \n";
		}
		if($PL_VALUES[4] == $R2 && $R2 != 1){
			$Sakusen .= "<option value=\"$c\"";
			$Sakusen .= "selected"if $c ==  $DUMMY{' EBMISSON'};
			$Sakusen .= ">$M \n";
		}
	}

#&ERROR("$DUMMY{' EBMISSON2'}あ$FORM{'b_mode'}x$FORM{'c_mode'}a$DUMMY{' EBMISSON'}ああ","@pair");
#&ERROR("$WN_sCS[0]");
if($FORM{'c_mode'} eq ""){$FORM{'c_mode'} = $FORM{'b_mode'};}
#if($FORM{'b_mode'} eq ""){&ERROR("$FORM{'b_mode'}xxx$FORM{'c_mode'}");}

	$Sakusen .= "</select>";
	$Toksen="特殊選択<select size=1 name=\"sentaku\" $STYLE_L>\n";
	if($FORM{'b_mode'} ne '回復' && $FORM{'c_mode'} ne '回復'){
		$Toksen .="<option value=0>なし</option>";
	}
	if($WN_sS[0] && ($WN_sS[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		$Toksen .= "<option value=41 ";
		$Toksen .= "selected"if 41 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sS[0]</option>";
	}
	if($WN_sS[0] && (($WN_sS[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sS[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sS[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		$Toksen .= "<option value=41 ";
		$Toksen .= "selected"if 41 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sS[0]</option>";
	}
	if($WN_sT[0] && ($WN_sT[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		$Toksen .= "<option value=42 ";
		$Toksen .= "selected"if 42 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sT[0]</option>";
	}
	if($WN_sT[0] && (($WN_sT[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sT[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sT[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		$Toksen .= "<option value=42 ";
		$Toksen .= "selected"if 42 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sT[0]</option>";
	}
	if($WN_sU[0] && ($WN_sU[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		$Toksen .= "<option value=43 ";
		$Toksen .= "selected"if 43 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sU[0]</option>";
	}
	if($WN_sU[0] && (($WN_sU[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sU[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sU[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		$Toksen .= "<option value=43 ";
		$Toksen .= "selected"if 43 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sU[0]</option>";
	}
	if($WN_sA[13] && ($WN_sA[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sA[13]"});
		$Toksen .= "<option value=9 ";
		$Toksen .= "selected"if 9 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sA[0] && (($WN_sA[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sA[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sA[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sA[13]"});
		$Toksen .= "<option value=9 ";
		$Toksen .= "selected"if 9 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sB[13] && ($WN_sB[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sB[13]"});
		$Toksen .= "<option value=10 ";
		$Toksen .= "selected"if 10 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sB[0] && (($WN_sB[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sB[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sB[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sB[13]"});
		$Toksen .= "<option value=10 ";
		$Toksen .= "selected"if 10 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sC[13] && ($WN_sC[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sC[13]"});
		$Toksen .= "<option value=11 ";
		$Toksen .= "selected"if 11 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sC[0] && (($WN_sC[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sC[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sC[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sC[13]"});
		$Toksen .= "<option value=11 ";
		$Toksen .= "selected"if 11 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sD[13] && ($WN_sD[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sD[13]"});
		$Toksen .= "<option value=38 ";
		$Toksen .= "selected"if 38 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	if($WN_sD[0] && (($WN_sD[7] =~ m/!6j|!6k|!76/ && $ALY_CLASS[17]=~ m/!p/) || ($WN_sD[7] =~ m/!77/ && $ALY_CLASS[17]=~ m/!E003/) || ($WN_sD[7] =~ m/!6l/ && $ALY_CLASS[17]=~ m/!q/)) && ($FORM{'c_mode'} eq '回復' || $FORM{'b_mode'} eq '回復')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$WN_sD[13]"});
		$Toksen .= "<option value=38 ";
		$Toksen .= "selected"if 38 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	#クラス固有技　防具を最上段にしている場合、使用不可
	if($WN_sA[1] > 20 && $WN_sCS[0] && ($WN_sCS[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[22]"});
		$Toksen .= "<option value=44 ";
		$Toksen .= "selected"if 44 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc[0]</option>";
	}
	#クラス固有技　防具を最上段にしている場合、使用不可
	if($WN_sA[1] > 20 && $WN_sCS2[0] && ($WN_sCS2[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc2=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[23]"});
		$Toksen .= "<option value=45 ";
		$Toksen .= "selected"if 45 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc2[0]</option>";
	}
	#クラス固有技　防具を最上段にしている場合、使用不可
	if($WN_sA[1] > 20 && $WN_sCS3[0] && ($WN_sCS3[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc3=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[24]"});
		$Toksen .= "<option value=46 ";
		$Toksen .= "selected"if 46 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc3[0]</option>";
	}
	#クラス固有技　防具を最上段にしている場合、使用不可
	if($WN_sA[1] > 20 && $WN_sCS4[0] && ($WN_sCS4[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc4=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[25]"});
		$Toksen .= "<option value=47 ";
		$Toksen .= "selected"if 47 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc4[0]</option>";
	}
	#クラス固有技　防具を最上段にしている場合、使用不可
	if($WN_sA[1] > 20 && $WN_sCS5[0] && ($WN_sCS5[7] !~ m/!6j|!6k|!6l|!76|!77|!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r|!8s|!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
		@WN_sCalc5=split(/\,/,$WEAPON_LIST{"$ALY_CLASS[26]"});
		$Toksen .= "<option value=48 ";
		$Toksen .= "selected"if 48 eq $DUMMY{' EBMISSON2'};
		$Toksen .= ">$WN_sCalc5[0]</option>";
	}

	#合成魔法(攻撃)
	if($ALY_CLASS[17] =~ m/!E011/){
		@Gousei=();@GouseiLv=();$GouseiCount=0;
	
	
		if($WN_sA[7] =~ m/!E0008/){

			if($WN_sB[7] =~ m/!E0008/){

				#風
				if($WN_sA[7] =~ m/!00/){
				
					#風と風
					if($WN_sB[7] =~ m/!00/){
						#合計Lv20以上　ライトニング
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbba";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}
						#合計Lv120以上　サンダーフレア
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbb";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}						
					#風と炎
					}elsif($WN_sB[7] =~ m/!01/){
						#合計Lv20以上　プラズマボール
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbk";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}
						#合計Lv120以上　プラズマストーム
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbl";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}											
					#風と水
					}elsif($WN_sB[7] =~ m/!03/){
						#合計Lv20以上　イオノスフィア
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbm";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}
						#合計Lv120以上　アトモスフィア
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbn";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}											
					#風と闇
					}elsif($WN_sB[7] =~ m/!05/){
						#合計Lv20以上　インフェスト
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbq";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}
						#合計Lv120以上　インフェルノ
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbr";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}											
					}

				#炎
				}elsif($WN_sA[7] =~ m/!01/){
					#炎と炎
					if($WN_sB[7] =~ m/!00/){
						#合計Lv20以上　ファイアボール
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbk";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}
						#合計Lv120以上　ファイアストーム
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbl";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}											
					#炎と風
					}elsif($WN_sB[7] =~ m/!00/){
						#合計Lv20以上　プラズマボール
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbk";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}
						#合計Lv120以上　プラズマストーム
						if(($WLV_A + $WLV_B) >= 20){$Gousei[$GouseiCount] = "rbbl";$GouseiLv[$GouseiCount]=0;$GouseiCount++;}											
					}
				}

			}
		
		}
	
	}

#$ALY_CLASS[17]
	$Toksen .= "</select>";

	if($ALY_CLASS[17] =~ m/!E001/){
		$HoSen="補助魔法選択<select size=1 name=\"Hosentaku\" $STYLE_L>\n";
		if($FORM{'b_mode'} ne '回復' && $FORM{'c_mode'} ne '回復'){
			$HoSen .="<option value=0>なし</option>";
		}
		#補助魔法1
		if($ALY_CLASS[17] =~ m/!E001/ && $WN_sS[0] && ($WN_sS[7] =~ m/!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
			$HoSen .= "<option value=41 ";
			$HoSen .= "selected"if 41 eq $DUMMY{' EBMISSON3'};
			$HoSen .= ">$WN_sS[0]</option>";
		}
		#補助魔法2
		if($ALY_CLASS[17] =~ m/!E001/ && $WN_sT[0] && ($WN_sT[7] =~ m/!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
			$HoSen .= "<option value=42 ";
			$HoSen .= "selected"if 42 eq $DUMMY{' EBMISSON3'};
			$HoSen .= ">$WN_sT[0]</option>";
		}
		#補助魔法3
		if($ALY_CLASS[17] =~ m/!E001/ && $WN_sU[0] && ($WN_sU[7] =~ m/!8k|!8l|!8m|!8n|!8o|!8p|!8q|!8r/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
			$HoSen .= "<option value=43 ";
			$HoSen .= "selected"if 43 eq $DUMMY{' EBMISSON3'};
			$HoSen .= ">$WN_sU[0]</option>";
		}
		$HoSen .= "</select>";

	}elsif($ALY_CLASS[17] =~ m/!E013/){
		$HoSen="補助魔法選択<select size=1 name=\"Hosentaku\" $STYLE_L>\n";
		if($FORM{'b_mode'} ne '回復' && $FORM{'c_mode'} ne '回復'){
			$HoSen .="<option value=0>なし</option>";
		}
		#神聖系補助魔法1
		if($ALY_CLASS[17] =~ m/!E013/ && $WN_sS[0] && ($WN_sS[7] =~ m/!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
			$HoSen .= "<option value=41 ";
			$HoSen .= "selected"if 41 eq $DUMMY{' EBMISSON3'};
			$HoSen .= ">$WN_sS[0]</option>";
		}
		#神聖系補助魔法2
		if($ALY_CLASS[17] =~ m/!E013/ && $WN_sT[0] && ($WN_sT[7] =~ m/!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
			$HoSen .= "<option value=42 ";
			$HoSen .= "selected"if 42 eq $DUMMY{' EBMISSON3'};
			$HoSen .= ">$WN_sT[0]</option>";
		}
		#神聖系補助魔法3
		if($ALY_CLASS[17] =~ m/!E013/ && $WN_sU[0] && ($WN_sU[7] =~ m/!8w/) && ($FORM{'c_mode'} eq '戦闘' || $FORM{'c_mode'} eq '内乱' || $FORM{'c_mode'} eq '亡命' || $FORM{'c_mode'} eq '探求' || $FORM{'b_mode'} eq '戦闘' || $FORM{'b_mode'} eq '内乱' || $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '探求')){
			$HoSen .= "<option value=43 ";
			$HoSen .= "selected"if 43 eq $DUMMY{' EBMISSON3'};
			$HoSen .= ">$WN_sU[0]</option>";
		}

		$HoSen .= "</select>";
	}else{
		$HoSen = "";
	}



	$battle="BATTLE_2";

	$NPC1 ="バランスの集い";
	$NPC2 ="メルト屋愛好会";

	$TESNAME ="1F";

	print "<span style=\"font-size:35px;\">$FORM{'b_mode'}</span>" if $FORM{'b_mode'} ne '戦闘';

	if ($FORM{'b_mode'} eq '戦闘' ||!$FORM{'b_mode'}){
		print << "		-----END-----";
		<script language="JavaScript">
		var timID;
		function cota(na,ma){fma.CNTRY.value=na;c=1;kikan(ma);}
		function cotb(nb,mb){fmb.CNTRY.value=nb;c=2;kikan(mb);}
		function kikan(ms){s = ms;clearTimeout(timID);
		if(s>0){s--;timID=setTimeout('kikan(s)',1000);}else if(c==1){fma.goa.click();}else if(c==2){fmb.gob.click();}
		}
		</script>


		-----END-----
#			<b style="font-size:13px;">$CONTINENT_A</b><br>
#			<b style="font-size:13px;">$CONTINENT_C</b><br>
		if($PL_VALUES[5]){&DBM_CONVERT('C',"$PL_VALUES[5]");$JIKANSA=$CL_VALUES[13];$JIKANSA=15 if $CL_VALUES[13]>14;
			if($CL_VALUES[7] > time){$HATUDO1="$CL_VALUES[6]";$HATUDO2="$CL_VALUES[8]";$HATUDO3="$CL_VALUES[9]";$HATUDO4="$CL_VALUES[10]";}
		}

#Back処理対策
		$CalcDate = time;

#シャングリラ
		foreach my $C_Name ( sort keys %C ) {
			@C_VALUES = split(/\s/,$C{$C_Name});
			$C_VALUES[14]=0 if !$C_VALUES[14];$C_VALUES[13]=0 if !$C_VALUES[13];$V_JIKANSA=$C_VALUES[13];$V_JIKANSA=15 if $C_VALUES[13]>14;
#$WW_FRAG==1 && $HIZUK_FRAG==1
#			if ($C_VALUES[39] eq "1"){
				if($HATUDO1 eq "$C_Name" || $HATUDO2 eq "$C_Name" || $HATUDO3 eq "$C_Name" || $HATUDO4 eq "$C_Name"){$MORATRI=1;}else{$MORATRI=0;}

				if($PL_VALUES[5] ne "$C_Name" && $WW_FRAG==1 && $HIZUK_FRAG==1){
					if($FORM{'CNTRY'} eq "$C_Name"){$RLO='0';}else{$RLO='0';}
					print "<input type=submit value=\"$C_Name\"";
					print "onClick=\"cota('$C_Name','$RLO');\" style=\" background:$C_VALUES[0];color:black\">\n";
#					print " style=\" background:$C_VALUES[0];color:black\">\n";

#				if ($PL_VALUES[5] ne "$C_Name" && $CVALS[49] ne "$C_Name"){
#					print "<input type=submit name=CNTRY value=\"$C_Name\"";
#					print " style=\" background:$C_VALUES[0];color:black\">\n";
#				}


				}elsif ($PL_VALUES[5] ne "$C_Name" && ($C_VALUES[14]+$V_JIKANSA*60) <= time && ($CL_VALUES[7] > time && (($CL_VALUES[14]+$JIKANSA*60) <= time && $MORATRI==1 || $C_VALUES[7] <= time && $MORATRI==0) || $C_VALUES[7] <= time && $CL_VALUES[7] <= time || ($CL_VALUES[14]+$JIKANSA*60) <= time && $C_VALUES[7] > time && $PL_VALUES[5] ne '' && ($PL_VALUES[5] eq "$C_VALUES[6]" || $PL_VALUES[5] eq "$C_VALUES[8]" || $PL_VALUES[5] eq "$C_VALUES[9]" || $PL_VALUES[5] eq "$C_VALUES[10]"))){
					if($FORM{'CNTRY'} eq "$C_Name"){$RLO='0';}else{$RLO='0';}
					print "<input type=submit value=\"$C_Name\"";
					print "onClick=\"cota('$C_Name','$RLO');\" style=\" background:$C_VALUES[0];color:black\">\n";
#					print " style=\" background:$C_VALUES[0];color:black\">\n";
				}
#			}

		}

		print "<input type=submit value=\"$NONE_NATIONALITY\"";
		print "onClick=\"cota('$NONE_NATIONALITY','0');\" style=\" background:#808080;color:black\">\n";
		print "<input type=submit value=\"$NPC1\"";
		print "onClick=\"cota('$NPC1','0');\" style=\" background:#ffdddd;color:black\">\n";
		print "<input type=submit value=\"$NPC2\"";
		print "onClick=\"cota('$NPC2','0');\" style=\" background:#ffdddd;color:black\">\n";

##ゼテギネア大陸
#		while (($C_Name,$C_Value) =each %C) {
#			@C_VALUES = split(/\s/,$C_Value);
#			$C_VALUES[14]=0 if !$C_VALUES[14];$C_VALUES[13]=0 if !$C_VALUES[13];$V_JIKANSA=$C_VALUES[13];$V_JIKANSA=30 if $C_VALUES[13]>29;
#
#			if ($C_VALUES[39] eq "1"){
#				if($HATUDO1 eq "$C_Name" || $HATUDO2 eq "$C_Name" || $HATUDO3 eq "$C_Name" || $HATUDO4 eq "$C_Name"){$MORATRI=1;}else{$MORATRI=0;}
#				if($PL_VALUES[5] ne "$C_Name" && $WW_FRAG==1 && $HIZUK_FRAG==1){
#					if($FORM{'CNTRY'} eq "$C_Name"){$RLO='5';}else{$RLO='2';}
#					print "<input type=submit value=\"$C_Name\"";
#					print "onClick=\"cota('$C_Name','$RLO');\" style=\" background:$C_VALUES[0];color:black\">\n";
#				}elsif ($PL_VALUES[5] ne "$C_Name" && ($C_VALUES[14]+$V_JIKANSA*60) <= time && ($CL_VALUES[7] > time && (($CL_VALUES[14]+$JIKANSA*60) <= time && $MORATRI==1 || $C_VALUES[7] <= time && $MORATRI==0) || $C_VALUES[7] <= time && $CL_VALUES[7] <= time || ($CL_VALUES[14]+$JIKANSA*60) <= time && $C_VALUES[7] > time && $PL_VALUES[5] ne '' && ($PL_VALUES[5] eq "$C_VALUES[6]" || $PL_VALUES[5] eq "$C_VALUES[8]" || $PL_VALUES[5] eq "$C_VALUES[9]" || $PL_VALUES[5] eq "$C_VALUES[10]"))){
#					if($FORM{'CNTRY'} eq "$C_Name"){$RLO='5';}else{$RLO='2';}
#					print "<input type=submit value=\"$C_Name\"";
#					print "onClick=\"cota('$C_Name','$RLO');\" style=\" background:$C_VALUES[0];color:black\">\n";
#				}
#			}
#
#		}
#	
#		print "<input type=submit value=\"$NONE_NATIONALITY\"";
#		print "onClick=\"cota('$NONE_NATIONALITY','3');\" style=\" background:#808080;color:black\">\n";
#		print "<input type=submit value=\"$NPC1\"";
#		print "onClick=\"cota('$NPC1','3');\" style=\" background:#ffdddd;color:black\">\n";
#
##ガリシア大陸
#		print "<br><br><b style=\"font-size:13px;\">$CONTINENT_B</b><br>";
#		while (($C_Name,$C_Value) =each %C) {
#			@C_VALUES = split(/\s/,$C_Value);
#			$C_VALUES[14]=0 if !$C_VALUES[14];$C_VALUES[13]=0 if !$C_VALUES[13];$V_JIKANSA=$C_VALUES[13];$V_JIKANSA=30 if $C_VALUES[13]>29;
#
#			if ($C_VALUES[39] eq "2"){
#				if($HATUDO1 eq "$C_Name" || $HATUDO2 eq "$C_Name" || $HATUDO3 eq "$C_Name" || $HATUDO4 eq "$C_Name"){$MORATRI=1;}else{$MORATRI=0;}
#				if($PL_VALUES[5] ne "$C_Name" && $WW_FRAG==1 && $HIZUK_FRAG==1){
#					if($FORM{'CNTRY'} eq "$C_Name"){$RLO='5';}else{$RLO='2';}
#					print "<input type=submit value=\"$C_Name\"";
#					print "onClick=\"cota('$C_Name','$RLO');\" style=\" background:$C_VALUES[0];color:black\">\n";
#				}elsif ($PL_VALUES[5] ne "$C_Name" && ($C_VALUES[14]+$V_JIKANSA*60) <= time && ($CL_VALUES[7] > time && (($CL_VALUES[14]+$JIKANSA*60) <= time && $MORATRI==1 || $C_VALUES[7] <= time && $MORATRI==0) || $C_VALUES[7] <= time && $CL_VALUES[7] <= time || ($CL_VALUES[14]+$JIKANSA*60) <= time && $C_VALUES[7] > time && $PL_VALUES[5] ne '' && ($PL_VALUES[5] eq "$C_VALUES[6]" || $PL_VALUES[5] eq "$C_VALUES[8]" || $PL_VALUES[5] eq "$C_VALUES[9]" || $PL_VALUES[5] eq "$C_VALUES[10]"))){
#					if($FORM{'CNTRY'} eq "$C_Name"){$RLO='5';}else{$RLO='2';}
#					print "<input type=submit value=\"$C_Name\"";
#					print "onClick=\"cotb('$C_Name','$RLO');\" style=\" background:$C_VALUES[0];color:black\">\n";
#				}
#			}
#
#		}
#	
#		print "<input type=submit value=\"$NONE_NATIONALITY\"";
#		print "onClick=\"cotb('$NONE_NATIONALITY','3');\" style=\" background:#808080;color:black\">\n";
#		print "<input type=submit value=\"$NPC2\"";
#		print "onClick=\"cotb('$NPC2','3');\" style=\" background:#ffdddd;color:black\">\n";
#
$nt = time;

#			<input type=hidden name="cmd" value="BATTLE_2">
#			<input type=hidden name="pname" value="$FORM{'pname'}">
#			<input type=hidden name="pass" value="$FORM{'pass'}">
#			<input type=hidden name="b_mode" value="$FORM{'b_mode'}">
#			<input type=hidden name="check" value="$DATE">
#			<input type=submit value="戦闘" $STYLE_B1 onClick="location.replace('$MAIN_SCRIPT?LOGO');">

		print << "		-----END-----";
			<form action="$MAIN_SCRIPT" method=POST name=fma target=Sub>
			<input type=hidden name="cmd" value="BATTLE_1">
			<input type=hidden name="pname" value="$FORM{'pname'}">
			<input type=hidden name="pass" value="$FORM{'pass'}">
			<input type=hidden name="c_mode" value="$FORM{'c_mode'}">
			<input type=hidden name="ntim" value="$FORM{'nowt'}">
			<input type=hidden name="nt" value="$nt">
			<input type=hidden name="CNTRY">
			<input type=hidden name="con" value="1">
			<input type=submit name="goa" style="display:none;">
			</form>
			<form action="$MAIN_SCRIPT" method=POST name=fmb target=Sub>
			<input type=hidden name="cmd" value="BATTLE_1">
			<input type=hidden name="pname" value="$FORM{'pname'}">
			<input type=hidden name="pass" value="$FORM{'pass'}">
			<input type=hidden name="c_mode" value="$FORM{'c_mode'}">
			<input type=hidden name="ntim" value="$FORM{'nowt'}">
			<input type=hidden name="nt" value="$nt">
			<input type=hidden name="CNTRY">
			<input type=hidden name="con" value="2">
			<input type=submit name="gob" style="display:none;">
			</form>
		-----END-----
	}
#$MAIN_SCRIPT
	if ($FORM{'b_mode'} eq '亡命'){
		$boumeiTag="&nbsp;亡命先<select name=\"boumeiC\">";
		while (($C_Name,$C_Value) =each %C) {
		$CTEMP=0;
		@C_VALUES = split(/\s/,$C_Value);
		$CTEMP=$C_VALUES[7];
#		if ($PL_VALUES[5] ne "$C_Name" && $C_VALUES[7] < time && $C_VALUES[39] eq $PL_VALUES[39]){
		if ($PL_VALUES[5] ne "$C_Name" && $C_VALUES[7] < time){

#		if ($PL_VALUES[5] ne "$C_Name" && $WW_FRAG==1 && $HIZUK_FRAG==1){
			$boumeiTag.="<option value=\"$C_Name\">$C_Name\n";$bf=1;
#		}elsif ($PL_VALUES[5] ne "$C_Name" && $C_VALUES[7] < time){
#			$boumeiTag.="<option value=\"$C_Name\">$C_Name\n";$bf=1;
		}
	}
#		$boumeiTag.="<option value=\"\" selected>$NONE_NATIONALITY\n"if ($PL_VALUES[5] && ($PL_VALUES[29] < 100 || $PL_VALUES[0] < 215) && $PL_VALUES[39] eq "1");
#		$boumeiTag.="<option value=\"\" selected>$NONE_NATIONALITY\n"if ($PL_VALUES[5] && ($PL_VALUES[29] < 100 || $PL_VALUES[0] < 215) && $PL_VALUES[39] eq "2");
		$boumeiTag.="<option value=\"\" selected>$NONE_NATIONALITY\n";
		$boumeiTag.="</select>";
		$boumeiTag='' if !$bf;

	}

	$VS_COUNTRY="$FORM{'CNTRY'}" if $FORM{'CNTRY'};
	$VS_COUNTRY="$PL_VALUES[5]" if !$FORM{'CNTRY'};
	@CL_VALUE = split(/\s/,$C{"$VS_COUNTRY"});
	@CL_VALUE2 = split(/\s/,$C{"$PL_VALUES[5]"}) if $PL_VALUES[5];

	$CL_VALUE[0]="$TABLE_COLOR2" if !$CL_VALUE[0];
	print << "	-----END-----" if $FORM{'b_mode'} ne '戦闘';
		<form action=$MAIN_SCRIPT method=POST target=Sub>
		<input type=hidden name="ntim" value="$FORM{'ntim'}">

		<table><tr><td style=\"background-color:$CL_VALUE[0];font-size:40px;\" colspan=8>
			<font color=$BG_STATUS>$VS_COUNTRY</font></td></tr>
	-----END-----

	if($FORM{'CNTRY'} eq "$NONE_NATIONALITY"){$FORM{'CNTRY'}='';}

#foreach my $name ( sort keys %hash ){
#	print "$name,$hash{$name}\n";
#}
#foreach my $name ( sort { $a <=> $b } keys %hash ){
#	print "$name,$hash{$name}\n";
#}
#&ERROR("いやっほおおおう");
$Key="";
	#通常
	if($BattleSort eq "0" || $BattleSort eq ""){
		while (($Key,$Value) = each %P){
			@VS_VALUES = split(/\s/,$Value);
	
			&REPAIR(\@VS_VALUES);
	
			if ($Key ne "$FORM{'pname'}"){

	#	&ERROR("$VS_VALUES[39]ああ$FORM{'con'}") if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && $WN_sS[7]=~ m/!6j|!6k/ && !$VS_VALUES[25] && $VS_VALUES[15] <= $VS_VALUES[16];
	#	&ERROR("$VS_VALUES[5]いい$PL_VALUES[5]") if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]";
	#			(&FILTING,$sousuiCh++) if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $VS_VALUES[6] ==1 && $PL_VALUES[0] >=170;
	
	
	
				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
	#			&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] ne '' && !$FORM{'b_mode'} && !$VS_VALUES[25];
	#			&FILTING if $VS_VALUES[39] eq "1" && $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq '' && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
	#			&FILTING if $VS_VALUES[39] eq "2" && $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq '' && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku2 < 40;
	
	#			if($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] ne '' && !$FORM{'b_mode'} && !$VS_VALUES[25]){&FILTING;}
	#			elsif($VS_VALUES[39] eq "1" && $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq '' && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40){&FILTING;}
	#			elsif($VS_VALUES[39] eq "2" && $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq '' && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku2 < 40){&FILTING;}
	#			&FILTING if $VS_VALUES[39] eq "1" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
	#			&FILTING if $VS_VALUES[39] eq "2" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku2 < 40;
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '亡命' && $VS_VALUES[0] > $PL_VALUES[0] && !$VS_VALUES[25] && !LOGIN_CHECK($Key);
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6j|!6k|!76|!77/ || $WN_sT[7]=~ m/!6j|!6k|!76|!77/ || $WN_sU[7]=~ m/!6j|!6k|!76|!77/ || $WN_sA[7]=~ m/!6j|!6k|!76|!77/ || $WN_sB[7]=~ m/!6j|!6k|!76|!77/ || $WN_sC[7]=~ m/!6j|!6k|!76|!77/ || $WN_sD[7]=~ m/!6j|!6k|!76|!77/) && $VS_VALUES[25] eq "0" && $VS_VALUES[15] <= $VS_VALUES[16];
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6l|!77/ || $WN_sT[7]=~ m/!6l|!77/ || $WN_sU[7]=~ m/!6l|!77/ || $WN_sA[7]=~ m/!6l|!77/ || $WN_sB[7]=~ m/!6l|!77/ || $WN_sC[7]=~ m/!6l|!77/ || $WN_sD[7]=~ m/!6l|!77/) && $VS_VALUES[25] eq "1" && $VS_VALUES[15] <= $VS_VALUES[16];
				(&FILTING,$sousuiCh++) if $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $VS_VALUES[6] ==1 && $PL_VALUES[0] >=170;
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[2] && $CL_VALUE2[2] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[3] && $CL_VALUE2[3] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[4] && $CL_VALUE2[4] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
	#			&FILTING if $FORM{'b_mode'} eq '探求';
			}
	#		if($FORM{'CNTRY'} eq '' && $VS_VALUES[5] eq '' && !$VS_VALUES[25]){$mukoku++;}
	#		if($FORM{'CNTRY'} eq '' && $VS_VALUES[5] eq '' && !$VS_VALUES[25] && $VS_VALUES[39] eq "1"){$mukoku++;}
	#		if($FORM{'CNTRY'} eq '' && $VS_VALUES[5] eq '' && !$VS_VALUES[25] && $VS_VALUES[39] eq "2"){$mukoku2++;}
		}
	#1型　キーを文字比較　ちょっと微妙かも
	}elsif($BattleSort eq "1"){

		foreach my $KeyCalc (sort keys %P ){
			@VS_VALUES = split(/\s/,$P{$KeyCalc});
			$Key = $KeyCalc;
			&REPAIR(\@VS_VALUES);
			if ($Key ne "$FORM{'pname'}"){
				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '亡命' && $VS_VALUES[0] > $PL_VALUES[0] && !$VS_VALUES[25] && !LOGIN_CHECK($Key);
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6j|!6k|!76|!77/ || $WN_sT[7]=~ m/!6j|!6k|!76|!77/ || $WN_sU[7]=~ m/!6j|!6k|!76|!77/ || $WN_sA[7]=~ m/!6j|!6k|!76|!77/ || $WN_sB[7]=~ m/!6j|!6k|!76|!77/ || $WN_sC[7]=~ m/!6j|!6k|!76|!77/ || $WN_sD[7]=~ m/!6j|!6k|!76|!77/) && $VS_VALUES[25] eq "0" && $VS_VALUES[15] <= $VS_VALUES[16];
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6l|!77/ || $WN_sT[7]=~ m/!6l|!77/ || $WN_sU[7]=~ m/!6l|!77/ || $WN_sA[7]=~ m/!6l|!77/ || $WN_sB[7]=~ m/!6l|!77/ || $WN_sC[7]=~ m/!6l|!77/ || $WN_sD[7]=~ m/!6l|!77/) && $VS_VALUES[25] eq "1" && $VS_VALUES[15] <= $VS_VALUES[16];
				(&FILTING,$sousuiCh++) if $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $VS_VALUES[6] ==1 && $PL_VALUES[0] >=170;
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[2] && $CL_VALUE2[2] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[3] && $CL_VALUE2[3] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[4] && $CL_VALUE2[4] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
			}
		}
	#2型　キーを数値比較　まぁ使える
	}elsif($BattleSort eq "2"){

		foreach $KeyCalc (sort {$P{$a} <=> $P{$b}} keys %P)  {

			@VS_VALUES = split(/\s/,$P{$KeyCalc});
			$Key = $KeyCalc;
			&REPAIR(\@VS_VALUES);
			if ($Key ne "$FORM{'pname'}"){
#				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;

#				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] ne "" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
#				&FILTING if $VS_VALUES[39] ne "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] ne "" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
#				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] eq "" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;

##ニ大陸
#				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] ne "" && !$FORM{'b_mode'} && !$VS_VALUES[25];
#				&FILTING if $VS_VALUES[39] ne "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] ne "" && !$FORM{'b_mode'} && !$VS_VALUES[25];
#				&FILTING if $VS_VALUES[39] eq "1" && $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] eq "" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 80;
#				&FILTING if $VS_VALUES[39] eq "2" && $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && $VS_VALUES[5] eq "" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku2 < 80;

#				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '亡命' && $VS_VALUES[0] > $PL_VALUES[0] && !$VS_VALUES[25] && !LOGIN_CHECK($Key);
#				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6j|!6k|!76|!77/ || $WN_sT[7]=~ m/!6j|!6k|!76|!77/ || $WN_sU[7]=~ m/!6j|!6k|!76|!77/ || $WN_sA[7]=~ m/!6j|!6k|!76|!77/ || $WN_sB[7]=~ m/!6j|!6k|!76|!77/ || $WN_sC[7]=~ m/!6j|!6k|!76|!77/ || $WN_sD[7]=~ m/!6j|!6k|!76|!77/) && $VS_VALUES[25] eq "0" && $VS_VALUES[15] <= $VS_VALUES[16];
#				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6l|!77/ || $WN_sT[7]=~ m/!6l|!77/ || $WN_sU[7]=~ m/!6l|!77/ || $WN_sA[7]=~ m/!6l|!77/ || $WN_sB[7]=~ m/!6l|!77/ || $WN_sC[7]=~ m/!6l|!77/ || $WN_sD[7]=~ m/!6l|!77/) && $VS_VALUES[25] eq "1" && $VS_VALUES[15] <= $VS_VALUES[16];
#				(&FILTING,$sousuiCh++) if $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $VS_VALUES[6] ==1 && $PL_VALUES[0] >=170;
#				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[2] && $CL_VALUE2[2] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
#				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[3] && $CL_VALUE2[3] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
#				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[4] && $CL_VALUE2[4] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}

				#シャングリラ時
				&FILTING if $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 80;
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '亡命' && $VS_VALUES[0] > $PL_VALUES[0] && !$VS_VALUES[25] && !LOGIN_CHECK($Key);
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6j|!6k|!76|!77/ || $WN_sT[7]=~ m/!6j|!6k|!76|!77/ || $WN_sU[7]=~ m/!6j|!6k|!76|!77/ || $WN_sA[7]=~ m/!6j|!6k|!76|!77/ || $WN_sB[7]=~ m/!6j|!6k|!76|!77/ || $WN_sC[7]=~ m/!6j|!6k|!76|!77/ || $WN_sD[7]=~ m/!6j|!6k|!76|!77/) && $VS_VALUES[25] eq "0" && $VS_VALUES[15] <= $VS_VALUES[16];
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6l|!77/ || $WN_sT[7]=~ m/!6l|!77/ || $WN_sU[7]=~ m/!6l|!77/ || $WN_sA[7]=~ m/!6l|!77/ || $WN_sB[7]=~ m/!6l|!77/ || $WN_sC[7]=~ m/!6l|!77/ || $WN_sD[7]=~ m/!6l|!77/) && $VS_VALUES[25] eq "1" && $VS_VALUES[15] <= $VS_VALUES[16];
				(&FILTING,$sousuiCh++) if $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $VS_VALUES[6] ==1 && $PL_VALUES[0] >=170;
				if ($VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[2] && $CL_VALUE2[2] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[3] && $CL_VALUE2[3] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[4] && $CL_VALUE2[4] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
			}
			if($FORM{'CNTRY'} eq '' && $VS_VALUES[5] eq '' && !$VS_VALUES[25]){$mukoku++;}
#			if($FORM{'CNTRY'} eq '' && $VS_VALUES[5] eq '' && !$VS_VALUES[25] && $VS_VALUES[39] eq "1"){$mukoku++;}
#			if($FORM{'CNTRY'} eq '' && $VS_VALUES[5] eq '' && !$VS_VALUES[25] && $VS_VALUES[39] eq "2"){$mukoku2++;}

		}

	#3型　キーに、9桁の値を付与(右に付与)　現在年月(YYYYMM)
	}elsif($BattleSort eq "3"){

		while (($Key,$Value) = each %P){

			@VS_VALUES = split(/\s/,$Value);

		}

		foreach $KeyCalc (sort {$P{$a} <=> $P{$b}} keys %P)  {

			@VS_VALUES = split(/\s/,$P{$KeyCalc});
			$Key = $KeyCalc;
			&REPAIR(\@VS_VALUES);
			if ($Key ne "$FORM{'pname'}"){
				&FILTING if $VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$FORM{'CNTRY'}" && !$FORM{'b_mode'} && !$VS_VALUES[25] && $mukoku < 40;
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '亡命' && $VS_VALUES[0] > $PL_VALUES[0] && !$VS_VALUES[25] && !LOGIN_CHECK($Key);
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6j|!6k|!76|!77/ || $WN_sT[7]=~ m/!6j|!6k|!76|!77/ || $WN_sU[7]=~ m/!6j|!6k|!76|!77/ || $WN_sA[7]=~ m/!6j|!6k|!76|!77/ || $WN_sB[7]=~ m/!6j|!6k|!76|!77/ || $WN_sC[7]=~ m/!6j|!6k|!76|!77/ || $WN_sD[7]=~ m/!6j|!6k|!76|!77/) && $VS_VALUES[25] eq "0" && $VS_VALUES[15] <= $VS_VALUES[16];
				&FILTING if $VS_VALUES[5] eq "$PL_VALUES[5]" && $PL_VALUES[5] && $FORM{'b_mode'} eq '回復' && ($WN_sS[7]=~ m/!6l|!77/ || $WN_sT[7]=~ m/!6l|!77/ || $WN_sU[7]=~ m/!6l|!77/ || $WN_sA[7]=~ m/!6l|!77/ || $WN_sB[7]=~ m/!6l|!77/ || $WN_sC[7]=~ m/!6l|!77/ || $WN_sD[7]=~ m/!6l|!77/) && $VS_VALUES[25] eq "1" && $VS_VALUES[15] <= $VS_VALUES[16];
				(&FILTING,$sousuiCh++) if $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $VS_VALUES[6] ==1 && $PL_VALUES[0] >=170;
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[2] && $CL_VALUE2[2] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[3] && $CL_VALUE2[3] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
				if ($VS_VALUES[39] eq "$FORM{'con'}" && $VS_VALUES[5] eq "$PL_VALUES[5]" && $FORM{'b_mode'} eq '内乱' && $PL_VALUES[6] ==0 && $VS_VALUES[6] ==-1 && $CL_VALUE2[4] && $CL_VALUE2[4] eq "$VS_VALUES[28]" && $PL_VALUES[0] >=100){&FILTING;}
			}
		}

	}
#	&ERROR("$Key");

	if($PL_VALUES[5] && !$PL_VALUES[28]){
		$M_AITE="$CL_VALUE2[6]";
	}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUE2[2]" && $CL_VALUE2[2]){
		$M_AITE="$CL_VALUE2[8]";
	}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUE2[3]" && $CL_VALUE2[3]){
		$M_AITE="$CL_VALUE2[9]";
	}elsif($PL_VALUES[5] && $PL_VALUES[28] eq "$CL_VALUE2[4]" && $CL_VALUE2[4]){
		$M_AITE="$CL_VALUE2[10]";
	}

	if ($FORM{'b_mode'} eq '' && !$PlMs){
		require './vatime.pl';
		&vatimeheader;
		if ($WW_FRAG==1 && $HIZUK_FRAG==1) {

		print "<tr><td bgcolor=\"$CL_VALUE[0]\">&nbsp;</td><td bgcolor=#000000 colspan=6>No-PLAYER</td></tr>" if $PL_VALUES[5] eq '' || $FORM{'CNTRY'} eq '';
		$battle="BATTLE_4" if $PL_VALUES[5] ne '' && $FORM{'CNTRY'} ne '';
		print << "		-----END-----"if $PL_VALUES[5] ne '' && $FORM{'CNTRY'} ne '';
			<tr><td bgcolor=$CL_VALUE[0] align=center>&nbsp;&nbsp;</td>
			<td bgcolor=$TABLE_COLOR1><input type=radio name=vsname checked value=\"$VS_COUNTRY\">
			<input type=hidden name=yousai value="true">
			$VS_COUNTRY防衛要塞<br>&nbsp;&nbsp;敵要塞本部への直接攻撃が可能\です。</td>
			<td bgcolor=$TABLE_COLOR1><img src=$IMG_FOLDER2/1000.gif></td><td bgcolor=$TABLE_COLOR1>－</td></tr>
		-----END-----
		$PlMs++ if $PL_VALUES[5] ne '' && $FORM{'CNTRY'} ne '';
		} else {

		print "<tr><td bgcolor=\"$CL_VALUE[0]\">&nbsp;</td><td bgcolor=#000000 colspan=6>No-PLAYER</td></tr>" if $CL_VALUE2[7] < time || $M_AITE ne "$VS_COUNTRY";
		$battle="BATTLE_4" if $CL_VALUE2[7] > time && $M_AITE eq "$VS_COUNTRY";
		print << "		-----END-----"if $CL_VALUE2[7] > time && $M_AITE eq "$VS_COUNTRY";
			<tr><td bgcolor=$CL_VALUE[0] align=center>&nbsp;&nbsp;</td>
			<td bgcolor=$TABLE_COLOR1><input type=radio name=vsname checked value=\"$VS_COUNTRY\">
			<input type=hidden name=yousai value="true">
			$VS_COUNTRY防衛要塞<br>&nbsp;&nbsp;敵要塞本部の直接攻撃が可能\です。</td>
			<td bgcolor=$TABLE_COLOR1><img src=$IMG_FOLDER2/1000.gif></td><td bgcolor=$TABLE_COLOR1>－</td></tr>
		-----END-----
		$PlMs++ if $CL_VALUE2[7] > time && $M_AITE eq "$VS_COUNTRY";
		}
	}
	$HiddenTag="<form action=$MAIN_SCRIPT method=POST target=Main><input type=hidden name=\"cmd\" value=\"CUSTOM\"><input type=hidden name=\"pname\" value=\"$FORM{'pname'}\"><input type=hidden name=\"pass\" value=\"$FORM{'pass'}\">";

	if ($FORM{'b_mode'} eq '亡命' && !$PlMs && $PL_VALUES[8] >= 30000 || $FORM{'b_mode'} eq '亡命' && !$PL_VALUES[5]){
		$BOMEIM=int($PL_VALUES[8]/10);
		$BOMEIM='30000' if $BOMEIM < 30000;
		$BOMEIM=0 if !$PL_VALUES[5];
		print << "		-----END-----";
			<tr></form><td bgcolor=\"$CL_VALUE[0]\">&nbsp;</td>
				$HiddenTag<td bgcolor=$TABLE_COLOR1 colspan=6>$boumeiTag
				亡命しますか？&nbsp;&nbsp;費用 \$$BOMEIM
				&nbsp;&nbsp;<input type=submit name="Cmode" value="亡命" 
				onClick="location.replace('$BACKFR');">
			</td></tr>
		-----END-----
	}
	if ($FORM{'b_mode'} eq '内乱' && !$sousuiCh && $PL_VALUES[0] >=170 && $PL_VALUES[6] ==0){$PlMs2=1;
		$hanran.= << "		-----END-----";
			<tr></form><td bgcolor=\"$CL_VALUE[0]\">&nbsp;</td>
				$HiddenTag<td bgcolor=$TABLE_COLOR1 colspan=6>
				総帥が不在のため、議会はあなたに全指揮権を委任する方針のようです。引き受けますか？
				<input type=submit name="Cmode" value="総帥就任" 
				onClick="location.replace('$BACKFR');">
			</td></tr>
		-----END-----
	}

	$NEWDATE=time;$SENTO=int(rand(3));
	if($SENTO == 1){$LAG="&nbsp;&nbsp;&nbsp;&nbsp;";}elsif($SENTO == 2){$LAG="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";}
	elsif($SENTO == 3){$LAG="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";}else{$LAG="";}
	$battle="BATTLE_5" if $FORM{'b_mode'} eq '回復';
	$battle="BATTLE_6" if $FORM{'b_mode'} eq '亡命' || $FORM{'b_mode'} eq '内乱';
	print << "	-----END-----" if $FORM{'b_mode'} ne '戦闘' && $PlMs;
		<tr><td bgcolor=\"$CL_VALUE[0]\"><a name=sbm></a>&nbsp;</td>
			<td colspan=7 bgcolor=\"$TABLE_COLOR1\">
			$Sakusen$Toksen$HoSen$boumeiTag
			<input type=hidden name="cmd" value="$battle">
			<input type=hidden name="pname" value="$FORM{'pname'}">
			<input type=hidden name="pass" value="$FORM{'pass'}">
			<input type=hidden name="b_mode" value="$FORM{'b_mode'}">
			<input type=hidden name="check" value="$DATE">
			<input type=hidden name="scheck" value="$NEWDATE">
			<input type=hidden name="ntim" value="$FORM{'ntim'}">
			$LAG<input type=submit value="戦闘" onClick="location.replace('$BACKFR');">
		</td></tr>
	-----END-----

	print $hanran if $FORM{'b_mode'} ne '戦闘' && $PlMs2;
	print << "	-----END-----" if $FORM{'b_mode'} eq '内乱' && !$PlMs && !$PlMs2;
			<tr></form><td bgcolor=\"$CL_VALUE[0]\">&nbsp;</td><td bgcolor=$TABLE_COLOR1 colspan=7>
				対戦相手が存在しないか階級レベルが足りない為、実行できません。
			</td></tr>
	-----END-----
	print << "	-----END-----" if $FORM{'b_mode'} eq '回復' && !$PlMs && !$PlMs2;
			<tr></form><td bgcolor=\"$CL_VALUE[0]\">&nbsp;</td><td bgcolor=$TABLE_COLOR1 colspan=7>
				回復相手がいません。
			</td></tr>
	-----END-----

	print "</table></form><br><br>";
	&FOOTER;
exit;
}
sub FILTING {
	if ($FORM{'b_mode'} eq "戦闘" || $FORM{'c_mode'} eq "戦闘"){
		require './vatime.pl';
		&vatimeheader;
	}

#	$LimitTime=time;
#	if($FORM{'ntim'}+120 < $LimitTime){
#		&ERROR('SystemError','システムチェックに時差があります。ステータス画面の更新を行ってください。');
#		print "てす\n";
#		print "<table border=1 bordercolor=#333333 cellspacing=0>\n";
#		print "<form action=$MAIN_SCRIPT method=POST target=Main>\n";
#		print "<input type=hidden name=cmd value=MAIN_FRAME>\n";
#		print "<input type=hidden name=pname value=$FORM{'pname'}>\n";
#		print "<input type=hidden name=pass value=$FORM{'pass'}><tr><td bgcolor=#000000>\n";
#		print "<b $chaStyl>&nbsp;</b><br>\n";
##		print "<input type=submit value=\"更新\" onClick=\"parent.frames[1].location.replace(\'$BACKFR\');\">\n";
#		print "<input type=submit value=\"更新\" onClick=\"parent.frames[1].location.replace(\'$BACKFR\');\">\n";
##		print "<input type=submit value=\"更新\" onClick=\"document.FM.target=\'Main\';document.FM.cmd.value=\'MAIN_FRAME\';\">";

#		print "</td></form></table>\n";exit;
#	}

#	&ERROR("$LimitTimeと$FORM{'ntim'}");
#	if ($LimitTime < time){&ERROR("$LimitTime");}

	$PlMs++;
	$IconTag=$Guarder='';
	if($PlMs==1){$rc='checked';}else{$rc='';}
	if($FORM{'b_mode'} eq '回復'){
		$hpkaifuku="$VS_VALUES[15]/$VS_VALUES[16]";
		if($VS_VALUES[25] eq "0"){$Seizon="<font color=#5779EE>出撃可</font>";}else{$Seizon="<font color=#dc143c>回復中</font>";}
#		if(LOGIN_CHECK($Key)){$Seizon="<font color=#5779EE>出撃可</font>";}else{$Seizon="<font color=#dc143c>回復中</font>";}
	}
	$IconTag="<img src=\"$IMG_FOLDER2/$VS_VALUES[27].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\">";
#	$IconTag="<img src=\"$IMG_FOLDER7/$VS_VALUES[40].gif\" width=\"64\" height=\"96\" style=\"filter:fliph();\">";
	print "<tr><td bgcolor=\"$CL_VALUE[0]\" align=center>&nbsp;&nbsp;</td>";

	print "<td bgcolor=\"$TABLE_COLOR1\"><input type=radio name=vsname value=\"$Key\" $rc onClick=\"location.replace('#sbm')\">";
	print "<span style=\"font-size:18px;color:$VS_VALUES[13];\">$Key</span>";

	print "<span style=\"font-size:15px;\"><b>".&RANK("$VS_VALUES[0]","$VS_VALUES[5]","$VS_VALUES[6]")."</b></span></td>";
	print "<td bgcolor=\"$TABLE_COLOR1\">$IconTag<font color=\"$VS_VALUES[13]\">$VS_VALUES[3]</font></td>";
	print "<td bgcolor=\"$TABLE_COLOR1\">".&STATUS_CONVERT("$VS_VALUES[24]",'j');
	print "</td><td bgcolor=\"$TABLE_COLOR1\">".&STATUS_CONVERT("$VS_VALUES[12]",'l');

	print "</td><td bgcolor=\"$TABLE_COLOR1\">".&STATUS_CONVERT("$VS_VALUES[31]",'e');
	if($PL_VALUES[29] > $VS_VALUES[29]){$LV_PL="<font color=#dc143c>↓</font>";}else{$LV_PL="<font color=#3769ef>↑</font>";}
	print "</td><td bgcolor=\"$TABLE_COLOR1\">$LV_PL";
	print "</td><td bgcolor=\"$TABLE_COLOR1\">";
	if($FORM{'b_mode'} eq '回復'){
	if(LOGIN_CHECK($Key)){$San="<font color=#dc143c>参戦中</font>";}else{$San="<font color=#3769ef>休戦中</font>";}
	print "<font color=#cac7c7>&nbsp;$San&nbsp;$Seizon&nbsp;$hpkaifuku&nbsp;</font>";}elsif ((($FORM{'CNTRY'} eq "$CL_VALUE2[6]") || ($FORM{'CNTRY'} eq "$CL_VALUE2[8]") || ($FORM{'CNTRY'} eq "$CL_VALUE2[9]") || ($FORM{'CNTRY'} eq "$CL_VALUE2[10]")) && ($FORM{'CNTRY'} ne '') && ($CL_VALUE2[7] > time) ||
	(($PL_VALUES[5] eq "$CL_VALUE[6]") || ($PL_VALUES[5] eq "$CL_VALUE[8]") || ($PL_VALUES[5] eq "$CL_VALUE[9]") || ($PL_VALUES[5] eq "$CL_VALUE[10]")) && ($PL_VALUES[5] ne '') && ($CL_VALUE[7] > time) ||
	$WW_FRAG==1){ print "&nbsp;<font color=#808080>不明</font>&nbsp;"; }elsif(LOGIN_CHECK($Key)){
	print "<font color=#dc143c>参戦中</font>";}else{ print "<font color=#3769ef>休戦中</font>"; }

	if($FORM{'b_mode'} eq '探求'){

	}
	print "</td></tr>";
}


1;

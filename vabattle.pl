sub vabattleheader{
#	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
#		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
#	@pairs = split(/\,/, $DUMMY{'EB'});
#		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&DBM_INPORT(P);&DBM_INPORT(C);
#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
#	&DBM_INPORT(R);
#	@R_VALUES = split(/\s/,$R{"server"});

#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
#	&ERROR('Error','ユニットとユーザのIDが一致していません。') if $COOKIE{'pname'} ne "$FORM{pname}";
#	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";
#	&ERROR('TimeOut','ユニット選択が遅すぎます。') if (($FORM{'scheck'} + 120) < time || $FORM{'scheck'} > time);
##	&ERROR('TimeOut','ユニット選択が遅すぎます。ステータス画面の更新ボタンを押下して下さい。') if (($FORM{'ntim'} + 120) < time);



	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);

	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});


#	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&DBM_INPORT(R);
	@R_VALUES = split(/\s/,$R{"server"});

#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
#	&ERROR('Error','ユニットとユーザのIDが一致していません。') if $COOKIE{'pname'} ne "$FORM{pname}";
#	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";
	&ERROR('TimeOut','ユニット選択が遅すぎます。') if (($FORM{'scheck'} + 120) < time || $FORM{'scheck'} > time);
#	&ERROR('TimeOut','ユニット選択が遅すぎます。ステータス画面の更新ボタンを押下して下さい。') if (($FORM{'ntim'} + 120) < time);

	&ERROR('NameError','IDが間違っているか、登録されていません。') if !@PL_VALUES;
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($FORM{'pass'},eb) ne "$PL_VALUES[2]";


	require './vatime.pl';
	&vatimeheader2;

	$KOKUSEKI=$FORM{'vsname'};

	SET_COOKIE:{
		my @gmt = gmtime(time + $COOKIE_KEEP*24*60*60);
		$gmt[0] = sprintf("%02d", $gmt[0]);$gmt[1] = sprintf("%02d", $gmt[1]);$gmt[2] = sprintf("%02d", $gmt[2]);
		$gmt[3] = sprintf("%02d", $gmt[3]);$gmt[5] += 1900;
		$gmt[4] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$gmt[4]];
		$gmt[6] = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$gmt[6]];
		my $date_gmt = "$gmt[6], $gmt[3]\-$gmt[4]\-$gmt[5] $gmt[2]:$gmt[1]:$gmt[0] GMT";
#		$SCKIE="Set-Cookie:EBMISSON=$FORM{'mode'}; expires=$date_gmt\nSet-Cookie:EBMISSON2=$FORM{'sentaku'}; expires=$date_gmt\nSet-Cookie:EBMISSON3=$FORM{'Hosentaku'}; expires=$date_gmt\n;";
		$SCKIE="Set-Cookie:EBMISSON=$FORM{'mode'}; expires=$date_gmt\nSet-Cookie:EBMISSON2=$FORM{'sentaku'}; expires=$date_gmt\nSet-Cookie:EBMISSON3=$FORM{'Hosentaku'}; expires=$date_gmt\n";
#		$SCKIE="Set-Cookie:EBMISSON=$FORM{'mode'}; expires=$date_gmt\n";
#		$SCKIE2="Set-Cookie:EBMISSON2=$FORM{'sentaku'}; expires=$date_gmt\n";
	}
}
sub vabattle1{

	&CANHEAD('PL','VS','CL','VC');
	&CANHEAD('VS','PL','VC','CL');

	&ERROR('SystemError','システムチェックに時差があります。') if ($FORM{'check'} < $PL_VALUES[26]);
}

sub vabattle2{
#		&ERROR("$FORM{'sentaku'}");
	require "./$LOG_FOLDER/$HASH_DATA";
	@PL_W=split(/\,/,$WEAPON_LIST{"$PL_WN"}); @PL_sB=split(/\,/,$WEAPON_LIST{"$PL_WB"}); @PL_sC=split(/\,/,$WEAPON_LIST{"$PL_WC"}); @PL_sD=split(/\,/,$WEAPON_LIST{"$PL_WD"});
	@VS_W=split(/\,/,$WEAPON_LIST{"$VS_WN"}); @VS_sB=split(/\,/,$WEAPON_LIST{"$VS_WB"}); @VS_sC=split(/\,/,$WEAPON_LIST{"$VS_WC"}); @VS_sD=split(/\,/,$WEAPON_LIST{"$VS_WD"});
#イベント用アビリティ
	require "./$LOG_FOLDER/$ABI_DATA";
	$PL_MAXHP=0;$PL_MAXMP=0;$VS_MAXHP=0;$VS_MAXMP=0;
	if($AbiSys == 1){
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		local($VABI_FLG,$VABI_A,$VABI_B,$VABI_C) = split(/!/,$VS_VALUES[52]);
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});
		@VABI_sA=split(/\,/,$ABINAME_LIST{"$VABI_A"});
		@VABI_sB=split(/\,/,$ABINAME_LIST{"$VABI_B"});
		@VABI_sC=split(/\,/,$ABINAME_LIST{"$VABI_C"});

		#最大HP情報を退避
		$PL_MAXHP = $PL_VALUES[16];
		$VS_MAXHP = $VS_VALUES[16];

		#最大MP情報を退避
		$PL_MAXMP = $PL_VALUES[18];
		$VS_MAXMP = $VS_VALUES[18];

		#全て無効 0で有効　1で無効
		$AbiMukou = '0';
		if($ABI_sA[2] =~ m/!A0055/ || $ABI_sB[2] =~ m/!A0055/ || $ABI_sC[2] =~ m/!A0055/ || $VABI_sA[2] =~ m/!A0055/ || $VABI_sB[2] =~ m/!A0055/ || $VABI_sC[2] =~ m/!A0055/){
			$AbiMukou = '1';

			#最大HPアップを習得していた場合　最大HP-20000
			if($ABI_sA[2] =~ m/!A0034/ || $ABI_sB[2] =~ m/!A0034/ || $ABI_sC[2] =~ m/!A0034/){
				$PL_VALUES[16]-=20000;
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}
			}
			if($VABI_sA[2] =~ m/!A0034/ || $VABI_sB[2] =~ m/!A0034/ || $VABI_sC[2] =~ m/!A0034/){
				$VS_VALUES[16]-=20000;
				if($VS_VALUES[15]>$VS_VALUES[16]){$VS_VALUES[15]=$VS_VALUES[16];}
			}
			#最大MPアップを習得していた場合　最大MP-1000
			if($ABI_sA[2] =~ m/!A0035/ || $ABI_sB[2] =~ m/!A0035/ || $ABI_sC[2] =~ m/!A0035/){
				$PL_VALUES[18]-=1000;
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}
			}
			if($VABI_sA[2] =~ m/!A0035/ || $VABI_sB[2] =~ m/!A0035/ || $VABI_sC[2] =~ m/!A0035/){
				$VS_VALUES[18]-=1000;
				if($VS_VALUES[17]>$VS_VALUES[18]){$VS_VALUES[17]=$VS_VALUES[18];}
			}

		}
	
		#対抗技術
		if($AbiMukou == 0){
			if($ABI_sA[2] =~ m/!A0117/){@VABI_sA="";}
			if($ABI_sB[2] =~ m/!A0117/){@VABI_sB="";}
			if($ABI_sC[2] =~ m/!A0117/){@VABI_sC="";}

			if($VABI_sA[2] =~ m/!A0117/){@VABI_sA="";}
			if($VABI_sB[2] =~ m/!A0117/){@VABI_sB="";}
			if($VABI_sC[2] =~ m/!A0117/){@VABI_sC="";}
		}

	}

##クラス変化時処理追加
	&GOUSEI('c1','PL','VS') if ($PL_VALUES[4] =~ /^64$|^65$|^70$|^71$|^72$|^131$|^132$|^133$|^134$|^135$|^203$/i);
	&GOUSEI('c1','VS','PL') if ($VS_VALUES[4] =~ /^64$|^65$|^70$|^71$|^72$|^131$|^132$|^133$|^134$|^135$|^203$/i);
#		&ERROR("$VS_VALUES[4]");
##クラス読み込み
	require "./$LOG_FOLDER/$CLASS_DATA";
	@PL_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});
	@VS_CLASS=split(/\,/,$VCLASS_LIST{"$VS_VALUES[4]"});



	#夜の恩寵
	if($AbiSys == 1){

#		if(($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i) && ($PL_VALUES[4] =~ /^64$|^65$/i) && ($ABI_sA[2] =~ m/!A0094/ || $ABI_sB[2] =~ m/!A0094/ || $ABI_sC[2] =~ m/!A0094/)){
		if(($TIME[2] =~ /^18$|^19$|^20$|^21$|^22$|^23$|^0$|^1$|^2$|^3$|^4$|^5$/i) && ($PL_CLASS[17] =~ m/!E004/) && ($ABI_sA[2] =~ m/!A0094/ || $ABI_sB[2] =~ m/!A0094/ || $ABI_sC[2] =~ m/!A0094/)){
			$PL_CLASS[1] = $PL_CLASS[1] + 3;$PL_CLASS[2] = $PL_CLASS[2] + 3;$PL_CLASS[3] = $PL_CLASS[3] + 3;$PL_CLASS[4] = $PL_CLASS[4] + 3;
		}
		if(($TIME[2] =~ /^18$|^19$|^20$|^21$|^22$|^23$|^0$|^1$|^2$|^3$|^4$|^5$/i) && ($VS_CLASS[17] =~ m/!E004/) && ($VABI_sA[2] =~ m/!A0094/ || $VABI_sB[2] =~ m/!A0094/ || $VABI_sC[2] =~ m/!A0094/)){
			$VS_CLASS[1] = $VS_CLASS[1] + 3;$VS_CLASS[2] = $VS_CLASS[2] + 3;$VS_CLASS[3] = $VS_CLASS[3] + 3;$VS_CLASS[4] = $VS_CLASS[4] + 3;
		}

	}

	#アンデッド補正 神聖系による補正-2はこれより下の構文で処理
	if(($TIME[2] =~ /^18$|^19$|^20$|^21$|^22$|^23$|^0$|^1$|^2$|^3$|^4$|^5$/i) && ($PL_CLASS[17] =~ m/!E004/)){
		$PL_CLASS[1] = $PL_CLASS[1] + 2;$PL_CLASS[2] = $PL_CLASS[2] + 2;$PL_CLASS[3] = $PL_CLASS[3] + 2;$PL_CLASS[4] = $PL_CLASS[4] + 2;
	}
	if(($TIME[2] =~ /^18$|^19$|^20$|^21$|^22$|^23$|^0$|^1$|^2$|^3$|^4$|^5$/i) && ($VS_CLASS[17] =~ m/!E004/)){
		$VS_CLASS[1] = $VS_CLASS[1] + 2;$VS_CLASS[2] = $VS_CLASS[2] + 2;$VS_CLASS[3] = $VS_CLASS[3] + 2;$VS_CLASS[4] = $VS_CLASS[4] + 2;
	}

	$Pl_EEXP = 0;$Vs_EEXP = 0;	#0：武器だけ　1：上書きされた　2：組み合わせ
	$Pl_SWName = $PL_W[0];$Vs_SWName = $VS_W[0];

	if($FORM{'sentaku'} eq "41" || $FORM{'sentaku'} eq "42" || $FORM{'sentaku'} eq "43"){
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_WS"});
	}elsif($FORM{'sentaku'} eq "9"){
		#装備品に込められた能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_W[13]"});
	}elsif($FORM{'sentaku'} eq "10"){
		#装備品に込められた能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_sB[13]"});
	}elsif($FORM{'sentaku'} eq "11"){
		#装備品に込められた能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_sC[13]"});
	}elsif($FORM{'sentaku'} eq "38"){
		#装備品に込められた能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_sD[13]"});
	}elsif($FORM{'sentaku'} eq "44"){
		#クラス能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_CLASS[22]"});
	}elsif($FORM{'sentaku'} eq "45"){
		#クラス能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_CLASS[23]"});
	}elsif($FORM{'sentaku'} eq "46"){
		#クラス能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_CLASS[24]"});
	}elsif($FORM{'sentaku'} eq "47"){
		#クラス能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_CLASS[25]"});
	}elsif($FORM{'sentaku'} eq "48"){
		#クラス能力の解放
		@PL_sS=split(/\,/,$WEAPON_LIST{"$PL_CLASS[26]"});
	}
	@VS_sS=split(/\,/,$WEAPON_LIST{"$VS_WS"});

	if ($FORM{'sentaku'} eq "45" || $FORM{'sentaku'} eq "46" || $FORM{'sentaku'} eq "47" || $FORM{'sentaku'} eq "48"){$FORM{'sentaku'} = "44";}


#ヒート、メルト用
	@PL_sSS1=split(/\,/,$WEAPON_LIST{"$PL_WSS1"});
	@PL_sSS2=split(/\,/,$WEAPON_LIST{"$PL_WSS2"});
	@PL_sSS3=split(/\,/,$WEAPON_LIST{"$PL_WSS3"});
	@VS_sSS1=split(/\,/,$WEAPON_LIST{"$VS_WSS1"});
	@VS_sSS2=split(/\,/,$WEAPON_LIST{"$VS_WSS2"});
	@VS_sSS3=split(/\,/,$WEAPON_LIST{"$VS_WSS3"});



#片手持ち：槍
	if($PL_W[7] =~ m/!1y04/ && $PL_CLASS[17] =~ m/!W018/){$PL_W[7] =~ s/!11/!10/g;}
	if($VS_W[7] =~ m/!1y04/ && $VS_CLASS[17] =~ m/!W018/){$VS_W[7] =~ s/!11/!10/g;}

	if($AbiSys == 1){

		if($ABI_sA[2] =~ m/!A0091/ || $ABI_sB[2] =~ m/!A0091/ || $ABI_sC[2] =~ m/!A0091/){$PL_W[7] =~ s/!11/!10/g;$PL_W[4] = int($PL_W[4]*1.2);}

	}

#ノックバック：弓
	if($PL_W[7] =~ m/!1a/ && $PL_CLASS[17] =~ m/!W020/){$PL_W[7] .= "!2g";}
	if($VS_W[7] =~ m/!1a/ && $VS_CLASS[17] =~ m/!W020/){$VS_W[7] .= "!2g";}


#セット不具合用　反属性攻撃の場合、セット効果を消滅させる		VSは41が空なら9が対象
	$Pl_AntiEl = 0;$Vs_AntiEl = 0;
#	if(((!$PL_sS[0] && $PL_W[7] =~ m/!00/) || ($PL_sS[0] && $PL_sS[7] =~ m/!00/)) && (((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!02/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!02/))){$Pl_AntiEl = 1;}
#	elsif(((!$PL_sS[0] && $PL_W[7] =~ m/!01/) || ($PL_sS[0] && $PL_sS[7] =~ m/!01/)) && (((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!03/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!03/))){$Pl_AntiEl = 1;}
#	elsif(((!$PL_sS[0] && $PL_W[7] =~ m/!02/) || ($PL_sS[0] && $PL_sS[7] =~ m/!02/)) && (((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!00/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!00/))){$Pl_AntiEl = 1;}
#	elsif(((!$PL_sS[0] && $PL_W[7] =~ m/!03/) || ($PL_sS[0] && $PL_sS[7] =~ m/!03/)) && (((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!01/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!01/))){$Pl_AntiEl = 1;}
#	elsif(((!$PL_sS[0] && $PL_W[7] =~ m/!04/) || ($PL_sS[0] && $PL_sS[7] =~ m/!04/)) && (((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!05/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!05/))){$Pl_AntiEl = 1;}
#	elsif(((!$PL_sS[0] && $PL_W[7] =~ m/!05/) || ($PL_sS[0] && $PL_sS[7] =~ m/!05/)) && (((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!04/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!04/))){$Pl_AntiEl = 1;}

#	if((((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!00/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!00/)) && ((!$PL_sS[0] && $PL_W[7] =~ m/!02/) || ($PL_sS[0] && $PL_sS[7] =~ m/!02/))){$Vs_AntiEl = 1;}
#	elsif((((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!01/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!01/)) && ((!$PL_sS[0] && $PL_W[7] =~ m/!03/) || ($PL_sS[0] && $PL_sS[7] =~ m/!03/))){$Vs_AntiEl = 1;}
#	elsif((((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!02/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!02/)) && ((!$PL_sS[0] && $PL_W[7] =~ m/!00/) || ($PL_sS[0] && $PL_sS[7] =~ m/!00/))){$Vs_AntiEl = 1;}
#	elsif((((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!03/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!03/)) && ((!$PL_sS[0] && $PL_W[7] =~ m/!01/) || ($PL_sS[0] && $PL_sS[7] =~ m/!01/))){$Vs_AntiEl = 1;}
#	elsif((((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!04/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!04/)) && ((!$PL_sS[0] && $PL_W[7] =~ m/!05/) || ($PL_sS[0] && $PL_sS[7] =~ m/!05/))){$Vs_AntiEl = 1;}
#	elsif((((!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")) && $VS_W[7] =~ m/!05/) || ($VS_VALUES[41] && $VS_VALUES[45] ne "1" && $VS_sS[7] =~ m/!05/)) && ((!$PL_sS[0] && $PL_W[7] =~ m/!04/) || ($PL_sS[0] && $PL_sS[7] =~ m/!04/))){$Vs_AntiEl = 1;}
#	&ERROR("$PL_sS[0]ああ$PL_W[7]ああ$VS_VALUES[41]ああ$VS_W[7]ああ$VS_sS[7]");

	#ここで属性を一度合わせる必要がある

#20091011 ADD
#	&SEINOU('sei','PL','VS','0') if ($PL_W[7]=~ m/!6d/ || $PL_sS[7]=~ m/!6d/ || $PL_CLASS[17] =~ m/E005/);
#	&SEINOU('sei','VS','PL','0') if ($VS_W[7]=~ m/!6d/ || $VS_sS[7]=~ m/!6d/ || $VS_CLASS[17] =~ m/E005/);
#20091011 ADD
#&ERROR("$VS_sS[0]");

#BattleLevel
	#PL側	
	#武器行使の場合
	$PL_ELWEA=99;
	if(!$PL_sS[0]){
		if($PL_W[7] =~ m/!00/){$PL_ELWEA=0;}
		elsif($PL_W[7] =~ m/!01/){$PL_ELWEA=1;}
		elsif($PL_W[7] =~ m/!02/){$PL_ELWEA=2;}
		elsif($PL_W[7] =~ m/!03/){$PL_ELWEA=3;}
		elsif($PL_W[7] =~ m/!04/){$PL_ELWEA=4;}
		elsif($PL_W[7] =~ m/!05/){$PL_ELWEA=5;}
	}
	#魔法・技・特殊行使の場合
	if($PL_sS[0]){
		if($PL_sS[7] =~ m/!00/){$PL_ELWEA=0;}
		elsif($PL_sS[7] =~ m/!01/){$PL_ELWEA=1;}
		elsif($PL_sS[7] =~ m/!02/){$PL_ELWEA=2;}
		elsif($PL_sS[7] =~ m/!03/){$PL_ELWEA=3;}
		elsif($PL_sS[7] =~ m/!04/){$PL_ELWEA=4;}
		elsif($PL_sS[7] =~ m/!05/){$PL_ELWEA=5;}
	}

	#VS側
	#武器行使の場合 
	$VS_ELWEA=99;
#	if(!$VS_VALUES[41] || ($VS_VALUES[41] && $VS_VALUES[45] eq "1")){
	if($VS_VALUES[45] eq "" || $VS_VALUES[45] eq "1" || $VS_VALUES[45] eq "0" || $VS_VALUES[45] eq "9"){
		if($VS_W[7] =~ m/!00/){$VS_ELWEA=0;}
		elsif($VS_W[7] =~ m/!01/){$VS_ELWEA=1;}
		elsif($VS_W[7] =~ m/!02/){$VS_ELWEA=2;}
		elsif($VS_W[7] =~ m/!03/){$VS_ELWEA=3;}
		elsif($VS_W[7] =~ m/!04/){$VS_ELWEA=4;}
		elsif($VS_W[7] =~ m/!05/){$VS_ELWEA=5;}
	}
	#魔法・技・特殊行使の場合
#	if($VS_VALUES[41] && $VS_VALUES[45] ne "1"){
	if($VS_VALUES[45] ne "" && $VS_VALUES[45] ne "1" && $VS_VALUES[45] ne "0" && $VS_VALUES[45] ne "9"){
		if($VS_sS[7] =~ m/!00/){$VS_ELWEA=0;}
		elsif($VS_sS[7] =~ m/!01/){$VS_ELWEA=1;}
		elsif($VS_sS[7] =~ m/!02/){$VS_ELWEA=2;}
		elsif($VS_sS[7] =~ m/!03/){$VS_ELWEA=3;}
		elsif($VS_sS[7] =~ m/!04/){$VS_ELWEA=4;}
		elsif($VS_sS[7] =~ m/!05/){$VS_ELWEA=5;}
	}

	if($PL_ELWEA == 0 && $VS_ELWEA == 2){$Pl_AntiEl = 1;}
	elsif($PL_ELWEA == 1 && $VS_ELWEA == 3){$Pl_AntiEl = 1;}
	elsif($PL_ELWEA == 2 && $VS_ELWEA == 0){$Pl_AntiEl = 1;}
	elsif($PL_ELWEA == 3 && $VS_ELWEA == 1){$Pl_AntiEl = 1;}
	elsif($PL_ELWEA == 4 && $VS_ELWEA == 5){$Pl_AntiEl = 1;}
	elsif($PL_ELWEA == 5 && $VS_ELWEA == 4){$Pl_AntiEl = 1;}


	if($VS_ELWEA == 0 && $PL_ELWEA == 2){$Vs_AntiEl = 1;}
	elsif($VS_ELWEA == 1 && $PL_ELWEA == 3){$Vs_AntiEl = 1;}
	elsif($VS_ELWEA == 2 && $PL_ELWEA == 0){$Vs_AntiEl = 1;}
	elsif($VS_ELWEA == 3 && $PL_ELWEA == 1){$Vs_AntiEl = 1;}
	elsif($VS_ELWEA == 4 && $PL_ELWEA == 5){$Vs_AntiEl = 1;}
	elsif($VS_ELWEA == 5 && $PL_ELWEA == 4){$Vs_AntiEl = 1;}

	#フォースエンスは無条件で打ち消す
	if($PL_sS[0] eq "フォースエンス"){$Vs_AntiEl = 1;}
	if($VS_sS[0] eq "フォースエンス"){$Pl_AntiEl = 1;}

#	if($PL_W[7] =~ m/!00/ && $VS_W[7] =~ m/!02/){$Pl_AntiEl = 1;}
#	elsif($PL_W[7] =~ m/!01/ && $VS_W[7] =~ m/!03/){$Pl_AntiEl = 1;}
#	elsif($PL_W[7] =~ m/!02/ && $VS_W[7] =~ m/!00/){$Pl_AntiEl = 1;}
#	elsif($PL_W[7] =~ m/!03/ && $VS_W[7] =~ m/!01/){$Pl_AntiEl = 1;}
#	elsif($PL_W[7] =~ m/!04/ && $VS_W[7] =~ m/!05/){$Pl_AntiEl = 1;}
#	elsif($PL_W[7] =~ m/!05/ && $VS_W[7] =~ m/!04/){$Pl_AntiEl = 1;}
#	if($VS_W[7] =~ m/!00/ && $PL_W[7] =~ m/!02/){$Vs_AntiEl = 1;}
#	elsif($VS_W[7] =~ m/!01/ && $PL_W[7] =~ m/!03/){$Vs_AntiEl = 1;}
#	elsif($VS_W[7] =~ m/!02/ && $PL_W[7] =~ m/!00/){$Vs_AntiEl = 1;}
#	elsif($VS_W[7] =~ m/!03/ && $PL_W[7] =~ m/!01/){$Vs_AntiEl = 1;}
#	elsif($VS_W[7] =~ m/!04/ && $PL_W[7] =~ m/!05/){$Vs_AntiEl = 1;}
#	elsif($VS_W[7] =~ m/!05/ && $PL_W[7] =~ m/!04/){$Vs_AntiEl = 1;}

	$PL_WW = 0;
	$VS_WW = 0;

	#特殊・魔法を選択
	if($PL_sS[11] =~ m/5/ || !$PL_sS[0]){$PL_WW = 1;}
	if($VS_sS[11] =~ m/5/ || !$VS_sS[0]){$VS_WW = 1;}
##セット・特定クラス装備時処理追加 #20100915 両者の攻撃属性を引き継ぐ
	&SEINOU('b','PL','VS',$Pl_AntiEl,$PL_WW,$VS_ELWEA) if ($PL_W[7]=~ m/!6d/ || $PL_sS[7]=~ m/!6d/ || $PL_CLASS[17] =~ m/!E005/);
	&SEINOU('b','VS','PL',$Vs_AntiEl,$VS_WW,$PL_ELWEA) if ($VS_W[7]=~ m/!6d/ || $VS_sS[7]=~ m/!6d/ || $VS_CLASS[17] =~ m/!E005/);

#エンチャントシステム
	$PL_STR = $PL_VALUES[19];
	$PL_VIT = $PL_VALUES[20];
	$PL_AGI = $PL_VALUES[21];
	$PL_DEX = $PL_VALUES[22];
	$PL_INT = $PL_VALUES[57];
	$PL_MEN = $PL_VALUES[58];
	$PL_MIR = $PL_VALUES[59];
	$PL_AI = $PL_VALUES[60];

	$VS_STR = $VS_VALUES[19];
	$VS_VIT = $VS_VALUES[20];
	$VS_AGI = $VS_VALUES[21];
	$VS_DEX = $VS_VALUES[22];
	$VS_INT = $VS_VALUES[57];
	$VS_MEN = $VS_VALUES[58];
	$VS_MIR = $VS_VALUES[59];
	$VS_AI = $VS_VALUES[60];
	
	$PL_STRZAN=0;
	$PL_VITZAN=0;
	$PL_AGIZAN=0;
	$PL_DEXZAN=0;
	$PL_INTZAN=0;
	$PL_MENZAN=0;
	$PL_MIRZAN=0;
	$PL_AIZAN=0;

$TES="$PL_W[0]";
$TES12="$PL_W[12]";


#装備名の色変更
	#最上段
	@PL_Count_A = split(/!/,$PL_VALUES[9]);
	$PL_Ent_A = 0;
	for ($LngEntCntA = 3; $LngEntCntA <= 33; $LngEntCntA++){
		if($PL_Count_A[$LngEntCntA] > 0){$PL_Ent_A = $PL_Ent_A + 1;}
	}
	if($PL_Ent_A > 0 && $PL_Ent_A <= 2){$PL_W[0] = "<font color=00ff00>$PL_W[0]</font>";}
	elsif($PL_Ent_A > 2 && $PL_Ent_A <= 4){$PL_W[0] = "<font color=ffff00>$PL_W[0]</font>";}
	elsif($PL_Ent_A > 4){$PL_W[0] = "<font color=ffD700>$PL_W[0]</font>";}

	#2段目
	@PL_Count_B = split(/!/,$PL_VALUES[10]);
	$PL_Ent_B = 0;
	for ($LngEntCntB = 3; $LngEntCntB <= 33; $LngEntCntB++){
		if($PL_Count_B[$LngEntCntB] > 0){$PL_Ent_B = $PL_Ent_B + 1;}
	}
	if($PL_Ent_B > 0 && $PL_Ent_B <= 2){$PL_sB[0] = "<font color=00ff00>$PL_sB[0]</font>";}
	elsif($PL_Ent_B > 2 && $PL_Ent_B <= 4){$PL_sB[0] = "<font color=ffff00>$PL_sB[0]</font>";}
	elsif($PL_Ent_B > 4){$PL_sB[0] = "<font color=ffD700>$PL_sB[0]</font>";}
	
	#3段目
	@PL_Count_C = split(/!/,$PL_VALUES[11]);
	$PL_Ent_C = 0;
	for ($LngEntCntC = 3; $LngEntCntC <= 33; $LngEntCntC++){
		if($PL_Count_C[$LngEntCntC] > 0){$PL_Ent_C = $PL_Ent_C + 1;}
	}
	if($PL_Ent_C > 0 && $PL_Ent_C <= 2){$PL_sC[0] = "<font color=00ff00>$PL_sC[0]</font>";}
	elsif($PL_Ent_C > 2 && $PL_Ent_C <= 4){$PL_sC[0] = "<font color=ffff00>$PL_sC[0]</font>";}
	elsif($PL_Ent_C > 4){$PL_sC[0] = "<font color=ffD700>$PL_sC[0]</font>";}
	#4段目
	@PL_Count_D = split(/!/,$PL_VALUES[38]);
	$PL_Ent_D = 0;
	for ($LngEntCntD = 3; $LngEntCntD <= 33; $LngEntCntD++){
		if($PL_Count_D[$LngEntCntD] > 0){$PL_Ent_D = $PL_Ent_D + 1;}
	}
	if($PL_Ent_D > 0 && $PL_Ent_D <= 2){$PL_sD[0] = "<font color=00ff00>$PL_sD[0]</font>";}
	elsif($PL_Ent_D > 2 && $PL_Ent_D <= 4){$PL_sD[0] = "<font color=ffff00>$PL_sD[0]</font>";}
	elsif($PL_Ent_D > 4){$PL_sD[0] = "<font color=ffD700>$PL_sD[0]</font>";}
	
	@VS_Count_A = split(/!/,$VS_VALUES[9]);
	$VS_Ent_A = 0;
	for ($LngEntCntA = 3; $LngEntCntA <= 33; $LngEntCntA++){
		if($VS_Count_A[$LngEntCntA] > 0){$VS_Ent_A = $VS_Ent_A + 1;}
	}
	if($VS_Ent_A > 0 && $VS_Ent_A <= 2){$VS_W[0] = "<font color=00ff00>$VS_W[0]</font>";}
	elsif($VS_Ent_A > 2 && $VS_Ent_A <= 4){$VS_W[0] = "<font color=ffff00>$VS_W[0]</font>";}
	elsif($VS_Ent_A > 4){$VS_W[0] = "<font color=ffD700>$VS_W[0]</font>";}

	#2段目
	@VS_Count_B = split(/!/,$VS_VALUES[10]);
	$VS_Ent_B = 0;
	for ($LngEntCntB = 3; $LngEntCntB <= 33; $LngEntCntB++){
		if($VS_Count_B[$LngEntCntB] > 0){$VS_Ent_B = $VS_Ent_B + 1;}
	}
	if($VS_Ent_B > 0 && $VS_Ent_B <= 2){$VS_sB[0] = "<font color=00ff00>$VS_sB[0]</font>";}
	elsif($VS_Ent_B > 2 && $VS_Ent_B <= 4){$VS_sB[0] = "<font color=ffff00>$VS_sB[0]</font>";}
	elsif($VS_Ent_B > 4){$VS_sB[0] = "<font color=ffD700>$VS_sB[0]</font>";}
	
	#3段目
	@VS_Count_C = split(/!/,$VS_VALUES[11]);
	$VS_Ent_C = 0;
	for ($LngEntCntC = 3; $LngEntCntC <= 33; $LngEntCntC++){
		if($VS_Count_C[$LngEntCntC] > 0){$VS_Ent_C = $VS_Ent_C + 1;}
	}
	if($VS_Ent_C > 0 && $VS_Ent_C <= 2){$VS_sC[0] = "<font color=00ff00>$VS_sC[0]</font>";}
	elsif($VS_Ent_C > 2 && $VS_Ent_C <= 4){$VS_sC[0] = "<font color=ffff00>$VS_sC[0]</font>";}
	elsif($VS_Ent_C > 4){$VS_sC[0] = "<font color=ffD700>$VS_sC[0]</font>";}
	#4段目
	@VS_Count_D = split(/!/,$VS_VALUES[38]);
	$VS_Ent_D = 0;
	for ($LngEntCntD = 3; $LngEntCntD <= 33; $LngEntCntD++){
		if($VS_Count_D[$LngEntCntD] > 0){$VS_Ent_D = $VS_Ent_D + 1;}
	}
	if($VS_Ent_D > 0 && $VS_Ent_D <= 2){$VS_sD[0] = "<font color=00ff00>$VS_sD[0]</font>";}
	elsif($VS_Ent_D > 2 && $VS_Ent_D <= 4){$VS_sD[0] = "<font color=ffff00>$VS_sD[0]</font>";}
	elsif($VS_Ent_D > 4){$VS_sD[0] = "<font color=ffD700>$VS_sD[0]</font>";}

#&ERROR("$PL_WFAと$PL_W[4]");




	if($BattleLevel eq "1"){
		#最上段の武器
#		if($PL_W[14] =~ m/A02/){
#			$PL_W[1] = int($PL_W[1] * 0.97);
#		}
		#技
#		if($PL_sS[11] eq "5"){
#			$PL_sS[1]-=50;
#		}
		#魔法
		if(($PL_sS[11] eq "1" || $PL_sS[11] eq "2" || $PL_sS[11] eq "3") && $PL_sS[7] !~ m/!6k/){
			$PL_sS[1] = int($PL_sS[1]*0.9);
		}
		#特殊
		if(($PL_sS[11] eq "6" || $PL_sS[11] eq "7" || $PL_sS[11] eq "8") && ($PL_sS[1] ne "ソ\ニックブラスト")){
			$PL_sS[1] = int($PL_sS[1]*0.93);
		}
		#最上段の武器
#		if($VS_W[14] =~ m/A02/){
#			$VS_W[1] = int($VS_W[1] * 0.97);
#		}
		#技
#		if($VS_sS[11] eq "5"){
#			$VS_sS[1]-=50;
#		}
		#魔法
		if($VS_sS[11] eq "1" || $VS_sS[11] eq "2" || $VS_sS[11] eq "3"){
			$VS_sS[1] = int($VS_sS[1]*0.9);
		}
		#特殊
		if(($VS_sS[11] eq "6" || $VS_sS[11] eq "7" || $VS_sS[11] eq "8") && ($VS_sS[1] ne "ソ\ニックブラスト")){
			$VS_sS[1] = int($VS_sS[1]*0.93);
		}
	}


#装備強化システム
	if($PL_WAEnt ne "" & $PL_WAEnt > 0){$PL_W[0] = "＋$PL_WAEnt $PL_W[0]";}
	if($PL_WBEnt ne "" & $PL_WBEnt > 0){$PL_sB[0] = "＋$PL_WBEnt $PL_sB[0]";}
	if($PL_WCEnt ne "" & $PL_WCEnt > 0){$PL_sC[0] = "＋$PL_WCEnt $PL_sC[0]";}
	if($PL_WDEnt ne "" & $PL_WDEnt > 0){$PL_sD[0] = "＋$PL_WDEnt $PL_sD[0]";}


	if($VS_WAEnt ne "" & $VS_WAEnt > 0){$VS_W[0] = "＋$VS_WAEnt $VS_W[0]";}
	if($VS_WBEnt ne "" & $VS_WBEnt > 0){$VS_sB[0] = "＋$VS_WBEnt $VS_sB[0]";}
	if($VS_WCEnt ne "" & $VS_WCEnt > 0){$VS_sC[0] = "＋$VS_WCEnt $VS_sC[0]";}
	if($VS_WDEnt ne "" & $VS_WDEnt > 0){$VS_sD[0] = "＋$VS_WDEnt $VS_sD[0]";}
	if($VS_WSEnt ne "" & $VS_WSEnt > 0){$VS_sS[0] = "＋$VS_WSEnt $VS_sS[0]";}
#&ERROR("$VS_WSEnt");
#補助魔法選択	攻撃専用
	$PL_HS = 0;
	if($FORM{'Hosentaku'} ne "" && ($FORM{'Hosentaku'} eq "41" || $FORM{'Hosentaku'} eq "42"|| $FORM{'Hosentaku'} eq "43")){

		$PL_HS = 1;
#		$PL_LVHH = int($PL_LVH/$WEAPON_LVUP);
		@PL_H=split(/\,/,$WEAPON_LIST{"$PL_WH"});

		if($PL_WHEnt ne "" & $PL_WHEnt > 0){
			$PL_sS[0] = "＋$PL_WHEnt $PL_sS[0]";
		}

	}
	else{
		if($PL_WSEnt ne "" & $PL_WSEnt > 0){
			$PL_sS[0] = "＋$PL_WSEnt $PL_sS[0]";
			
			#強化反映
			
			
		}
	}

#トランキライズ　自分・相手の装備品効果を無効化　属性除く
	if($PL_H[7] =~ m/!8v/){

		if($PL_sS[0]){$PL_sS[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($PL_W[0]){$PL_W[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($PL_sB[0]){$PL_sB[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($PL_sC[0]){$PL_sC[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($PL_sD[0]){$PL_sD[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($VS_sS[0]){$VS_sS[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($VS_W[0]){$VS_W[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($VS_sB[0]){$VS_sB[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($VS_sC[0]){$VS_sC[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}
		if($VS_sD[0]){$VS_sD[7] =~ s/!20|!21|!22|!23|!24|!25|!26|!27|!28|!29|!2a|!2b|!2c|!2d|!2e|!2f|!2g|!2h|!2i|!2j|!2k|!2o|!2p|!2q|!2r|!2s|!40|!41|!42|!43|!44|!45|!46|!47|!48|!49|!4a|!4b/!xx/g;}

	}

#20190423 強化値リセット
	$PL_ReGoth = 0;
	if($PL_WAEnt > 0){$PL_ReGoth = $PL_ReGoth + int(($PL_WAEnt + 1)*($PL_WAEnt / 2) * 100000);$PL_WAEnt=0;}
	if($PL_WBEnt > 0){$PL_ReGoth = $PL_ReGoth + int(($PL_WBEnt + 1)*($PL_WBEnt / 2) * 100000);$PL_WBEnt=0;}
	if($PL_WCEnt > 0){$PL_ReGoth = $PL_ReGoth + int(($PL_WCEnt + 1)*($PL_WCEnt / 2) * 100000);$PL_WCEnt=0;}
	if($PL_WDEnt > 0){$PL_ReGoth = $PL_ReGoth + int(($PL_WDEnt + 1)*($PL_WDEnt / 2) * 100000);$PL_WDEnt=0;}
	if($PL_WHEnt > 0){$PL_WHEnt = 0;}
	if($PL_WSEnt > 0){$PL_WSEnt = 0;}

	if($VS_WAEnt > 0){$VS_ReGoth = $VS_ReGoth + int(($VS_WAEnt + 1)*($VS_WAEnt / 2) * 100000);$VS_WAEnt=0;}
	if($VS_WBEnt > 0){$VS_ReGoth = $VS_ReGoth + int(($VS_WBEnt + 1)*($VS_WBEnt / 2) * 100000);$VS_WBEnt=0;}
	if($VS_WCEnt > 0){$VS_ReGoth = $VS_ReGoth + int(($VS_WCEnt + 1)*($VS_WCEnt / 2) * 100000);$VS_WCEnt=0;}
	if($VS_WDEnt > 0){$VS_ReGoth = $VS_ReGoth + int(($VS_WDEnt + 1)*($VS_WDEnt / 2) * 100000);$VS_WDEnt=0;}
	if($VS_WSEnt > 0){$VS_WSEnt = 0;}

	$PL_VALUES[8]=$PL_VALUES[8]+$PL_ReGoth;
	$VS_VALUES[8]=$VS_VALUES[8]+$VS_ReGoth;

#装備強化反映
	$PL_REDPoint = 0;
	$VS_REDPoint = 0;
	
	$PL_SHDPointENT = 0;
	$VS_SHDPointENT = 0;
	
	$PL_REDPerPoint = 1;
	$VS_REDPerPoint = 1;

	$PL_ToreEntPoint = 0;
	$VS_ToreEntPoint = 0;

	$PL_MFEntPoint = 0;
	$VS_MFEntPoint = 0;

	$PL_GothEntPoint = 0;
	$VS_GothEntPoint = 0;


	if($PL_WAEnt ne "" & $PL_WAEnt > 0){
		#杖以外の武器
		if($PL_W[14] =~ m/A02/ && $PL_W[14] !~ m/A15/){
			$PL_W[1] = $PL_W[1] + int(30 * $PL_WAEnt / $PL_W[3]);
			$PL_W[2] = $PL_W[2] + int(1 * $PL_WAEnt / 5);
			$PL_W[4] = $PL_W[4] - int(2 * $PL_WAEnt / 10);
			if($PL_W[4] < 40){$PL_W[4] = 40;}
		#杖の場合
		}elsif($PL_W[14] =~ m/A02/ && $PL_W[14] =~ m/A15/){
			$PL_W[1] = $PL_W[1] + int(10 * $PL_WAEnt / $PL_W[3]);
			$PL_W[2] = $PL_W[2] + int(1 * $PL_WAEnt / 5);
			$PL_W[4] = $PL_W[4] - int(2 * $PL_WAEnt / 10);
			if($PL_W[4] < 40){$PL_W[4] = 40;}
		#盾の場合
		}elsif($PL_W[14] =~ m/A29/){
			$PL_REDPoint = $PL_REDPoint + 30 * $PL_WAEnt;
			$PL_SHDPointENT = $PL_SHDPointENT + int(1 * $PL_WAEnt / 10);
		#体防具
		}elsif($PL_W[14] =~ m/A28/){
			$PL_REDPoint = $PL_REDPoint + 50 * $PL_WAEnt;
			$PL_REDPerPoint = $PL_REDPerPoint - (int($PL_WAEnt / 10) * 0.01);
		#頭防具
		}elsif($PL_W[14] =~ m/A27/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WAEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WAEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WAEnt / 10);
		#装飾品
		}elsif($PL_W[14] =~ m/A30/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WAEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WAEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WAEnt / 10);
		}
	}
	if($PL_WBEnt ne "" & $PL_WBEnt > 0){

		#杖の場合
		if($PL_sB[14] =~ m/A02/ && $PL_sB[14] =~ m/A15/){
			$PL_sB[1] = $PL_sB[1] + int(10 * $PL_WBEnt / $PL_sB[3]);
			$PL_sB[2] = $PL_sB[2] + int(1 * $PL_WBEnt / 5);
			$PL_sB[4] = $PL_sB[4] - int(2 * $PL_WBEnt / 10);
			if($PL_sB[4] < 40){$PL_sB[4] = 40;}
		#盾の場合
		}elsif($PL_sB[14] =~ m/A29/){
			$PL_REDPoint = $PL_REDPoint + 30 * $PL_WBEnt;
			$PL_SHDPointENT = $PL_SHDPointENT + int(1 * $PL_WBEnt / 10);
		#体防具
		}elsif($PL_sB[14] =~ m/A28/){
			$PL_REDPoint = $PL_REDPoint + 50 * $PL_WBEnt;
			$PL_REDPerPoint = $PL_REDPerPoint - (int($PL_WBEnt / 10) * 0.01);
		#頭防具
		}elsif($PL_sB[14] =~ m/A27/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WBEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WBEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WBEnt / 10);
		#装飾品
		}elsif($PL_sB[14] =~ m/A30/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WBEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WBEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WBEnt / 10);
		}

	}

	if($PL_WCEnt ne "" & $PL_WCEnt > 0){

		#杖の場合
		if($PL_sC[14] =~ m/A02/ && $PL_sC[14] =~ m/A15/){
			$PL_sC[1] = $PL_sC[1] + int(10 * $PL_WCEnt / $PL_sC[3]);
			$PL_sC[2] = $PL_sC[2] + int(1 * $PL_WCEnt / 5);
			$PL_sC[4] = $PL_sC[4] - int(2 * $PL_WCEnt / 10);
			if($PL_sC[4] < 40){$PL_sC[4] = 40;}
		#盾の場合
		}elsif($PL_sC[14] =~ m/A29/){
			$PL_REDPoint = $PL_REDPoint + 30 * $PL_WCEnt;
			$PL_SHDPointENT = $PL_SHDPointENT + int(1 * $PL_WCEnt / 10);
		#体防具
		}elsif($PL_sC[14] =~ m/A28/){
			$PL_REDPoint = $PL_REDPoint + 50 * $PL_WCEnt;
			$PL_REDPerPoint = $PL_REDPerPoint - (int($PL_WCEnt / 10) * 0.01);
		#頭防具
		}elsif($PL_sC[14] =~ m/A27/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WCEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WCEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WCEnt / 10);
		#装飾品
		}elsif($PL_sC[14] =~ m/A30/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WCEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WCEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WCEnt / 10);
		}

	}

	if($PL_WDEnt ne "" & $PL_WDEnt > 0){

		#杖の場合
		if($PL_sD[14] =~ m/A02/ && $PL_sD[14] =~ m/A15/){
			$PL_sD[1] = $PL_sD[1] + int(10 * $PL_WDEnt / $PL_sD[3]);
			$PL_sD[2] = $PL_sD[2] + int(1 * $PL_WDEnt / 5);
			$PL_sD[4] = $PL_sD[4] - int(2 * $PL_WDEnt / 10);
			if($PL_sD[4] < 40){$PL_sD[4] = 40;}
		#盾の場合
		}elsif($PL_sD[14] =~ m/A29/){
			$PL_REDPoint = $PL_REDPoint + 30 * $PL_WDEnt;
			$PL_SHDPointENT = $PL_SHDPointENT + int(1 * $PL_WDEnt / 10);
		#体防具
		}elsif($PL_sD[14] =~ m/A28/){
			$PL_REDPoint = $PL_REDPoint + 50 * $PL_WDEnt;
			$PL_REDPerPoint = $PL_REDPerPoint - (int($PL_WDEnt / 10) * 0.01);
		#頭防具
		}elsif($PL_sD[14] =~ m/A27/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WDEnt;
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WDEnt / 5);
			$PL_MFEntPoint = $PL_MFEntPoint + int(1 * $PL_WDEnt / 10);
		#装飾品
		}elsif($PL_sD[14] =~ m/A30/){
			$PL_REDPoint = $PL_REDPoint + 10 * $PL_WDEnt;
			$PL_GothEntPoint = $PL_GothEntPoint + int(1 * $PL_WDEnt / 5);
			$PL_ToreEntPoint = $PL_ToreEntPoint + int(1 * $PL_WDEnt / 10);
		}

	}










	if($VS_WAEnt ne "" & $VS_WAEnt > 0){
		#杖以外の武器
		if($VS_W[14] =~ m/A02/ && $VS_W[14] !~ m/A15/){
			$VS_W[1] = $VS_W[1] + int(30 * $VS_WAEnt / $VS_W[3]);
			$VS_W[2] = $VS_W[2] + int(1 * $VS_WAEnt / 5);
			$VS_W[4] = $VS_W[4] - int(2 * $VS_WAEnt / 10);
			if($VS_W[4] < 40){$VS_W[4] = 40;}
		#杖の場合
		}elsif($VS_W[14] =~ m/A02/ && $VS_W[14] =~ m/A15/){
			$VS_W[1] = $VS_W[1] + int(10 * $VS_WAEnt / $VS_W[3]);
			$VS_W[2] = $VS_W[2] + int(1 * $VS_WAEnt / 5);
			$VS_W[4] = $VS_W[4] - int(2 * $VS_WAEnt / 10);
			if($VS_W[4] < 40){$VS_W[4] = 40;}
		#盾の場合
		}elsif($VS_W[14] =~ m/A29/){
			$VS_REDPoint = $VS_REDPoint + 30 * $VS_WAEnt;
			$VS_SHDPointENT = $VS_SHDPointENT + int(1 * $VS_WAEnt / 10);
		#体防具
		}elsif($VS_W[14] =~ m/A28/){
			$VS_REDPoint = $VS_REDPoint + 50 * $VS_WAEnt;
			$VS_REDPerPoint = $VS_REDPerPoint - (int($VS_WAEnt / 10) * 0.01);
		#頭防具
		}elsif($VS_W[14] =~ m/A27/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WAEnt;
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WAEnt / 5);
			$VS_MFEntPoint = $VS_MFEntPoint + int(1 * $VS_WAEnt / 10);
		#装飾品
		}elsif($VS_W[14] =~ m/A30/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WAEnt;
			$VS_GothEntPoint = $VS_GothEntPoint + int(1 * $VS_WAEnt / 5);
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WAEnt / 10);
		}
	}
	if($VS_WBEnt ne "" & $VS_WBEnt > 0){

		#杖の場合
		if($VS_sB[14] =~ m/A02/ && $VS_sB[14] =~ m/A15/){
			$VS_sB[1] = $VS_sB[1] + int(10 * $VS_WBEnt / $VS_sB[3]);
			$VS_sB[2] = $VS_sB[2] + int(1 * $VS_WBEnt / 5);
			$VS_sB[4] = $VS_sB[4] - int(2 * $VS_WBEnt / 10);
			if($VS_sB[4] < 40){$VS_sB[4] = 40;}
		#盾の場合
		}elsif($VS_sB[14] =~ m/A29/){
			$VS_REDPoint = $VS_REDPoint + 30 * $VS_WBEnt;
			$VS_SHDPointENT = $VS_SHDPointENT + int(1 * $VS_WBEnt / 10);
		#体防具
		}elsif($VS_sB[14] =~ m/A28/){
			$VS_REDPoint = $VS_REDPoint + 50 * $VS_WBEnt;
			$VS_REDPerPoint = $VS_REDPerPoint - (int($VS_WBEnt / 10) * 0.01);
		#頭防具
		}elsif($VS_sB[14] =~ m/A27/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WBEnt;
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WBEnt / 5);
			$VS_MFEntPoint = $VS_MFEntPoint + int(1 * $VS_WBEnt / 10);
		#装飾品
		}elsif($VS_sB[14] =~ m/A30/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WBEnt;
			$VS_GothEntPoint = $VS_GothEntPoint + int(1 * $VS_WBEnt / 5);
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WBEnt / 10);
		}

	}

	if($VS_WCEnt ne "" & $VS_WCEnt > 0){

		#杖の場合
		if($VS_sC[14] =~ m/A02/ && $VS_sC[14] =~ m/A15/){
			$VS_sC[1] = $VS_sC[1] + int(10 * $VS_WCEnt / $VS_sC[3]);
			$VS_sC[2] = $VS_sC[2] + int(1 * $VS_WCEnt / 5);
			$VS_sC[4] = $VS_sC[4] - int(2 * $VS_WCEnt / 10);
			if($VS_sC[4] < 40){$VS_sC[4] = 40;}
		#盾の場合
		}elsif($VS_sC[14] =~ m/A29/){
			$VS_REDPoint = $VS_REDPoint + 30 * $VS_WCEnt;
			$VS_SHDPointENT = $VS_SHDPointENT + int(1 * $VS_WCEnt / 10);
		#体防具
		}elsif($VS_sC[14] =~ m/A28/){
			$VS_REDPoint = $VS_REDPoint + 50 * $VS_WCEnt;
			$VS_REDPerPoint = $VS_REDPerPoint - (int($VS_WCEnt / 10) * 0.01);
		#頭防具
		}elsif($VS_sC[14] =~ m/A27/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WCEnt;
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WCEnt / 5);
			$VS_MFEntPoint = $VS_MFEntPoint + int(1 * $VS_WCEnt / 10);
		#装飾品
		}elsif($VS_sC[14] =~ m/A30/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WCEnt;
			$VS_GothEntPoint = $VS_GothEntPoint + int(1 * $VS_WCEnt / 5);
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WCEnt / 10);
		}

	}

	if($VS_WDEnt ne "" & $VS_WDEnt > 0){

		#杖の場合
		if($VS_sD[14] =~ m/A02/ && $VS_sD[14] =~ m/A15/){
			$VS_sD[1] = $VS_sD[1] + int(10 * $VS_WDEnt / $VS_sD[3]);
			$VS_sD[2] = $VS_sD[2] + int(1 * $VS_WDEnt / 5);
			$VS_sD[4] = $VS_sD[4] - int(2 * $VS_WDEnt / 10);
			if($VS_sD[4] < 40){$VS_sD[4] = 40;}
		#盾の場合
		}elsif($VS_sD[14] =~ m/A29/){
			$VS_REDPoint = $VS_REDPoint + 30 * $VS_WDEnt;
			$VS_SHDPointENT = $VS_SHDPointENT + int(1 * $VS_WDEnt / 10);
		#体防具
		}elsif($VS_sD[14] =~ m/A28/){
			$VS_REDPoint = $VS_REDPoint + 50 * $VS_WDEnt;
			$VS_REDPerPoint = $VS_REDPerPoint - (int($VS_WDEnt / 10) * 0.01);
		#頭防具
		}elsif($VS_sD[14] =~ m/A27/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WDEnt;
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WDEnt / 5);
			$VS_MFEntPoint = $VS_MFEntPoint + int(1 * $VS_WDEnt / 10);
		#装飾品
		}elsif($VS_sD[14] =~ m/A30/){
			$VS_REDPoint = $VS_REDPoint + 10 * $VS_WDEnt;
			$VS_GothEntPoint = $VS_GothEntPoint + int(1 * $VS_WDEnt / 5);
			$VS_ToreEntPoint = $VS_ToreEntPoint + int(1 * $VS_WDEnt / 10);
		}

	}



	#武器だけの情報をダミー配列で確保
	@PL_WDu = @PL_W;$PL_WDuLv=$PL_WLV;
	@VS_WDu = @VS_W;$VS_WDuLv=$VS_WLV;

	#VS側の41が回復魔法等の場合は迎撃は無効化する
	if($Vs_sS[7] =~ m/!6j|!6k|!6l/){@VS_sS=();}
	#特殊が存在する場合、装備品9の迎撃時のdecreaseを無効化
#	if($PL_sS[7] =~ m/!6s/){$PL_W[7] =~ s/!6s/!xx/g;}
#	if($VS_sS[7] =~ m/!6s/){$VS_W[7] =~ s/!6s/!xx/g;}
	if($PL_sS[0]){$PL_W[7] =~ s/!6s/!xx/g;}
	if($VS_sS[0]){$VS_W[7] =~ s/!6s/!xx/g;}
#		&ERROR("$PL_W[7]");

	$Pl_SSName = $Pl_sS[0];$Vs_SSName = $Vs_sS[0];

#ストックフラグ　武器攻撃、技攻撃時のみ立ちます
	$PL_STF = 1;

#特殊・魔法以外フラグ
	$Pl_WOnly = 0;
	$Vs_WOnly = 0;

#魔法フラグ
	$Pl_MOnly = 0;
	$Vs_MOnly = 0;

#弓以外フラグ
	$Pl_AOnly = 0;
	$Vs_AOnly = 0;

#		&ERROR("$PL_W[12]","$PL_sS[11]");
#$tes = "$PL_W[12]$PL_sS[12]";

#		&ERROR("$FORM{'sentaku'}");
##特殊を見る
#		$TES="$PL_W[0]";&ERROR("$PL_sS[12]","$PL_W[12]");
#$TES="$PL_W[0]";

#技補正用　Lv
$Pl_LvCalc = 0;$Pl_wazat=0;
$Vs_LvCalc = 0;$Vs_wazat=0;

#	if($PL_sS[11] !~ m/0/){$PL_LVS = 0;}
#	if($VS_sS[11] !~ m/0/){$VS_LVS = 0;}
	
	if($PL_sS[11] =~ m/1|2|3|4/){
		$PL_LVSS = int($PL_LVS/$WEAPON_LVUP);

#		#実験　魔法と武器の名前をくっつける
#		$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)<br>$PL_W[0]";

		#魔法をセット！
		#Aが杖・指輪・オーブの場合は組み合わせる
		if ($PL_W[7] =~ m/!13|!14|!15|!19/){
			$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)<br>$PL_W[0]";
#			$PL_W[1] = $PL_sS[1] + int($PL_W[1]/$PL_W[3]/7);
			$PL_W[1] = $PL_sS[1];
			$PL_W[2] = $PL_sS[2];
			$PL_W[3] = $PL_sS[3];
			$PL_W[4] = $PL_sS[4];
			
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;
			$PL_W[7] .= $PL_sS[7];

			$PL_WLV = $PL_LVS;

			$Pl_EEXP = 2;

			$PL_STF = 0;
			$Pl_MOnly = 1;

			#魔法使用時、片手情報をクリアする
			$PL_W[7] =~ s/!10/!xx/g;

		}else{
			#上記以外の場合は単に上書きする
			$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)";
			$PL_W[1] = $PL_sS[1];
			$PL_W[2] = $PL_sS[2];
			$PL_W[3] = $PL_sS[3];
			$PL_W[4] = $PL_sS[4];

			#武器の属性をダミーコードに書き換える
			$PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$PL_W[7] = $PL_sS[7];

			$PL_WLV = $PL_LVS;

			$Pl_EEXP = 1;

			$PL_STF = 0;
			$Pl_MOnly = 1;

			#魔法使用時、片手情報をクリアする
			$PL_W[7] =~ s/!10/!xx/g;

		}
#	}
	}elsif($PL_sS[11] =~ m/5/){
		$PL_STF = 0;				#ストック不可
		$Pl_WOnly = 1;

		$PL_LVSS = int($PL_LVS/$WEAPON_LVUP);
		$Pl_tekiyo = 0;

#		&ERROR("$PL_sS[12]ざあ$PL_W[12]");

		#得意補正をぶつける
		if($PL_CLASS[17] =~ m/!W001/ && $PL_W[12] =~ m/e001/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W002/ && $PL_W[12] =~ m/e001/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W003/ && $PL_W[12] =~ m/e002/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W004/ && $PL_W[12] =~ m/e002/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W005/ && $PL_W[12] =~ m/e003/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W006/ && $PL_W[12] =~ m/e003/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W007/ && $PL_W[12] =~ m/e004/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W008/ && $PL_W[12] =~ m/e004/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W009/ && $PL_W[12] =~ m/e007/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W010/ && $PL_W[12] =~ m/e007/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W011/ && $PL_W[12] =~ m/e008/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W012/ && $PL_W[12] =~ m/e008/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W013/ && $PL_W[12] =~ m/e010/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W014/ && $PL_W[12] =~ m/e012/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W015/ && $PL_W[12] =~ m/e012/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W016/ && $PL_W[12] =~ m/e013/){$PL_W[1] = int($PL_W[1] * 1.05);}
		elsif($PL_CLASS[17] =~ m/!W017/ && $PL_W[12] =~ m/e013/){$PL_W[1] = int($PL_W[1] * 1.02);$PL_W[2]+=3;}

		if($PL_W[12] =~ m/e001/ && $PL_sS[12] =~ m/e001/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e002/ && $PL_sS[12] =~ m/e002/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e003/ && $PL_sS[12] =~ m/e003/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e004/ && $PL_sS[12] =~ m/e004/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e005/ && $PL_sS[12] =~ m/e005/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e006/ && $PL_sS[12] =~ m/e006/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e007/ && $PL_sS[12] =~ m/e007/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e008/ && $PL_sS[12] =~ m/e008/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e009/ && $PL_sS[12] =~ m/e009/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e010/ && $PL_sS[12] =~ m/e010/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e011/ && $PL_sS[12] =~ m/e011/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e012/ && $PL_sS[12] =~ m/e012/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e013/ && $PL_sS[12] =~ m/e013/){$Pl_tekiyo = 1;}
		if($PL_W[12] =~ m/e014/ && $PL_sS[12] =~ m/e014/){$Pl_tekiyo = 1;}

		if($Pl_tekiyo eq "1"){

			$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)<br>$PL_W[0]";

			#回数補正なしの攻撃力加算
			if($PL_sS[12] !~ m/ef001/){
				$PL_W[1]=int($PL_W[1] * ($PL_sS[1]/1000));
			}
			#命中
			$PL_W[2]=int($PL_W[2] + $PL_sS[2]);
			#回数　回数補正有り時のみ　　攻撃力の計算も行う
			$CalcA=0;
			if($PL_sS[12] =~ m/ef001/){

				$CalcA=int($PL_W[1]*$PL_W[3]);
#				$WN_sA[3] = $WN_sS[3];
				$CalcA=$CalcA/$PL_sS[3];
				$PL_sS[1]=int($CalcA * ($PL_sS[1]/1000));
				$PL_W[1]=$PL_sS[1];
				$PL_W[3] = $PL_sS[3];
#				&ERROR("$PL_W[1]ああ$PL_W[3]");

			}
			#MP加算
			$PL_W[4]=$PL_W[4]+$PL_sS[4];


			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$PL_W[7] .= $PL_sS[7];

			$Pl_wazat=1;
			$Pl_LvCalc = $PL_WLV;
			$PL_WLV = $PL_LVS;

			$Pl_EEXP = 2;
			$Pl_AOnly = 1;

		}else{
			$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)";
			if($PL_sS[12] =~ m/ef001/){
				$PL_W[1] = int($PL_sS[1]/$PL_sS[3]);
			}else{
				$PL_W[1] = $PL_sS[1];
			}

			$PL_W[2] = $PL_sS[2];

			$PL_W[3] = $PL_sS[3];

			$PL_W[4] = $PL_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$PL_W[7] = $PL_sS[7];

			$PL_WLV = $PL_LVS;

			$Pl_EEXP = 1;
		}

	}elsif($PL_sS[11] =~ m/6|7|8/){
		$PL_LVSS = int($PL_LVS/$WEAPON_LVUP);

		#Aが指輪・オーブの場合は組み合わせる
		if ($PL_W[7] =~ m/!13|!14/){
			$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)<br>$PL_W[0]";
			$PL_W[1] = $PL_sS[1];
			$PL_W[2] = $PL_sS[2];
			$PL_W[3] = $PL_sS[3];
			$PL_W[4] = $PL_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$PL_W[7] .= $PL_sS[7];

			$PL_WLV = $PL_LVS;

			$Pl_EEXP = 2;

			$PL_STF = 0;
		}else{
			#上記以外の場合は単に上書きする
			$PL_W[0] = "$PL_sS[0](Level.$PL_LVSS)";
			$PL_W[1] = $PL_sS[1];
			$PL_W[2] = $PL_sS[2];
			$PL_W[3] = $PL_sS[3];
			$PL_W[4] = $PL_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$PL_W[7] = $PL_sS[7];

			$PL_WLV = $PL_LVS;

			$Pl_EEXP = 1;

			$PL_STF = 0;
		}

	}else{
	#武器攻撃ONLY
		$Pl_WOnly = 1;
		$Pl_AOnly = 1;
		#得意補正をぶつける
		if($PL_CLASS[17] =~ m/!W001/ && $PL_W[12] =~ m/e001/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W002/ && $PL_W[12] =~ m/e001/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W003/ && $PL_W[12] =~ m/e002/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W004/ && $PL_W[12] =~ m/e002/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W005/ && $PL_W[12] =~ m/e003/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W006/ && $PL_W[12] =~ m/e003/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W007/ && $PL_W[12] =~ m/e004/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W008/ && $PL_W[12] =~ m/e004/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W009/ && $PL_W[12] =~ m/e007/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W010/ && $PL_W[12] =~ m/e007/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W011/ && $PL_W[12] =~ m/e008/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W012/ && $PL_W[12] =~ m/e008/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W013/ && $PL_W[12] =~ m/e010/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W014/ && $PL_W[12] =~ m/e012/){$PL_W[1] = int($PL_W[1] * 1.02);}
		elsif($PL_CLASS[17] =~ m/!W015/ && $PL_W[12] =~ m/e012/){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2]+=3;}
		elsif($PL_CLASS[17] =~ m/!W016/ && $PL_W[12] =~ m/e013/){$PL_W[1] = int($PL_W[1] * 1.05);}
		elsif($PL_CLASS[17] =~ m/!W017/ && $PL_W[12] =~ m/e013/){$PL_W[1] = int($PL_W[1] * 1.02);$PL_W[2]+=3;}

	}


	#ネクロマンシーは加算しない
	if($VS_sS[11] =~ m/1|2|3|4/ && $VS_sS[7] !~ m/!77/){
		$VS_LVSS = int($VS_LVS/$WEAPON_LVUP);

#		#実験　魔法と武器の名前をくっつける
#		$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)<br>$VS_W[0]";

		#魔法をセット！
		#Aが杖・指輪・オーブの場合は組み合わせる
		if ($VS_W[7] =~ m/!13|!14|!15|!19/){
			$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)<br>$VS_W[0]";
#			$VS_W[1] = $VS_sS[1] + int($VS_W[1]/$VS_W[3]/7);
			$VS_W[1] = $VS_sS[1];
			$VS_W[2] = $VS_sS[2];
			$VS_W[3] = $VS_sS[3];
			$VS_W[4] = $VS_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$VS_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$VS_W[7] .= $VS_sS[7];

			$VS_WLV = $VS_LVS;

			$Vs_MOnly = 1;
			$Vs_EEXP = 2;

			#魔法使用時、片手情報をクリアする
			$VS_W[7] =~ s/!10/!xx/g;

		}else{
			#上記以外の場合は単に上書きする
			$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)";
			$VS_W[1] = $VS_sS[1];
			$VS_W[2] = $VS_sS[2];
			$VS_W[3] = $VS_sS[3];
			$VS_W[4] = $VS_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$VS_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$VS_W[7] = $VS_sS[7];

			$VS_WLV = $VS_LVS;

			$Vs_EEXP = 1;
			$Vs_MOnly = 1;

			#魔法使用時、片手情報をクリアする
			$VS_W[7] =~ s/!10/!xx/g;

		}
#	}
	}elsif($VS_sS[11] =~ m/5/){
		$VS_STF = 0;				#ストック不可
		$Vs_WOnly = 1;

		$VS_LVSS = int($VS_LVS/$WEAPON_LVUP);
		$Vs_tekiyo = 0;

		#得意補正をぶつける
		if($VS_CLASS[17] =~ m/!W001/ && $VS_W[12] =~ m/e001/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W002/ && $VS_W[12] =~ m/e001/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W003/ && $VS_W[12] =~ m/e002/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W004/ && $VS_W[12] =~ m/e002/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W005/ && $VS_W[12] =~ m/e003/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W006/ && $VS_W[12] =~ m/e003/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W007/ && $VS_W[12] =~ m/e004/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W008/ && $VS_W[12] =~ m/e004/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W009/ && $VS_W[12] =~ m/e007/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W010/ && $VS_W[12] =~ m/e007/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W011/ && $VS_W[12] =~ m/e008/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W012/ && $VS_W[12] =~ m/e008/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W013/ && $VS_W[12] =~ m/e010/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W014/ && $VS_W[12] =~ m/e012/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W015/ && $VS_W[12] =~ m/e012/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W016/ && $VS_W[12] =~ m/e013/){$VS_W[1] = int($VS_W[1] * 1.05);}
		elsif($VS_CLASS[17] =~ m/!W017/ && $VS_W[12] =~ m/e013/){$VS_W[1] = int($VS_W[1] * 1.02);$VS_W[2]+=3;}

		if($VS_W[12] =~ m/e001/ && $VS_sS[12] =~ m/e001/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e002/ && $VS_sS[12] =~ m/e002/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e003/ && $VS_sS[12] =~ m/e003/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e004/ && $VS_sS[12] =~ m/e004/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e005/ && $VS_sS[12] =~ m/e005/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e006/ && $VS_sS[12] =~ m/e006/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e007/ && $VS_sS[12] =~ m/e007/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e008/ && $VS_sS[12] =~ m/e008/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e009/ && $VS_sS[12] =~ m/e009/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e010/ && $VS_sS[12] =~ m/e010/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e011/ && $VS_sS[12] =~ m/e011/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e012/ && $VS_sS[12] =~ m/e012/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e013/ && $VS_sS[12] =~ m/e013/){$Vs_tekiyo = 1;}
		if($VS_W[12] =~ m/e014/ && $VS_sS[12] =~ m/e014/){$Vs_tekiyo = 1;}
		if($Vs_tekiyo eq "1"){

			$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)<br>$VS_W[0]";

			#回数補正なしの攻撃力加算
			if($VS_sS[12] !~ m/ef001/){
				$VS_W[1]=int($VS_W[1] * ($VS_sS[1]/1000));
			}
			#命中
			$VS_W[2]=int($VS_W[2] + $VS_sS[2]);
			#回数　回数補正有り時のみ　　攻撃力の計算も行う
			$CalcA=0;
			if($VS_sS[12] =~ m/ef001/){

				$CalcA=int($VS_W[1]*$VS_W[3]);
#				$WN_sA[3] = $WN_sS[3];
				$CalcA=$CalcA/$VS_sS[3];
				$VS_sS[1]=int($CalcA * ($VS_sS[1]/1000));
				$VS_W[1]=$VS_sS[1];
				$VS_W[3] = $VS_sS[3];
#				&ERROR("$VS_W[1]ああ$VS_W[3]");

			}
			#MP加算
			$VS_W[4]=$VS_W[4]+$VS_sS[4];


			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$VS_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$VS_W[7] .= $VS_sS[7];

			$Vs_wazat=1;
			$Vs_LvCalc = $VS_WLV;
			$VS_WLV = $VS_LVS;

			$Vs_EEXP = 2;
			$Vs_AOnly = 1;

		}else{
			$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)";

			if($VS_sS[12] =~ m/ef001/){
				$VS_W[1] = int($VS_sS[1]/$VS_sS[3]);
			}else{
				$VS_W[1] = $VS_sS[1];
			}

			$VS_W[1] = $VS_sS[1];
			$VS_W[2] = $VS_sS[2];
			$VS_W[3] = $VS_sS[3];
			$VS_W[4] = $VS_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$VS_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$VS_W[7] = $VS_sS[7];

			$VS_WLV = $VS_LVS;

			$Vs_EEXP = 1;
		}



	}elsif($VS_sS[11] =~ m/6|7|8/){
		$VS_LVSS = int($VS_LVS/$WEAPON_LVUP);

		#Aが指輪・オーブの場合は組み合わせる
		if ($VS_W[7] =~ m/!13|!14/){
			$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)<br>$VS_W[0]";
			$VS_W[1] = $VS_sS[1];
			$VS_W[2] = $VS_sS[2];
			$VS_W[3] = $VS_sS[3];
			$VS_W[4] = $VS_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$VS_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$VS_W[7] .= $VS_sS[7];

			$VS_WLV = $VS_LVS;

			$Vs_EEXP = 2;
		}else{
			#上記以外の場合は単に上書きする
			$VS_W[0] = "$VS_sS[0](Level.$VS_LVSS)";
			$VS_W[1] = $VS_sS[1];
			$VS_W[2] = $VS_sS[2];
			$VS_W[3] = $VS_sS[3];
			$VS_W[4] = $VS_sS[4];
			#武器の属性をダミーコードに書き換える　Sが無属性なら書き換えない？
			$VS_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

			$VS_W[7] = $VS_sS[7];

			$VS_WLV = $VS_LVS;

			$Vs_EEXP = 1;
		}

	}else{
		#得意補正をぶつける
		$Vs_WOnly = 1;
		$Vs_AOnly = 1;
		if($VS_CLASS[17] =~ m/!W001/ && $VS_W[12] =~ m/e001/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W002/ && $VS_W[12] =~ m/e001/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W003/ && $VS_W[12] =~ m/e002/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W004/ && $VS_W[12] =~ m/e002/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W005/ && $VS_W[12] =~ m/e003/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W006/ && $VS_W[12] =~ m/e003/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W007/ && $VS_W[12] =~ m/e004/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W008/ && $VS_W[12] =~ m/e004/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W009/ && $VS_W[12] =~ m/e007/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W010/ && $VS_W[12] =~ m/e007/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W011/ && $VS_W[12] =~ m/e008/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W012/ && $VS_W[12] =~ m/e008/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W013/ && $VS_W[12] =~ m/e010/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W014/ && $VS_W[12] =~ m/e012/){$VS_W[1] = int($VS_W[1] * 1.02);}
		elsif($VS_CLASS[17] =~ m/!W015/ && $VS_W[12] =~ m/e012/){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2]+=3;}
		elsif($VS_CLASS[17] =~ m/!W016/ && $VS_W[12] =~ m/e013/){$VS_W[1] = int($VS_W[1] * 1.05);}
		elsif($VS_CLASS[17] =~ m/!W017/ && $VS_W[12] =~ m/e013/){$VS_W[1] = int($VS_W[1] * 1.02);$VS_W[2]+=3;}


	}


#補助魔法の効果を加算　基本的に如何なるパターンでも効果を加算
	if($PL_HS eq "1"){

		$DumW = "$PL_H[0]<br>";
		$DumW .= "$PL_W[0]";
		$DumW2 = "$PL_W[0]";
		$PL_W[0] = $DumW;
		$PL_W[4] += $PL_H[4];

		$HoEle = 0;
		#ユニットエレメントとの補正
		#風
		#炎
		if($PL_W[7]=~ m/!01/ && $PL_VALUES[31] eq "1"){$HoEle = 1;}
		#大地
		#水
		if($PL_W[7]=~ m/!03/ && $PL_VALUES[31] eq "3"){$HoEle = 1;}

		#確認後、補助魔法側の属性を消して受け継がせる
		$PL_H[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;

		$PL_W[7] .= $PL_H[7];

	}

#魔導器Lv3ボーナス　ダメージ25％軽減
	if($Pl_maba eq "1"){$VS_W[1] = int($VS_W[1] * 0.75);}
	if($Vs_maba eq "1"){$PL_W[1] = int($PL_W[1] * 0.75);}

#物理攻撃時、命中半減
	if($Pl_WOnly eq "1" && $PL_CLASS[17] =~ m/!W019/){$PL_W[2] = int($PL_W[2]/2);}
	if($Vs_WOnly eq "1" && $VS_CLASS[17] =~ m/!W019/){$VS_W[2] = int($VS_W[2]/2);}

#L・N恐怖付与　対戦相手がL・N時は攻撃力5％低下　防御力5％低下
	if($VS_VALUES[12] >= 36 && ($PL_sB[0] =~ m/!E0039/ || $PL_sC[0] =~ m/!E0039/ || $PL_sD[0] =~ m/!E0039/)){
		$PL_W[1] = int($PL_W[1] * 1.05);
		$VS_W[1] = int($VS_W[1] * 0.95);
	}

	if($PL_VALUES[12] >= 36 && ($VS_sB[0] =~ m/!E0039/ || $VS_sC[0] =~ m/!E0039/ || $VS_sD[0] =~ m/!E0039/)){
		$VS_W[1] = int($VS_W[1] * 1.05);
		$PL_W[1] = int($PL_W[1] * 0.95);
	}

#テレポート処理時　自分・相手の攻撃・命中を0にする
	if($PL_W[7] =~ m/!8e|!8f/){

		$PL_W[1] = 100;$PL_W[2] = 0;#$PL_W[0]="TEST";
		$VS_W[1] = 100;$VS_W[2] = 0;$VS_W[7] = "";

	}
	#補助魔法　攻撃では激減
	if($PL_W[7] =~ m/!8g/ && $PL_W[7] !~ m/!8k|!8l|!8m|!8o|!8p|!8q|!8r|!8s/){
		$PL_W[1] = 100;$PL_W[2] = 0;#$PL_W[0]="TEST";
	}elsif($VS_W[7] =~ m/!8g/ && $VS_W[7] !~ m/!8k|!8l|!8m|!8o|!8p|!8q|!8r|!8s/){
		$VS_W[1] = 100;$VS_W[2] = 0;
	}

	#神聖系補助魔法は除外
	if($PL_W[7] =~ m/!8w/ && $PL_W[7] !~ m/!8t|!8u|!8v/){
		$PL_W[1] = 100;$PL_W[2] = 0;#$PL_W[0]="TEST";
	}elsif($VS_W[7] =~ m/!8w/ && $VS_W[7] !~ m/!8t|!8u|!8v/){
		$VS_W[1] = 100;$VS_W[2] = 0;
	}

#デフ系補正
	@CC=split(/!/,$CL_VALUES[46]);
	#本隊
	if($CC[1] > time && $PL_VALUES[28] eq ""){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水 0123
		if($CC[0] eq "1"){
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[0] eq "2"){
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[0] eq "3"){
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[0] eq "4"){
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}

	}
	if($CC[3] > time && $PL_VALUES[28] eq $CL_VALUES[2]){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($CC[2] eq "1"){
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[2] eq "2"){
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[2] eq "3"){
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[2] eq "4"){
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}

	}
	if($CC[5] > time && $PL_VALUES[28] eq $CL_VALUES[3]){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($CC[4] eq "1"){
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[4] eq "2"){
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[4] eq "3"){
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[4] eq "4"){
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}

	}
	if($CC[7] > time && $PL_VALUES[28] eq $CL_VALUES[4]){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($CC[6] eq "1"){
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[6] eq "2"){
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[6] eq "3"){
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}elsif($CC[6] eq "4"){
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 1.2);}
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 0.8);}
		}

	}

	@VCC=split(/!/,$VC_VALUES[46]);
	#本隊
	if($VCC[1] > time && $VS_VALUES[28] eq ""){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($VCC[0] eq "1"){
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[0] eq "2"){
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[0] eq "3"){
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[0] eq "4"){
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}

	}
	if($VCC[3] > time && $VS_VALUES[28] eq $CL_VALUES[2]){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($VCC[2] eq "1"){
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[2] eq "2"){
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[2] eq "3"){
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[2] eq "4"){
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}

	}
	if($VCC[5] > time && $VS_VALUES[28] eq $CL_VALUES[3]){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($VCC[4] eq "1"){
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[4] eq "2"){
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[4] eq "3"){
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[4] eq "4"){
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}

	}
	if($VCC[7] > time && $VS_VALUES[28] eq $CL_VALUES[4]){

		#自分武器属性と一致　1：風　2：炎　3：大地　4：水
		if($VCC[6] eq "1"){
			if($VS_W[7]=~ m/!00/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!02/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[6] eq "2"){
			if($VS_W[7]=~ m/!01/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!03/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[6] eq "3"){
			if($VS_W[7]=~ m/!02/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!00/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}elsif($VCC[6] eq "4"){
			if($VS_W[7]=~ m/!03/){$VS_W[1] = int($VS_W[1] * 1.2);}
			if($PL_W[7]=~ m/!01/){$PL_W[1] = int($PL_W[1] * 0.8);}
		}

	}
#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0){

		#シールドブレイク
#		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0074/ || $ABI_sB[2] =~ m/!A0074/ || $ABI_sC[2] =~ m/!A0074/) && rand(100) < 30 + $PL_VALUES[14]){
		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0074/ || $ABI_sB[2] =~ m/!A0074/ || $ABI_sC[2] =~ m/!A0074/)){
			if($VS_sB[7] =~ m/!12/){@VS_sB=();}
			if($VS_sC[7] =~ m/!12/){@VS_sC=();}
			if($VS_sD[7] =~ m/!12/){@VS_sD=();}
		
		}
#		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0074/ || $VABI_sB[2] =~ m/!A0074/ || $VABI_sC[2] =~ m/!A0074/) && rand(100) < 30 + $VS_VALUES[14]){
		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0074/ || $VABI_sB[2] =~ m/!A0074/ || $VABI_sC[2] =~ m/!A0074/)){
		
			if($PL_sB[7] =~ m/!12/){@PL_sB=();}
			if($PL_sC[7] =~ m/!12/){@PL_sC=();}
			if($PL_sD[7] =~ m/!12/){@PL_sD=();}
		
		}

		#アーマーブレイク
#		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0089/ || $ABI_sB[2] =~ m/!A0089/ || $ABI_sC[2] =~ m/!A0089/) && rand(100) < 30 + $PL_VALUES[14]){
		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0089/ || $ABI_sB[2] =~ m/!A0089/ || $ABI_sC[2] =~ m/!A0089/)){
		
			if($VS_sB[7] =~ m/!1s|!1u|!1w/){@VS_sB=();}
			if($VS_sC[7] =~ m/!1s|!1u|!1w/){@VS_sC=();}
			if($VS_sD[7] =~ m/!1s|!1u|!1w/){@VS_sD=();}
		
		}
#		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0089/ || $VABI_sB[2] =~ m/!A0089/ || $VABI_sC[2] =~ m/!A0089/) && rand(100) < 30 + $VS_VALUES[14]){
		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0089/ || $VABI_sB[2] =~ m/!A0089/ || $VABI_sC[2] =~ m/!A0089/)){
		
			if($PL_sB[7] =~ m/!1s|!1u|!1w/){@PL_sB=();}
			if($PL_sC[7] =~ m/!1s|!1u|!1w/){@PL_sC=();}
			if($PL_sD[7] =~ m/!1s|!1u|!1w/){@PL_sD=();}
		
		}

		#ヘッドブレイク
#		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0090/ || $ABI_sB[2] =~ m/!A0090/ || $ABI_sC[2] =~ m/!A0090/) && rand(100) < 30 + $PL_VALUES[14]){
		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0090/ || $ABI_sB[2] =~ m/!A0090/ || $ABI_sC[2] =~ m/!A0090/)){
		
			if($VS_sB[7] =~ m/!1t|!1v|!1x/){@VS_sB=();}
			if($VS_sC[7] =~ m/!1t|!1v|!1x/){@VS_sC=();}
			if($VS_sD[7] =~ m/!1t|!1v|!1x/){@VS_sD=();}
		
		}
#		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0090/ || $VABI_sB[2] =~ m/!A0090/ || $VABI_sC[2] =~ m/!A0090/) && rand(100) < 30 + $VS_VALUES[14]){
		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0090/ || $VABI_sB[2] =~ m/!A0090/ || $VABI_sC[2] =~ m/!A0090/)){
		
			if($PL_sB[7] =~ m/!1t|!1v|!1x/){@PL_sB=();}
			if($PL_sC[7] =~ m/!1t|!1v|!1x/){@PL_sC=();}
			if($PL_sD[7] =~ m/!1t|!1v|!1x/){@PL_sD=();}
		
		}
		
		#アクセサリを狙う
		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0105/ || $ABI_sB[2] =~ m/!A0105/ || $ABI_sC[2] =~ m/!A0105/)){
		
			if($VS_sB[7] =~ m/!13|!14|!16|!17/){@VS_sB=();}
			if($VS_sC[7] =~ m/!13|!14|!16|!17/){@VS_sC=();}
			if($VS_sD[7] =~ m/!13|!14|!16|!17/){@VS_sD=();}
		
		}
		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0105/ || $VABI_sB[2] =~ m/!A0105/ || $VABI_sC[2] =~ m/!A0105/)){
		
			if($PL_sB[7] =~ m/!13|!14|!16|!17/){@PL_sB=();}
			if($PL_sC[7] =~ m/!13|!14|!16|!17/){@PL_sC=();}
			if($PL_sD[7] =~ m/!13|!14|!16|!17/){@PL_sD=();}
		
		}
		
		#アタッカー
		if($PL_VALUES[14] >= 15 && ($Pl_WOnly eq "1" || $PL_sS[0] eq "怒号魔破拳") && ($ABI_sA[2] =~ m/!A0007/ || $ABI_sB[2] =~ m/!A0007/ || $ABI_sC[2] =~ m/!A0007/)){$PL_W[1] = int($PL_W[1] * 1.15);}
		#ディフェンダー
		if($PL_VALUES[14] >= 15 && ($ABI_sA[2] =~ m/!A0008/ || $ABI_sB[2] =~ m/!A0008/ || $ABI_sC[2] =~ m/!A0008/)){$VS_W[1] = int($VS_W[1] * 0.85);}
		#マジックブースト
		if($PL_VALUES[14] >= 15 && ($Pl_WOnly ne "1" && $PL_sS[0] ne "怒号魔破拳") && ($ABI_sA[2] =~ m/!A0009/ || $ABI_sB[2] =~ m/!A0009/ || $ABI_sC[2] =~ m/!A0009/)){$PL_W[1] = int($PL_W[1] * 1.15);}
		#チェイサー
		if($PL_VALUES[14] >= 15 && ($ABI_sA[2] =~ m/!A0010/ || $ABI_sB[2] =~ m/!A0010/ || $ABI_sC[2] =~ m/!A0010/)){$VS_W[2] = int($VS_W[2] * 0.8);}
		#スナイパー
		if($PL_VALUES[14] >= 15 && ($ABI_sA[2] =~ m/!A0011/ || $ABI_sB[2] =~ m/!A0011/ || $ABI_sC[2] =~ m/!A0011/)){$PL_W[2] = int($PL_W[2] * 1.2);}

		#斬り払い
		if($PL_W[12] =~ m/e001|e012|e013/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0017/ || $ABI_sB[2] =~ m/!A0017/ || $ABI_sC[2] =~ m/!A0017/)){$VS_W[2] = int($VS_W[2] * 0.85);}
		if($VS_W[12] =~ m/e001|e012|e013/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0017/ || $VABI_sB[2] =~ m/!A0017/ || $VABI_sC[2] =~ m/!A0017/)){$PL_W[2] = int($PL_W[2] * 0.85);}
		#撃ち落とし
		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0018/ || $ABI_sB[2] =~ m/!A0018/ || $ABI_sC[2] =~ m/!A0018/)){$VS_W[2] = int($VS_W[2] * 0.9);}
		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0018/ || $VABI_sB[2] =~ m/!A0018/ || $VABI_sC[2] =~ m/!A0018/)){$PL_W[2] = int($PL_W[2] * 0.9);}

		#槍修練
		if($PL_W[12] =~ m/e007/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0021/ || $ABI_sB[2] =~ m/!A0021/ || $ABI_sC[2] =~ m/!A0021/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e007/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0021/ || $VABI_sB[2] =~ m/!A0021/ || $VABI_sC[2] =~ m/!A0021/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#剣修練
		if($PL_W[12] =~ m/e001/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0022/ || $ABI_sB[2] =~ m/!A0022/ || $ABI_sC[2] =~ m/!A0022/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e001/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0022/ || $VABI_sB[2] =~ m/!A0022/ || $VABI_sC[2] =~ m/!A0022/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#斧修練
		if($PL_W[12] =~ m/e002/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0023/ || $ABI_sB[2] =~ m/!A0023/ || $ABI_sC[2] =~ m/!A0023/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e002/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0023/ || $VABI_sB[2] =~ m/!A0023/ || $VABI_sC[2] =~ m/!A0023/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#刀修練
		if($PL_W[12] =~ m/e012/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0024/ || $ABI_sB[2] =~ m/!A0024/ || $ABI_sC[2] =~ m/!A0024/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e012/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0024/ || $VABI_sB[2] =~ m/!A0024/ || $VABI_sC[2] =~ m/!A0024/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#突剣修練
		if($PL_W[12] =~ m/e013/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0025/ || $ABI_sB[2] =~ m/!A0025/ || $ABI_sC[2] =~ m/!A0025/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e013/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0025/ || $VABI_sB[2] =~ m/!A0025/ || $VABI_sC[2] =~ m/!A0025/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#槌修練
		if($PL_W[12] =~ m/e003/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0026/ || $ABI_sB[2] =~ m/!A0026/ || $ABI_sC[2] =~ m/!A0026/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e003/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0026/ || $VABI_sB[2] =~ m/!A0026/ || $VABI_sC[2] =~ m/!A0026/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#爪修練
		if($PL_W[12] =~ m/e004/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0027/ || $ABI_sB[2] =~ m/!A0027/ || $ABI_sC[2] =~ m/!A0027/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e004/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0027/ || $VABI_sB[2] =~ m/!A0027/ || $VABI_sC[2] =~ m/!A0027/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#弓修練
		if($PL_W[12] =~ m/e009/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0028/ || $ABI_sB[2] =~ m/!A0028/ || $ABI_sC[2] =~ m/!A0028/)){$PL_W[1] = int($PL_W[1] * 1.07);$PL_W[2] = int($PL_W[2] * 1.07);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e009/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0028/ || $VABI_sB[2] =~ m/!A0028/ || $VABI_sC[2] =~ m/!A0028/)){$VS_W[1] = int($VS_W[1] * 1.07);$VS_W[2] = int($VS_W[2] * 1.07);$VS_W[4] = int($VS_W[4]*0.85);}
		#銃修練
		if($PL_W[12] =~ m/e011/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0029/ || $ABI_sB[2] =~ m/!A0029/ || $ABI_sC[2] =~ m/!A0029/)){$PL_W[1] = int($PL_W[1] * 1.05);$PL_W[2] = int($PL_W[2] * 1.05);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e011/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0029/ || $VABI_sB[2] =~ m/!A0029/ || $VABI_sC[2] =~ m/!A0029/)){$VS_W[1] = int($VS_W[1] * 1.05);$VS_W[2] = int($VS_W[2] * 1.05);$VS_W[4] = int($VS_W[4]*0.85);}
		#鞭修練
		if($PL_W[12] =~ m/e008/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0030/ || $ABI_sB[2] =~ m/!A0030/ || $ABI_sC[2] =~ m/!A0030/)){$PL_W[1] = int($PL_W[1] * 1.04);$PL_W[2] = int($PL_W[2] * 1.04);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e008/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0030/ || $VABI_sB[2] =~ m/!A0030/ || $VABI_sC[2] =~ m/!A0030/)){$VS_W[1] = int($VS_W[1] * 1.04);$VS_W[2] = int($VS_W[2] * 1.04);$VS_W[4] = int($VS_W[4]*0.85);}
		#人形修練
		if($PL_W[12] =~ m/e014/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0031/ || $ABI_sB[2] =~ m/!A0031/ || $ABI_sC[2] =~ m/!A0031/)){$PL_W[1] = int($PL_W[1] * 1.20);$PL_W[2] = int($PL_W[2] * 1.20);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e014/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0031/ || $VABI_sB[2] =~ m/!A0031/ || $VABI_sC[2] =~ m/!A0031/)){$VS_W[1] = int($VS_W[1] * 1.20);$VS_W[2] = int($VS_W[2] * 1.20);$VS_W[4] = int($VS_W[4]*0.85);}
		#吹き矢修練
		if($PL_W[12] =~ m/e010/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0032/ || $ABI_sB[2] =~ m/!A0032/ || $ABI_sC[2] =~ m/!A0032/)){$PL_W[1] = int($PL_W[1] * 1.1);$PL_W[2] = int($PL_W[2] * 1.1);$PL_W[4] = int($PL_W[4]*0.85);}
		if($VS_W[12] =~ m/e010/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0032/ || $VABI_sB[2] =~ m/!A0032/ || $VABI_sC[2] =~ m/!A0032/)){$VS_W[1] = int($VS_W[1] * 1.1);$VS_W[2] = int($VS_W[2] * 1.1);$VS_W[4] = int($VS_W[4]*0.85);}

		#弾道学
		
		#弓懸

		#竜の恩寵
		if($PL_W[7] =~ m/!1k/ && ($ABI_sA[2] =~ m/!A0093/ || $ABI_sB[2] =~ m/!A0093/ || $ABI_sC[2] =~ m/!A0093/)){$PL_W[1] = int($PL_W[1] * 1.3);$PL_W[2] = int($PL_W[2] * 1.3);}
		if($VS_W[7] =~ m/!1k/ && ($VABI_sA[2] =~ m/!A0093/ || $VABI_sB[2] =~ m/!A0093/ || $VABI_sC[2] =~ m/!A0093/)){$VS_W[1] = int($VS_W[1] * 1.3);$VS_W[2] = int($VS_W[2] * 1.3);}

		#レジストファイア
		if($VS_W[7] =~ m/!01/ && ($ABI_sA[2] =~ m/!A0039/ || $ABI_sB[2] =~ m/!A0039/ || $ABI_sC[2] =~ m/!A0039/)){$VS_W[1] = int($VS_W[1] * 0.5);}
		if($PL_W[7] =~ m/!01/ && ($VABI_sA[2] =~ m/!A0039/ || $VABI_sB[2] =~ m/!A0039/ || $VABI_sC[2] =~ m/!A0039/)){$PL_W[1] = int($PL_W[1] * 0.5);}
		#レジストウォータ
		if($VS_W[7] =~ m/!03/ && ($ABI_sA[2] =~ m/!A0040/ || $ABI_sB[2] =~ m/!A0040/ || $ABI_sC[2] =~ m/!A0040/)){$VS_W[1] = int($VS_W[1] * 0.5);}
		if($PL_W[7] =~ m/!03/ && ($VABI_sA[2] =~ m/!A0040/ || $VABI_sB[2] =~ m/!A0040/ || $VABI_sC[2] =~ m/!A0040/)){$PL_W[1] = int($PL_W[1] * 0.5);}
		#レジストウインド
		if($VS_W[7] =~ m/!00/ && ($ABI_sA[2] =~ m/!A0041/ || $ABI_sB[2] =~ m/!A0041/ || $ABI_sC[2] =~ m/!A0041/)){$VS_W[1] = int($VS_W[1] * 0.5);}
		if($PL_W[7] =~ m/!00/ && ($VABI_sA[2] =~ m/!A0041/ || $VABI_sB[2] =~ m/!A0041/ || $VABI_sC[2] =~ m/!A0041/)){$PL_W[1] = int($PL_W[1] * 0.5);}
		#レジストアース
		if($VS_W[7] =~ m/!02/ && ($ABI_sA[2] =~ m/!A0042/ || $ABI_sB[2] =~ m/!A0042/ || $ABI_sC[2] =~ m/!A0042/)){$VS_W[1] = int($VS_W[1] * 0.5);}
		if($PL_W[7] =~ m/!02/ && ($VABI_sA[2] =~ m/!A0042/ || $VABI_sB[2] =~ m/!A0042/ || $VABI_sC[2] =~ m/!A0042/)){$PL_W[1] = int($PL_W[1] * 0.5);}
		#レジストセイント
		if($VS_W[7] =~ m/!04/ && ($ABI_sA[2] =~ m/!A0043/ || $ABI_sB[2] =~ m/!A0043/ || $ABI_sC[2] =~ m/!A0043/)){$VS_W[1] = int($VS_W[1] * 0.25);}
		if($PL_W[7] =~ m/!04/ && ($VABI_sA[2] =~ m/!A0043/ || $VABI_sB[2] =~ m/!A0043/ || $VABI_sC[2] =~ m/!A0043/)){$PL_W[1] = int($PL_W[1] * 0.25);}
		#レジストダーク
		if($VS_W[7] =~ m/!05/ && ($ABI_sA[2] =~ m/!A0044/ || $ABI_sB[2] =~ m/!A0044/ || $ABI_sC[2] =~ m/!A0044/)){$VS_W[1] = int($VS_W[1] * 0.25);}
		if($PL_W[7] =~ m/!05/ && ($VABI_sA[2] =~ m/!A0044/ || $VABI_sB[2] =~ m/!A0044/ || $VABI_sC[2] =~ m/!A0044/)){$PL_W[1] = int($PL_W[1] * 0.25);}
		#レジストエーテル
		if($VS_W[7] !~ m/!00|!01|!02|!03|!04|!05/ && ($ABI_sA[2] =~ m/!A0045/ || $ABI_sB[2] =~ m/!A0045/ || $ABI_sC[2] =~ m/!A0045/)){$VS_W[1] = int($VS_W[1] * 0.25);}
		if($PL_W[7] !~ m/!00|!01|!02|!03|!04|!05/ && ($VABI_sA[2] =~ m/!A0045/ || $VABI_sB[2] =~ m/!A0045/ || $VABI_sC[2] =~ m/!A0045/)){$PL_W[1] = int($PL_W[1] * 0.25);}

#		#連撃
#		if(($ABI_sA[2] =~ m/!A0056/ || $ABI_sB[2] =~ m/!A0056/ || $ABI_sC[2] =~ m/!A0056/) && rand(100) < 30){
#			$PL_WHIT=20+rand(41);
#			$PL_W[3] = int($PL_W[3] * (100+$PL_WHIT) / 100);
#		}
#		if(($VABI_sA[2] =~ m/!A0056/ || $VABI_sB[2] =~ m/!A0056/ || $VABI_sC[2] =~ m/!A0056/) && rand(100) < 30){
#			$VS_WHIT=20+rand(41);
#			$VS_W[3] = int($VS_W[3] * (100+$VS_WHIT) / 100);
#		}

		#一刀一閃
		if($PL_W[12] =~ m/e012/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0102/ || $ABI_sB[2] =~ m/!A0102/ || $ABI_sC[2] =~ m/!A0102/) && rand(100) < 50){
			$PL_WHIT=10+rand(51);
			$PL_W[3] = int($PL_W[3] * (100+$PL_WHIT) / 100);
		}
		if($VS_W[12] =~ m/e012/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0102/ || $VABI_sB[2] =~ m/!A0102/ || $VABI_sC[2] =~ m/!A0102/) && rand(100) < 50){
			$VS_WHIT=10+rand(51);
			$VS_W[3] = int($VS_W[3] * (100+$VS_WHIT) / 100);
		}

		#弾道学
		if($PL_W[12] =~ m/e009|e010|e011/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0103/ || $ABI_sB[2] =~ m/!A0103/ || $ABI_sC[2] =~ m/!A0103/)){
			$PL_W[2] = int($PL_W[2] * 1.3);
		}
		if($VS_W[12] =~ m/e009|e010|e011/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0103/ || $VABI_sB[2] =~ m/!A0103/ || $VABI_sC[2] =~ m/!A0103/)){
			$VS_W[2] = int($VS_W[2] * 1.3);
		}

		#夜の恩寵　デメリット　神聖属性に弱い
		if($VS_W[7] =~ m/!04/ && ($PL_CLASS[17] =~ m/!E004/) && ($ABI_sA[2] =~ m/!A0094/ || $ABI_sB[2] =~ m/!A0094/ || $ABI_sC[2] =~ m/!A0094/)){
			$PL_CLASS[1] = $PL_CLASS[1] - 3;$PL_CLASS[2] = $PL_CLASS[2] - 3;$PL_CLASS[3] = $PL_CLASS[3] - 3;$PL_CLASS[4] = $PL_CLASS[4] - 3;
		}
		if($PL_W[7] =~ m/!04/ && ($VS_CLASS[17] =~ m/!E004/) && ($VABI_sA[2] =~ m/!A0094/ || $VABI_sB[2] =~ m/!A0094/ || $VABI_sC[2] =~ m/!A0094/)){
			$VS_CLASS[1] = $VS_CLASS[1] - 3;$VS_CLASS[2] = $VS_CLASS[2] - 3;$VS_CLASS[3] = $VS_CLASS[3] - 3;$VS_CLASS[4] = $VS_CLASS[4] - 3;
		}

		#アンデッド弱点属性 対戦相手の攻撃属性が神聖属性の場合は全補正-3　時間関係なし
		if($VS_W[7] =~ m/!04/ && ($PL_CLASS[17] =~ m/!E004/)){
			$PL_CLASS[1] = $PL_CLASS[1] - 3;$PL_CLASS[2] = $PL_CLASS[2] - 3;$PL_CLASS[3] = $PL_CLASS[3] - 3;$PL_CLASS[4] = $PL_CLASS[4] - 3;
		}
		if($PL_W[7] =~ m/!04/ && ($VS_CLASS[17] =~ m/!E004/)){
			$VS_CLASS[1] = $VS_CLASS[1] - 3;$VS_CLASS[2] = $VS_CLASS[2] - 3;$VS_CLASS[3] = $VS_CLASS[3] - 3;$VS_CLASS[4] = $VS_CLASS[4] - 3;
		}

		#消耗戦
		if($ABI_sA[2] =~ m/!A0073/ || $ABI_sB[2] =~ m/!A0073/ || $ABI_sC[2] =~ m/!A0073/){$PL_W[4]*=2;$VS_W[4]*=2;}
		if($VABI_sA[2] =~ m/!A0073/ || $VABI_sB[2] =~ m/!A0073/ || $VABI_sC[2] =~ m/!A0073/){$PL_W[4]*=2;$VS_W[4]*=2;}

		#貫通攻撃
		if($FORM{'yousai'} && ($ABI_sA[2] =~ m/!A0058/ || $ABI_sB[2] =~ m/!A0058/ || $ABI_sC[2] =~ m/!A0058/)){$PL_W[1]=int($PL_W[1]*1.2);}

		#反骨精神　瀕死になるほど攻撃力アップ

		#オーバードライブ
		if($ABI_sA[2] =~ m/!A0059/ || $ABI_sB[2] =~ m/!A0059/ || $ABI_sC[2] =~ m/!A0059/){$PL_W[1]=int($PL_W[1]*0.8);$VS_W[1]=int($VS_W[1]*0.8);}
		if($VABI_sA[2] =~ m/!A0059/ || $VABI_sB[2] =~ m/!A0059/ || $VABI_sC[2] =~ m/!A0059/){$PL_W[1]=int($PL_W[1]*0.8);$VS_W[1]=int($VS_W[1]*0.8);}

		#ファイアブースト
		if($PL_W[7] =~ m/!01/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0062/ || $ABI_sB[2] =~ m/!A0062/ || $ABI_sC[2] =~ m/!A0062/)){$PL_W[1] = int($PL_W[1] * 1.2);}
		if($VS_W[7] =~ m/!01/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0062/ || $VABI_sB[2] =~ m/!A0062/ || $VABI_sC[2] =~ m/!A0062/)){$VS_W[1] = int($VS_W[1] * 1.2);}
		#ウォータブースト
		if($PL_W[7] =~ m/!03/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0063/ || $ABI_sB[2] =~ m/!A0063/ || $ABI_sC[2] =~ m/!A0063/)){$PL_W[1] = int($PL_W[1] * 1.2);}
		if($VS_W[7] =~ m/!03/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0063/ || $VABI_sB[2] =~ m/!A0063/ || $VABI_sC[2] =~ m/!A0063/)){$VS_W[1] = int($VS_W[1] * 1.2);}
		#ウインドブースト
		if($PL_W[7] =~ m/!00/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0064/ || $ABI_sB[2] =~ m/!A0064/ || $ABI_sC[2] =~ m/!A0064/)){$PL_W[1] = int($PL_W[1] * 1.2);}
		if($VS_W[7] =~ m/!00/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0064/ || $VABI_sB[2] =~ m/!A0064/ || $VABI_sC[2] =~ m/!A0064/)){$VS_W[1] = int($VS_W[1] * 1.2);}
		#アースブースト
		if($PL_W[7] =~ m/!02/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0065/ || $ABI_sB[2] =~ m/!A0065/ || $ABI_sC[2] =~ m/!A0065/)){$PL_W[1] = int($PL_W[1] * 1.2);}
		if($VS_W[7] =~ m/!02/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0065/ || $VABI_sB[2] =~ m/!A0065/ || $VABI_sC[2] =~ m/!A0065/)){$VS_W[1] = int($VS_W[1] * 1.2);}
		#セイントブースト
		if($PL_W[7] =~ m/!04/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0066/ || $ABI_sB[2] =~ m/!A0066/ || $ABI_sC[2] =~ m/!A0066/)){$PL_W[1] = int($PL_W[1] * 1.1);}
		if($VS_W[7] =~ m/!04/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0066/ || $VABI_sB[2] =~ m/!A0066/ || $VABI_sC[2] =~ m/!A0066/)){$VS_W[1] = int($VS_W[1] * 1.1);}
		#ダークブースト
		if($PL_W[7] =~ m/!05/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0067/ || $ABI_sB[2] =~ m/!A0067/ || $ABI_sC[2] =~ m/!A0067/)){$PL_W[1] = int($PL_W[1] * 1.1);}
		if($VS_W[7] =~ m/!05/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0067/ || $VABI_sB[2] =~ m/!A0067/ || $VABI_sC[2] =~ m/!A0067/)){$VS_W[1] = int($VS_W[1] * 1.1);}		
		#エーテルブースト
		if($PL_W[7] !~ m/!00|!01|!02|!03|!04|!05/ && $Pl_WOnly ne "1"  && ($ABI_sA[2] =~ m/!A0068/ || $ABI_sB[2] =~ m/!A0068/ || $ABI_sC[2] =~ m/!A0068/)){$PL_W[1] = int($PL_W[1] * 1.1);}
		if($VS_W[7] !~ m/!00|!01|!02|!03|!04|!05/ && $Vs_WOnly ne "1"  && ($VABI_sA[2] =~ m/!A0068/ || $VABI_sB[2] =~ m/!A0068/ || $VABI_sC[2] =~ m/!A0068/)){$VS_W[1] = int($VS_W[1] * 1.1);}

		#四属性強化
		if($PL_W[7] =~ m/!00|!01|!02|!03/ && ($ABI_sA[2] =~ m/!A0120/ || $ABI_sB[2] =~ m/!A0120/ || $ABI_sC[2] =~ m/!A0120/)){$PL_W[1] = int($PL_W[1] * 1.2);}
		if($VS_W[7] =~ m/!00|!01|!02|!03/ && ($VABI_sA[2] =~ m/!A0120/ || $VABI_sB[2] =~ m/!A0120/ || $VABI_sC[2] =~ m/!A0120/)){$VS_W[1] = int($VS_W[1] * 1.2);}

		#攻補正アップ
		if($ABI_sA[2] =~ m/!A0046/ || $ABI_sB[2] =~ m/!A0046/ || $ABI_sC[2] =~ m/!A0046/){$PL_CLASS[1]+=1;}
		if($VABI_sA[2] =~ m/!A0046/ || $VABI_sB[2] =~ m/!A0046/ || $VABI_sC[2] =~ m/!A0046/){$VS_CLASS[1]+=1;}
		#防補正アップ
		if($ABI_sA[2] =~ m/!A0047/ || $ABI_sB[2] =~ m/!A0047/ || $ABI_sC[2] =~ m/!A0047/){$PL_CLASS[2]+=2;}
		if($VABI_sA[2] =~ m/!A0047/ || $VABI_sB[2] =~ m/!A0047/ || $VABI_sC[2] =~ m/!A0047/){$VS_CLASS[2]+=2;}
		#回補正アップ
		if($ABI_sA[2] =~ m/!A0048/ || $ABI_sB[2] =~ m/!A0048/ || $ABI_sC[2] =~ m/!A0048/){$PL_CLASS[3]+=3;}
		if($VABI_sA[2] =~ m/!A0048/ || $VABI_sB[2] =~ m/!A0048/ || $VABI_sC[2] =~ m/!A0048/){$VS_CLASS[3]+=3;}

		#回避ブースト
		if($ABI_sA[2] =~ m/!A0101/ || $ABI_sB[2] =~ m/!A0101/ || $ABI_sC[2] =~ m/!A0101/){$PL_CLASS[3]=$PL_CLASS[3]*2;}
		if($VABI_sA[2] =~ m/!A0101/ || $VABI_sB[2] =~ m/!A0101/ || $VABI_sC[2] =~ m/!A0101/){$VS_CLASS[3]=$VS_CLASS[3]*2;}

		#命補正アップ
		if($ABI_sA[2] =~ m/!A0049/ || $ABI_sB[2] =~ m/!A0049/ || $ABI_sC[2] =~ m/!A0049/){$PL_CLASS[4]+=3;}
		if($VABI_sA[2] =~ m/!A0049/ || $VABI_sB[2] =~ m/!A0049/ || $VABI_sC[2] =~ m/!A0049/){$VS_CLASS[4]+=3;}

		#先制行動
		$PL_SENSEI = 0;$VS_SENSEI = 0;
		if($ABI_sA[2] =~ m/!A0050/ || $ABI_sB[2] =~ m/!A0050/ || $ABI_sC[2] =~ m/!A0050/){$PL_SENSEI = 1;}
		if($VABI_sA[2] =~ m/!A0050/ || $VABI_sB[2] =~ m/!A0050/ || $VABI_sC[2] =~ m/!A0050/){$VS_SENSEI = 1;}
		#絶対後攻
		$PL_KOUKOU = 0;$VS_KOUKOU = 0;
		if($ABI_sA[2] =~ m/!A0051/ || $ABI_sB[2] =~ m/!A0051/ || $ABI_sC[2] =~ m/!A0051/){$PL_KOUKOU = 1;$VS_W[1] = int($VS_W[1] * 0.88);}
		if($VABI_sA[2] =~ m/!A0051/ || $VABI_sB[2] =~ m/!A0051/ || $VABI_sC[2] =~ m/!A0051/){$VS_KOUKOU = 1;$PL_W[1] = int($PL_W[1] * 0.88);}		
		#さきがけ
		$PL_SAKIGAKE = 0;$VS_SAKIGAKE = 0;
		if($ABI_sA[2] =~ m/!A0054/ || $ABI_sB[2] =~ m/!A0054/ || $ABI_sC[2] =~ m/!A0054/){$PL_SAKIGAKE = 1;$PL_W[1] = int($PL_W[1] * 0.75);}
		if($VABI_sA[2] =~ m/!A0054/ || $VABI_sB[2] =~ m/!A0054/ || $VABI_sC[2] =~ m/!A0054/){$VS_SAKIGAKE = 1;$VS_W[1] = int($VS_W[1] * 0.75);}		

		#カウンター　迎撃限定
		if($VABI_sA[2] =~ m/!A0053/ || $VABI_sB[2] =~ m/!A0053/ || $VABI_sC[2] =~ m/!A0053/){$PL_W[1] = int($PL_W[1] * 0.9);$VS_W[1] = int($VS_W[1] * 1.1);}

	}

#
#装備品による回避補正
	$PL_EQDOGPoint = 0;
	$VS_EQDOGPoint = 0;
	
	if($PL_W[16] > 0 && $PL_W[16] ne ""){$PL_EQDOGPoint = $PL_EQDOGPoint + $PL_W[16];}
	if($PL_sB[16] > 0 && $PL_sB[16] ne ""){$PL_EQDOGPoint = $PL_EQDOGPoint + $PL_sB[16];}
	if($PL_sC[16] > 0 && $PL_sC[16] ne ""){$PL_EQDOGPoint = $PL_EQDOGPoint + $PL_sC[16];}
	if($PL_sD[16] > 0 && $PL_sD[16] ne ""){$PL_EQDOGPoint = $PL_EQDOGPoint + $PL_sD[16];}

	if($VS_W[16] > 0 && $VS_W[16] ne ""){$VS_EQDOGPoint = $VS_EQDOGPoint + $VS_W[16];}
	if($VS_sB[16] > 0 && $VS_sB[16] ne ""){$VS_EQDOGPoint = $VS_EQDOGPoint + $VS_sB[16];}
	if($VS_sC[16] > 0 && $VS_sC[16] ne ""){$VS_EQDOGPoint = $VS_EQDOGPoint + $VS_sC[16];}
	if($VS_sD[16] > 0 && $VS_sD[16] ne ""){$VS_EQDOGPoint = $VS_EQDOGPoint + $VS_sD[16];}

	if($PL_EQDOGPoint > 0){$VS_W[2] = int($VS_W[2] * (100 - $PL_EQDOGPoint) / 100);}
	if($VS_EQDOGPoint > 0){$PL_W[2] = int($PL_W[2] * (100 - $VS_EQDOGPoint) / 100);}
	
	if($VS_W[2] < 5){$VS_W[2] = 5;}
	if($PL_W[2] < 5){$PL_W[2] = 5;}


	if($PL_W[7] !~ m/!1a/ && $PL_CLASS[17]=~ m/!E005/){$PL_W[1]=int($PL_W[1]*0.7);$PL_W[2]=int($PL_W[2]*0.7);$PL_W[4]+=40;if($PL_W[4]>4000){$PL_W[4]=4000;}}
	elsif($PL_W[7] =~ m/!1a/ && $PL_CLASS[17]=~ m/!E005/ && $Pl_AOnly ne '1'){$PL_W[1]=int($PL_W[1]*0.7);$PL_W[2]=int($PL_W[2]*0.7);$PL_W[4]+=40;if($PL_W[4]>4000){$PL_W[4]=4000;}}
	if($VS_W[7] !~ m/!1a/ && $VS_CLASS[17]=~ m/!E005/){$VS_W[1]=int($VS_W[1]*0.7);$VS_W[2]=int($VS_W[2]*0.7);$VS_W[4]+=40;if($VS_W[4]>4000){$VS_W[4]=4000;}}
	elsif($VS_W[7] =~ m/!1a/ && $VS_CLASS[17]=~ m/!E005/ && $Vs_AOnly ne '1'){$VS_W[1]=int($VS_W[1]*0.7);$VS_W[2]=int($VS_W[2]*0.7);$VS_W[4]+=40;if($VS_W[4]>4000){$VS_W[4]=4000;}}

#回復魔法強化　if $FORM{'b_mode'} eq '亡命';
	if($FORM{'b_mode'} eq '回復' && $PL_CLASS[17]=~ m/!E010/){

		#ヒーリングオールの消費MPを-100する
		if($PL_W[7]=~ m/!6k/){$PL_W[4] = $PL_W[4] - 100;}

		#ヒーリング、ヒーリングプラスの効力を+25％する
		if($PL_W[7]=~ m/!6j|!76/){$PL_W[1]=int($PL_W[1]*1.25);}

	}

#マインドバングル

	if($PL_W[7] =~ m/!E0038/ && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = int($PL_W[1] * 1.03);$PL_W[4] = int($PL_W[4] * 0.8);}
	if($PL_sB[7] =~ m/!E0038/ && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = int($PL_W[1] * 1.03);$PL_W[4] = int($PL_W[4] * 0.8);}
	if($PL_sC[7] =~ m/!E0038/ && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = int($PL_W[1] * 1.03);$PL_W[4] = int($PL_W[4] * 0.8);}
	if($PL_sD[7] =~ m/!E0038/ && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = int($PL_W[1] * 1.03);$PL_W[4] = int($PL_W[4] * 0.8);}

	if($VS_W[7] =~ m/!E0038/ && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = int($VS_W[1] * 1.03);$VS_W[4] = int($VS_W[4] * 0.8);}
	if($VS_sB[7] =~ m/!E0038/ && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = int($VS_W[1] * 1.03);$VS_W[4] = int($VS_W[4] * 0.8);}
	if($VS_sC[7] =~ m/!E0038/ && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = int($VS_W[1] * 1.03);$VS_W[4] = int($VS_W[4] * 0.8);}
	if($VS_sD[7] =~ m/!E0038/ && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = int($VS_W[1] * 1.03);$VS_W[4] = int($VS_W[4] * 0.8);}

	#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0 && $FORM{'b_mode'} eq '回復'){

		#回復修練
		if($ABI_sA[2] =~ m/!A0060/ || $ABI_sB[2] =~ m/!A0060/ || $ABI_sC[2] =~ m/!A0060/){$PL_W[1] = int($PL_W[1] * 1.25);$PL_W[4] = int($PL_W[4] * 0.75);}

	}

#クリスマス用　OF相手に対する攻撃力304倍
#	if(($DATE-$VS_VALUES[26]) < 1200 && $battleflag == 0 && $PL_W[7] !~ m/!6o/){
#	}else{
#		$PL_W[1]= int($PL_W[1] * 304);
#	}



#	if($PL_W[7] !~ m/!1a/ && $PL_CLASS[17]=~ m/!E005/){$$SF[1]=int($$SA[1]*0.7);$$SA[2]-=20;$$SA[4]+=40;}
#	elsif($$SA[7] =~ m/!1a/ && $$PS[17]=~ m/!E005/ && $_[1] eq 'PL' && $Pl_AOnly ne '1'){$$SF[1]=int($$SA[1]*0.7);$$SA[2]-=20;$$SA[4]+=40;}
#	elsif($$SA[7] =~ m/!1a/ && $$PS[17]=~ m/!E005/ && $_[1] eq 'VS' && $Vs_AOnly ne '1'){$$SF[1]=int($$SA[1]*0.7);$$SA[2]-=20;$$SA[4]+=40;}
#

#	if($PL_W[0] =~ m/アイアン/){&ERROR("$PL_sS[12]","$PL_W[12]");}

##クラス変化時処理追加
#	&GOUSEI('c1','PL','VS') if ($PL_VALUES[4] =~ /^64$|^65$|^70$|^71$|^72$|^131$|^132$|^133$|^134$|^135$|^203$/i);
#	&GOUSEI('c1','VS','PL') if ($VS_VALUES[4] =~ /^64$|^65$|^70$|^71$|^72$|^131$|^132$|^133$|^134$|^135$|^203$/i);
##クラス読み込み
#	require "./$LOG_FOLDER/$CLASS_DATA";
#	@PL_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});
#	@VS_CLASS=split(/\,/,$VCLASS_LIST{"$VS_VALUES[4]"});
####通常武器・合成魔法武器経験値処理
	&GOUSEI('k','PL','VS');
	&GOUSEI('k','VS','PL');
##セット・特定クラス装備時処理追加
#	&SEINOU('b','PL','VS') if ($PL_W[7]=~ m/!6d/);
#	&SEINOU('b','VS','PL') if ($VS_W[7]=~ m/!6d/);
##合成魔法装備時処理追加 20100326 凍結
#	&GOUSEI('g','PL','VS') if ($PL_W[7]=~ m/!1c/ && ($PL_sB[7]=~ m/!1c/ || $PL_sC[7]=~ m/!1c/ || $PL_sD[7]=~ m/!1c/));
#	&GOUSEI('g','VS','PL') if ($VS_W[7]=~ m/!1c/ && ($VS_sB[7]=~ m/!1c/ || $VS_sC[7]=~ m/!1c/ || $VS_sD[7]=~ m/!1c/));
##防具処理
#	&ELEMENT('via','PL','VS') if $PL_W[1] > 30 && $PL_W[7]!~ m/!6h/ && (($PL_W[7]=~ m/!10/ && ($PL_sB[7]=~ m/!12/ || $PL_sC[7]=~ m/!12/ || $PL_sD[7]=~ m/!12/)) || ($PL_W[7]=~ m/!18/ && $PL_CLASS[17] =~ m/!1/ && ($PL_sB[7]=~ m/!15|!19/ || $PL_sC[7]=~ m/!15|!19/ || $PL_sD[7]=~ m/!15|!19/)) || ($PL_sB[7]=~ m/!13|!14|!16|!17/ || $PL_sC[7]=~ m/!13|!14|!16|!17/ || $PL_sD[7]=~ m/!13|!14|!16|!17/) || ($PL_sB[7]=~ m/!1s|!1u|!1w/ || $PL_sC[7]=~ m/!1s|!1u|!1w/ || $PL_sD[7]=~m/!1s|!1u|!1w/) || ($PL_sB[7]=~ m/!1t|!1v|!1x/ || $PL_sC[7]=~ m/!1t|!1v|!1x/ || $PL_sD[7]=~m/!1t|!1v|!1x/));
#	&ELEMENT('via','VS','PL') if $VS_W[1] > 30 && $VS_W[7]!~ m/!6h/ && (($VS_W[7]=~ m/!10/ && ($VS_sB[7]=~ m/!12/ || $VS_sC[7]=~ m/!12/ || $VS_sD[7]=~ m/!12/)) || ($VS_W[7]=~ m/!18/ && $VS_CLASS[17] =~ m/!1/ && ($VS_sB[7]=~ m/!15|!19/ || $VS_sC[7]=~ m/!15|!19/ || $VS_sD[7]=~ m/!15|!19/)) || ($VS_sB[7]=~ m/!13|!14|!16|!17/ || $VS_sC[7]=~ m/!13|!14|!16|!17/ || $VS_sD[7]=~ m/!13|!14|!16|!17/) || ($VS_sB[7]=~ m/!1s|!1u|!1w/ || $VS_sC[7]=~ m/!1s|!1u|!1w/ || $VS_sD[7]=~m/!1s|!1u|!1w/) || ($VS_sB[7]=~ m/!1t|!1v|!1x/ || $VS_sC[7]=~ m/!1t|!1v|!1x/ || $VS_sD[7]=~m/!1t|!1v|!1x/));
	&ELEMENT('via','PL','VS') if $PL_W[7]!~ m/!6h/ && (($PL_W[7]=~ m/!10/ && ($PL_sB[7]=~ m/!12/ || $PL_sC[7]=~ m/!12/ || $PL_sD[7]=~ m/!12/)) || ($PL_W[7]=~ m/!18/ && $PL_CLASS[17] =~ m/!1|!E007|!E008/ && ($PL_sB[7]=~ m/!15|!19/ || $PL_sC[7]=~ m/!15|!19/ || $PL_sD[7]=~ m/!15|!19/)) || ($PL_sB[7]=~ m/!13|!14|!16|!17/ || $PL_sC[7]=~ m/!13|!14|!16|!17/ || $PL_sD[7]=~ m/!13|!14|!16|!17/) || ($PL_sB[7]=~ m/!1s|!1u|!1w/ || $PL_sC[7]=~ m/!1s|!1u|!1w/ || $PL_sD[7]=~m/!1s|!1u|!1w/) || ($PL_sB[7]=~ m/!1t|!1v|!1x|!E0003/ || $PL_sC[7]=~ m/!1t|!1v|!1x|!E0003/ || $PL_sD[7]=~m/!1t|!1v|!1x|!E0003/));
	&ELEMENT('via','VS','PL') if $VS_W[7]!~ m/!6h/ && (($VS_W[7]=~ m/!10/ && ($VS_sB[7]=~ m/!12/ || $VS_sC[7]=~ m/!12/ || $VS_sD[7]=~ m/!12/)) || ($VS_W[7]=~ m/!18/ && $VS_CLASS[17] =~ m/!1|!E007|!E008/ && ($VS_sB[7]=~ m/!15|!19/ || $VS_sC[7]=~ m/!15|!19/ || $VS_sD[7]=~ m/!15|!19/)) || ($VS_sB[7]=~ m/!13|!14|!16|!17/ || $VS_sC[7]=~ m/!13|!14|!16|!17/ || $VS_sD[7]=~ m/!13|!14|!16|!17/) || ($VS_sB[7]=~ m/!1s|!1u|!1w/ || $VS_sC[7]=~ m/!1s|!1u|!1w/ || $VS_sD[7]=~m/!1s|!1u|!1w/) || ($VS_sB[7]=~ m/!1t|!1v|!1x|!E0003/ || $VS_sC[7]=~ m/!1t|!1v|!1x|!E0003/ || $VS_sD[7]=~m/!1t|!1v|!1x|!E0003/));

#エンチャントシステム　※打ち消し処理後
	#最上段のエンチャント
	if($PL_flgEnt > 0){
		#魔法ブースト
		if($PL_WA08 ne "" && $PL_WA08 > 0 && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA08 * 0.01);}
		#火属性攻撃力
		if($PL_WA14 ne "" && $PL_WA14 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA14 * 0.007);}
		#水属性攻撃力
		if($PL_WA15 ne "" && $PL_WA15 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA15 * 0.007);}
		#大地属性攻撃力
		if($PL_WA16 ne "" && $PL_WA16 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA16 * 0.007);}
		#風属性攻撃力
		if($PL_WA17 ne "" && $PL_WA17 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA17 * 0.007);}
		#神聖属性攻撃力
		if($PL_WA18 ne "" && $PL_WA18 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA18 * 0.007);}
		#暗黒属性攻撃力
		if($PL_WA19 ne "" && $PL_WA19 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA19 * 0.007);}

		#火属性ダメージ軽減
		if($PL_WA20 ne "" && $PL_WA20 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA20 * 0.015);}
		#水属性ダメージ軽減
		if($PL_WA21 ne "" && $PL_WA21 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA21 * 0.015);}
		#大地属性ダメージ軽減
		if($PL_WA22 ne "" && $PL_WA22 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA22 * 0.015);}
		#風属性ダメージ軽減
		if($PL_WA23 ne "" && $PL_WA23 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA23 * 0.015);}
		#神聖属性ダメージ軽減
		if($PL_WA24 ne "" && $PL_WA24 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($PL_WA25 ne "" && $PL_WA25 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA25 * 0.015);}
		#無属性ダメージ軽減
		if($PL_WA26 ne "" && $PL_WA26 > 0 && $VS_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WA26 * 0.02);}
	}
	if($PL_flgEnt2 > 0){
		#魔法ブースト
		if($PL_WB08 ne "" && $PL_WB08 > 0 && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB08 * 0.01);}
		#火属性攻撃力
		if($PL_WB14 ne "" && $PL_WB14 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB14 * 0.007);}
		#水属性攻撃力
		if($PL_WB15 ne "" && $PL_WB15 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB15 * 0.007);}
		#大地属性攻撃力
		if($PL_WB16 ne "" && $PL_WB16 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB16 * 0.007);}
		#風属性攻撃力
		if($PL_WB17 ne "" && $PL_WB17 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB17 * 0.007);}
		#神聖属性攻撃力
		if($PL_WB18 ne "" && $PL_WB18 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB18 * 0.007);}
		#暗黒属性攻撃力
		if($PL_WB19 ne "" && $PL_WB19 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB19 * 0.007);}

		#火属性ダメージ軽減
		if($PL_WB20 ne "" && $PL_WB20 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB20 * 0.015);}
		#水属性ダメージ軽減
		if($PL_WB21 ne "" && $PL_WB21 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB21 * 0.015);}
		#大地属性ダメージ軽減
		if($PL_WB22 ne "" && $PL_WB22 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB22 * 0.015);}
		#風属性ダメージ軽減
		if($PL_WB23 ne "" && $PL_WB23 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB23 * 0.015);}
		#神聖属性ダメージ軽減
		if($PL_WB24 ne "" && $PL_WB24 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($PL_WB25 ne "" && $PL_WB25 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB25 * 0.015);}
		#無属性ダメージ軽減
		if($PL_WB26 ne "" && $PL_WB26 > 0 && $VS_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WB26 * 0.02);}
	}
	if($PL_flgEnt3 > 0){
		#魔法ブースト
		if($PL_WC08 ne "" && $PL_WC08 > 0 && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC08 * 0.01);}
		#火属性攻撃力
		if($PL_WC14 ne "" && $PL_WC14 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC14 * 0.007);}
		#水属性攻撃力
		if($PL_WC15 ne "" && $PL_WC15 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC15 * 0.007);}
		#大地属性攻撃力
		if($PL_WC16 ne "" && $PL_WC16 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC16 * 0.007);}
		#風属性攻撃力
		if($PL_WC17 ne "" && $PL_WC17 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC17 * 0.007);}
		#神聖属性攻撃力
		if($PL_WC18 ne "" && $PL_WC18 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC18 * 0.007);}
		#暗黒属性攻撃力
		if($PL_WC19 ne "" && $PL_WC19 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC19 * 0.007);}

		#火属性ダメージ軽減
		if($PL_WC20 ne "" && $PL_WC20 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC20 * 0.015);}
		#水属性ダメージ軽減
		if($PL_WC21 ne "" && $PL_WC21 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC21 * 0.015);}
		#大地属性ダメージ軽減
		if($PL_WC22 ne "" && $PL_WC22 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC22 * 0.015);}
		#風属性ダメージ軽減
		if($PL_WC23 ne "" && $PL_WC23 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC23 * 0.015);}
		#神聖属性ダメージ軽減
		if($PL_WC24 ne "" && $PL_WC24 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($PL_WC25 ne "" && $PL_WC25 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC25 * 0.015);}
		#無属性ダメージ軽減
		if($PL_WC26 ne "" && $PL_WC26 > 0 && $VS_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WC26 * 0.02);}
	}
	if($PL_flgEnt4 > 0){
		#魔法ブースト
		if($PL_WD08 ne "" && $PL_WD08 > 0 && $PL_sS[11] =~ m/1|2|3|4/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD08 * 0.01);}
		#火属性攻撃力
		if($PL_WD14 ne "" && $PL_WD14 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD14 * 0.007);}
		#水属性攻撃力
		if($PL_WD15 ne "" && $PL_WD15 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD15 * 0.007);}
		#大地属性攻撃力
		if($PL_WD16 ne "" && $PL_WD16 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD16 * 0.007);}
		#風属性攻撃力
		if($PL_WD17 ne "" && $PL_WD17 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD17 * 0.007);}
		#神聖属性攻撃力
		if($PL_WD18 ne "" && $PL_WD18 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD18 * 0.007);}
		#暗黒属性攻撃力
		if($PL_WD19 ne "" && $PL_WD19 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD19 * 0.007);}

		#火属性ダメージ軽減
		if($PL_WD20 ne "" && $PL_WD20 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD20 * 0.015);}
		#水属性ダメージ軽減
		if($PL_WD21 ne "" && $PL_WD21 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD21 * 0.015);}
		#大地属性ダメージ軽減
		if($PL_WD22 ne "" && $PL_WD22 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD22 * 0.015);}
		#風属性ダメージ軽減
		if($PL_WD23 ne "" && $PL_WD23 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD23 * 0.015);}
		#神聖属性ダメージ軽減
		if($PL_WD24 ne "" && $PL_WD24 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($PL_WD25 ne "" && $PL_WD25 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD25 * 0.015);}
		#無属性ダメージ軽減
		if($PL_WD26 ne "" && $PL_WD26 > 0 && $VS_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$VS_W[1] = $VS_W[1] - int($VS_W[1] * $PL_WD26 * 0.02);}
	}

	if($VS_flgEnt > 0){
		#魔法ブースト
		if($VS_WA08 ne "" && $VS_WA08 > 0 && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA08 * 0.01);}
		#火属性攻撃力
		if($VS_WA14 ne "" && $VS_WA14 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA14 * 0.007);}
		#水属性攻撃力
		if($VS_WA15 ne "" && $VS_WA15 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA15 * 0.007);}
		#大地属性攻撃力
		if($VS_WA16 ne "" && $VS_WA16 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA16 * 0.007);}
		#風属性攻撃力
		if($VS_WA17 ne "" && $VS_WA17 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA17 * 0.007);}
		#神聖属性攻撃力
		if($VS_WA18 ne "" && $VS_WA18 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA18 * 0.007);}
		#暗黒属性攻撃力
		if($VS_WA19 ne "" && $VS_WA19 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA19 * 0.007);}

		#火属性ダメージ軽減
		if($VS_WA20 ne "" && $VS_WA20 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA20 * 0.015);}
		#水属性ダメージ軽減
		if($VS_WA21 ne "" && $VS_WA21 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA21 * 0.015);}
		#大地属性ダメージ軽減
		if($VS_WA22 ne "" && $VS_WA22 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA22 * 0.015);}
		#風属性ダメージ軽減
		if($VS_WA23 ne "" && $VS_WA23 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA23 * 0.015);}
		#神聖属性ダメージ軽減
		if($VS_WA24 ne "" && $VS_WA24 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($VS_WA25 ne "" && $VS_WA25 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA25 * 0.015);}
		#無属性ダメージ軽減
		if($VS_WA26 ne "" && $VS_WA26 > 0 && $PL_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WA26 * 0.02);}
	}
	if($VS_flgEnt2 > 0){
		#魔法ブースト
		if($VS_WB08 ne "" && $VS_WB08 > 0 && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB08 * 0.01);}
		#火属性攻撃力
		if($VS_WB14 ne "" && $VS_WB14 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB14 * 0.007);}
		#水属性攻撃力
		if($VS_WB15 ne "" && $VS_WB15 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB15 * 0.007);}
		#大地属性攻撃力
		if($VS_WB16 ne "" && $VS_WB16 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB16 * 0.007);}
		#風属性攻撃力
		if($VS_WB17 ne "" && $VS_WB17 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB17 * 0.007);}
		#神聖属性攻撃力
		if($VS_WB18 ne "" && $VS_WB18 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB18 * 0.007);}
		#暗黒属性攻撃力
		if($VS_WB19 ne "" && $VS_WB19 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB19 * 0.007);}

		#火属性ダメージ軽減
		if($VS_WB20 ne "" && $VS_WB20 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB20 * 0.015);}
		#水属性ダメージ軽減
		if($VS_WB21 ne "" && $VS_WB21 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB21 * 0.015);}
		#大地属性ダメージ軽減
		if($VS_WB22 ne "" && $VS_WB22 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB22 * 0.015);}
		#風属性ダメージ軽減
		if($VS_WB23 ne "" && $VS_WB23 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB23 * 0.015);}
		#神聖属性ダメージ軽減
		if($VS_WB24 ne "" && $VS_WB24 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($VS_WB25 ne "" && $VS_WB25 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB25 * 0.015);}
		#無属性ダメージ軽減
		if($VS_WB26 ne "" && $VS_WB26 > 0 && $PL_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WB26 * 0.02);}
	}
	if($VS_flgEnt3 > 0){
		#魔法ブースト
		if($VS_WC08 ne "" && $VS_WC08 > 0 && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC08 * 0.01);}
		#火属性攻撃力
		if($VS_WC14 ne "" && $VS_WC14 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC14 * 0.007);}
		#水属性攻撃力
		if($VS_WC15 ne "" && $VS_WC15 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC15 * 0.007);}
		#大地属性攻撃力
		if($VS_WC16 ne "" && $VS_WC16 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC16 * 0.007);}
		#風属性攻撃力
		if($VS_WC17 ne "" && $VS_WC17 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC17 * 0.007);}
		#神聖属性攻撃力
		if($VS_WC18 ne "" && $VS_WC18 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC18 * 0.007);}
		#暗黒属性攻撃力
		if($VS_WC19 ne "" && $VS_WC19 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC19 * 0.007);}

		#火属性ダメージ軽減
		if($VS_WC20 ne "" && $VS_WC20 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC20 * 0.015);}
		#水属性ダメージ軽減
		if($VS_WC21 ne "" && $VS_WC21 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC21 * 0.015);}
		#大地属性ダメージ軽減
		if($VS_WC22 ne "" && $VS_WC22 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC22 * 0.015);}
		#風属性ダメージ軽減
		if($VS_WC23 ne "" && $VS_WC23 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC23 * 0.015);}
		#神聖属性ダメージ軽減
		if($VS_WC24 ne "" && $VS_WC24 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($VS_WC25 ne "" && $VS_WC25 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC25 * 0.015);}
		#無属性ダメージ軽減
		if($VS_WC26 ne "" && $VS_WC26 > 0 && $PL_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WC26 * 0.02);}
	}
	if($VS_flgEnt4 > 0){
		#魔法ブースト
		if($VS_WD08 ne "" && $VS_WD08 > 0 && $VS_sS[11] =~ m/1|2|3|4/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD08 * 0.01);}
		#火属性攻撃力
		if($VS_WD14 ne "" && $VS_WD14 > 0 && $VS_W[7] =~ m/!01/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD14 * 0.007);}
		#水属性攻撃力
		if($VS_WD15 ne "" && $VS_WD15 > 0 && $VS_W[7] =~ m/!03/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD15 * 0.007);}
		#大地属性攻撃力
		if($VS_WD16 ne "" && $VS_WD16 > 0 && $VS_W[7] =~ m/!02/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD16 * 0.007);}
		#風属性攻撃力
		if($VS_WD17 ne "" && $VS_WD17 > 0 && $VS_W[7] =~ m/!00/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD17 * 0.007);}
		#神聖属性攻撃力
		if($VS_WD18 ne "" && $VS_WD18 > 0 && $VS_W[7] =~ m/!04/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD18 * 0.007);}
		#暗黒属性攻撃力
		if($VS_WD19 ne "" && $VS_WD19 > 0 && $VS_W[7] =~ m/!05/){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD19 * 0.007);}

		#火属性ダメージ軽減
		if($VS_WD20 ne "" && $VS_WD20 > 0 && $PL_W[7] =~ m/!01/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD20 * 0.015);}
		#水属性ダメージ軽減
		if($VS_WD21 ne "" && $VS_WD21 > 0 && $PL_W[7] =~ m/!03/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD21 * 0.015);}
		#大地属性ダメージ軽減
		if($VS_WD22 ne "" && $VS_WD22 > 0 && $PL_W[7] =~ m/!02/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD22 * 0.015);}
		#風属性ダメージ軽減
		if($VS_WD23 ne "" && $VS_WD23 > 0 && $PL_W[7] =~ m/!00/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD23 * 0.015);}
		#神聖属性ダメージ軽減
		if($VS_WD24 ne "" && $VS_WD24 > 0 && $PL_W[7] =~ m/!04/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD24 * 0.015);}
		#暗黒属性ダメージ軽減
		if($VS_WD25 ne "" && $VS_WD25 > 0 && $PL_W[7] =~ m/!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD25 * 0.015);}
		#無属性ダメージ軽減
		if($VS_WD26 ne "" && $VS_WD26 > 0 && $PL_W[7] !~ m/!00|!01|!02|!03|!04|!05/){$PL_W[1] = $PL_W[1] - int($PL_W[1] * $VS_WD26 * 0.02);}
	}
	
#戦術適性
	if($PL_WA28 ne "" && $PL_WA28 > 0 && $PL_flgEnt > 0){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WA28 * 0.01);}
	elsif($PL_WB28 ne "" && $PL_WB28 > 0 && $PL_flgEnt2 > 0){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WB28 * 0.01);}
	elsif($PL_WC28 ne "" && $PL_WC28 > 0 && $PL_flgEnt3 > 0){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WC28 * 0.01);}
	elsif($PL_WD28 ne "" && $PL_WD28 > 0 && $PL_flgEnt4 > 0){$PL_W[1] = $PL_W[1] + int($PL_W[1] * $PL_WD28 * 0.01);}

	if($VS_WA28 ne "" && $VS_WA28 > 0 && $VS_flgEnt > 0){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WA28 * 0.01);}
	elsif($VS_WB28 ne "" && $VS_WB28 > 0 && $VS_flgEnt2 > 0){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WB28 * 0.01);}
	elsif($VS_WC28 ne "" && $VS_WC28 > 0 && $VS_flgEnt3 > 0){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WC28 * 0.01);}
	elsif($VS_WD28 ne "" && $VS_WD28 > 0 && $VS_flgEnt4 > 0){$VS_W[1] = $VS_W[1] + int($VS_W[1] * $VS_WD28 * 0.01);}

#新ステータスダウン
#$phyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">貫通攻撃発動</font>";
#$vhyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">貫通攻撃発動</font>";




	#20190326 新ステータスダウン
	if($PL_W[7] =~ m/!22/ && $VS_W[7] !~ m/!4b/ && $VS_sB[7] !~ m/!4b/ && $VS_sC[7] !~ m/!4b/ && $VS_sD[7] !~ m/!4b/){
			$VS_CLASS[1] = $VS_CLASS[1] - 2;
			$phyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">攻↓発動</font>";
#			$PL_CLASS[1] = $PL_CLASS[1] + 3;$PL_CLASS[2] = $PL_CLASS[2] + 3;$PL_CLASS[3] = $PL_CLASS[3] + 3;$PL_CLASS[4] = $PL_CLASS[4] + 3;
#			$VS_CLASS[1] = $VS_CLASS[1] + 3;$VS_CLASS[2] = $VS_CLASS[2] + 3;$VS_CLASS[3] = $VS_CLASS[3] + 3;$VS_CLASS[4] = $VS_CLASS[4] + 3;
	}
	if($PL_W[7] =~ m/!23/ && $VS_W[7] !~ m/!4b/ && $VS_sB[7] !~ m/!4b/ && $VS_sC[7] !~ m/!4b/ && $VS_sD[7] !~ m/!4b/){$VS_CLASS[2] = $VS_CLASS[2] - 4;$phyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">防↓発動</font>";}
	if($PL_W[7] =~ m/!24/ && $VS_W[7] !~ m/!4b/ && $VS_sB[7] !~ m/!4b/ && $VS_sC[7] !~ m/!4b/ && $VS_sD[7] !~ m/!4b/){$VS_CLASS[3] = $VS_CLASS[3] - 3;$phyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">避↓発動</font>";}
	if($PL_W[7] =~ m/!25/ && $VS_W[7] !~ m/!4b/ && $VS_sB[7] !~ m/!4b/ && $VS_sC[7] !~ m/!4b/ && $VS_sD[7] !~ m/!4b/){$VS_CLASS[4] = $VS_CLASS[4] - 3;$phyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">命↓発動</font>";}

	if($VS_W[7] =~ m/!22/ && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/ && $PL_sD[7] !~ m/!4b/){$PL_CLASS[1] = $PL_CLASS[1] - 2;$vhyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">攻↓発動</font>";}
	if($VS_W[7] =~ m/!23/ && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/ && $PL_sD[7] !~ m/!4b/){$PL_CLASS[2] = $PL_CLASS[2] - 4;$vhyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">防↓発動</font>";}
	if($VS_W[7] =~ m/!24/ && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/ && $PL_sD[7] !~ m/!4b/){$PL_CLASS[3] = $PL_CLASS[3] - 3;$vhyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">避↓発動</font>";}
	if($VS_W[7] =~ m/!25/ && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/ && $PL_sD[7] !~ m/!4b/){$PL_CLASS[4] = $PL_CLASS[4] - 3;$vhyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">命↓発動</font>";}

#print "$FORM{'pname'}は、$Ch_rankに";
	&ERROR("ダブルアタックを行うには $STATUS_NAME[5] が足りません。") if $FORM{'mode'} == 8 && $PL_VALUES[17] < $PL_W[4]*2;
	&ERROR('noEnergy','MP が足りません。') if $PL_VALUES[17] < $PL_W[4];
##初期計算
	&SYUSEI('v','PL','Pl');
	&SYUSEI('v','VS','Vs');
}
sub vabattle3{
##相手の作戦
	$VsMsnNo=int(rand(8)+1) if !$FORM{'pmode'};
#$VsMsnNo=8;
##クラス修正
	&SYUSEI('s','PL','Pl');
	&SYUSEI('s','VS','Vs');
##作戦修正
	&SYUSEI('m',"$FORM{'mode'}",'Pl','PL',"$PL_VALUES[4]");
	&SYUSEI('m',"$VsMsnNo",'Vs','VS',"$VS_VALUES[4]");
	
#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0){
		#消費MP軽減
		if($ABI_sA[2] =~ m/!A0038/ || $ABI_sB[2] =~ m/!A0038/ || $ABI_sC[2] =~ m/!A0038/){$PL_W[4]=int($PL_W[4]*0.85);}

		#弓懸
		if($PL_W[12] =~ m/e009/ && $Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0104/ || $ABI_sB[2] =~ m/!A0104/ || $ABI_sC[2] =~ m/!A0104/)){
			$PL_W[3] = int($PL_W[3] * 1.25);
		}
		if($VS_W[12] =~ m/e009/ && $Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0104/ || $VABI_sB[2] =~ m/!A0104/ || $VABI_sC[2] =~ m/!A0104/)){
			$VS_W[3] = int($VS_W[3] * 1.25);
		}

	}
	
##防具計算特殊効果修正
	&SYUSEI('est','PL','Pl','VS');
	&SYUSEI('est','VS','Vs','PL');
}
sub vabattle3_1{
##武器特殊効果修正
	&SYUSEI('aria','PL','Pl','VS','Vs','75','65');
	&SYUSEI('aria','VS','Vs','PL','Pl','85','77');
}
sub vabattle4{
##Initiative
	&SYUSEI('ini','PL','Pl');
	&SYUSEI('ini','VS','Vs');
##命中・画像
	$mei_Pl_Check=sprintf("%.2f",$PL_W[2]+$Pl_MisPoint-$Vs_SpPoint);#命中率
	$mei_Vs_Check=sprintf("%.2f",$VS_W[2]+$Vs_MisPoint-$Pl_SpPoint);#命中率
	$hImg="<img src=\"$IMG_FOLDER1/hit.gif\">";
	$mImg="<img src=\"$IMG_FOLDER1/miss.gif\">";
	$gImg="<img src=\"$IMG_FOLDER1/guard2.gif\" width = \"33\" height = \"10\">";
	$lImg="<img src=\"$IMG_FOLDER1/Lucky.gif\" width = \"33\" height = \"10\">";
#	$gImg="<img src=\"$IMG_FOLDER1/guard.gif\" width = \"33\" height = \"10\">";
#	$hImg="<img src=\"$IMG_FOLDER1/hit.gif\">";
#	$gImg="<img src=\"$IMG_FOLDER1/hit.gif\">";
#	$mImg="<img src=\"$IMG_FOLDER1/miss.gif\">";
}
sub vabattle4_1{
##特殊効果2
	&SYUSEI('hina','PL','Pl','VS','Vs','75','90');
	&SYUSEI('hina','VS','Vs','PL','Pl','90','95');
}
sub vabattle5{

	$Pl_sensei=sprintf("%.2f",$Pl_Initiative/$Vs_Initiative*100-50);
	$Vs_sensei=sprintf("%.2f",$Vs_Initiative/$Pl_Initiative*100-50);

	$Pl_iniCheck=sprintf("%.2f",rand(100));
	$Vs_iniCheck=sprintf("%.2f",rand(100));

	$Pl_Initiative+=sprintf("%.2f",rand(10)) if $Pl_sensei > $Pl_iniCheck;
	$Vs_Initiative+=sprintf("%.2f",rand(10)) if $Vs_sensei > $Vs_iniCheck;

	$Pl_Ini=$Pl_Initiative;
	$Vs_Ini=$Vs_Initiative;

	$test_Pl_AtPoint=int($Pl_AttPoint*$PL_W[3]);#素の攻撃力
	$test_Vs_AtPoint=int($Vs_AttPoint*$VS_W[3]);#素の攻撃力

#	&ERROR("$$SOああ$Pl_DefPointいい");

#貫通攻撃
#	$Pl_AttPoint=$Pl_AttPoint-$Vs_DefPoint*(rand(20)+90)/$PL_W[3];
#	$Vs_AttPoint=$Vs_AttPoint-$Pl_DefPoint*(rand(20)+90)/$VS_W[3];

#	if($Pl_WOnly eq "1" && $PL_WA33 ne "" && $PL_WA33 > 0 && rand(100) <= ($PL_WA33 * 2)){
	if($PL_WA33 ne "" && $PL_WA33 > 0 && rand(100) <= ($PL_WA33 * 2)){
#		print "<font color=\"#00FF00\">$PL_VALUES[3]は貫通攻撃を発動！！</font><br>\n";
		$phyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">貫通攻撃発動</font>";
		$Pl_AttPoint=$Pl_AttPoint;
	}else{
		$Pl_AttPoint=$Pl_AttPoint-$Vs_DefPoint*(rand(20)+90)/$PL_W[3];
	}

#	if($Vs_WOnly eq "1" && $VS_WA33 ne "" && $VS_WA33 > 0 && rand(100) <= ($VS_WA33 * 2)){
	if($VS_WA33 ne "" && $VS_WA33 > 0 && rand(100) <= ($VS_WA33 * 2)){
#		print "<font color=\"#00FF00\">$VS_VALUES[3]は貫通攻撃を発動！！</font><br>\n";
		$vhyou1.="<BR><font color=#00FF00 style=\"font-size:12px;\">貫通攻撃発動</font>";
		$Vs_AttPoint=$Vs_AttPoint;
	}else{
		$Vs_AttPoint=$Vs_AttPoint-$Pl_DefPoint*(rand(20)+90)/$VS_W[3];
	}
#盾のガード発動率を設定
	#$$SGP=$$E3;
	#$PL_ShDPoint

	$PL_KaihiShD = $PL_ShDPoint;
	$VS_KaihiShD = $VS_ShDPoint;
	
#	if($PL_ShDPoint eq "" || $Vs_WOnly ne "1"){$PL_ShDPoint = 0;}#else{$PL_ShDPoint = int($PL_ShDPoint * 1.3);}
#	if($VS_ShDPoint eq "" || $Pl_WOnly ne "1"){$VS_ShDPoint = 0;}#else{$VS_ShDPoint = int($VS_ShDPoint * 1.3);}
##	if($PL_ShDPoint eq ""){$PL_ShDPoint = 0;}else{$PL_ShDPoint = int($PL_ShDPoint * 1.3);}
##	if($VS_ShDPoint eq ""){$VS_ShDPoint = 0;}else{$VS_ShDPoint = int($VS_ShDPoint * 1.3);}
	$Pl_Redac=0;$Vs_Redac=0;

#アビリティシステム
	$PL_GateKeeper=0;
	if($AbiSys == 1 && $AbiMukou == 0){
		if($PL_KaihiShD ne "" || $PL_KaihiShD > 0){
			$PL_ShDPoint = $PL_KaihiShD;

			#盾修練
			if($ABI_sA[2] =~ m/!A0033/ || $ABI_sB[2] =~ m/!A0033/ || $ABI_sC[2] =~ m/!A0033/){$PL_ShDPoint+=10;}
			#ゲートキーパー
			if($PL_VALUES[14] >= 15 && ($ABI_sA[2] =~ m/!A0012/ || $ABI_sB[2] =~ m/!A0012/ || $ABI_sC[2] =~ m/!A0012/)){$PL_ShDPoint = $PL_ShDPoint + int($PL_VALUES[14] / 2) + 20;$PL_GateKeeper=1;}

		}
		if($VS_KaihiShD ne "" || $VS_KaihiShD > 0){

			$VS_ShDPoint = $VS_KaihiShD;
			#盾修練
			if($VABI_sA[2] =~ m/!A0033/ || $VABI_sB[2] =~ m/!A0033/ || $VABI_sC[2] =~ m/!A0033/){$VS_ShDPoint+=10;}

		}

		#ダメージリダクション
		$Pl_Redac=0;$Vs_Redac=0;
		if($ABI_sA[2] =~ m/!A0052/ || $ABI_sB[2] =~ m/!A0052/ || $ABI_sC[2] =~ m/!A0052/){$Vs_AtPoint=-15000;$Pl_Redac=1;}
		if($VABI_sA[2] =~ m/!A0052/ || $VABI_sB[2] =~ m/!A0052/ || $VABI_sC[2] =~ m/!A0052/){$Pl_AtPoint=-15000;$Vs_Redac=1;}
		
	}

#装備品によるダメージリダクション
#	$PL_EQREDPoint = 0;
#	$VS_EQREDPoint = 0;
	
#	if($PL_W[15] > 0 && $PL_W[15] ne ""){$PL_EQREDPoint = $PL_EQREDPoint + $PL_W[15];}
#	if($PL_sB[15] > 0 && $PL_sB[15] ne ""){$PL_EQREDPoint = $PL_EQREDPoint + $PL_sB[15];}
#	if($PL_sC[15] > 0 && $PL_sC[15] ne ""){$PL_EQREDPoint = $PL_EQREDPoint + $PL_sC[15];}
#	if($PL_sD[15] > 0 && $PL_sD[15] ne ""){$PL_EQREDPoint = $PL_EQREDPoint + $PL_sD[15];}

#	if($VS_W[15] > 0 && $VS_W[15] ne ""){$VS_EQREDPoint = $VS_EQREDPoint + $VS_W[15];}
#	if($VS_sB[15] > 0 && $VS_sB[15] ne ""){$VS_EQREDPoint = $VS_EQREDPoint + $VS_sB[15];}
#	if($VS_sC[15] > 0 && $VS_sC[15] ne ""){$VS_EQREDPoint = $VS_EQREDPoint + $VS_sC[15];}
#	if($VS_sD[15] > 0 && $VS_sD[15] ne ""){$VS_EQREDPoint = $VS_EQREDPoint + $VS_sD[15];}

#	if($PL_EQREDPoint > 0){$Vs_AtPoint = $Vs_AtPoint - int($PL_EQREDPoint / $VS_W[3]);$Pl_Redac=1;}
#	if($VS_EQREDPoint > 0){$Pl_AtPoint = $Pl_AtPoint - int($VS_EQREDPoint / $PL_W[3]);$Vs_Redac=1;}





#装備強化システム
	if($PL_REDPoint > 0){$Vs_AtPoint = $Vs_AtPoint - int($PL_REDPoint / $VS_W[3]);$Pl_Redac=1;}
	if($VS_REDPoint > 0){$Pl_AtPoint = $Pl_AtPoint - int($VS_REDPoint / $PL_W[3]);$Vs_Redac=1;}

	if($PL_SHDPointENT > 0){$PL_ShDPoint = $PL_ShDPoint + $PL_SHDPointENT;}
	if($VS_SHDPointENT > 0){$VS_ShDPoint = $VS_ShDPoint + $VS_SHDPointENT;}

	$Vs_AtPoint = int($Vs_AtPoint * $PL_REDPerPoint);
	$Pl_AtPoint = int($Pl_AtPoint * $VS_REDPerPoint);

	#回復行動時はガードしない
	if($FORM{'b_mode'} eq '回復'){$VS_ShDPoint=0;}

#	#特殊・魔法攻撃には適用しない　※ゲートキーパー使用時除く
#	if($Vs_WOnly ne "1" && $PL_GateKeeper ne "1"){$PL_ShDPoint = 0;}#else{$PL_ShDPoint = int($PL_ShDPoint * 1.3);}
#	if($Pl_WOnly ne "1"){$VS_ShDPoint = 0;}#else{$VS_ShDPoint = int($VS_ShDPoint * 1.3);}

#20100516 魔法・特殊はガード除外
	if($PL_KaihiShD ne "" || $PL_KaihiShD > 0){$PL_ShDPoint = $PL_KaihiShD;}
	if($VS_KaihiShD ne "" || $VS_KaihiShD > 0){$VS_ShDPoint = $VS_KaihiShD;}
#	if($FORM{'b_mode'} eq '回復'){$VS_ShDPoint=0;}

#	if($AbiSys == 1 && $AbiMukou == 0){

#		#シールドブレイク
#		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0074/ || $ABI_sB[2] =~ m/!A0074/ || $ABI_sC[2] =~ m/!A0074/)){$VS_ShDPoint=0;}
#		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0074/ || $VABI_sB[2] =~ m/!A0074/ || $VABI_sC[2] =~ m/!A0074/)){$PL_ShDPoint=0;}

#	}

	#回数攻撃による攻撃力補正
	$PL_KaisuHosei = 1;
	$VS_KaisuHosei = 1;

	#マスターバングルによる完全回避
	$PL_PERFREE = 0;
	$VS_PERFREE = 0;

	if($PL_W[7] =~ m/!E0037/){$PL_PERFREE = $PL_PERFREE + 10;}
	if($PL_sB[7] =~ m/!E0037/){$PL_PERFREE = $PL_PERFREE + 10;}
	if($PL_sC[7] =~ m/!E0037/){$PL_PERFREE = $PL_PERFREE + 10;}
	if($PL_sD[7] =~ m/!E0037/){$PL_PERFREE = $PL_PERFREE + 10;}

	if($VS_W[7] =~ m/!E0037/){$VS_PERFREE = $VS_PERFREE + 10;}
	if($VS_sB[7] =~ m/!E0037/){$VS_PERFREE = $VS_PERFREE + 10;}
	if($VS_sC[7] =~ m/!E0037/){$VS_PERFREE = $VS_PERFREE + 10;}
	if($VS_sD[7] =~ m/!E0037/){$VS_PERFREE = $VS_PERFREE + 10;}

	if($FORM{'b_mode'} eq '回復'){$VS_PERFREE=0;}


	#射程武器による完全回避　20190524
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0200/){$PL_PERFREE = $PL_PERFREE + 20;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0201/){$PL_PERFREE = $PL_PERFREE + 24;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0202/){$PL_PERFREE = $PL_PERFREE + 28;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0203/){$PL_PERFREE = $PL_PERFREE + 32;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0204/){$PL_PERFREE = $PL_PERFREE + 36;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0205/){$PL_PERFREE = $PL_PERFREE + 40;}

	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0206/){$PL_PERFREE = $PL_PERFREE + 10;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0207/){$PL_PERFREE = $PL_PERFREE + 12;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0208/){$PL_PERFREE = $PL_PERFREE + 14;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0209/){$PL_PERFREE = $PL_PERFREE + 16;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0210/){$PL_PERFREE = $PL_PERFREE + 18;}
	if($Pl_WOnly eq "1" && $PL_W[7] =~ m/!E0211/){$PL_PERFREE = $PL_PERFREE + 20;}



	#ガード仕様凍結に伴い、0固定とする
#	$PL_ShDPoint=0;
#	$VS_ShDPoint=0;

	if($PL_CLASS[2]>0){$PL_DMGCUT = int($PL_CLASS[2]/2-0.5)/10;}else{$PL_DMGCUT=0.05;};
	if($VS_CLASS[2]>0){$VS_DMGCUT = int($VS_CLASS[2]/2-0.5)/10;}else{$VS_DMGCUT=0.05;};

	#ゲートキーパー
	if($PL_GateKeeper eq "1"){$PL_DMGCUT = $PL_DMGCUT + 0.3;}

	#装備武器ガード
	if($AbiSys == 1){

		if($Pl_WOnly eq "1" && ($ABI_sA[2] =~ m/!A0092/ || $ABI_sB[2] =~ m/!A0092/ || $ABI_sC[2] =~ m/!A0092/)){$PL_DMGCUT=0.2;$PL_ShDPoint = $PL_ShDPoint + 11;}
		if($Vs_WOnly eq "1" && ($VABI_sA[2] =~ m/!A0092/ || $VABI_sB[2] =~ m/!A0092/ || $VABI_sC[2] =~ m/!A0092/)){$VS_DMGCUT=0.2;$VS_ShDPoint = $VS_ShDPoint + 11;}

	}

#	&ERROR("$PL_ShDPointと$VS_ShDPointと$Pl_WOnly");
#$PL_ShDPoint=50;
	$LOP=($VS_W[3]+$PL_W[3])*2;
	$LOP=100 if $LOP > 100;
	for ($Plt=1;$Plt < $LOP; $Plt++ ){
		if($Pl_Initiative >= $Vs_Initiative){
			$Initivs=1;
		}else{
			$Initivs=0;
		}
		if($VS_W >= $VS_W[3] && $PL_W >= $PL_W[3]){
			last;
		}
		if ($Vs_AtPoint < $PL_VALUES[15] && $PL_W < $PL_W[3] && ($Initivs || $VS_W >= $VS_W[3])){
			$Pl_Check=sprintf("%.2f",rand(100));$PL_W++;
			$Pl_Initiative-=1+sprintf("%.2f",rand(1));
	
#			if($COOKIE{'pass'} eq $MASTERPASS){$phyou1.="($Pl_Check%)$Pl_Initiative<font color=#997788 style=\"font-size:12px;\">[$Plt]</font>";}

#			if($Pl_Check < $mei_Pl_Check){
#			if(int($Pl_Check + $VS_ShDPoint) < $mei_Pl_Check){
#			if(($Pl_Check < $mei_Pl_Check) && ($VS_ShDPoint <= int(rand(100)))){
			if($Pl_Check < $mei_Pl_Check){
#				if($VS_ShDPoint <= int(rand(100)) && ($VS_PERFREE <= int(rand(100)) || $YousaiKaihi <= int(rand(100)))){
#					$PlResult.="$hImg$phyou1";$Pl_Times++;
##					$Pl_AtPoint+=$Pl_AttPoint;
#					$Pl_AtPoint = $Pl_AtPoint + int($Pl_AttPoint * $PL_KaisuHosei);
#					$PL_KaisuHosei = $PL_KaisuHosei + 0.01;
#				}else{
##					$PlResult.="$gImg$phyou1";
#					$PlResult.="$gImg$phyou1";#$Pl_Times++;
##					$Pl_AtPoint+=int($Pl_AttPoint*0.5);
#				}

				if($VS_PERFREE > int(rand(100)) || $YousaiKaihi > int(rand(100))){
					$PlResult.="$lImg";
				}elsif($VS_ShDPoint > int(rand(100))){

					$PlResult.="$gImg";$Pl_Times++;
					$Pl_AtPoint+=int($Pl_AttPoint*(1 - $VS_DMGCUT));

				}else{
					$PlResult.="$hImg";$Pl_Times++;
					$Pl_AtPoint = $Pl_AtPoint + int($Pl_AttPoint * $PL_KaisuHosei);
					$PL_KaisuHosei = $PL_KaisuHosei + 0.01;
				}
				
			}else{
				$PlResult.="$mImg";
				$PL_KaisuHosei = 1;
			}
			unless($PL_W % 10){$PlResult.="<br>\n";}
		next;
		}elsif($Vs_AtPoint >= $PL_VALUES[15]){
			$PL_W=$PL_W[3];
		}
		if ($Pl_AtPoint < $VS_VALUES[15] && $VS_W < $VS_W[3] && (!$Initivs || $PL_W >= $PL_W[3])){
			$Vs_Check=sprintf("%.2f",rand(100));$VS_W++;
			$Vs_Initiative-=1+sprintf("%.2f",rand(2));

#			if($COOKIE{'pass'} eq $MASTERPASS){$vhyou1.="($Vs_Check%)$Vs_Initiative<font color=#997788 style=\"font-size:12px;\">[$Plt]</font>";}

#			if($Vs_Check < $mei_Vs_Check){
#			if(int($Vs_Check + $PL_ShDPoint) < $mei_Vs_Check){
#			if(($Vs_Check < $mei_Vs_Check) && ($PL_ShDPoint <= int(rand(100)))){
			if($Vs_Check < $mei_Vs_Check){
#				if($PL_ShDPoint <= int(rand(100)) && ($PL_PERFREE <= int(rand(100)))){
#					$VsResult.="$hImg$vhyou1";$Vs_Times++;
##					$Vs_AtPoint+=int($Vs_AttPoint);
#					$Vs_AtPoint = int($Vs_AtPoint + int($Vs_AttPoint * $VS_KaisuHosei));
#					$VS_KaisuHosei = $VS_KaisuHosei + 0.01;

#				}else{
##					$VsResult.="$gImg$vhyou1";
#					$VsResult.="$gImg$vhyou1";#$Vs_Times++;
##					$Vs_AtPoint+=int($Vs_AttPoint*0.5);
#					$VS_KaisuHosei = 1;
#				}
				
				if($PL_PERFREE > int(rand(100))){
					$VsResult.="$lImg";
				}elsif($PL_ShDPoint > int(rand(100))){

					$VsResult.="$gImg";$Vs_Times++;
					$Vs_AtPoint+=int($Vs_AttPoint*(1 - $PL_DMGCUT));

				}else{
					$VsResult.="$hImg";$Vs_Times++;
					$Vs_AtPoint = $Vs_AtPoint + int($Vs_AttPoint * $VS_KaisuHosei);
					$VS_KaisuHosei = $VS_KaisuHosei + 0.01;
				}

			}else{
				$VsResult.="$mImg";
			}
			unless($VS_W % 10){$VsResult.="<br>\n";}
		next;
		}elsif($Pl_AtPoint >= $VS_VALUES[15]){
			$VS_W=$VS_W[3];
		}
	}
	
#アビリティシステムの影響
	if($Pl_AtPoint < 0 && $Vs_Redac eq "1"){$Pl_AtPoint=0;}
	if($Vs_AtPoint < 0 && $Pl_Redac eq "1"){$Vs_AtPoint=0;}
	
	$Pl_AtPoint=int $Pl_AtPoint;
	$Vs_AtPoint=int $Vs_AtPoint;
}
sub vabattle5_1{
###ここに入れるの特殊
	&URSULA('ariel','PL','Pl','VS','Vs','94','254','220','90');
	&URSULA('ariel','VS','Vs','PL','Pl','97','244','170','95');
}
sub vabattle6_1{
		if($PL_VALUES[29] > 100){$PLLVKYU=100;}else{$PLLVKYU=$PL_VALUES[29];}
		if($VS_VALUES[29] > 100){$VSLVKYU=100;}else{$VSLVKYU=$VS_VALUES[29];}
#		&ERROR("$TES");
	#お金計算基本
		$PL_In[2]=int(rand(250)+1300)+($PL_VALUES[0]*3)+$PL_VALUES[29]+$VS_VALUES[19]+$VS_VALUES[20]+$VS_VALUES[21]+$VS_VALUES[22]+$VS_VALUES[29];

	WORL:{
		$VS_VALUES[15] == 0 && $PL_VALUES[15] > 0 && do{
		$PONGARI=0;$battleflag=0;

		if (($CL_VALUES[7] > time && $VS_VALUES[5] && ($CL_VALUES[6] eq $VS_VALUES[5] || $CL_VALUES[8] eq $VS_VALUES[5] || $CL_VALUES[9] eq $VS_VALUES[5] || $CL_VALUES[10] eq $VS_VALUES[5])) || ($VC_VALUES[7] > time && $PL_VALUES[5] && ($VC_VALUES[6] eq $PL_VALUES[5] || $VC_VALUES[8] eq $PL_VALUES[5] || $VC_VALUES[9] eq $PL_VALUES[5] || $VC_VALUES[10] eq $PL_VALUES[5]))){$battleflag=1;}
		#（自分の国が戦争中＆相手国が目標に含まれている）or（相手国が戦争中＆自国が目標に含まれている

		#世界大戦
		if($WW_FRAG==1){
		}else{

			if(($DATE-$VS_VALUES[26]) < 1200 && $battleflag == 0 && $PL_W[7] !~ m/!6o/){
				$PL_VALUES[33]++;$PONGARI=1;$R_VALUES[3]+=1;
			}

		}

		if($PL_VALUES[33] > 2 && $PONGARI==1){$PL_VALUES[17]=0;}
		if($PL_VALUES[33] > 4){$PL_VALUES[19]--;$PL_VALUES[20]--;$PL_VALUES[21]--;$PL_VALUES[22]--;}
		if($PL_VALUES[33] > 9){$PL_VALUES[18]=0;$PL_VALUES[8]=0;}
		$PL_VALUES[34]++;
		if($PL_VALUES[34] == 50){$PL_VALUES[33]--;$PL_VALUES[34]=0;}
		$PL_VALUES[33]=0 if $PL_VALUES[33] < 0;
#ALI変化処理
		if($PL_W[7] !~ m/!6p/ && $PL_sB[7] !~ m/!6p/ && $PL_sC[7] !~ m/!6p/ && $PL_sD[7] !~ m/!6p/){
		  if($PL_VALUES[29] <= $VS_VALUES[29] && $VS_W[7] !~ m/!6s/){
			$LVALI_FRAG=$VS_VALUES[29]-$PL_VALUES[29];
			if($LVALI_FRAG <= 20){
				$PL_VALUES[12]+=4;
			}elsif($LVALI_FRAG > 20 && $LVALI_FRAG <= 40){
				$PL_VALUES[12]+=6;
			}elsif($LVALI_FRAG > 40 && $LVALI_FRAG <= 60){
				$PL_VALUES[12]+=8;
			}else{
				$PL_VALUES[12]+=10;
			}
		  }elsif($PL_VALUES[29] >= 90 && $VS_VALUES[29] < 30){
			$PL_VALUES[12]-=4;
		  }else{
			$PL_VALUES[12]--;
		  }

		  if($PL_VALUES[12] >= $VS_VALUES[12]){
			$ALI_FRAG=$PL_VALUES[12]-$VS_VALUES[12];
			if($ALI_FRAG > 10 && $ALI_FRAG <= 20){
				$PL_VALUES[12]++;
			}elsif($ALI_FRAG > 20 && $ALI_FRAG <= 30){
				$PL_VALUES[12]+=int(rand(1)+1);
			}else{
				$PL_VALUES[12]+=int(rand(2)+1);
			}
		  }else{
			$ALI_FRAG=$VS_VALUES[12]-$PL_VALUES[12];
			if($ALI_FRAG <= 10){
				$PL_VALUES[12]--;
			}elsif($ALI_FRAG > 10 && $ALI_FRAG <= 20){
				$PL_VALUES[12]-=int(rand(1)+1);
			}else{
				$PL_VALUES[12]-=int(rand(2)+1);
			}
		  }
		}

			$PL_VALUES[12]=100 if $PL_VALUES[12] > 100;
			$PL_VALUES[12]=0 if $PL_VALUES[12] < 0;

			$ResultBattle=0;$R_VALUES[1]+=1;
			$PL_In[0]=int(rand(5)+8);$VS_In[0]=int(rand(2)+4);
#階級
			$PL_In[1]=2+int((101-$PLLVKYU)/10);
			$VS_In[1]=-1-int($VSLVKYU/20);
#お金
			$VS_In[2]=int($PL_In[2]/3);
			$PL_In[2]+=int($VS_VALUES[16]/20);
			$PL_VALUES[24]++ if $VS_VALUES[16] > 70000;
			$PL_VALUES[24]++ if $VS_VALUES[16] > 60000;
			$PL_VALUES[24]++ if $VS_VALUES[16] > 50000;
			$PL_VALUES[24]++ if $VS_VALUES[16] > 40000;
			$PL_VALUES[24]++ if $VS_VALUES[16] > 30000;
			$PL_VALUES[24]++ if $VS_VALUES[16] > 20000;
			$PL_VALUES[24]++ if $VS_VALUES[16] > 10000;
			$PL_VALUES[24]++;

#アビリティシステム
			#取得熟練度アップ
			if($AbiSys == 1 && $AbiMukou == 0){
				if($ABI_sA[2] =~ m/!A0005/ || $ABI_sB[2] =~ m/!A0005/ || $ABI_sC[2] =~ m/!A0005/){$PL_VALUES[24]++;}
			}

			$VS_VALUES[25]=1;
#			($PL_VALUES[0]=0,$PL_VALUES[5]="$FORM{'boumeiC'}",$B_Com='成功',$PL_VALUES[6]=0)if $FORM{'b_mode'} eq '亡命';


			if ($FORM{'b_mode'} eq '亡命'){
				$PL_VALUES[0]=0;
				$PL_VALUES[5]="$FORM{'boumeiC'}";
				$B_Com='成功';
				$PL_VALUES[6]=0;


				if($HoushoFlg == 1){

					@HC=split(/!/,$PL_VALUES[50]);
					if($HC[0] eq ""){$HC[0] = 0;}
					if($HC[1] eq ""){$HC[1] = 0;}
					if($HC[2] eq ""){$HC[2] = 0;}
					
					#現在貢献点をクリア
					$HC[0] = 0;

					$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

				}
				
				#新型褒章システム
#				if($NewHoushoFlg == 1){
#				
#					@HC=split(/!/,$PL_VALUES[50]);
#					if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
#					if($HC[1] eq ""){$HC[1] = 0;}
#					if($HC[2] eq ""){$HC[2] = 0;}
#
#					$HC[1] = 0;
#					
#					$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
#				
#				}

			}

#			if ($FORM{'b_mode'} eq '亡命'){
#
#				$PL_VALUES[0]=0;$PL_VALUES[5]="$FORM{'boumeiC'}";$B_Com='成功';$PL_VALUES[6]=0;
#
##				&DBM_INPORT(C);
#				while (($NC_Name,$NC_Value) =each %C) {
#
#					if($NC_Name eq $PL_VALUES[5]){
#
#						@NC_VALUES = split(/\s/,$NC_Value);
#						$PL_VALUES[39] = $NC_VALUES[39];
#					}
#
#				}
#
#			}


			($PL_VALUES[6]="$VS_VALUES[6]",$PL_VALUES[28]="$VS_VALUES[28]",$VS_VALUES[6]=0,$VS_VALUES[28]='',$B_Com='成功') if $FORM{'b_mode'} eq '内乱';
		last WORL;};
		$PL_VALUES[15] == 0 && $VS_VALUES[15] > 0 && do {
#		&ERROR("$TESだよん");
#武器名格納してるよ

#イベント用アビリティ
	$tensei = 1;
	#転生成功率アップ
	if($AbiSys == 1 && $AbiMukou == 0 && ($ABI_sA[2] =~ m/!A0001/ || $ABI_sB[2] =~ m/!A0001/ || $ABI_sC[2] =~ m/!A0001/)){$tensei = 4;}
	#輪廻転生
	if($AbiSys == 1 && $AbiMukou == 0 && ($ABI_sA[2] =~ m/!A0082/ || $ABI_sB[2] =~ m/!A0082/ || $ABI_sC[2] =~ m/!A0082/)){$tensei = 26;}


	#アンサタクロス
#	if($PL_W[7] =~ m/!8x/ || $PL_sB[7] =~ m/!8x/ || $PL_sC[7] =~ m/!8x/ || $PL_sD[7] =~ m/!8x/){$tensei = $tensei * 100;}
	if($PL_W[7] =~ m/!8x/ || $PL_sB[7] =~ m/!8x/ || $PL_sC[7] =~ m/!8x/ || $PL_sD[7] =~ m/!8x/){$tensei = $tensei * 10;}


	#転生処理
#			if(rand(255) > 253){
			if(rand(255) > (254 - $tensei)){
				$PL_VALUES[4]=59 if $PL_VALUES[4] =~ /^0$|^1$|^4$|^5$|^6$|^9$/i && $PL_VALUES[12]==0 && $PL_VALUES[24]>=400;
				if($PL_VALUES[4] =~ /^1$|^8$|^9$|^10$|^11$|^16$|^17$|^18$|^38$|^39$|^40$|^43$|^44$|^47$|^48$|^49$|^61$|^79$|^80$|^121$|^122$|^123$|^124$|^125$|^132$|^134$|^135$|^154$|^155$|^156$|^170$|^171$|^172$|^174$|^178$|^179$|^184$|^185$/i){
#					if($PL_W[0] eq 'ライトニ\ー\ド\ル' && $PL_VALUES[16]>=20000 && $PL_VALUES[18]>=1500 && $PL_VALUES[19]>=40 && $PL_VALUES[22]>=40 && $PL_VALUES[12]>=96){$PL_VALUES[4]=113;}
					if($TES eq 'ライトニ\ー\ド\ル' && $PL_VALUES[16]>=20000 && $PL_VALUES[18]>=1500 && $PL_VALUES[19]>=40 && $PL_VALUES[22]>=40 && $PL_VALUES[12]>=96){$PL_VALUES[4]=113;}
					elsif($TES eq 'ライトニードル' && $PL_VALUES[16]>=20000 && $PL_VALUES[18]>=1500 && $PL_VALUES[19]>=40 && $PL_VALUES[22]>=40 && $PL_VALUES[12]>=96){$PL_VALUES[4]=113;}
#					elsif($PL_W[0] eq '大天使の羽根' && $PL_VALUES[16]>=25000 && $PL_VALUES[18]>=1700 && $PL_VALUES[21]>=40 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=96){$PL_VALUES[4]=116;$PL_VALUES[31]=4;}
					elsif($TES eq '大天使の羽根' && $PL_VALUES[16]>=25000 && $PL_VALUES[18]>=1700 && $PL_VALUES[21]>=40 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=96){$PL_VALUES[4]=116;$PL_VALUES[31]=4;}
					elsif($PL_VALUES[16]>=40000 && $PL_VALUES[18]>=2800 && $PL_VALUES[19]>=50 && $PL_VALUES[12]>=96){$PL_VALUES[4]=23;}
				}
#				if($PL_VALUES[4] =~ /^0$|^2$|^3$|^4$|^5$|^12$|^13$|^14$|^165$|^166$|^168$/i && $PL_W[0] eq '大天使の羽根' && $PL_VALUES[16]>=25000 && $PL_VALUES[18]>=1700 && $PL_VALUES[21]>=40 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=96){$PL_VALUES[4]=115;$PL_VALUES[31]=4;}
				if($PL_VALUES[4] =~ /^0$|^2$|^3$|^4$|^5$|^12$|^13$|^14$|^165$|^166$|^168$/i && $TES eq '大天使の羽根' && $PL_VALUES[16]>=25000 && $PL_VALUES[18]>=1700 && $PL_VALUES[21]>=40 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=96){$PL_VALUES[4]=115;$PL_VALUES[31]=4;}
				if($PL_VALUES[4] =~ /^2$|^60$|^184$/i && $PL_VALUES[16]>=20000 && $PL_VALUES[21]==50 && $PL_VALUES[22]>=45 && $PL_VALUES[24]>=1100 && $PL_VALUES[12]<12){$PL_VALUES[4]=56;$PL_VALUES[31]=5;}

				if($PL_VALUES[4]==14){
#					if($PL_W[0] eq 'ブリューナク' && $PL_VALUES[16]>=60000 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=45 && $PL_VALUES[12]<=12){$PL_VALUES[4]=160;$PL_VALUES[31]=5;}
#					elsif($PL_W[0] eq 'ゼピュロス' && $PL_VALUES[16]>=60000 && $PL_VALUES[18]>=2500 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=50 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=48 && $PL_VALUES[12]<60){$PL_VALUES[4]=141;}
#					elsif($PL_W[0] eq 'ザンジバル' && $PL_VALUES[16]>=60000 && $PL_VALUES[18]>=2500 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=50 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=72 && $PL_VALUES[12]<84){$PL_VALUES[4]=195;}
#					elsif($PL_W[0] eq 'ブリュンヒルド' && $PL_VALUES[16]>=60000 && $PL_VALUES[18]>=2500 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=50 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=72 && $PL_VALUES[12]<84){$PL_VALUES[4]=196;}
#					elsif($PL_W[0] eq 'カラドボルグ' && $PL_VALUES[16]>=40000 && $PL_VALUES[24]>=1000 && $PL_VALUES[19]>=50 && $PL_VALUES[12]>=36 && $PL_VALUES[12]<72){$PL_VALUES[4]=143;$PL_VALUES[31]=2;}
					if($TES eq 'ブリューナク' && $PL_VALUES[16]>=60000 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=45 && $PL_VALUES[12]<=12){$PL_VALUES[4]=160;$PL_VALUES[31]=5;}
					elsif($TES eq 'ゼピュロス' && $PL_VALUES[16]>=60000 && $PL_VALUES[18]>=2500 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=50 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=48 && $PL_VALUES[12]<60){$PL_VALUES[4]=141;}
					elsif($TES eq 'ザンジバル' && $PL_VALUES[16]>=60000 && $PL_VALUES[18]>=2500 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=50 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=72 && $PL_VALUES[12]<84){$PL_VALUES[4]=195;}
					elsif($TES eq 'ブリュンヒルド' && $PL_VALUES[16]>=60000 && $PL_VALUES[18]>=2500 && $PL_VALUES[24]>=1200 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=50 && $PL_VALUES[22]>=45 && $PL_VALUES[12]>=72 && $PL_VALUES[12]<84){$PL_VALUES[4]=196;}
					elsif($TES eq 'カラドボルグ' && $PL_VALUES[16]>=40000 && $PL_VALUES[24]>=1000 && $PL_VALUES[19]>=50 && $PL_VALUES[12]>=36 && $PL_VALUES[12]<72){$PL_VALUES[4]=143;$PL_VALUES[31]=2;}
				}

				if($PL_VALUES[4]==217){
#					if(($TES eq 'リムファイアー' || $TES eq 'カマンダスガン' || $TES eq 'アッサルト') && $PL_VALUES[24]>=1200 && $PL_VALUES[12]<=100){$PL_VALUES[4]=219;}
					if($TES12 =~ m/e011/ && $PL_VALUES[24]>=1200 && $PL_VALUES[12]<=100){$PL_VALUES[4]=219;}
				}
				if($PL_VALUES[4]==36){
					if($PL_VALUES[24]>=1000 && $PL_VALUES[12]<=35){$PL_VALUES[4]=220;}
				}

#option value=\"$c\"";
				if($PL_VALUES[4]==192 && $PL_VALUES[16]>=60000 && $PL_VALUES[24]>=1500 && $PL_VALUES[19]>=50 && $PL_VALUES[12]<12){$PL_VALUES[4]=193;$PL_VALUES[31]=5;}
#				$PL_VALUES[4]=129 if ($PL_W[0] eq 'カラドボルグ' && $PL_VALUES[4]==127 && $PL_VALUES[16]>=60000 && $PL_VALUES[24]>=1100 && $PL_VALUES[19]>=45 && $PL_VALUES[22]>=40 && $PL_VALUES[12]<=11);
#				$PL_VALUES[4]=130 if ($PL_W[0] eq 'アースジャベリン' && $PL_VALUES[4]==128 && $PL_VALUES[16]>=55000 && $PL_VALUES[24]>=1100 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=40 && $PL_VALUES[22]>=45 && $PL_VALUES[12]<=11);
#				$PL_VALUES[4]=207 if ($PL_W[0] eq 'ベンティスカ' && $PL_VALUES[4]==206 && $PL_VALUES[16]>=55000 && $PL_VALUES[24]>=1100 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=45 && $PL_VALUES[22]>=40 && $PL_VALUES[12]<=11);
				$PL_VALUES[4]=129 if ($TES eq 'イセベルグ' && $PL_VALUES[4]==127 && $PL_VALUES[16]>=60000 && $PL_VALUES[24]>=1100 && $PL_VALUES[19]>=45 && $PL_VALUES[22]>=40 && $PL_VALUES[12]<=11);
				$PL_VALUES[4]=130 if ($TES eq 'アースジャベリン' && $PL_VALUES[4]==128 && $PL_VALUES[16]>=55000 && $PL_VALUES[24]>=1100 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=40 && $PL_VALUES[22]>=45 && $PL_VALUES[12]<=11);
				$PL_VALUES[4]=207 if ($TES eq 'ベンティスカ' && $PL_VALUES[4]==206 && $PL_VALUES[16]>=55000 && $PL_VALUES[24]>=1100 && $PL_VALUES[19]>=50 && $PL_VALUES[20]>=45 && $PL_VALUES[22]>=40 && $PL_VALUES[12]<=11);
				$PL_VALUES[4]=71 if ($PL_VALUES[4]==93 && $PL_VALUES[12]==48 && $PL_VALUES[24]>=1200);
				$PL_VALUES[4]=71 if ($PL_VALUES[4]==93 && $VS_VALUES[4]==71 && $PL_VALUES[12]==48 && $PL_VALUES[24]>=200);
			}

			$ResultBattle=1;$R_VALUES[2]+=1;
			$PL_In[0]=int (rand(2)+4);$VS_In[0]=int(rand(5)+8);
			$PL_In[1]=-1-int($PLLVKYU/20);$VS_In[1]=2+int((101-$VSLVKYU)/10);
			$VS_In[2]=int($PL_In[2]/2);
			$PL_In[2]=int($PL_In[2]/3);
			$VS_VALUES[24]++;$PL_VALUES[25]=1;
			($PL_In[1]=int($PL_VALUES[0]/-3)*2,$PL_In[0]=$PL_In[2]='0',$B_Com='失敗') if $FORM{'b_mode'} eq '亡命';
			$B_Com='失敗' if $FORM{'b_mode'} eq '内乱';
		last WORL;};
		$VS_VALUES[15] > 0 && $PL_VALUES[15] > 0 && do{
			$ResultBattle=2;
			$PL_In[0]=int(rand(3)+4);$VS_In[0]=int(rand(3)+4);
			$PL_In[1]=int(rand(1));$VS_In[1]=1-int(($VSLVKYU-$PLLVKYU)/20);
			$PL_In[2]=int($PL_In[2]/4);
			$VS_In[2]=int($PL_In[2]/2);
			($PL_In[1]=int($PL_VALUES[0]/-3)*2,$PL_In[0]=$PL_In[2]='0',$B_Com='失敗') if $FORM{'b_mode'} eq '亡命';
			$B_Com='失敗' if $FORM{'b_mode'} eq '内乱';
		last WORL;};
	}
}
sub vabattle6_2{
#レベルによる補助、お金減算
	$PL_In[2]=int($PL_In[2]*1.5) if $PL_VALUES[29] < 100;
	$VS_In[2]=int($VS_In[2]*1.5) if $VS_VALUES[29] < 100;
#ダウジングロッド
#	if ($PL_W[7] =~ m/!18/ && ($PL_sB[7] =~ m/!6n/ || $PL_sC[7] =~ m/!6n/ || $PL_sD[7] =~ m/!6n/) && $PL_CLASS[17] =~ m/!1/){
#	if ($PL_W[7] =~ m/!18/ && ($PL_sB[7] =~ m/!6n/ || $PL_sC[7] =~ m/!6n/ || $PL_sD[7] =~ m/!6n/)){
	if ($PL_W[7] =~ m/!18/ && ($PL_W[7] =~ m/!6n/ || $PL_sB[7] =~ m/!6n/ || $PL_sC[7] =~ m/!6n/ || $PL_sD[7] =~ m/!6n/) && $PL_CLASS[17] =~ m/!1|!E007|!E008/){
#	if ($PL_W[7] =~ m/!6n/ || $PL_sB[7] =~ m/!6n/ || $PL_sC[7] =~ m/!6n/ || $PL_sD[7] =~ m/!6n/){
		$PL_In[2]=int($PL_In[2]*2);
	}


#獲得Goth5倍　＠テスト鯖用
#	$PL_In[2]=int($PL_In[2]*5);
	#エンチャント　獲得Gothアップ
#	$PL_GothUP = 1;
#	$VS_GothUP = 1;
	
#	$PL_GothUP = $PL_WA27 + $PL_WB27 + $PL_WC27 + $PL_WD27;
#	$VS_GothUP = $VS_WA27 + $VS_WB27 + $VS_WC27 + $VS_WD27;

#	if($PL_WA27 ne "" && $PL_WA27 > 0 && $PL_flgEnt > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WA27*0.05);}
#	if($PL_WA27 ne "" && $PL_WA27 > 0 && $PL_flgEnt > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WA27*0.05);}
#	if($PL_WB27 ne "" && $PL_WB27 > 0 && $PL_flgEnt2 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WB27*0.05);}
#	if($PL_WC27 ne "" && $PL_WC27 > 0 && $PL_flgEnt3 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WC27*0.05);}
#	if($PL_WD27 ne "" && $PL_WD27 > 0 && $PL_flgEnt4 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WD27*0.05);}
#	if($VS_WA27 ne "" && $VS_WA27 > 0 && $VS_flgEnt > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WA27*0.05);}
#	if($VS_WB27 ne "" && $VS_WB27 > 0 && $VS_flgEnt2 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WB27*0.05);}
#	if($VS_WC27 ne "" && $VS_WC27 > 0 && $VS_flgEnt3 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WC27*0.05);}
#	if($VS_WD27 ne "" && $VS_WD27 > 0 && $VS_flgEnt4 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WD27*0.05);}


	if($PL_WA27 ne "" && $PL_WA27 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WA27*0.05);}
	if($PL_WB27 ne "" && $PL_WB27 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WB27*0.05);}
	if($PL_WC27 ne "" && $PL_WC27 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WC27*0.05);}
	if($PL_WD27 ne "" && $PL_WD27 > 0){$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_WD27*0.05);}
	if($VS_WA27 ne "" && $VS_WA27 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WA27*0.05);}
	if($VS_WB27 ne "" && $VS_WB27 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WB27*0.05);}
	if($VS_WC27 ne "" && $VS_WC27 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WC27*0.05);}
	if($VS_WD27 ne "" && $VS_WD27 > 0){$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_WD27*0.05);}


#20181206 獲得Goth1.5倍
#$PL_In[0]=int($PL_In[0]*1.5);
#$VS_In[0]=int($VS_In[0]*1.5);

	$PL_In[2]=$PL_In[2] + int($PL_In[2]*$PL_GothEntPoint*0.05);
	$VS_In[2]=$VS_In[2] + int($VS_In[2]*$VS_GothEntPoint*0.05);


#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0){
		#獲得GOTHアップ
		if($ABI_sA[2] =~ m/!A0003/ || $ABI_sB[2] =~ m/!A0003/ || $ABI_sC[2] =~ m/!A0003/){$PL_In[0]=int($PL_In[0]*1.3);}
		if($VABI_sA[2] =~ m/!A0003/ || $VABI_sB[2] =~ m/!A0003/ || $VABI_sC[2] =~ m/!A0003/){$VS_In[0]=int($VS_In[0]*1.3);}
	}
	
	if($PL_W[7] =~ m/!6s/ || $VS_W[7] =~ m/!6s/){
		$PL_In[2]=int($PL_In[2]/3);
		$VS_In[2]=int($VS_In[2]/3);
	}
	if($FORM{'mode'} > 6){
		$FORM{'mode'}=6;
	}
	if($PL_sB[7]=~ m/!16/ || $PL_sC[7]=~ m/!16/ || $PL_sD[7]=~ m/!16/){
		$FORM{'mode'}=1;
	}

#アビリティシステム　AP獲得　APアップ
	$PL_ABHyouji = "";
	$VS_ABHyouji = "";
	if($AbiSys == 1){
	
		$PL_APBouns=0;
		$VS_APBouns=0;
		#取得APアップ
		if(($ABI_sA[2] =~ m/!A0004/ || $ABI_sB[2] =~ m/!A0004/ || $ABI_sC[2] =~ m/!A0004/) && ($AbiMukou == 0)){$PL_APBouns = 2;}
		if(($VABI_sA[2] =~ m/!A0004/ || $VABI_sB[2] =~ m/!A0004/ || $VABI_sC[2] =~ m/!A0004/) && ($AbiMukou == 0)){$VS_APBouns = 2;}

		#戦闘勝利時
		if($PL_VALUES[53] eq ""){$PL_VALUES[53] = 0;}
		if($VS_VALUES[53] eq ""){$VS_VALUES[53] = 0;}
		if($ResultBattle==0){
			$PL_VALUES[53] = $PL_VALUES[53] + 4 + $PL_APBouns;
			$VS_VALUES[53] = $VS_VALUES[53] + 4 + $VS_APBouns;
		#戦闘敗北時
		}elsif($ResultBattle==1){
			$PL_VALUES[53] = $PL_VALUES[53] + 2;
			$VS_VALUES[53] = $VS_VALUES[53] + 2;
		#引分け時
		}else{
			$PL_VALUES[53] = $PL_VALUES[53] + 1;
			$VS_VALUES[53] = $VS_VALUES[53] + 1;		
		}
		
		#APの限界値は9999とする
		if($PL_VALUES[53] > 9999){$PL_VALUES[53]=9999;}
		if($VS_VALUES[53] > 9999){$VS_VALUES[53]=9999;}

		#MP表示の直下にセットしているアビリティを表示する
		$PL_ABHyouji = "<br><font color=#73652b>";
		$VS_ABHyouji = "<br><font color=#73652b>";
		if($ABI_sA[0] ne ""){$PL_ABHyouji.="$ABI_sA[0]<br>";}
		if($ABI_sB[0] ne ""){$PL_ABHyouji.="$ABI_sB[0]<br>";}
		if($ABI_sC[0] ne ""){$PL_ABHyouji.="$ABI_sC[0]";}
		if($VABI_sA[0] ne ""){$VS_ABHyouji.="$VABI_sA[0]<br>";}
		if($VABI_sB[0] ne ""){$VS_ABHyouji.="$VABI_sB[0]<br>";}
		if($VABI_sC[0] ne ""){$VS_ABHyouji.="$VABI_sC[0]";}
		$PL_ABHyouji.="</font>";
		$VS_ABHyouji.="</font>";
		
	}

	$PL_In[2]=10 if $PL_In[2]<10;
	$VS_In[2]=10 if $VS_In[2]<10;
	$PL_VALUES[0]+=$PL_In[1];
	$VS_VALUES[0]+=$VS_In[1];
	$PL_VALUES[8]+=$PL_In[2];
	$VS_VALUES[8]+=$VS_In[2];

	$KakutokuGoth = $PL_In[2];
	if(!$PL_VALUES[5]){$PL_VALUES[0]=0;}
	if(!$VS_VALUES[5]){$VS_VALUES[0]=0;}

	$PL_VALUES[14]+=int($FORM{'mode'}/1.4+4);
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
	($ResultTag.="$VS_VALUES[3]撃破。<br>",$PL_VALUES[1].="$VS_VALUES[3]撃破。",$VS_VALUES[1].="$VS_VALUES[3]戦闘不\能\。")	if $ResultBattle==0;
	($ResultTag.="$PL_VALUES[3]戦闘不\能\。<br>",$PL_VALUES[1].="$PL_VALUES[3]戦闘不\能\。",$VS_VALUES[1].="$PL_VALUES[3]撃破。")	if $ResultBattle==1;
	($PL_VALUES[1].='[ON狩り]',$VS_VALUES[1].='[被ON狩り]')if $PONGARI==1;
	&HEADER;

	if($world){$VSIMAGE="<img src=\"$IMG_FOLDER2/10000.gif\"> ";}
	if($PL_VALUES[27]>=700){$PSIZE=72;}else{$PSIZE=64;}
	if($VS_VALUES[27]>=700){$VSIZE=72;}else{$VSIZE=64;}
	$PIMAGE="$IMG_FOLDER2/$PL_VALUES[27].gif";
	$VIMAGE="$IMG_FOLDER2/$VS_VALUES[27].gif";
	if($PL_VALUES[36]==1){$PIMAGE="$IMG_FOLDER5/$PL_CLASS[18]";$PSIZE=64;}
	if($VS_VALUES[36]==1){$VIMAGE="$IMG_FOLDER5/$VS_CLASS[18]";$VSIZE=64;}
	$PLIMAGE="<img src=\"$PIMAGE\" width=\"$PSIZE\" height=\"$PSIZE\">";
	$VSIMAGE.="<img src=\"$VIMAGE\" style=\"filter:fliph();\" width=\"$VSIZE\" height=\"$VSIZE\">";

	if($Vs_HyoHP eq ""){
		$Vs_HyoHP = $Vs_BfrHP;
	}
#メンテ時は詳細表示
	if($COOKIE{'pass'} eq $MASTERPASS){
#		$phyouji="<br><font color=#73652b>ATK=$test_Pl_AtPoint(STR1+$PL_agD STR2+$PL_agD2) DEF=$Pl_DefPoint(RES1+$PLCSS RES2+$PLBSS) AGI=$Pl_SpPoint(AGI1+$PLFP AGI2+$PLGP) DEX=$mei_Pl_Check(DEX1+$PL_mei DEX2+$PL_mei2) Ini=$Pl_Ini($Pl_sensei% > $Pl_iniCheck%) +$PL_In[2]goth</font>";
##		$phyouji="<br><font color=#73652b>ATK=$test_Pl_AtPoint(STR1+$PL_agD STR2+$PL_agD2 STR3+$PL_agDD3) DEF=$Pl_DefPoint(RES1+$PLCSS RES2+$PLBSS RES3+$PLDDSS) AGI=$Pl_SpPoint(AGI1+$PLFP AGI2+$PLGP AGI3+$PLDDP) DEX=$test_Pl_Check(DEX1+$PL_mei DEX2+$PL_mei2 DEX3+$PL_mei3) Ini=$Pl_Ini</font>";
#		$vhyouji="<br><font color=#73652b>ATK=$test_Vs_AtPoint(STR1+$VS_agD STR2+$VS_agD2) DEF=$Vs_DefPoint(RES1+$VSCSS RES2+$VSBSS) AGI=$Vs_SpPoint(AGI1+$VSFP AGI2+$VSGP) DEX=$mei_Vs_Check(DEX1+$VS_mei DEX2+$VS_mei2) Ini=$Vs_Ini($Vs_sensei% > $Vs_iniCheck%) +$VS_In[2]goth</font>";
##		$vhyouji="<br><font color=#73652b>ATK=$test_Vs_AtPoint(STR1+$VS_agD STR2+$VS_agD2 STR3+$VS_agDD3) DEF=$Vs_DefPoint(RES1+$VSCSS RES2+$VSBSS RES3+$VSDDSS) AGI=$Vs_SpPoint(AGI1+$VSFP AGI2+$VSGP AGI3+$VSDDP) DEX=$test_Vs_Check(DEX1+$VS_mei DEX2+$VS_mei2 DEX3+$VS_mei3) Ini=$Vs_Ini</font>";

	}
#		&ERROR("$VS_VALUES[4]ああ$VS_CLASS[0]");

	print << "	-----END-----";
	<!--美乳-->
	<div align=center>

	<table border=0 bgcolor=#231f1f width=100% cellspacing=0 cellpadding=0 style="padding:2px;">
	<tr><td align=center width=50% bgcolor="$CL_VALUES[0]" style="color:#000000;font-size:25pt;">
		<b>$PL_Country</b></td>
		<td align=center width=50% bgcolor="$VC_VALUES[0]" style="color:#000000;font-size:25pt;">
		<b>$VS_Country</b></td></tr>
	<tr><td align=center width=50%><font color=$PL_VALUES[13] style="font-size:18pt;">$PL_VALUES[3]</font><br>
		<div style="font-size:15px;">（$FORM{'pname'}$Pl_Kaikyu）</div></td>
		<td align=center width=50%><font color=$VS_VALUES[13] style="font-size:18pt;">$VS_VALUES[3]</font><br>
		<div style="font-size:15px;">（$FORM{'vsname'}$Vs_Kaikyu）</div></td></tr>
	<tr><td align=center width=50% height=100 valign=bottom>
		<div align=center>$PLIMAGE</div>
		<font color=#997788 style="font-size:12px;">$PL_CLASS[0]</font>
		<div style="font-size:15px;">【$Pl_MsnStyle】</div>
		<table $TBL_TAG1><tr><td style="font-size:15px;"><b>HP</b>&nbsp;</td>
			<td>$PL_HPTAG</td><td width=50 align=right style="font-size:14px;"><span id=cplhp>$Pl_BfrHP</span></td>
			<td style="font-size:14px;">/<b>$PL_VALUES[16]</b></td></tr></table></td>
	<td align=center width=50% height=100 valign=bottom>
		<div align=center>$VSIMAGE</div>
		<font color=#997788 style="font-size:12px;">$VS_CLASS[0]</font>
		<div style="font-size:15px;">【$Vs_MsnStyle】</div>
		<table $TBL_TAG1><tr><td style="font-size:15px;"><b>HP</b>&nbsp;</td>
			<td>$VS_HPTAG</td><td width=50 align=right style="font-size:14px;"><span id=cvshp>$Vs_HyoHP</span></td>
			<td style="font-size:14px;">/<b>$VS_VALUES[16]</b></td></tr></table></td></tr>
	<tr><td align=center valign=top width=40%><font color=#778899 style="font-size:16px;"><b>$PL_WeaponNameA</b>
			<font style="font-size:12px;"><b>$PL_ShieldNameA</b></font></font><div align=center>$PlResult<div align=center>$PlsumDmg<br>
			<b $chaStyl>$STATUS_NAME[5]:-$PL_W[4]$phyou1$PL_ABHyouji$phyouji</b></div></td>
			<td align=center valign=top width=40%><font color=#778899 style="font-size:16px;"><b>$VS_WeaponNameA</b>
			<font style="font-size:12px;"><b>$VS_ShieldNameA</b></font></font><div align=center>$VsResult<div align=center>$VssumDmg<br>
			<b $chaStyl>$STATUS_NAME[5]:-$VS_W[4]$vhyou1$VS_ABHyouji$vhyouji</b></div></td></tr></table>
	<div style="line-height:4pt;">&nbsp;</div>
		<table><tr><td bgcolor=#231f1f style="line-height:18px;font-size:14px;padding:5px;">
	-----END-----
		if ($PONGARI){
		print "<table><tr><td><font color=\"#ff0080\"><b>从‘　。‘从☆ <font size=150%>ON狩り</font> （‘◇‘☆彡</b><br>！！カウント$PL_VALUES[33]！！</font></td></tr></table><br>\n";
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
		print $PL_In[1] > 0 ? '昇格<br>':$PL_In[1] < 0 ? '降格<br>':'<br>';
	}
	$Ch_rank=&RANK($VS_VALUES[0],$VS_VALUES[5],$VS_VALUES[6]);
	if($Ch_rank ne $Vs_Kaikyu && $Ch_rank){
		print "$FORM{'vsname'}は、$Ch_rankに";
		print $VS_In[1] > 0 ? '昇格<br>':$VS_In[1] < 0 ? '降格<br>':'<br>';
	}
#			<td>$VS_HPTAG</td><td width=50 align=right style="font-size:14px;"><span id=cvshp>$Vs_BfrHP</span></td>
##武芸指南書"
	if (($PL_W[7] =~ m/!6r/ || $PL_sB[7] =~ m/!6r/ || $PL_sC[7] =~ m/!6r/ || $PL_sD[7] =~ m/!6r/) && $PL_W[7] !~ m/!zd/){
		$PL_In[0]*=2;
	}
	if($PL_W[7] =~ m/!64/){$PL_In[0]=$PL_In[0]*3;}
	if($VS_W[7] =~ m/!zd/){$VS_In[0]=0;}
	if($PL_VALUES[5] ne ""){
		$PL_In[4]=$PL_In[0]*($VS_VALUES[0]+1)+($PL_VALUES[0]*2+1);
	}else{
		$PL_In[4]=$PL_In[0]*($VS_VALUES[0]+1);
	}

#EXPに補正 Lvボーナス
	$PL_In[4] = $PL_In[4] + int($PL_VALUES[29] * 0.2) + int($VS_VALUES[29] * 0.2) + int(rand(250));
	
#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0){
		#獲得EXPアップ
		if($ABI_sA[2] =~ m/!A0002/ || $ABI_sB[2] =~ m/!A0002/ || $ABI_sC[2] =~ m/!A0002/){$PL_In[4]=int($PL_In[4]*1.3);}

		#武器指南
		if($ABI_sA[2] =~ m/!A0019/ || $ABI_sB[2] =~ m/!A0019/ || $ABI_sC[2] =~ m/!A0019/){$PL_In[0]=int($PL_In[0]*1.5);}
		if($VABI_sA[2] =~ m/!A0019/ || $VABI_sB[2] =~ m/!A0019/ || $VABI_sC[2] =~ m/!A0019/){$VS_In[0]=int($PL_In[0]*1.5);}
		
	}
	
	#テスト用
#	$PL_In[4]=$PL_In[4]*5;

##イベント　20180821 20181206
#	$PL_In[4] = int($PL_In[4] * 1.5);


	$PL_VALUES[30]+=$PL_In[4];
	print "$FORM{'pname'} は $PL_In[4] の経験値 と $KakutokuGoth Goth を獲得<br>";
#"
	$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
	$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;

	if (($PL_VALUES[29]+1)*200 <= $PL_VALUES[30]){&BATTLE_3;}
#	&BATTLE_3;
#20190322 ステータスダウンは凍結
#	if (($ResultBattle==1 && $PL_CLASS[17] !~ m/E009/ && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/ && $PL_sD[7] !~ m/!4b/) || ($PL_W[7] =~ m/!zd/ || $PL_sB[7] =~ m/!zd/ || $PL_sC[7] =~ m/!zd/ || $PL_sD[7] =~ m/!zd/)){
#		sub DOWN{"<font color=#dc143c>$_[0]がわずかにダウン。</font><br>";}
#		$Event=int(rand(70));
#		if ($Event == 12 && $PL_VALUES[19] >= 1){print &DOWN("$STATUS_NAME[0]");$PL_VALUES[19]--;$PL_STR--;}
#		if ($Event == 13 && $PL_VALUES[20] >= 1){print &DOWN("$STATUS_NAME[1]");$PL_VALUES[20]--;$PL_VIT--;}
#		if ($Event == 14 && $PL_VALUES[21] >= 1){print &DOWN("$STATUS_NAME[2]");$PL_VALUES[21]--;$PL_AGI--;}
#		if ($Event == 15 && $PL_VALUES[22] >= 1){print &DOWN("$STATUS_NAME[3]");$PL_VALUES[22]--;$PL_DEX--;}
##		if ($Event == 12 && $PL_VALUES[19] >= 1){print &DOWN("腕力");$PL_VALUES[19]--;$PL_STR--;}
##		if ($Event == 13 && $PL_VALUES[20] >= 1){print &DOWN("体力");$PL_VALUES[20]--;$PL_VIT--;}
##		if ($Event == 14 && $PL_VALUES[21] >= 1){print &DOWN("素早さ");$PL_VALUES[21]--;$PL_AGI--;}
##		if ($Event == 15 && $PL_VALUES[22] >= 1){print &DOWN("器用さ");$PL_VALUES[22]--;$PL_DEX--;}
#		if ($Event == 16 && $PL_VALUES[16] >= 5000){print &DOWN("$STATUS_NAME[4]");$PL_VALUES[16]=int($PL_VALUES[16]*0.995);}
#		if ($Event == 17 && $PL_VALUES[18] >= 100){print &DOWN("$STATUS_NAME[5]");$PL_VALUES[18]=int($PL_VALUES[18]*0.995);}
##		if ($Event == 18 && $PL_VALUES[57] >= 1){print &DOWN("知力");$PL_VALUES[57]--;$PL_INT--;}
##		if ($Event == 19 && $PL_VALUES[58] >= 1){print &DOWN("精神");$PL_VALUES[58]--;$PL_MEN--;}
##		if ($Event == 20 && $PL_VALUES[59] >= 1){print &DOWN("魅力");$PL_VALUES[59]--;$PL_MIR--;}
##		if ($Event == 21 && $PL_VALUES[60] >= 1){print &DOWN("愛");$PL_VALUES[60]--;$PL_AI--;}
#	}

}

##武具経験値処理
sub vabattle7{
	&EXP('PL','p');
	&EXP('VS','vs');
	
	$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
	$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;

#アビリティシステム
	if($AbiSys == 1){

		if($PL_MAXHP > 0){$PL_VALUES[16] = $PL_MAXHP;}
		if($PL_MAXMP > 0){$PL_VALUES[18] = $PL_MAXMP;}
		if($VS_MAXHP > 0){$VS_VALUES[16] = $VS_MAXHP;}
		if($VS_MAXMP > 0){$VS_VALUES[18] = $VS_MAXMP;}

	}else{
	
		if($PL_VALUES[52] ne ""){$PL_VALUES[52] = ""}
		if($PL_VALUES[53] ne ""){$PL_VALUES[53] = ""}
	
	}

#	$PL_VALUES[19] = $PL_STR;
#	$PL_VALUES[20] = $PL_VIT;
#	$PL_VALUES[21] = $PL_AGI;
#	$PL_VALUES[22] = $PL_DEX;
#	$VS_VALUES[19] = $VS_STR;
#	$VS_VALUES[20] = $VS_VIT;
#	$VS_VALUES[21] = $VS_AGI;
#	$VS_VALUES[22] = $VS_DEX;

}
sub vabattle8{
#	$CL_VALUES[1]+=$VS_VALUES[0]+20+int(rand(5));
#	$CL_VALUES[1]+=int(($VS_VALUES[0]+20+int(rand(5)))*2);
	$CL_VALUES[1]+=int(($VS_VALUES[0]+40+int(100)+int(rand(30)))*3);
	$CL_VALUES[1]=200000 if $CL_VALUES[1] > 200000;

##クラス変化時処理追加
	&GOUSEI('c2','PL','VS') if $PL_VALUES[4] =~ /^65$|^70$|^197$|^198$|^199$|^200$|^201$|^208$|^209$|^210$|^211$/i;
	&GOUSEI('c2','VS','PL') if $VS_VALUES[4] =~ /^65$|^70$|^197$|^198$|^199$|^200$|^201$|^208$|^209$|^210$|^211$/i;
#####系譜
	$R_VALUES[0]+=1;#戦闘回数
	$R_VALUES[5]+=$Pl_AtPoint;#ダメージ
	$R_VALUES[6]+=$Vs_AtPoint;#被ダメージ
	$R_VALUES[8]+=($PL_In[2]+$VS_In[2]);#goth
	$R_VALUES[9]+=$PL_In[4];#経験値$Sakusen
	$R_VALUES[66]+=$VS_VALUES[0]+20;#国費
#####作戦使用回数
	my@sakusen=('通常攻撃','突撃','防御','ヒットアンドアウェイ','狙撃','捨て身','見切り','ダブルアタック');
		for($p=0; $p < @sakusen; $p++){
			if($sakusen[$p] eq "$Pl_MsnStyle"){$psasen=$p+138;last;}
		}
		for($v=0; $v < @sakusen; $v++){
			if($sakusen[$v] eq "$Vs_MsnStyle"){$vsasen=$v+146;last;}
		}
	$R_VALUES[$psasen]+=1;
	$R_VALUES[$vsasen]+=1;	
}
sub vabattle9{

	dbmopen (%PL,"$DBM_P",0666);
		$PL{"$FORM{'pname'}"}="@PL_VALUES";
		$PL{"$FORM{'vsname'}"}="@VS_VALUES" if !$FORM{'yousai'};
	dbmclose %PL;

	dbmopen (%R,"$DBM_R",0666);
		$R{"server"}="@R_VALUES";
	dbmclose %R;

	if (($FORM{'b_mode'} eq '内乱' && $B_Com && $PL_VALUES[6] == 1) || $TheEnd){
		dbmopen (%DH,"$DBM_H",0666);
			$DH{"$DATE"}="<B class=rb3>$PL_VALUES[5]</B> で内乱勃発 $FORM{'pname'} が全権を掌握。$FORM{'vsname'}失脚。（$FORM{'pname'}革命）" if $B_Com;
			$DH{"$DATE"}="<B class=rb3>$PL_VALUES[5]</B>の侵攻により、$VS_VALUES[3]が陥落。<B class=rb4>$VS_Country</B>滅亡。<BR>〉 〉 〉 〉 〉 〉 〉 〉 〉 MVP 〈 $FORM{'pname'} 〉$TROPHIES $Mone $Getcard" if $TheEnd;
		dbmclose %DH;
	}

	if ($PL_Country ne "$NONE_NATIONALITY" && !$FORM{'b_mode'}){
		dbmopen (%CL,"$DBM_C",0666);
			$CL{"$PL_Country"}="@CL_VALUES" if $CL{"$PL_Country"} && $PL_Country ne "$NONE_NATIONALITY";
			$CL{"$VS_Country"}="@VC_VALUES" if $FORM{'yousai'} && !$TheEnd;
			delete $CL {"$VS_Country"} if $CL{"$VS_Country"} && $TheEnd;
		dbmclose %CL;
	}
	&UNLOCK;

#	$NEWDATE2=time;
#</tr></table><table border=1 bordercolor=#333333 bgcolor=#000000 cellspacing=0>
#	<form action=$MAIN_SCRIPT name="FM" method="POST" target=Sub><td colspan=7>
#	<input type=hidden name=cmd value=BATTLE_2>
#	<input type=hidden name="pname" value="$FORM{'pname'}">
#	<input type=hidden name="pass" value="$FORM{'pass'}">
#	<input type=hidden name="check" value="$DATE">
#	<input type=hidden name="scheck" value="$NEWDATE2">
#	<b $chaStyl> </b><br>
#	<input type=submit name="b_mode" value="再攻撃" $STYLE_B1>
#	</td>

	print << "	END_OF_HTML";
	</td></tr></table><table border=1 bordercolor=#333333 cellspacing=0>
	<form action=$MAIN_SCRIPT method=POST id=go target=Main>
	<input type=hidden name=cmd value=MAIN_FRAME>
	<input type=hidden name=pname value=$FORM{'pname'}>
	<input type=hidden name=pass value=$FORM{'pass'}>
	<input type=submit value="帰還" name="gogo" style="display:none;" onClick=\"parent.Sub.location.replace(\'$BACKFR\');\">
	</form><tr><td bgcolor=\"$BG_STATUS\"><b $chaStyl>&nbsp;</b><br>
	<input type=submit value="帰還" onClick=\"kikan(0);\">
	</td>
	</tr></table>
	</body>
	</html>
	END_OF_HTML
}

##防具装備"
sub ELEMENT{
		my$PA="$_[1]_VALUES";my$PS="$_[1]_CLASS";my$SL="$_[1]_ShieldNameA";
		my$SM="$_[2]_W";my$SA="$_[1]_W";my$SB="$_[1]_sB";my$SC="$_[1]_sC";my$D0="$_[1]_sD";my$S0="$_[1]_sS";#武器
		my$SF="$_[1]_LVB";my$SJ="$_[1]_LVC";my$D1="$_[1]_LVD";#防具レベル
		my$SD="$_[1]_agD";my$SE="$_[1]_agD2";my$D2="$_[1]_agDD3";#STR補正
		my$SO="$_[1]CSS";my$SN="$_[1]BSS";my$D3="$_[1]DDSS";#RES補正
		my$TC="$_[1]FP";my$TD="$_[1]GP";my$D4="$_[1]DDP";#回避率補正
		my$TI="$_[1]_mei";my$TJ="$_[1]_mei2";my$D5="$_[1]_mei3";#命中率補正
		my$TK="$_[1]_estini";my$TL="$_[1]_estini2";my$D6="$_[1]_estini3";#ini補正
		my$SR="$_[1]_BFLAG";my$SS="$_[1]_CFLAG";my$D7="$_[1]_DFLAG";my$S7="$_[1]_SFLAG";#防具フラグ

		my$E0="$_[1]_WDu";my$E1="$_[1]_WDuLv";my$E2="$_[1]_agDD4";my$E3="$_[1]WDuSS";my$E4="$_[1]WDuDP";my$E5="$_[1]_mei4";
		my$E6="$_[1]_estini4";my$E7="$_[1]_WDuFLAG";

		my$SGP="$_[1]_ShDPoint";		#ガード率

		my$WFA="$_[1]_WFA";my$WFB="$_[1]_WFB";my$WFC="$_[1]_WFC";my$WFD="$_[1]_WFD";

#		if($$WFA > 0){$R_A ="+";}else{$R_A="";}if($$WFB > 0){$R_B ="+";}else{$R_B="";}if($$WFC > 0){$R_C ="+";}else{$R_C="";}if($$WFD > 0){$R_D ="+";}else{$R_D="";}

#		#強化システムによる装飾品のST補正計算
		$AccPointA = 0;
		$AccPointB = 0;
		$AccPointC = 0;
		$AccPointD = 0;
		
#		$AccPointA = $$WFA - 4;
#		$AccPointB = $$WFB - 4;
#		$AccPointC = $$WFC - 4;
#		$AccPointD = $$WFD - 4;

#		if($$WFA > 0 && $AccPointA <= 0){$AccPointA = 1;}elsif($$WFA > 0){$AccPointA+=1;}
#		if($$WFB > 0 && $AccPointB <= 0){$AccPointB = 1;}elsif($$WFB > 0){$AccPointB+=1;}
#		if($$WFC > 0 && $AccPointC <= 0){$AccPointC = 1;}elsif($$WFC > 0){$AccPointC+=1;}
#		if($$WFD > 0 && $AccPointD <= 0){$AccPointD = 1;}elsif($$WFD > 0){$AccPointD+=1;}

#$R_A$$WFA
#if($$S0[0]){$$S7=1;}
if($$S0[0]){$$S7=1;}
#if($PL_sS[0] eq "属性ブレス" || $PL_sS[0] eq "サンダーブレス"){$$S7=1;}
#&ERROR("$R_A$$WFAと$R_B$$WFB");

#&ERROR("$PL_WDuLv");

$Staff = 0;

#	if($PL_A3 eq ""){$PL_A3 = 0;}
#	if($PL_A4 eq ""){$PL_A4 = 0;}
#	if($PL_A5 eq ""){$PL_A5 = 0;}
#	if($PL_A6 eq ""){$PL_A6 = 0;}
#	if($PL_B3 eq ""){$PL_B3 = 0;}
#	if($PL_B4 eq ""){$PL_B4 = 0;}
#	if($PL_B5 eq ""){$PL_B5 = 0;}
#	if($PL_B6 eq ""){$PL_B6 = 0;}
#	if($PL_C3 eq ""){$PL_C3 = 0;}
#	if($PL_C4 eq ""){$PL_C4 = 0;}
#	if($PL_C5 eq ""){$PL_C5 = 0;}
#	if($PL_C6 eq ""){$PL_C6 = 0;}
#	if($PL_D3 eq ""){$PL_D3 = 0;}
#	if($PL_D4 eq ""){$PL_D4 = 0;}
#	if($PL_D5 eq ""){$PL_D5 = 0;}
#	if($PL_D6 eq ""){$PL_D6 = 0;}

#$PL_WDuLv $PL_LVSS
#		if($_[1] eq 'PL'){$$E1 = $PL_WDuLv;}
#		if($_[1] eq 'VS'){$$E1 = $VS_WDuLv;}
#$PL_WDuLv $PL_LVSS
		if($_[1] eq 'PL' && $Pl_EEXP ne "0"){$$E1 = $PL_WDuLv;}
		if($_[1] eq 'VS' && $Vs_EEXP ne "0"){$$E1 = $VS_WDuLv;}

	#武器だけの情報をダミー配列で確保$Pl_EEXP = 0;$Vs_EEXP = 0;	#0：武器だけ　1：上書きされた　2：組み合わせ
#	@PL_WDu = @PL_W;$PL_WDuLv=$PL_WLV;
#	@VS_WDu = @VS_W;$VS_WDuLv=$VS_WLV;

#武器も必要では？　特殊[41-43]　防具[9]が成り立つ　防具状態の場合のみ効力を発揮したい
#変数9
#	if($$E0[1] <= 25){

#INT補正の物理影響を中断させる　INT補正は表示するが、計算処理で影響させない
#			$Pl_MOnly = 1;

$flg_Hyo = 0;
$PL_flgEnt = 0;
$VS_flgEnt = 0;
$PL_flgEnt2 = 0;
$VS_flgEnt2 = 0;
$PL_flgEnt3 = 0;
$VS_flgEnt3 = 0;
$PL_flgEnt4 = 0;
$VS_flgEnt4 = 0;


		if(!($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) && !($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) && !($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) && !($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) && !($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) && !($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){

#	$$SD=$$SD+$$SE+$$D2+$$E2;#攻撃力合算
#	$$SO=$$SO+$$SN+$$D3+$$E3;#防御力合算
#	$$TC=$$TC+$$TD+$$D4+$$E4;#回避力合算
#	$$TI=$$TI+$$TJ+$$D5+$$E5;#命中率合算
#	$$TK=$$TK+$$TL+$$D6+$$E6;#Initiative合算

			if($$E0[7] =~ m/!13|!14/ || ($$E0[7] =~ m/!15|!19/ && $$PS[17]=~ m/!1|!E007|!E008/ && $$SA[7] =~ m/!18/)){
				if($$E0[7] =~ m/!00|!01|!02|!03|!04|!05/){$$E2=int($$E0[10]+$$E1/2475);}
				else{$$E2=int($$E0[10]+$$E1/4950);}
				if ($$E0[7] =~ m/!15|!19/ && (($$SA[7] =~ m/!00/ && $$E0[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$E0[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$E0[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$E0[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$E0[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$E0[7] =~ m/!05/))){
					$$E2=int($$E2*1.3);
				}elsif (($$SA[7] =~ m/!00/ && $$E0[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$E0[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$E0[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$E0[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$E0[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$E0[7] =~ m/!05/)){
					$$E2=int($$E2*1.2);
				}elsif (($$SA[7] =~ m/!00/ && $$E0[7] =~ m/!02/) || ($$SA[7] =~ m/!01/ && $$E0[7] =~ m/!03/) || ($$SA[7] =~ m/!02/ && $$E0[7] =~ m/!00/) || ($$SA[7] =~ m/!03/ && $$E0[7] =~ m/!01/) || ($$SA[7] =~ m/!04/ && $$E0[7] =~ m/!05/) || ($$SA[7] =~ m/!05/ && $$E0[7] =~ m/!04/)){
					$$E2=int($$E2/2);
				}
				if($$E0[7] =~ m/!13/){
					if($$E0[7] =~ m/!00|!01|!02|!03|!04|!05/){$$E5=int($$E0[1]+$$E1/2475);}
					else{$$E5=int($$E0[1]+$$E1/4950);}		
					$$E2=$$E2+$AccPointA;$$E5=$$E5+$AccPointA;
					if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
						$$SL.="(STR+$$E2 DEX+$$E5)";
					}else{
						$$SL.="<br>$$E0[0](STR+$$E2 DEX+$$E5)";
					}
					$$E7=1;
					$flg_Hyo = 1;
				}elsif($$E0[7] =~ m/!14/){
					$$E6=int($$E0[1]+$$E1/1650);
					$$E2=$$E2+$AccPointA;$$E6=$$E6+$AccPointA;
					if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
						$$SL.="(STR+$$E2 INI+$$E6)";
					}else{
						$$SL.="<br>$$E0[0](STR+$$E2 INI+$$E6)";
					}
					$$E7=1;
					$flg_Hyo = 1;
				}elsif($$E0[7] =~ m/!15|!19/ && $Staff < 2 && $$SA[7] =~ m/!18/ && $$PS[17]=~ m/!1|!E007|!E008/){
					if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
						$$SL.="(INT+$$E2)";
						if($_[1] eq 'PL'){$$E2=$$E2+$PL_A11;}
						if($_[1] eq 'VS'){$$E2=$$E2+$VS_A11;}
						if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$E2 = 0;}
						if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$E2 = 0;}
					}else{
						$$SL.="<br>$$E0[0](INT+$$E2)";
						if($_[1] eq 'PL'){$$E2=$$E2+$PL_A11;}
						if($_[1] eq 'VS'){$$E2=$$E2+$VS_A11;}
						if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$E2 = 0;}
						if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$E2 = 0;}
					}
					$$E7=1;
					$flg_Hyo = 1;
				}

				if($$E0[7] =~ m/!15|!19/){$Staff = $Staff + 1;}

			}

			if($$SA[7] =~ m/!10/ && $$E0[7] =~ m/!12/ && $$SC[7] !~ m/!12/ && $$D0[7] !~ m/!12/){
				$$E3=int($$E0[1]+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
					$$E3*=2;
				}
				$$SGP=$$E3;
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3)";
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}
	#体防具
			if($$E0[7] =~ m/!1s/ && $$SB[7] !~ m/!1s|!1u|!1w/ && $$SC[7] !~ m/!1s|!1u|!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
				$$E3=int($$E0[1]+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
					$$E3=int($$E3/2);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3)";
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}
			if($$E0[7] =~ m/!1u/ && $$SB[7] !~ m/!1s|!1u|!1w/ && $$SC[7] !~ m/!1s|!1u|!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
				$$E3=int($$E0[1]+$$E1/2475);$$E5=int($$E0[1]/3+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;#$$E5*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
					$$E3=int($$E3/2);$$E5=int($$E5/2);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3 DEX+$$E5)";
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3 DEX+$$E5)";
				}
				$$E7=1;
				$flg_Hyo = 1;

			}
			if($$E0[7] =~ m/!1w/ && $$SB[7] !~ m/!1s|!1u|!1w/ && $$SC[7] !~ m/!1s|!1u|!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
				$$E3=int($$E0[1]+$$E1/2475);$$E2=int($$E0[10]+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;#$$E2*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
					$$E3=int($$E3/2);$$E2=int($$E2/2);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3 INT+$$E2)";
					if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$E2 = 0;}
					if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$E2 = 0;}
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3 INT+$$E2)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}
	#頭防具
			if($$E0[7] =~ m/!1t/ && $$SB[7] !~ m/!1t|!1v|!1x|!E0003/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
				$$E3=int($$E0[1]+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
#					$$E3=int($$E3/2);
					$$E3=int($$E3*1.5);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3)";
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3)";
				}
				$$E7=1;
				$flg_Hyo = 1;
				
			}
			if($$E0[7] =~ m/!1v/ && $$SB[7] !~ m/!1t|!1v|!1x|!E0003/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
				$$E3=int($$E0[1]+$$E1/2475);$$E4=int($$E0[10]+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;#$$E4*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
					$$E3=int($$E3/2);$$E4=int($$E4/2);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3 AGI+$$E4)";
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3 AGI+$$E4)";
				}

				$$E7=1;
				$flg_Hyo = 1;
			}
			if($$E0[7] =~ m/!1x/ && $$SB[7] !~ m/!1t|!1v|!1x|!E0003/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
				$$E3=int($$E0[1]+$$E1/2475);$$E2=int($$E0[10]+$$E1/2475);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;#$$E2*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
					$$E3=int($$E3/2);$$E2=int($$E2/2);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3 INT+$$E2)";
					if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$E2 = 0;}
					if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$E2 = 0;}
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3 INT+$$E2)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}
			#200905New! E3 RES  E2 STR  E4 AGI
			if($$E0[7] =~ m/!E0003/ && $$SB[7] !~ m/!1t|!1v|!1x|!E0003/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
#				$$E3=int($$E0[1]+$$E1/2475);$$E2=int(5+$$E1/2475);$$E4=int(2+$$E1/2475);
				$$E3=int($$E0[1]+$$E1/2475);$$E2=int(3+$$E1/4950);$$E4=int(1+$$E1/4950);
				if (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#					$$E3*=2;#$$E2*=2;
					$$E3=int($$E3*1.5);
				}elsif (($$E0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$E0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$E0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$E0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$E0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$E0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
					$$E3=int($$E3/2);$$E2=int($$E2/2);$$E4=int($$E4/2);
				}
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(RES+$$E3 STR+$$E2 AGI+$$E4)";
				}else{
					$$SL.="<br>$$E0[0](RES+$$E3 STR+$$E2 AGI+$$E4)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}

			if($$E0[7] =~ m/!16/ && $$SB[7] !~ m/!16/ && $$SC[7] !~ m/!16/ && $$D0[7] !~ m/!16/){
				$$E4=int($$E0[1]+$$E1/2475);
				$$E4=$$E4+$AccPointA;
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(AGI+$$E4)";
				}else{
					$$SL.="<br>$$E0[0](AGI+$$E4)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}
			if($$E0[7] =~ m/!17/){
				$$E4=int($$E0[1]+$$E1/2475);$$E5=int($$E0[10]+$$E1/2475);
				$$E4=$$E4+$AccPointA;$$E5=$$E5+$AccPointA;
				if(($_[1] eq 'PL' && $Pl_EEXP eq "2") || ($_[1] eq 'VS' && $Vs_EEXP eq "2")){
					$$SL.="(AGI+$$E4 DEX+$$E5)";
				}else{
					$$SL.="<br>$$E0[0](AGI+$$E4 DEX+$$E5)";
				}
				$$E7=1;
				$flg_Hyo = 1;
			}

			#エンチャントフラグ
			if($_[1] eq 'PL'){$PL_flgEnt = 1;}
			if($_[1] eq 'VS'){$VS_flgEnt = 1;}
			
#			if($_[1] eq 'PL' && $flg_Hyo eq "1"){
			if($_[1] eq 'PL'){
				if($$E2 eq ""){$$E2 = 0;}
				if($$E3 eq ""){$$E3 = 0;}
				if($$E4 eq ""){$$E4 = 0;}
				if($$E5 eq ""){$$E5 = 0;}

				$$E2 = $$E2 + $PL_WA03;
#				$$E3 = $$E3 + $PL_WA04;
				$$E4 = $$E4 + $PL_WA05;
				$$E5 = $$E5 + $PL_WA06;

				$$E3 = $$E3 + $PL_WA13;

			}
#			if($_[1] eq 'VS' && $flg_Hyo eq "1"){
			if($_[1] eq 'VS'){
				if($$E2 eq ""){$$E2 = 0;}
				if($$E3 eq ""){$$E3 = 0;}
				if($$E4 eq ""){$$E4 = 0;}
				if($$E5 eq ""){$$E5 = 0;}

				$$E2 = $$E2 + $VS_WA03;
#				$$E3 = $$E3 + $VS_WA04;
				$$E4 = $$E4 + $VS_WA05;
				$$E5 = $$E5 + $VS_WA06;

				$$E3 = $$E3 + $VS_WA13;

			}
			
		}
#	}


$flg_Hyo = 0;

#防具1
	if(!($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) && !($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) && !($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) && !($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) && !($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) && !($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
		
		$flg_EntCnt = 1;
		
		if($$SB[7] =~ m/!13|!14/ || ($$SB[7] =~ m/!15|!19/ && $$PS[17]=~ m/!1|!E007|!E008/ && $$SA[7] =~ m/!18/)){

#			$$SD=int($$SB[10]+$$SF/2475);
			if($$SB[7] =~ m/!00|!01|!02|!03|!04|!05/){$$SD=int($$SB[10]+$$SF/2475);}
			else{$$SD=int($$SB[10]+$$SF/4950);}

			if ($$SB[7] =~ m/!15|!19/ && (($$SA[7] =~ m/!00/ && $$SB[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$SB[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$SB[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$SB[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$SB[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$SB[7] =~ m/!05/))){
				$$SD=int($$SD*1.3);
			}elsif (($$SA[7] =~ m/!00/ && $$SB[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$SB[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$SB[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$SB[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$SB[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$SB[7] =~ m/!05/)){
				$$SD=int($$SD*1.2);
			}elsif (($$SA[7] =~ m/!00/ && $$SB[7] =~ m/!02/) || ($$SA[7] =~ m/!01/ && $$SB[7] =~ m/!03/) || ($$SA[7] =~ m/!02/ && $$SB[7] =~ m/!00/) || ($$SA[7] =~ m/!03/ && $$SB[7] =~ m/!01/) || ($$SA[7] =~ m/!04/ && $$SB[7] =~ m/!05/) || ($$SA[7] =~ m/!05/ && $$SB[7] =~ m/!04/)){
				$$SD=int($$SD/2);
			}
			if($$SB[7] =~ m/!13/){
				if($$SB[7] =~ m/!00|!01|!02|!03|!04|!05/){$$TI=int($$SB[1]+$$SF/2475);}
				else{$$TI=int($$SB[1]+$$SF/4950);}		
				$$SD=$$SD+$AccPointB;$$TI=$$TI+$AccPointB;
#				$$TI=int($$SB[1]+$$SF/2475);
				$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](STR+$$SD DEX+$$TI)";$$SR=1;
				$flg_Hyo = 1;
			}elsif($$SB[7] =~ m/!14/){
				$$TL=int($$SB[1]+$$SF/1650);
				$$SD=$$SD+$AccPointB;$$TL=$$TL+$AccPointB;
				$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](STR+$$SD INI+$$TL)";$$SR=1;
				$flg_Hyo = 1;
			}elsif($$SB[7] =~ m/!15|!19/ && $Staff < 2 && $$SA[7] =~ m/!18/ && $$PS[17]=~ m/!1|!E007|!E008/){
				$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](INT+$$SD)";$$SR=1;
				if($_[1] eq 'PL'){$$SD=$$SD+$PL_B11;}
				if($_[1] eq 'VS'){$$SD=$$SD+$VS_B11;}
				if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$SD = 0;}
				if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$SD = 0;}
				$flg_Hyo = 1;
			}

			if($$SB[7] =~ m/!15|!19/){$Staff = $Staff + 1;}

		}

		if($$SA[7] =~ m/!10/ && $$SB[7] =~ m/!12/ && $$SC[7] !~ m/!12/ && $$D0[7] !~ m/!12/){
			$$SN=int($$SB[1]+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
				$$SN*=2;
			}
			$$SGP=$$SN;
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN)";$$SR=1;
			$flg_Hyo = 1;
		}
#体防具
		if($$SB[7] =~ m/!1s/ && $$SC[7] !~ m/!1s|!1u|!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
			$$SN=int($$SB[1]+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN)";$$SR=1;
			$flg_Hyo = 1;
		}
		if($$SB[7] =~ m/!1u/ && $$SC[7] !~ m/!1s|!1u|!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
			$$SN=int($$SB[1]+$$SF/2475);$$TI=int($$SB[1]/3+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;#$$TI*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);$$TI=int($$TI/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN DEX+$$TI)";$$SR=1;
			$flg_Hyo = 1;
		}
		if($$SB[7] =~ m/!1w/ && $$SC[7] !~ m/!1s|!1u|!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
			$$SN=int($$SB[1]+$$SF/2475);$$SD=int($$SB[10]+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;#$$SD*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);$$SD=int($$SD/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN INT+$$SD)";$$SR=1;
			if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$SD = 0;}
			if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$SD = 0;}
			$flg_Hyo = 1;
		}
#頭防具
		if($$SB[7] =~ m/!1t/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
			$$SN=int($$SB[1]+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN)";$$SR=1;
			$flg_Hyo = 1;
		}
		if($$SB[7] =~ m/!1v/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
			$$SN=int($$SB[1]+$$SF/2475);$$TC=int($$SB[10]+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;#$$TC*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);$$TC=int($$TC/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN AGI+$$TC)";$$SR=1;
			$flg_Hyo = 1;
		}
		if($$SB[7] =~ m/!1x/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
			$$SN=int($$SB[1]+$$SF/2475);$$SD=int($$SB[10]+$$SF/2475);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;#$$SD*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);$$SD=int($$SD/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN INT+$$SD)";$$SR=1;
			if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$SD = 0;}
			if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$SD = 0;}
			$flg_Hyo = 1;
		}
		#200905 SD str tc agi
		if($$SB[7] =~ m/!E0003/ && $$SC[7] !~ m/!1t|!1v|!1x|!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
#			$$SN=int($$SB[1]+$$SF/2475);$$SD=int(5+$$SF/2475);$$TC=int(2+$$SF/2475);
			$$SN=int($$SB[1]+$$SF/2475);$$SD=int(3+$$SF/4950);$$TC=int(1+$$SF/4950);
			if (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SN*=2;#$$SD*=2;
				$$SN=int($$SN*1.5);
			}elsif (($$SB[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SB[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SB[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SB[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SB[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SB[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SN=int($$SN/2);$$SD=int($$SD/2);$$TC=int($$TC/2);
			}
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](RES+$$SN STR+$$SD AGI+$$TC)";$$SR=1;
			$flg_Hyo = 1;
		}

		if($$SB[7] =~ m/!16/ && $$SC[7] !~ m/!16/ && $$D0[7] !~ m/!16/){
			$$TC=int($$SB[1]+$$SF/2475);
			$$TC=$$TC+$AccPointB;
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](AGI+$$TC)";$$SR=1;
			$flg_Hyo = 1;
		}
		if($$SB[7] =~ m/!17/){
			$$TC=int($$SB[1]+$$SF/2475);$$TI=int($$SB[10]+$$SF/2475);
			$$TC=$$TC+$AccPointB;$$TI=$$TI+$AccPointB;
			$$SL.="<br>$R_B$$WFB&nbsp;$$SB[0](AGI+$$TC DEX+$$TI)";$$SR=1;
			$flg_Hyo = 1;
		}

#	$$SD=$$SD+$$SE+$$D2+$$E2;#攻撃力合算
#	$$SO=$$SO+$$SN+$$D3+$$E3;#防御力合算
#	$$TC=$$TC+$$TD+$$D4+$$E4;#回避力合算
#	$$TI=$$TI+$$TJ+$$D5+$$E5;#命中率合算
#	$$TK=$$TK+$$TL+$$D6+$$E6;#Initiative合算		#エンチャント

		#エンチャントフラグ
		if($_[1] eq 'PL'){$PL_flgEnt2 = 1;}
		if($_[1] eq 'VS'){$VS_flgEnt2 = 1;}

		#エンチャント
		if($_[1] eq 'PL' && $flg_Hyo eq "1"){
			$$SD = $$SD + $PL_WB03;
#			$$SO = $$SO + $PL_WB04;
			$$TC = $$TC + $PL_WB05;
			$$TI = $$TI + $PL_WB06;

			$$SO = $$SO + $PL_WB13;

		}
		if($_[1] eq 'VS' && $flg_Hyo eq "1"){
			$$SD = $$SD + $VS_WB03;
#			$$SO = $$SO + $VS_WB04;
			$$TC = $$TC + $VS_WB05;
			$$TI = $$TI + $VS_WB06;

			$$SO = $$SO + $VS_WB13;

		}
			
	}
$flg_Hyo = 0;
#&ERROR("$$SM[7]あ$$SC[7]いい$$SM[0]あ$$SC[0]");

	if(!($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) && !($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) && !($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) && !($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) && !($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) && !($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
		
		if($$SC[7] =~ m/!13|!14/ || ($$SC[7] =~ m/!15|!19/ && $$PS[17]=~ m/!1|!E007|!E008/ && $$SA[7] =~ m/!18/)){
#			$$SE=int($$SC[10]+$$SJ/2475);
			if($$SC[7] =~ m/!00|!01|!02|!03|!04|!05/){$$SE=int($$SC[10]+$$SJ/2475);}
			else{$$SE=int($$SC[10]+$$SJ/4950);}
			if ($$SC[7] =~ m/!15|!19/ && (($$SA[7] =~ m/!00/ && $$SC[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$SC[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$SC[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$SC[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$SC[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$SC[7] =~ m/!05/))){
				$$SE=int($$SE*1.3);
			}elsif (($$SA[7] =~ m/!00/ && $$SC[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$SC[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$SC[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$SC[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$SC[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$SC[7] =~ m/!05/)){
				$$SE=int($$SE*1.2);
			}elsif (($$SA[7] =~ m/!00/ && $$SC[7] =~ m/!02/) || ($$SA[7] =~ m/!01/ && $$SC[7] =~ m/!03/) || ($$SA[7] =~ m/!02/ && $$SC[7] =~ m/!00/) || ($$SA[7] =~ m/!03/ && $$SC[7] =~ m/!01/) || ($$SA[7] =~ m/!04/ && $$SC[7] =~ m/!05/) || ($$SA[7] =~ m/!05/ && $$SC[7] =~ m/!04/)){
				$$SE=int($$SE/2);
			}
			if($$SC[7] =~ m/!13/){
#				$$TJ=int($$SC[1]+$$SJ/2475);
				if($$SC[7] =~ m/!00|!01|!02|!03|!04|!05/){$$TJ=int($$SC[1]+$$SJ/2475);}
				else{$$TJ=int($$SC[1]+$$SJ/4950);}		
				$$SE=$$SE+$AccPointC;$$TJ=$$TJ+$AccPointC;

				$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](STR+$$SE DEX+$$TJ)";$$SS=1;
				$flg_Hyo = 1;
			}elsif($$SC[7] =~ m/!14/){
				$$TK=int($$SC[1]+$$SJ/1650);
				$$SE=$$SE+$AccPointC;$$TK=$$TK+$AccPointC;
				$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](STR+$$SE INI+$$TK)";$$SS=1;
				$flg_Hyo = 1;
			}elsif($$SC[7] =~ m/!15|!19/ && $Staff < 2 && $$SA[7] =~ m/!18/ && $$PS[17]=~ m/!1|!E007|!E008/){
				$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](INT+$$SE)";$$SS=1;
				if($_[1] eq 'PL'){$$SE=$$SE+$PL_C11;}
				if($_[1] eq 'VS'){$$SE=$$SE+$VS_C11;}
				if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$SE = 0;}
				if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$SE = 0;}
				$flg_Hyo = 1;
			}

			if($$SC[7] =~ m/!15|!19/){$Staff = $Staff + 1;}

		}
#		if($$SA[7] =~ m/!10/ && $$SC[7] =~ m/!12/){
		if($$SA[7] =~ m/!10/ && $$SC[7] =~ m/!12/ && $$D0[7] !~ m/!12/){
			$$SO=int($$SC[1]+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
				$$SO*=2;
			}
			$$SGP=$$SO;
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO)";$$SS=1;
			$flg_Hyo = 1;
		}

#体防具
		if($$SC[7] =~ m/!1s/ && $$D0[7] !~ m/!1s|!1u|!1w/){
			$$SO=int($$SC[1]+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO)";$$SS=1;
			$flg_Hyo = 1;
		}
		if($$SC[7] =~ m/!1u/ && $$D0[7] !~ m/!1s|!1u|!1w/){
			$$SO=int($$SC[1]+$$SJ/2475);$$TJ=int($$SC[1]/3+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;#$$TJ*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);$$TJ=int($$TJ/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO DEX+$$TJ)";$$SS=1;
			$flg_Hyo = 1;
		}
		if($$SC[7] =~ m/!1w/ && $$D0[7] !~ m/!1s|!1u|!1w/){
			$$SO=int($$SC[1]+$$SJ/2475);$$SE=int($$SC[10]+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;#$$SE*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);$$SE=int($$SE/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO INT+$$SE)";$$SS=1;
			$flg_Hyo = 1;
			if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$SE = 0;}
			if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$SE = 0;}
		}
#頭防具
		if($$SC[7] =~ m/!1t/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
			$$SO=int($$SC[1]+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO)";$$SS=1;
			$flg_Hyo = 1;
		}
		if($$SC[7] =~ m/!1v/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
			$$SO=int($$SC[1]+$$SJ/2475);$$TD=int($$SC[10]+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;#$$TD*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);$$TD=int($$TD/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO AGI+$$TD)";$$SS=1;
			$flg_Hyo = 1;
		}
		if($$SC[7] =~ m/!1x/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
			$$SO=int($$SC[1]+$$SJ/2475);$$SE=int($$SC[10]+$$SJ/2475);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;#$$SE*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);$$SE=int($$SE/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO INT+$$SE)";$$SS=1;
			if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$SE = 0;}
			if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$SE = 0;}
			$flg_Hyo = 1;
		}
		#200905 se str td agi
		if($$SC[7] =~ m/!E0003/ && $$D0[7] !~ m/!1t|!1v|!1x|!E0003/){
#			$$SO=int($$SC[1]+$$SJ/2475);$$SE=int(5+$$SJ/2475);$$TD=int(2+$$SJ/2475);
			$$SO=int($$SC[1]+$$SJ/2475);$$SE=int(3+$$SJ/4950);$$TD=int(1+$$SJ/4950);
			if (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$SO*=2;#$$SE*=2;
				$$SO=int($$SO*1.5);
			}elsif (($$SC[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$SC[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$SC[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$SC[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$SC[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$SC[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$SO=int($$SO/2);$$SE=int($$SE/2);$$TD=int($$TD/2);
			}
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](RES+$$SO STR+$$SE AGI+$$TD)";$$SS=1;
			$flg_Hyo = 1;
		}

		if($$SC[7] =~ m/!16/ && $$D0[7] !~ m/!16/){
			$$TD=int($$SC[1]+$$SJ/2475);
			$$TD=$$TD+$AccPointC;
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](AGI+$$TD)";$$SS=1;
			$flg_Hyo = 1;
		}
		if($$SC[7] =~ m/!17/){
			$$TD=int($$SC[1]+$$SJ/2475);$$TJ=int($$SC[10]+$$SJ/2475);
			$$TD=$$TD+$AccPointC;$$TJ=$$TJ+$AccPointC;
			$$SL.="<br>$R_C$$WFC&nbsp;$$SC[0](AGI+$$TD DEX+$$TJ)";$$SS=1;
			$flg_Hyo = 1;
		}

#	$$SD=$$SD+$$SE+$$D2+$$E2;#攻撃力合算
#	$$SO=$$SO+$$SN+$$D3+$$E3;#防御力合算
#	$$TC=$$TC+$$TD+$$D4+$$E4;#回避力合算
#	$$TI=$$TI+$$TJ+$$D5+$$E5;#命中率合算
#	$$TK=$$TK+$$TL+$$D6+$$E6;#Initiative合算		#エンチャント
		#エンチャントフラグ
		if($_[1] eq 'PL'){$PL_flgEnt3 = 1;}
		if($_[1] eq 'VS'){$VS_flgEnt3 = 1;}

		#エンチャント
#			&ERROR("$_[1]ああ$PL_WC03と$flg_Hyo");
		if($_[1] eq 'PL' && $flg_Hyo eq "1"){
			$$SE = $$SE + $PL_WC03;
#			$$SN = $$SN + $PL_WC04;
			$$TD = $$TD + $PL_WC04;
			$$TJ = $$TJ + $PL_WC04;

			$$SN = $$SN + $PL_WC13;

		}
		if($_[1] eq 'VS' && $flg_Hyo eq "1"){
			$$SE = $$SE + $VS_WC03;
			$$SN = $$SN + $VS_WC04;
			$$TD = $$TD + $VS_WC05;
			$$TJ = $$TJ + $VS_WC06;

			$$SN = $$SN + $VS_WC13;

		}

	}
$flg_Hyo = 0;

	if(!($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) && !($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) && !($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) && !($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) && !($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) && !($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){

		if($$D0[7] =~ m/!13|!14/ || ($$D0[7] =~ m/!15|!19/ && $$PS[17]=~ m/!1|!E007|!E008/ && $$SA[7] =~ m/!18/)){
#			$$D2=int($$D0[10]+$$D1/2475);
			if($$D0[7] =~ m/!00|!01|!02|!03|!04|!05/){$$D2=int($$D0[10]+$$D1/2475);}
			else{$$D2=int($$D0[10]+$$D1/4950);}

			if ($$D0[7] =~ m/!15|!19/ && (($$SA[7] =~ m/!00/ && $$D0[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$D0[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$D0[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$D0[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$D0[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$D0[7] =~ m/!05/))){
				$$D2=int($$D2*1.3);
			}elsif (($$SA[7] =~ m/!00/ && $$D0[7] =~ m/!00/) || ($$SA[7] =~ m/!01/ && $$D0[7] =~ m/!01/) || ($$SA[7] =~ m/!02/ && $$D0[7] =~ m/!02/) || ($$SA[7] =~ m/!03/ && $$D0[7] =~ m/!03/) || ($$SA[7] =~ m/!04/ && $$D0[7] =~ m/!04/) || ($$SA[7] =~ m/!05/ && $$D0[7] =~ m/!05/)){
				$$D2=int($$D2*1.2);
			}elsif (($$SA[7] =~ m/!00/ && $$D0[7] =~ m/!02/) || ($$SA[7] =~ m/!01/ && $$D0[7] =~ m/!03/) || ($$SA[7] =~ m/!02/ && $$D0[7] =~ m/!00/) || ($$SA[7] =~ m/!03/ && $$D0[7] =~ m/!01/) || ($$SA[7] =~ m/!04/ && $$D0[7] =~ m/!05/) || ($$SA[7] =~ m/!05/ && $$D0[7] =~ m/!04/)){
				$$D2=int($$D2/2);
			}
			if($$D0[7] =~ m/!13/){
#				$$D5=int($$D0[1]+$$D1/2475);
				if($$D0[7] =~ m/!00|!01|!02|!03|!04|!05/){$$D5=int($$D0[1]+$$D1/2475);}
				else{$$D5=int($$D0[1]+$$D1/4950);}		
				$$D2=$$D2+$AccPointD;$$D5=$$D5+$AccPointD;

				$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](STR+$$D2 DEX+$$D5)";$$D7=1;
				$flg_Hyo = 1;
			}elsif($$D0[7] =~ m/!14/){
				$$D6=int($$D0[1]+$$D1/1650);
				$$D2=$$D2+$AccPointD;$$D6=$$D6+$AccPointD;
				$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](STR+$$D2 INI+$$D6)";$$D7=1;
				$flg_Hyo = 1;
			}elsif($$D0[7] =~ m/!15|!19/ && $Staff < 2 && $$SA[7] =~ m/!18/ && $$PS[17]=~ m/!1|!E007|!E008/){
				$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](INT+$$D2)";$$D7=1;
				if($_[1] eq 'PL'){$$D2=$$D2+$PL_D11;}
				if($_[1] eq 'VS'){$$D2=$$D2+$VS_D11;}
				if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$D2 = 0;}
				if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$D2 = 0;}
				$flg_Hyo = 1;
			}

			if($$D0[7] =~ m/!15|!19/){$Staff = $Staff + 1;}

		}
		if($$SA[7] =~ m/!10/ && $$D0[7] =~ m/!12/){
			$$D3=int($$D0[1]+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
				$$D3*=2;
			}
			$$SGP=$$D3;
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3)";$$D7=1;
			$flg_Hyo = 1;
		}

#体防具
		if($$D0[7] =~ m/!1s/){
			$$D3=int($$D0[1]+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3)";$$D7=1;
			$flg_Hyo = 1;
		}
		if($$D0[7] =~ m/!1u/){
			$$D3=int($$D0[1]+$$D1/2475);$$D5=int($$D0[1]/3+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;#$$D5*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);$$D5=int($$D5/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3 DEX+$$D5)";$$D7=1;
			$flg_Hyo = 1;
		}
		if($$D0[7] =~ m/!1w/){
			$$D3=int($$D0[1]+$$D1/2475);$$D2=int($$D0[10]+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;#$$D2*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);$$D2=int($$D2/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3 INT+$$D2)";$$D7=1;
			if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$D2 = 0;}
			if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$D2 = 0;}
			$flg_Hyo = 1;
		}
#頭防具
		if($$D0[7] =~ m/!1t/){
			$$D3=int($$D0[1]+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3)";$$D7=1;
			$flg_Hyo = 1;
		}
		if($$D0[7] =~ m/!1v/){
			$$D3=int($$D0[1]+$$D1/2475);$$D4=int($$D0[10]+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;#$$D4*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);$$D4=int($$D4/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3 AGI+$$D4)";$$D7=1;
			$flg_Hyo = 1;
		}
		if($$D0[7] =~ m/!1x/){
			$$D3=int($$D0[1]+$$D1/2475);$$D2=int($$D0[10]+$$D1/2475);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;#$$D2*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);$$D2=int($$D2/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3 INT+$$D2)";$$D7=1;
			if($_[1] eq 'PL' && $Pl_MOnly ne '1'){$$D2 = 0;}
			if($_[1] eq 'VS' && $Vs_MOnly ne '1'){$$D2 = 0;}
			$flg_Hyo = 1;
		}
		if($$D0[7] =~ m/!E0003/){
#			$$D3=int($$D0[1]+$$D1/2475);$$D2=int($$D0[10]+$$D1/2475);$$D4=int($$D0[10]+$$D1/2475);
			$$D3=int($$D0[1]+$$D1/2475);$$D2=int(3+$$D1/4950);$$D4=int(2+$$D1/4950);
			if (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!04/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!05/)){
#				$$D3*=2;#$$D2*=2;
				$$D3=int($$D3*1.5);
			}elsif (($$D0[7] =~ m/!00/ && $$SM[7] =~ m/!02/) || ($$D0[7] =~ m/!01/ && $$SM[7] =~ m/!03/) || ($$D0[7] =~ m/!02/ && $$SM[7] =~ m/!00/) || ($$D0[7] =~ m/!03/ && $$SM[7] =~ m/!01/) || ($$D0[7] =~ m/!04/ && $$SM[7] =~ m/!05/) || ($$D0[7] =~ m/!05/ && $$SM[7] =~ m/!04/)){
				$$D3=int($$D3/2);$$D2=int($$D2/2);$$D4=int($$D4/2);
			}
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](RES+$$D3 STR+$$D2 AGI+$$D4)";$$D7=1;
			$flg_Hyo = 1;
		}

		if($$D0[7] =~ m/!16/){
			$$D4=int($$D0[1]+$$D1/2475);
			$$D4=$$D4+$AccPointD;
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](AGI+$$D4)";$$D7=1;
			$flg_Hyo = 1;
		}
		if($$D0[7] =~ m/!17/){
			$$D4=int($$D0[1]+$$D1/2475);$$D5=int($$D0[10]+$$D1/2475);
			$$D4=$$D4+$AccPointD;$$D0=$$D0+$AccPointD;
			$$SL.="<br>$R_D$$WFD&nbsp;$$D0[0](AGI+$$D4 DEX+$$D5)";$$D7=1;
			$flg_Hyo = 1;
		}

		#エンチャントフラグ
		if($_[1] eq 'PL'){$PL_flgEnt4 = 1;}
		if($_[1] eq 'VS'){$VS_flgEnt4 = 1;}

		if($_[1] eq 'PL' && $flg_Hyo eq "1"){
			$$D2 = $$D2 + $PL_WD03;
#			$$D3 = $$D3 + $PL_WD04;
			$$D4 = $$D4 + $PL_WD05;
			$$D5 = $$D5 + $PL_WD06;

			$$D3 = $$D3 + $PL_WD13;
		}
		if($_[1] eq 'VS' && $flg_Hyo eq "1"){
			$$D2 = $$D2 + $VS_WA03;
#			$$D3 = $$D3 + $VS_WA04;
			$$D4 = $$D4 + $VS_WA05;
			$$D5 = $$D5 + $VS_WA06;
			
			$$D3 = $$D3 + $VS_WA13;
		}
		
	}

	$$SD=$$SD+$$SE+$$D2+$$E2;#攻撃力合算
	$$SO=$$SO+$$SN+$$D3+$$E3;#防御力合算
	$$TC=$$TC+$$TD+$$D4+$$E4;#回避力合算
	$$TI=$$TI+$$TJ+$$D5+$$E5;#命中率合算
	$$TK=$$TK+$$TL+$$D6+$$E6;#Initiative合算
#&ERROR("$$SDあ$$SEい$$D2う","$$SOあ$$SNい$$D3う");
}
######性能変化
sub SEINOU{
	if($_[0] eq 'b'){
		$PA="$_[1]_VALUES";$PS="$_[1]_CLASS";
		$SA="$_[1]_W";$SB="$_[1]_sB";$SC="$_[1]_sC";$SD="$_[1]_sD";$SF="$_[1]_sS";
#セット装備
#		if($$SA[7]=~ m/!50|!51|!52|!53|!54|!55|!57/ && $_[3] eq '0' && $_[4] eq '1'){
		if($$SA[7]=~ m/!50|!51|!52|!53|!54|!55|!57/ && $_[4] eq '1'){
#		if($$SA[7]=~ m/!50|!51|!52|!53|!54|!55|!57/ && $_[3] eq '0' && $_[4] eq '1' && $PL_VALUES[5] eq "あいうえおだよん"){

#			#超神聖：既存
#			if($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && (($$SB[1] <= 40 && $$SB[7]=~ m/!50/ && $$SC[7] !~ m/!12/ && $$SD[7] !~ m/!12/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!50/ && $$SD[7] !~ m/!12/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!50/))){$$SA[1]+=5500;$$SA[2]-=2;$$SA[4]+=110;}
#			#超神聖：既存+兜/鎧　武器だけは名称使用ダメ　特殊使用時も反映されちゃうから
#			if($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SB[0] eq "聖者の盾" && (($$SC[0] eq "サザンクロス" || $$SC[0] eq "フロイデヘルム") || ($$SD[0] eq "サザンクロス" || $$SD[0] eq "フロイデヘルム"))){$$SA[2]+=22;$$SA[4]-=70;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SC[0] eq "聖者の盾" && (($$SB[0] eq "サザンクロス" || $$SB[0] eq "フロイデヘルム") || ($$SD[0] eq "サザンクロス" || $$SD[0] eq "フロイデヘルム"))){$$SA[2]+=22;$$SA[4]-=70;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SD[0] eq "聖者の盾" && (($$SB[0] eq "サザンクロス" || $$SB[0] eq "フロイデヘルム") || ($$SC[0] eq "サザンクロス" || $$SC[0] eq "フロイデヘルム"))){$$SA[2]+=22;$$SA[4]-=70;}
#			#超神聖：フルコンプ
#			if($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SB[0] eq "聖者の盾" && $$SC[0] eq "サザンクロス" && $$SD[0] eq "フロイデヘルム"){$$SA[1]+=2000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SB[0] eq "聖者の盾" && $$SD[0] eq "サザンクロス" && $$SC[0] eq "フロイデヘルム"){$$SA[1]+=2000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SC[0] eq "聖者の盾" && $$SB[0] eq "サザンクロス" && $$SD[0] eq "フロイデヘルム"){$$SA[1]+=2000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SC[0] eq "聖者の盾" && $$SD[0] eq "サザンクロス" && $$SB[0] eq "フロイデヘルム"){$$SA[1]+=2000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SD[0] eq "聖者の盾" && $$SB[0] eq "サザンクロス" && $$SC[0] eq "フロイデヘルム"){$$SA[1]+=2000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!50/ && $$SA[0] eq "オラシオン" && $$SD[0] eq "聖者の盾" && $$SC[0] eq "サザンクロス" && $$SB[0] eq "フロイデヘルム"){$$SA[1]+=2000;$$SA[4]-=40;}

			#セット値計算
			#超神聖セット
			$SetPointA = 0;
			if($$SA[0] eq "オラシオン" && $_[5] ne "5" && ($$SB[0] eq "聖者の盾" || $$SC[0] eq "聖者の盾" || $$SD[0] eq "聖者の盾")){$SetPointA = $SetPointA + 50;}
			if($$SA[0] eq "オラシオン" && $_[5] ne "5" && ($$SB[0] eq "サザンクロス" || $$SC[0] eq "サザンクロス" || $$SD[0] eq "サザンクロス")){$SetPointA = $SetPointA + 50;}
			if($$SA[0] eq "オラシオン" && $_[5] ne "5" && ($$SB[0] eq "フロイデヘルム" || $$SC[0] eq "フロイデヘルム" || $$SD[0] eq "フロイデヘルム")){$SetPointA = $SetPointA + 50;}

			#オウガセット
			$SetPointB = 0;
			if($$SA[0] eq "オウガブレード" && $_[5] ne "4" && ($$SB[0] eq "オウガシールド" || $$SC[0] eq "オウガシールド" || $$SD[0] eq "オウガシールド")){$SetPointB = $SetPointB + 50;}
			if($$SA[0] eq "オウガブレード" && $_[5] ne "4" && ($$SB[0] eq "オウガアーマー" || $$SC[0] eq "オウガアーマー" || $$SD[0] eq "オウガアーマー")){$SetPointB = $SetPointB + 50;}
			if($$SA[0] eq "オウガブレード" && $_[5] ne "4" && ($$SB[0] eq "オウガヘルム" || $$SC[0] eq "オウガヘルム" || $$SD[0] eq "オウガヘルム")){$SetPointB = $SetPointB + 50;}

			#暗黒魔道器セット
			$SetPointC = 0;
			if($$SA[0] eq "ダグザハンマー" && $_[5] ne "4" && ($$SB[0] eq "死霊の指輪" || $$SC[0] eq "死霊の指輪" || $$SD[0] eq "死霊の指輪")){$SetPointC = $SetPointC + 50;}
			if($$SA[0] eq "ダグザハンマー" && $_[5] ne "4" && ($$SB[0] eq "死神の甲冑" || $$SC[0] eq "死神の甲冑" || $$SD[0] eq "死神の甲冑")){$SetPointC = $SetPointC + 50;}
			if($$SA[0] eq "ダグザハンマー" && $_[5] ne "4" && ($$SB[0] eq "スカルマスク" || $$SC[0] eq "スカルマスク" || $$SD[0] eq "スカルマスク")){$SetPointC = $SetPointC + 50;}

			#狩人セット
			$SetPointD = 0;
			if($$SA[0] eq "シャーウッド" && ($$SB[0] eq "フォレストブーツ" || $$SC[0] eq "フォレストブーツ" || $$SD[0] eq "フォレストブーツ")){$SetPointD = $SetPointD + 50;}
			if($$SA[0] eq "シャーウッド" && ($$SB[0] eq "グリンサーコート" || $$SC[0] eq "グリンサーコート" || $$SD[0] eq "グリンサーコート")){$SetPointD = $SetPointD + 50;}
			if($$SA[0] eq "シャーウッド" && ($$SB[0] eq "ウッドブランチ" || $$SC[0] eq "ウッドブランチ" || $$SD[0] eq "ウッドブランチ")){$SetPointD = $SetPointD + 50;}

			#にぎりセット
			$SetPointE = 0;
			if($$SA[0] eq "にぎりがくさい剣" && ($$SB[0] eq "むずがゆい小手" || $$SC[0] eq "むずがゆい小手" || $$SD[0] eq "むずがゆい小手")){$SetPointE = $SetPointE + 50;}
			if($$SA[0] eq "にぎりがくさい剣" && ($$SB[0] eq "汗くさい甲冑" || $$SC[0] eq "汗くさい甲冑" || $$SD[0] eq "汗くさい甲冑")){$SetPointE = $SetPointE + 50;}
			if($$SA[0] eq "にぎりがくさい剣" && ($$SB[0] eq "ヌメヌメする兜" || $$SC[0] eq "ヌメヌメする兜" || $$SD[0] eq "ヌメヌメする兜")){$SetPointE = $SetPointE + 50;}

			if($SetPointA >= 50){$$SA[1]+=5500;$$SA[2]-=2;$$SA[4]+=110;}#超神聖 Lv1
			if($SetPointA >= 100){$$SA[2]+=22;$$SA[4]-=70;}#超神聖 Lv2
			if($SetPointA >= 150){$$SA[1]+=4000;$$SA[4]-=70;}#超神聖 Lv3

			if($SetPointB >= 50){$$SA[2]+=48;$$SA[4]+=80;}#鬼セLv1
			if($SetPointB >= 100){$$SA[1]+=3000;$$SA[4]-=40;}#鬼セLv2
			if($SetPointB >= 150){$$SA[1]+=5000;$$SA[4]-=80;}#鬼セLv3

#			#鬼セ
#			if($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && (($$SB[1] <= 40 && $$SB[7]=~ m/!51/ && $$SC[7] !~ m/!12/ && $$SD[7] !~ m/!12/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!51/ && $$SD[7] !~ m/!12/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!51/))){$$SA[2]+=48;$$SA[4]+=80;}
#			#鬼セ：既存+兜/鎧
#			if($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SB[0] eq "オウガシールド" && (($$SC[0] eq "オウガアーマー" || $$SC[0] eq "オウガヘルム") || ($$SD[0] eq "オウガアーマー" || $$SD[0] eq "オウガヘルム"))){$$SA[1]+=3000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SC[0] eq "オウガシールド" && (($$SB[0] eq "オウガアーマー" || $$SB[0] eq "オウガヘルム") || ($$SD[0] eq "オウガアーマー" || $$SD[0] eq "オウガヘルム"))){$$SA[1]+=3000;$$SA[4]-=40;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SD[0] eq "オウガシールド" && (($$SC[0] eq "オウガアーマー" || $$SC[0] eq "オウガヘルム") || ($$SB[0] eq "オウガアーマー" || $$SB[0] eq "オウガヘルム"))){$$SA[1]+=3000;$$SA[4]-=40;}
#			#鬼セ：フルコンプ
#			if($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SB[0] eq "オウガシールド" && $$SC[0] eq "オウガアーマー" && $$SD[0] eq "オウガヘルム"){$$SA[1]+=3000;$$SA[4]-=80;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SB[0] eq "オウガシールド" && $$SD[0] eq "オウガアーマー" && $$SC[0] eq "オウガヘルム"){$$SA[1]+=3000;$$SA[4]-=80;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SC[0] eq "オウガシールド" && $$SB[0] eq "オウガアーマー" && $$SD[0] eq "オウガヘルム"){$$SA[1]+=3000;$$SA[4]-=80;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SC[0] eq "オウガシールド" && $$SD[0] eq "オウガアーマー" && $$SB[0] eq "オウガヘルム"){$$SA[1]+=3000;$$SA[4]-=80;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SD[0] eq "オウガシールド" && $$SB[0] eq "オウガアーマー" && $$SC[0] eq "オウガヘルム"){$$SA[1]+=3000;$$SA[4]-=80;}
#			elsif($$SA[7]=~ m/!51/ && $$SA[0] eq "オウガブレード" && $$SD[0] eq "オウガシールド" && $$SC[0] eq "オウガアーマー" && $$SB[0] eq "オウガヘルム"){$$SA[1]+=3000;$$SA[4]-=80;}

#			#魔導器
#			if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && (($$SB[1] <= 20 && $$SB[7]=~ m/!52/) || ($$SC[1] <= 20 && $$SC[7]=~ m/!52/) || ($$SD[1] <= 20 && $$SD[7]=~ m/!52/))){$$SA[2]+=25;$$SA[4]+=120;$$SO+=18;}
#			#魔導器：既存+兜/鎧
#			if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && (($$SC[0] eq "死神の甲冑" || $$SC[0] eq "スカルマスク") || ($$SD[0] eq "死神の甲冑" || $$SD[0] eq "スカルマスク"))){$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && (($$SB[0] eq "死神の甲冑" || $$SB[0] eq "スカルマスク") || ($$SD[0] eq "死神の甲冑" || $$SD[0] eq "スカルマスク"))){$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && (($$SC[0] eq "死神の甲冑" || $$SC[0] eq "スカルマスク") || ($$SB[0] eq "死神の甲冑" || $$SB[0] eq "スカルマスク"))){$$SA[4]-=40;$$SO+=4;}
#			#魔導器：フルコンプ
#			if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && $$SC[0] eq "死神の甲冑" && $$SD[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && $$SD[0] eq "死神の甲冑" && $$SC[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && $$SB[0] eq "死神の甲冑" && $$SD[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && $$SD[0] eq "死神の甲冑" && $$SB[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && $$SB[0] eq "死神の甲冑" && $$SC[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;}
#			elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && $$SC[0] eq "死神の甲冑" && $$SB[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;}
			
			$PL_DEFP = 0;$VS_DEFP = 0;
			if($_[1] eq 'PL'){

				$Pl_maba = 0;
				if($SetPointC >= 50){$$SA[2]+=25;$$SA[4]+=120;$PL_DEFP+=20;}#魔導器Lv1
				if($SetPointC >= 100){$$SA[4]-=40;$$SO+=4;$PL_DEFP+=7;}#魔導器Lv2
				if($SetPointC >= 150){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;$PL_DEFP+=8;$Pl_maba = 1;}#魔導器Lv3

#				#魔導器
#				if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && (($$SB[1] <= 40 && $$SB[7]=~ m/!52/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!52/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!52/))){$$SA[2]+=25;$$SA[4]+=120;$PL_DEFP+=20;}
#				#魔導器：既存+兜/鎧
#				if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && (($$SC[0] eq "死神の甲冑" || $$SC[0] eq "スカルマスク") || ($$SD[0] eq "死神の甲冑" || $$SD[0] eq "スカルマスク"))){$$SA[4]-=40;$PL_DEFP+=7;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && (($$SB[0] eq "死神の甲冑" || $$SB[0] eq "スカルマスク") || ($$SD[0] eq "死神の甲冑" || $$SD[0] eq "スカルマスク"))){$$SA[4]-=40;$PL_DEFP+=7;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && (($$SC[0] eq "死神の甲冑" || $$SC[0] eq "スカルマスク") || ($$SB[0] eq "死神の甲冑" || $$SB[0] eq "スカルマスク"))){$$SA[4]-=40;$PL_DEFP+=7;}
#				#魔導器：フルコンプ
#				if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && $$SC[0] eq "死神の甲冑" && $$SD[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$PL_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && $$SD[0] eq "死神の甲冑" && $$SC[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$PL_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && $$SB[0] eq "死神の甲冑" && $$SD[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$PL_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && $$SD[0] eq "死神の甲冑" && $$SB[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$PL_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && $$SB[0] eq "死神の甲冑" && $$SC[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$PL_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && $$SC[0] eq "死神の甲冑" && $$SB[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$PL_DEFP+=8;}
			}elsif($_[1] eq 'VS'){

				$Vs_maba = 0;
				if($SetPointC >= 50){$$SA[2]+=25;$$SA[4]+=120;$VS_DEFP+=20;}#魔導器Lv1
				if($SetPointC >= 100){$$SA[4]-=40;$$SO+=4;$VS_DEFP+=7;}#魔導器Lv2
				if($SetPointC >= 150){$$SA[2]+=8;$$SA[4]-=40;$$SO+=4;$VS_DEFP+=8;$Vs_maba = 1;}#魔導器Lv3

#				#魔導器
#				if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && (($$SB[1] <= 40 && $$SB[7]=~ m/!52/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!52/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!52/))){$$SA[2]+=25;$$SA[4]+=120;$VS_DEFP+=20;}
#				#魔導器：既存+兜/鎧
#				if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && (($$SC[0] eq "死神の甲冑" || $$SC[0] eq "スカルマスク") || ($$SD[0] eq "死神の甲冑" || $$SD[0] eq "スカルマスク"))){$$SA[4]-=40;$VS_DEFP+=7;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && (($$SB[0] eq "死神の甲冑" || $$SB[0] eq "スカルマスク") || ($$SD[0] eq "死神の甲冑" || $$SD[0] eq "スカルマスク"))){$$SA[4]-=40;$VS_DEFP+=7;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && (($$SC[0] eq "死神の甲冑" || $$SC[0] eq "スカルマスク") || ($$SB[0] eq "死神の甲冑" || $$SB[0] eq "スカルマスク"))){$$SA[4]-=40;$VS_DEFP+=7;}
#				#魔導器：フルコンプ
#				if($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && $$SC[0] eq "死神の甲冑" && $$SD[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$VS_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SB[0] eq "死霊の指輪" && $$SD[0] eq "死神の甲冑" && $$SC[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$VS_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && $$SB[0] eq "死神の甲冑" && $$SD[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$VS_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SC[0] eq "死霊の指輪" && $$SD[0] eq "死神の甲冑" && $$SB[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$VS_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && $$SB[0] eq "死神の甲冑" && $$SC[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$VS_DEFP+=8;}
#				elsif($$SA[7]=~ m/!52/ && $$SA[0] eq "ダグザハンマー" && $$SD[0] eq "死霊の指輪" && $$SC[0] eq "死神の甲冑" && $$SB[0] eq "スカルマスク"){$$SA[2]+=8;$$SA[4]-=40;$VS_DEFP+=8;}

			}



			if($SetPointD >= 50){$$SA[1]-=1200;$$SA[3]+=6;}#狩人Lv1
			if($SetPointD >= 100){$$SA[1]+=100;$$SA[4]-=20;}#狩人Lv2
			if($SetPointD >= 150){$$SA[1]+=100;$$SA[2]+=10;$$SA[4]-=40;}#狩人Lv3

#			#狩人
#			if($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && (($$SB[1] <= 40 && $$SB[7]=~ m/!53/ && $$SC[7] !~ m/!16/ && $$SD[7] !~ m/!16/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!53/ && $$SD[7] !~ m/!16/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!53/))){$$SA[1]-=1200;$$SA[3]+=6;}
#			#狩人：既存+兜/鎧
#			if($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SB[0] eq "フォレストブーツ" && (($$SC[0] eq "グリンサーコート" || $$SC[0] eq "ウッドブランチ") || ($$SD[0] eq "グリンサーコート" || $$SD[0] eq "ウッドブランチ"))){$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SC[0] eq "フォレストブーツ" && (($$SB[0] eq "グリンサーコート" || $$SB[0] eq "ウッドブランチ") || ($$SD[0] eq "グリンサーコート" || $$SD[0] eq "ウッドブランチ"))){$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SD[0] eq "フォレストブーツ" && (($$SC[0] eq "グリンサーコート" || $$SC[0] eq "ウッドブランチ") || ($$SB[0] eq "グリンサーコート" || $$SB[0] eq "ウッドブランチ"))){$$SA[4]-=20;}
#			#狩人：フルコンプ
#			if($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SB[0] eq "フォレストブーツ" && $$SC[0] eq "グリンサーコート" && $$SD[0] eq "ウッドブランチ"){$$SA[2]+=20;$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SB[0] eq "フォレストブーツ" && $$SD[0] eq "グリンサーコート" && $$SC[0] eq "ウッドブランチ"){$$SA[2]+=20;$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SC[0] eq "フォレストブーツ" && $$SB[0] eq "グリンサーコート" && $$SD[0] eq "ウッドブランチ"){$$SA[2]+=20;$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SC[0] eq "フォレストブーツ" && $$SD[0] eq "グリンサーコート" && $$SB[0] eq "ウッドブランチ"){$$SA[2]+=20;$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SD[0] eq "フォレストブーツ" && $$SB[0] eq "グリンサーコート" && $$SC[0] eq "ウッドブランチ"){$$SA[2]+=20;$$SA[4]-=20;}
#			elsif($$SA[7]=~ m/!53/ && $$SA[0] eq "シャーウッド" && $$SD[0] eq "フォレストブーツ" && $$SC[0] eq "グリンサーコート" && $$SB[0] eq "ウッドブランチ"){$$SA[2]+=20;$$SA[4]-=20;}

			#にぎり
			if($SetPointE >= 50){$$SA[1]*=70;$$SA[2]*=2;$$SA[3]-=9;$$SA[4]*=6;}#握りセットLv1
			if($SetPointE >= 100){$$SA[4]=int($$SA[4]*0.8);}#握りセットLv2
			if($SetPointE >= 150){$$SA[4]=int($$SA[4]*0.5);}#握りセットLv3

#			#にぎりッセ
#			if($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && (($$SB[1] <= 40 && $$SB[7]=~ m/!54/ && $$SC[7] !~ m/!12/ && $$SD[7] !~ m/!12/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!54/ && $$SD[7] !~ m/!12/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!54/))){$$SA[1]*=70;$$SA[2]*=2;$$SA[3]-=9;$$SA[4]*=6;}
#			#にぎりッセ：既存+兜/鎧
#			if($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SB[0] eq "むずがゆい小手" && (($$SC[0] eq "汗くさい甲冑" || $$SC[0] eq "ヌメヌメする兜") || ($$SD[0] eq "汗くさい甲冑" || $$SD[0] eq "ヌメヌメする兜"))){$$SA[4]=int($$SA[4]*0.8);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SC[0] eq "むずがゆい小手" && (($$SB[0] eq "汗くさい甲冑" || $$SB[0] eq "ヌメヌメする兜") || ($$SD[0] eq "汗くさい甲冑" || $$SD[0] eq "ヌメヌメする兜"))){$$SA[4]=int($$SA[4]*0.8);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SD[0] eq "むずがゆい小手" && (($$SC[0] eq "汗くさい甲冑" || $$SC[0] eq "ヌメヌメする兜") || ($$SB[0] eq "汗くさい甲冑" || $$SB[0] eq "ヌメヌメする兜"))){$$SA[4]=int($$SA[4]*0.8);}
#			#にぎりッセ：フルコンプ
#			if($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SB[0] eq "むずがゆい小手" && $$SC[0] eq "汗くさい甲冑" && $$SD[0] eq "ヌメヌメする兜"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SB[0] eq "むずがゆい小手" && $$SD[0] eq "汗くさい甲冑" && $$SC[0] eq "ヌメヌメする兜"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SC[0] eq "むずがゆい小手" && $$SB[0] eq "汗くさい甲冑" && $$SD[0] eq "ヌメヌメする兜"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SC[0] eq "むずがゆい小手" && $$SD[0] eq "汗くさい甲冑" && $$SB[0] eq "ヌメヌメする兜"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SD[0] eq "むずがゆい小手" && $$SB[0] eq "汗くさい甲冑" && $$SC[0] eq "ヌメヌメする兜"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!54/ && $$SA[0] eq "にぎりがくさい剣" && $$SD[0] eq "むずがゆい小手" && $$SC[0] eq "汗くさい甲冑" && $$SB[0] eq "ヌメヌメする兜"){$$SA[4]=int($$SA[4]*0.5);}

			#お菓子		Lv1：HP回復10％　MP回復3％　Lv2：HP回復20％　MP回復6％　Lv3：HP回復30％　MP回復10％
#			if($$SA[7]=~ m/!55/ && (($$SB[1] <= 20 && $$SB[7]=~ m/!55/ && $$SC[7] !~ m/!12/ && $$SD[7] !~ m/!12/) || ($$SC[1] <= 20 && $$SC[7]=~ m/!55/ && $$SD[7] !~ m/!12/) || ($$SD[1] <= 20 && $$SD[7]=~ m/!55/))){$$SA[1]*=4;$$SA[4]*=5;}
			#お菓子：既存+兜/鎧
#			if($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SB[0] eq "チョコレートの盾" && (($$SC[0] eq "砂糖菓子のヨロイ" || $$SC[0] eq "キャンディヘルム") || ($$SD[0] eq "砂糖菓子のヨロイ" || $$SD[0] eq "キャンディヘルム"))){$$SA[4]=int($$SA[4]*0.8);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SC[0] eq "チョコレートの盾" && (($$SB[0] eq "砂糖菓子のヨロイ" || $$SB[0] eq "キャンディヘルム") || ($$SD[0] eq "砂糖菓子のヨロイ" || $$SD[0] eq "キャンディヘルム"))){$$SA[4]=int($$SA[4]*0.8);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SD[0] eq "チョコレートの盾" && (($$SC[0] eq "砂糖菓子のヨロイ" || $$SC[0] eq "キャンディヘルム") || ($$SB[0] eq "砂糖菓子のヨロイ" || $$SB[0] eq "キャンディヘルム"))){$$SA[4]=int($$SA[4]*0.8);}
			#お菓子：フルコンプ
#			if($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SB[0] eq "チョコレートの盾" && $$SC[0] eq "砂糖菓子のヨロイ" && $$SD[0] eq "キャンディヘルム"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SB[0] eq "チョコレートの盾" && $$SD[0] eq "砂糖菓子のヨロイ" && $$SC[0] eq "キャンディヘルム"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SC[0] eq "チョコレートの盾" && $$SB[0] eq "砂糖菓子のヨロイ" && $$SD[0] eq "キャンディヘルム"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SC[0] eq "チョコレートの盾" && $$SD[0] eq "砂糖菓子のヨロイ" && $$SB[0] eq "キャンディヘルム"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SD[0] eq "チョコレートの盾" && $$SB[0] eq "砂糖菓子のヨロイ" && $$SC[0] eq "キャンディヘルム"){$$SA[4]=int($$SA[4]*0.5);}
#			elsif($$SA[7]=~ m/!55/ && $$SA[0] eq "シュガーケーン" && $$SD[0] eq "チョコレートの盾" && $$SC[0] eq "砂糖菓子のヨロイ" && $$SB[0] eq "キャンディヘルム"){$$SA[4]=int($$SA[4]*0.5);}

			#愛
			if($$SA[7]=~ m/!57/ && (($$SB[1] <= 40 && $$SB[7]=~ m/!58/ && $$SC[7] !~ m/!16/ && $$SD[7] !~ m/!16/) || ($$SC[1] <= 40 && $$SC[7]=~ m/!58/ && $$SD[7] !~ m/!16/) || ($$SD[1] <= 40 && $$SD[7]=~ m/!58/))){$$SA[1]+=6000;$$SA[2]-=20;$$SA[4]+=100;}
		}

#		if($$SA[7] =~ m/!61|!62|!63/){
		if($$SF[7] =~ m/!61|!62|!63/){
			@array1=(ubaa,ubab,ubac,ubad,ubae,ubaf) if $$SF[7] =~ m/!61/;
			@array1=(ubag,ubah,ubai,ubaj,ubak,ubal) if $$SF[7] =~ m/!62/;
			@array1=(ubao,ubap,ubaq,ubar,ubas,ubat) if $$SF[7] =~ m/!63/;
			@$SF=split(/\,/,$WEAPON_LIST{"$array1[$$PA[31]]"});
		}
#		if($$SA[7] =~ m/!6o/){
		if($$SF[7] =~ m/!6o/){
#			unless((($$SA[7] =~ m/!6j|!6k/ && $$PS[17]=~ m/!p/) || ($$PS[17]=~ m/!q/ && $$SA[7] =~ m/!6l/)) && $CL_VALUES[7] > time && $FORM{'b_mode'} eq '回復'){
			unless((($$SF[7] =~ m/!6j|!6k|!76/ && $$PS[17]=~ m/!p/) || ($$PS[17]=~ m/!q/ && $$SF[7] =~ m/!6l/)) && $FORM{'b_mode'} eq '回復'){
				@$SF=split(/\,/,$WEAPON_LIST{"p"});
			}
		}


		if($$PS[17]){
			if($$SA[0] eq 'リムファイアー' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ubbd"});}
			if($$SA[0] eq 'カマンダスガン' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ubbe"});}
			if($$SA[0] eq 'アッサルト' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ubbf"});}
			if($$SA[0] eq 'マスケットガン' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ub0200a"});}
			if($$SA[0] eq 'ペトロネル' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ub0201a"});}
			if($$SA[0] eq 'バンドゥイチャクマ' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ub0202a"});}
			if($$SA[0] eq 'デリンジャー' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ub0203a"});}
			if($$SA[0] eq 'アサルトライフル' && $$PS[17]=~ m/!3/){@$SA=split(/\,/,$WEAPON_LIST{"ub0204a"});}
			if($$SA[0] eq 'アンビシオン' && $$PS[17]=~ m/!W103/){@$SA=split(/\,/,$WEAPON_LIST{"ub1haba"});}

#		#ディアナで弓以外を使用した場合は性能低下
#		&ERROR("$Pl_AOnly");
#		if($$SA[7] !~ m/!1a/ && $$PS[17]=~ m/!E005/){$$SF[1]=int($$SA[1]*0.7);$$SA[2]-=20;$$SA[4]+=40;if($$SA[4] > 4000){$$SA[4]=4000;}}
#		elsif($$SA[7] =~ m/!1a/ && $$PS[17]=~ m/!E005/ && $_[1] eq 'PL' && $Pl_AOnly ne '1'){$$SF[1]=int($$SA[1]*0.7);$$SA[2]-=20;$$SA[4]+=40;if($$SA[4] > 4000){$$SA[4]=4000;}}
#		elsif($$SA[7] =~ m/!1a/ && $$PS[17]=~ m/!E005/ && $_[1] eq 'VS' && $Vs_AOnly ne '1'){$$SF[1]=int($$SA[1]*0.7);$$SA[2]-=20;$$SA[4]+=40;if($$SA[4] > 4000){$$SA[4]=4000;}}
#&ERROR("$$SA[7]ああ$$PS[17]");


#&ERROR("$$SF[0]");
#			if($$SA[0] eq 'ジハド' && $$PS[17]=~ m/!7/){$$SA[1]+=10200;$$SA[4]+=110;}#ジハド
			if($$SF[0] eq 'ジハド' && $$PS[17]=~ m/!7/){$$SF[1]+=10200;$$SF[4]+=110;}#ジハド
#			if($$SA[0] eq 'サッドソ\ング' && $$PS[17]=~ m/!m/){$$SA[1]+=1600;$$SA[2]+=20;$$SA[3]-=2;}#サッドソング
			if($$SF[0] eq 'サッドソ\ング' && $$PS[17]=~ m/!m/){$$SF[1]+=1600;$$SF[2]+=20;$$SF[3]-=2;}#サッドソング
#			if($$SA[0] eq 'サイレントソ\ング' && $$PS[17]=~ m/!n/){$$SA[1]+=2400;$$SA[2]+=10;}#サイレントソング
			if($$SF[0] eq 'サイレントソ\ング' && $$PS[17]=~ m/!n/){$$SF[1]+=2400;$$SF[2]+=10;}#サイレントソング
#			if($$SA[0] eq 'バニッシュ' && $$PS[17]=~ m/!l/){$$SA[1]+=11800;$$SA[2]+=20;$$SA[4]+=105;}#バニッシュ
			if($$SF[0] eq 'バニッシュ' && $$PS[17]=~ m/!l/){$$SF[1]+=11800;$$SF[2]+=20;$$SF[4]+=105;}#バニッシュ
#			if($$SA[0] eq 'マジックボム' && $$PS[17]=~ m/!8/){$$SA[2]+=50;}#フェアリー
			if($$SF[0] eq 'マジックボム' && $$PS[17]=~ m/!8/){$$SF[2]+=50;}#フェアリー
#			if($$SA[0] eq 'ジェミニアタック' && $$PS[17]=~ m/!6/){$$SA[2]+=50;}#ジェミニ
			if($$SF[0] eq 'ジェミニアタック' && $$PS[17]=~ m/!6/){$$SF[2]+=50;}#ジェミニ
#			if($$SA[0] eq 'ギガントブロウ' && $$PS[17]=~ m/!9/){$$SA[1]+=6000;$$SA[2]-=30;}#ジャイアント
			if($$SF[0] eq 'ギガントブロウ' && $$PS[17]=~ m/!9/){$$SF[1]+=6000;$$SF[2]-=30;}#ジャイアント
#			if($$SA[7] =~ m/!1k/ && $$PS[17]=~ m/!5/){$$SA[2]+=18;$$SO+=20;}#ドラゴンテイミング
			if($$SF[7] =~ m/!1k/ && $$PS[17]=~ m/!5/){$$SF[2]+=18;$$SO+=20;}#ドラゴンテイミング
#			if($$SA[7] =~ m/!1l/ && $$PS[17]=~ m/!4/){$$SA[2]+=25;$$SO+=5;}#ビーストテイミング
			if($$SF[7] =~ m/!1l/ && $$PS[17]=~ m/!4/){$$SF[2]+=25;$$SO+=5;}#ビーストテイミング
#			if($$SA[0] eq 'メテオストライク' && $$PS[17]=~ m/!a/){@$SA=split(/\,/,$WEAPON_LIST{"ubaz"});}#メテオストライク
			if($$SF[0] eq 'メテオストライク' && $$PS[17]=~ m/!a/){@$SF=split(/\,/,$WEAPON_LIST{"ubaz"});}#メテオストライク
#			if($$SA[0] eq 'ダークロア' && $$PS[17]=~ m/!b/){@$SA=split(/\,/,$WEAPON_LIST{"ubbb"});}#ダークロア
			if($$SF[0] eq 'ダークロア' && $$PS[17]=~ m/!b/){@$SF=split(/\,/,$WEAPON_LIST{"ubbb"});}#ダークロア

			if($$SF[0] eq 'ロンギコルニス' && $$PS[17]=~ m/!W104/){@$SF=split(/\,/,$WEAPON_LIST{"ub2de"});}#ダークロア

#			if($$SA[0] eq 'サモンダークネス' && $$PS[17]=~ m/!o/){
#				@$PS=split(/\,/,$VCLASS_LIST{"23"});
#				@$SA=split(/\,/,$WEAPON_LIST{"4hea"});
#				if($$PA[11]){
#					@$SC=split(/\,/,$WEAPON_LIST{"4he"});
#				}
#			}#サモンダークネス
			if($$SF[0] eq 'サモンダークネス' && $$PS[17]=~ m/!o/){
				@$PS=split(/\,/,$VCLASS_LIST{"23"});
				@$SF=split(/\,/,$WEAPON_LIST{"xx4hea"});
				if($$PA[11]){
					@$SC=split(/\,/,$WEAPON_LIST{"4he"});
				}
			}#サモンダークネス
#			if($$SA[0] eq 'スターティアラ' && $$PS[17]=~ m/!c/){@$SA=split(/\,/,$WEAPON_LIST{"ubba"});}#スターティアラ
			if($$SF[0] eq 'スターティアラ' && $$PS[17]=~ m/!c/){@$SF=split(/\,/,$WEAPON_LIST{"ubba"});}#スターティアラ
#			if($$SA[0] eq 'サモンダークネス' && $$PS[17]=~ m/!u/){
			if($$SF[0] eq 'サモンダークネス' && $$PS[17]=~ m/!u/){
				@array1=(20,21,27);#クラス
				@array2=(ba,'q',hab);#武器
				my$check=int(rand(3)); 
				@$PS=split(/\,/,$VCLASS_LIST{"$array1[$check]"});
#				@$SA=split(/\,/,$WEAPON_LIST{"$array2[$check]"});
#				$$SA[1]+=2500;$$SA[2]+=20;
				@$SF=split(/\,/,$WEAPON_LIST{"$array2[$check]"});
				$$SF[1]+=2500;$$SF[2]+=20;
			}#サモンダークネス

		}


	}
}

sub SYUSEI{
	my$AT="$_[2]_AttPoint";my$DE="$_[2]_DefPoint";my$SP="$_[2]_SpPoint";my$WM="$_[2]_MisPoint";

	if($_[0] eq 'v'){
		my$PW="$_[1]_W";my$PWL="$_[1]_GOWLV";my$PA="$_[1]_VALUES";
		my$ME="$_[1]_mei";my$KA="$_[2]_Kaikyu";my$WS="$_[2]wl";
		my$WN="$_[1]_WeaponNameA";my$PX="$_[1]_sS";

		$$WS=int($$PWL/$WEAPON_LVUP);
#$PL_WDuLv $PL_LVSS
		if($_[1] eq 'PL' && $Pl_EEXP ne "0"){my$PWL = $PL_LVSS;$$WS = int($PL_WDuLv/100);}
#		if($_[1] eq 'PL' && $Pl_EEXP eq "1"){my$PWL = $PL_LVSS;$$WS = int($PL_WDuLv/100);}
		if($_[1] eq 'VS' && $Vs_EEXP ne "0"){my$PWL = $VS_LVSS;$$WS = int($VS_WDuLv/100);}

#			$Pl_LvCalc = $PL_WLV;

#			$$AT=int($$PW[1]*($$PWL*0.00003+1));
		if($_[1] eq 'PL'){
			if($Pl_wazat eq "0"){
				$$AT=int($$PW[1]*($$PWL*0.00003+1));
			}else{
				$$AT=int($$PW[1]*($Pl_LvCalc*0.00003+1));
			}
		}elsif($_[1] eq 'VS'){
			if($Vs_wazat eq "0"){
				$$AT=int($$PW[1]*($$PWL*0.00003+1));
			}else{
				$$AT=int($$PW[1]*($Vs_LvCalc*0.00003+1));
			}
		}

		$$DE=$$PA[20]*2;$$SP=50+$$PA[21];
#命中補正下方調整 20100329再調整 20100719元に戻し 20100905再調整
#		$$WM=52+sprintf("%.2f",rand(6))+$$PA[22]+$$ME*2;
#		$$WM=52+sprintf("%.2f",rand(6))+$$PA[22]+int($$ME*1.67);
		$$WM=52+sprintf("%.2f",rand(6))+$$PA[22]+int($$ME*1.8);
		$$KA=&RANK($$PA[0],$$PA[5],$$PA[6]);
#&ERROR("$$PWL");

#$$WN="$$PW[0](Level.$$WS)";
#		&ERROR("$$PX[12]","$$PW[12]");
		if($$PX[0]){
			if($$PX[11] =~ m/1|2|3|4/ && $$PW[7] =~ m/!13|!14|!15|!19/){
				$$WN="$$PW[0](Level.$$WS)";
			}else{
				$$WN="$$PW[0]";
			}

			if($$PX[11] =~ m/5/){
#				$$PW[0].= "a";
				#杖以外の武器で且つ、武器の種類と技の種類が一致する場合に組み合わせる
				if($$PX[12] =~ m/all/){
					$$WN="$$PW[0](Level.$$WS)";
				}elsif($$PX[12] =~ m/two/ && $$PW[7] =~ m/11/){
					$$WN="$$PW[0](Level.$$WS)";
				}elsif($$PX[12] eq $PW[12]){
					$$WN="$$PW[0](Level.$$WS)";
				}elsif($$PX[12] =~ m/e002e003e004e007/ && ($$PW[12] =~ m/e002/ || $$PW[12] =~ m/e003/ || $$PW[12] =~ m/e004/ || $$PW[12] =~ m/e007/)){
##$$PW[0].="bb";
					$$WN="$$PW[0](Level.$$WS)";
				}else{
##$$PW[0].="cc";
					$$WN="$$PW[0]";
				}

			}elsif($$PX[11] =~ m/6|7|8/){

				#Aが指輪・オーブの場合は組み合わせる
				if ($$PW[7] =~ m/!13|!14/){
					$$WN="$$PW[0](Level.$$WS)";
				}else{
					$$WN="$$PW[0]";
				}

			}
		}else{
			$$WN="$$PW[0](Level.$$WS)";
		}

#		if($_[1] eq 'PL' && $PL_HS eq "1"){
#			$$WN="$$PW[0](Level.$$WS)";
#			$$WN.="<br>$PL_H[0]";
#			$PL_HOJONAME="$PL_H[0]";
#		}

	}
##作戦修正
	if($_[0] eq 'm'){
		#$_[4] がクラス値
		$MsnStyle="$_[2]_MsnStyle";my$PW="$_[3]_W";
		if($_[1] == 1){
			$$MsnStyle='通常攻撃';
		}elsif($_[1] == 2){
			$$AT*=1.3;$$DE*=0.7;$$MsnStyle='突撃';
		}elsif($_[1] == 3){
			$$AT*=0.8;$$DE*=2;$$MsnStyle='防御';
		}elsif($_[1] == 4){
			$$MsnStyle='ヒットアンドアウェイ';
		}elsif($_[1] == 5){
			$$MsnStyle='狙撃';$$PW[2]+=20;
		}elsif($_[1] == 6){
			$$AT*=2;$$DE*=0.35;$$PW[2]-=10;$$MsnStyle='捨て身';
		}elsif($_[1] == 7){
			$$AT*=0.9;$$SP*=1.13;$$PW[2]+=10;$$MsnStyle='見切り';
		}elsif($_[1] == 8){
			$$PW[3]*=2;$$PW[4]*=2;$$MsnStyle='ダブルアタック';
			
			if($AbiSys == 1 && $AbiMukou == 0){
				#片手修練
				if($_[3] eq 'PL'){
					if($ABI_sA[2] =~ m/!A0020/ || $ABI_sB[2] =~ m/!A0020/ || $ABI_sC[2] =~ m/!A0020/){$$PW[4]=int($$PW[4]/2*1.5);}
				}else{
					if($VABI_sA[2] =~ m/!A0020/ || $VABI_sB[2] =~ m/!A0020/ || $VABI_sC[2] =~ m/!A0020/){$$PW[4]=int($$PW[4]/2*1.5);}
				}
			}
			
		}elsif($_[1] == 9 && $_[4] == 80){
			#速攻　回+4に相当 威力1.3倍　消費MP1.5倍
			$$AT*=1.3;$$SP*=1.2;$$PW[4]=int($$PW[4]*1.5);$$MsnStyle='速攻';
#		}elsif($_[1] == 9 && ($_[4] == 50 || $_[4] == 51 || $_[4] == 216)){
		}elsif(($_[1] == 10 && $_[4] == 50) || ($_[1] == 11 && $_[4] == 51) || ($_[1] == 12 && $_[4] == 216)){
			#大防御　防*2.5　威力低下なし　消費MP1.2倍
			$$DE*=2.5;$$PW[4]=int($$PW[4]*1.2);$$MsnStyle='大防御';
		}else{
			$$MsnStyle='通常攻撃';
		}
	}
##クラス修正
	if($_[0] eq 's'){
		my$PS="$_[1]_CLASS";my$PW="$_[1]_W";my$PA="$_[1]_VALUES";
		#攻補正加算　魔法時
#		$$PS[1]+=4 if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!1|!E007|!E008/;
		$$PS[1]+=2 if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!E007/;
		$$PS[1]+=3 if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!1|!E008/;
		$$PS[1]+=2 if $$PW[7] =~ m/!00/ && $$PA[31]==0 || $$PW[7] =~ m/!01/ && $$PA[31]==1 || $$PW[7] =~ m/!02/ && $$PA[31]==2 || $$PW[7] =~ m/!03/ && $$PA[31]==3 || $$PW[7] =~ m/!04/ && $$PA[31]==4 || $$PW[7] =~ m/!05/ && $$PA[31]==5;
		$$AT*=0.9+$$PS[1]/20;
		$$DE*=1+$$PS[2]/10;
#		$$SP*=1+$$PS[3]/20; #20090523 修正by304
		$$SP*=1+$$PS[3]/15;
#		$$WM+=$$PS[4]*2;
		if($$PS[4]>0){
			$$WM+=$$PS[4]*3;
		}else{
			$$WM+=$$PS[4]*2;
		}
	}
	if($_[0] eq 'est'){
		my$PW="$_[1]_W";my$PBW="$_[1]_sB";my$PCW="$_[1]_sC";my$PDW="$_[1]_sD";my$PSW="$_[1]_sS";
		my$VW="$_[3]_W";my$VBW="$_[3]_sB";my$VCW="$_[3]_sC";my$VDW="$_[3]_sD";my$VSW="$_[3]_sS";
		my$PA="$_[1]_VALUES";my$PB="$_[3]_VALUES";
		my$AG="$_[1]FP";my$WS="$_[1]CSS";
		my$BAG="$_[1]_agD";my$PS="$_[1]_CLASS";
	##防具STR修正
#by304 20090525	20091206基に戻す
		$$AT*=(1+$$BAG/100);
#		if ($_[1] eq "PL" && $$PW[7] =~ m/!18/){$$AT*=(1+$$BAG/100);}
#		elsif ($_[1] eq "PL" && $$PW[7] !~ m/!18/ && $Pl_WOnly eq "1"){$$AT*=(1+$$BAG/70);}
#		elsif ($_[1] eq "PL" && $$PW[7] !~ m/!18/){$$AT*=(1+$$BAG/100);}
#		elsif ($_[1] eq "VS" && $$PW[7] =~ m/!18/){$$AT*=(1+$$BAG/100);}
#		elsif ($_[1] eq "VS" && $$PW[7] !~ m/!18/ && $Vs_WOnly eq "1"){$$AT*=(1+$$BAG/70);}
#		elsif ($_[1] eq "VS" && $$PW[7] !~ m/!18/){$$AT*=(1+$$BAG/100);}

	#ダグザ不具合修正
#		$aaa = $$WS;
		if($_[1] eq "PL"){$$WS+=$PL_DEFP;}
		if($_[1] eq "VS"){$$WS+=$VS_DEFP;}
#		&ERROR("$aaaあああ$$WS");

#	#装備品の防御力に防補正の影響を適用する" #20101124撤廃
#	if($_[1] eq "PL"){
#		if($PL_CLASS[2]>0){$PL_DMGRED = 1 + int($PL_CLASS[2]/2-0.5)/10;}else{$PL_DMGRED=1;}
#		$$WS = $$WS * $PL_DMGRED;
#	}
#	if($_[1] eq "VS"){
#		if($VS_CLASS[2]>0){$VS_DMGRED = 1 + int($VS_CLASS[2]/2-0.5)/10;}else{$VS_DMGRED=1;}
#		$$WS = $$WS * $VS_DMGRED;
#	}
	
	#エンチャント
	$VITHosei = 0;
	if($_[1] eq "PL"){
		if($PL_WA04 ne "" && $PL_WA04 > 0 && $PL_flgEnt > 0){$VITHosei = $VITHosei + $PL_WA04;}
		if($PL_WB04 ne "" && $PL_WB04 > 0 && $PL_flgEnt2 > 0){$VITHosei = $VITHosei + $PL_WB04;}
		if($PL_WC04 ne "" && $PL_WC04 > 0 && $PL_flgEnt3 > 0){$VITHosei = $VITHosei + $PL_WC04;}
		if($PL_WD04 ne "" && $PL_WD04 > 0 && $PL_flgEnt4 > 0){$VITHosei = $VITHosei + $PL_WD04;}
	}
	if($_[1] eq "VS"){
		if($VS_WA04 ne "" && $VS_WA04 > 0 && $VS_flgEnt > 0){$VITHosei = $VITHosei + $VS_WA04;}
		if($VS_WB04 ne "" && $VS_WB04 > 0 && $VS_flgEnt2 > 0){$VITHosei = $VITHosei + $VS_WB04;}
		if($VS_WC04 ne "" && $VS_WC04 > 0 && $VS_flgEnt3 > 0){$VITHosei = $VITHosei + $VS_WC04;}
		if($VS_WD04 ne "" && $VS_WD04 > 0 && $VS_flgEnt4 > 0){$VITHosei = $VITHosei + $VS_WD04;}
	}

#エンチャントシステム　RESアップ 盾・体防具・頭防具に付与
	$RESHosei = 0;
	if($_[1] eq "PL"){
		if($PL_WA13 ne "" && $PL_WA13 > 0 && $PL_flgEnt > 0){$RESHosei = $RESHosei + $PL_WA13;}
		if($PL_WB13 ne "" && $PL_WB13 > 0 && $PL_flgEnt2 > 0){$RESHosei = $RESHosei + $PL_WB13;}
		if($PL_WC13 ne "" && $PL_WC13 > 0 && $PL_flgEnt3 > 0){$RESHosei = $RESHosei + $PL_WC13;}
		if($PL_WD13 ne "" && $PL_WD13 > 0 && $PL_flgEnt4 > 0){$RESHosei = $RESHosei + $PL_WD13;}
		$$WS+=$RESHosei;
	}
	if($_[1] eq "VS"){
		if($VS_WA13 ne "" && $VS_WA13 > 0 && $VS_flgEnt > 0){$RESHosei = $RESHosei + $VS_WA13;}
		if($VS_WB13 ne "" && $VS_WB13 > 0 && $VS_flgEnt2 > 0){$RESHosei = $RESHosei + $VS_WB13;}
		if($VS_WC13 ne "" && $VS_WC13 > 0 && $VS_flgEnt3 > 0){$RESHosei = $RESHosei + $VS_WC13;}
		if($VS_WD13 ne "" && $VS_WD13 > 0 && $VS_flgEnt4 > 0){$RESHosei = $RESHosei + $VS_WD13;}
		$$WS+=$RESHosei;
	}



	##防具RES修正
#		$$DE+=$$WS*6-int(($$PB[19] + $VITHosei)/5);
		$$DE+=$$WS*6-int(($$PB[19] + $VITHosei)/4);
	##20090711 最大HPによる、防具RES補正の追加　最大HP50000以上で既存補正　最大HPが下がる度に低下
		if ($$PB[16] < 50000){$$DE = int($$DE * (1 - $$PB[16]/100000));}


	##防具AGI修正
		$$SP+=$$AG;
	##避アップ
		$$SP+=3 if $$PW[7] =~ m/!27/;
#	##RESの修正　by 304 1→1.1　20091108
		$$DE=int($$DE*1.1);
	##防御アップ
		$$DE+=10 if $$PW[7] =~ m/!26/;
	##対魔法処理
		$$AT*=0.68 if $$PW[7] =~ m/!18/ && ($$VW[7] =~ m/!6a/ || $$VBW[7] =~ m/!6a/ || $$VCW[7] =~ m/!6a/ || $$VDW[7] =~ m/!6a/);
	##魔法軽減10％
		$$AT*=0.9 if $$PW[7] =~ m/!18/ && ($$VW[7] =~ m/!E0006/ || $$VBW[7] =~ m/!E0006/ || $$VCW[7] =~ m/!E0006/ || $$VDW[7] =~ m/!E0006/);
	##魔法軽減20％
		$$AT*=0.8 if $$PW[7] =~ m/!18/ && ($$VW[7] =~ m/!E0007/ || $$VBW[7] =~ m/!E0007/ || $$VCW[7] =~ m/!E0007/ || $$VDW[7] =~ m/!E0007/);
	}
	if($_[0] eq 'ini'){
		my$PW="$_[1]_W";my$PBW="$_[1]_sB";my$PCW="$_[1]_sC";my$PDW="$_[1]_sD";my$PSW="$_[1]_sS";
		my$MsnStyle="$_[2]_MsnStyle";
		my$PINI="$_[2]_Initiative";
		my$ESI="$_[1]_estini";my$PS="$_[1]_CLASS";
		my$MS="$_[1]_message";
	##Initiativeランダム処理
		$$PINI=$$SP+sprintf("%.2f",rand(5))+$$ESI*2;
		$Vs_Initiative-=4;
	##狙撃で上昇
		$$PINI+=9+sprintf("%.2f",rand(3)) if $$MsnStyle eq '狙撃';
	##ヒットアンドアウェイで上昇
		$$PINI=int($$PINI*1.15+sprintf("%.2f",rand(7))) if $$MsnStyle eq 'ヒットアンドアウェイ';
	##槍・鞭・ドール・スペシャル(1)Initiative
		$$PINI+=1+sprintf("%.2f",rand(2)) if $$PW[7] =~ m/!1e|!1f|!1p|!30/;
	##スペシャル(2)Initiative
		$$PINI+=4+sprintf("%.2f",rand(3)) if $$PW[7] =~ m/!31/;
	##スペシャル(3)Initiative
		$$PINI+=7+sprintf("%.2f",rand(4)) if $$PW[7] =~ m/!32/;
	##弓Initiative&性能変化
		if($$PW[7] =~ m/!1a/ && $$PS[17] =~ m/!2/){
			$$PINI+=43+sprintf("%.2f",rand(7));$$PW[2]+=40;
		}

#アビリティシステム
	if($AbiSys == 1 && $AbiMukou == 0){

		if ($_[1] eq "PL"){

			#先制行動
			if($PL_SENSEI eq "1"){$$PINI+=3;}
			#絶対後攻
			if($PL_KOUKOU eq "1"){$$PINI-=255;}
			#さきがけ
			if($PL_SAKIGAKE eq "1"){$$PINI+=255;}

		}
		if ($_[1] eq "VS"){

			#先制行動
			if($VS_SENSEI eq "1"){$$PINI+=3;}
			#絶対後攻
			if($VS_KOUKOU eq "1"){$$PINI-=255;}
			#さきがけ
			if($VS_SAKIGAKE eq "1"){$$PINI+=255;}

		}

	}

	#クイックムーブ
		#$Pl_QM = 0;#$Vs_QM = 0;
		if(($$PW[7] =~ m/!8o|!x8o/ || $$PSW[7] =~ m/!8o|!x8o/) && $$PS[17] =~ m/!E001/){
			$$PINI+=5;
			if($_[1] eq 'PL'){
				$Pl_QM = 1;$$MS.='1001';
				if($PL_VALUES[31] eq "0"){$$PINI+=7;}
			}
#			elsif($_[1] eq 'VS'){
#				$Vs_QM = 1;
#				if($VS_VALUES[31] eq "0"){$$PINI+=7;}
#			}
		}

	#スロウムーブ
		#$Pl_SM = 0;#$Vs_SM = 0;
		if(($$PW[7] =~ m/!8p|!x8p/ || $$PSW[7] =~ m/!8p|!x8p/) && $$PS[17] =~ m/!E001/){

			$SHa = int($PL_LVH/1000);
			if($_[1] eq 'PL'){
				if($PL_VALUES[31] eq "3"){$SHa+=10;}
			}

			$CLS = 100 - $SHa;
			if($$PS[17] =~ m/!E001/){$CLS-=45;}
			if($$PS[17] =~ m/!E002/){$CLS-=10;}
			if(rand(100) > $CLS){
				$Pl_SM=1;$$MS.='1002';
			}

#			elsif($_[1] eq 'VS'){
#				$Vs_SM = 1;
#				if($VS_VALUES[31] eq "0"){$$PINI+=7;}
#			}
		}
		if($_[1] eq 'VS' && $Pl_SM eq "1"){
			$$PINI-=7;
		}

	##魔法Initiative
#		$$PINI+=13+sprintf("%.2f",rand(4)) if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!1/;
#		$$PINI+=5+sprintf("%.2f",rand(4)) if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!1|!E007|!E008/;
		$$PINI+=3+sprintf("%.2f",rand(4)) if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!E007/;
		$$PINI+=5+sprintf("%.2f",rand(4)) if $$PW[7] =~ m/!18/ && $$PS[17] =~ m/!1|!E008/;
	##召喚・吹き矢Initiative
		$$PINI+=6 if $$PW[7] =~ m/!1h|!1g/;
	##竜言語Initiative
#		$$PINI-=8+sprintf("%.2f",rand(2)) if $$PW[7] =~ m/!1r/;
		$$PINI+=2+sprintf("%.2f",rand(2)) if $$PW[7] =~ m/!1r/;
	##銃Initiative
		$$PINI+=70+sprintf("%.2f",rand(20)) if $$PW[7] =~ m/!1b/ && $$PS[17] =~ m/!3/;
	##盾Initiative低下
#		$$PINI-=2*$$PS[3] if $$PS[3] > 0 && $$PW[7] =~ m/!10/ && ($$PBW[7] =~ m/!12/ || $$PCW[7] =~ m/!12/ || $$PDW[7] =~ m/!12/);
	##鎧Initiative低下
#		$$PINI-=3*$$PS[3] if $$PS[3] > 0 && ($$PBW[7] =~ m/!1s|!1u|!1w/ || $$PCW[7] =~ m/!1s|!1u|!1w/ || $$PDW[7] =~ m/!1s|!1u|!1w/);
	##頭防具Initiative低下
#		$$PINI-=1*$$PS[3] if $$PS[3] > 0 && ($$PBW[7] =~ m/!1t|!1v|!1x|!E0003/ || $$PCW[7] =~ m/!1t|!1v|!1x|!E0003/ || $$PDW[7] =~ m/!1t|!1v|!1x|!E0003/);
	}

	if($_[0] eq 'aria'){
		my$PW="$_[1]_W";my$PBW="$_[1]_sB";my$PCW="$_[1]_sC";my$PDW="$_[1]_sD";my$PSW="$_[1]_sS";
		my$VW="$_[3]_W";my$VBW="$_[3]_sB";my$VCW="$_[3]_sC";my$VDW="$_[3]_sD";my$VSW="$_[3]_sS";
		my$PA="$_[1]_VALUES";my$PB="$_[3]_VALUES";
		my$VAT="$_[4]_AttPoint";my$VDE="$_[4]_DefPoint";
		my$VSP="$_[4]_SpPoint";my$VWM="$_[4]_MisPoint";
		my$MS="$_[1]_message";my$PS="$_[1]_CLASS";my$PC="$_[1]_CRITICAL";
#&ERROR("$_[0]い$$PW[7]あ$$PS[17]");
	##怒りの一撃	100％→60％に変更　20091206
		if(($$PW[7] =~ m/!28/ || $$PSW[7] =~ m/!28/) && int(rand(100)) <= 60 && $$VW[7] !~ m/!42/ && $$VBW[7] !~ m/!42/ && $$VCW[7] !~ m/!42/ && $$VDW[7] !~ m/!42/){
			$$VDE*=0.8;$$MS.='c';
			$R_VALUES[10]++ if $_[1] eq 'PL';
			$R_VALUES[11]++ if $_[1] eq 'VS';
		}
	##エレメントブレイク
		if(($$PW[7] =~ m/!2s/ || $$PSW[7] =~ m/!2s/) && ($$PW[7] =~ m/!00/ && $$PB[31]==2 || $$PW[7] =~ m/!01/ && $$PB[31]==3 || $$PW[7] =~ m/!02/ && $$PB[31]==0 || $$PW[7] =~ m/!03/ && $$PB[31]==1 || $$PW[7] =~ m/!04/ && $$PB[31]==5 || $$PW[7] =~ m/!05/ && $$PB[31]==4)){
			$$VAT*=0.9;$$VDE*=0.85;$$VSP*=0.9;$$VWM*=0.95;$$MS.='r';
			$R_VALUES[157]++ if $_[1] eq 'PL';
			$R_VALUES[158]++ if $_[1] eq 'VS';
		}
	##呪いの一撃
		if(($$PW[7] =~ m/!2a/ || $$PSW[7] =~ m/!2a/) && $$VW[7] !~ m/!44/ && $$VBW[7] !~ m/!44/ && $$VCW[7] !~ m/!44/ && $$VDW[7] !~ m/!44/){
			if(rand(100) > $_[5]){
				$$VAT*=0.9;$$VDE*=0.9;$$VSP*=0.9;$$VWM*=0.9;$$MS.='d';
				$R_VALUES[75]++ if $_[1] eq 'PL';
				$R_VALUES[76]++ if $_[1] eq 'VS';
			}
			$R_VALUES[107]++ if $_[1] eq 'PL';
			$R_VALUES[108]++ if $_[1] eq 'VS';
		}
	##麻痺
		if(($$PW[7] =~ m/!2c/ || $$PSW[7] =~ m/!2c/) && $$VW[7] !~ m/!46|!4a/ && $$VBW[7] !~ m/!46|!4a/ && $$VCW[7] !~ m/!46|!4a/ && $$VDW[7] !~ m/!46|!4a/){
			if(rand(100) > $_[5]){
				$$VSP*=0.7;$$MS.='h';
				$R_VALUES[78]++ if $_[1] eq 'PL';
				$R_VALUES[79]++ if $_[1] eq 'VS';
			}
			$R_VALUES[110]++ if $_[1] eq 'PL';
			$R_VALUES[111]++ if $_[1] eq 'VS';
		}
	##スタンスローター
		if(($$PW[7] =~ m/!8k/ || $$PSW[7] =~ m/!8k/) && $$VW[7] !~ m/!46|!4a/ && $$VBW[7] !~ m/!46|!4a/ && $$VCW[7] !~ m/!46|!4a/ && $$VDW[7] !~ m/!46|!4a/){
			$Hose = int($PL_LVH/1000);
			if($HoEle eq "1"){$Hose+=5;}
			$CL = 100 - $Hose;
			if($$PS[17] =~ m/!E001/){$CL-=25;}
			if($$PS[17] =~ m/!E002/){$CL-=10;}
			if(rand(100) > $CL){
				$$VWM=0;$$MS.='1000';
			}
		}
	##スランバーミスト
		if(($$PW[7] =~ m/!8l/ || $$PSW[7] =~ m/!8l/) && $$VW[7] !~ m/!46|!4a/ && $$VBW[7] !~ m/!46|!4a/ && $$VCW[7] !~ m/!46|!4a/ && $$VDW[7] !~ m/!46|!4a/){
			$Hose = int($PL_LVH/1000);
			if($HoEle eq "1"){$Hose+=5;}
			$CL = 100 - $Hose;
			if($$PS[17] =~ m/!E001/){$CL-=15;}
			if($$PS[17] =~ m/!E002/){$CL-=10;}
			if(rand(100) > $CL){
				$$VWM=0;$$MS.='j';$$DE*=0.7;
			}
		}
	##ディープメドゥ
		if(($$PW[7] =~ m/!8r/ || $$PSW[7] =~ m/!8r/) && $$VW[7] !~ m/!46|!4a/ && $$VBW[7] !~ m/!46|!4a/ && $$VCW[7] !~ m/!46|!4a/ && $$VDW[7] !~ m/!46|!4a/){
			$Hose = int($PL_LVH/1100);
			if($HoEle eq "1"){$Hose+=10;}
			$CL = 100 - $Hose;
			if($$PS[17] =~ m/!E001/){$CL-=25;}
			if($$PS[17] =~ m/!E002/){$CL-=10;}
#			$CL=0;
			if(rand(100) > $CL){

				my $x = 0;
				my $y = $$VW[3] * 0.66;
				$x = 1 if($y > 0 and $y != int($y));
				$y = $y + $x;
				#$$VWM=0;
				$$MS.='t';$$VW[3]=int($y);
			}
		}

	#ここではメッセージ表示のみ取り扱う
	##クイックムーブ
#		if($Pl_QM eq "1"){$$MS.='1001';}

	##スロウムーブ
#		if($Pl_SM eq "1"){$$MS.='1002';}

	##パワーダウンフラグ
	$flg_Pd = 0;$flg_PUD=0;
	if($_[1] eq 'PL' && ($PL_sSS1[7] =~ m/!2q/ || $PL_sSS2[7] =~ m/!2q/ || $PL_sSS3[7] =~ m/!2q/)){$flg_Pd = 1;$flg_PUD=1;}
	if($_[1] eq 'VS' && ($VS_sSS1[7] =~ m/!2q/ || $VS_sSS2[7] =~ m/!2q/ || $VS_sSS3[7] =~ m/!2q/)){$flg_Pd = 1;$flg_PUD=1;}

	##パワーダウン  || $PL_sSS1[7] =~ m/!2q/ || $PL_sSS2[7] =~ m/!2q/ || $PL_sSS3[7] =~ m/!2q/
		if($$PW[7] !~ m/!6h/ && ($$PW[7] =~ m/!2o/ || $$PBW[7] =~ m/!2q/ || $$PCW[7] =~ m/!2q/ || $$PDW[7] =~ m/!2q/ || $$PSW[7] =~ m/!2q/ || $flg_Pd eq "1")){

			if($flg_PUD eq "1"){
				if(rand(100) > $_[5]+15){
					$$VAT*=0.95;$$MS.='i';
					$R_VALUES[88]++ if $_[1] eq 'PL';
					$R_VALUES[89]++ if $_[1] eq 'VS';
				}
				$R_VALUES[118]++ if $_[1] eq 'PL';
				$R_VALUES[119]++ if $_[1] eq 'VS';
			}else{
				if(rand(100) > $_[5]){
					$$VAT*=0.7;$$MS.='i';
					$R_VALUES[88]++ if $_[1] eq 'PL';
					$R_VALUES[89]++ if $_[1] eq 'VS';
				}
				$R_VALUES[118]++ if $_[1] eq 'PL';
				$R_VALUES[119]++ if $_[1] eq 'VS';
			}
		}

	##パワーアップフラグ
	$flg_PU = 0;
	if($_[1] eq 'PL' && ($PL_sSS1[7] =~ m/!2r/ || $PL_sSS2[7] =~ m/!2r/ || $PL_sSS3[7] =~ m/!2r/)){$flg_PU = 1;}
	if($_[1] eq 'VS' && ($VS_sSS1[7] =~ m/!2r/ || $VS_sSS2[7] =~ m/!2r/ || $VS_sSS3[7] =~ m/!2r/)){$flg_PU = 1;}

	##パワーアップ
#		&ERROR("$$PSW[7]");
		if($$PW[7] !~ m/!6h/ && ($$PBW[7] =~ m/!2r/ || $$PCW[7] =~ m/!2r/ || $$PDW[7] =~ m/!2r/ || $$PSW[7] =~ m/!2r/ || $flg_PU eq "1")){
			if($flg_PU eq "1"){
				if(rand(100) > $_[6]+15){
					$$AT*=1.05;$$MS.='s';
					$R_VALUES[21]++ if $_[1] eq 'PL';
					$R_VALUES[22]++ if $_[1] eq 'VS';
				}
				$R_VALUES[23]++ if $_[1] eq 'PL';
				$R_VALUES[24]++ if $_[1] eq 'VS';
			}else{
				if(rand(100) > $_[6]){
					$$AT*=1.3;$$MS.='s';
					$R_VALUES[21]++ if $_[1] eq 'PL';
					$R_VALUES[22]++ if $_[1] eq 'VS';
				}
				$R_VALUES[23]++ if $_[1] eq 'PL';
				$R_VALUES[24]++ if $_[1] eq 'VS';
			}
		}
	##特殊命中
		if($$PW[7] =~ m/!6h/){
			my$MsnStyle="$_[2]_MsnStyle";
			$$AT=0;$$VSP/=4;$$VDE=0;$$PW[2]=0;
			$$PW[3]/=2 if $$MsnStyle eq 'ダブルアタック';
		#ドラッグイーター
			if($$PW[7] =~ m/!65/ || $$PSW[7] =~ m/!65/){
				$$WM=90;$$AT=int($$PB[15]*0.5);
				$R_VALUES[13]++ if $_[1] eq 'PL';
				$R_VALUES[14]++ if $_[1] eq 'VS';
			}
		#パンプキンボム
			if($$PW[7] =~ m/!66/ || $$PSW[7] =~ m/!66/){
				$$WM=1000;$$AT=int($$PA[15]*0.8);$$MS.='q';
				if($$PB[15] < 0){$$PB[15]=0;$$PB[25]=1;}
				$R_VALUES[94]++ if $_[1] eq 'PL';
				$R_VALUES[95]++ if $_[1] eq 'VS';
			}
		#かぼちゃうぉーず
			if($$PW[7] =~ m/!67/ || $$PSW[7] =~ m/!67/){
				$$WM=75;$$AT=int($$PB[15]*0.09);
				$R_VALUES[15]++ if $_[1] eq 'PL';
				$R_VALUES[16]++ if $_[1] eq 'VS';
			}
		#魔法のラッパ
			if($$PW[7] =~ m/!6i/ || $$PSW[7] =~ m/!6i/){
				$$WM=300;$$AT=int($$VW[5]/5*rand(1)*($$PA[16]/200000+0.8));
				$R_VALUES[26]++ if $_[1] eq 'PL';
				$R_VALUES[35]++ if $_[1] eq 'VS';
			}
		#ストライクノヴァ
			if($$PW[7] =~ m/!60/ || $$PSW[7] =~ m/!60/){
				$$WM=36;my$PWL="$_[1]_GOWLV";
				$$AT=$$PB[16] if $_[1] eq 'PL';
				$$AT=30000*(90+rand(20))/100*(1+$$PWL*3/100000) if $_[1] eq 'VS';
			}
		#ワードオブペイン
			if(($$PW[7] =~ m/!69/ || $$PSW[7] =~ m/!69/) && $$PS[17] =~ m/!1|!E007|!E008/){
				$$WM=90;$$AT=int($$PA[16]-$$PA[15]);
				$R_VALUES[17]++ if $_[1] eq 'PL';
				$R_VALUES[18]++ if $_[1] eq 'VS';
			}
		#シャイニング
			if(($$PW[7] =~ m/!64/ || $$PSW[7] =~ m/!64/) && $$PS[17] =~ m/!1|!E007|!E008/){
				$$WM=70;$$AT=int($$PB[15]*0.9);
				$R_VALUES[135]++ if $_[1] eq 'PL';
				$R_VALUES[137]++ if $_[1] eq 'VS';
			}
		}
	##ノックバック
		if(($$PW[7] =~ m/!2g/ || $$PC) && $$VW[3] > 1){
			if(rand(100) > $_[5]){
				$$VW[3]-=1;$$MS.='l';
				$R_VALUES[98]++ if $_[1] eq 'PL';
				$R_VALUES[99]++ if $_[1] eq 'VS';
			}
			$R_VALUES[124]++ if $_[1] eq 'PL';
			$R_VALUES[125]++ if $_[1] eq 'VS';
		}
	##方向転換
		if($$PW[7] =~ m/!2h/ && $$VW[3] > 1){
			if(rand(100) > $_[5]){
				$$VW[3]=int(rand($$VW[3]));
				$$VW[3]=1 if $$VW[3]==0;$$MS.='k';
				$R_VALUES[96]++ if $_[1] eq 'PL';
				$R_VALUES[97]++ if $_[1] eq 'VS';
			}
			$R_VALUES[122]++ if $_[1] eq 'PL';
			$R_VALUES[123]++ if $_[1] eq 'VS';
		}
	}
	if($_[0] eq 'hina'){
		my$PW="$_[1]_W";my$VW="$_[3]_W";my$VBW="$_[3]_sB";my$VCW="$_[3]_sC";my$VDW="$_[3]_sD";
		my$PA="$_[1]_VALUES";my$PB="$_[3]_VALUES";my$PS="$_[1]_CLASS";
		my$MS="$_[1]_message";my$RA1="$_[1]_toku1";my$RA3="$_[1]_toku3";
	##睡眠(Initiative無効処理)
		if(($$PW[7] =~ m/!2d/ || $$PSW[7] =~ m/!2d/) && $$VW[7] !~ m/!47|!4a/ && $$VBW[7] !~ m/!47|!4a/ && $$VCW[7] !~ m/!47|!4a/ && $$VDW[7] !~ m/!47|!4a/){
			if(rand(100) > $_[5] || $$PS[17] =~ m/!r/){
				my$VINI="$_[4]_Initiative";$$VINI=1;$$MS.='j';
				$R_VALUES[82]++ if $_[1] eq 'PL';
				$R_VALUES[83]++ if $_[1] eq 'VS';
			}
			$R_VALUES[112]++ if $_[1] eq 'PL';
			$R_VALUES[113]++ if $_[1] eq 'VS';
		}
	#毒処理プレイヤーサイド
		if(($$PW[7] =~ m/!2b|!8m/ || $$PSW[7] =~ m/!2b|!8m/) && $$VW[7] !~ m/!45|!4a/ && $$VBW[7] !~ m/!45|!4a/ && $$VCW[7] !~ m/!45|!4a/ && $$VDW[7] !~ m/!45|!4a/){
			$$PB[15]-=int($$PB[16]/20);$$MS.='e';
			if($$PB[15]<0){$$PB[15]=0;$$PB[25]=1;}
			$R_VALUES[80]++ if $_[1] eq 'PL';
			$R_VALUES[81]++ if $_[1] eq 'VS';
		}
	#石化処理プレイヤーサイド
		if(($$PW[7] =~ m/!2e/ || $$PSW[7] =~ m/!2e/) && $$VW[7] !~ m/!48|!4a/ && $$VBW[7] !~ m/!48|!4a/ && $$VCW[7] !~ m/!48|!4a/ && $$VDW[7] !~ m/!48|!4a/){
			if(rand(100) > $_[6]){
				my$VC="mei_$_[4]_Check";$$VC=0;$$MS.='f';
				$R_VALUES[84]++ if $_[1] eq 'PL';
				$R_VALUES[85]++ if $_[1] eq 'VS';
			}
			$R_VALUES[114]++ if $_[1] eq 'PL';
			$R_VALUES[115]++ if $_[1] eq 'VS';
		}
	}
}
#合成
sub GOUSEI{
	my$PA="$_[1]_VALUES";
#合成武器LV
	if($_[0] eq 'k'){
		my$PBUKI="$_[1]bukihenka";my$SA="$_[1]_W";
		my$WLV="$_[1]_WLV";my$GLV="$_[1]_GOWLV";
		my$LB="$_[1]_LVB";my$LC="$_[1]_LVC";my$LD="$_[1]_LVD";
		my$SB="$_[1]_sB";my$SC="$_[1]_sC";my$SD="$_[1]_sD";
		$$PBUKI="$$SA[0]";$$GLV=$$WLV;
		if($$SA[7]=~ m/!1c/){
			$$GLV=int(($$WLV+$$LB)/2) if $$SB[7]=~ m/!1c/;
			$$GLV=int(($$WLV+$$LC)/2) if $$SC[7]=~ m/!1c/;
			$$GLV=int(($$WLV+$$LD)/2) if $$SD[7]=~ m/!1c/;
		}
	}
#合成魔法 Copyright ミリ・ルー
	if($_[0] eq 'g'){
		my$PS="$_[1]_CLASS";my$GO="$_[1]_GOFRAG";
		my$SA="$_[1]_W";my$SB="$_[1]_sB";my$SC="$_[1]_sC";my$SD="$_[1]_sD";my$SS="$_[1]_sS";

		my @BOOKS_LIST = ('属性魔導書','風の魔導書','炎の魔導書','大地の魔導書','水の魔導書','暗黒魔導書');
		sub isSynthesize(){
		  my ($weaponA, $weaponB, $weaponC, $weaponD) = @_;
		  if(&is1stSynthe($weaponA)){
		    my @books = ();
		    if(my $ret = &is2ndSynthe($weaponB, $weaponC, $weaponD)){
		      @books = ($weaponA, $ret);
		    }
		    return @books;
		  }else{
		    return undef;
		  }
		}
		sub is1stSynthe(){
		  my ($weaponA) = @_;
		  return &isBook($weaponA);
		}
		sub is2ndSynthe(){
		  my ($weaponB, $weaponC, $weaponD) = @_;
		  if(&isBook($weaponB)){
		    return $weaponB;
		  }elsif(&isBook($weaponC)){
		    return $weaponC;
		  }elsif(&isBook($weaponD)){
		    return $weaponD;
		  }else{
		    return undef;
		  }
		}
		sub isBook(){
		  my ($weapon) = @_;
		  my $book;
		  foreach $book (@BOOKS_LIST){
		    return $book if($book eq $weapon);
		  }
		  return undef;
		}
		my $element = $$PA[31];
		my $weaponA = $$SA[0];
		my $weaponB = $$SB[0];
		my $weaponC = $$SC[0];
		my $weaponD = $$SD[0];
		if(@ret = &isSynthesize($weaponA, $weaponB, $weaponC, $weaponD)){
		sub getSynthesizeName(){
		  my ($book1, $book2, $element) = @_;
		  if($book1 eq '属性魔導書' && $book2 eq '属性魔導書'){
		    if($$PS[17]=~ m/!t/){
			return $synthesizewifiAttributeHash2{$element};}else{
			return $synthesizewifiAttributeHash{$element};}
		  }
		  if($book1 eq '属性魔導書'){
		    if($$PS[17]=~ m/!t/){
			return $synthesizeAttributeHash2{$element}{$book2};}else{
			return $synthesizeAttributeHash{$element}{$book2};}
		  }elsif($book2 eq '属性魔導書'){
		    if($$PS[17]=~ m/!t/){
			return $synthesizeAttributeHash2{$element}{$book1};}else{
			return $synthesizeAttributeHash{$element}{$book1};}
		  }else{
		    if($$PS[17]=~ m/!t/){
			return $synthesizeWithoutAttributeHash2{$book1}{$book2};}else{
			return $synthesizeWithoutAttributeHash{$book1}{$book2};}
		  }
		}
		  $weaponA = &getSynthesizeName($ret[0], $ret[1], $element);
			if($$SA[7]=~ m/!1c/ && !$weaponA eq ''){
				@$SA=split(/\,/,$WEAPON_LIST{"$weaponA"});
			}
		}
		$$GO=1;
	}
##クラス変化
	if($_[0] eq 'c1'){
		$ST="$_[1]_CLASSFRAG";

		if($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i){
#		&ERROR("$$PA[4]あああ$TIME[2]");
			if($$PA[4]==64){$$PA[4]=65;$$ST=1;}
			if($$PA[4]==71){$$PA[4]=210;$$ST=2;}
			if($$PA[4]==72){$$PA[4]=211;$$ST=3;}
		}
		if($$PA[6] == 1 && $$PA[4] =~ /^131$|^132$|^133$|^134$|^135$/i){
			$$PA[4]+=66;$$ST=4;
		}
		if($$PA[4]==203){
			if($$PA[12] > 71){
				$$PA[4]=208;$$ST=9;
			}elsif($$PA[12] < 36){
				$$PA[4]=209;$$ST=9;
			}
		}
	}
##クラス変化終了
	if($_[0] eq 'c2'){
		$ST="$_[1]_CLASSFRAG";
		$$PA[4]=64 if $$ST == 1;
		$$PA[4]=71 if $$ST == 2;
		$$PA[4]=72 if $$ST == 3;
		$$PA[4]-=66 if $$ST == 4;
		$$PA[4]=203 if $$ST == 9;
	}
}
######戦闘時のコメント
sub MESSAGE{
	$PA="$_[1]_VALUES";
	$PB="$_[2]_VALUES";
	$AA="$_[1]_message";$AB="$_[1]_witi";
##ここから
	if($$AA =~ m/a/){$$AB .= "<font color=#ff0080>$$PA[3]が渾身の一撃！$$PB[3]は瀕死状態！！</font><br>\n";}
	if($$AA =~ m/b/){$$AB .= "<font color=#ff0080>$$PA[3]が必殺の一撃！$$PB[3]は戦闘不\能\！！</font><br>\n";}
	if($$AA =~ m/c/){$$AB .= "<font color=#aaaaaa>$$PA[3]が怒りの一撃！$$PB[3]は防御力低下！！</font><br>\n";}
	if($$AA =~ m/d/){$$AB .= "<font color=#8d61af>$$PA[3]が呪いの一撃！$$PB[3]は全能\力低下！！</font><br>\n";}
	if($$AA =~ m/e/){$$AB .= "<font color=#b0d980>$$PB[3]は毒ダメージ！！</font><br>\n";}
	if($$AA =~ m/f/){$$AB .= "<font color=#b0a580>$$PB[3]は石化した！！</font><br>\n";}
	if($$AA =~ m/g/){$$AB .= "<font color=#ff9cb3>$$PB[3]は魅了され自分を攻撃！！</font><br>\n";}
	if($$AA =~ m/h/){$$AB .= "<font color=#efe98a>$$PB[3]は麻痺した！！</font><br>\n";}
	if($$AA =~ m/1000/){$$AB .= "<font color=#ff9cb3>$$PB[3]は麻痺した！！</font><br>\n";}
	if($$AA =~ m/1001/){$$AB .= "<font color=#c6d5f9>$$PA[3]はクイックムーブを発動！$$PA[3]のInitiative上昇！！</font><br>\n";}
	if($$AA =~ m/1002/){$$AB .= "<font color=#b0d980>$$PA[3]はスロウムーブを発動！$$PB[3]のInitiative低下！！</font><br>\n";}
	if($$AA =~ m/i/){$$AB .= "<font color=#efb9f1>$$PB[3]は攻撃力低下！！</font><br>\n";}
	if($$AA =~ m/j/){$$AB .= "<font color=#c6d5f9>$$PB[3]は眠った！！</font><br>\n";}
	if($$AA =~ m/k/){$$AB .= "<font color=#efe98a>$$PB[3]は大回転！！</font><br>\n";}
	if($$AA =~ m/l/){$$AB .= "<font color=#b3b68a>ノックバック！$$PB[3]は怯んだ！！</font><br>\n";}
	if($$AA =~ m/m/){$$AB .= "$$PA[3]「$$PA[7]」<br>\n";}
	if($$AA =~ m/n/){$$AB .= "<font color=#b34f63>$$PB[3]はMP減少！！</font><br>\n";}
	if($$AA =~ m/o/){$$AB .= "<font color=#eeeeee>シャイニング成功！！<br>眩い光が$$PB[3]を包む！！</font><br>\n";}
	if($$AA =~ m/p/){$$AB .= "<font color=#ff4d4d>$$PB[3]は即死！！</font><br>\n";}
	if($$AA =~ m/q/){$$AB .= "<font color=#ff4d4d>$$PA[3]は自爆した！！</font><br>\n";}
	if($$AA =~ m/r/){$$AB .= "エレメントブレイク！$$PB[3]は全能\力低下！！<br>\n";}
	if($$AA =~ m/s/){$$AB .= "<font color=#efb9f1>$$PA[3]は攻撃力上昇！！</font><br>\n";}
	if($$AA =~ m/t/){$$AB .= "<font color=#b0d980>$$PB[3]は攻撃回数が低下！！</font><br>\n";}
	print "$$AB";
}
sub URSULA{
	if($_[0] eq 'ariel'){
		my$PW="$_[1]_W";my$PBW="$_[1]_sB";my$PCW="$_[1]_sC";my$PDW="$_[1]_sD";my$PSW="$_[1]_sS";
		my$VW="$_[3]_W";my$VBW="$_[3]_sB";my$VCW="$_[3]_sC";my$VDW="$_[3]_sD";my$VSW="$_[3]_sS";
		my$PA="$_[1]_VALUES";my$PB="$_[3]_VALUES";
		my$PAT="$_[2]_AtPoint";my$VAT="$_[4]_AtPoint";
		my$MS="$_[1]_message";my$PS="$_[1]_CLASS";
		my$TIME="$_[2]_Times";
	#魅了
		if($$PW[7] =~ m/!2f/ && $$TIME && $$VW[7] !~ m/!49|!4a/ && $$VBW[7] !~ m/!49|!4a/ && $$VCW[7] !~ m/!49|!4a/ && $$VDW[7] !~ m/!49|!4a/){
			if(rand(100) > $_[5]){
				$$PAT+=$$VAT;$$VAT-=$$VAT;$$MS.='g';
				$R_VALUES[86]++ if $_[1] eq 'PL';
				$R_VALUES[87]++ if $_[1] eq 'VS';
			}
			$R_VALUES[116]++ if $_[1] eq 'PL';
			$R_VALUES[117]++ if $_[1] eq 'VS';
		}
	#渾身
		if($$PW[7] =~ m/!20/ && $$TIME && $$PA[15] > $$VAT && int($$PB[15]-$$PAT) > int($$PB[16]*0.1) && $$VW[7] !~ m/!40/ && $$VBW[7] !~ m/!40/ && $$VCW[7] !~ m/!40/ && $$VDW[7] !~ m/!40/){
			if(rand(255) > $_[6]){
				$$PAT=int($$PB[15]-$$PB[16]*0.1);$$MS.='a';
				$R_VALUES[71]++ if $_[1] eq 'PL';
				$R_VALUES[72]++ if $_[1] eq 'VS';
			}
			$R_VALUES[103]++ if $_[1] eq 'PL';
			$R_VALUES[104]++ if $_[1] eq 'VS';
		}
	#必殺
		if($$PW[7] =~ m/!21/ && $$TIME && $$PA[15] > $$VAT && $$PB[15] > $$PAT && int($$PA[15]-$$VAT) <= int($$PA[16]*0.1) && $$VW[7] !~ m/!41/ && $$VBW[7] !~ m/!41/ && $$VCW[7] !~ m/!41/ && $$VDW[7] !~ m/!41/){
			if(rand(255) > $_[7]){
				$$PAT=$$PB[15];$$MS.='b';
				$R_VALUES[73]++ if $_[1] eq 'PL';
				$R_VALUES[74]++ if $_[1] eq 'VS';
			}
			$R_VALUES[105]++ if $_[1] eq 'PL';
			$R_VALUES[106]++ if $_[1] eq 'VS';
		}
	#MP↓処理プレイヤーサイド
		if ($$PW[7] =~ m/!2k/ && $$TIME){
			if(rand(100) > $_[8]){
				$$PB[17]*=0.9;$$MS.='n';
				$R_VALUES[92]++ if $_[1] eq 'PL';
				$R_VALUES[93]++ if $_[1] eq 'VS';
			}
			$R_VALUES[120]++ if $_[1] eq 'PL';
			$R_VALUES[121]++ if $_[1] eq 'VS';
		}
	#説得処理プレイヤーサイド
		if ($$PW[7] =~ m/!6c/ || $$PBW[7] =~ m/!6c/ || $$PCW[7] =~ m/!6c/ || $$PDW[7] =~ m/!6c/){$$MS.='m';$R_VALUES[90]++ if $_[1] eq 'PL';$R_VALUES[91]++ if $_[1] eq 'VS';}
	#シャイニング
		if($$PW[7] =~ m/!64/ && $$PS[17] =~ m/!1|!E007|!E008/ && $$TIME){$$MS.='o';$R_VALUES[134]++ if $_[1] eq 'PL';$R_VALUES[136]++ if $_[1] eq 'VS';}
	#パンプキンボム
		if($$PW[7] =~ m/!66/){$$PA[15]=0;$$PA[25]=1;}
	#かぼちゃうぉーず
		if($PL_W[7] =~ m/!67/ && $$TIME){$$PA[15]-=int($$PA[15]*0.09*$$TIME);}
	}
}
sub CANHEAD{
	my$PA="$_[0]_VALUES";my$CA="$_[2]_VALUES";
	my$JA="$_[2]JIKANSA";my$PC="$_[0]_Country";
	if($$PA[5]){
		$$CA[14]=0 if !$$CA[14];$$CA[13]=0 if !$$CA[13];
		$$JA=$$CA[13];$$JA=15 if $$CA[13]>14;
		if(($$CA[14]+$$JA*60) > time){
			&ERROR('PsrError','宣戦布告時間中です。') if $_[0] eq 'PL' && ($$CA[6] eq "$KOKUSEKI" || $$CA[8] eq "$KOKUSEKI" || $$CA[9] eq "$KOKUSEKI" || $$CA[10] eq "$KOKUSEKI") || $_[0] eq 'VS';
		}
	}
	&REPAIR(\@$PA);
	if (@$CA){$$PC="$$PA[5]";}else{$$PC=$NONE_NATIONALITY;$$CA[0]='#808080';}
}
#経験値
sub EXP{
	my$PA="$_[0]_VALUES";my$IN="$_[0]_In";my$GO="$_[0]_GOFRAG";
	my$PW="$_[0]_W";my$PBW="$_[0]_sB";my$PCW="$_[0]_sC";my$PDW="$_[0]_sD";my$PSW="$_[0]_sS";
	my$BF="$_[0]_BFLAG";my$CF="$_[0]_CFLAG";my$DF="$_[0]_DFLAG";my$SF="$_[0]_SFLAG";
	my$BW="WLDUMMY$_[0]B";my$CW="WLDUMMY$_[0]C";my$DW="WLDUMMY$_[0]D";my$SW="WLDUMMY$_[0]S";
	my$BL="$_[0]_LVB";my$CL="$_[0]_LVC";my$DL="$_[0]_LVD";my$SL="$_[0]_LVS";
	my$WN="$_[0]_WN";my$WB="$_[0]_WB";my$WC="$_[0]_WC";my$WD="$_[0]_WD";my$WS="$_[0]_WS";
	my$WL="WLDUMMY$_[0]";my$WLV="$_[0]_WLV";
	my$HE="$_[0]bukihenka";my$PN="$_[1]name";

#	my$A3="$_[0]_A3";my$A4="$_[0]_A4";my$A5="$_[0]_A5";my$A6="$_[0]_A6";my$A7="$_[0]_A7";my$A8="$_[0]_A8";
#	my$A9="$_[0]_A9";my$A10="$_[0]_A10";my$A11="$_[0]_A11";my$A12="$_[0]_A12";my$A13="$_[0]_A13";my$A14="$_[0]_A14";
#	my$A15="$_[0]_A15";my$A16="$_[0]_A16";my$A17="$_[0]_A17";my$A18="$_[0]_A18";
#	my$B3="$_[0]_B3";my$B4="$_[0]_B4";my$B5="$_[0]_B5";my$B6="$_[0]_B6";my$B7="$_[0]_B7";my$B8="$_[0]_B8";
#	my$B9="$_[0]_B9";my$B10="$_[0]_B10";my$B11="$_[0]_B11";my$B12="$_[0]_B12";my$B13="$_[0]_B13";my$B14="$_[0]_B14";
#	my$B15="$_[0]_B15";my$B16="$_[0]_B16";my$B17="$_[0]_B17";my$B18="$_[0]_B18";
#	my$C3="$_[0]_C3";my$C4="$_[0]_C4";my$C5="$_[0]_C5";my$C6="$_[0]_C6";my$C7="$_[0]_C7";my$C8="$_[0]_C8";
#	my$C9="$_[0]_C9";my$C10="$_[0]_C10";my$C11="$_[0]_C11";my$C12="$_[0]_C12";my$C13="$_[0]_C13";my$C14="$_[0]_C14";
#	my$C15="$_[0]_C15";my$C16="$_[0]_C16";my$C17="$_[0]_C17";my$C18="$_[0]_C18";
#	my$D3="$_[0]_D3";my$D4="$_[0]_D4";my$D5="$_[0]_D5";my$D6="$_[0]_D6";my$D7="$_[0]_D7";my$D8="$_[0]_D8";
#	my$D9="$_[0]_D9";my$D10="$_[0]_D10";my$D11="$_[0]_D11";my$D12="$_[0]_D12";my$D13="$_[0]_D13";my$D14="$_[0]_D14";
#	my$D15="$_[0]_D15";my$D16="$_[0]_D16";my$D17="$_[0]_D17";my$D18="$_[0]_D18";
	
#	my$WFA="$_[0]_WFA";my$WFB="$_[0]_WFB";my$WFC="$_[0]_WFC";my$WFD="$_[0]_WFD";

#&ERROR("$PL_WFAと$$WFA");


#	local($PL_WN,$PL_WLV,$PL_A3,$PL_A4,$PL_A5,$PL_A6,$PL_A7,$PL_A8,$PL_A9,$PL_A10,$PL_A11,$PL_A12,$PL_A13,$PL_A14,$PL_A15,$PL_A16,$PL_A17,$PL_A18,$PL_A18) = split(/!/,$PL_VALUES[9]); 
#	local($PL_WB,$PL_LVB,$PL_B3,$PL_B4,$PL_B5,$PL_B6,$PL_B7,$PL_B8,$PL_B9,$PL_B10,$PL_B11,$PL_B12,$PL_B13,$PL_B14,$PL_B15,$PL_B16,$PL_B17,$PL_B18,$PL_B18) = split(/!/,$PL_VALUES[10]); 
#	local($PL_WC,$PL_LVC,$PL_C3,$PL_C4,$PL_C5,$PL_C6,$PL_C7,$PL_C8,$PL_C9,$PL_C10,$PL_C11,$PL_C12,$PL_C13,$PL_C14,$PL_C15,$PL_C16,$PL_C17,$PL_C18,$PL_C18) = split(/!/,$PL_VALUES[11]); 
#	local($PL_WD,$PL_LVD,$PL_D3,$PL_D4,$PL_D5,$PL_D6,$PL_D7,$PL_D8,$PL_D9,$PL_D10,$PL_D11,$PL_D12,$PL_D13,$PL_D14,$PL_D15,$PL_D16,$PL_D17,$PL_D18,$PL_D18) = split(/!/,$PL_VALUES[38]); 

#	local($VS_WN,$VS_WLV,$VS_A3,$VS_A4,$VS_A5,$VS_A6,$VS_A7,$VS_A8,$VS_A9,$VS_A10,$VS_A11,$VS_A12,$VS_A13,$VS_A14,$VS_A15,$VS_A16,$VS_A17,$VS_A18,$VS_A18) = split(/!/,$VS_VALUES[9]); 
#	local($VS_WB,$VS_LVB,$VS_B3,$VS_B4,$VS_B5,$VS_B6,$VS_B7,$VS_B8,$VS_B9,$VS_B10,$VS_B11,$VS_B12,$VS_B13,$VS_B14,$VS_B15,$VS_B16,$VS_B17,$VS_B18,$VS_B18) = split(/!/,$VS_VALUES[10]); 
#	local($VS_WC,$VS_LVC,$VS_C3,$VS_C4,$VS_C5,$VS_C6,$VS_C7,$VS_C8,$VS_C9,$VS_C10,$VS_C11,$VS_C12,$VS_C13,$VS_C14,$VS_C15,$VS_C16,$VS_C17,$VS_C18,$VS_C18) = split(/!/,$VS_VALUES[11]); 
#	local($VS_WD,$VS_LVD,$VS_D3,$VS_D4,$VS_D5,$VS_D6,$VS_D7,$VS_D8,$VS_D9,$VS_D10,$VS_D11,$VS_D12,$VS_D13,$VS_D14,$VS_D15,$VS_D16,$VS_D17,$VS_D18,$VS_D18) = split(/!/,$VS_VALUES[38]); 

#&ERROR("$FORM{'sentaku'}ああ$Pl_EEXP");

#補助魔法使用時のメッセージ不具合を修正
	if($PL_HS eq "1" && $_[0] eq 'PL'){
		$$HE = $DumW2;
		$Pl_SWName = $DumW2;
		$HEx=int($$IN[0]*2/3);
	}

	if($$PW[7] =~ m/!10/ && $$PW[1] <= 40 && $$PW[1] > 0){
		$$IN[0]=int($$IN[0]*2/3);
	}
	if($$BF && $$CF && $$DF){
		$$IN[3]=int($$IN[0]/3);
		$$IN[0]=int($$IN[0]*4/6+0.6);
	}elsif($$BF || $$CF || $$DF){
		$$IN[0]=int($$IN[0]*2/2);
		$$IN[3]=int($$IN[0]/1.5+1);
	}else{
		$$IN[3]=0;
	}
	if($$GO){
		if($$PBW[7]=~ m/!1c/){$$BF=1;}elsif($$PCW[7]=~ m/!1c/){$$CF=1;}elsif($$PDW[7]=~ m/!1c/){$$DF=1;}
		if($$BF && $$CF && $$DF){
			$$IN[3]=int($$IN[0]/2+0.4);
			$$IN[0]=int($$IN[0]/2+0.4);
		}else{
			$$IN[3]=int($$IN[0]/1.5+0.4);
			$$IN[0]=int($$IN[0]/1.5+0.4);
		}
	}
	if($$BF){
		$$BW=$$BL;
		$$BL+=$$IN[3] if $$BL < $MAX_WEAPONLV*100;
		$$BL=$MAX_WEAPONLV*100 if $$BL > $MAX_WEAPONLV*100;
		if(int($$BL/$WEAPON_LVUP) > int($$BW/$WEAPON_LVUP) && $$BL < $MAX_WEAPONLV*100){
		print "<font color=#f7e957>$FORM{\"$PN\"}の$$PBW[0]がレべルアップ</font><br>\n";}
#		$$PA[10]="$$WB!$$BL!$$WFB!$$B3!$$B4!$$B5!$$B6!$$B7!$$B8!$$B9!$$B10!$$B11!$$B12!$$B13!$$B14!$$B15!$$B16!$$B17!$$B18";
		if($_[0] eq 'PL'){$$PA[10]="$$WB!$$BL!$PL_WBEnt!$PL_WB03!$PL_WB04!$PL_WB05!$PL_WB06!$PL_WB07!$PL_WB08!$PL_WB09!$PL_WB10!$PL_WB11!$PL_WB12!$PL_WB13!$PL_WB14!$PL_WB15!$PL_WB16!$PL_WB17!$PL_WB18!$PL_WB19!$PL_WB20!$PL_WB21!$PL_WB22!$PL_WB23!$PL_WB24!$PL_WB25!$PL_WB26!$PL_WB27!$PL_WB28!$PL_WB29!$PL_WB30!$PL_WB31!$PL_WB32!$PL_WB33!$PL_WB34!$PL_WB35!$PL_WB36!$PL_WB37!$PL_WB38!$PL_WB39!$PL_WB40!$PL_WB41!$PL_WB42";}
		if($_[0] eq 'VS'){$$PA[10]="$$WB!$$BL!$VS_WBEnt!$VS_WB03!$VS_WB04!$VS_WB05!$VS_WB06!$VS_WB07!$VS_WB08!$VS_WB09!$VS_WB10!$VS_WB11!$VS_WB12!$VS_WB13!$VS_WB14!$VS_WB15!$VS_WB16!$VS_WB17!$VS_WB18!$VS_WB19!$VS_WB20!$VS_WB21!$VS_WB22!$VS_WB23!$VS_WB24!$VS_WB25!$VS_WB26!$VS_WB27!$VS_WB28!$VS_WB29!$VS_WB30!$VS_WB31!$VS_WB32!$VS_WB33!$VS_WB34!$VS_WB35!$VS_WB36!$VS_WB37!$VS_WB38!$VS_WB39!$VS_WB40!$VS_WB41!$VS_WB42";}
	}
	if($$CF){
		$$CW=$$CL;
		$$CL+=$$IN[3] if $$CL < $MAX_WEAPONLV*100;
		$$CL=$MAX_WEAPONLV*100 if $$CL > $MAX_WEAPONLV*100;
		if(int($$CL/$WEAPON_LVUP) > int($$CW/$WEAPON_LVUP) && $$CL < $MAX_WEAPONLV*100){
		print "<font color=#f7e957>$FORM{\"$PN\"}の$$PCW[0]がレべルアップ</font><br>\n";}
#		$$PA[11]="$$WC!$$CL!$$WFC!$$C3!$$C4!$$C5!$$C6!$$C7!$$C8!$$C9!$$C10!$$C11!$$C12!$$C13!$$C14!$$C15!$$C16!$$C17!$$C18";
		if($_[0] eq 'PL'){$$PA[11]="$$WC!$$CL!$PL_WCEnt!$PL_WC03!$PL_WC04!$PL_WC05!$PL_WC06!$PL_WC07!$PL_WC08!$PL_WC09!$PL_WC10!$PL_WC11!$PL_WC12!$PL_WC13!$PL_WC14!$PL_WC15!$PL_WC16!$PL_WC17!$PL_WC18!$PL_WC19!$PL_WC20!$PL_WC21!$PL_WC22!$PL_WC23!$PL_WC24!$PL_WC25!$PL_WC26!$PL_WC27!$PL_WC28!$PL_WC29!$PL_WC30!$PL_WC31!$PL_WC32!$PL_WC33!$PL_WC34!$PL_WC35!$PL_WC36!$PL_WC37!$PL_WC38!$PL_WC39!$PL_WC40!$PL_WC41!$PL_WC42";}
		if($_[0] eq 'VS'){$$PA[11]="$$WC!$$CL!$VS_WCEnt!$VS_WC03!$VS_WC04!$VS_WC05!$VS_WC06!$VS_WC07!$VS_WC08!$VS_WC09!$VS_WC10!$VS_WC11!$VS_WC12!$VS_WC13!$VS_WC14!$VS_WC15!$VS_WC16!$VS_WC17!$VS_WC18!$VS_WC19!$VS_WC20!$VS_WC21!$VS_WC22!$VS_WC23!$VS_WC24!$VS_WC25!$VS_WC26!$VS_WC27!$VS_WC28!$VS_WC29!$VS_WC30!$VS_WC31!$VS_WC32!$VS_WC33!$VS_WC34!$VS_WC35!$VS_WC36!$VS_WC37!$VS_WC38!$VS_WC39!$VS_WC40!$VS_WC41!$VS_WC42";}

	}
	if($$DF){
		$$DW=$$DL;
		$$DL+=$$IN[3] if $$DL < $MAX_WEAPONLV*100;
		$$DL=$MAX_WEAPONLV*100 if $$DL > $MAX_WEAPONLV*100;
		if(int($$DL/$WEAPON_LVUP) > int($$DW/$WEAPON_LVUP) && $$DL < $MAX_WEAPONLV*100){
		print "<font color=#f7e957>$FORM{\"$PN\"}の$$PDW[0]がレべルアップ</font><br>\n";}
#		$$PA[38]="$$WD!$$DL!$$WFD!$$D3!$$D4!$$D5!$$D6!$$D7!$$D8!$$D9!$$D10!$$D11!$$D12!$$D13!$$D14!$$D15!$$D16!$$D17!$$D18";
		if($_[0] eq 'PL'){$$PA[38]="$$WD!$$DL!$PL_WDEnt!$PL_WD03!$PL_WD04!$PL_WD05!$PL_WD06!$PL_WD07!$PL_WD08!$PL_WD09!$PL_WD10!$PL_WD11!$PL_WD12!$PL_WD13!$PL_WD14!$PL_WD15!$PL_WD16!$PL_WD17!$PL_WD18!$PL_WD19!$PL_WD20!$PL_WD21!$PL_WD22!$PL_WD23!$PL_WD24!$PL_WD25!$PL_WD26!$PL_WD27!$PL_WD28!$PL_WD29!$PL_WD30!$PL_WD31!$PL_WD32!$PL_WD33!$PL_WD34!$PL_WD35!$PL_WD36!$PL_WD37!$PL_WD38!$PL_WD39!$PL_WD40!$PL_WD41!$PL_WD42";}
		if($_[0] eq 'VS'){$$PA[38]="$$WD!$$DL!$VS_WDEnt!$VS_WD03!$VS_WD04!$VS_WD05!$VS_WD06!$VS_WD07!$VS_WD08!$VS_WD09!$VS_WD10!$VS_WD11!$VS_WD12!$VS_WD13!$VS_WD14!$VS_WD15!$VS_WD16!$VS_WD17!$VS_WD18!$VS_WD19!$VS_WD20!$VS_WD21!$VS_WD22!$VS_WD23!$VS_WD24!$VS_WD25!$VS_WD26!$VS_WD27!$VS_WD28!$VS_WD29!$VS_WD30!$VS_WD31!$VS_WD32!$VS_WD33!$VS_WD34!$VS_WD35!$VS_WD36!$VS_WD37!$VS_WD38!$VS_WD39!$VS_WD40!$VS_WD41!$VS_WD42";}

	}

#補助魔法のレベルアップ
	if($_[0] eq 'PL' && $PL_HS eq "1"){
		$PL_LVHH = int($PL_LVH/$WEAPON_LVUP);
#		$PL_LVH+=$$IN[3] if $PL_LVH < $MAX_WEAPONLV*100;
		$PL_LVH+=$HEx if $PL_LVH < $MAX_WEAPONLV*100;
		$PL_LVH=$MAX_WEAPONLV*100 if $PL_LVH > $MAX_WEAPONLV*100;
		if(int($PL_LVH/$WEAPON_LVUP) > $PL_LVHH && $PL_LVH < $MAX_WEAPONLV*100){
		print "<font color=#f7e957>$FORM{\"$PN\"}の$PL_H[0]がレべルアップ</font><br>\n";}
		$$PA[$FORM{'Hosentaku'}]="$PL_WH!$PL_LVH!$PL_WHEnt";
#	&ERROR("$PL_HSああ$FORM{'Hosentaku'}いい$PL_WH!$PL_LVHうう$Pl_EEXPええ$$PA[$FORM{'sentaku'}]あ$$PA[$FORM{'Hosentaku'}]");
	}

#	if($$SF){
		if($_[0] eq 'VS' && $Vs_EEXP eq "1" && $VS_sS[0]){
#			$$SW=$$SL;
#			$$SL+=$$IN[3] if $$SL < $MAX_WEAPONLV*100;
#			$$SL=$MAX_WEAPONLV*100 if $$SL > $MAX_WEAPONLV*100;
#			if(int($$SL/$WEAPON_LVUP) > int($$SW/$WEAPON_LVUP) && $$SL < $MAX_WEAPONLV*100){
#			$$SW=$$SL;
			$VS_LVS+=$$IN[0] if $$SL < $MAX_WEAPONLV*100;
			$VS_LVS=$MAX_WEAPONLV*100 if $VS_LVS > $MAX_WEAPONLV*100;
#			if(int($$SL/$WEAPON_LVUP) > int($$SW/$WEAPON_LVUP) && $$SL < $MAX_WEAPONLV*100){
			if(int($VS_LVS/$WEAPON_LVUP) > $VS_LVSS && $VS_LVS < $MAX_WEAPONLV*100){
			print "<font color=#f7e957>$FORM{\"$PN\"}の$$PSW[0]がレべルアップ</font><br>\n";}
#			$$PA[41]="$$WS!$VS_LVS";

			if($VS_VALUES[45] eq "90"){
				@VS_WSELE = split(/!/,$VS_VALUES[9]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WAEnt!$VS_WA03!$VS_WA04!$VS_WA05!$VS_WA06!$VS_WA07!$VS_WA08!$VS_WA09!$VS_WA10!$VS_WA11!$VS_WA12!$VS_WA13!$VS_WA14!$VS_WA15!$VS_WA16!$VS_WA17!$VS_WA18!$VS_WA19!$VS_WA20!$VS_WA21!$VS_WA22!$VS_WA23!$VS_WA24!$VS_WA25!$VS_WA26!$VS_WA27!$VS_WA28!$VS_WA29!$VS_WA30!$VS_WA31!$VS_WA32!$VS_WA33!$VS_WA34!$VS_WA35!$VS_WA36!$VS_WA37!$VS_WA38!$VS_WA39!$VS_WA40!$VS_WA41!$VS_WA42";}

			}elsif($VS_VALUES[45] eq "100"){
				@VS_WSELE = split(/!/,$VS_VALUES[10]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFB!$$B3!$$B4!$$B5!$$B6!$$B7!$$B8!$$B9!$$B10!$$B11!$$B12!$$B13!$$B14!$$B15!$$B16!$$B17!$$B18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WBEnt!$VS_WB03!$VS_WB04!$VS_WB05!$VS_WB06!$VS_WB07!$VS_WB08!$VS_WB09!$VS_WB10!$VS_WB11!$VS_WB12!$VS_WB13!$VS_WB14!$VS_WB15!$VS_WB16!$VS_WB17!$VS_WB18!$VS_WB19!$VS_WB20!$VS_WB21!$VS_WB22!$VS_WB23!$VS_WB24!$VS_WB25!$VS_WB26!$VS_WB27!$VS_WB28!$VS_WB29!$VS_WB30!$VS_WB31!$VS_WB32!$VS_WB33!$VS_WB34!$VS_WB35!$VS_WB36!$VS_WB37!$VS_WB38!$VS_WB39!$VS_WB40!$VS_WB41!$VS_WB42";}

			}elsif($VS_VALUES[45] eq "110"){
				@VS_WSELE = split(/!/,$VS_VALUES[11]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFC!$$C3!$$C4!$$C5!$$C6!$$C7!$$C8!$$C9!$$C10!$$C11!$$C12!$$C13!$$C14!$$C15!$$C16!$$C17!$$C18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WCEnt!$VS_WC03!$VS_WC04!$VS_WC05!$VS_WC06!$VS_WC07!$VS_WC08!$VS_WC09!$VS_WC10!$VS_WC11!$VS_WC12!$VS_WC13!$VS_WC14!$VS_WC15!$VS_WC16!$VS_WC17!$VS_WC18!$VS_WC19!$VS_WC20!$VS_WC21!$VS_WC22!$VS_WC23!$VS_WC24!$VS_WC25!$VS_WC26!$VS_WC27!$VS_WC28!$VS_WC29!$VS_WC30!$VS_WC31!$VS_WC32!$VS_WC33!$VS_WC34!$VS_WC35!$VS_WC36!$VS_WC37!$VS_WC38!$VS_WC39!$VS_WC40!$VS_WC41!$VS_WC42";}

			}elsif($VS_VALUES[45] eq "380"){
				@VS_WSELE = split(/!/,$VS_VALUES[38]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFD!$$D3!$$D4!$$D5!$$D6!$$D7!$$D8!$$D9!$$D10!$$D11!$$D12!$$D13!$$D14!$$D15!$$D16!$$D17!$$D18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WDEnt!$VS_WD03!$VS_WD04!$VS_WD05!$VS_WD06!$VS_WD07!$VS_WD08!$VS_WD09!$VS_WD10!$VS_WD11!$VS_WD12!$VS_WD13!$VS_WD14!$VS_WD15!$VS_WD16!$VS_WD17!$VS_WD18!$VS_WD19!$VS_WD20!$VS_WD21!$VS_WD22!$VS_WD23!$VS_WD24!$VS_WD25!$VS_WD26!$VS_WD27!$VS_WD28!$VS_WD29!$VS_WD30!$VS_WD31!$VS_WD32!$VS_WD33!$VS_WD34!$VS_WD35!$VS_WD36!$VS_WD37!$VS_WD38!$VS_WD39!$VS_WD40!$VS_WD41!$VS_WD42";}

			}elsif($VS_VALUES[45] eq "390"){
				$$WS = "";
			
			}else{
				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WSEnt";
			}

#			&ERROR("$VS_WSELEあ$VS_WSELE[0]ああ$VS_WSELE[1]");

#			$$PA[$VS_LVSET]="$$WS!$VS_LVS";
#			$$PA[41]="$$WS!$$SL";
		}elsif($_[0] eq 'VS' && $Vs_EEXP eq "2" && $VS_sS[0]){
#			$$SW=$$SL;
#			$$SL+=$$IN[3] if $$SL < $MAX_WEAPONLV*100;
#			$$SL=$MAX_WEAPONLV*100 if $$SL > $MAX_WEAPONLV*100;
#			if(int($$SL/$WEAPON_LVUP) > int($$SW/$WEAPON_LVUP) && $$SL < $MAX_WEAPONLV*100){

			$VS_LVS+=$$IN[0] if $$SL < $MAX_WEAPONLV*100;
			$VS_LVS=$MAX_WEAPONLV*100 if $VS_LVSS > $MAX_WEAPONLV*100;
			if(int($VS_LVS/$WEAPON_LVUP) > $VS_LVSS && $VS_LVS < $MAX_WEAPONLV*100){
#			print "<font color=#f7e957>$FORM{\"$PN\"}の$Vs_SSNameがレべルアップ</font><br>\n";}
			print "<font color=#f7e957>$FORM{\"$PN\"}の$$PSW[0]がレべルアップ</font><br>\n";}
#			$$PA[41]="$$WS!$$SL";
#			$$PA[41]="$$WS!$VS_LVS";

			if($VS_VALUES[45] eq "90"){
				@VS_WSELE = split(/!/,$VS_VALUES[9]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WAEnt!$VS_WA03!$VS_WA04!$VS_WA05!$VS_WA06!$VS_WA07!$VS_WA08!$VS_WA09!$VS_WA10!$VS_WA11!$VS_WA12!$VS_WA13!$VS_WA14!$VS_WA15!$VS_WA16!$VS_WA17!$VS_WA18!$VS_WA19!$VS_WA20!$VS_WA21!$VS_WA22!$VS_WA23!$VS_WA24!$VS_WA25!$VS_WA26!$VS_WA27!$VS_WA28!$VS_WA29!$VS_WA30!$VS_WA31!$VS_WA32!$VS_WA33!$VS_WA34!$VS_WA35!$VS_WA36!$VS_WA37!$VS_WA38!$VS_WA39!$VS_WA40!$VS_WA41!$VS_WA42";}

			}elsif($VS_VALUES[45] eq "100"){
				@VS_WSELE = split(/!/,$VS_VALUES[10]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFB!$$B3!$$B4!$$B5!$$B6!$$B7!$$B8!$$B9!$$B10!$$B11!$$B12!$$B13!$$B14!$$B15!$$B16!$$B17!$$B18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WBEnt!$VS_WB03!$VS_WB04!$VS_WB05!$VS_WB06!$VS_WB07!$VS_WB08!$VS_WB09!$VS_WB10!$VS_WB11!$VS_WB12!$VS_WB13!$VS_WB14!$VS_WB15!$VS_WB16!$VS_WB17!$VS_WB18!$VS_WB19!$VS_WB20!$VS_WB21!$VS_WB22!$VS_WB23!$VS_WB24!$VS_WB25!$VS_WB26!$VS_WB27!$VS_WB28!$VS_WB29!$VS_WB30!$VS_WB31!$VS_WB32!$VS_WB33!$VS_WB34!$VS_WB35!$VS_WB36!$VS_WB37!$VS_WB38!$VS_WB39!$VS_WB40!$VS_WB41!$VS_WB42";}

			}elsif($VS_VALUES[45] eq "110"){
				@VS_WSELE = split(/!/,$VS_VALUES[11]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFC!$$C3!$$C4!$$C5!$$C6!$$C7!$$C8!$$C9!$$C10!$$C11!$$C12!$$C13!$$C14!$$C15!$$C16!$$C17!$$C18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WCEnt!$VS_WC03!$VS_WC04!$VS_WC05!$VS_WC06!$VS_WC07!$VS_WC08!$VS_WC09!$VS_WC10!$VS_WC11!$VS_WC12!$VS_WC13!$VS_WC14!$VS_WC15!$VS_WC16!$VS_WC17!$VS_WC18!$VS_WC19!$VS_WC20!$VS_WC21!$VS_WC22!$VS_WC23!$VS_WC24!$VS_WC25!$VS_WC26!$VS_WC27!$VS_WC28!$VS_WC29!$VS_WC30!$VS_WC31!$VS_WC32!$VS_WC33!$VS_WC34!$VS_WC35!$VS_WC36!$VS_WC37!$VS_WC38!$VS_WC39!$VS_WC40!$VS_WC41!$VS_WC42";}
			}elsif($VS_VALUES[45] eq "380"){
				@VS_WSELE = split(/!/,$VS_VALUES[38]);
				$$WS = $VS_WSELE[0];
#				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$$WFD!$$D3!$$D4!$$D5!$$D6!$$D7!$$D8!$$D9!$$D10!$$D11!$$D12!$$D13!$$D14!$$D15!$$D16!$$D17!$$D18";
				if($_[0] eq 'VS'){$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WDEnt!$VS_WD03!$VS_WD04!$VS_WD05!$VS_WD06!$VS_WD07!$VS_WD08!$VS_WD09!$VS_WD10!$VS_WD11!$VS_WD12!$VS_WD13!$VS_WD14!$VS_WD15!$VS_WD16!$VS_WD17!$VS_WD18!$VS_WD19!$VS_WD20!$VS_WD21!$VS_WD22!$VS_WD23!$VS_WD24!$VS_WD25!$VS_WD26!$VS_WD27!$VS_WD28!$VS_WD29!$VS_WD30!$VS_WD31!$VS_WD32!$VS_WD33!$VS_WD34!$VS_WD35!$VS_WD36!$VS_WD37!$VS_WD38!$VS_WD39!$VS_WD40!$VS_WD41!$VS_WD42";}
			}elsif($VS_VALUES[45] eq "390"){
				$$WS = "";
			}else{
				$$PA[$VS_LVSET]="$$WS!$VS_LVS!$VS_WSEnt";
			}
#			&ERROR("$VS_WSELEあ$VS_WSELE[0]ああ$VS_WSELE[1]");

#			$$PA[$VS_LVSET]="$$WS!$VS_LVS";
		}elsif($_[0] eq 'PL' && $Pl_EEXP eq "1" && $PL_sS[0]){
#			$$SW=$$SL;
#			$$SL+=$$IN[3] if $$SL < $MAX_WEAPONLV*100;
#			$$SL=$MAX_WEAPONLV*100 if $$SL > $MAX_WEAPONLV*100;
#			if(int($$SL/$WEAPON_LVUP) > int($$SW/$WEAPON_LVUP) && $$SL < $MAX_WEAPONLV*100){
#&ERROR("$FORM{'sentaku'}ああいい$Pl_EEXP");
			$PL_LVS+=$$IN[0] if $$SL < $MAX_WEAPONLV*100;
			$PL_LVS=$MAX_WEAPONLV*100 if $PL_LVS > $MAX_WEAPONLV*100;
#&ERROR("$PL_LVSああ$PL_LVSS");
#			if(int($PL_LVS/$WEAPON_LVUP) > int($PL_LVSS/$WEAPON_LVUP) && $PL_LVS < $MAX_WEAPONLV*100){
			if(int($PL_LVS/$WEAPON_LVUP) > $PL_LVSS && $PL_LVS < $MAX_WEAPONLV*100){

			print "<font color=#f7e957>$FORM{\"$PN\"}の$$PSW[0]がレべルアップ</font><br>\n";}
#			$$PA[$FORM{'sentaku'}]="$$WS!$$SL";	

#			$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS";	

			if($FORM{'sentaku'} eq "9"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WAEnt!$PL_WA03!$PL_WA04!$PL_WA05!$PL_WA06!$PL_WA07!$PL_WA08!$PL_WA09!$PL_WA10!$PL_WA11!$PL_WA12!$PL_WA13!$PL_WA14!$PL_WA15!$PL_WA16!$PL_WA17!$PL_WA18!$PL_WA19!$PL_WA20!$PL_WA21!$PL_WA22!$PL_WA23!$PL_WA24!$PL_WA25!$PL_WA26!$PL_WA27!$PL_WA28!$PL_WA29!$PL_WA30!$PL_WA31!$PL_WA32!$PL_WA33!$PL_WA34!$PL_WA35!$PL_WA36!$PL_WA37!$PL_WA38!$PL_WA39!$PL_WA40!$PL_WA41!$PL_WA42";}
			elsif($FORM{'sentaku'} eq "10"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WBEnt!$PL_WB03!$PL_WB04!$PL_WB05!$PL_WB06!$PL_WB07!$PL_WB08!$PL_WB09!$PL_WB10!$PL_WB11!$PL_WB12!$PL_WB13!$PL_WB14!$PL_WB15!$PL_WB16!$PL_WB17!$PL_WB18!$PL_WB19!$PL_WB20!$PL_WB21!$PL_WB22!$PL_WB23!$PL_WB24!$PL_WB25!$PL_WB26!$PL_WB27!$PL_WB28!$PL_WB29!$PL_WB30!$PL_WB31!$PL_WB32!$PL_WB33!$PL_WB34!$PL_WB35!$PL_WB36!$PL_WB37!$PL_WB38!$PL_WB39!$PL_WB40!$PL_WB41!$PL_WB42";}
			elsif($FORM{'sentaku'} eq "11"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WCEnt!$PL_WC03!$PL_WC04!$PL_WC05!$PL_WC06!$PL_WC07!$PL_WC08!$PL_WC09!$PL_WC10!$PL_WC11!$PL_WC12!$PL_WC13!$PL_WC14!$PL_WC15!$PL_WC16!$PL_WC17!$PL_WC18!$PL_WC19!$PL_WC20!$PL_WC21!$PL_WC22!$PL_WC23!$PL_WC24!$PL_WC25!$PL_WC26!$PL_WC27!$PL_WC28!$PL_WC29!$PL_WC30!$PL_WC31!$PL_WC32!$PL_WC33!$PL_WC34!$PL_WC35!$PL_WC36!$PL_WC37!$PL_WC38!$PL_WC39!$PL_WC40!$PL_WC41!$PL_WC42";}
			elsif($FORM{'sentaku'} eq "38"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WDEnt!$PL_WD03!$PL_WD04!$PL_WD05!$PL_WD06!$PL_WD07!$PL_WD08!$PL_WD09!$PL_WD10!$PL_WD11!$PL_WD12!$PL_WD13!$PL_WD14!$PL_WD15!$PL_WD16!$PL_WD17!$PL_WD18!$PL_WD19!$PL_WD20!$PL_WD21!$PL_WD22!$PL_WD23!$PL_WD24!$PL_WD25!$PL_WD26!$PL_WD27!$PL_WD28!$PL_WD29!$PL_WD30!$PL_WD31!$PL_WD32!$PL_WD33!$PL_WD34!$PL_WD35!$PL_WD36!$PL_WD37!$PL_WD38!$PL_WD39!$PL_WD40!$PL_WD41!$PL_WD42";}
			elsif($FORM{'sentaku'} eq "41"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WSEnt";}
			elsif($FORM{'sentaku'} eq "42"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WSEnt";}
			elsif($FORM{'sentaku'} eq "43"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WSEnt";}

		}elsif($_[0] eq 'PL' && $Pl_EEXP eq "2" && $PL_sS[0]){
#			$$SW=$$SL;
#			$$SL+=$$IN[3] if $$SL < $MAX_WEAPONLV*100;
#			$$SL=$MAX_WEAPONLV*100 if $$SL > $MAX_WEAPONLV*100;
#			if(int($$SL/$WEAPON_LVUP) > int($$SW/$WEAPON_LVUP) && $$SL < $MAX_WEAPONLV*100){
#			print "<font color=#f7e957>$FORM{\"$PN\"}の$Pl_SSNameがレべルアップ</font><br>\n";}
#			$$PA[$FORM{'sentaku'}]="$$WS!$$SL";		

			$PL_LVS+=$$IN[0] if $$SL < $MAX_WEAPONLV*100;
			$PL_LVS=$MAX_WEAPONLV*100 if $PL_LVS > $MAX_WEAPONLV*100;
			if(int($PL_LVS/$WEAPON_LVUP) > $PL_LVSS && $PL_LVS < $MAX_WEAPONLV*100){
			print "<font color=#f7e957>$FORM{\"$PN\"}の$$PSW[0]がレべルアップ</font><br>\n";}
#			$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS";	
#			if($FORM{'sentaku'} eq "9"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";}
#			elsif($FORM{'sentaku'} eq "10"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$$WFB!$$B3!$$B4!$$B5!$$B6!$$B7!$$B8!$$B9!$$B10!$$B11!$$B12!$$B13!$$B14!$$B15!$$B16!$$B17!$$B18";}
#			elsif($FORM{'sentaku'} eq "11"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$$WFC!$$C3!$$C4!$$C5!$$C6!$$C7!$$C8!$$C9!$$C10!$$C11!$$C12!$$C13!$$C14!$$C15!$$C16!$$C17!$$C18";}
#			elsif($FORM{'sentaku'} eq "38"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$$WFD!$$D3!$$D4!$$D5!$$D6!$$D7!$$D8!$$D9!$$D10!$$D11!$$D12!$$D13!$$D14!$$D15!$$D16!$$D17!$$D18";}
			if($FORM{'sentaku'} eq "9"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WAEnt!$PL_WA03!$PL_WA04!$PL_WA05!$PL_WA06!$PL_WA07!$PL_WA08!$PL_WA09!$PL_WA10!$PL_WA11!$PL_WA12!$PL_WA13!$PL_WA14!$PL_WA15!$PL_WA16!$PL_WA17!$PL_WA18!$PL_WA19!$PL_WA20!$PL_WA21!$PL_WA22!$PL_WA23!$PL_WA24!$PL_WA25!$PL_WA26!$PL_WA27!$PL_WA28!$PL_WA29!$PL_WA30!$PL_WA31!$PL_WA32!$PL_WA33!$PL_WA34!$PL_WA35!$PL_WA36!$PL_WA37!$PL_WA38!$PL_WA39!$PL_WA40!$PL_WA41!$PL_WA42";}
			elsif($FORM{'sentaku'} eq "10"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WBEnt!$PL_WB03!$PL_WB04!$PL_WB05!$PL_WB06!$PL_WB07!$PL_WB08!$PL_WB09!$PL_WB10!$PL_WB11!$PL_WB12!$PL_WB13!$PL_WB14!$PL_WB15!$PL_WB16!$PL_WB17!$PL_WB18!$PL_WB19!$PL_WB20!$PL_WB21!$PL_WB22!$PL_WB23!$PL_WB24!$PL_WB25!$PL_WB26!$PL_WB27!$PL_WB28!$PL_WB29!$PL_WB30!$PL_WB31!$PL_WB32!$PL_WB33!$PL_WB34!$PL_WB35!$PL_WB36!$PL_WB37!$PL_WB38!$PL_WB39!$PL_WB40!$PL_WB41!$PL_WB42";}
			elsif($FORM{'sentaku'} eq "11"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WCEnt!$PL_WC03!$PL_WC04!$PL_WC05!$PL_WC06!$PL_WC07!$PL_WC08!$PL_WC09!$PL_WC10!$PL_WC11!$PL_WC12!$PL_WC13!$PL_WC14!$PL_WC15!$PL_WC16!$PL_WC17!$PL_WC18!$PL_WC19!$PL_WC20!$PL_WC21!$PL_WC22!$PL_WC23!$PL_WC24!$PL_WC25!$PL_WC26!$PL_WC27!$PL_WC28!$PL_WC29!$PL_WC30!$PL_WC31!$PL_WC32!$PL_WC33!$PL_WC34!$PL_WC35!$PL_WC36!$PL_WC37!$PL_WC38!$PL_WC39!$PL_WC40!$PL_WC41!$PL_WC42";}
			elsif($FORM{'sentaku'} eq "38"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WDEnt!$PL_WD03!$PL_WD04!$PL_WD05!$PL_WD06!$PL_WD07!$PL_WD08!$PL_WD09!$PL_WD10!$PL_WD11!$PL_WD12!$PL_WD13!$PL_WD14!$PL_WD15!$PL_WD16!$PL_WD17!$PL_WD18!$PL_WD19!$PL_WD20!$PL_WD21!$PL_WD22!$PL_WD23!$PL_WD24!$PL_WD25!$PL_WD26!$PL_WD27!$PL_WD28!$PL_WD29!$PL_WD30!$PL_WD31!$PL_WD32!$PL_WD33!$PL_WD34!$PL_WD35!$PL_WD36!$PL_WD37!$PL_WD38!$PL_WD39!$PL_WD40!$PL_WD41!$PL_WD42";}
			elsif($FORM{'sentaku'} eq "41"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WSEnt";}
			elsif($FORM{'sentaku'} eq "42"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WSEnt";}
			elsif($FORM{'sentaku'} eq "43"){$$PA[$FORM{'sentaku'}]="$$WS!$PL_LVS!$PL_WSEnt";}

		}
#	}
#&ERROR("$Pl_EEXPあああ$Vs_EEXP");
	if($_[0] eq 'PL' && $Pl_EEXP eq "0"){
		$$WL=$$WLV;$$WLV+=$$IN[0] if $$WLV < $MAX_WEAPONLV*100;
		$$WLV=$MAX_WEAPONLV*100 if $$WLV > $MAX_WEAPONLV*100;
		if(int($$WLV/$WEAPON_LVUP) > int($$WL/$WEAPON_LVUP) && $$WLV < $MAX_WEAPONLV*100){
			print "<font color=#f7e957>$FORM{\"$PN\"}の$$HEがレべルアップ</font><br>\n";
		}
#		$$PA[9]="$$WN!$$WLV!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";
		$$PA[9]="$$WN!$$WLV!$PL_WAEnt!$PL_WA03!$PL_WA04!$PL_WA05!$PL_WA06!$PL_WA07!$PL_WA08!$PL_WA09!$PL_WA10!$PL_WA11!$PL_WA12!$PL_WA13!$PL_WA14!$PL_WA15!$PL_WA16!$PL_WA17!$PL_WA18!$PL_WA19!$PL_WA20!$PL_WA21!$PL_WA22!$PL_WA23!$PL_WA24!$PL_WA25!$PL_WA26!$PL_WA27!$PL_WA28!$PL_WA29!$PL_WA30!$PL_WA31!$PL_WA32!$PL_WA33!$PL_WA34!$PL_WA35!$PL_WA36!$PL_WA37!$PL_WA38!$PL_WA39!$PL_WA40!$PL_WA41!$PL_WA42";
#		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1oa!0';}
		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1024a!0';}
	}elsif($_[0] eq 'PL' && $Pl_EEXP eq "2"){
#		$$WL=$$WLV;$$WLV+=$$IN[0] if $$WLV < $MAX_WEAPONLV*100;
#		$$WLV=$MAX_WEAPONLV*100 if $$WLV > $MAX_WEAPONLV*100;
#		if(int($$WLV/$WEAPON_LVUP) > int($$WL/$WEAPON_LVUP) && $$WLV < $MAX_WEAPONLV*100){
#			print "<font color=#f7e957>$FORM{\"$PN\"}の$$HEがレべルアップ</font><br>\n";
#			print "<font color=#f7e957>$FORM{\"$PN\"}の$Pl_SWNameがレべルアップ</font><br>\n";
#		}
#		$$PA[9]="$$WN!$$WLV";
		$$WL=$PL_WDuLv;$PL_WDuLv+=$$IN[0] if $PL_WDuLv < $MAX_WEAPONLV*100;
		$PL_WDuLv=$MAX_WEAPONLV*100 if $PL_WDuLv > $MAX_WEAPONLV*100;
		if(int($PL_WDuLv/$WEAPON_LVUP) > int($$WL/$WEAPON_LVUP) && $PL_WDuLv < $MAX_WEAPONLV*100){
			print "<font color=#f7e957>$FORM{\"$PN\"}の$Pl_SWNameがレべルアップ</font><br>\n";
		}
#		$$PA[9]="$$WN!$PL_WDuLv!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";
		$$PA[9]="$$WN!$PL_WDuLv!$PL_WAEnt!$PL_WA03!$PL_WA04!$PL_WA05!$PL_WA06!$PL_WA07!$PL_WA08!$PL_WA09!$PL_WA10!$PL_WA11!$PL_WA12!$PL_WA13!$PL_WA14!$PL_WA15!$PL_WA16!$PL_WA17!$PL_WA18!$PL_WA19!$PL_WA20!$PL_WA21!$PL_WA22!$PL_WA23!$PL_WA24!$PL_WA25!$PL_WA26!$PL_WA27!$PL_WA28!$PL_WA29!$PL_WA30!$PL_WA31!$PL_WA32!$PL_WA33!$PL_WA34!$PL_WA35!$PL_WA36!$PL_WA37!$PL_WA38!$PL_WA39!$PL_WA40!$PL_WA41!$PL_WA42";
#		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1oa!0';}
		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1024a!0';}
	}

	if($_[0] eq 'VS' && $Vs_EEXP eq "0"){
		$$WL=$$WLV;$$WLV+=$$IN[0] if $$WLV < $MAX_WEAPONLV*100;
		$$WLV=$MAX_WEAPONLV*100 if $$WLV > $MAX_WEAPONLV*100;
		if(int($$WLV/$WEAPON_LVUP) > int($$WL/$WEAPON_LVUP) && $$WLV < $MAX_WEAPONLV*100){
			print "<font color=#f7e957>$FORM{\"$PN\"}の$$HEがレべルアップ</font><br>\n";
		}
#		$$PA[9]="$$WN!$$WLV!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";
		$$PA[9]="$$WN!$$WLV!$VS_WAEnt!$VS_WA03!$VS_WA04!$VS_WA05!$VS_WA06!$VS_WA07!$VS_WA08!$VS_WA09!$VS_WA10!$VS_WA11!$VS_WA12!$VS_WA13!$VS_WA14!$VS_WA15!$VS_WA16!$VS_WA17!$VS_WA18!$VS_WA19!$VS_WA20!$VS_WA21!$VS_WA22!$VS_WA23!$VS_WA24!$VS_WA25!$VS_WA26!$VS_WA27!$VS_WA28!$VS_WA29!$VS_WA30!$VS_WA31!$VS_WA32!$VS_WA33!$VS_WA34!$VS_WA35!$VS_WA36!$VS_WA37!$VS_WA38!$VS_WA39!$VS_WA40!$VS_WA41!$VS_WA42";
#		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1oa!0';}
		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1024a!0';}
	}elsif($_[0] eq 'VS' && $Vs_EEXP eq "2"){
#		$$WL=$$WLV;$$WLV+=$$IN[0] if $$WLV < $MAX_WEAPONLV*100;
#		$$WLV=$MAX_WEAPONLV*100 if $$WLV > $MAX_WEAPONLV*100;
#		if(int($$WLV/$WEAPON_LVUP) > int($$WL/$WEAPON_LVUP) && $$WLV < $MAX_WEAPONLV*100){
#			print "<font color=#f7e957>$FORM{\"$PN\"}の$$HEがレべルアップ</font><br>\n";
#			print "<font color=#f7e957>$FORM{\"$PN\"}の$Vs_SWNameがレべルアップ</font><br>\n";
#		}
#		$$PA[9]="$$WN!$$WLV";
		$$WL=$VS_WDuLv;$VS_WDuLv+=$$IN[0] if $VS_WDuLv < $MAX_WEAPONLV*100;
		$VS_WDuLv=$MAX_WEAPONLV*100 if $VS_WDuLv > $MAX_WEAPONLV*100;
		if(int($VS_WDuLv/$WEAPON_LVUP) > int($$WL/$WEAPON_LVUP) && $VS_WDuLv < $MAX_WEAPONLV*100){
			print "<font color=#f7e957>$FORM{\"$PN\"}の$Vs_SWNameがレべルアップ</font><br>\n";
		}
#		$$PA[9]="$$WN!$VS_WDuLv!$$WFA!$$A3!$$A4!$$A5!$$A6!$$A7!$$A8!$$A9!$$A10!$$A11!$$A12!$$A13!$$A14!$$A15!$$A16!$$A17!$$A18";
#		$$PA[9]="$$WN!$$WLV!$PL_WAEnt!$PL_WA03!$PL_WA04!$PL_WA05!$PL_WA06!$PL_WA07!$PL_WA08!$PL_WA09!$PL_WA10!$PL_WA11!$PL_WA12!$PL_WA13!$PL_WA14!$PL_WA15!$PL_WA16!$PL_WA17!$PL_WA18!$PL_WA19!$PL_WA20!$PL_WA21!$PL_WA22!$PL_WA23!$PL_WA24!$PL_WA25!$PL_WA26!$PL_WA27!$PL_WA28!$PL_WA29!$PL_WA30!$PL_WA31!$PL_WA32!$PL_WA33!$PL_WA34!$PL_WA35!$PL_WA36!$PL_WA37!$PL_WA38!$PL_WA39!$PL_WA40!$PL_WA41!$PL_WA42";
		$$PA[9]="$$WN!$VS_WDuLv!$VS_WAEnt!$VS_WA03!$VS_WA04!$VS_WA05!$VS_WA06!$VS_WA07!$VS_WA08!$VS_WA09!$VS_WA10!$VS_WA11!$VS_WA12!$VS_WA13!$VS_WA14!$VS_WA15!$VS_WA16!$VS_WA17!$VS_WA18!$VS_WA19!$VS_WA20!$VS_WA21!$VS_WA22!$VS_WA23!$VS_WA24!$VS_WA25!$VS_WA26!$VS_WA27!$VS_WA28!$VS_WA29!$VS_WA30!$VS_WA31!$VS_WA32!$VS_WA33!$VS_WA34!$VS_WA35!$VS_WA36!$VS_WA37!$VS_WA38!$VS_WA39!$VS_WA40!$VS_WA41!$VS_WA42";
#		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1oa!0';}
		if($$PW[7] =~ m/!1m|!1n|!zc/){$$PA[9]='1024a!0';}
	}
	

#	$Pl_SWName = $Pl_W[0];$Vs_SWName = $Vs_W[0];
#	$Pl_SSName = $Pl_sS[0];$Vs_SSName = $Vs_sS[0];
#	if($$PSW[0] eq "属性ブレス"){
#		print "<font color=#f7e957>テスト中。$PL_sS[0]</font><br>\n";
#	}
#$Vs_DefPoint
#	print "<font color=#f7e957>$Vs_DefPointと$Pl_AttPoint</font><br>\n";
}
1;
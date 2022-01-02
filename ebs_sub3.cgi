sub GETIP{
	$for    = $ENV{'HTTP_FORWARDED'};
	$xfor   = $ENV{'HTTP_X_FORWARDED_FOR'};
	$sp_host   = $ENV{'HTTP_SP_HOST'};
	$client_ip = $ENV{'HTTP_CLIENT_IP'};
	$http_from = $ENV{'HTTP_FROM'};

	$trueip = $sp_host   if ($sp_host ne "");
	$trueip = $via       if ($via =~ s/.*\s(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/);
	if( $client_ip=~ s/^(\d+)\.(\d+)\.(\d+)\.(\d+)(\D*).*/$1.$2.$3.$4/ ){
		$trueip = $client_ip;
	}elsif( $client_ip=~ s/^([\dA-F]{2})([\dA-F]{2})([\dA-F]{2})([\dA-F]{2})/$1$2$3$4/i){
		$client_ip = join('.', hex($1), hex($2), hex($3), hex($4)); 
		$trueip = $client_ip;
	}
	$trueip = $for       if ($for =~ s/.*\s(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/);
	$trueip = $xfor      if ($xfor =~ s/^(\d+)\.(\d+)\.(\d+)\.(\d+)(\D*).*/$1.$2.$3.$4/);
	$trueip = $http_from if ($http_from ne "");
	return $trueip;
}
sub STATUS{
	&DBM_CONVERT('P',"$FORM{pname}") if !$FORM{'Cmode'};

	if(!@PL_VALUES){
	require 'ebs_sub9.cgi';&SAVELORD;
	&DBM_CONVERT('P',"$FORM{pname}") if !$FORM{'Cmode'};
	}
	&DBM_CONVERT('C',"$PL_VALUES[5]") if $PL_VALUES[5];

	&ERROR('NameError','IDが間違っているか、登録されていません。') if !@PL_VALUES;
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($FORM{'pass'},eb) ne "$PL_VALUES[2]";
	if ($FORM{'login'}){
	$PL_VALUES[26] = time;
#	if($PL_VALUES[26] >= time){}else{$PL_VALUES[26]=time;$flagd=1;}
	if($PL_VALUES[26] >= time-$kk_time*60){}else{$PL_VALUES[26]=time;$flagd=1;}

	dbmopen (%PL,"$DBM_P",0666);
		$PL{"$FORM{'pname'}"}="@PL_VALUES";
	dbmclose %PL;}

#	my ($DatHp,$Result) = split(/\!/,$PL_VALUES[1]);	#戦闘履歴のコンバート
#	&ERROR("$DATEああ$DatHpいいtime");
#&ERROR(time);

#	&ERROR('SystemError',"ユーザー情報の取得に失敗しました。");

#	$xxs=time;
#	&ERROR("$xxs");

#	&REPAIR(PL);
	&REPAIR(\@PL_VALUES);

	if ($FORM{'login'}){
	my $addr    = $ENV{'REMOTE_ADDR'};
	my $host    = $ENV{'REMOTE_HOST'};
	if (($host eq $addr) || ($host eq '')) {$host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;}
	$trueip = &GETIP;$TAZYU=$CKFRAG=0;
	dbmopen (%L,"$DBM_L",0666);
		foreach (sort {$b <=> $a} keys %L){$lc++;@lgn=split(/!/,$L{"$_"});
		$TAZYU=1 if ($lgn[0] ne "$FORM{'pname'}" && $lgn[1] eq "$addr" && $lgn[2] eq "$host" && $lgn[3] eq "$ENV{'HTTP_USER_AGENT'}" && $lgn[4] eq "$trueip" );
		delete $L{"$_"} if ( $lc > 151 || $lgn[0] eq "$FORM{'pname'}" );
		$CKFRAG=1 if ($lgn[0] eq "$FORM{'pname'}" && ($_ + 120) > time);
		}
		$L{"$DATE"}="$FORM{'pname'}!$addr!$host!$ENV{'HTTP_USER_AGENT'}!$trueip!$TAZYU";
	dbmclose %L;
#	&ERROR('LoginError','2分以内の連続ログイン規制中') if $CKFRAG==1;
	}
	SET_COOKIE:{
		my @gmt = gmtime(time + $COOKIE_KEEP*24*60*60);
		$gmt[0] = sprintf("%02d", $gmt[0]);	$gmt[1] = sprintf("%02d", $gmt[1]);
		$gmt[2] = sprintf("%02d", $gmt[2]);	$gmt[3] = sprintf("%02d", $gmt[3]);	$gmt[5] += 1900;
		$gmt[4] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$gmt[4]];
		$gmt[6] = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$gmt[6]];
		my $date_gmt = "$gmt[6], $gmt[3]\-$gmt[4]\-$gmt[5] $gmt[2]:$gmt[1]:$gmt[0] GMT";
		my $cook = "pname:$FORM{'pname'},pass:$FORM{'pass'}";$SCKIE="Set-Cookie: EB=$cook; expires=$date_gmt\n";
	}
	if ($PL_VALUES[28]){
		foreach ("$CL_VALUES[2]","$CL_VALUES[3]","$CL_VALUES[4]"){if ($PL_VALUES[28] eq "$_") {$DeleteFlag=1;}}
		if (!$DeleteFlag){$PL_VALUES[28]="";$flagd=1; if ($PL_VALUES[6] eq "-1"){$PL_VALUES[6]='0';}}
	}
	if ($PL_VALUES[5] && !@CL_VALUES){
		$PL_VALUES[5]=$PL_VALUES[28]='';
		$PL_VALUES[0]=$PL_VALUES[6]='0';
		$flagd=1;
	}elsif($PL_VALUES[5] && $FORM{'login'} && time > ($PL_VALUES[26] + $HOUCHI*24*60*60) && $PL_VALUES[6]==0){
		$PL_VALUES[5]=$PL_VALUES[28]='';
		$PL_VALUES[0]=$PL_VALUES[6]='0';
		$flagd=1;
	}
	if (!$PL_VALUES[5] && $PL_VALUES[6]){$PL_VALUES[6]='0';$flagd=1;}
	if ($flagd){
		dbmopen (%PL,"$DBM_P",0666);
			$PL{"$FORM{'pname'}"}="@PL_VALUES";
		dbmclose %PL;
	}

#	local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#	local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#	local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#	local($WN_D2,$WLV_D2) = split(/!/,$PL_VALUES[38]);
#	local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
#	local($WN_T,$WLV_T) = split(/!/,$PL_VALUES[42]);
#	local($WN_U,$WLV_U) = split(/!/,$PL_VALUES[43]);

	local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);
	local($WN_B,$WLV_B,$WBEnt,$WB03,$WB04,$WB05,$WB06,$WB07,$WB08,$WB09,$WB10,$WB11,$WB12,$WB13,$WB14,$WB15,$WB16,$WB17,$WB18,$WB19,$WB20,$WB21,$WB22,$WB23,$WB24,$WB25,$WB26,$WB27,$WB28,$WB29,$WB30,$WB31,$WB32,$WB33,$WB34,$WB35,$WB36,$WB37,$WB38,$WB39,$WB40,$WB41,$WB42) = split(/!/,$PL_VALUES[10]);
	local($WN_C,$WLV_C,$WCEnt,$WC03,$WC04,$WC05,$WC06,$WC07,$WC08,$WC09,$WC10,$WC11,$WC12,$WC13,$WC14,$WC15,$WC16,$WC17,$WC18,$WC19,$WC20,$WC21,$WC22,$WC23,$WC24,$WC25,$WC26,$WC27,$WC28,$WC29,$WC30,$WC31,$WC32,$WC33,$WC34,$WC35,$WC36,$WC37,$WC38,$WC39,$WC40,$WC41,$WC42) = split(/!/,$PL_VALUES[11]);
	local($WN_D2,$WLV_D2,$WDEnt,$WD03,$WD04,$WD05,$WD06,$WD07,$WD08,$WD09,$WD10,$WD11,$WD12,$WD13,$WD14,$WD15,$WD16,$WD17,$WD18,$WD19,$WD20,$WD21,$WD22,$WD23,$WD24,$WD25,$WD26,$WD27,$WD28,$WD29,$WD30,$WD31,$WD32,$WD33,$WD34,$WD35,$WD36,$WD37,$WD38,$WD39,$WD40,$WD41,$WD42) = split(/!/,$PL_VALUES[38]);
	local($WN_S,$WLV_S,$WSEnt,$WS03,$WS04,$WS05,$WS06,$WS07,$WS08,$WS09,$WS10,$WS11,$WS12,$WS13,$WS14,$WS15,$WS16,$WS17,$WS18,$WS19,$WS20,$WS21,$WS22,$WS23,$WS24,$WS25,$WS26,$WS27,$WS28,$WS29,$WS30,$WS31,$WS32,$WS33,$WS34,$WS35,$WS36,$WS37,$WS38,$WS39,$WS40,$WS41,$WS42) = split(/!/,$PL_VALUES[41]);
	local($WN_T,$WLV_T,$WTEnt,$WT03,$WT04,$WT05,$WT06,$WT07,$WT08,$WT09,$WT10,$WT11,$WT12,$WT13,$WT14,$WT15,$WT16,$WT17,$WT18,$WT19,$WT20,$WT21,$WT22,$WT23,$WT24,$WT25,$WT26,$WT27,$WT28,$WT29,$WT30,$WT31,$WT32,$WT33,$WT34,$WT35,$WT36,$WT37,$WT38,$WT39,$WT40,$WT41,$WT42) = split(/!/,$PL_VALUES[42]);
	local($WN_U,$WLV_U,$WUEnt,$WU03,$WU04,$WU05,$WU06,$WU07,$WU08,$WU09,$WU10,$WU11,$WU12,$WU13,$WU14,$WU15,$WU16,$WU17,$WU18,$WU19,$WU20,$WU21,$WU22,$WU23,$WU24,$WU25,$WU26,$WU27,$WU28,$WU29,$WU30,$WU31,$WU32,$WU33,$WU34,$WU35,$WU36,$WU37,$WU38,$WU39,$WU40,$WU41,$WU42) = split(/!/,$PL_VALUES[43]);

	if($PL_VALUES[25] == 0){$CONDITIONAL = '<font color=#5779EE>出撃可</font>';}
	elsif($PL_VALUES[25] == 1){$CONDITIONAL = '<font color=#dc143c>回復中</font>';}

	$CL_VALUES[0]='#808080' if !$PL_VALUES[5];
	if(($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i) && ($PL_VALUES[4] =~ /^64$|^71$|^72$/i)){
		if($PL_VALUES[4]==71){$PL_VALUES[4]=210;$CLASS_FRAG=1;}
		if($PL_VALUES[4]==72){$PL_VALUES[4]=211;$CLASS_FRAG=2;}
		if($PL_VALUES[4]==64){$PL_VALUES[4]=65;$CLASS_FRAG=3;}
	}
	if($PL_VALUES[6]==1){
		if($PL_VALUES[4]==131){$PL_VALUES[4]=197;$CLASS_FRAG=4;}
		elsif($PL_VALUES[4]==132){$PL_VALUES[4]=198;$CLASS_FRAG=5;}
		elsif($PL_VALUES[4]==133){$PL_VALUES[4]=199;$CLASS_FRAG=6;}
		elsif($PL_VALUES[4]==134){$PL_VALUES[4]=200;$CLASS_FRAG=7;}
		elsif($PL_VALUES[4]==135){$PL_VALUES[4]=201;$CLASS_FRAG=8;}
	}
	if($PL_VALUES[4]==203){
		if($PL_VALUES[12] > 71){
			$PL_VALUES[4]=208;$CLASS_FRAG=9;
		}if($PL_VALUES[12] < 36){
			$PL_VALUES[4]=209;$CLASS_FRAG=9;
		}
	}
	@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});@WN_sD2=split(/\,/,$WEAPON_LIST{"$WN_D2"});
	@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});
	if($WN_sA[7]=~ m/!1c/ && $WN_sB[7]=~ m/!1c/){
		$WEP_D=int(($WLV_A+$WLV_B)/2%$WEAPON_LVUP);
		$WLV_D=int(($WLV_A+$WLV_B)/2/$WEAPON_LVUP);
	}
	if($WN_sA[7]=~ m/!1c/ && $WN_sC[7]=~ m/!1c/){
		$WEP_D=int(($WLV_A+$WLV_C)/2%$WEAPON_LVUP);
		$WLV_D=int(($WLV_A+$WLV_C)/2/$WEAPON_LVUP);
	}
	if($WN_sA[7]=~ m/!1c/ && $WN_sD2[7]=~ m/!1c/){
		$WEP_D=int(($WLV_A+$WLV_D2)/2%$WEAPON_LVUP);
		$WLV_D=int(($WLV_A+$WLV_D2)/2/$WEAPON_LVUP);
	}
	if($WN_sB[7]=~ m/!1c/ && $WN_sC[7]=~ m/!1c/){
		$WEP_D=int(($WLV_B+$WLV_C)/2%$WEAPON_LVUP);
		$WLV_D=int(($WLV_B+$WLV_C)/2/$WEAPON_LVUP);
	}
	if($WN_sB[7]=~ m/!1c/ && $WN_sD2[7]=~ m/!1c/){
		$WEP_D=int(($WLV_B+$WLV_D2)/2%$WEAPON_LVUP);
		$WLV_D=int(($WLV_B+$WLV_D2)/2/$WEAPON_LVUP);
	}
	if($WN_sC[7]=~ m/!1c/ && $WN_sD2[7]=~ m/!1c/){
		$WEP_D=int(($WLV_C+$WLV_D2)/2%$WEAPON_LVUP);
		$WLV_D=int(($WLV_C+$WLV_D2)/2/$WEAPON_LVUP);
	}

	$WEP_E=$WLV_A;
	$WEP_A=$WLV_A%$WEAPON_LVUP;
	$WEP_B=$WLV_B%$WEAPON_LVUP;
	$WEP_C=$WLV_C%$WEAPON_LVUP;
	$WEP_D2=$WLV_D2%$WEAPON_LVUP;
	$WEP_S=$WLV_S%$WEAPON_LVUP;
	$WEP_T=$WLV_T%$WEAPON_LVUP;
	$WEP_U=$WLV_U%$WEAPON_LVUP;
	$WLV_A=int$WLV_A/$WEAPON_LVUP;
	$WLV_B=int$WLV_B/$WEAPON_LVUP;
	$WLV_C=int$WLV_C/$WEAPON_LVUP;
	$WLV_D2=int$WLV_D2/$WEAPON_LVUP;
	$WLV_S=int$WLV_S/$WEAPON_LVUP;
	$WLV_T=int$WLV_T/$WEAPON_LVUP;
	$WLV_U=int$WLV_U/$WEAPON_LVUP;

##クラス読み込み
	require "./$LOG_FOLDER/$CLASS_DATA";
	@ALY_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

#ブレス攻撃
	if($WN_sS[7] =~ m/!61/){
	@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
	@WN_sS=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sS[7] =~ m/!62/){
	@array=(ubag,ubah,ubai,ubaj,ubak,ubal);
	@WN_sS=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sT[7] =~ m/!61/){
	@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
	@WN_sT=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sT[7] =~ m/!62/){
	@array=(ubag,ubah,ubai,ubaj,ubak,ubal);
	@WN_sT=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sU[7] =~ m/!61/){
	@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
	@WN_sU=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sU[7] =~ m/!62/){
	@array=(ubag,ubah,ubai,ubaj,ubak,ubal);
	@WN_sU=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
#コッレクティオ
	if($WN_sS[7] =~ m/!63/){
	@array=(ubao,ubap,ubaq,ubar,ubas,ubat);
	@WN_sS=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sT[7] =~ m/!63/){
	@array=(ubao,ubap,ubaq,ubar,ubas,ubat);
	@WN_sT=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
	if($WN_sU[7] =~ m/!63/){
	@array=(ubao,ubap,ubaq,ubar,ubas,ubat);
	@WN_sU=split(/\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"});
	}
##得意武器性能変化
	$WN_sA[2]+=40 if $WN_sA[7] =~ m/!1a/ && $ALY_CLASS[17] =~ m/!2/;#弓

#BattleLevel
	if($BattleLevel eq "1"){
		#最上段の武器
#		if($WN_sA[14] =~ m/A02/){
#			$WN_sA[1] = int($WN_sA[1] * 0.97);
##			$WN_sA[2] = int($WN_sA[2] * 0.97);
#		}
		#技
#		if($WN_sS[11] eq "5"){
#			$WN_sS[1]-=50;
#		}
		#魔法
		if($WN_sS[11] eq "1" || $WN_sS[11] eq "2" || $WN_sS[11] eq "3"){
			$WN_sS[1] = int($WN_sS[1]*0.9);
#			$WN_sS[2] = int($WN_sS[2]*0.95);
		}
		#特殊
		if($WN_sS[11] eq "6" || $WN_sS[11] eq "7" || $WN_sS[11] eq "8"){
			$WN_sS[1] = int($WN_sS[1]*0.93);
#			$WN_sS[2] = int($WN_sS[2]*0.97);
		}
	}

#片手持ち：槍 $PL_W[7] =~ s/!00|!01|!02|!03|!04|!05/!xx/g;
	if($WN_sA[7] =~ m/!1y04/ && $ALY_CLASS[17]=~ m/!W018/){$WN_sA[7] =~ s/!11/!10/g;}

	if($AbiSys == 1){
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		require "./$LOG_FOLDER/$ABI_DATA";
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

		if($ABI_sA[2] =~ m/!A0091/ || $ABI_sB[2] =~ m/!A0091/ || $ABI_sC[2] =~ m/!A0091/){$WN_sA[7] =~ s/!11/!10/g;$WN_sA[4] = int($WN_sA[4]*1.2);}

	}

#ノックバック：弓
	if($WN_sA[7] =~ m/!1a/ && $ALY_CLASS[17] =~ m/!W020/){$WN_sA[7] .= "!2g";}

	#ディアナで弓以外を使用した場合は性能低下
	if($WN_sA[7] !~ m/!1a/ && $ALY_CLASS[17]=~ m/!E005/){$WN_sA[1]=int($WN_sA[1]*0.7);$WN_sA[2]=int($WN_sA[2]*0.7);$WN_sA[4]+=40;}

#特定武器にて
#	&ERROR("$WN_sA[0]ああ$ALY_CLASS[17]いい");
	if ($WN_sA[7]=~ m/!6d/ || $WN_sS[7]=~ m/!6d/){

		if($WN_sA[0] eq 'リムファイアー' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ubbd"});}
		if($WN_sA[0] eq 'カマンダスガン' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ubbe"});}
		if($WN_sA[0] eq 'アッサルト' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ubbf"});}
		if($WN_sA[0] eq 'マスケットガン' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ub0200a"});}
		if($WN_sA[0] eq 'ペトロネル' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ub0201a"});}
		if($WN_sA[0] eq 'バンドゥイチャクマ' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ub0202a"});}
		if($WN_sA[0] eq 'デリンジャー' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ub0203a"});}
		if($WN_sA[0] eq 'アサルトライフル' && $ALY_CLASS[17]=~ m/!3/){@WN_sA=split(/\,/,$WEAPON_LIST{"ub0204a"});}

		if($WN_sA[0] eq 'アンビシオン' && $ALY_CLASS[17]=~ m/!W103/){@WN_sA=split(/\,/,$WEAPON_LIST{"ub1haba"});}

		if($WN_sS[0] eq 'ジハド' && $ALY_CLASS[17]=~ m/!7/){$WN_sS[1]+=10200;$WN_sS[4]+=110;}
		if($WN_sS[0] eq 'サッドソ\ング' && $ALY_CLASS[17]=~ m/!m/){$WN_sS[1]+=1600;$WN_sS[2]+=20;$WN_sS[3]-=2;}
		if($WN_sS[0] eq 'サイレントソ\ング' && $ALY_CLASS[17]=~ m/!n/){$WN_sS[1]+=2400;$WN_sS[2]+=10;}
		if($WN_sS[0] eq 'バニッシュ' && $ALY_CLASS[17]=~ m/!l/){$WN_sS[1]+=11800;$WN_sS[2]+=20;$WN_sS[4]+=105;}#バニッシュ
		if($WN_sS[0] eq 'メテオストライク' && $ALY_CLASS[17]=~ m/!a/){@WN_sS=split(/\,/,$WEAPON_LIST{"ubaz"});}
		if($WN_sS[0] eq 'スターティアラ' && $ALY_CLASS[17]=~ m/!c/){@WN_sS=split(/\,/,$WEAPON_LIST{"ubba"});}
		if($WN_sS[0] eq 'ダークロア' && $ALY_CLASS[17]=~ m/!b/){@WN_sS=split(/\,/,$WEAPON_LIST{"ubbb"});}
		if($WN_sS[0] eq 'サモンダークネス' && $ALY_CLASS[17]=~ m/!o/){@WN_sS=split(/\,/,$WEAPON_LIST{"ubbc"});}
		if($WN_sS[0] eq 'マジックボム' && $ALY_CLASS[17]=~ m/!8/){$WN_sS[2]+=50;}
		if($WN_sS[0] eq 'ジェミニアタック' && $ALY_CLASS[17]=~ m/!6/){$WN_sS[2]+=50;}
		if($WN_sS[0] eq 'ギガントブロウ' && $ALY_CLASS[17]=~ m/!9/){$WN_sS[1]+=5000;$WN_sS[2]-=10;}
		if($WN_sS[0] eq 'サモンダークネス' && $ALY_CLASS[17]=~ m/!u/){@WN_sS=split(/\,/,$WEAPON_LIST{"ubbg"});}

		if($WN_sS[0] eq 'ロンギコルニス' && $ALY_CLASS[17]=~ m/!W104/){@WN_sS=split(/\,/,$WEAPON_LIST{"ub2de"});}

		if($WN_sS[7] =~ m/!1k/ && $ALY_CLASS[17]=~ m/!5/){$WN_sS[2]+=20;}
		if($WN_sS[7] =~ m/!1l/ && $ALY_CLASS[17]=~ m/!4/){$WN_sS[2]+=20;}
		if($WN_sA[7] =~ m/!6w/){
			if($ALY_CLASS[3] > 0){#$WN_sA[1]/=$ALY_CLASS[3]+1;
								$WN_sA[3]+=$ALY_CLASS[3];}
		}
		if($WN_sS[7] =~ m/!6w/){
			if($ALY_CLASS[3] > 0){#$WN_sS[1]/=$ALY_CLASS[3]+1;
								$WN_sS[3]+=$ALY_CLASS[3];}
		}
#		if($WN_sS[7] =~ m/!6o/){
#			unless((($WN_sS[7] =~ m/!6j|!6k/ && $ALY_CLASS[17] =~ m/!p/) || ($WN_sS[7]=~ m/!6l/ && $ALY_CLASS[17] =~ m/!q/)) && $CL_VALUES[7] > time){
#				@WN_sS=split(/\,/,$WEAPON_LIST{"p"});
#			}
#		}

	#セット装備
#		if($WN_sA[7] =~ m/!50/ && $WN_sA[0] eq "オラシオン" && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!50/ && $WN_sC[7] !~ m/!12/ && $WN_sD2[7] !~ m/!12/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!50/ && $WN_sD2[7] !~ m/!12/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!50/))){$WN_sA[1]+=5500;$WN_sA[2]-=2;$WN_sA[4]+=110;}#超神聖
#		if($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sB[0] eq "聖者の盾" && (($WN_sC[0] eq "サザンクロス" || $WN_sC[0] eq "フロイデヘルム") || ($WN_sD2[0] eq "サザンクロス" || $WN_sD2[0] eq "フロイデヘルム"))){$WN_sA[2]+=22;$WN_sA[4]-=70;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sC[0] eq "聖者の盾" && (($WN_sB[0] eq "サザンクロス" || $WN_sB[0] eq "フロイデヘルム") || ($WN_sD2[0] eq "サザンクロス" || $WN_sD2[0] eq "フロイデヘルム"))){$WN_sA[2]+=22;$WN_sA[4]-=70;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sD2[0] eq "聖者の盾" && (($WN_sB[0] eq "サザンクロス" || $WN_sB[0] eq "フロイデヘルム") || ($WN_sC[0] eq "サザンクロス" || $WN_sC[0] eq "フロイデヘルム"))){$WN_sA[2]+=22;$WN_sA[4]-=70;}
#		if($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sB[0] eq "聖者の盾" && $WN_sC[0] eq "サザンクロス" && $WN_sD2[0] eq "フロイデヘルム"){$WN_sA[1]+=2000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sB[0] eq "聖者の盾" && $WN_sD2[0] eq "サザンクロス" && $WN_sC[0] eq "フロイデヘルム"){$WN_sA[1]+=2000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sC[0] eq "聖者の盾" && $WN_sB[0] eq "サザンクロス" && $WN_sD2[0] eq "フロイデヘルム"){$WN_sA[1]+=2000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sC[0] eq "聖者の盾" && $WN_sD2[0] eq "サザンクロス" && $WN_sB[0] eq "フロイデヘルム"){$WN_sA[1]+=2000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sD2[0] eq "聖者の盾" && $WN_sB[0] eq "サザンクロス" && $WN_sC[0] eq "フロイデヘルム"){$WN_sA[1]+=2000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!50/ && $WN_sA[0] eq "オラシオン" && $WN_sD2[0] eq "聖者の盾" && $WN_sC[0] eq "サザンクロス" && $WN_sB[0] eq "フロイデヘルム"){$WN_sA[1]+=2000;$WN_sA[4]-=40;}

#		if($WN_sA[7] =~ m/!51/ && $WN_sA[0] eq "オウガブレード" && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!51/ && $WN_sC[7] !~ m/!12/ && $WN_sD2[7] !~ m/!12/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!51/ && $WN_sD2[7] !~ m/!12/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!51/))){$WN_sA[2]+=48;$WN_sA[4]+=80;}#鬼セ
#		if($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sB[0] eq "オウガシールド" && (($WN_sC[0] eq "オウガアーマー" || $WN_sC[0] eq "オウガヘルム") || ($WN_sD2[0] eq "オウガアーマー" || $WN_sD2[0] eq "オウガヘルム"))){$WN_sA[1]+=3000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sC[0] eq "オウガシールド" && (($WN_sB[0] eq "オウガアーマー" || $WN_sB[0] eq "オウガヘルム") || ($WN_sD2[0] eq "オウガアーマー" || $WN_sD2[0] eq "オウガヘルム"))){$WN_sA[1]+=3000;$WN_sA[4]-=40;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sD2[0] eq "オウガシールド" && (($WN_sC[0] eq "オウガアーマー" || $WN_sC[0] eq "オウガヘルム") || ($WN_sB[0] eq "オウガアーマー" || $WN_sB[0] eq "オウガヘルム"))){$WN_sA[1]+=3000;$WN_sA[4]-=40;}
#		if($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sB[0] eq "オウガシールド" && $WN_sC[0] eq "オウガアーマー" && $WN_sD2[0] eq "オウガヘルム"){$WN_sA[1]+=3000;$WN_sA[4]-=80;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sB[0] eq "オウガシールド" && $WN_sD2[0] eq "オウガアーマー" && $WN_sC[0] eq "オウガヘルム"){$WN_sA[1]+=3000;$WN_sA[4]-=80;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sC[0] eq "オウガシールド" && $WN_sB[0] eq "オウガアーマー" && $WN_sD2[0] eq "オウガヘルム"){$WN_sA[1]+=3000;$WN_sA[4]-=80;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sC[0] eq "オウガシールド" && $WN_sD2[0] eq "オウガアーマー" && $WN_sB[0] eq "オウガヘルム"){$WN_sA[1]+=3000;$WN_sA[4]-=80;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sD2[0] eq "オウガシールド" && $WN_sB[0] eq "オウガアーマー" && $WN_sC[0] eq "オウガヘルム"){$WN_sA[1]+=3000;$WN_sA[4]-=80;}
#		elsif($WN_sA[7]=~ m/!51/ && $WN_sA[0] eq "オウガブレード" && $WN_sD2[0] eq "オウガシールド" && $WN_sC[0] eq "オウガアーマー" && $WN_sB[0] eq "オウガヘルム"){$WN_sA[1]+=3000;$WN_sA[4]-=80;}

#		if($WN_sA[7] =~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!52/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!52/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!52/))){$WN_sA[2]+=25;$WN_sA[4]+=120;}#魔導器
#		if($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sB[0] eq "死霊の指輪" && (($WN_sC[0] eq "死神の甲冑" || $WN_sC[0] eq "スカルマスク") || ($WN_sD2[0] eq "死神の甲冑" || $WN_sD2[0] eq "スカルマスク"))){$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sC[0] eq "死霊の指輪" && (($WN_sB[0] eq "死神の甲冑" || $WN_sB[0] eq "スカルマスク") || ($WN_sD2[0] eq "死神の甲冑" || $WN_sD2[0] eq "スカルマスク"))){$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sD2[0] eq "死霊の指輪" && (($WN_sC[0] eq "死神の甲冑" || $WN_sC[0] eq "スカルマスク") || ($WN_sB[0] eq "死神の甲冑" || $WN_sB[0] eq "スカルマスク"))){$WN_sA[4]-=40;$$SO+=4;}
#		if($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sB[0] eq "死霊の指輪" && $WN_sC[0] eq "死神の甲冑" && $WN_sD2[0] eq "スカルマスク"){$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sB[0] eq "死霊の指輪" && $WN_sD2[0] eq "死神の甲冑" && $WN_sC[0] eq "スカルマスク"){$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sC[0] eq "死霊の指輪" && $WN_sB[0] eq "死神の甲冑" && $WN_sD2[0] eq "スカルマスク"){$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sC[0] eq "死霊の指輪" && $WN_sD2[0] eq "死神の甲冑" && $WN_sB[0] eq "スカルマスク"){$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sD2[0] eq "死霊の指輪" && $WN_sB[0] eq "死神の甲冑" && $WN_sC[0] eq "スカルマスク"){$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}
#		elsif($WN_sA[7]=~ m/!52/ && $WN_sA[0] eq "ダグザハンマー" && $WN_sD2[0] eq "死霊の指輪" && $WN_sC[0] eq "死神の甲冑" && $WN_sB[0] eq "スカルマスク"){$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}

#		if($WN_sA[7] =~ m/!53/ && $WN_sA[0] eq "シャーウッド" && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!53/ && $WN_sC[7] !~ m/!16/ && $WN_sD2[7] !~ m/!16/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!53/ && $WN_sD2[7] !~ m/!16/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!53/))){$WN_sA[1]-=1200;$WN_sA[3]+=6;}#狩人
#		if($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sB[0] eq "フォレストブーツ" && (($WN_sC[0] eq "グリンサーコート" || $WN_sC[0] eq "ウッドブランチ") || ($WN_sD2[0] eq "グリンサーコート" || $WN_sD2[0] eq "ウッドブランチ"))){$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sC[0] eq "フォレストブーツ" && (($WN_sB[0] eq "グリンサーコート" || $WN_sB[0] eq "ウッドブランチ") || ($WN_sD2[0] eq "グリンサーコート" || $WN_sD2[0] eq "ウッドブランチ"))){$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sD2[0] eq "フォレストブーツ" && (($WN_sC[0] eq "グリンサーコート" || $WN_sC[0] eq "ウッドブランチ") || ($WN_sB[0] eq "グリンサーコート" || $WN_sB[0] eq "ウッドブランチ"))){$WN_sA[4]-=20;}
#		if($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sB[0] eq "フォレストブーツ" && $WN_sC[0] eq "グリンサーコート" && $WN_sD2[0] eq "ウッドブランチ"){$WN_sA[2]+=20;$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sB[0] eq "フォレストブーツ" && $WN_sD2[0] eq "グリンサーコート" && $WN_sC[0] eq "ウッドブランチ"){$WN_sA[2]+=20;$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sC[0] eq "フォレストブーツ" && $WN_sB[0] eq "グリンサーコート" && $WN_sD2[0] eq "ウッドブランチ"){$WN_sA[2]+=20;$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sC[0] eq "フォレストブーツ" && $WN_sD2[0] eq "グリンサーコート" && $WN_sB[0] eq "ウッドブランチ"){$WN_sA[2]+=20;$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sD2[0] eq "フォレストブーツ" && $WN_sB[0] eq "グリンサーコート" && $WN_sC[0] eq "ウッドブランチ"){$WN_sA[2]+=20;$WN_sA[4]-=20;}
#		elsif($WN_sA[7]=~ m/!53/ && $WN_sA[0] eq "シャーウッド" && $WN_sD2[0] eq "フォレストブーツ" && $WN_sC[0] eq "グリンサーコート" && $WN_sB[0] eq "ウッドブランチ"){$WN_sA[2]+=20;$WN_sA[4]-=20;}

#		if($WN_sA[7] =~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!54/ && $WN_sC[7] !~ m/!12/ && $WN_sD2[7] !~ m/!12/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!54/ && $WN_sD2[7] !~ m/!12/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!54/))){$WN_sA[1]*=70;$WN_sA[2]*=2;$WN_sA[3]-=9;$WN_sA[4]*=6;}#握りッセ
#		if($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sB[0] eq "むずがゆい小手" && (($WN_sC[0] eq "汗くさい甲冑" || $WN_sC[0] eq "ヌメヌメする兜") || ($WN_sD2[0] eq "汗くさい甲冑" || $WN_sD2[0] eq "ヌメヌメする兜"))){$WN_sA[4]=int($WN_sA[4]*0.8);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sC[0] eq "むずがゆい小手" && (($WN_sB[0] eq "汗くさい甲冑" || $WN_sB[0] eq "ヌメヌメする兜") || ($WN_sD2[0] eq "汗くさい甲冑" || $WN_sD2[0] eq "ヌメヌメする兜"))){$WN_sA[4]=int($WN_sA[4]*0.8);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sD2[0] eq "むずがゆい小手" && (($WN_sC[0] eq "汗くさい甲冑" || $WN_sC[0] eq "ヌメヌメする兜") || ($WN_sB[0] eq "汗くさい甲冑" || $WN_sB[0] eq "ヌメヌメする兜"))){$WN_sA[4]=int($WN_sA[4]*0.8);}
#		if($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sB[0] eq "むずがゆい小手" && $WN_sC[0] eq "汗くさい甲冑" && $WN_sD2[0] eq "ヌメヌメする兜"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sB[0] eq "むずがゆい小手" && $WN_sD2[0] eq "汗くさい甲冑" && $WN_sC[0] eq "ヌメヌメする兜"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sC[0] eq "むずがゆい小手" && $WN_sB[0] eq "汗くさい甲冑" && $WN_sD2[0] eq "ヌメヌメする兜"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sC[0] eq "むずがゆい小手" && $WN_sD2[0] eq "汗くさい甲冑" && $WN_sB[0] eq "ヌメヌメする兜"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sD2[0] eq "むずがゆい小手" && $WN_sB[0] eq "汗くさい甲冑" && $WN_sC[0] eq "ヌメヌメする兜"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!54/ && $WN_sA[0] eq "にぎりがくさい剣" && $WN_sD2[0] eq "むずがゆい小手" && $WN_sC[0] eq "汗くさい甲冑" && $WN_sB[0] eq "ヌメヌメする兜"){$WN_sA[4]=int($WN_sA[4]*0.5);}

		#セット装備の値計算
		#超神聖セット
		$SetPointA = 0;
		if($WN_sA[0] eq "オラシオン" && ($WN_sB[0] eq "聖者の盾" || $WN_sC[0] eq "聖者の盾" || $WN_sD2[0] eq "聖者の盾")){$SetPointA = $SetPointA + 50;}
		if($WN_sA[0] eq "オラシオン" && ($WN_sB[0] eq "サザンクロス" || $WN_sC[0] eq "サザンクロス" || $WN_sD2[0] eq "サザンクロス")){$SetPointA = $SetPointA + 50;}
		if($WN_sA[0] eq "オラシオン" && ($WN_sB[0] eq "フロイデヘルム" || $WN_sC[0] eq "フロイデヘルム" || $WN_sD2[0] eq "フロイデヘルム")){$SetPointA = $SetPointA + 50;}

		#オウガセット
		$SetPointB = 0;
		if($WN_sA[0] eq "オウガブレード" && ($WN_sB[0] eq "オウガシールド" || $WN_sC[0] eq "オウガシールド" || $WN_sD2[0] eq "オウガシールド")){$SetPointB = $SetPointB + 50;}
		if($WN_sA[0] eq "オウガブレード" && ($WN_sB[0] eq "オウガアーマー" || $WN_sC[0] eq "オウガアーマー" || $WN_sD2[0] eq "オウガアーマー")){$SetPointB = $SetPointB + 50;}
		if($WN_sA[0] eq "オウガブレード" && ($WN_sB[0] eq "オウガヘルム" || $WN_sC[0] eq "オウガヘルム" || $WN_sD2[0] eq "オウガヘルム")){$SetPointB = $SetPointB + 50;}

		#暗黒魔道器セット
		$SetPointC = 0;
		if($WN_sA[0] eq "ダグザハンマー" && ($WN_sB[0] eq "死霊の指輪" || $WN_sC[0] eq "死霊の指輪" || $WN_sD2[0] eq "死霊の指輪")){$SetPointC = $SetPointC + 50;}
		if($WN_sA[0] eq "ダグザハンマー" && ($WN_sB[0] eq "死神の甲冑" || $WN_sC[0] eq "死神の甲冑" || $WN_sD2[0] eq "死神の甲冑")){$SetPointC = $SetPointC + 50;}
		if($WN_sA[0] eq "ダグザハンマー" && ($WN_sB[0] eq "スカルマスク" || $WN_sC[0] eq "スカルマスク" || $WN_sD2[0] eq "スカルマスク")){$SetPointC = $SetPointC + 50;}

		#狩人セット
		$SetPointD = 0;
		if($WN_sA[0] eq "シャーウッド" && ($WN_sB[0] eq "フォレストブーツ" || $WN_sC[0] eq "フォレストブーツ" || $WN_sD2[0] eq "フォレストブーツ")){$SetPointD = $SetPointD + 50;}
		if($WN_sA[0] eq "シャーウッド" && ($WN_sB[0] eq "グリンサーコート" || $WN_sC[0] eq "グリンサーコート" || $WN_sD2[0] eq "グリンサーコート")){$SetPointD = $SetPointD + 50;}
		if($WN_sA[0] eq "シャーウッド" && ($WN_sB[0] eq "ウッドブランチ" || $WN_sC[0] eq "ウッドブランチ" || $WN_sD2[0] eq "ウッドブランチ")){$SetPointD = $SetPointD + 50;}

		#にぎりセット
		$SetPointE = 0;
		if($WN_sA[0] eq "にぎりがくさい剣" && ($WN_sB[0] eq "むずがゆい小手" || $WN_sC[0] eq "むずがゆい小手" || $WN_sD2[0] eq "むずがゆい小手")){$SetPointE = $SetPointE + 50;}
		if($WN_sA[0] eq "にぎりがくさい剣" && ($WN_sB[0] eq "汗くさい甲冑" || $WN_sC[0] eq "汗くさい甲冑" || $WN_sD2[0] eq "汗くさい甲冑")){$SetPointE = $SetPointE + 50;}
		if($WN_sA[0] eq "にぎりがくさい剣" && ($WN_sB[0] eq "ヌメヌメする兜" || $WN_sC[0] eq "ヌメヌメする兜" || $WN_sD2[0] eq "ヌメヌメする兜")){$SetPointE = $SetPointE + 50;}

		if($SetPointA >= 50){$WN_sA[1]+=5500;$WN_sA[2]-=2;$WN_sA[4]+=110;}#超神聖 Lv1
		if($SetPointA >= 100){$WN_sA[2]+=22;$WN_sA[4]-=70;}#超神聖 Lv2
		if($SetPointA >= 150){$WN_sA[1]+=4000;$WN_sA[4]-=70;}#超神聖 Lv3

		if($SetPointB >= 50){$WN_sA[2]+=48;$WN_sA[4]+=80;}#鬼セLv1
		if($SetPointB >= 100){$WN_sA[1]+=3000;$WN_sA[4]-=40;}#鬼セLv2
		if($SetPointB >= 150){$WN_sA[1]+=5000;$WN_sA[4]-=80;}#鬼セLv3

		if($SetPointC >= 50){$WN_sA[2]+=25;$WN_sA[4]+=120;}#魔導器Lv1
		if($SetPointC >= 100){$WN_sA[4]-=40;$$SO+=4;}#魔導器Lv2
		if($SetPointC >= 150){$$WN_sA[2]+=8;$WN_sA[4]-=40;$$SO+=4;}#魔導器Lv3

		if($SetPointD >= 50){$WN_sA[1]-=1200;$WN_sA[3]+=6;}#狩人Lv1
		if($SetPointD >= 100){$WN_sA[1]+=100;$WN_sA[4]-=20;}#狩人Lv2
		if($SetPointD >= 150){$WN_sA[1]+=100;$WN_sA[2]+=10;$WN_sA[4]-=40;}#狩人Lv3

		if($SetPointE >= 50){$WN_sA[1]*=70;$WN_sA[2]*=2;$WN_sA[3]-=9;$WN_sA[4]*=6;}#握りセットLv1
		if($SetPointE >= 100){$WN_sA[4]=int($WN_sA[4]*0.8);}#握りセットLv2
		if($SetPointE >= 150){$WN_sA[4]=int($WN_sA[4]*0.5);}#握りセットLv3


#		if($WN_sA[7] =~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!55/ && $WN_sC[7] !~ m/!12/ && $WN_sD2[7] !~ m/!12/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!55/ && $WN_sD2[7] !~ m/!12/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!55/))){$WN_sA[1]*=4;$WN_sA[4]*=5;}#お菓子
#		if($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sB[0] eq "チョコレートの盾" && (($WN_sC[0] eq "砂糖菓子のヨロイ" || $WN_sC[0] eq "キャンディヘルム") || ($WN_sD2[0] eq "砂糖菓子のヨロイ" || $WN_sD2[0] eq "キャンディヘルム"))){$WN_sA[4]=int($WN_sA[4]*0.8);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sC[0] eq "チョコレートの盾" && (($WN_sB[0] eq "砂糖菓子のヨロイ" || $WN_sB[0] eq "キャンディヘルム") || ($WN_sD2[0] eq "砂糖菓子のヨロイ" || $WN_sD2[0] eq "キャンディヘルム"))){$WN_sA[4]=int($WN_sA[4]*0.8);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sD2[0] eq "チョコレートの盾" && (($WN_sC[0] eq "砂糖菓子のヨロイ" || $WN_sC[0] eq "キャンディヘルム") || ($WN_sB[0] eq "砂糖菓子のヨロイ" || $WN_sB[0] eq "キャンディヘルム"))){$WN_sA[4]=int($WN_sA[4]*0.8);}
#		if($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sB[0] eq "チョコレートの盾" && $WN_sC[0] eq "砂糖菓子のヨロイ" && $WN_sD2[0] eq "キャンディヘルム"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sB[0] eq "チョコレートの盾" && $WN_sD2[0] eq "砂糖菓子のヨロイ" && $WN_sC[0] eq "キャンディヘルム"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sC[0] eq "チョコレートの盾" && $WN_sB[0] eq "砂糖菓子のヨロイ" && $WN_sD2[0] eq "キャンディヘルム"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sC[0] eq "チョコレートの盾" && $WN_sD2[0] eq "砂糖菓子のヨロイ" && $WN_sB[0] eq "キャンディヘルム"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sD2[0] eq "チョコレートの盾" && $WN_sB[0] eq "砂糖菓子のヨロイ" && $WN_sC[0] eq "キャンディヘルム"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		elsif($WN_sA[7]=~ m/!55/ && $WN_sA[0] eq "シュガーケーン" && $WN_sD2[0] eq "チョコレートの盾" && $WN_sC[0] eq "砂糖菓子のヨロイ" && $WN_sB[0] eq "キャンディヘルム"){$WN_sA[4]=int($WN_sA[4]*0.5);}
#		if($WN_sA[7] =~ m/!55/){$WN_sA[4]=10;}
#		$oka = 0;
#		if($WN_sA[7]=~ m/!55/){$oka=$oka+1;}
#		if($WN_sB[7]=~ m/!55/){$oka=$oka+1;}
#		if($WN_sC[7]=~ m/!55/){$oka=$oka+1;}
#		if($WN_sD2[7]=~ m/!55/){$oka=$oka+1;}

#		if($oka == 2){$WN_sA[4]=int($WN_sA[4]*0.5);}

		if($WN_sA[7] =~ m/!57/ && (($WN_sB[1] <= 20 && $WN_sB[7]=~ m/!58/) || ($WN_sC[1] <= 20 && $WN_sC[7]=~ m/!58/) || ($WN_sD2[1] <= 20 && $WN_sD2[7]=~ m/!58/))){$WN_sA[1]+=6000;$WN_sA[2]-=20;$WN_sA[4]+=100;}#恋人
	}

#エンチャントシステム
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
#	if($WA34 ne ""){$WN_sA[7] .= "!ENTCRI00$WA34";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA35 ne ""){$WN_sA[7] .= "!ENTCRI00$WA35";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA36 ne ""){$WN_sA[7] .= "!ENTCRI00$WA36";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA37 ne ""){$WN_sA[7] .= "!ENTCRI00$WA37";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA38 ne ""){$WN_sA[7] .= "!ENTCRI00$WA38";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA39 ne ""){$WN_sA[7] .= "!ENTCRI00$WA39";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA40 ne ""){$WN_sA[7] .= "!ENTCRI00$WA40";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA41 ne ""){$WN_sA[7] .= "!ENTCRI00$WA41";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}
#	if($WA42 ne ""){$WN_sA[7] .= "!ENTCRI00$WA42";$WN_sA[7] =~ s/!ENTCRI0010/!ENTCRI010/g;}


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
	if($Ent_D > 0 && $Ent_D <= 2){$WN_sD2[0] = "<font color=00ff00>$WN_sD2[0]</font>";}
	elsif($Ent_D > 2 && $Ent_D <= 4){$WN_sD2[0] = "<font color=ffff00>$WN_sD2[0]</font>";}
	elsif($Ent_D > 4){$WN_sD2[0] = "<font color=ffD700>$WN_sD2[0]</font>";}
	

	if($WAEnt ne "" && $WAEnt > 0){$WN_sA[0] = "＋$WAEnt $WN_sA[0]";}
	if($WBEnt ne "" && $WBEnt > 0){$WN_sB[0] = "＋$WBEnt $WN_sB[0]";}
	if($WCEnt ne "" && $WCEnt > 0){$WN_sC[0] = "＋$WCEnt $WN_sC[0]";}
	if($WDEnt ne "" && $WDEnt > 0){$WN_sD2[0] = "＋$WDEnt $WN_sD2[0]";}
	if($WSEnt ne "" && $WSEnt > 0){$WN_sS[0] = "＋$WSEnt $WN_sS[0]";}
	if($WTEnt ne "" && $WTEnt > 0){$WN_sT[0] = "＋$WTEnt $WN_sT[0]";}
	if($WUEnt ne "" && $WUEnt > 0){$WN_sU[0] = "＋$WUEnt $WN_sU[0]";}
	



##技を最上段に設置している場合の表示変更	※武器を装備している場合　且つ、武器と技属性が一致している場合に限り
	$flg_tekiyo = 0;
	if($WN_sS[11] eq "5"){
		if($WN_sA[12] =~ m/e001/ && $WN_sS[12] =~ m/e001/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e002/ && $WN_sS[12] =~ m/e002/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e003/ && $WN_sS[12] =~ m/e003/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e004/ && $WN_sS[12] =~ m/e004/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e005/ && $WN_sS[12] =~ m/e005/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e006/ && $WN_sS[12] =~ m/e006/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e007/ && $WN_sS[12] =~ m/e007/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e008/ && $WN_sS[12] =~ m/e008/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e009/ && $WN_sS[12] =~ m/e009/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e010/ && $WN_sS[12] =~ m/e010/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e011/ && $WN_sS[12] =~ m/e011/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e012/ && $WN_sS[12] =~ m/e012/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e013/ && $WN_sS[12] =~ m/e013/){$flg_tekiyo = 1;}
		if($WN_sA[12] =~ m/e014/ && $WN_sS[12] =~ m/e014/){$flg_tekiyo = 1;}

#		&ERROR("$flg_tekiyo");

		if($flg_tekiyo eq "1"){
			#攻撃力　ここでは、回数補正なし版の計算
			if($WN_sS[12] !~ m/ef001/){
				$WN_sS[1]=int($WN_sA[1] * ($WN_sS[1]/1000));
			}
			#命中
			$WN_sS[2]=int($WN_sA[2] + $WN_sS[2]);
			#回数　回数補正有り時のみ　　攻撃力の計算も行う
			if($WN_sS[12] =~ m/ef001/){

				$CalcA=int($WN_sA[1]*$WN_sA[3]);
#				$WN_sA[3] = $WN_sS[3];
				$CalcA=$CalcA/$WN_sS[3];
				$WN_sS[1]=int($CalcA * ($WN_sS[1]/1000));

			}else{
				#武器攻撃回数を引き継ぐ
				$WN_sS[3] = $WN_sA[3];

			}
			#MP加算
			$WN_sS[4]=$WN_sA[4]+$WN_sS[4];

		}else{

			#ブラスト用
			if($WN_sS[12] =~ m/ef001/ && $WN_sS[0] ne "ソ\ニックブラスト"){
#			if($WN_sS[12] =~ m/ef001/){
				$WN_sS[1]=int($WN_sS[1]/$WN_sS[3]);
			}

		}

	}

#装備品強化システム
#	if($WAEnt ne "" && $WAEnt > 0){$WN_sA[0] = "＋$WAEnt $WN_sA[0]";}
#	if($WBEnt ne "" && $WBEnt > 0){$WN_sB[0] = "＋$WBEnt $WN_sB[0]";}
#	if($WCEnt ne "" && $WCEnt > 0){$WN_sC[0] = "＋$WCEnt $WN_sC[0]";}
#	if($WDEnt ne "" && $WDEnt > 0){$WN_sD2[0] = "＋$WDEnt $WN_sD2[0]";}
#	if($WSEnt ne "" && $WSEnt > 0){$WN_sS[0] = "＋$WSEnt $WN_sS[0]";}
#	if($WTEnt ne "" && $WTEnt > 0){$WN_sT[0] = "＋$WTEnt $WN_sT[0]";}
#	if($WUEnt ne "" && $WUEnt > 0){$WN_sU[0] = "＋$WUEnt $WN_sU[0]";}


	if($WAEnt ne "" && $WAEnt > 0){
		#武器の場合
		if($WN_sA[14] =~ m/A02/){
			#杖以外
			if($WN_sA[14] =~ m/A02/ && $WN_sA[14] !~ m/A15/){
				$WN_sA[1] = $WN_sA[1] + int(30 * $WAEnt / $WN_sA[3]);
				$WN_sA[2] = $WN_sA[2] + int(1 * $WAEnt/5);
				$WN_sA[4] = $WN_sA[4] - int(2 * $WAEnt/10);
				if($WN_sA[4] < 40){$WN_sA[4] = 40;}
			#杖
			}elsif($WN_sA[14] =~ m/A02/ && $WN_sA[14] =~ m/A15/){
				$WN_sA[1] = $WN_sA[1] + int(10 * $WAEnt / $WN_sA[3]);
				$WN_sA[2] = $WN_sA[2] + int(1 * $WAEnt/5);
				$WN_sA[4] = $WN_sA[4] - int(2 * $WAEnt/10);
				if($WN_sA[4] < 40){$WN_sA[4] = 40;}
			}
		#盾 等々は現状は不要　元から表示を行っていない
#		}elsif($WN_sA[14] =~ m/A29/){
		}
	}

	&HEADER(Status);

		if($ALY_CLASS[13] <= 35){$ALI='C';}
		elsif($ALY_CLASS[12] > 35 && $ALY_CLASS[13] <= 71){$ALI='N';}
		elsif($ALY_CLASS[12] > 71){$ALI='L';}
		elsif($ALY_CLASS[12] >= 0 && $ALY_CLASS[13] <= 71){$ALI='N･C';}
		elsif($ALY_CLASS[12] > 35){$ALI='L･N';}
		else{$ALI='L･N･C';}

		if($ALY_CLASS[5]){
			if($ALY_CLASS[10] > 0){$ALI = $ALI."、HP…$ALY_CLASS[10]";
				if($ALY_CLASS[10] < 80000){$ALI = $ALI.'以上';}
			}
			if($ALY_CLASS[11] > 0){$ALI = $ALI."、MP…$ALY_CLASS[11]";
				if($ALY_CLASS[11] < 4000){$ALI = $ALI.'以上';}
			}
			if($ALY_CLASS[6] > 0){$ALI = $ALI.'、STR…'.&STATUS_CONVERT("$ALY_CLASS[6]",'s');
				if($ALY_CLASS[6] < 50){$ALI = $ALI.'以上';}
			}
			if($ALY_CLASS[7] > 0){$ALI = $ALI.'、VIT…'.&STATUS_CONVERT("$ALY_CLASS[7]",'s');
				if($ALY_CLASS[7] < 50){$ALI = $ALI.'以上';}
			}
			if($ALY_CLASS[8] > 0){$ALI = $ALI.'、AGI…'.&STATUS_CONVERT("$ALY_CLASS[8]",'s');
				if($ALY_CLASS[8] < 50){$ALI = $ALI.'以上';}
			}
			if($ALY_CLASS[9] > 0){$ALI = $ALI.'、DEX…'.&STATUS_CONVERT("$ALY_CLASS[9]",'s');
				if($ALY_CLASS[9] < 50){$ALI = $ALI.'以上';}
			}
			if($ALY_CLASS[14] > 0){
				if($ALY_CLASS[14] >= 1100){$AMA=$ALY_CLASS[14]-1000;$AMA="+$AMA"}
				$ALI = $ALI.'、熟練度…'.&STATUS_CONVERT("$ALY_CLASS[14]",'j')."$AMA以上";
			}
			if($ALY_CLASS[21]){$ALI = $ALI.'、指揮…'.&STATUS_CONVERT("$ALY_CLASS[21]",'z').'以上';}
			if($ALY_CLASS[20]){$ALY_CLASS[20]-=200;$ALI = $ALI."、熟練度がDになってからの撃破数が$ALY_CLASS[20]以下";}
			if($ALY_CLASS[15]){
				if($ALY_CLASS[15] =~ /!1b/i){$ALY_CLASS[15]="銃";}
				if($ALY_CLASS[15] =~ /!6e/i){$ALY_CLASS[15]="ブラスト攻撃";}
				$ALI = $ALI."、装備…$ALY_CLASS[15]";
			}
		}

if($ALY_CLASS[1]){if($ALY_CLASS[1]>0){$ALY_CLASS[1]="+$ALY_CLASS[1]"};$HOSEI = $HOSEI."攻$ALY_CLASS[1]&nbsp;";}
if($ALY_CLASS[2]){if($ALY_CLASS[2]<0){$ALY_CLASS[2]=int($ALY_CLASS[2]/2-0.5);}if($ALY_CLASS[2]>0){$ALY_CLASS[2]=int($ALY_CLASS[2]/2+0.5);$ALY_CLASS[2]="+$ALY_CLASS[2]"};$HOSEI = $HOSEI."防$ALY_CLASS[2]&nbsp;";}
if($ALY_CLASS[3]){if($ALY_CLASS[3]>0){$ALY_CLASS[3]="+$ALY_CLASS[3]"};$HOSEI = $HOSEI."避$ALY_CLASS[3]&nbsp;";}
if($ALY_CLASS[4]){if($ALY_CLASS[4]>0){$ALY_CLASS[4]="+$ALY_CLASS[4]"};$HOSEI = $HOSEI."命$ALY_CLASS[4]&nbsp;";}
if($ALY_CLASS[17]){
	@tokuclass = split(/!/,$ALY_CLASS[17]);
	foreach $j(@tokuclass){$tokuarray .= $VCLTO_LIST{"$j"}."&nbsp";}
	$HOSEI .= "$tokuarray";
}
if(!$ALY_CLASS[1] && !$ALY_CLASS[2] && !$ALY_CLASS[3] && !$ALY_CLASS[4] && !$ALY_CLASS[17]){$HOSEI = '無し'}

print << "-----END-----";
	<table width=100% height=100% id="clas1" style="position:absolute;visibility:hidden;"><tr><td align=center>
	<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr>
	<td style="background-color:$TABLE_COLOR2;padding:3px;"><b>$ALY_CLASS[0]</b></td>
	<td align="right" style="background-color:$TABLE_COLOR2;"><a href="Javascript:hideclas1();"><b>×</b></a></td></tr>
	<tr>
	<td width="300" colspan="2" style="padding:5px;">

	<table style="font-size:12px;">
		<tr><td><b>クラスチェンジ条件</b></td><td rowspan="3"><img src="$IMG_FOLDER5/$ALY_CLASS[18]" style="border:none;width:64;height:64;" align="right"></td></tr>
		<tr><td style="padding-left:10px;">アラインメント…$ALI</td></tr>
		<tr><td style="padding-left:10px;padding-top:10px;padding-bottom:10px;padding-top:10px;">補正…$HOSEI</td></tr>
		<tr><td colspan="2">$ALY_CLASS[19]</td></tr>
	</table>

	</td>
	</tr></table>
	</td></tr></table>

-----END-----

print << "-----END-----";
	<table width=100% height=100% id="claspl1" style="position:absolute;visibility:hidden;"><tr><td align=center>
	<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr>
	<td style="background-color:$TABLE_COLOR2;padding:3px;"><b>"テスト"</b></td>
	<td align="right" style="background-color:$TABLE_COLOR2;"><a href="Javascript:hideclaspl1();"><b>×</b></a></td></tr>
	<tr>
	<td width="300" colspan="2" style="padding:5px;">

	<table style="font-size:12px;">
		<tr><td><b>ステータス</b></td><td rowspan="3"><img src="$IMG_FOLDER5/$ALY_CLASS[18]" style="border:none;width:64;height:64;" align="right"></td></tr>
		<tr><td style="padding-left:10px;">アラインメント…$ALI</td></tr>
		<tr><td style="padding-left:10px;padding-top:10px;padding-bottom:10px;padding-top:10px;">補正…$HOSEI</td></tr>
		<tr><td colspan="2">$ALY_CLASS[19]</td></tr>
	</table>

	</td>
	</tr></table>
	</td></tr></table>

-----END-----

	$RHP=int($PL_VALUES[15]/$PL_VALUES[16]*100);$ZHP=100-$RHP;
	$RMP=int($PL_VALUES[17]/$PL_VALUES[18]*100);$ZMP=100-$RMP;
#	print "<a name=#top></a><table border=0 cellspacing=0 cellpadding=0 height=100% bgcolor=\"$BG_STATUS\"><tr><td>&nbsp;</td><td><span style=\"font-size:3pt;\"><br></span>";
#	print "<table border=0 cellspacing=0 cellpadding=0><tr><td rowspan=2> ";
#	print "</td><td rowspan=2 valign=top><table border=0 cellspacing=0 cellpadding=0>";

	print "<a name=#top></a><table border=0 cellspacing=0 cellpadding=0 height=100% bgcolor=\"$BG_STATUS\"><tr><td>&nbsp;</td><td><span style=\"font-size:3pt;\"><br></span>";
	print "<table border=0 cellspacing=0 cellpadding=0><tr><td rowspan=2> ";
	print "<table border=0 cellspacing=0 cellpadding=0><tr><img src=\"$IMG_FOLDER7/$PL_VALUES[40].gif\" width=\"64\" height=\"96\"></tr></table>";
	print "</td><td rowspan=2 valign=top><table border=0 cellspacing=0 cellpadding=0>";


	print "<tr><td class=td3 nowrap align=center><b>ALI</b></td>";
	print "<td class=td3 nowrap align=center><b>ELE</b></td></tr>";
	print "<tr><td class=td2 nowrap align=center><small>".&STATUS_CONVERT("$PL_VALUES[12]",'a')."</small></td>";
	print "<td class=td2 nowrap align=center>".&STATUS_CONVERT("$PL_VALUES[31]",'e')."</td></tr>";

#	print "<tr class=td3 nowrap align=center><b>陣形</b></tr>";
#	print "<tr class=td2 nowrap align=center><small>フリーファイト</small></tr>";
#	print "<tr><td class=td3 nowrap align=center><b>陣形</b></td></tr>";
#	print "<tr><td class=td2 nowrap align=center><small>フリーファイト</small></td></tr>";

#MVPとChainは未実装で！

#	print "<tr><td class=td3 nowrap align=center><b>MVP</b></td>";
#	print "<td class=td3 nowrap align=center><b>Chain</b></td></tr>";
#	print "<tr><td class=td2 nowrap align=center><small>0</small></td>";
#	print "<td class=td2 nowrap align=center><small>0</small></td></tr>";

	print "<tr><td class=td3 nowrap align=center><b>熟練度</b></td>";
	print "<td class=td3 nowrap align=center><b>RISK</b></td></tr>";
	print "<tr><td class=td2 nowrap align=center>".&STATUS_CONVERT("$PL_VALUES[24]",'j')."</td>";
	print "<td class=td2 nowrap align=center><small><span id=risk></span></small></td></tr>";

	if($PL_VALUES[32] > 9){
		print "<tr><td rowspan=2 class=td2 nowrap align=center><span id=cond>$CONDITIONAL</span><br><span id=ato style=\"font-size:10px;\"></span></td><td class=td3 nowrap align=center><b>指揮</b></td></tr>";
		print "<tr><td class=td2 nowrap align=center><small>".&STATUS_CONVERT("$PL_VALUES[32]",'z')."</small></td></tr>";
	}else{
		print "<tr><td rowspan=2 colspan=2 class=td2 nowrap align=center><span id=cond>$CONDITIONAL</span><br><span id=ato style=\"font-size:10px;\"></span></td></tr>";
	}

	if($PL_VALUES[27]>700){$PSIZE='72';}else{$PSIZE='64';}
	$PL_VALUES[5]="$NONE_NATIONALITY" if !$PL_VALUES[5];
	print "</table></td><td class=td2 nowrap align=center  COLSPAN=2><img src=\"$IMG_FOLDER2/$PL_VALUES[27].gif\" width=\"$PSIZE\" height=\"$PSIZE\"></td>";
	print "<td class=td2 nowrap align=center>&nbsp;&nbsp;<font style=\"color:$CL_VALUES[0];font-size:15px;\">($PL_VALUES[5])&nbsp;".&RANK("$PL_VALUES[0]","$PL_VALUES[5]","$PL_VALUES[6]")."";
	print "&nbsp;&nbsp;<br>&nbsp;&nbsp;$PL_VALUES[28]" if $PL_VALUES[28];
	print "</font>&nbsp;&nbsp;<br>&nbsp;&nbsp;<span style=\"color:$PL_VALUES[13];font-size:20px;\">$FORM{pname}</span>&nbsp;&nbsp;</td>";
#	print "</font>&nbsp;&nbsp;<br>&nbsp;&nbsp;<a href=\"Javascript:showclaspl1();\"><span style=\"color:$PL_VALUES[13];font-size:20px;\">$FORM{pname}</span></a>&nbsp;&nbsp;</td>";
#<a href=\"Javascript:showclaspl1();\">
	print "<td class=td2 nowrap rowspan=2><table border=0 cellspacing=0 cellpadding=0>";
	print "<tr><td style=\"font-size:6px;\" nowrap colspan=10><b id=hpb><img src=\"$IMG_FOLDER1/hpb.gif\" width=\"$RHP%\" height=\"7\"><img src=\"$IMG_FOLDER1/zhb.gif\" width=\"$ZHP%\" height=\"7\"></b></td></tr>";

	print "<tr><td class=td3 nowrap align=center><b>$STATUS_NAME[4]</b></td><td class=td2 nowrap align=right>&nbsp;&nbsp;<b id=j_hp>$PL_VALUES[15]</b></td>";
	print "<td class=td3 nowrap align=center><b>$STATUS_NAME[5]</b></td><td class=td2 nowrap align=right>&nbsp;&nbsp;<b id=j_en>$PL_VALUES[17]</b>";
	print "<td class=td3 nowrap align=center><font color=#DDA7BC><b>$STATUS_NAME[0]</b></font></td><td class=td4 nowrap align=center width=\"50\">".&STATUS_CONVERT("$PL_VALUES[19]",'s');
	$STR=$PL_VALUES[19]*2-2;$STRZ=(50-$PL_VALUES[19])*2;
	print "<br><img src=\"$IMG_FOLDER1/str.gif\" width=\"$STR%\" height=\"4\"><img src=\"$IMG_FOLDER1/szb.gif\" width=\"$STRZ%\" height=\"4\"></td></tr>";
#	print "<td class=td3 nowrap align=center><b>腕力</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[19]";
#	print "</td><td class=td3 nowrap align=center><b>知力</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[57]";
	print "</td></tr>";

	print "<tr><td class=td1 nowrap align=center>MAX</td><td class=td2 nowrap align=right>&nbsp;&nbsp;<b>$PL_VALUES[16]</b></td>";
	print "<td class=td1 nowrap align=center>&nbsp;MAX&nbsp;</td><td class=td2 nowrap align=right>&nbsp;&nbsp;<b>$PL_VALUES[18]</b></td>";
	print "<td class=td3 nowrap align=center><font color=#92B68D><b>$STATUS_NAME[1]</b></font></td><td class=td4 nowrap align=center width=\"50\">".&STATUS_CONVERT("$PL_VALUES[20]",'s');
	$VIT=$PL_VALUES[20]*2-2;$VITZ=(50-$PL_VALUES[20])*2;
	print "<br><img src=\"$IMG_FOLDER1/vit.gif\" width=\"$VIT%\" height=\"4\"><img src=\"$IMG_FOLDER1/szb.gif\" width=\"$VITZ%\" height=\"4\"></td></tr>";
#	print "<td class=td3 nowrap align=center><b>体力</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[20]";
#	print "</td><td class=td3 nowrap align=center><b>精神</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[58]";
	print "</td></tr>";

	print "<tr><td class=td3 nowrap align=center><b>Lv.</b></td><td class=td2 nowrap align=right><b>$PL_VALUES[29]</b></td>";
	print "<td class=td3 nowrap align=center><b>Exp</b></td><td class=td2 nowrap align=right>&nbsp;&nbsp;<b>$PL_VALUES[30]</b></td>";
	print "<td class=td3 nowrap align=center><font color=#E2D0A7><b>$STATUS_NAME[2]</b></font></td><td class=td4 nowrap align=center width=\"50\">".&STATUS_CONVERT("$PL_VALUES[21]",'s');
	$AGI=$PL_VALUES[21]*2-2;$AGIZ=(50-$PL_VALUES[21])*2;
	print "<br><img src=\"$IMG_FOLDER1/agi.gif\" width=\"$AGI%\" height=\"4\"><img src=\"$IMG_FOLDER1/szb.gif\" width=\"$AGIZ%\" height=\"4\"></td></tr>";
#	print "<td class=td3 nowrap align=center><b>素早さ</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[21]";
#	print "</td><td class=td3 nowrap align=center><b>魅力</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[59]";
	print "</td></tr>";

	print "<tr><td class=td3 nowrap align=center>Goth</td><td class=td2 nowrap align=right><b>$PL_VALUES[8]</b></td>";
	$NEXT=($PL_VALUES[29]+1)*200;
	print "<td class=td1 nowrap align=center>&nbsp;NEXT&nbsp;</td><td class=td2 nowrap align=right>&nbsp;&nbsp;<b>$NEXT</b></td>";
	print "<td class=td3 nowrap align=center><font color=#A1C3C2>&nbsp;<b>$STATUS_NAME[3]</b>&nbsp;</font></td><td class=td4 nowrap align=center width=\"50\">".&STATUS_CONVERT("$PL_VALUES[22]",'s');
	$AGH=$PL_VALUES[22]*2-2;$AGHZ=(50-$PL_VALUES[22])*2;
	print "<br><img src=\"$IMG_FOLDER1/agh.gif\" width=\"$AGH%\" height=\"4\"><img src=\"$IMG_FOLDER1/szb.gif\" width=\"$AGHZ%\" height=\"4\"></td></tr>";
#	print "<td class=td3 nowrap align=center><b>器用さ</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[22]";
#	print "</td><td class=td3 nowrap align=center><b>愛</b></td><td class=td4 nowrap align=center width=\"50\">$PL_VALUES[60]";
	print "</td></tr>";

	print "<tr><td style=\"font-size:6px;\" nowrap colspan=10><b id=mpb><img src=\"$IMG_FOLDER1/mpb.gif\" width=\"$RMP%\" height=\"7\"><img src=\"$IMG_FOLDER1/zhb.gif\" width=\"$ZMP%\" height=\"7\"></b></td></tr>";
	print "</table></td></tr>";
	print "<tr><td class=td3 style=\"font-size:12px;border:1px solid $TABLE_BORDER;\" nowrap align=center><span class=td3><b>$STATUS_NAME[6]</b></span></td><td style=\"font-size:12px;border:1px solid $TABLE_BORDER;\" nowrap align=center><a href=\"Javascript:showclas1();\"><font size=\"2\">$ALY_CLASS[0]</font></a></td><td class=td2 nowrap align=center>$PL_VALUES[3]</td></tr>";
	print "</table></td>";
	print "<td>&nbsp;</td></tr><tr><td>&nbsp;</td>";
	print "<td><table border=0 cellspacing=0 cellpadding=0 width=100%>";
	print "<tr><td style=\"font-size:12px;line-height:17px;\" valign=top nowrap width=50%>";

	$PL_VALUES[4]=71 if $CLASS_FRAG == 1;
	$PL_VALUES[4]=72 if $CLASS_FRAG == 2;
	$PL_VALUES[4]=64 if $CLASS_FRAG == 3;
	$PL_VALUES[4]=131 if $CLASS_FRAG == 4;
	$PL_VALUES[4]=132 if $CLASS_FRAG == 5;
	$PL_VALUES[4]=133 if $CLASS_FRAG == 6;
	$PL_VALUES[4]=134 if $CLASS_FRAG == 7;
	$PL_VALUES[4]=135 if $CLASS_FRAG == 8;
	$PL_VALUES[4]=203 if $CLASS_FRAG == 9;

#ここから装備
#	if($WN_sA[7]=~ m/!1d/ && ($WN_sB[7]=~ m/!1c/ || $WN_sC[7]=~ m/!1c/ || $WN_sD2[7]=~ m/!1c/)){
	if($ALY_CLASS[17] =~ m/!E011|!E012/ && $WN_sD[7]=~ m/!E0008/){
		print"<span class=td3>&nbsp;&nbsp;<b>装備</b>&nbsp;&nbsp;</span>&nbsp;<b>".$WN_sA[0]."</b>&nbsp;Lv.$WLV_D/exp.$WEP_D<br>";
		print "<span class=td3>&nbsp;&nbsp;性\能\&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sA[9].gif\">&nbsp;&nbsp;攻：".&STATUS_CONVERT($WN_sA[1]*(($WLV_D*0.003)+1)*$WN_sA[3]/500,'s')."&nbsp;（".&STATUS_CONVERT($WN_sA[1]*$WN_sA[3]/500,'s')."）&nbsp;命：".&STATUS_CONVERT($WN_sA[2]/4,'s')."&nbsp;&nbsp;回：$WN_sA[3]&nbsp;&nbsp;MP：$WN_sA[4]&nbsp;&nbsp;";
	}else{
		print"<span class=td3>&nbsp;&nbsp;<b>装備</b>&nbsp;&nbsp;</span>&nbsp;<b>".$WN_sA[0]."</b>&nbsp;Lv.$WLV_A/exp.$WEP_A<br>";
		print "<span class=td3>&nbsp;&nbsp;性\能\&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sA[9].gif\">&nbsp;&nbsp;攻：".&STATUS_CONVERT($WN_sA[1]*(($WLV_A*0.003)+1)*$WN_sA[3]/500,'s')."&nbsp;（".&STATUS_CONVERT($WN_sA[1]*$WN_sA[3]/500,'s')."）&nbsp;命：".&STATUS_CONVERT($WN_sA[2]/4,'s')."&nbsp;&nbsp;回：$WN_sA[3]&nbsp;&nbsp;MP：$WN_sA[4]&nbsp;&nbsp;";
	}
##特殊能力
#	foreach $j (@WN_sA_ef){
#		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
#		$tokusyu .= "<a href=\"Javascript:showclasy$j();\">$vijunu[0]</a>&nbsp;"if $j;
	$EntCnt = 0;
	foreach $j (@WN_sA_ef){
		$testcolor = $j;
		@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
		if($j =~ m/ENT/){
#			$tokusyu .= "<a href=\"Javascript:showclasy$j();\"><font color=00ff00>$vijunu[0]</font></a>&nbsp;"if $j;
			if($vijunu[0] ne ""){
				$tokusyuuniq .= "<a href=\"Javascript:showclasy$j();\"><font color=00ff00>$vijunu[0]</font></a>&nbsp;"if $j;
				$EntCnt = $EntCnt + 1;
				if($EntCnt > 6){
					$tokusyuuniq .= "<br><span class=td3>&nbsp;&nbsp;固有\&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
					$EntCnt = 0;
				}
			}else{
				$tokusyuuniq .= "<a href=\"Javascript:showclasy$j();\"><font color=00ff00>$vijunu[0]</font></a>"if $j;		
			}
		}else{
			$tokusyu .= "<a href=\"Javascript:showclasy$j();\">$vijunu[0]</a>&nbsp;"if $j;				
		}
print << "-----END-----"if $j;
	<table width=100% height=100% id="clas$j" style="position:absolute;visibility:hidden;top:26px;left:281px;"><tr><td align=center>
	<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr><td style="background-color:$TABLE_COLOR2;padding:3px;" colspan=2><b>$vijunu[0]</b></td>
	<td style="background-color:$TABLE_COLOR2;" colspan=2><a href="Javascript:hideclasy$j();"><b>×</b></a></td></tr>
	<tr><td width="300" colspan="2" style="padding:5px;">$vijunu[1]</td>
	</tr></table>
	</td></tr></table>
-----END-----
	}
#	print "$tokusyu";

##防具数値算出
	if($WN_sA[7]=~ m/!12/){$WNA=int($WN_sA[1]+$WEP_E/2475);print "RES+$WNA&nbsp;";}
	elsif($WN_sA[7]=~ m/!13/ && $WN_sA[7] =~ m/!00|!01|!02|!03|!04|!05/){$WNA=int($WN_sA[10]+$WEP_E/2475);
								$WNB=int($WN_sA[1]+$WEP_E/2475);
							print "STR+$WNA&nbsp;";print "DEX+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!13/){$WNA=int($WN_sA[10]+$WEP_E/4950);
								$WNB=int($WN_sA[1]+$WEP_E/4950);
							print "STR+$WNA&nbsp;";print "DEX+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!14/){$WNA=int($WN_sA[10]+$WEP_E/2475);$WNB=int($WN_sA[1]+$WEP_E/1650);print "STR+$WNA&nbsp;";print "INI+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!15|!19/ && $WN_sA[7] =~ m/!00|!01|!02|!03|!04|!05/){$WNA=int($WN_sA[10]+$WEP_E/2475);print "INT+$WNA&nbsp;";}
	elsif($WN_sA[7]=~ m/!15|!19/){$WNA=int($WN_sA[10]+$WEP_E/4950);print "INT+$WNA&nbsp;";}
	elsif($WN_sA[7]=~ m/!16/){$WNA=int($WN_sA[1]+$WEP_E/2475);print "AGI+$WNA&nbsp;";}
	elsif($WN_sA[7]=~ m/!17/){$WNA=int($WN_sA[1]+$WEP_E/2475);$WNB=int($WN_sA[10]+$WEP_E/2475);print "AGI+$WNA&nbsp;";print "DEX+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!1s/){$WNA=int($WN_sA[1]+$WEP_E/2475);print "RES+$WNA&nbsp;";}
	elsif($WN_sA[7]=~ m/!1t/){$WNA=int($WN_sA[1]+$WEP_E/2475);print "RES+$WNA&nbsp;";}
	elsif($WN_sA[7]=~ m/!E0003/){$WNA=int($WN_sA[1]+$WEP_E/2475);print "RES+$WNA&nbsp;";
								$WNB=int(3+$WEP_E/4950);print "STR+$WNB&nbsp;";
								$WNC=int(1+$WEP_E/4950);print "AGI+$WNC&nbsp;";
							}

	elsif($WN_sA[7]=~ m/!1u/){$WNA=int($WN_sA[1]+$WEP_E/2475);$WNB=int($WN_sA[1]/3+$WEP_E/2475);print "RES+$WNA&nbsp;";print "DEX+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!1v/){$WNA=int($WN_sA[1]+$WEP_E/2475);$WNB=int($WN_sA[10]+$WEP_E/2475);print "RES+$WNA&nbsp;";print "AGI+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!1w/){$WNA=int($WN_sA[1]+$WEP_E/2475);$WNB=int($WN_sA[10]+$WEP_E/2475);print "RES+$WNA&nbsp;";print "INT+$WNB&nbsp;";}
	elsif($WN_sA[7]=~ m/!1x/){$WNA=int($WN_sA[1]+$WEP_E/2475);$WNB=int($WN_sA[10]+$WEP_E/2475);print "RES+$WNA&nbsp;";print "INT+$WNB&nbsp;";}

#	if($WN_sA[15] > 0 && $WN_sA[15] ne ""){print "ダメージ軽減+$WN_sA[15]&nbsp;";}
	if($WN_sA[16] > 0 && $WN_sA[16] ne ""){print "回避+$WN_sA[16]&nbsp;";}

	print "$tokusyu";
	
#	if($tokusyuuniq ne ""){
	if($Ent_A > 0){
		print "<br><span class=td3>&nbsp;&nbsp;固有\&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$tokusyuuniq";
	}
	
#杖計算　3・4つはだめー &nbsp;&nbsp;RES+$WN_sB[15]&nbsp;&nbsp;回避+
	$Staff = 0;
	$BouguB = 0;
	$BouguC = 0;
	$BouguD = 0;
	if ($WN_sA[7]=~ m/!15|!19/){$Staff = 1;}

#	if($WN_sA[7] !~ m/!6h/ && ($WN_sB[7]=~ m/!13|!14|!17/ && $WN_sA[1] >25) || ($WN_sC[7]!~ m/!16/ && $WN_sD2[7]!~ m/!16/ && $WN_sB[7]=~ m/!16/) || ($WN_sB[7]=~ m/!15|!19/ && $WN_sA[7]=~ m/!18/ && $ALY_CLASS[17] =~ m/!1|!E007|!E008/) || ($WN_sC[7]!~ m/!12/ && $WN_sD2[7]!~ m/!12/ && $WN_sB[7]=~ m/!12/ && $WN_sA[7]=~ m/!10/) || ($WN_sB[7]=~ m/!i1/) && $WN_sB[1] <=31 && $WN_sB[1] >0 || $WN_sB[7]=~ m/!6c/){
#	if($WN_sA[7] !~ m/!6h/ && (($WN_sB[7]=~ m/!13/ && $Ring == 0 && $WN_sA[1] >25) || ($WN_sB[7]=~ m/!14|!17/ && $WN_sA[1] >25)) || ($WN_sC[7]!~ m/!16/ && $WN_sD2[7]!~ m/!16/ && $WN_sB[7]=~ m/!16/) || ($WN_sB[7]=~ m/!15|!19/ && $WN_sA[7]=~ m/!18/ && $ALY_CLASS[17] =~ m/!1/) || ($WN_sC[7]!~ m/!12/ && $WN_sD2[7]!~ m/!12/ && $WN_sB[7]=~ m/!12/ && $WN_sA[7]=~ m/!10/) || ($WN_sB[7]=~ m/!i1/) && $WN_sB[1] <=31 && $WN_sB[1] >0 || $WN_sB[7]=~ m/!6c/){
	if($WN_sA[7] !~ m/!6h/ && ($WN_sB[7]=~ m/!13|!14|!17/ && $WN_sA[1] > 40) || ($WN_sC[7]!~ m/!16/ && $WN_sD2[7]!~ m/!16/ && $WN_sB[7]=~ m/!16/) || ($WN_sB[7]=~ m/!15|!19/ && $Staff < 2 && ($WN_sA[7]=~ m/!18/ || $WN_sS[7]=~ m/!18/) && $ALY_CLASS[17] =~ m/!1|!E007|!E008/) || ($WN_sC[7]!~ m/!12/ && $WN_sD2[7]!~ m/!12/ && $WN_sB[7]=~ m/!12/ && $WN_sA[7]=~ m/!10/) || ($WN_sC[7]!~ m/!1s|!1u|!1w/ && $WN_sD2[7]!~ m/!1s|!1u|!1w/ && $WN_sB[7]=~ m/!1s|!1u|!1w/) || ($WN_sC[7]!~ m/!1t|!1v|!1x|!E0003/ && $WN_sD2[7]!~ m/!1t|!1v|!1x|!E0003/ && $WN_sB[7]=~ m/!1t|!1v|!1x|!E0003/) || ($WN_sB[7]=~ m/!i1/) && $WN_sB[1] <=41 && $WN_sB[1] >0 || $WN_sB[7]=~ m/!6c/){
		print"<br><span class=td3>&nbsp;&nbsp;防具&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sB[9].gif\">&nbsp;&nbsp;<b>".$WN_sB[0]."</b>";
		if ($WN_sB[7]=~ m/!15|!19/){$Staff = $Staff + 1;}
		$BouguB = 1;
	}elsif($WN_sB[7]=~ m/!1c/ && $WN_sA[7]=~ m/!1d/){
		print"<br><span class=td3>&nbsp;&nbsp;魔導書&nbsp;&nbsp;</span>&nbsp;".$ret[0]."&nbsp;Lv.$WLV_A/exp.$WEP_A&nbsp;&nbsp;".$ret[1]."</b>";
	}elsif($ALY_CLASS[17] =~ m/!E011|!E012/ && $WN_sB[7]=~ m/!E0008/){
#		print"<br><span class=td3>&nbsp;&nbsp;魔導書&nbsp;&nbsp;</span>&nbsp;".$ret[0]."&nbsp;Lv.$WLV_A/exp.$WEP_A&nbsp;&nbsp;".$ret[1]."</b>";
		print"<br><span class=td3>&nbsp;&nbsp;防具&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sB[9].gif\">&nbsp;&nbsp;<b>".$WN_sB[0]."</b>";
	}else{
		print'<br>&nbsp;&nbsp;予備&nbsp;&nbsp;&nbsp;&nbsp;<b>'.$WN_sB[0].'</b>';
	}
	print "&nbsp;Lv.$WLV_B/exp.$WEP_B" if $WN_sB[0];
#	if($WN_sB[1] > 0 && $WN_sB[1] ne "" && $BouguB == 1){print"&nbsp;&nbsp;RES+$WN_sB[1]";}
#	if($WN_sB[15] > 0 && $WN_sB[15] ne "" && $BouguB == 1){print"&nbsp;&nbsp;ダメージ軽減+$WN_sB[15]";}
	if($WN_sB[16] > 0 && $WN_sB[16] ne "" && $BouguB == 1){print"&nbsp;&nbsp;回避+$WN_sB[16]";}
	print "<br>";

#	if($WN_sA[7] !~ m/!6h/ && ($WN_sC[7]=~ m/!13|!14|!16|!17/ && $WN_sA[1] >25) || ($WN_sC[7]=~ m/!15|!19/ && $WN_sA[7]=~ m/!18/ && $ALY_CLASS[17] =~ m/!1|!E007|!E008/) || ($WN_sC[7]=~ m/!12/ && $WN_sA[7]=~ m/!10/) || ($WN_sC[7]=~ m/!i1/) && $WN_sC[1] <=31 && $WN_sC[1] >0 || $WN_sC[7]=~ m/!6c/){
	if($WN_sA[7] !~ m/!6h/ && ($WN_sC[7]=~ m/!13|!14|!17/ && $WN_sA[1] > 40) || ($WN_sD2[7]!~ m/!16/ && $WN_sC[7]=~ m/!16/) || ($WN_sC[7]=~ m/!15|!19/ && $Staff < 2 && ($WN_sA[7]=~ m/!18/ || $WN_sS[7]=~ m/!18/) && $ALY_CLASS[17] =~ m/!1|!E007|!E008/) || ($WN_sD2[7]!~ m/!12/ && $WN_sC[7]=~ m/!12/ && $WN_sA[7]=~ m/!10/) || ($WN_sD2[7]!~ m/!1s|!1u|!1w/ && $WN_sC[7]=~ m/!1s|!1u|!1w/) || ($WN_sD2[7]!~ m/!1t|!1v|!1x|!E0003/ && $WN_sC[7]=~ m/!1t|!1v|!1x|!E0003/) || ($WN_sC[7]=~ m/!i1/) && $WN_sC[1] <=41 && $WN_sC[1] >0 || $WN_sC[7]=~ m/!6c/){
		print"<span class=td3>&nbsp;&nbsp;防具&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sC[9].gif\">&nbsp;&nbsp;<b>".$WN_sC[0]."</b>";
		if ($WN_sC[7]=~ m/!15|!19/){$Staff = $Staff + 1;}
		$BouguC = 1;
	}elsif($WN_sC[7]=~ m/!1c/ && $WN_sA[7]=~ m/!1d/){
		print"<span class=td3>&nbsp;&nbsp;魔導書&nbsp;&nbsp;</span>&nbsp;".$ret[0]."&nbsp;Lv.$WLV_A/exp.$WEP_A&nbsp;&nbsp;".$ret[1]."</b>";
	}elsif($ALY_CLASS[17] =~ m/!E011|!E012/ && $WN_sC[7]=~ m/!E0008/){
#		print"<span class=td3>&nbsp;&nbsp;魔導書&nbsp;&nbsp;</span>&nbsp;".$ret[0]."&nbsp;Lv.$WLV_A/exp.$WEP_A&nbsp;&nbsp;".$ret[1]."</b>";
		print"<span class=td3>&nbsp;&nbsp;防具&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sC[9].gif\">&nbsp;&nbsp;<b>".$WN_sC[0]."</b>";
	}else{
		print'&nbsp;&nbsp;予備&nbsp;&nbsp;&nbsp;&nbsp;<b>'.$WN_sC[0].'</b>';
	}
	print "&nbsp;Lv.$WLV_C/exp.$WEP_C" if $WN_sC[0];
#	if($WN_sC[1] > 0 && $WN_sC[1] ne "" && $BouguC == 1){print"&nbsp;&nbsp;RES+$WN_sC[1]";}
#	if($WN_sC[15] > 0 && $WN_sC[15] ne "" && $BouguC == 1){print"&nbsp;&nbsp;ダメージ軽減+$WN_sC[15]";}
	if($WN_sC[16] > 0 && $WN_sC[16] ne "" && $BouguC == 1){print"&nbsp;&nbsp;回避+$WN_sC[16]";}
	print "<br>";

	if($WN_sA[7] !~ m/!6h/ && ($WN_sD2[7]=~ m/!13|!14|!16|!17/ && $WN_sA[1] > 40) || ($WN_sD2[7]=~ m/!15|!19/ && $Staff < 2 && ($WN_sA[7]=~ m/!18/ || $WN_sS[7]=~ m/!18/) && $ALY_CLASS[17] =~ m/!1|!E007|!E008/) || ($WN_sD2[7]=~ m/!12/ && $WN_sA[7]=~ m/!10/) || ($WN_sD2[7]=~ m/!1s|!1u|!1w/) || ($WN_sD2[7]=~ m/!1t|!1v|!1x|!E0003/) || ($WN_sD2[7]=~ m/!i1/) && $WN_sD2[1] <=41 && $WN_sD2[1] >0 || $WN_sD2[7]=~ m/!6c/){
		print"<span class=td3>&nbsp;&nbsp;防具&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sD2[9].gif\">&nbsp;&nbsp;<b>".$WN_sD2[0]."</b>";
		$BouguD = 1;
	}elsif($WN_sD2[7]=~ m/!1c/ && $WN_sA[7]=~ m/!1d/){
		print"<span class=td3>&nbsp;&nbsp;魔導書&nbsp;&nbsp;</span>&nbsp;".$ret[0]."&nbsp;Lv.$WLV_A/exp.$WEP_A&nbsp;&nbsp;".$ret[1]."</b>";
	}elsif($ALY_CLASS[17] =~ m/!E011|!E012/ && $WN_sD2[7]=~ m/!E0008/){
#		print"<span class=td3>&nbsp;&nbsp;魔導書&nbsp;&nbsp;</span>&nbsp;".$ret[0]."&nbsp;Lv.$WLV_A/exp.$WEP_A&nbsp;&nbsp;".$ret[1]."</b>";
		print"<span class=td3>&nbsp;&nbsp;防具&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sD2[9].gif\">&nbsp;&nbsp;<b>".$WN_sD2[0]."</b>";
	}else{
		print'&nbsp;&nbsp;予備&nbsp;&nbsp;&nbsp;&nbsp;<b>'.$WN_sD2[0].'</b>';
	}
	print "&nbsp;Lv.$WLV_D2/exp.$WEP_D2" if $WN_sD2[0];
#	if($WN_sD2[1] > 0 && $WN_sD2[1] ne "" && $BouguD == 1){print"&nbsp;&nbsp;RES+$WN_sD2[1]";}
#	if($WN_sD2[15] > 0 && $WN_sD2[15] ne "" && $BouguD == 1){print"&nbsp;&nbsp;ダメージ軽減+$WN_sD2[15]";}
	if($WN_sD2[16] > 0 && $WN_sD2[16] ne "" && $BouguD == 1){print"&nbsp;&nbsp;回避+$WN_sD2[16]";}


	print "</td>";
	print "<td style=\"font-size:12px;line-height:17px;\" valign=top nowrap width=50%>";

#特殊
$HyS = "装備";
	if ($WN_sS[11] >= 1 && $WN_sS[11] <= 3){$HyS = "魔法";}
	elsif ($WN_sS[11] == 4){$HyS = "合成魔法";}
	elsif ($WN_sS[11] == 5){$HyS = "必殺技";}
	elsif ($WN_sS[11] >= 6 && $WN_sS[11] <= 8){$HyS = "特殊";}
	if ($WN_sT[11] >= 1 && $WN_sT[11] <= 3){$HyT = "魔法";}
	elsif ($WN_sT[11] == 4){$HyT = "合成魔法";}
	elsif ($WN_sT[11] == 5){$HyT = "必殺技";}
	elsif ($WN_sT[11] >= 6 && $WN_sT[11] <= 8){$HyT = "特殊";}
	if ($WN_sU[11] >= 1 && $WN_sU[11] <= 3){$HyU = "魔法";}
	elsif ($WN_sU[11] == 4){$HyU = "合成魔法";}
	elsif ($WN_sU[11] == 5){$HyU = "必殺技";}
	elsif ($WN_sU[11] >= 6 && $WN_sU[11] <= 8){$HyU = "特殊";}

	#ディアナで弓以外を使用した場合は性能低下
#	if($WN_sA[7] =~ m/!1a/ && $ALY_CLASS[17]=~ m/!E005/){$WN_sS[1]=int($WN_sS[1]*0.7);$WN_sS[2]=int($WN_sS[2]*0.7);$WN_sS[4]+=40;}

	if($PL_VALUES[41] && $WN_sS[7]=~ m/!1d/ && ($WN_sA[7]=~ m/!1c/ || $WN_sB[7]=~ m/!1c/ || $WN_sD[7]=~ m/!1c/ || $WN_sD2[7]=~ m/!1c/)){
		print"<span class=td3>&nbsp;&nbsp;<b>$HyS</b>&nbsp;&nbsp;</span>&nbsp;<b>".$WN_sS[0]."</b>&nbsp;Lv.$WLV_D/exp.$WEP_D<br>";
		print "<span class=td3>&nbsp;&nbsp;性\能\&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sS[9].gif\">&nbsp;&nbsp;攻：".&STATUS_CONVERT($WN_sS[1]*(($WLV_D*0.003)+1)*$WN_sS[3]/500,'s')."&nbsp;（".&STATUS_CONVERT($WN_sS[1]*$WN_sS[3]/500,'s')."）&nbsp;命：".&STATUS_CONVERT($WN_sS[2]/4,'s')."&nbsp;&nbsp;回：$WN_sS[3]&nbsp;&nbsp;MP：$WN_sS[4]&nbsp;&nbsp;<br>";
	#技
	}elsif($PL_VALUES[41] && $WN_sS[11] =~ m/5/){
		print"<span class=td3>&nbsp;&nbsp;<b>$HyS</b>&nbsp;&nbsp;</span>&nbsp;<b>".$WN_sS[0]."</b>&nbsp;Lv.$WLV_S/exp.$WEP_S<br>";
		print "<span class=td3>&nbsp;&nbsp;性\能\&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sS[9].gif\">&nbsp;&nbsp;攻：".&STATUS_CONVERT($WN_sS[1]*(($WLV_A*0.003)+1)*$WN_sS[3]/500,'s')."&nbsp;（".&STATUS_CONVERT($WN_sS[1]*$WN_sS[3]/500,'s')."）&nbsp;命：".&STATUS_CONVERT($WN_sS[2]/4,'s')."&nbsp;&nbsp;回：$WN_sS[3]&nbsp;&nbsp;MP：$WN_sS[4]&nbsp;&nbsp;<br>";
	}elsif($PL_VALUES[41]){
		print"<span class=td3>&nbsp;&nbsp;<b>$HyS</b>&nbsp;&nbsp;</span>&nbsp;<b>".$WN_sS[0]."</b>&nbsp;Lv.$WLV_S/exp.$WEP_S<br>";
		print "<span class=td3>&nbsp;&nbsp;性\能\&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sS[9].gif\">&nbsp;&nbsp;攻：".&STATUS_CONVERT($WN_sS[1]*(($WLV_S*0.003)+1)*$WN_sS[3]/500,'s')."&nbsp;（".&STATUS_CONVERT($WN_sS[1]*$WN_sS[3]/500,'s')."）&nbsp;命：".&STATUS_CONVERT($WN_sS[2]/4,'s')."&nbsp;&nbsp;回：$WN_sS[3]&nbsp;&nbsp;MP：$WN_sS[4]&nbsp;&nbsp;<br>";
	}else{
#		print'&nbsp;&nbsp;予備&nbsp;&nbsp;&nbsp;&nbsp;<b>'.$WN_sS[0].'</b>';
	}
##特殊能力2
	foreach $j2 (@WN_sS_ef){
#		$j2.="x$j2";
		@vijunu2=split(/\,/,$WEAPONEF_LIST{"$j2"});
		$tokusyu2 .= "<a href=\"Javascript:showclasx$j2();\">$vijunu2[0]</a>&nbsp;"if $j2;
print << "-----END-----"if $j2;
	<table width=100% height=100% id="clas$j2" style="position:absolute;visibility:hidden;top:26px;left:281px;"><tr><td align=center>
	<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr><td style="background-color:$TABLE_COLOR2;padding:3px;" colspan=2><b>$vijunu2[0]</b></td>
	<td style="background-color:$TABLE_COLOR2;" colspan=2><a href="Javascript:hideclasx$j2();"><b>×</b></a></td></tr>
	<tr><td width="300" colspan="2" style="padding:5px;">$vijunu2[1]</td>
	</tr></table>
	</td></tr></table>
-----END-----
	}
#	print "$tokusyu2<br>";
	print "<span class=td3>&nbsp;&nbsp;性\能\&nbsp;&nbsp</span>&nbsp;&nbsp$tokusyu2&nbsp;&nbsp<br>" if $PL_VALUES[41];

#	print "&nbsp;Lv.$WLV_S/exp.$WEP_S" if $WN_sS[0];print "<br>";


	if($PL_VALUES[42]){
		print"<span class=td3>&nbsp;&nbsp;$HyT&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sT[9].gif\">&nbsp;&nbsp;<b>".$WN_sT[0]."</b>";
	}else{
#		print'&nbsp;&nbsp;予備&nbsp;&nbsp;&nbsp;&nbsp;<b>'.$WN_sT[0].'</b>';
	}
	print "&nbsp;Lv.$WLV_T/exp.$WEP_T<br>" if $WN_sT[0];
#	print "<br>";

	if($PL_VALUES[43]){
		print"<span class=td3>&nbsp;&nbsp;$HyU&nbsp;&nbsp;</span>&nbsp;<img src=\"$IMG_FOLDER4/$WN_sU[9].gif\">&nbsp;&nbsp;<b>".$WN_sU[0]."</b>";
	}else{
#		print'&nbsp;&nbsp;予備&nbsp;&nbsp;&nbsp;&nbsp;<b>'.$WN_sU[0].'</b>';
	}
	print "&nbsp;Lv.$WLV_U/exp.$WEP_U" if $WN_sU[0];print "<br>";

	print "</td>";
	print "<td style=\"font-size:12px;line-height:17px;\" valign=top nowrap width=50%>";



	print "</td><td style=\"font-size:12px;line-height:17px;\" valign=top nowrap width=50%>";
	print "<span class=td3>&nbsp;&nbsp;<b>LASTBATTLE</b>&nbsp;&nbsp;</span>&nbsp;&nbsp;";
	($DatHp,$Result) = split(/!/,$PL_VALUES[1]);
	print &DATE_DECORD("$DatHp")."&nbsp;<br>&nbsp;&nbsp;$Result";
#世界大戦

	if($PL_VALUES[28] ne ''){
  			if($PL_VALUES[28] eq $CL_VALUES[2]){
			$MOKUHYO="$CL_VALUES[8]";
		}elsif($PL_VALUES[28] eq $CL_VALUES[3]){
			$MOKUHYO="$CL_VALUES[9]";
		}elsif($PL_VALUES[28] eq $CL_VALUES[4]){
			$MOKUHYO="$CL_VALUES[10]";
		}
	}else{
		$MOKUHYO="$CL_VALUES[6]";
	}

	if($MOKUHYO eq "バルダー装備を崇める会かも"){$MOKUHYO="";}

	if($WW_FRAG==1 && $HIZUK_FRAG==1){$TIME[4]+=1;
		print "<br><span class=td3><font size=2>&nbsp;&nbsp;<b>世界大戦</b>&nbsp;&nbsp;</span>&nbsp;&nbsp; Limit:";
		print "$TIME[4]月$TIME[3]日&nbsp;($WW_TIME1:00～$WW_TIME2:59)<br><span style=\"border:1px solid #5779EE;font-size:13px;\">&nbsp;&nbsp;<b>任務</b>&nbsp;&nbsp;</span>";
		print "&nbsp;&nbsp;<b>すべての国の攻略と要塞の破壊</b>";
	}
	elsif (($CL_VALUES[7] > time || $CL_VALUES[37] > time) && $MOKUHYO ne ""){
		if($CL_VALUES[6] eq 'フォーチュン使用！'){
			print "<br><span class=td3>&nbsp;&nbsp;<b>!Check</b>&nbsp;&nbsp;</span>&nbsp;&nbsp;<b style=\"color:$CL_VALUES[0];\">フォーチュン発動中！</b> Limit：".&DATE_DECORD("$CL_VALUES[37]");
		}else{
			$JIKANSA=$CL_VALUES[13];$JIKANSA=15 if $CL_VALUES[13]>14;$FILIP=$CL_VALUES[14]+$JIKANSA*60;
			print "<br><span class=td3>&nbsp;&nbsp;<b>戦略</b>&nbsp;&nbsp;</span>&nbsp;&nbsp;<b style=\"color:$CL_VALUES[0];\">$CL_VALUES[5]</b>";
			if ($FILIP > time){
				print " Start：".&DATE_DECORD("$FILIP");
			}else{
				print " Limit：".&DATE_DECORD("$CL_VALUES[7]");
			}
			print "<br><span style=\"border:1px solid #5779EE;font-size:13px;\">&nbsp;&nbsp;<b>任務</b>&nbsp;&nbsp;</span>";
			if($PL_VALUES[28] ne ''){
	  			if($PL_VALUES[28] eq $CL_VALUES[2]){
					$MOKUHYO="$CL_VALUES[8]";
				}elsif($PL_VALUES[28] eq $CL_VALUES[3]){
					$MOKUHYO="$CL_VALUES[9]";
				}elsif($PL_VALUES[28] eq $CL_VALUES[4]){
					$MOKUHYO="$CL_VALUES[10]";
				}
			}else{
				$MOKUHYO="$CL_VALUES[6]";
			}
			print "&nbsp;&nbsp;<b>$MOKUHYO 本国の攻略と要塞の破壊</b>";
		}
	}
	print "</td></tr></table></td><td>&nbsp;</td></tr><tr><td>&nbsp;</td>";
$BBS="<td><input type=button value=\"&nbsp;BBS&nbsp;\" onClick=\"window.open('$YOUR_BBS')\"></td>"if $YOUR_BBS;
$WIKI="<td><input type=button value=\"WIKI\" onClick=\"window.open('$YOUR_WIKI')\"></td>"if $YOUR_WIKI;
$RULES="<td><input type=button value=\"手引&nbsp;\" onClick=\"window.open('$YOUR_RULES')\"></td>"if $YOUR_RULES;
#$BOUMEI_BUTTON="<td><input type=submit name=\"b_mode\" value=\"亡命\" onClick=\"lag(5);document.FM.cmd.value='BATTLE_1';Move()\"></td>";
#$NAIRAN_BUTTON="<td><input type=submit name=\"b_mode\" value=\"内乱\" onClick=\"lag(5);document.FM.cmd.value='BATTLE_1';Move()\"></td>";
$BOUMEI_BUTTON="<td><input type=submit name=\"b_mode\" value=\"亡命\" onClick=\"document.FM.cmd.value='BATTLE_1';Move()\"></td>";
$NAIRAN_BUTTON="<td><input type=submit name=\"b_mode\" value=\"内乱\" onClick=\"document.FM.cmd.value='BATTLE_1';Move()\"></td>";

#$BattleX="<td><input type=\"submit\" name=\"b_mode\" value=\"戦闘\" onClick=\"lag(0);document.FM.cmd.value='BATTLE_1';Move()\"></td>";


	if ($PL_VALUES[5] ne $NONE_NATIONALITY && $YOUR_CHAT){
	($sec,$min,$hour,$mday,$mon,$year,$wday,$d,$d) = localtime(time - 9*60*60);$mday+=9;
	$COUT=crypt "$PL_VALUES[5]",$mday;
	$CHAT="<input type=button value=\"CHAT\" $STYLE_B1 onClick=\"parent.Sub.location.replace('$YOUR_CHAT?room=$COUT\@toeb')\">";
	}elsif($PL_VALUES[5] eq $NONE_NATIONALITY && $YOUR_CHAT){
	($sec,$min,$hour,$mday,$mon,$year,$wday,$d,$d) = localtime(time - 9*60*60);$mday+=9;
	$COUT2=crypt "無国籍",$mday;
	$CHAT="<input type=button value=\"CHAT\" $STYLE_B1 onClick=\"parent.Sub.location.replace('$YOUR_CHAT?room=$COUT2\@toeb')\">";
	}
	($sec,$min,$hour,$mday,$mon,$year,$wday,$d,$d) = localtime(time - 9*60*60);$mday+=9;
	$COUT3=crypt "304鯖全体",$mday;
	$CHAT2="<input type=button value=\"酒場\" $STYLE_B1 onClick=\"parent.Sub.location.replace('$YOUR_CHAT2?room=$COUT3\@frame')\">";

$tag1='戦闘';
#$calx=time;
	require './vatime.pl';
	&vatimeheader3;
if((($WN_sS[7] =~ m/!6j|!6k|!76/ || $WN_sT[7] =~ m/!6j|!6k|!76/ || $WN_sU[7] =~ m/!6j|!6k|!76/) && $ALY_CLASS[17]=~ m/!p/) || (($WN_sS[7] =~ m/!6l/ || $WN_sT[7] =~ m/!6l/ || $WN_sU[7] =~ m/!6l/) && $ALY_CLASS[17]=~ m/!q/) || (($WN_sS[7] =~ m/!77/ || $WN_sT[7] =~ m/!77/ || $WN_sU[7] =~ m/!77/) && $ALY_CLASS[17]=~ m/!E003/)){
#	$BOUMEI_BUTTON="<td>&nbsp;&nbsp;</td>" if $PL_VALUES[5] ne $NONE_NATIONALITY;
#	$NAIRAN_BUTTON="<td>&nbsp;&nbsp;</td>";
#	$NAIRAN_BUTTON="";
#	$HEAL="<td><input type=submit name=\"b_mode\" value=\"回復\" onClick=\"lag(3);document.FM.cmd.value='BATTLE_1';Move()\"></td>";
#	$CCCC="<td>&nbsp;&nbsp;</td>";
#	$tag1='回復';
}
#	<td><input type=button value="情報" onClick="lag(0);parent.Sub.location.replace('$MAIN_SCRIPT?C_LIST')"></td>
#	<td><input type=submit name="custom" value="技術" onClick="lag(0);document.FM.cmd.value='ABISET';Move()"></td>
#	<td><input type=submit name="custom" value="褒章" onClick="lag(0);document.FM.cmd.value='KOUKENSET';Move()"></td>
#	<td><input type=submit name="custom" value="技術" onClick="lag(0);document.FM.cmd.value='ABISET';Move()"></td>

#	<td><input type=submit name="b_mode" value="$tag1" onClick="lag(0);document.FM.cmd.value='BATTLE_1';Move();"></td>
#	<td><input type=button value="市場" $STYLE_B1 onClick="parent.Sub.location.replace('./auction.cgi')"></td>

print << "-----END-----";
	<td><form action=$MAIN_SCRIPT name="FM" method="POST" target=Sub>
	<script language="JavaScript">
		function Move(){parent.Sub.location.replace("$BACKFR");}
	</script>
	
		<input type=hidden name=cmd>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
		<input type=hidden name=nowt value=$calx>
	<table border="0" cellspacing="0" cellpadding="0" id="btn">
	<tr><td>&nbsp;&nbsp;</td>
	<td><input type=submit name=\"b_mode\" value=\"$tag1\" onClick=\"document.FM.cmd.value='BATTLE_1';Move()\"></td>
	<td><input type=submit name=\"b_mode\" value=\"回復\" onClick=\"document.FM.cmd.value='BATTLE_1';Move()\"></td>
	<td>&nbsp;&nbsp;</td>
	$BOUMEI_BUTTON
	$NAIRAN_BUTTON
	<td>&nbsp;&nbsp;</td>
	<td>&nbsp;&nbsp;</td>
	<td><input type=button value="自国" onClick="parent.Sub.location.replace('$MAIN_SCRIPT?MY_LIST')"></td>
	<td><input type=button value="情報" onClick="parent.Sub.location.replace('$MAIN_SCRIPT?CO_LIST')"></td>
	<td><input type=submit name="custom" value="歴史" onClick="document.FM.cmd.value='HIS';Move()"></td>
	<td>&nbsp;&nbsp;</td>
	$BBS
	$RULES
	$WIKI
	<td>&nbsp;&nbsp;</td>
	<td>&nbsp;&nbsp;</td>
	<td>&nbsp;&nbsp;</td>
	
	<td><input type=submit value="更新" onClick="document.FM.target='Main';document.FM.cmd.value='MAIN_FRAME';"></td>
	</tr><tr>
	<td>&nbsp;&nbsp;</td>
	<td><input type=submit name="custom" value="$CUSTOM_NAME" onClick="document.FM.cmd.value='CUSTOMING';Move()"></td>
	<td><input type=submit name="custom" value="褒章" onClick="document.FM.cmd.value='KOUKENSET';Move()"></td>
	<td>&nbsp;&nbsp;</td>
	<td><input type=submit name="custom" value="装備" onClick="document.FM.cmd.value='EQUIPMENT';Move()"></td>
	<td><input type=submit name="custom" value="発言" onClick="document.FM.cmd.value='COM';Move()"></td>
	<td>&nbsp;&nbsp;</td>
	<td>&nbsp;&nbsp;</td>
	<td><input type=submit name="custom" value="特殊"  onClick="document.FM.cmd.value='SPC';Move()"></td>
	<td>&nbsp;&nbsp;</td>
	<td><input type=submit name="custom" value="勢力"  onClick="document.FM.cmd.value='RANKINGS';Move()"></td>
	<td>&nbsp;&nbsp;</td>
	<td><input type=submit name="custom" value="伝言"  onClick="document.FM.cmd.value='DENGON';Move()"></td>
	<td>$CHAT</td>
	<td><input type=submit name="custom" value=" 会議"  onClick="document.FM.cmd.value='Kaigi';Move()"></td>
	<td><input type=button value="酒場" $STYLE_B1 onClick=\"window.open('./kaigisitu.cgi')\"><td>
	<td>&nbsp;&nbsp;</td>
	<td><input type=button value="終了" onClick="top.close()"></td>

	</table></form></td>
	<td>&nbsp;&nbsp;</td>
	</tr></table>
-----END-----
	print "<script language=\"JavaScript\">location.href='#top';\n</script>\n" if $BANNER_DISPLAY;
	print << "	-----END-----";
	<script language="JavaScript">
	var h=$PL_VALUES[15];var m=$PL_VALUES[17];var r=$PL_VALUES[14];var timerID;
	myDate1 = new Date();
	var m_time=myDate1.getTime();
	HERepair();
	function HERepair(){
		myDate2 = new Date();
		n_time=myDate2.getTime();
		sasi = (m_time - n_time)/-1000;

		if (r > 1){r =Math.round ($PL_VALUES[14] - sasi*$RISK_REPAIR);}else{r = '－';}
		if (cond.innerText=='出撃可'){risk.innerHTML=r;}

		if (h < $PL_VALUES[16]){
			h = $PL_VALUES[15] + sasi*($PL_VALUES[16]*$HP_REPAIR/100+$HP_REPAIR2);
			n = ($PL_VALUES[16] - $PL_VALUES[15] - sasi*($PL_VALUES[16]*$HP_REPAIR/100+$HP_REPAIR2))/($PL_VALUES[16]*$HP_REPAIR/100+$HP_REPAIR2);
			if ((n/60) < 1){
				hp ='' + Math.round(n) + '秒';
			}else{
				hp = '' + Math.round(n/60-0.5) + '分';
			}
				h2 = ($PL_VALUES[15] + sasi*($PL_VALUES[16]*$HP_REPAIR/100+$HP_REPAIR2))/$PL_VALUES[16]*100;h3=100-Math.round (h2);
		}else{
			h = $PL_VALUES[16];h2=100;h3=0;hp = '－';
		}

		if (m < $PL_VALUES[18]){
			m = $PL_VALUES[17] + sasi*$EN_REPAIR;
			mpa = ($PL_VALUES[18] - $PL_VALUES[17] - sasi*$EN_REPAIR)/$EN_REPAIR;
			if ((mpa/60) < 1){
				mp ='' + Math.round(mpa) + '秒';
			}else{
				mp = '' + Math.round(mpa/60-0.5) + '分';
			}
			m2 = ($PL_VALUES[17] + sasi*$EN_REPAIR)/$PL_VALUES[18]*100;m3=100-Math.round (m2);
		}else{
			m = $PL_VALUES[18];m2=100;m3=0;mp = '－';
		}

		if (h >= $PL_VALUES[16] && cond.innerText=='回復中'){
			cond.innerText='出撃可';cond.style.color='#5779EE';
		}
		if (h >= $PL_VALUES[16] && m >= $PL_VALUES[18]){
			ato.innerHTML = '全回復';
		}else{
			ato.innerHTML = hp + '/' + mp;
		}
		hpb.innerHTML='<img src="$IMG_FOLDER1/hpb.gif" width="' + Math.round (h2) + '%" height="7"><img src="$IMG_FOLDER1/zhb.gif" width="' + h3 + '%" height="7">';
		mpb.innerHTML='<img src="$IMG_FOLDER1/mpb.gif" width="' + Math.round (m2) + '%" height="7"><img src="$IMG_FOLDER1/zhb.gif" width="' + m3 + '%" height="7">';
		j_hp.innerText=Math.round (h);
		j_en.innerText=Math.round (m);
		clearTimeout(timerID);
		timerID = setTimeout(\"HERepair()\",5000);
	}
	function lag(ms) {
		s = ms;btn.style.visibility = "hidden";clearTimeout(timerID);
		if(s>0){
			ato.innerHTML='再表\示 <B>' + ms + '</B>';s--;timerID = setTimeout('lag(s)',1000);
		}else{
			btn.style.visibility = "visible";HERepair();
		}
	}
	</script>
	-----END-----
	exit;
}


1;

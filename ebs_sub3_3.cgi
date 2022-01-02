sub FRAME{
	print <<"	-----END-----";
HTTP/1.1 200 OK
Content-Type: text/html

<script language="JavaScript"><!--
	if (window.name.match(/vtoeb\$/)) {
	document.write ('<html><head>');
	document.write ('<title>Tactics Ogre de Endless Battle 304 Edition</title></head>');
	document.write ('<frameset rows="$UPPER_FRAME,*" border="0" framespacing="0">');
	document.write ('<frame name="Main" frameborder="NO" src="$MAIN_SCRIPT?LOGIN">');
	document.write ('<frame name="Sub" frameborder="NO" src="$MAIN_SCRIPT?LOG0">');
	document.write ('</frameset>');
	document.write ('</html>');
	}else{}
// --></script>
<noscript>JavaScript対応ブラウザでお遊び下さい。</noscript>
	-----END-----
}
sub CUSTOMIZE{
#	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
#		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
#	@pairs = split(/\,/, $DUMMY{'EB'});
#		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
#	&ERROR('Error','ユニットとユーザのIDが一致していません。') if $COOKIE{'pname'} ne "$FORM{pname}";
#	&LOCK;
#	&DBM_CONVERT('P',"$FORM{pname}");$flagp=1;
#	&DBM_CONVERT('C',"$PL_VALUES[5]") if $PL_VALUES[5];
#	&UNLOCK;
#	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
#	&ERROR('Error','ユニットとユーザのIDが一致していません。') if $COOKIE{'pname'} ne "$FORM{pname}";
	&LOCK;
	&DBM_CONVERT('P',"$FORM{pname}");$flagp=1;
	&DBM_CONVERT('C',"$PL_VALUES[5]") if $PL_VALUES[5];
#	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($FORM{'pass'},eb) ne "$PL_VALUES[2]";
	
	$PL_VALUES[5]='' if $PL_VALUES[5] && !@CL_VALUES;
	$PL_VALUES[6]='0' if !$PL_VALUES[5];
	if ($PL_VALUES[28]){
		foreach ("$CL_VALUES[2]","$CL_VALUES[3]","$CL_VALUES[4]"){if ($PL_VALUES[28] eq "$_") {$DeleteFlag=1;}}
		if (!$DeleteFlag){$PL_VALUES[6]=$PL_VALUES[28]="";}
	}
$_="$FORM{'Cmode'}";
CUSTOM:{
	/^売却$/ && do{	$SW=$PL_VALUES[10] if $FORM{'sellw'}==1;$SW=$PL_VALUES[11] if $FORM{'sellw'}==2;$SW=$PL_VALUES[38] if $FORM{'sellw'}==3;
		$SW=$PL_VALUES[41] if $FORM{'sellw'}==4;$SW=$PL_VALUES[42] if $FORM{'sellw'}==5;$SW=$PL_VALUES[43] if $FORM{'sellw'}==6;$SW=$PL_VALUES[46] if $FORM{'sellw'}==7;
		my($wk,$wl)= split(/!/,$SW);my@www=split(/\,/,$WEAPON_LIST{"$wk"});
		&ERROR('だーめっ！') if $www[7] =~ m/!zd/;
		&ERROR('売れないよ～') if $FORM{'sellw'}==0;
		if($FORM{'sellw'}==1 && $PL_VALUES[10]){
			$PL_VALUES[10]='';$PL_VALUES[8]+=int $www[5]/2;
		}elsif($FORM{'sellw'}==2 && $PL_VALUES[11]){
			$PL_VALUES[11]='';$PL_VALUES[8]+=int $www[5]/2;
		}elsif($FORM{'sellw'}==3 && $PL_VALUES[38]){
			$PL_VALUES[38]='';$PL_VALUES[8]+=int $www[5]/2;
		}elsif($FORM{'sellw'}==4 && $PL_VALUES[41]){
			$PL_VALUES[41]='';$PL_VALUES[8]+=int $www[5]/2;
		}elsif($FORM{'sellw'}==5 && $PL_VALUES[42]){
			$PL_VALUES[42]='';$PL_VALUES[8]+=int $www[5]/2;
		}elsif($FORM{'sellw'}==6 && $PL_VALUES[43]){
			$PL_VALUES[43]='';$PL_VALUES[8]+=int $www[5]/2;
		}elsif($FORM{'sellw'}==7 && $PL_VALUES[46]){
			$PL_VALUES[46]='';$PL_VALUES[8]+=int $www[5]/2;
		}
	last CUSTOM;};
	/^忘れる$/ && do{
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});
		&ERROR("システムエラー") if $AbiSys == 0;
		$SW=$ABI_A if $FORM{'sellAbi'}==1;$SW=$ABI_B if $FORM{'sellAbi'}==2;$SW=$ABI_C if $FORM{'sellAbi'}==3;
		&ERROR('忘れられない') if $FORM{'sellAbi'}==0;
		
		if($FORM{'sellAbi'}==1 && $ABI_A ne ""){
			$ABI_A = "";
			$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			
			#最大HPアップを忘れる場合
			if($ABI_sA[2] =~ m/!A0034/){
			
				#他に最大HPアップを持っていない場合に限り、最大HP-20000を行う
				if($ABI_sB[2] !~ m/!A0034/ && $ABI_sC[2] !~ m/!A0034/){$PL_VALUES[16]-=20000;}
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}

			}
			#最大MPアップを忘れる場合
			if($ABI_sA[2] =~ m/!A0035/){
			
				#他に最大MPアップを持っていない場合に限り、最大MP-1000を行う
				if($ABI_sB[2] !~ m/!A0035/ && $ABI_sC[2] !~ m/!A0035/){$PL_VALUES[18]-=1000;}
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}

			}
			
		}
		elsif($FORM{'sellAbi'}==2 && $ABI_B ne ""){
			$ABI_B = "";
			$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			
			#最大HPアップを忘れる場合
			if($ABI_sB[2] =~ m/!A0034/){
			
				#他に最大HPアップを持っていない場合に限り、最大HP-20000を行う
				if($ABI_sA[2] !~ m/!A0034/ && $ABI_sC[2] !~ m/!A0034/){$PL_VALUES[16]-=20000;}
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}

			}
			#最大MPアップを忘れる場合
			if($ABI_sB[2] =~ m/!A0035/){
			
				#他に最大MPアップを持っていない場合に限り、最大MP-1000を行う
				if($ABI_sA[2] !~ m/!A0035/ && $ABI_sC[2] !~ m/!A0035/){$PL_VALUES[18]-=1000;}
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}

			}

		}
		elsif($FORM{'sellAbi'}==3 && $ABI_C ne ""){
			$ABI_C = "";
			$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";

			#最大HPアップを忘れる場合
			if($ABI_sC[2] =~ m/!A0034/){
			
				#他に最大HPアップを持っていない場合に限り、最大HP-20000を行う
				if($ABI_sB[2] !~ m/!A0034/ && $ABI_sA[2] !~ m/!A0034/){$PL_VALUES[16]-=20000;}
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}

			}
			#最大MPアップを忘れる場合
			if($ABI_sC[2] =~ m/!A0035/){
			
				#他に最大MPアップを持っていない場合に限り、最大MP-1000を行う
				if($ABI_sB[2] !~ m/!A0035/ && $ABI_sA[2] !~ m/!A0035/){$PL_VALUES[18]-=1000;}
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}

			}

		}

	last CUSTOM;};
	
	/^技術並び替え$/ && do{
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		if ($FORM{'sorte'} eq "1"){
			if($FORM{'sorter'} eq "2"){
				($ABI_A,$ABI_B)=($ABI_B,$ABI_A);
				$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			}elsif($FORM{'sorter'} eq "3"){
				($ABI_A,$ABI_C)=($ABI_C,$ABI_A);
				$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			}
		}
		elsif ($FORM{'sorte'} eq "2"){
			if($FORM{'sorter'} eq "1"){
				($ABI_B,$ABI_A)=($ABI_A,$ABI_B);
				$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			}elsif($FORM{'sorter'} eq "3"){
				($ABI_B,$ABI_C)=($ABI_C,$ABI_B);
				$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			}
		}
		elsif ($FORM{'sorte'} eq "3"){
			if($FORM{'sorter'} eq "1"){
				($ABI_C,$ABI_A)=($ABI_A,$ABI_C);
				$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			}elsif($FORM{'sorter'} eq "2"){
				($ABI_C,$ABI_B)=($ABI_B,$ABI_C);
				$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			}
		}
	last CUSTOM;};

	/^技術習得$/ && do{
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});
		my@www=split(/\,/,$ABINAME_LIST{"$FORM{'buyabi'}"});
#		if(length($FORM{'buyw'}) == 2){&ERROR("その武器は買えません。");}

		&ERROR("APが足りません") if $PL_VALUES[53] < $www[1];
#		&ERROR("$FORM{'buyabi'}");
		$PL_VALUES[53]-=$www[1];

		if($ABI_sA[0] eq ""){$ABI_A = "$FORM{'buyabi'}";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
		elsif($ABI_sB[0] eq ""){$ABI_B = "$FORM{'buyabi'}";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
		elsif($ABI_sC[0] eq ""){$ABI_C = "$FORM{'buyabi'}";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}

		#最大HPアップ
		if($www[2] =~ m/!A0034/){
			if($ABI_sA[2] !~ m/!A0034/ && $ABI_sB[2] !~ m/!A0034/ && $ABI_sC[2] !~ m/!A0034/){$PL_VALUES[16]+=20000;}
		}
		#最大MPアップ
		if($www[2] =~ m/!A0035/){
			if($ABI_sA[2] !~ m/!A0035/ && $ABI_sB[2] !~ m/!A0035/ && $ABI_sC[2] !~ m/!A0035/){$PL_VALUES[18]+=1000;}
		}

		#？？？？
		if($www[2] =~ m/!A0077/){
			my@al=keys %ABINAME_LIST;$alw=@al;
			$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
			@q=split(/\,/,$ABINAME_LIST{"$gw"});
			#自身を引っ張ってしまった場合は、発声練習でｷﾘｯ
			if($gw eq "1076a"){$gw = "1060a";}
			#最大アップ系もはずれで回避させる
			if($gw eq "1033a"){$gw = "1082a";}
			if($gw eq "1034a"){$gw = "1083a";}
			if($ABI_A eq "1076a"){$ABI_A = "$gw";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
			if($ABI_B eq "1076a"){$ABI_B = "$gw";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
			if($ABI_C eq "1076a"){$ABI_C = "$gw";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
		}

	last CUSTOM;};

	/^シャッフル実行$/ && do{	
		&ERROR('所持金が足りません。') if $PL_VALUES[8] < 2000000;

		$PL_VALUES[8]=$PL_VALUES[8]-2000000;

#		local($WN_A,$WLV_A,$WF_A,$WSTR_A,$WVIT_A,$WDEX_A,$WAGI_A,$WMP_A,$WWHT_A,$WHP_A,$WMP_A,$WINI_A,$WMIND_A,$WMAXD_A,$WRES_A,$WDRI_A,$WLUC_A,$WPA_A,$WTRA_A) = split(/!/,$PL_VALUES[9]);
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);
		local($WN_B,$WLV_B,$WBEnt,$WB03,$WB04,$WB05,$WB06,$WB07,$WB08,$WB09,$WB10,$WB11,$WB12,$WB13,$WB14,$WB15,$WB16,$WB17,$WB18,$WB19,$WB20,$WB21,$WB22,$WB23,$WB24,$WB25,$WB26,$WB27,$WB28,$WB29,$WB30,$WB31,$WB32,$WB33,$WB34,$WB35,$WB36,$WB37,$WB38,$WB39,$WB40,$WB41,$WB42) = split(/!/,$PL_VALUES[10]);
		local($WN_C,$WLV_C,$WCEnt,$WC03,$WC04,$WC05,$WC06,$WC07,$WC08,$WC09,$WC10,$WC11,$WC12,$WC13,$WC14,$WC15,$WC16,$WC17,$WC18,$WC19,$WC20,$WC21,$WC22,$WC23,$WC24,$WC25,$WC26,$WC27,$WC28,$WC29,$WC30,$WC31,$WC32,$WC33,$WC34,$WC35,$WC36,$WC37,$WC38,$WC39,$WC40,$WC41,$WC42) = split(/!/,$PL_VALUES[11]);
		local($WN_D,$WLV_D,$WDEnt,$WD03,$WD04,$WD05,$WD06,$WD07,$WD08,$WD09,$WD10,$WD11,$WD12,$WD13,$WD14,$WD15,$WD16,$WD17,$WD18,$WD19,$WD20,$WD21,$WD22,$WD23,$WD24,$WD25,$WD26,$WD27,$WD28,$WD29,$WD30,$WD31,$WD32,$WD33,$WD34,$WD35,$WD36,$WD37,$WD38,$WD39,$WD40,$WD41,$WD42) = split(/!/,$PL_VALUES[38]);
			@q=split(/\,/,$WEAPON_LIST{"$WN_A"});
			
			$MFUP=0;
			if($WA12 ne "" && $WA12 > 0){$MFUP = $MFUP + $WA12 * 2;}
			if($WB12 ne "" && $WB12 > 0){$MFUP = $MFUP + $WB12 * 2;}
			if($WC12 ne "" && $WC12 > 0){$MFUP = $MFUP + $WC12 * 2;}
			if($WD12 ne "" && $WD12 > 0){$MFUP = $MFUP + $WD12 * 2;}
#$MFUP = 9999;
#			$ent="!0";	#ここでは装備品EXPをクリアしない

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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
				}
				
				#マジックファインド　頭防具限定|A30
				$ent_mf="!0";
				if($q[14] =~ m/A27/ && (rand(100) < 5 + $MFUP)){

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
					$MFUP = $MFUP * 0.9;
				
				}elsif($q[14] =~ m/A30/ && (rand(255) < 3 + $MFUP)){

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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;

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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
				}

#&ERROR("あ$q[14]");
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
				
#				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi!$ent_dl!$ent_mnb!$ent_kabok!$ent_kabog!$ent_tore!$ent_mf!$ent_res!$ent_fireb!$ent_waterb!$ent_earthb!$ent_windb!$ent_saintb!$ent_darkb!$ent_fireg!$ent_waterg!$ent_earthg!$ent_windg!$ent_saintg!$ent_darkg!$ent_img!$ent_gou!$ent_hhp!$ent_mmp!$ent_dam!$ent_hea!$ent_cri";
				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi$ent_dl$ent_mnb$ent_kabok$ent_kabog$ent_tore$ent_mf$ent_res$ent_fireb$ent_waterb$ent_earthb$ent_windb$ent_saintb$ent_darkb$ent_fireg$ent_waterg$ent_earthg$ent_windg$ent_saintg$ent_darkg$ent_img$ent_gou$ent_hhp$ent_mmp$ent_dam$ent_hea$ent_cri$ent_brk";

				$PL_VALUES[9]="$WN_A!$WLV_A!$WAEnt";
				$PL_VALUES[9].=$ent;

	last CUSTOM;};

	/^褒章交換$/ && do{
	@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}
#		local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#		local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#		local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#		local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);

		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);
		local($WN_B,$WLV_B,$WBEnt,$WB03,$WB04,$WB05,$WB06,$WB07,$WB08,$WB09,$WB10,$WB11,$WB12,$WB13,$WB14,$WB15,$WB16,$WB17,$WB18,$WB19,$WB20,$WB21,$WB22,$WB23,$WB24,$WB25,$WB26,$WB27,$WB28,$WB29,$WB30,$WB31,$WB32,$WB33,$WB34,$WB35,$WB36,$WB37,$WB38,$WB39,$WB40,$WB41,$WB42) = split(/!/,$PL_VALUES[10]);
		local($WN_C,$WLV_C,$WCEnt,$WC03,$WC04,$WC05,$WC06,$WC07,$WC08,$WC09,$WC10,$WC11,$WC12,$WC13,$WC14,$WC15,$WC16,$WC17,$WC18,$WC19,$WC20,$WC21,$WC22,$WC23,$WC24,$WC25,$WC26,$WC27,$WC28,$WC29,$WC30,$WC31,$WC32,$WC33,$WC34,$WC35,$WC36,$WC37,$WC38,$WC39,$WC40,$WC41,$WC42) = split(/!/,$PL_VALUES[11]);
		local($WN_D,$WLV_D,$WDEnt,$WD03,$WD04,$WD05,$WD06,$WD07,$WD08,$WD09,$WD10,$WD11,$WD12,$WD13,$WD14,$WD15,$WD16,$WD17,$WD18,$WD19,$WD20,$WD21,$WD22,$WD23,$WD24,$WD25,$WD26,$WD27,$WD28,$WD29,$WD30,$WD31,$WD32,$WD33,$WD34,$WD35,$WD36,$WD37,$WD38,$WD39,$WD40,$WD41,$WD42) = split(/!/,$PL_VALUES[38]);

		local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
		local($WN_T,$WLV_T) = split(/!/,$PL_VALUES[42]);
		local($WN_U,$WLV_U) = split(/!/,$PL_VALUES[43]);
		local($WN_Y,$WLV_Y) = split(/!/,$PL_VALUES[46]);

		@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
		@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
		@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
		@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});
		@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
		@WN_sT=split(/\,/,$WEAPON_LIST{"$WN_T"});
		@WN_sU=split(/\,/,$WEAPON_LIST{"$WN_U"});
		@WN_sY=split(/\,/,$WEAPON_LIST{"$WN_Y"});
		require "./$LOG_FOLDER/$KOUKEN_DATA";


		my@www=split(/\,/,$KOUKEN_LIST{"$FORM{'buyw'}"});
#		if(length($FORM{'buyw'}) == 2){&ERROR("その武器は買えません。");}

		&ERROR("貢献値が足りません") if $HC[1] < $www[1];
		&ERROR("ストックが埋まっている為、実行できません") if $PL_VALUES[46] ne "";
		&ERROR("戦略中は、褒章交換できません。") if (($WW_FRAG==1 && $HIZUK_FRAG==1) || ($CL_VALUES[7] > time || $CL_VALUES[37] > time));
#		&ERROR("$FORM{'buyabi'}");
		$HC[1]-=$www[1];
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		#トレジャー用エンチャント
		if($www[0] eq "トレジャー袋(上級)" || $www[0] eq "トレジャー袋(下級)"){
			my@al=keys %WEAPON_LIST;$alw=@al;
			$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
			@q=split(/\,/,$WEAPON_LIST{"$gw"});
			
			$MFUP=0;
			if($WA12 ne "" && $WA12 > 0){$MFUP = $MFUP + $WA12 * 2;}
			if($WB12 ne "" && $WB12 > 0){$MFUP = $MFUP + $WB12 * 2;}
			if($WC12 ne "" && $WC12 > 0){$MFUP = $MFUP + $WC12 * 2;}
			if($WD12 ne "" && $WD12 > 0){$MFUP = $MFUP + $WD12 * 2;}

#			$ent="!0";

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
				

#				&ERROR("$ent_ent");
#				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi!$ent_dl!$ent_mnb!$ent_kabok!$ent_kabog!$ent_tore!$ent_mf!$ent_res!$ent_fireb!$ent_waterb!$ent_earthb!$ent_windb!$ent_saintb!$ent_darkb!$ent_fireg!$ent_waterg!$ent_earthg!$ent_windg!$ent_saintg!$ent_darkg!$ent_img!$ent_gou!$ent_hhp!$ent_mmp!$ent_dam!$ent_hea!$ent_cri";
				$ent .= "$ent_ent$ent_str$ent_vit$ent_dex$ent_agi$ent_dl$ent_mnb$ent_kabok$ent_kabog$ent_tore$ent_mf$ent_res$ent_fireb$ent_waterb$ent_earthb$ent_windb$ent_saintb$ent_darkb$ent_fireg$ent_waterg$ent_earthg$ent_windg$ent_saintg$ent_darkg$ent_img$ent_gou$ent_hhp$ent_mmp$ent_dam$ent_hea$ent_cri$ent_brk";

		}

		#装備品強化値
		$ent_ent="!0!0";
#&ERROR("$gw$ent_entああ$ent");
		#トレジャー袋(上級)の処理
		if($www[0] eq "トレジャー袋(上級)"){

			if($q[11] ne "0"){$ent="";}
			
#			&ERROR("$q[0]ああ$q[8]");
			if ($q[17] == 1){

				$PL_VALUES[46]="$gw$ent_ent$ent";

			}elsif ($q[17] == 2 && rand(100) > 75){

				$PL_VALUES[46]="$gw$ent_ent$ent";
				
			}elsif ($q[17] == 3 && rand(100) > 50){

				$PL_VALUES[46]="$gw$ent_ent$ent";

			}else{
				$gw = "0045a";
				$PL_VALUES[46]="$gw!0";

			}
		#トレジャー袋(下級)の処理
		}elsif($www[0] eq "トレジャー袋(下級)"){

			if($q[11] ne "0"){$ent="";}

#			&ERROR("$q[0]ああ$q[8]");
			if ($q[17] == 1){

				$PL_VALUES[46]="$gw$ent_ent$ent";

			}else{
			
				$gw = "0038a";
				$PL_VALUES[46]="$gw!0";

			}
		}else{

			$PL_VALUES[46]="$www[2]!0";
#			if (!$PL_VALUES[10] && $www[3] == 0){$PL_VALUES[10]="$www[2]!0";}
#			elsif (!$PL_VALUES[11] && $www[3] == 0){$PL_VALUES[11]="$www[2]!0";}
#			elsif (!$PL_VALUES[38] && $www[3] == 0){$PL_VALUES[38]="$www[2]!0";}
#			elsif (!$PL_VALUES[41] && $www[3] != 0){$PL_VALUES[41]="$www[2]!0";}
#			elsif (!$PL_VALUES[42] && $www[3] != 0){$PL_VALUES[42]="$www[2]!0";}
#			elsif (!$PL_VALUES[43] && $www[3] != 0){$PL_VALUES[43]="$www[2]!0";}
		}

	last CUSTOM;};
	
	/^道具使用$/ && do{	$SW=$PL_VALUES[10] if $FORM{'shiyoi'}==1;$SW=$PL_VALUES[11] if $FORM{'shiyoi'}==2;$SW=$PL_VALUES[38] if $FORM{'shiyoi'}==3;
		$SW=$PL_VALUES[41] if $FORM{'shiyoi'}==4;$SW=$PL_VALUES[42] if $FORM{'shiyoi'}==5;$SW=$PL_VALUES[43] if $FORM{'shiyoi'}==6;$SW=$PL_VALUES[46] if $FORM{'shiyoi'}==7;
		my($wk,$wl)= split(/!/,$SW);my@www=split(/\,/,$WEAPON_LIST{"$wk"});
		&ERROR('だーめっ！') if $www[7] =~ m/!zd/;
#		&ERROR('売れないよ～') if $FORM{'shiyoi'}==0;
#		&REPAIR(\@PL_VALUES);
		&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
		
		#キュアリーフ
		if($www[7] =~ m/!E0015/){

			$PL_VALUES[15]=$PL_VALUES[15]+4000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

		#キュアシード
		}elsif($www[7] =~ m/!E0016/){

			$PL_VALUES[15]=$PL_VALUES[15]+12000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

		#キュアペースト
		}elsif($www[7] =~ m/!E0017/){

			$PL_VALUES[15]=$PL_VALUES[15]+36000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

		#キュアエキス
		}elsif($www[7] =~ m/!E0018/){

			$PL_VALUES[15] = $PL_VALUES[16];

		#マジックリーフ
		}elsif($www[7] =~ m/!E0019/){

			$PL_VALUES[17]=$PL_VALUES[17]+150;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#マジックシード
		}elsif($www[7] =~ m/!E0020/){

			$PL_VALUES[17]=$PL_VALUES[17]+400;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#マジックペースト
		}elsif($www[7] =~ m/!E0021/){

			$PL_VALUES[17]=$PL_VALUES[17]+900;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#マジックエキス
		}elsif($www[7] =~ m/!E0022/){

			$PL_VALUES[17]=$PL_VALUES[17]+1500;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#剣の紋章
		}elsif($www[7] =~ m/!E0100/){

			if($PL_VALUES[19] < 50){$PL_VALUES[19]=$PL_VALUES[19]+1;}

		#守護の腕輪
		}elsif($www[7] =~ m/!E0101/){

			if($PL_VALUES[20] < 50){$PL_VALUES[20]=$PL_VALUES[20]+1;}

		#俊敏の石
		}elsif($www[7] =~ m/!E0102/){

			if($PL_VALUES[21] < 50){$PL_VALUES[21]=$PL_VALUES[21]+1;}

		#精密の水晶
		}elsif($www[7] =~ m/!E0103/){

			if($PL_VALUES[22] < 50){$PL_VALUES[22]=$PL_VALUES[22]+1;}

		#賢者の果実
		}elsif($www[7] =~ m/!E0023/){

			$PL_VALUES[15]=$PL_VALUES[15]+25000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

			$PL_VALUES[17]=$PL_VALUES[17]+800;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#天使の果実
		}elsif($www[7] =~ m/!E0024/){

			$PL_VALUES[15] = $PL_VALUES[16];
			$PL_VALUES[17] = $PL_VALUES[18];

		#腐りかけた果実
		}elsif($www[7] =~ m/!E0025/){
			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";

			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && ($PL_VALUES[28] eq $NP_VALS[28])){

					&REPAIR(\@NP_VALS);

					if($NP_VALS[25] ne "1"){

						$NP_VALS[15] = $NP_VALS[15] + int($PL_VALUES[15]/2);
						$NP_VALS[1]="$DATE!$PL_VALUES[3]は腐りかけた果実を行使！";

						if($NP_VALS[15] >= $NP_VALS[16]){
							$NP_VALS[15] = $NP_VALS[16];
						}

						dbmopen (%P,"$DBM_P",0666);
							$P{"$key"}="@NP_VALS";
						dbmclose %P;

					}
				}

			}

			$PL_VALUES[15]=0;
			$PL_VALUES[25]=1;

		}else{&ERROR("システムエラー");}

		if($FORM{'shiyoi'}==1 && $PL_VALUES[10]){
			$PL_VALUES[10]='';
		}elsif($FORM{'shiyoi'}==2 && $PL_VALUES[11]){
			$PL_VALUES[11]='';
		}elsif($FORM{'shiyoi'}==3 && $PL_VALUES[38]){
			$PL_VALUES[38]='';
		}elsif($FORM{'shiyoi'}==4 && $PL_VALUES[41]){
			$PL_VALUES[41]='';
		}elsif($FORM{'shiyoi'}==5 && $PL_VALUES[42]){
			$PL_VALUES[42]='';
		}elsif($FORM{'shiyoi'}==6 && $PL_VALUES[43]){
			$PL_VALUES[43]='';
		}elsif($FORM{'shiyoi'}==7 && $PL_VALUES[46]){
			$PL_VALUES[46]='';
		}
	last CUSTOM;};
	/^武器修復1$/ && do{$PL_VALUES[9]='2hy!0';last CUSTOM;};
	/^武器修復2$/ && do{$PL_VALUES[10]='2hy!0';last CUSTOM;};
	/^武器修復3$/ && do{$PL_VALUES[11]='2hy!0';last CUSTOM;};
	/^武器修復4$/ && do{$PL_VALUES[38]='2hy!0';last CUSTOM;};
	/^特殊修復1$/ && do{$PL_VALUES[41]='';last CUSTOM;};
	/^特殊修復2$/ && do{$PL_VALUES[42]='';last CUSTOM;};
	/^特殊修復3$/ && do{$PL_VALUES[43]='';last CUSTOM;};
	/^ランクアップ$/ && do{my($wk,$wl) = split(/!/,$PL_VALUES[9]);
		&ERROR('条件を満たしておりません') if ($wl < ($WEAPON_RANKUP * $WEAPON_LVUP) || length($FORM{'wname'}) != length($wk)+1);
#
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);

		if((length($FORM{'wname'}) - length($wk)) >= 2){&ERROR("改造エラーです。");}

		if ($FORM{'wname'} =~ m/^$wk/){
			$PL_VALUES[9]="$FORM{'wname'}!0!$WAEnt!$WA03!$WA04!$WA05!$WA06!$WA07!$WA08!$WA09!$WA10!$WA11!$WA12!$WA13!$WA14!$WA15!$WA16!$WA17!$WA18!$WA19!$WA20!$WA21!$WA22!$WA23!$WA24!$WA25!$WA26!$WA27!$WA28!$WA29!$WA30!$WA31!$WA32!$WA33!$WA34!$WA35!$WA36!$WA37!$WA38!$WA39!$WA40!$WA41!$WA42";
		}
	last CUSTOM;};
	/^特殊ランクアップ$/ && do{my($sk,$sl) = split(/!/,$PL_VALUES[41]);
		&ERROR('条件を満たしておりません') if ($sl < ($WEAPON_RANKUP * $WEAPON_LVUP) || length($FORM{'sname'}) != length($sk)+1);
		if ($FORM{'sname'} =~ m/^$sk/){
			local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[41]);
			$PL_VALUES[41]="$FORM{'sname'}!0!$WAEnt";
		}
	last CUSTOM;};
	/^装備$/ && do{
		if ($FORM{'soubi'} eq "B" && $PL_VALUES[10]){($PL_VALUES[9],$PL_VALUES[10])=($PL_VALUES[10],$PL_VALUES[9]);}
	 elsif ($FORM{'soubi'} eq "C" && $PL_VALUES[11]){($PL_VALUES[9],$PL_VALUES[11])=($PL_VALUES[11],$PL_VALUES[9]);}
	 elsif ($FORM{'soubi'} eq "D" && $PL_VALUES[38]){($PL_VALUES[9],$PL_VALUES[38])=($PL_VALUES[38],$PL_VALUES[9]);}
	last CUSTOM;};

	/^装備並び替え$/ && do{
#		if ($FORM{'sorte'} eq "0"){
#			if($FORM{'sorter'} eq "1"){
#				($PL_VALUES[9],$PL_VALUES[10])=($PL_VALUES[10],$PL_VALUES[9]);
#				if($PL_VALUES[45] eq "10"){$PL_VALUES[45] = "11";}
#				elsif($PL_VALUES[45] eq "100"){$PL_VALUES[45] = "110";}
#			}elsif($FORM{'sorter'} eq "3"){
#				($PL_VALUES[10],$PL_VALUES[38])=($PL_VALUES[38],$PL_VALUES[10]);			
#				if($PL_VALUES[45] eq "10"){$PL_VALUES[45] = "38";}
#				elsif($PL_VALUES[45] eq "100"){$PL_VALUES[45] = "380";}
#			}
#		}
#		elsif ($FORM{'sorte'} eq "1"){
		if ($FORM{'sorte'} eq "1"){
			if($FORM{'sorter'} eq "2"){
				($PL_VALUES[10],$PL_VALUES[11])=($PL_VALUES[11],$PL_VALUES[10]);
				if($PL_VALUES[45] eq "10"){$PL_VALUES[45] = "11";}
				elsif($PL_VALUES[45] eq "100"){$PL_VALUES[45] = "110";}
			}elsif($FORM{'sorter'} eq "3"){
				($PL_VALUES[10],$PL_VALUES[38])=($PL_VALUES[38],$PL_VALUES[10]);			
				if($PL_VALUES[45] eq "10"){$PL_VALUES[45] = "38";}
				elsif($PL_VALUES[45] eq "100"){$PL_VALUES[45] = "380";}
			}
		}
		elsif ($FORM{'sorte'} eq "2"){
			if($FORM{'sorter'} eq "1"){
				($PL_VALUES[11],$PL_VALUES[10])=($PL_VALUES[10],$PL_VALUES[11]);
				if($PL_VALUES[45] eq "11"){$PL_VALUES[45] = "10";}
				elsif($PL_VALUES[45] eq "110"){$PL_VALUES[45] = "100";}
			}elsif($FORM{'sorter'} eq "3"){
				($PL_VALUES[11],$PL_VALUES[38])=($PL_VALUES[38],$PL_VALUES[11]);			
				if($PL_VALUES[45] eq "11"){$PL_VALUES[45] = "38";}
				elsif($PL_VALUES[45] eq "110"){$PL_VALUES[45] = "380";}
			}
		}
		elsif ($FORM{'sorte'} eq "3"){
			if($FORM{'sorter'} eq "1"){
				($PL_VALUES[38],$PL_VALUES[10])=($PL_VALUES[10],$PL_VALUES[38]);
				if($PL_VALUES[45] eq "38"){$PL_VALUES[45] = "10";}
				elsif($PL_VALUES[45] eq "380"){$PL_VALUES[45] = "100";}
			}elsif($FORM{'sorter'} eq "2"){
				($PL_VALUES[38],$PL_VALUES[11])=($PL_VALUES[11],$PL_VALUES[38]);			
				if($PL_VALUES[45] eq "38"){$PL_VALUES[45] = "11";}
				elsif($PL_VALUES[45] eq "380"){$PL_VALUES[45] = "110";}
			}
		}
	last CUSTOM;};

	/^特殊並び替え$/ && do{
		if ($FORM{'sorts'} eq "1"){
			if($FORM{'sortsr'} eq "2"){
				($PL_VALUES[41],$PL_VALUES[42])=($PL_VALUES[42],$PL_VALUES[41]);
				if($PL_VALUES[45] eq "41"){$PL_VALUES[45] = "42";}
			}elsif($FORM{'sortsr'} eq "3"){
				($PL_VALUES[41],$PL_VALUES[43])=($PL_VALUES[43],$PL_VALUES[41]);			
				if($PL_VALUES[45] eq "41"){$PL_VALUES[45] = "43";}
			}
		}
		elsif ($FORM{'sorts'} eq "2"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[42],$PL_VALUES[41])=($PL_VALUES[41],$PL_VALUES[42]);
				if($PL_VALUES[45] eq "42"){$PL_VALUES[45] = "41";}
			}elsif($FORM{'sortsr'} eq "3"){
				($PL_VALUES[42],$PL_VALUES[43])=($PL_VALUES[43],$PL_VALUES[42]);			
				if($PL_VALUES[45] eq "42"){$PL_VALUES[45] = "43";}
			}
		}
		elsif ($FORM{'sorts'} eq "3"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[43],$PL_VALUES[41])=($PL_VALUES[41],$PL_VALUES[43]);
				if($PL_VALUES[45] eq "43"){$PL_VALUES[45] = "41";}
			}elsif($FORM{'sortsr'} eq "2"){
				($PL_VALUES[43],$PL_VALUES[42])=($PL_VALUES[42],$PL_VALUES[43]);			
				if($PL_VALUES[45] eq "43"){$PL_VALUES[45] = "42";}
			}
		}
	last CUSTOM;};


	/^\装\備倉庫使用$/ && do{
		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}
		
		if($HC[1] < 2){&ERROR("貢献値が足りません。");}
		$HC[1] = $HC[1] - 2;
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		#&ERROR("貢献値が足りません。");
		if ($FORM{'sorte'} eq "1"){
			if($FORM{'sorter'} eq "0"){
				($PL_VALUES[10],$PL_VALUES[55])=($PL_VALUES[55],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "1"){
				($PL_VALUES[10],$PL_VALUES[56])=($PL_VALUES[56],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "2"){
				($PL_VALUES[10],$PL_VALUES[57])=($PL_VALUES[57],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "3"){
				if($PL_VALUES[29] < 200){&ERROR("レベルが足りません。");}
				($PL_VALUES[10],$PL_VALUES[58])=($PL_VALUES[58],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "4"){
				if($PL_VALUES[29] < 500){&ERROR("レベルが足りません。");}
				($PL_VALUES[10],$PL_VALUES[59])=($PL_VALUES[59],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "5"){
				if($PL_VALUES[29] < 1000){&ERROR("レベルが足りません。");}
				($PL_VALUES[10],$PL_VALUES[60])=($PL_VALUES[60],$PL_VALUES[10]);
			}
		}
		elsif ($FORM{'sorte'} eq "2"){
			if($FORM{'sorter'} eq "0"){
				($PL_VALUES[11],$PL_VALUES[55])=($PL_VALUES[55],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "1"){
				($PL_VALUES[11],$PL_VALUES[56])=($PL_VALUES[56],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "2"){
				($PL_VALUES[11],$PL_VALUES[57])=($PL_VALUES[57],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "3"){
				if($PL_VALUES[29] < 200){&ERROR("レベルが足りません。");}
				($PL_VALUES[11],$PL_VALUES[58])=($PL_VALUES[58],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "4"){
				if($PL_VALUES[29] < 500){&ERROR("レベルが足りません。");}
				($PL_VALUES[11],$PL_VALUES[59])=($PL_VALUES[59],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "5"){
				if($PL_VALUES[29] < 1000){&ERROR("レベルが足りません。");}
				($PL_VALUES[11],$PL_VALUES[60])=($PL_VALUES[60],$PL_VALUES[11]);
			}
		}
		elsif ($FORM{'sorte'} eq "3"){
			if($FORM{'sorter'} eq "0"){
				($PL_VALUES[38],$PL_VALUES[55])=($PL_VALUES[55],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "1"){
				($PL_VALUES[38],$PL_VALUES[56])=($PL_VALUES[56],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "2"){
				($PL_VALUES[38],$PL_VALUES[57])=($PL_VALUES[57],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "3"){
				if($PL_VALUES[29] < 200){&ERROR("レベルが足りません。");}
				($PL_VALUES[38],$PL_VALUES[58])=($PL_VALUES[58],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "4"){
				if($PL_VALUES[29] < 500){&ERROR("レベルが足りません。");}
				($PL_VALUES[38],$PL_VALUES[59])=($PL_VALUES[59],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "5"){
				if($PL_VALUES[29] < 1000){&ERROR("レベルが足りません。");}
				($PL_VALUES[38],$PL_VALUES[60])=($PL_VALUES[60],$PL_VALUES[38]);
			}
		}


	last CUSTOM;};


	/^特殊倉庫使用$/ && do{
		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}
		
		if($HC[1] < 2){&ERROR("貢献値が足りません。");}
		$HC[1] = $HC[1] - 2;
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		#&ERROR("貢献値が足りません。");
		if ($FORM{'sorts'} eq "1"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[41],$PL_VALUES[61])=($PL_VALUES[61],$PL_VALUES[41]);
			}elsif($FORM{'sortsr'} eq "2"){
				if($PL_VALUES[29] < 300){&ERROR("レベルが足りません。");}
				($PL_VALUES[41],$PL_VALUES[62])=($PL_VALUES[62],$PL_VALUES[41]);
			}elsif($FORM{'sortsr'} eq "3"){
				if($PL_VALUES[29] < 800){&ERROR("レベルが足りません。");}
				($PL_VALUES[41],$PL_VALUES[63])=($PL_VALUES[63],$PL_VALUES[41]);
			}
		}
		elsif ($FORM{'sorts'} eq "2"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[42],$PL_VALUES[61])=($PL_VALUES[61],$PL_VALUES[42]);
			}elsif($FORM{'sortsr'} eq "2"){
				if($PL_VALUES[29] < 300){&ERROR("レベルが足りません。");}
				($PL_VALUES[42],$PL_VALUES[62])=($PL_VALUES[62],$PL_VALUES[42]);
			}elsif($FORM{'sortsr'} eq "3"){
				if($PL_VALUES[29] < 800){&ERROR("レベルが足りません。");}
				($PL_VALUES[42],$PL_VALUES[63])=($PL_VALUES[63],$PL_VALUES[42]);
			}
		}
		elsif ($FORM{'sorts'} eq "3"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[43],$PL_VALUES[61])=($PL_VALUES[61],$PL_VALUES[43]);
			}elsif($FORM{'sortsr'} eq "2"){
				if($PL_VALUES[29] < 300){&ERROR("レベルが足りません。");}
				($PL_VALUES[43],$PL_VALUES[62])=($PL_VALUES[62],$PL_VALUES[43]);
			}elsif($FORM{'sortsr'} eq "3"){
				if($PL_VALUES[29] < 800){&ERROR("レベルが足りません。");}
				($PL_VALUES[43],$PL_VALUES[63])=($PL_VALUES[63],$PL_VALUES[43]);
			}
		}

	last CUSTOM;};

	/^取り出す$/ && do{
		&ERROR("システムエラー") if !$PL_VALUES[46];
		local($WN_Y,$WLV_Y) = split(/!/,$PL_VALUES[46]);
		@WN_sY=split(/\,/,$WEAPON_LIST{"$WN_Y"});

		if (!$PL_VALUES[10] && ($WN_sY[11] == 0 || $WN_sY[11] == 9)){$PL_VALUES[10]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[11] && ($WN_sY[11] == 0 || $WN_sY[11] == 9)){$PL_VALUES[11]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[38] && ($WN_sY[11] == 0 || $WN_sY[11] == 9)){$PL_VALUES[38]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[41] && $WN_sY[11] != 0 && $WN_sY[11] != 9){$PL_VALUES[41]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[42] && $WN_sY[11] != 0 && $WN_sY[11] != 9){$PL_VALUES[42]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[43] && $WN_sY[11] != 0 && $WN_sY[11] != 9){$PL_VALUES[43]=$PL_VALUES[46];$PL_VALUES[46]="";}

	last CUSTOM;};

	/^設定$/ && do{
		#0で既存動作　1で武器だけで反撃
		$PL_VALUES[45] = $FORM{'AtSet'};
	last CUSTOM;};

	/^購入$/ && do{
		my@www=split(/\,/,$WEAPON_LIST{"$FORM{'buyw'}"});
#		if(length($FORM{'buyw'}) == 2){&ERROR("その武器は買えません。");}

		if($www[6] == 2){
			$PL_VALUES[18]=0;
			#ランキング用 アイテム獲得数　0はアイテム獲得　1はMVP　2は図鑑登録 3は不正カウント
			@RC=split(/!/,$PL_VALUES[47]);
			if($RC[3] eq ""){$RC[3] = 0;}
			$RC[3] = $RC[3] + 1;
			$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";
			&ERROR("その武器は買えません。");

		}
		if($www[6] == 8 && $PL_VALUES[5]){
			$PL_VALUES[18]=0;
			#ランキング用 アイテム獲得数　0はアイテム獲得　1はMVP　2は図鑑登録 3は不正カウント
			@RC=split(/!/,$PL_VALUES[47]);
			if($RC[3] eq ""){$RC[3] = 0;}
			$RC[3] = $RC[3] + 1;
			$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";
			&ERROR("その武器は買えません。");

		}
		$PL_VALUES[8]-=$www[5];
		if (!$PL_VALUES[10] && $www[11] == 0){$PL_VALUES[10]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[11] && $www[11] == 0){$PL_VALUES[11]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[38] && $www[11] == 0){$PL_VALUES[38]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[41] && $www[11] != 0){$PL_VALUES[41]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[42] && $www[11] != 0){$PL_VALUES[42]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[43] && $www[11] != 0){$PL_VALUES[43]="$FORM{'buyw'}!0";}
	last CUSTOM;};

	/^チェンジ$/ && do{
		&ERROR('ERROR','お金が足りないぜ旦那ぁ！') if $PL_VALUES[8] < 100000;
		$PL_VALUES[8]-=100000;
		$PL_VALUES[27]=$FORM{'icon'};
		$PL_VALUES[40]=$FORM{'icon2'};
		$PL_VALUES[13]=$FORM{'MsColor'};
		$PL_VALUES[3]=$FORM{'MsName'};
	last CUSTOM;};

	/^Custom$/ && do{&ERROR('熟練度が足りません') if $PL_VALUES[24] < 210;
		$PL_VALUES[8]-=20000;$PL_VALUES[23]++;$PL_VALUES[27]=$FORM{'icon'};$PL_VALUES[40]=$FORM{'icon2'};
		$PL_VALUES[13]=$FORM{'MsColor'};

	require "./$LOG_FOLDER/$CLASS_DATA";
	my@plclass=split(/\,/,$VCLASS_LIST{"$FORM{'MsType'}"});
		unless($plclass[12] <= $PL_VALUES[12] && $plclass[13] >= $PL_VALUES[12]){
			&ERROR('ERROR','ALIだーめっ！');
		}
		if($plclass[6] > $PL_VALUES[19]){&ERROR('ERROR','STRだーめっ！');}
		if($plclass[7] > $PL_VALUES[20]){&ERROR('ERROR','VITだーめっ！');}
		if($plclass[8] > $PL_VALUES[21]){&ERROR('ERROR','AGIだーめっ！');}
		if($plclass[9] > $PL_VALUES[22]){&ERROR('ERROR','DEXだーめっ！');}
		if($plclass[10] > $PL_VALUES[16]){&ERROR('ERROR','HPだーめっ！');}
		if($plclass[11] > $PL_VALUES[18]){&ERROR('ERROR','MPだーめっ！');}
		if($plclass[14] > $PL_VALUES[24]){&ERROR('ERROR','熟練度だーめっ！');}
		if($plclass[15]){
			local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
			local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
			my@wwa=split(/\,/,$WEAPON_LIST{"$WN_A"});
			my@wws=split(/\,/,$WEAPON_LIST{"$WN_S"});
			if($plclass[5]==4){
				if($wwa[7] !~ m/$plclass[15]/i && $wws[7] !~ m/$plclass[15]/i){&ERROR('ERROR','武器だーめっ！');}
			}elsif($plclass[5]==1 && $PL_VALUES[4] == 219){
				if($wwa[12] !~ m/e011/){&ERROR('ERROR','武器だーめっ！');}
			}else{
				if($plclass[15] ne $wwa[0] && $plclass[15] ne $wws[0]){&ERROR('ERROR','武器だーめっ！');}
			}
		}

		if($plclass[16]){
			if($PL_VALUES[4] !~ /$plclass[16]/i){&ERROR('ERROR','クラスだーめっ！');}
		}
		if($plclass[20]){
			if($plclass[20] < $PL_VALUES[24]){&ERROR('ERROR','熟練度下限だーめっ！');}
		}
		if($plclass[21]){
			if($plclass[21] > $PL_VALUES[32]){&ERROR('ERROR','指揮だーめっ！');}
		}
		$PL_VALUES[24]-=110;$PL_VALUES[24]=890 if($PL_VALUES[24] > 890);
		$PL_VALUES[4]=$FORM{'MsType'};
		$PL_VALUES[3]=$FORM{'MsName'};$PL_VALUES[31]=$FORM{'element'};
		if($plclass[17] =~ m/!x/){$PL_VALUES[31]=2;}
		if($plclass[17] =~ m/!y/){$PL_VALUES[31]=4;}
		if($plclass[17] =~ m/!z/){$PL_VALUES[31]=5;}
		if($PL_VALUES[4] =~ /^64$|^65$|^72$|^90$/i){$PL_VALUES[9]="1oa!0";}
	last CUSTOM;};
	/^$STATUS_NAME[4]アップ$/ && do{
		my$Chmn = ($PL_VALUES[16]+5000 + ($FORM{'hcheck'} - 1) * 100) * $FORM{'hcheck'};
		$PL_VALUES[8]-=$Chmn;
		$PL_VALUES[16]+=200*$FORM{'hcheck'};
		
		$LIMIT_HP = $MAX_HP;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0034/ || $ABI_sB[2] =~ m/!A0034/ || $ABI_sC[2] =~ m/!A0034/){$LIMIT_HP=90000;}
			$PL_VALUES[16]=$LIMIT_HP if $PL_VALUES[16] > $LIMIT_HP;

		}else{
			$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[4]アップ×１$/ && do{
		my$Chmn = ($PL_VALUES[16]+5000);
		$PL_VALUES[8]-=$Chmn;
		$PL_VALUES[16]+=200*1;
		
		$LIMIT_HP = $MAX_HP;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0034/ || $ABI_sB[2] =~ m/!A0034/ || $ABI_sC[2] =~ m/!A0034/){$LIMIT_HP=90000;}
			$PL_VALUES[16]=$LIMIT_HP if $PL_VALUES[16] > $LIMIT_HP;

		}else{
			$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[4]アップ×５$/ && do{
		my$Chmn = ($PL_VALUES[16]+5000) * 5 + 2000;
		$PL_VALUES[8]-=$Chmn;
		$PL_VALUES[16]+=200*5;
		
		$LIMIT_HP = $MAX_HP;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0034/ || $ABI_sB[2] =~ m/!A0034/ || $ABI_sC[2] =~ m/!A0034/){$LIMIT_HP=90000;}
			$PL_VALUES[16]=$LIMIT_HP if $PL_VALUES[16] > $LIMIT_HP;

		}else{
			$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[4]アップ×１０$/ && do{
		my$Chmn = ($PL_VALUES[16]+5000) * 10 + 9000;
		$PL_VALUES[8]-=$Chmn;
		$PL_VALUES[16]+=200*10;
		
		$LIMIT_HP = $MAX_HP;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0034/ || $ABI_sB[2] =~ m/!A0034/ || $ABI_sC[2] =~ m/!A0034/){$LIMIT_HP=90000;}
			$PL_VALUES[16]=$LIMIT_HP if $PL_VALUES[16] > $LIMIT_HP;

		}else{
			$PL_VALUES[16]=$MAX_HP if $PL_VALUES[16] > $MAX_HP;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]アップ$/ && do{
		my$Cemn = ($PL_VALUES[18]*10+5000 + ($FORM{'echeck'} - 1) * 25) * $FORM{'echeck'};
		$PL_VALUES[8]-=$Cemn;
		$PL_VALUES[18]+=5*$FORM{'echeck'};
		
		$LIMIT_MP = $MAX_EN;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0035/ || $ABI_sB[2] =~ m/!A0035/ || $ABI_sC[2] =~ m/!A0035/){$LIMIT_MP=5000;}
			$PL_VALUES[18]=$LIMIT_MP if $PL_VALUES[18] > $LIMIT_MP;

		}else{
			$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]アップ×１$/ && do{
		my$Cemn = ($PL_VALUES[18]*10+5000);
		$PL_VALUES[8]-=$Cemn;
		$PL_VALUES[18]+=5*1;
		
		$LIMIT_MP = $MAX_EN;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0035/ || $ABI_sB[2] =~ m/!A0035/ || $ABI_sC[2] =~ m/!A0035/){$LIMIT_MP=5000;}
			$PL_VALUES[18]=$LIMIT_MP if $PL_VALUES[18] > $LIMIT_MP;

		}else{
			$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]アップ×５$/ && do{
		my$Cemn = ($PL_VALUES[18]*10+5000) * 5 + 500;
		$PL_VALUES[8]-=$Cemn;
		$PL_VALUES[18]+=5*5;
		
		$LIMIT_MP = $MAX_EN;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0035/ || $ABI_sB[2] =~ m/!A0035/ || $ABI_sC[2] =~ m/!A0035/){$LIMIT_MP=5000;}
			$PL_VALUES[18]=$LIMIT_MP if $PL_VALUES[18] > $LIMIT_MP;

		}else{
			$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]アップ×１０$/ && do{
		my$Cemn = ($PL_VALUES[18]*10+5000) * 10 + 2250;
		$PL_VALUES[8]-=$Cemn;
		$PL_VALUES[18]+=5*10;
		
		$LIMIT_MP = $MAX_EN;
		if($AbiSys == 1){
			require "./$LOG_FOLDER/$ABI_DATA";
			local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
			@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
			@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
			@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});

			if($ABI_sA[2] =~ m/!A0035/ || $ABI_sB[2] =~ m/!A0035/ || $ABI_sC[2] =~ m/!A0035/){$LIMIT_MP=5000;}
			$PL_VALUES[18]=$LIMIT_MP if $PL_VALUES[18] > $LIMIT_MP;

		}else{
			$PL_VALUES[18]=$MAX_EN if $PL_VALUES[18] > $MAX_EN;
		}

		&ERROR('条件を満たしていません') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^Lv.アップ$/ && do{
		$TIKIM2=int(1000*$PL_VALUES[29]+100000);
		&ERROR('条件を満たしていません') if $PL_VALUES[8] < $TIKIM2;
		$PL_VALUES[8]-=$TIKIM2;$PL_VALUES[29]++;
		last CUSTOM;
		};
	/^ALIアップ$/ && do{&ERROR('条件を満たしていません') if $PL_VALUES[8] < 400000;
		$PL_VALUES[8]-=400000;if($PL_VALUES[12] < 100){$PL_VALUES[12]+=12;}
		if($PL_VALUES[12] > 100){$PL_VALUES[12]=100;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[0]アップ$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('条件を満たしていません') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[19] < 50){$PL_VALUES[19]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[19]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[1]アップ$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('条件を満たしていません') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[20] < 50){$PL_VALUES[20]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[20]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[3]アップ$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('条件を満たしていません') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[22] < 50){$PL_VALUES[22]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[22]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[2]アップ$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('条件を満たしていません') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[21] < 50){$PL_VALUES[21]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[21]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};

	$FORM{'mahouCheck'} && $PL_VALUES[5] && do{
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
#		&DBM_CONVERT('P');$flagp=1;
		#ハーネラ
		if ($FORM{'Xmode'} eq "プレイハーネラ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 1;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 1;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 1;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 1;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!プレイハーネラを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "デフハーネラ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 1;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 1;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 1;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 1;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!デフハーネラを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;#$flagp=1;
		}
		#ゾショネル
		if ($FORM{'Xmode'} eq "プレイゾショネル"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 2;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 2;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 2;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 2;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!プレイゾショネルを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "デフゾショネル"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 2;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 2;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 2;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 2;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!デフゾショネルを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;#$flagp=1;
		}
		#バーサ
		if ($FORM{'Xmode'} eq "プレイバーサ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 3;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 3;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 3;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 3;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!プレイバーサを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "デフバーサ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 3;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 3;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 3;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 3;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!デフバーサを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;#$flagp=1;
		}
		#グルーザ
		if ($FORM{'Xmode'} eq "プレイグルーザ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 4;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 4;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 4;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 4;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!プレイグルーザを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "デフグルーザ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#総帥の場合
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 4;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第一隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 4;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第二隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 4;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#第三隊長の場合
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 4;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!デフグルーザを使用しました。";

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;#$flagp=1;
		}
		if ($FORM{'Xmode'} eq "マーシーレイン"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
#			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
#			&ERROR('MPが足りません。') if $PL_VALUES[17] < 400;
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 600;

			#回復量計算　ユニットエレメント一致で30
			$PL_LP = 0.2;
			if($PL_VALUES[31] eq "3"){$PL_LP = 0.3;}

			&DBM_INPORT(P);

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
#				$PL_LP = 0.05;
#			}elsif($HealerCount <= 20 && $HealerCount >= 16){
#				$PL_LP = 0.10;if($PL_VALUES[31] eq "3"){$PL_LP = 0.12;}
#			}elsif($HealerCount <= 15 && $HealerCount >= 11){
#				$PL_LP = 0.14;if($PL_VALUES[31] eq "3"){$PL_LP = 0.18;}
#			}elsif($HealerCount <= 10 && $HealerCount >= 6){
#				$PL_LP = 0.17;if($PL_VALUES[31] eq "3"){$PL_LP = 0.24;}
#			}

			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && ($PL_VALUES[28] eq $NP_VALS[28])){

					&REPAIR(\@NP_VALS);

					if($NP_VALS[25] ne "1"){

						$NP_VALS[15] = int($NP_VALS[15] + int($NP_VALS[16] * $PL_LP));
						$NP_VALS[1]="$DATE!$PL_VALUES[3]はマーシーレインを行使！";

						if($NP_VALS[15] >= $NP_VALS[16]){
							$NP_VALS[15] = $NP_VALS[16];
						}

						dbmopen (%P,"$DBM_P",0666);
							$P{"$key"}="@NP_VALS";
						dbmclose %P;

					}
				}

			}

			$PL_VALUES[15] = int($PL_VALUES[15] + int($PL_VALUES[16] * $PL_LP));
			if($PL_VALUES[15] >= $PL_VALUES[16]){
				$PL_VALUES[15] = $PL_VALUES[16];
			}
#			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!マーシーレインを使用しました。";

			if($HoushoFlg == 1){
				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] eq ""){$HC[0] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}
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
				#現在貢献点＞最大貢献点の場合は記録
				if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
		
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;#$flagp=1;
		}
		if ($FORM{'Xmode'} eq "マーティライズ"){

			&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
#			&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
			&ERROR('MPが足りません。') if $PL_VALUES[17] < 1500;

			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && ($PL_VALUES[28] eq $NP_VALS[28])){

					&REPAIR(\@NP_VALS);

					if($NP_VALS[25] eq "1"){

#						$NP_VALS[15] = $NP_VALS[16];
						$NP_VALS[25] = 0;
						if($NP_VALS[15] <= 0){$NP_VALS[15] = 1;}
						$NP_VALS[1]="$DATE!$PL_VALUES[3]はマーティライズを行使！";

						if($NP_VALS[15] >= $NP_VALS[16]){
							$NP_VALS[15] = $NP_VALS[16];
						}

						dbmopen (%P,"$DBM_P",0666);
							$P{"$key"}="@NP_VALS";
						dbmclose %P;

					}
				}

			}

			$PL_VALUES[17] = $PL_VALUES[17] - 1500;
			$PL_VALUES[15] = 0;
			$PL_VALUES[25] = 1;
			$PL_VALUES[1]="$DATE!マーティライズを使用しました。$PL_VALUES[3]は戦闘不能\";

			if($HoushoFlg == 1){
				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] eq ""){$HC[0] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}
				#現在貢献点+80
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
				#現在貢献点＞最大貢献点の場合は記録
				if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
		
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			#貢献値加算
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#総帥の場合、貢献点+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;#$flagp=1;
		}

	last CUSTOM;};

	/^変更$/ && do{$PL_VALUES[7]="$FORM{'com'}";
	last CUSTOM;};
	/^アイコンチェンジ$/ && do{
		$PL_VALUES[36]="$FORM{'unitColor'}";
	last CUSTOM;};
#	/^倉庫入れ替え$/ && do{
#		###38は装備スロットとしてつかっちゃったので他変数でヨロピク　by304 20090212
#		if(!$PL_VALUES[38]){
#			$PL_VALUES[38]="$PL_VALUES[4],$PL_VALUES[9],$PL_VALUES[10],$PL_VALUES[11],$PL_VALUES[31],$PL_VALUES[24]";
#			$PL_VALUES[4]=0;
#			$PL_VALUES[9]=a;
#			$PL_VALUES[10]='';
#			$PL_VALUES[11]='';
#			$PL_VALUES[31]=0;
#			$PL_VALUES[24]=100;
#		}else{
#			$miche="$PL_VALUES[4],$PL_VALUES[9],$PL_VALUES[10],$PL_VALUES[11],$PL_VALUES[31],$PL_VALUES[24]";
#			my@souko=split(/,/,$PL_VALUES[38]) if $PL_VALUES[38];
#			$PL_VALUES[4]=$souko[0];
#			$PL_VALUES[9]=$souko[1];
#			$PL_VALUES[10]=$souko[2];
#			$PL_VALUES[11]=$souko[3];
#			$PL_VALUES[31]=$souko[4];
#			$PL_VALUES[24]=$souko[5];
#			$PL_VALUES[38]=$miche;
#		}

#	last CUSTOM;};
	/^亡命$/ && do{
		if($PL_VALUES[5]){
		$BOMEIM=int($PL_VALUES[8]/10);$BOMEIM='30000' if $BOMEIM < 30000;
		$PL_VALUES[8]-=$BOMEIM;
		}
		$PL_VALUES[5]="$FORM{'boumeiC'}";$PL_VALUES[28]='';$PL_VALUES[0]=$PL_VALUES[6]=0;

		#褒章システム	亡命の場合は、現在貢献点をクリアする
		if($HoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			
			#現在貢献点をクリア
			$HC[0] = 0;

#			#現在貢献点＞最大貢献点の場合は記録
#			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}

#			#累計貢献点の計算
#			$HC[2] = $HC[2] + 100;

			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		#新型褒章システム
#		if($NewHoushoFlg == 1){
#		
#			@HC=split(/!/,$PL_VALUES[50]);
#			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
#			if($HC[1] eq ""){$HC[1] = 0;}
#			if($HC[2] eq ""){$HC[2] = 0;}
#
#			$HC[1] = 0;
#			
#			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
#		
#		}

		#救済措置orz
#				&ERROR("$PL_VALUES[5]う$NC_Nameあ00あ$NC_VALUES[39]");
#		&DBM_INPORT(C);
#		while (($NC_Name,$NC_Value) =each %C) {
#				&ERROR("$NC_Nameああ$NC_VALUES[39]");
#
#			if($NC_Name eq $PL_VALUES[5]){
#
#				@NC_VALUES = split(/\s/,$NC_Value);
#				$PL_VALUES[39] = $NC_VALUES[39];
#			}
#
#		}

	last CUSTOM;};
	/^入隊$/ && do{$PL_VALUES[28]="$FORM{'inunit'}";last CUSTOM;};
	/^除隊$/ && do{$PL_VALUES[28]="";$PL_VALUES[6]="0";last CUSTOM;};
	/^部隊作成$/ && do{&ERROR('部隊名が記入されていません') if !$FORM{'uname'};
		if($FORM{'uname'} eq "$CL_VALUES[2]" || $FORM{'uname'} eq "$CL_VALUES[3]" || $FORM{'uname'} eq "$CL_VALUES[4]"){&ERROR('同名の部隊が既に存在します。');}
		&ERROR("部隊名に「未結成」を含める事は出来ません。") if $FORM{'uname'} =~ /未結成$/ ;
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		$flagc=1;$PL_VALUES[8]-=$MAKE_TEAM;
		UNIT:for ($i=2;$i <= 4; $i++){if (!$CL_VALUES[$i]){$CL_VALUES[$i]="$FORM{'uname'}";last UNIT;}}
	last CUSTOM;};
	/^部隊再編$/ && do{&ERROR('部隊名が記入されていません') if !$FORM{'suname'};
		if($FORM{'suname'} eq "$CL_VALUES[2]" || $FORM{'suname'} eq "$CL_VALUES[3]" || $FORM{'suname'} eq "$CL_VALUES[4]"){&ERROR('同名の部隊が既に存在します。');}
		&ERROR("部隊名に「未結成」を含める事は出来ません。") if $FORM{'suname'} =~ /未結成$/ ;
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		$flagc=1;
		$PL_VALUES[8]-=$NAME_TEAM;
		if($CL_VALUES[2] eq $PL_VALUES[28]){

			&DBM_INPORT(P);
			dbmopen (%P,"$DBM_P",0666);
			foreach $key (keys %P){
				@VS_VALUES = split(/\s/,$P{$key});
				#自国の変更前部隊のメンバーを全員、変更後部隊に編入する
				if($VS_VALUES[5] eq $PL_VALUES[5] && $VS_VALUES[28] eq $PL_VALUES[28] ){
					&REPAIR(\@VS_VALUES);
					$VS_VALUES[28] = "$FORM{'suname'}";
				}
				$P{"$key"}="@VS_VALUES";
			}

			dbmclose %P;
			$CL_VALUES[2]=$PL_VALUES[28]="$FORM{'suname'}";

		}elsif($CL_VALUES[3] eq $PL_VALUES[28]){

			&DBM_INPORT(P);
			dbmopen (%P,"$DBM_P",0666);
			foreach $key (keys %P){
				@VS_VALUES = split(/\s/,$P{$key});
				#自国の変更前部隊のメンバーを全員、変更後部隊に編入する
				if($VS_VALUES[5] eq $PL_VALUES[5] && $VS_VALUES[28] eq $PL_VALUES[28] ){
					&REPAIR(\@VS_VALUES);
					$VS_VALUES[28] = "$FORM{'suname'}";
				}
				$P{"$key"}="@VS_VALUES";
			}

			dbmclose %P;
			$CL_VALUES[3]=$PL_VALUES[28]="$FORM{'suname'}";


		}elsif($CL_VALUES[4] eq $PL_VALUES[28]){

			&DBM_INPORT(P);
			dbmopen (%P,"$DBM_P",0666);
			foreach $key (keys %P){
				@VS_VALUES = split(/\s/,$P{$key});
				#自国の変更前部隊のメンバーを全員、変更後部隊に編入する
				if($VS_VALUES[5] eq $PL_VALUES[5] && $VS_VALUES[28] eq $PL_VALUES[28] ){
					&REPAIR(\@VS_VALUES);
					$VS_VALUES[28] = "$FORM{'suname'}";
				}
				$P{"$key"}="@VS_VALUES";
			}

			dbmclose %P;
			$CL_VALUES[4]=$PL_VALUES[28]="$FORM{'suname'}";


		}else{&ERROR('部隊が存在しません。');}
	last CUSTOM;};
	/^建国$/ && do{
		&DBM_INPORT(P);
#20090531　304が封印　国名によってはエラーが発生するので封印
#		my$checkcname=substr("$FORM{'cname'}",0,8);
#		while (my($key,$value) = each %P){
#			my@VS_VALUE = split(/\s/,$value);
#			if($FORM{'cname'} eq "$VS_VALUE[5]"){
#				&ERROR('同名の国が既に存在します。');
#			}
#			&ERROR('似たような国名がが既に存在します。') if "$VS_VALUE[5]" =~ m/\^$checkcname/;
#		}
		&DBM_INPORT('C');
		my@C=%C;
		my$C=@C/2;
		&ERROR('だーめっ！') if $C >= $COUNTRY_MAX;
#		&ERROR('だーめっ！') if $C > 12;
		&ERROR('同名の国が既に存在します。') if $C{"$FORM{'cname'}"};
		&ERROR('国名の最後に「･」を含める事は出来ません。') if $FORM{'cname'} =~ /･$/i ;
		&ERROR("国名に「$NONE_NATIONALITY」を含める事は出来ません。") if $FORM{'cname'} =~ /$NONE_NATIONALITY$/ ;
		&ERROR("その国名で建国することは出来ません。") if $FORM{'cname'} eq "フォーチュン使用！";
		&ERROR(noName) if !$FORM{'cname'};@CL_VALUES='';$Moto="$PL_VALUES[5]" if $PL_VALUES[5];
		&DBM_INPORT(R);@R_VALUES = split(/\s/,$R{"server"});$R_VALUES[155]++;$flagr=1;
		$PL_VALUES[8]-=$MAKE_COUNTRY;$PL_VALUES[5]="$FORM{'cname'}";$PL_VALUES[28]='';$PL_VALUES[32]++;
		if($PL_VALUES[32] > $PL_VALUES[35]*10){$PL_VALUES[32]=$PL_VALUES[35]*10;}
		$PL_VALUES[0]='220';$PL_VALUES[6]='1';

		#褒章システム	建国の場合は、現在貢献点をクリアする
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
#		if($NewHoushoFlg == 1){
		
#			@HC=split(/!/,$PL_VALUES[50]);
#			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
#			if($HC[1] eq ""){$HC[1] = 0;}
#			if($HC[2] eq ""){$HC[2] = 0;}

#			$HC[1] = 0;
			
#			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		
#		}
				
		$CL_VALUES[0]='#'.$FORM{'cl'};$CL_VALUES[1]=30000;$CL_VALUES[7]=time;$CL_VALUES[39]=$PL_VALUES[39];
		$CL_VALUES[11]="$YOUSAI_HP!$YOUSAI_HP!$DATE";$CL_VALUES[12]="1!1!1!$FORM{'cname'}防衛要塞";$flagc=1;
		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
		$HISTORY="$FORM{'pname'} が<B class=rb1>$FORM{'cname'}</B>を建国。最高指導者に$FORM{'pname'}が就任。" if !$Moto;
		$HISTORY="$FORM{'pname'} が<B class=rb1>$FORM{'cname'}</B>を樹立。$Motoに対して独立を宣言。" if $Moto;
#		$HISTORY="$CONの$FORM{'pname'} が<B class=rb1>$FORM{'cname'}</B>を建国。最高指導者に$FORM{'pname'}が就任。" if !$Moto;
#		$HISTORY="$CONの$FORM{'pname'} が<B class=rb1>$FORM{'cname'}</B>を樹立。$Motoに対して独立を宣言。" if $Moto;
	last CUSTOM;};
	/^解放$/ && do{
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		&ERROR('総帥・隊長以外は使用できません。') if $PL_VALUES[6] eq "0";
		&ERROR('戦闘不能\中は使用できません。') if $PL_VALUES[25] eq "1";
		&ERROR('MPが足りません。オーブを解放する際、MPを800消費します。') if $PL_VALUES[17] < 800;

		require "./$LOG_FOLDER/$HASH_DATA";
#		local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#		local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#		local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#		local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);
	
#		@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
#		@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});

		$a=$FORM{'TSet'};$b=$FORM{'OSet'};
#		&ERROR("$aああ$b");
#		$PL_VALUES[26] = time;
#		if($PL_VALUES[26] >= time-$kk_time*60){}else{$PL_VALUES[26]=time;}
	
#		dbmopen (%PL,"$DBM_P",0666);
#			$PL{"$FORM{'pname'}"}="@PL_VALUES";
#		dbmclose %PL;}

#		&REPAIR(\@PL_VALUES);
#		$PL_VALUES[17] = $PL_VALUES[17] - 800;

		if($FORM{'OSet'} eq "10"){
			local($WN_O,$WLV_O) = split(/!/,$PL_VALUES[10]);
			@WN_sO=split(/\,/,$WEAPON_LIST{"$WN_O"});
			$PL_VALUES[10]="";
		}elsif($FORM{'OSet'} eq "11"){
			local($WN_O,$WLV_O) = split(/!/,$PL_VALUES[11]);
			@WN_sO=split(/\,/,$WEAPON_LIST{"$WN_O"});
			$PL_VALUES[11]="";
		}elsif($FORM{'OSet'} eq "38"){
			local($WN_O,$WLV_O) = split(/!/,$PL_VALUES[38]);
			@WN_sO=split(/\,/,$WEAPON_LIST{"$WN_O"});
			$PL_VALUES[38]="";
		}

		if($HoushoFlg == 1){
			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			#現在貢献点+100
			$HC[0] = $HC[0] + 100;
			$HC[2] = $HC[2] + 100;

			#現在貢献点＞最大貢献点の場合は記録
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
	
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		#貢献値加算
		if($NewHoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}

			$HC[1] = $HC[1] + 10;
			$HC[2] = $HC[2] + 10;
			#総帥の場合、貢献点+10
			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 10;}
			
			if($HC[1] > 9999){$HC[1] = 9999;}
			
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		if($WN_sO[7] =~ m/!87|!88|!89|!8a|!8b|!8c/){

			#オーブダメージを計算
			$OD = 0;
			require "./$LOG_FOLDER/$CLASS_DATA";
			@PL_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

			if($PL_CLASS[2] < 0){$PL_CLASS[2]=int($PL_CLASS[2]/2-0.5);}if($PL_CLASS[2] > 0){$PL_CLASS[2]=int($PL_CLASS[2]/2+0.5);}
			$VIT = int($PL_VALUES[20] * $PL_CLASS[2]);
			$LV = $PL_VALUES[29];
			if($LV > 200){$LV = 200;}
			$EL = 1;#風炎大地水
			$OName="";
			if($WN_sO[7] =~ m/!87/){$OName="サモンイシュタル";$OName2="光のオーブ：";}
			elsif($WN_sO[7] =~ m/!88/){$OName="サモンアスモデ";$OName2="闇のオーブ：";}
			elsif($WN_sO[7] =~ m/!89/){$OName="サモンゾショネル";$OName2="炎のオーブ：";}
			elsif($WN_sO[7] =~ m/!8a/){$OName="サモングルーザ";$OName2="水のオーブ：";}
			elsif($WN_sO[7] =~ m/!8b/){$OName="サモンハーネラ";$OName2="風のオーブ：";}
			elsif($WN_sO[7] =~ m/!8c/){$OName="サモンバーサ";$OName2="大地のオーブ：";}


			if($WN_sO[7] =~ m/!87/ && $PL_VALUES[31] eq "4"){
				$EL = 1.2;
			}elsif($WN_sO[7] =~ m/!88/ && $PL_VALUES[31] eq "5"){
				$EL = 1.2;
			}elsif($WN_sO[7] =~ m/!89/ && $PL_VALUES[31] eq "1"){
				$EL = 1.2;
			}elsif($WN_sO[7] =~ m/!8a/ && $PL_VALUES[31] eq "3"){
				$EL = 1.2;
			}elsif($WN_sO[7] =~ m/!8b/ && $PL_VALUES[31] eq "0"){
				$EL = 1.2;
			}elsif($WN_sO[7] =~ m/!8c/ && $PL_VALUES[31] eq "2"){
				$EL = 1.2;
			}

			$OL = int($WLV_O / 100);

#20181111 UPDATE オーブダメージを上方調整する
#			$OD = int($VIT * $LV * $PL_VALUES[15] / 40000 * $EL * (($OL + 51) / 100));
			$OD = int($VIT * $LV * $PL_VALUES[15] / 40000 * $EL * (($OL + 101) / 100) + int(rand(20000)));

			#ターゲット情報を取得
			$TCon = "";$TTeam = "";
			if($FORM{'TSet'} eq "10"){
				$TCON = $CL_VALUES[6];$TTeam = "";
			}elsif($FORM{'TSet'} eq "11"){
				$TCON = $CL_VALUES[6];$TTeam = "8";
			}elsif($FORM{'TSet'} eq "12"){
				$TCON = $CL_VALUES[6];$TTeam = "9";
			}elsif($FORM{'TSet'} eq "13"){
				$TCON = $CL_VALUES[6];$TTeam = "10";
			}elsif($FORM{'TSet'} eq "20"){
				$TCON = $CL_VALUES[8];$TTeam = "";
			}elsif($FORM{'TSet'} eq "21"){
				$TCON = $CL_VALUES[8];$TTeam = "8";
			}elsif($FORM{'TSet'} eq "22"){
				$TCON = $CL_VALUES[8];$TTeam = "9";
			}elsif($FORM{'TSet'} eq "23"){
				$TCON = $CL_VALUES[8];$TTeam = "10";
			}elsif($FORM{'TSet'} eq "30"){
				$TCON = $CL_VALUES[9];$TTeam = "";
			}elsif($FORM{'TSet'} eq "31"){
				$TCON = $CL_VALUES[9];$TTeam = "8";
			}elsif($FORM{'TSet'} eq "32"){
				$TCON = $CL_VALUES[9];$TTeam = "9";
			}elsif($FORM{'TSet'} eq "33"){
				$TCON = $CL_VALUES[9];$TTeam = "10";
			}elsif($FORM{'TSet'} eq "40"){
				$TCON = $CL_VALUES[10];$TTeam = "";
			}elsif($FORM{'TSet'} eq "41"){
				$TCON = $CL_VALUES[10];$TTeam = "8";
			}elsif($FORM{'TSet'} eq "42"){
				$TCON = $CL_VALUES[10];$TTeam = "9";
			}elsif($FORM{'TSet'} eq "43"){
				$TCON = $CL_VALUES[10];$TTeam = "10";
			}
			#選択国の部隊を取得しないとぬるぽ
			
			$TTT = "";
			while (($C_Name,$C_Value) =each %C) {
				@C_VALUES = split(/\s/,$C_Value);

#				&ERROR("$C_Name");

				#国名
				if($C_Name eq $TCON){

					#部隊を取得
					if($TTeam eq ""){$TTT = "";}
					elsif($TTeam eq "8"){$TTT = $C_VALUES[8];}
					elsif($TTeam eq "9"){$TTT = $C_VALUES[9];}
					elsif($TTeam eq "10"){$TTT = $C_VALUES[10];}

				}

			}

#$OD
#				&ERROR("$TCONあああ$TTT");

			&DBM_INPORT(P);
			dbmopen (%P,"$DBM_P",0666);
			foreach $key (keys %P){
				@VS_VALUES = split(/\s/,$P{$key});
				if($VS_VALUES[5] eq $TCON && ($TTT eq $VS_VALUES[28] || ($TTT eq "" && $VS_VALUES[28] eq ""))){
#				&ERROR("$VS_VALUES[5]");
					&REPAIR(\@VS_VALUES);
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]は$ONameを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15] = int($VS_VALUES[15] - $OD);
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}
				$P{"$key"}="@VS_VALUES";
			}
	
			dbmclose %P;

			if($TTT eq ""){$TTT ="本隊";}

#		$testes = $CL_VALUES[45];
#		$CL_VALUES[45] = time + 1200;
			$message0="<b class=rb3>$PL_VALUES[5]</b>が";
			$message0.="<b class=rb3>$TCONの$TTT</b>に";
			$message0.="$OName2$ONameを解放しました。";

			dbmopen (%DH,"$DBM_H",0666);
				$DH{"$DATE"}="$message0";
			dbmclose %DH;

		}

		$CL_VALUES[45] = time + 1200;
		$flagc=1;
		#$flagp=1;
#	&LOCK;
#	if($flagr){dbmopen (%R,"$DBM_R",0666);$R{"server"}="@R_VALUES";dbmclose %R;}
#	if($flagp){dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;}
#	if($flagc){dbmopen (%CL,"$DBM_C",0666);$CL{"$PL_VALUES[5]"}="@CL_VALUES";dbmclose %CL;}
#	if($HISTORY){dbmopen (%DH,"$DBM_H",0666);$DH{"$DATE"}="$HISTORY";dbmclose %DH;}
#	if($HISTORY2){$DATESA=$DATE+$JIKANSA*60;dbmopen (%DH,"$DBM_H",0666);$DH{"$DATESA"}="$HISTORY2";dbmclose %DH;}
#	&UNLOCK;

	last CUSTOM;};
	/^要塞改名$/ && do{
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		&ERROR('要塞名の最後に「･」を含める事は出来ません。') if $FORM{'yoname'} =~ /･$/i ;
		&ERROR(noName) if !$FORM{'yoname'};&ERROR('国費が足りません。') if $CL_VALUES[1] < $NAME_YOSAI;
		$CL_VALUES[1]-=$NAME_YOSAI;@Y_ST=split(/!/,$CL_VALUES[12]);
		$CL_VALUES[12]="$Y_ST[0]!$Y_ST[1]!$Y_ST[2]!$FORM{'yoname'}";$flagc=1;$flagp=0;
	last CUSTOM;};
	/^解散$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && do{$flagc=1;$flagp=0;
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		$CL_VALUES[2]='' if $FORM{'delunit'} eq "$CL_VALUES[2]";
		$CL_VALUES[3]='' if $FORM{'delunit'} eq "$CL_VALUES[3]";
		$CL_VALUES[4]='' if $FORM{'delunit'} eq "$CL_VALUES[4]";
	last CUSTOM;};
#	/^停戦$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time && do{
#		&DBM_INPORT(P);
#		&DBM_INPORT(C);
#		&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
#
#		$M_AITEX0="$CL_VALUES[6]";
#		$M_AITEX1="$CL_VALUES[8]";
#		$M_AITEX2="$CL_VALUES[9]";
#		$M_AITEX3="$CL_VALUES[10]";
#		&ERROR('戦略勝利時は、停戦宣言を行うことはできません。') if !$C{"$M_AITEX0"} && !$C{"$M_AITEX1"} && !$C{"$M_AITEX2"} && !$C{"$M_AITEX3"};
#
#		$flagc=1;$flagp=1;
#		$CL_VALUES[7]=time;
#		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
#		$HISTORY="$CONの<B class=rb3>$PL_VALUES[5]</B>が停戦を宣言しました。";
##		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>が停戦を宣言しました。";
#	last CUSTOM;};
	/^停戦宣言$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time && do{
		&DBM_INPORT(P);
		&DBM_INPORT(C);
		&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};

		$M_AITEX0="$CL_VALUES[6]";
		$M_AITEX1="$CL_VALUES[8]";
		$M_AITEX2="$CL_VALUES[9]";
		$M_AITEX3="$CL_VALUES[10]";
		&ERROR('戦略勝利時は、停戦宣言を行うことはできません。') if !$C{"$M_AITEX0"} && !$C{"$M_AITEX1"} && !$C{"$M_AITEX2"} && !$C{"$M_AITEX3"};
#		&ERROR("$FORM{'TeiSet'}");
		$flagc=1;$flagp=1;

		if ($FORM{'TeiSet'} eq "1"){
			&ERROR('選択した国は既に滅亡しています。') if !$C{"$M_AITEX0"};
			$aite=$CL_VALUES[6];

			if($CL_VALUES[6] eq $CL_VALUES[8]){
				$CL_VALUES[8]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[6] eq $CL_VALUES[9]){
				$CL_VALUES[9]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[6] eq $CL_VALUES[10]){
				$CL_VALUES[10]="バルダー装備を崇める会かも";
			}

			$CL_VALUES[6] = "バルダー装備を崇める会かも";

		}elsif ($FORM{'TeiSet'} eq "2"){
			&ERROR('選択した国は既に滅亡しています。') if !$C{"$M_AITEX1"};
			$aite=$CL_VALUES[8];

			if($CL_VALUES[8] eq $CL_VALUES[6]){
				$CL_VALUES[6]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[8] eq $CL_VALUES[9]){
				$CL_VALUES[9]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[8] eq $CL_VALUES[10]){
				$CL_VALUES[10]="バルダー装備を崇める会かも";
			}

			$CL_VALUES[8] = "バルダー装備を崇める会かも";

		}elsif ($FORM{'TeiSet'} eq "3"){
			&ERROR('選択した国は既に滅亡しています。') if !$C{"$M_AITEX2"};
			$aite=$CL_VALUES[9];

			if($CL_VALUES[9] eq $CL_VALUES[6]){
				$CL_VALUES[6]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[9] eq $CL_VALUES[8]){
				$CL_VALUES[8]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[9] eq $CL_VALUES[10]){
				$CL_VALUES[10]="バルダー装備を崇める会かも";
			}

			$CL_VALUES[9] = "バルダー装備を崇める会かも";

		}elsif ($FORM{'TeiSet'} eq "4"){
			&ERROR('選択した国は既に滅亡しています。') if !$C{"$M_AITEX3"};
			$aite=$CL_VALUES[10];

			if($CL_VALUES[10] eq $CL_VALUES[6]){
				$CL_VALUES[6]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[10] eq $CL_VALUES[8]){
				$CL_VALUES[8]="バルダー装備を崇める会かも";
			}elsif($CL_VALUES[10] eq $CL_VALUES[9]){
				$CL_VALUES[9]="バルダー装備を崇める会かも";
			}

			$CL_VALUES[10] = "バルダー装備を崇める会かも";

		}

		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}

#		$HISTORY="$CONの<B class=rb3>$PL_VALUES[5]</B>が<B class=rb2>$aite</B>に停戦を宣言しました。";
		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>が<B class=rb2>$aite</B>に停戦を宣言しました。";
	last CUSTOM;};
	/^発動$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && $CL_VALUES[7] < time && do{
		&DBM_INPORT(P);
		&DBM_INPORT(C);
		&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		$flagc=1;$flagp=1;$CL_VALUES[13]=0 if !$CL_VALUES[13];
		$JIKANSA=$CL_VALUES[13];$JIKANSA=15 if $CL_VALUES[13]>14;
		$CL_VALUES[7]=time+10800*$FORM{'kikan'};$PL_VALUES[32]+=1;
		&DBM_INPORT(R);@R_VALUES = split(/\s/,$R{"server"});$R_VALUES[156]++;$flagr=1;
		if($PL_VALUES[32] > $PL_VALUES[35]*10){$PL_VALUES[32]=$PL_VALUES[35]*10;}
		$CL_VALUES[1]-=$FORM{'dmmy'};
		$CL_VALUES[6]="$FORM{'main'}";$CL_VALUES[5]="$FORM{'mname'}";$CL_VALUES[14]="$DATE";
		$CL_VALUES[8]="$FORM{'u1'}";$CL_VALUES[9]="$FORM{'u2'}";$CL_VALUES[10]="$FORM{'u3'}";

		$CL_VALUES[45]=time + $JIKANSA * 60 + 1200;

		if ($CL_VALUES[8] eq $CL_VALUES[6]){$TEKI_1='';}
		elsif ($CL_VALUES[8] ne ''){$TEKI_1="/$CL_VALUES[8]";}
		if ($CL_VALUES[9] eq $CL_VALUES[6]){$TEKI_2='';}
		elsif ($CL_VALUES[9] eq $CL_VALUES[8]){$TEKI_2='';}
		elsif ($CL_VALUES[9] ne ''){$TEKI_2="/$CL_VALUES[9]";}
		if ($CL_VALUES[10] eq $CL_VALUES[6]){$TEKI_3='';}
		elsif ($CL_VALUES[10] eq $CL_VALUES[8]){$TEKI_3='';}
		elsif ($CL_VALUES[10] eq $CL_VALUES[9]){$TEKI_3='';}
		elsif ($CL_VALUES[10] ne ''){$TEKI_3="/$CL_VALUES[10]";}
		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
#		$HISTORY="$CONの<B class=rb3>$PL_VALUES[5]</B>が戦略準備中。$JIKANSA分後に侵攻開始。" if $CL_VALUES[13];
#		$HISTORY2="$CONの<B class=rb3>$PL_VALUES[5]</B>が$FORM{'mname'}を発動。<B class=rb2>$CL_VALUES[6]$TEKI_1$TEKI_2$TEKI_3</B>へ侵攻開始。";
		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>が戦略準備中。$JIKANSA分後に侵攻開始。" if $CL_VALUES[13];
		$HISTORY2="<B class=rb3>$PL_VALUES[5]</B>が$FORM{'mname'}を発動。<B class=rb2>$CL_VALUES[6]$TEKI_1$TEKI_2$TEKI_3</B>へ侵攻開始。";

		#褒章システム	発動時にONの場合、貢献点+100	総帥は、ONOFF関係なしで+100
		if($HoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			
			#現在貢献点+100
			$HC[0] = $HC[0] + 100;

			#現在貢献点＞最大貢献点の場合は記録
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}

			#累計貢献点の計算
			$HC[2] = $HC[2] + 100;

			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && $NP_VALS[26] >= time-1200){

					&REPAIR(\@NP_VALS);

					@HNC=split(/!/,$NP_VALS[50]);

					#現在貢献点+100
					$HNC[0] = $HNC[0] + 100;

					#現在貢献点＞最大貢献点の場合は記録
					if($HNC[0] > $HNC[1]){$HNC[1] = $HNC[0];}
		
					#累計貢献点の計算
					$HNC[2] = $HNC[2] + 100;

					$NP_VALS[50] = "$HNC[0]!$HNC[1]!$HNC[2]!";

					dbmopen (%P,"$DBM_P",0666);
						$P{"$key"}="@NP_VALS";
					dbmclose %P;
				}

			}

		}

	last CUSTOM;};
	$FORM{'yousaiCheck'} && $PL_VALUES[6] != 0 && $PL_VALUES[5] && do{
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		@Y_HP=split(/!/,$CL_VALUES[11]);
		@Y_ST=split(/!/,$CL_VALUES[12]);$flagc=1;
		&DBM_INPORT(P);

		$YO_HP=int($Y_HP[1]*0.3)-37000;
		$YO_STR=int($Y_ST[0]*400)+9600;
		$YO_VIT=int($Y_ST[1]*400)+9600;
		$YO_AGI=int($Y_ST[2]*400)+9600;

		&ERROR('国費が足りません。') if ($FORM{'Cmode'} ne "回復小" && $FORM{'Cmode'} ne "回復大" && $PL_VALUES[6] eq "-1" && $CL_VALUES[1] < 150000);
		if ($FORM{'Cmode'} eq "回復小"){$Y_HP[0]+=int($Y_HP[1]*0.25);$CL_VALUES[1]-=6000;}
		if ($FORM{'Cmode'} eq "回復大"){$Y_HP[0]+=int($Y_HP[1]*0.8);$CL_VALUES[1]-=30000;}
		if ($FORM{'Cmode'} eq "HP強化"){$Y_HP[1]+=5000;$CL_VALUES[1]-=$YO_HP;}
		if ($FORM{'Cmode'} eq "攻撃力強化"){$Y_ST[0]++;$CL_VALUES[1]-=$YO_STR;}
		if ($FORM{'Cmode'} eq "防御力強化"){$Y_ST[1]++;$CL_VALUES[1]-=$YO_VIT;}
		if ($FORM{'Cmode'} eq "命中力強化"){$Y_ST[2]++;$CL_VALUES[1]-=$YO_AGI;}
		if ($FORM{'Cmode'} eq "属性変更"){$CL_VALUES[47]=$FORM{'Zsentaku'};$CL_VALUES[1]-=50000;}
		$CL_VALUES[11]="$Y_HP[0]!$Y_HP[1]!$Y_HP[2]";
		$CL_VALUES[12]="$Y_ST[0]!$Y_ST[1]!$Y_ST[2]!$Y_ST[3]";
	last CUSTOM;};
	$FORM{'cardCheck'} && $PL_VALUES[6] != 0 && $PL_VALUES[5] && do{
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		&DBM_INPORT(P);$flagc=1;$flagp=0;
		if ($FORM{'Emode'} eq "カード破棄"){$CL_VALUES[15]='';}

		#フォーチュンの場合、以下の効果にランダムで振り替え (フール　マジシャン)
		$Card_F = 0;
		if($FORM{'Emode'} eq 'フォーチュン'){
			$Card_F = 1;
			if(int(rand(100)) > 90){
				$FORM{'Emode'} = "マジシャン";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "プリエステス";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "フール";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "ラヴァーズ";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "チャリオット";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "ハーミット";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "エンペラー";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "ジャスティス";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "エンプレス";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "デス";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "スター";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "デビル";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "サン";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "タワー";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "ムーン";
			}else{
				$FORM{'Emode'} = "ジャッジメント";
			}
		}
#		&ERROR("$FORM{'Emode'}と$FORM{'chisa'}");
		if($CL_VALUES[15] || $MENTE){
			dbmopen (%P,"$DBM_P",0666);
		foreach $key (keys %P){
			@VS_VALUES = split(/\s/,$P{$key});
		#フール
			if ($FORM{'Emode'} eq "フール"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}" && $VS_VALUES[0] < 30 && ($DATE-$VS_VALUES[26]) > 1200){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はフールのカードを発動！";
				$HOUTIDATE="$key<>$VS_VALUES[0]<>$VS_VALUES[1]<>$VS_VALUES[2]<>$VS_VALUES[3]<>$VS_VALUES[4]<>$VS_VALUES[5]<>$VS_VALUES[6]<>$VS_VALUES[7]<>$VS_VALUES[8]<>$VS_VALUES[9]<>$VS_VALUES[10]<>$VS_VALUES[11]<>$VS_VALUES[12]<>$VS_VALUES[13]<>$VS_VALUES[14]<>$VS_VALUES[15]<>$VS_VALUES[16]<>$VS_VALUES[17]<>$VS_VALUES[18]<>$VS_VALUES[19]<>$VS_VALUES[20]<>$VS_VALUES[21]<>$VS_VALUES[22]<>$VS_VALUES[23]<>$VS_VALUES[24]<>$VS_VALUES[25]<>$VS_VALUES[26]<>$VS_VALUES[27]<>$VS_VALUES[28]<>$VS_VALUES[29]<>$VS_VALUES[30]<>$VS_VALUES[31]<>$VS_VALUES[32]<>$VS_VALUES[33]<>$VS_VALUES[34]<>$VS_VALUES[35]<>$VS_VALUES[36]<>$VS_VALUES[37]<>$VS_VALUES[38]<>$VS_VALUES[39]<>$VS_VALUES[40]<>$VS_VALUES[41]<>$VS_VALUES[42]<>$VS_VALUES[43]<>$VS_VALUES[44]<>$VS_VALUES[45]<>$VS_VALUES[46]<>$VS_VALUES[47]<>$VS_VALUES[48]<>$VS_VALUES[49]<>$VS_VALUES[50]<>$VS_VALUES[51]<>$VS_VALUES[52]<>$VS_VALUES[53]<>$VS_VALUES[54]<>$VS_VALUES[55]<>$VS_VALUES[56]<>$VS_VALUES[57]<>$VS_VALUES[58]<>$VS_VALUES[59]<>$VS_VALUES[60]<>$VS_VALUES[61]<>$VS_VALUES[62]<>$VS_VALUES[63]<>$VS_VALUES[64]<>$VS_VALUES[65]<>$VS_VALUES[66]<>$VS_VALUES[67]<>$VS_VALUES[68]<>$VS_VALUES[69]<>$VS_VALUES[70]<>$VS_VALUES[71]<>$VS_VALUES[72]<>$VS_VALUES[73]<>$VS_VALUES[74]<>$VS_VALUES[75]<>$VS_VALUES[76]<>$VS_VALUES[77]<>$VS_VALUES[78]<>$VS_VALUES[79]<>\n";
				if(!open(OUT,">$LOG_FOLDER2/$key.cgi")){&ERROR('Error',"バックアップ失敗。「$key」このユニット名を管理人に報告して下さい。");}
				print OUT $HOUTIDATE;close(OUT);
				chmod(0666,"$LOG_FOLDER2/$key.cgi");
				delete $P{"$key"};
				}
			}
		#マジシャン
			if ($FORM{'Emode'} eq "マジシャン"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はマジシャンのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=20000+int(rand(20000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#プリエステス
			if ($FORM{'Emode'} eq "プリエステス"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はプリエステスのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						if(($DATE-$VS_VALUES[26]) < 1200){
							$VS_VALUES[15]+=int($VS_VALUES[16]*0.3);
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#エンプレス
			if ($FORM{'Emode'} eq "エンプレス"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はエンプレスのカードを発動！";
					if(($DATE-$VS_VALUES[26]) < 1200){
						$VS_VALUES[25]=0;
					}
				}$P{"$key"}="@VS_VALUES";}
		#エンペラー
			if ($FORM{'Emode'} eq "エンペラー"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はエンペラーのカードを発動！";
					if(($DATE-$VS_VALUES[26]) < 1200){
						$VS_VALUES[17]+=1000;
					}
				}$P{"$key"}="@VS_VALUES";}
		#ラヴァーズ
			if ($FORM{'Emode'} eq "ラヴァーズ"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]はラヴァーズのカードを発動！";
					$VS_VALUES[25]=1;
				}$P{"$key"}="@VS_VALUES";}
		#チャリオット
			if ($FORM{'Emode'} eq "チャリオット"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はチャリオットのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=20000+int(rand(15000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#ハーミット
			if ($FORM{'Emode'} eq "ハーミット"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はハーミットのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=1000+int(rand(60000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#ジャスティス
			if ($FORM{'Emode'} eq "ジャスティス"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はジャスティスのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=20000+int(rand(22000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#デス
#			if ($FORM{'Emode'} eq "デス"){
#				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
#				&REPAIR(\@VS_VALUES);
#				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はデスのカードを発動！";

#					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
#						if($VS_VALUES[15] <= ($VS_VALUES[16]/2)){
#							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
#							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
#							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
#							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
#						}
#					}
#				}$P{"$key"}="@VS_VALUES";}
			if ($FORM{'Emode'} eq "デス"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);$VS_VALUES[1]="$DATE!$PL_VALUES[5]はデスのカードを発動！";
					if($VS_VALUES[0] <= 99 && ($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16])){
						$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
						($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
#					}else{
#						$VS_VALUES[15]=$VS_VALUES[16];$VS_VALUES[25]=0;
					}
				}$P{"$key"}="@VS_VALUES";}
		#テンパランス
			if ($FORM{'Emode'} eq "テンパランス"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はテンパランスのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						if(($DATE-$VS_VALUES[26]) < 1200){
							$VS_VALUES[15]+=int($VS_VALUES[16]*0.6);
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#デビル
			if ($FORM{'Emode'} eq "デビル"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はデビルのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=int(rand(65000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#タワー
			if ($FORM{'Emode'} eq "タワー"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はタワーのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=8000+int(rand(5000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#スター
			if ($FORM{'Emode'} eq "スター"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はスターのカードを発動！";
					if(($DATE-$VS_VALUES[26]) < 1200){
						$VS_VALUES[17]+=500;
					}
				}$P{"$key"}="@VS_VALUES";}
		#ムーン
			if ($FORM{'Emode'} eq "ムーン"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);$VS_VALUES[1]="$DATE!$PL_VALUES[5]はムーンのカードを発動！";
					if($VS_VALUES[0] >= 200){
						$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
						($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
					}else{
						$VS_VALUES[15]=$VS_VALUES[16];$VS_VALUES[25]=0;
					}
				}$P{"$key"}="@VS_VALUES";}
		#サン
			if ($FORM{'Emode'} eq "サン"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}" || $VS_VALUES[5] eq $PL_VALUES[5]){
				&REPAIR(\@VS_VALUES);$VS_VALUES[1]="$DATE!$PL_VALUES[5]はサンのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){

						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 100;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 95;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 83;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 71;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 59;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 47;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 35;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 23;
						$VS_VALUES[15]-=int(rand(18000)) if $VS_VALUES[12] <= 11;

						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#ジャッジメント
			if ($FORM{'Emode'} eq "ジャッジメント"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]はジャッジメントのカードを発動！";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=30000+int(rand(30000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;戦闘不\能\。");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
			#デバッグ1
				if ($FORM{'Emode'} eq "デバッグ1"){
					$VS_VALUES[8]=1000000;$VS_VALUES[16]=80000;$VS_VALUES[18]=4000;
					$VS_VALUES[19]=50;$VS_VALUES[20]=50;$VS_VALUES[21]=50;$VS_VALUES[22]=50;$VS_VALUES[29]=100;
					$VS_VALUES[24]=1000;
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]はデバッグモードを発動！";
					$P{"$key"}="@VS_VALUES";
				}
			#デバッグ2
				if ($FORM{'Emode'} eq "デバッグ2"){
					$VS_VALUES[15]=100;
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]はデバッグモードを発動！";
					$P{"$key"}="@VS_VALUES";
				}
			}
			dbmclose %P;

			dbmopen (%CLA,"$DBM_C",0666);
			while (my($key,$value) = each %CLA){
				my@VL_VALUE = split(/\s/,$value);
#				$x.=$key;
#				if ($FORM{'Emode'} eq 'フォーチュン'){if("$key" eq "$FORM{'chisa'}"){$VL_VALUE[5]="";$VL_VALUE[6]="フォーチュン使用！";$VL_VALUE[7]=$DATE;$VL_VALUE[8]="";$VL_VALUE[9]="";$VL_VALUE[10]="";$VL_VALUE[14]="";$VL_VALUE[37]=$DATE+300;}$CLA{"$key"}="@VL_VALUE";}
				if ($FORM{'Emode'} eq 'ハングドマン'){if("$key" eq "$FORM{'chisa'}"){$VL_VALUE[1]-=30000+int(rand(80000));if($VL_VALUE[1] < 0){$VL_VALUE[1]=0;}}$CLA{"$key"}="@VL_VALUE";}
			}
			dbmclose %CLA;

#			&ERROR("フォーチュンだよ$x");

			if($Card_F eq "1"){
				$Effect_F="($FORM{'Emode'})";
				$FORM{'Emode'}="フォーチュン";
			}else{$Effect_F="";}

			$message="<b class=rb3>$PL_VALUES[5]</b>が";
			$message.="<b class=rb3>$FORM{'chisa'}</b>に" if $CL_VALUES[15] =~ m/a|b|g|h|j|k|l|m|n|p|q|s|t|u/;
			$message.="$FORM{'Emode'}のカード$Effect_Fを発動しました。";

			dbmopen (%DH,"$DBM_H",0666);
				$DH{"$DATE"}="$message";
			dbmclose %DH;

			if ($FORM{'Emode'} eq 'ハイエロファント'){$CL_VALUES[5]="";$CL_VALUES[7]=$DATE;$CL_VALUES[8]="";$CL_VALUES[9]="";$CL_VALUES[10]="";$CL_VALUES[14]="";}
			if ($FORM{'Emode'} eq 'ストレングス'){$CL_VALUES[1]+=30000+int(rand(80000));if($CL_VALUES[1] > 200000){$CL_VALUES[1]=200000;}}
			if ($FORM{'Emode'} eq 'ワールド'){$CL_VALUES[38]=$DATE+3600;}
		}
		$CL_VALUES[15]='';

	last CUSTOM;};

	/^応戦$/ && $PL_VALUES[5] && $PL_VALUES[6] && $CL_VALUES[7] && do{
		&DBM_INPORT(C);&ERROR('国が存在しません。') if !$C{"$PL_VALUES[5]"};
		if ($FORM{'main'} and $FORM{'main'} ne '応戦先 '){$CL_VALUES[6]="$FORM{'main'}";$CNAME[0]=$FORM{'main'};$c++;}
		if ($FORM{'u1'} and $FORM{'u1'} ne '応戦先 '){$CL_VALUES[8]="$FORM{'u1'}";$CNAME[1]=$FORM{'u1'};}
		if ($FORM{'u2'} and $FORM{'u2'} ne '応戦先 '){$CL_VALUES[9]="$FORM{'u2'}";$CNAME[2]=$FORM{'u2'};}
		if ($FORM{'u3'} and $FORM{'u3'} ne '応戦先 '){$CL_VALUES[10]="$FORM{'u3'}";$CNAME[3]=$FORM{'u3'};}
		$flagc=1;$flagp=0;$CL_VALUES[14]="0";
		$CL_FRAG="$CL_VALUES[7]";$CL_VALUES[1]-=$FORM{'dmmy'};
		if($CL_FRAG > time){$CL_VALUES[7]+=1800*$FORM{'kikan'};}
		else{$CL_VALUES[7]=time+1800*$FORM{'kikan'};$CL_VALUES[5]="応戦開始";}

		$CL_VALUES[45] = time;

		if ($CNAME[1] eq $CNAME[0]){$TEKI_1='';}
		elsif ($c && $CNAME[1] ne ''){$TEKI_1="/$CNAME[1]";}
		elsif (!$c && $CNAME[1] ne ''){$TEKI_1="$CNAME[1]";$c++;}
		if ($CNAME[2] eq $CNAME[0]){$TEKI_2='';}
		elsif ($CNAME[2] eq $CNAME[1]){$TEKI_2='';}
		elsif ($c && $CNAME[2] ne ''){$TEKI_2="/$CNAME[2]";}
		elsif (!$c && $CNAME[2] ne ''){$TEKI_2="$CNAME[2]";$c++;}
		if ($CNAME[3] eq $CNAME[0]){$TEKI_3='';}
		elsif ($CNAME[3] eq $CNAME[1]){$TEKI_3='';}
		elsif ($CNAME[3] eq $CNAME[2]){$TEKI_3='';}
		elsif ($c && $CNAME[3] ne ''){$TEKI_3="/$CNAME[3]";}
		elsif (!$c && $CNAME[3] ne ''){$TEKI_3="$CNAME[3]";$c++;}
		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
#		$HISTORY="$CONの<B class=rb3>$PL_VALUES[5]</B>が、<B class=rb2>$CNAME[0]$TEKI_1$TEKI_2$TEKI_3</B>に応戦開始。";
		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>が、<B class=rb2>$CNAME[0]$TEKI_1$TEKI_2$TEKI_3</B>に応戦開始。";
	last CUSTOM;};
	/^隊長就任$/ && $PL_VALUES[5] && !$PL_VALUES[6] && do{&DBM_INPORT(P);
		while (my($key,$value) = each %P){my@VS_VALUE = split(/\s/,$value);
#			if($FORM{'team'} eq ""){&ERROR('エラー');}
			if($FORM{'team'} eq "$VS_VALUE[28]" && $VS_VALUE[6] == -1){
				&ERROR('別の人物が既に就任しています。');
			}
		}
		if($FORM{'team'} ne ""){$PL_VALUES[6]='-1';$PL_VALUES[28]="$FORM{'team'}";}
	last CUSTOM;};
	/^総帥就任$/ && $PL_VALUES[5] && $PL_VALUES[6] == 0 && do{&DBM_INPORT(P);
		while (my($key,$value) = each %P){my@VS_VALUE = split(/\s/,$value);
			if($PL_VALUES[5] eq "$VS_VALUE[5]" && $VS_VALUE[6] == 1){&ERROR('別の人物が既に就任しています。');}
		}
		$PL_VALUES[6]='1';$PL_VALUES[28]='';$PL_VALUES[0]='220';
		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
#		$HISTORY="$CONで$FORM{'pname'} の総帥就任を <B class=rb1>$PL_VALUES[5]</B>議会が承認。$FORM{'pname'}に全指揮権委任。";
		$HISTORY="$FORM{'pname'} の総帥就任を <B class=rb1>$PL_VALUES[5]</B>議会が承認。$FORM{'pname'}に全指揮権委任。";
	last CUSTOM;};
	/^スキル強化$/ && do{&DBM_INPORT(P);
		require "./$LOG_FOLDER/$HASH_DATA";
		local($WN_S,$WLV_S,$WSEnt) = split(/!/,$PL_VALUES[41]);
		local($WN_T,$WLV_T,$WTEnt) = split(/!/,$PL_VALUES[42]);
		local($WN_U,$WLV_U,$WUEnt) = split(/!/,$PL_VALUES[43]);

		if($WSEnt < 100){
			if($WSEnt eq ""){$WSEnt = 0;}
			$Flg_EntSkill = 0;
			if($WLV_S >= 9900){
				$Flg_EntSkill = 1;
			}elsif($WN_S == $WN_T){
				$Flg_EntSkill = 2;
			}elsif($WN_S == $WN_U){
				$Flg_EntSkill = 3;
			}

			if($Flg_EntSkill == 0){}
			elsif($Flg_EntSkill == 1){$WSEnt = $WSEnt + 1;$WLV_S = 0;}
			elsif($Flg_EntSkill == 2){$WSEnt = $WSEnt + 1;$WLV_S = 0;$PL_VALUES[42] = "";}
			elsif($Flg_EntSkill == 3){$WSEnt = $WSEnt + 1;$WLV_S = 0;$PL_VALUES[43] = "";}

			$PL_VALUES[41] = "$WN_S!$WLV_S!$WSEnt";

		}
	last CUSTOM;};
	/^武具初期化$/ && do{&DBM_INPORT(P);
		require "./$LOG_FOLDER/$HASH_DATA";
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);

		if($PL_VALUES[8] >= 5000000){
			$PL_VALUES[8] = $PL_VALUES[8] - 5000000;
			$WAEnt = 0;

			$PL_VALUES[9] = "$WN_A!$WLV_A!$WAEnt!$WA03!$WA04!$WA05!$WA06!$WA07!$WA08!$WA09!$WA10!$WA11!$WA12!$WA13!$WA14!$WA15!$WA16!$WA17!$WA18!$WA19!$WA20!$WA21!$WA22!$WA23!$WA24!$WA25!$WA26!$WA27!$WA28!$WA29!$WA30!$WA31!$WA32!$WA33!$WA34!$WA35!$WA36!$WA37!$WA38!$WA39!$WA40!$WA41!$WA42";

		}
		
	last CUSTOM;};
	/^武具強化$/ && do{&DBM_INPORT(P);
		require "./$LOG_FOLDER/$HASH_DATA";
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);

		if($WAEnt eq ""){$WAEnt = 0;}
		$EntCost = ($WAEnt + 1) * 100000;
		if($PL_VALUES[8] >= $EntCost && $WAEnt < 100){
			$PL_VALUES[8] = $PL_VALUES[8] - $EntCost;
			$WAEnt = $WAEnt + 1;

			#強化時、低確率でリセットされずに付与されたエンチャントが+1
			if($WAEnt > rand(1001)){
			
				if(10 > rand(100) && $WA03 > 0 && $WA03 < 10){$WA03 = $WA03 + 1;}
				if(10 > rand(100) && $WA04 > 0 && $WA04 < 10){$WA04 = $WA04 + 1;}
				if(10 > rand(100) && $WA05 > 0 && $WA05 < 10){$WA05 = $WA05 + 1;}
				if(10 > rand(100) && $WA06 > 0 && $WA06 < 10){$WA06 = $WA06 + 1;}
				if(10 > rand(100) && $WA07 > 0 && $WA07 < 10){$WA07 = $WA07 + 1;}
				if(10 > rand(100) && $WA08 > 0 && $WA08 < 10){$WA08 = $WA08 + 1;}
				if(10 > rand(100) && $WA09 > 0 && $WA09 < 10){$WA09 = $WA09 + 1;}
				if(10 > rand(100) && $WA10 > 0 && $WA10 < 10){$WA10 = $WA10 + 1;}
				if(10 > rand(100) && $WA11 > 0 && $WA11 < 10){$WA11 = $WA11 + 1;}
				if(10 > rand(100) && $WA12 > 0 && $WA12 < 10){$WA12 = $WA12 + 1;}
				if(10 > rand(100) && $WA13 > 0 && $WA13 < 10){$WA13 = $WA13 + 1;}
				if(10 > rand(100) && $WA14 > 0 && $WA14 < 10){$WA14 = $WA14 + 1;}
				if(10 > rand(100) && $WA15 > 0 && $WA15 < 10){$WA15 = $WA15 + 1;}
				if(10 > rand(100) && $WA16 > 0 && $WA16 < 10){$WA16 = $WA16 + 1;}
				if(10 > rand(100) && $WA17 > 0 && $WA17 < 10){$WA17 = $WA17 + 1;}
				if(10 > rand(100) && $WA18 > 0 && $WA18 < 10){$WA18 = $WA18 + 1;}
				if(10 > rand(100) && $WA19 > 0 && $WA19 < 10){$WA19 = $WA19 + 1;}
				if(10 > rand(100) && $WA20 > 0 && $WA20 < 10){$WA20 = $WA20 + 1;}
				if(10 > rand(100) && $WA21 > 0 && $WA21 < 10){$WA21 = $WA21 + 1;}
				if(10 > rand(100) && $WA22 > 0 && $WA22 < 10){$WA22 = $WA22 + 1;}
				if(10 > rand(100) && $WA23 > 0 && $WA23 < 10){$WA23 = $WA23 + 1;}
				if(10 > rand(100) && $WA24 > 0 && $WA24 < 10){$WA24 = $WA24 + 1;}
				if(10 > rand(100) && $WA25 > 0 && $WA25 < 10){$WA25 = $WA25 + 1;}
				if(10 > rand(100) && $WA26 > 0 && $WA26 < 10){$WA26 = $WA26 + 1;}
				if(10 > rand(100) && $WA27 > 0 && $WA27 < 10){$WA27 = $WA27 + 1;}
				if(10 > rand(100) && $WA28 > 0 && $WA28 < 10){$WA28 = $WA28 + 1;}
				if(10 > rand(100) && $WA29 > 0 && $WA29 < 10){$WA29 = $WA29 + 1;}
				if(10 > rand(100) && $WA30 > 0 && $WA30 < 10){$WA30 = $WA30 + 1;}
				if(10 > rand(100) && $WA31 > 0 && $WA31 < 10){$WA31 = $WA31 + 1;}
				if(10 > rand(100) && $WA32 > 0 && $WA32 < 10){$WA32 = $WA32 + 1;}
				if(10 > rand(100) && $WA33 > 0 && $WA33 < 10){$WA33 = $WA33 + 1;}
			
			
			}



			$PL_VALUES[9] = "$WN_A!$WLV_A!$WAEnt!$WA03!$WA04!$WA05!$WA06!$WA07!$WA08!$WA09!$WA10!$WA11!$WA12!$WA13!$WA14!$WA15!$WA16!$WA17!$WA18!$WA19!$WA20!$WA21!$WA22!$WA23!$WA24!$WA25!$WA26!$WA27!$WA28!$WA29!$WA30!$WA31!$WA32!$WA33!$WA34!$WA35!$WA36!$WA37!$WA38!$WA39!$WA40!$WA41!$WA42";
		}

	last CUSTOM;};

}
	&ERROR('資金が足りません。') if $PL_VALUES[8] < 0 || $CL_VALUES[1] < 0;
	if($flagr){dbmopen (%R,"$DBM_R",0666);$R{"server"}="@R_VALUES";dbmclose %R;}
	if($flagp){dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;}
	if($flagc){dbmopen (%CL,"$DBM_C",0666);$CL{"$PL_VALUES[5]"}="@CL_VALUES";dbmclose %CL;}
	if($HISTORY){dbmopen (%DH,"$DBM_H",0666);$DH{"$DATE"}="$HISTORY";dbmclose %DH;}
	if($HISTORY2){$DATESA=$DATE+$JIKANSA*60;dbmopen (%DH,"$DBM_H",0666);$DH{"$DATESA"}="$HISTORY2";dbmclose %DH;}
	&UNLOCK;
}


1;

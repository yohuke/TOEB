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
<noscript>JavaScript�Ή��u���E�U�ł��V�щ������B</noscript>
	-----END-----
}
sub CUSTOMIZE{
#	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
#		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
#	@pairs = split(/\,/, $DUMMY{'EB'});
#		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIE�������ɂȂ��Ă��܂��B') if !$COOKIE{'pname'};
#	&ERROR('Error','���j�b�g�ƃ��[�U��ID����v���Ă��܂���B') if $COOKIE{'pname'} ne "$FORM{pname}";
#	&LOCK;
#	&DBM_CONVERT('P',"$FORM{pname}");$flagp=1;
#	&DBM_CONVERT('C',"$PL_VALUES[5]") if $PL_VALUES[5];
#	&UNLOCK;
#	&ERROR('PwdError','�p�X���[�h���Ԉ���Ă��鋰�ꂪ����܂��B') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
#	&ERROR('COOKIE�������ɂȂ��Ă��܂��B') if !$COOKIE{'pname'};
#	&ERROR('Error','���j�b�g�ƃ��[�U��ID����v���Ă��܂���B') if $COOKIE{'pname'} ne "$FORM{pname}";
	&LOCK;
	&DBM_CONVERT('P',"$FORM{pname}");$flagp=1;
	&DBM_CONVERT('C',"$PL_VALUES[5]") if $PL_VALUES[5];
#	&ERROR('PwdError','�p�X���[�h���Ԉ���Ă��鋰�ꂪ����܂��B') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";
	&ERROR('PwdError','�p�X���[�h���Ԉ���Ă��鋰�ꂪ����܂��B') if crypt ($FORM{'pass'},eb) ne "$PL_VALUES[2]";
	
	$PL_VALUES[5]='' if $PL_VALUES[5] && !@CL_VALUES;
	$PL_VALUES[6]='0' if !$PL_VALUES[5];
	if ($PL_VALUES[28]){
		foreach ("$CL_VALUES[2]","$CL_VALUES[3]","$CL_VALUES[4]"){if ($PL_VALUES[28] eq "$_") {$DeleteFlag=1;}}
		if (!$DeleteFlag){$PL_VALUES[6]=$PL_VALUES[28]="";}
	}
$_="$FORM{'Cmode'}";
CUSTOM:{
	/^���p$/ && do{	$SW=$PL_VALUES[10] if $FORM{'sellw'}==1;$SW=$PL_VALUES[11] if $FORM{'sellw'}==2;$SW=$PL_VALUES[38] if $FORM{'sellw'}==3;
		$SW=$PL_VALUES[41] if $FORM{'sellw'}==4;$SW=$PL_VALUES[42] if $FORM{'sellw'}==5;$SW=$PL_VALUES[43] if $FORM{'sellw'}==6;$SW=$PL_VALUES[46] if $FORM{'sellw'}==7;
		my($wk,$wl)= split(/!/,$SW);my@www=split(/\,/,$WEAPON_LIST{"$wk"});
		&ERROR('���[�߂��I') if $www[7] =~ m/!zd/;
		&ERROR('����Ȃ���`') if $FORM{'sellw'}==0;
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
	/^�Y���$/ && do{
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});
		&ERROR("�V�X�e���G���[") if $AbiSys == 0;
		$SW=$ABI_A if $FORM{'sellAbi'}==1;$SW=$ABI_B if $FORM{'sellAbi'}==2;$SW=$ABI_C if $FORM{'sellAbi'}==3;
		&ERROR('�Y����Ȃ�') if $FORM{'sellAbi'}==0;
		
		if($FORM{'sellAbi'}==1 && $ABI_A ne ""){
			$ABI_A = "";
			$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			
			#�ő�HP�A�b�v��Y���ꍇ
			if($ABI_sA[2] =~ m/!A0034/){
			
				#���ɍő�HP�A�b�v�������Ă��Ȃ��ꍇ�Ɍ���A�ő�HP-20000���s��
				if($ABI_sB[2] !~ m/!A0034/ && $ABI_sC[2] !~ m/!A0034/){$PL_VALUES[16]-=20000;}
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}

			}
			#�ő�MP�A�b�v��Y���ꍇ
			if($ABI_sA[2] =~ m/!A0035/){
			
				#���ɍő�MP�A�b�v�������Ă��Ȃ��ꍇ�Ɍ���A�ő�MP-1000���s��
				if($ABI_sB[2] !~ m/!A0035/ && $ABI_sC[2] !~ m/!A0035/){$PL_VALUES[18]-=1000;}
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}

			}
			
		}
		elsif($FORM{'sellAbi'}==2 && $ABI_B ne ""){
			$ABI_B = "";
			$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";
			
			#�ő�HP�A�b�v��Y���ꍇ
			if($ABI_sB[2] =~ m/!A0034/){
			
				#���ɍő�HP�A�b�v�������Ă��Ȃ��ꍇ�Ɍ���A�ő�HP-20000���s��
				if($ABI_sA[2] !~ m/!A0034/ && $ABI_sC[2] !~ m/!A0034/){$PL_VALUES[16]-=20000;}
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}

			}
			#�ő�MP�A�b�v��Y���ꍇ
			if($ABI_sB[2] =~ m/!A0035/){
			
				#���ɍő�MP�A�b�v�������Ă��Ȃ��ꍇ�Ɍ���A�ő�MP-1000���s��
				if($ABI_sA[2] !~ m/!A0035/ && $ABI_sC[2] !~ m/!A0035/){$PL_VALUES[18]-=1000;}
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}

			}

		}
		elsif($FORM{'sellAbi'}==3 && $ABI_C ne ""){
			$ABI_C = "";
			$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";

			#�ő�HP�A�b�v��Y���ꍇ
			if($ABI_sC[2] =~ m/!A0034/){
			
				#���ɍő�HP�A�b�v�������Ă��Ȃ��ꍇ�Ɍ���A�ő�HP-20000���s��
				if($ABI_sB[2] !~ m/!A0034/ && $ABI_sA[2] !~ m/!A0034/){$PL_VALUES[16]-=20000;}
				if($PL_VALUES[15]>$PL_VALUES[16]){$PL_VALUES[15]=$PL_VALUES[16];}

			}
			#�ő�MP�A�b�v��Y���ꍇ
			if($ABI_sC[2] =~ m/!A0035/){
			
				#���ɍő�MP�A�b�v�������Ă��Ȃ��ꍇ�Ɍ���A�ő�MP-1000���s��
				if($ABI_sB[2] !~ m/!A0035/ && $ABI_sA[2] !~ m/!A0035/){$PL_VALUES[18]-=1000;}
				if($PL_VALUES[17]>$PL_VALUES[18]){$PL_VALUES[17]=$PL_VALUES[18];}

			}

		}

	last CUSTOM;};
	
	/^�Z�p���ёւ�$/ && do{
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

	/^�Z�p�K��$/ && do{
		local($ABI_FLG,$ABI_A,$ABI_B,$ABI_C) = split(/!/,$PL_VALUES[52]);
		@ABI_sA=split(/\,/,$ABINAME_LIST{"$ABI_A"});
		@ABI_sB=split(/\,/,$ABINAME_LIST{"$ABI_B"});
		@ABI_sC=split(/\,/,$ABINAME_LIST{"$ABI_C"});
		my@www=split(/\,/,$ABINAME_LIST{"$FORM{'buyabi'}"});
#		if(length($FORM{'buyw'}) == 2){&ERROR("���̕���͔����܂���B");}

		&ERROR("AP������܂���") if $PL_VALUES[53] < $www[1];
#		&ERROR("$FORM{'buyabi'}");
		$PL_VALUES[53]-=$www[1];

		if($ABI_sA[0] eq ""){$ABI_A = "$FORM{'buyabi'}";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
		elsif($ABI_sB[0] eq ""){$ABI_B = "$FORM{'buyabi'}";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
		elsif($ABI_sC[0] eq ""){$ABI_C = "$FORM{'buyabi'}";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}

		#�ő�HP�A�b�v
		if($www[2] =~ m/!A0034/){
			if($ABI_sA[2] !~ m/!A0034/ && $ABI_sB[2] !~ m/!A0034/ && $ABI_sC[2] !~ m/!A0034/){$PL_VALUES[16]+=20000;}
		}
		#�ő�MP�A�b�v
		if($www[2] =~ m/!A0035/){
			if($ABI_sA[2] !~ m/!A0035/ && $ABI_sB[2] !~ m/!A0035/ && $ABI_sC[2] !~ m/!A0035/){$PL_VALUES[18]+=1000;}
		}

		#�H�H�H�H
		if($www[2] =~ m/!A0077/){
			my@al=keys %ABINAME_LIST;$alw=@al;
			$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
			@q=split(/\,/,$ABINAME_LIST{"$gw"});
			#���g�����������Ă��܂����ꍇ�́A�������K�ŷد
			if($gw eq "1076a"){$gw = "1060a";}
			#�ő�A�b�v�n���͂���ŉ��������
			if($gw eq "1033a"){$gw = "1082a";}
			if($gw eq "1034a"){$gw = "1083a";}
			if($ABI_A eq "1076a"){$ABI_A = "$gw";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
			if($ABI_B eq "1076a"){$ABI_B = "$gw";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
			if($ABI_C eq "1076a"){$ABI_C = "$gw";$PL_VALUES[52] = "$ABI_FLG!$ABI_A!$ABI_B!$ABI_C";}
		}

	last CUSTOM;};

	/^�V���b�t�����s$/ && do{	
		&ERROR('������������܂���B') if $PL_VALUES[8] < 2000000;

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
#			$ent="!0";	#�����ł͑����iEXP���N���A���Ȃ�

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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
				}
				
				#�}�W�b�N�t�@�C���h�@���h�����|A30
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
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
					$MFUP = $MFUP * 0.9;
				
				}

#&ERROR("��$q[14]");
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
					$MFUP = $MFUP * 0.9;
					
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
				
#				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi!$ent_dl!$ent_mnb!$ent_kabok!$ent_kabog!$ent_tore!$ent_mf!$ent_res!$ent_fireb!$ent_waterb!$ent_earthb!$ent_windb!$ent_saintb!$ent_darkb!$ent_fireg!$ent_waterg!$ent_earthg!$ent_windg!$ent_saintg!$ent_darkg!$ent_img!$ent_gou!$ent_hhp!$ent_mmp!$ent_dam!$ent_hea!$ent_cri";
				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi$ent_dl$ent_mnb$ent_kabok$ent_kabog$ent_tore$ent_mf$ent_res$ent_fireb$ent_waterb$ent_earthb$ent_windb$ent_saintb$ent_darkb$ent_fireg$ent_waterg$ent_earthg$ent_windg$ent_saintg$ent_darkg$ent_img$ent_gou$ent_hhp$ent_mmp$ent_dam$ent_hea$ent_cri$ent_brk";

				$PL_VALUES[9]="$WN_A!$WLV_A!$WAEnt";
				$PL_VALUES[9].=$ent;

	last CUSTOM;};

	/^�J�͌���$/ && do{
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
#		if(length($FORM{'buyw'}) == 2){&ERROR("���̕���͔����܂���B");}

		&ERROR("�v���l������܂���") if $HC[1] < $www[1];
		&ERROR("�X�g�b�N�����܂��Ă���ׁA���s�ł��܂���") if $PL_VALUES[46] ne "";
		&ERROR("�헪���́A�J�͌����ł��܂���B") if (($WW_FRAG==1 && $HIZUK_FRAG==1) || ($CL_VALUES[7] > time || $CL_VALUES[37] > time));
#		&ERROR("$FORM{'buyabi'}");
		$HC[1]-=$www[1];
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		#�g���W���[�p�G���`�����g
		if($www[0] eq "�g���W���[��(�㋉)" || $www[0] eq "�g���W���[��(����)"){
			my@al=keys %WEAPON_LIST;$alw=@al;
			$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
			@q=split(/\,/,$WEAPON_LIST{"$gw"});
			
			$MFUP=0;
			if($WA12 ne "" && $WA12 > 0){$MFUP = $MFUP + $WA12 * 2;}
			if($WB12 ne "" && $WB12 > 0){$MFUP = $MFUP + $WB12 * 2;}
			if($WC12 ne "" && $WC12 > 0){$MFUP = $MFUP + $WC12 * 2;}
			if($WD12 ne "" && $WD12 > 0){$MFUP = $MFUP + $WD12 * 2;}

#			$ent="!0";

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
				

#				&ERROR("$ent_ent");
#				$ent .= "$ent_str$ent_vit$ent_dex$ent_agi!$ent_dl!$ent_mnb!$ent_kabok!$ent_kabog!$ent_tore!$ent_mf!$ent_res!$ent_fireb!$ent_waterb!$ent_earthb!$ent_windb!$ent_saintb!$ent_darkb!$ent_fireg!$ent_waterg!$ent_earthg!$ent_windg!$ent_saintg!$ent_darkg!$ent_img!$ent_gou!$ent_hhp!$ent_mmp!$ent_dam!$ent_hea!$ent_cri";
				$ent .= "$ent_ent$ent_str$ent_vit$ent_dex$ent_agi$ent_dl$ent_mnb$ent_kabok$ent_kabog$ent_tore$ent_mf$ent_res$ent_fireb$ent_waterb$ent_earthb$ent_windb$ent_saintb$ent_darkb$ent_fireg$ent_waterg$ent_earthg$ent_windg$ent_saintg$ent_darkg$ent_img$ent_gou$ent_hhp$ent_mmp$ent_dam$ent_hea$ent_cri$ent_brk";

		}

		#�����i�����l
		$ent_ent="!0!0";
#&ERROR("$gw$ent_ent����$ent");
		#�g���W���[��(�㋉)�̏���
		if($www[0] eq "�g���W���[��(�㋉)"){

			if($q[11] ne "0"){$ent="";}
			
#			&ERROR("$q[0]����$q[8]");
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
		#�g���W���[��(����)�̏���
		}elsif($www[0] eq "�g���W���[��(����)"){

			if($q[11] ne "0"){$ent="";}

#			&ERROR("$q[0]����$q[8]");
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
	
	/^����g�p$/ && do{	$SW=$PL_VALUES[10] if $FORM{'shiyoi'}==1;$SW=$PL_VALUES[11] if $FORM{'shiyoi'}==2;$SW=$PL_VALUES[38] if $FORM{'shiyoi'}==3;
		$SW=$PL_VALUES[41] if $FORM{'shiyoi'}==4;$SW=$PL_VALUES[42] if $FORM{'shiyoi'}==5;$SW=$PL_VALUES[43] if $FORM{'shiyoi'}==6;$SW=$PL_VALUES[46] if $FORM{'shiyoi'}==7;
		my($wk,$wl)= split(/!/,$SW);my@www=split(/\,/,$WEAPON_LIST{"$wk"});
		&ERROR('���[�߂��I') if $www[7] =~ m/!zd/;
#		&ERROR('����Ȃ���`') if $FORM{'shiyoi'}==0;
#		&REPAIR(\@PL_VALUES);
		&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
		
		#�L���A���[�t
		if($www[7] =~ m/!E0015/){

			$PL_VALUES[15]=$PL_VALUES[15]+4000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

		#�L���A�V�[�h
		}elsif($www[7] =~ m/!E0016/){

			$PL_VALUES[15]=$PL_VALUES[15]+12000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

		#�L���A�y�[�X�g
		}elsif($www[7] =~ m/!E0017/){

			$PL_VALUES[15]=$PL_VALUES[15]+36000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

		#�L���A�G�L�X
		}elsif($www[7] =~ m/!E0018/){

			$PL_VALUES[15] = $PL_VALUES[16];

		#�}�W�b�N���[�t
		}elsif($www[7] =~ m/!E0019/){

			$PL_VALUES[17]=$PL_VALUES[17]+150;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#�}�W�b�N�V�[�h
		}elsif($www[7] =~ m/!E0020/){

			$PL_VALUES[17]=$PL_VALUES[17]+400;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#�}�W�b�N�y�[�X�g
		}elsif($www[7] =~ m/!E0021/){

			$PL_VALUES[17]=$PL_VALUES[17]+900;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#�}�W�b�N�G�L�X
		}elsif($www[7] =~ m/!E0022/){

			$PL_VALUES[17]=$PL_VALUES[17]+1500;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#���̖��
		}elsif($www[7] =~ m/!E0100/){

			if($PL_VALUES[19] < 50){$PL_VALUES[19]=$PL_VALUES[19]+1;}

		#���̘r��
		}elsif($www[7] =~ m/!E0101/){

			if($PL_VALUES[20] < 50){$PL_VALUES[20]=$PL_VALUES[20]+1;}

		#�r�q�̐�
		}elsif($www[7] =~ m/!E0102/){

			if($PL_VALUES[21] < 50){$PL_VALUES[21]=$PL_VALUES[21]+1;}

		#�����̐���
		}elsif($www[7] =~ m/!E0103/){

			if($PL_VALUES[22] < 50){$PL_VALUES[22]=$PL_VALUES[22]+1;}

		#���҂̉ʎ�
		}elsif($www[7] =~ m/!E0023/){

			$PL_VALUES[15]=$PL_VALUES[15]+25000;
			if($PL_VALUES[15] > $PL_VALUES[16]){$PL_VALUES[15] = $PL_VALUES[16];}

			$PL_VALUES[17]=$PL_VALUES[17]+800;
			if($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}

		#�V�g�̉ʎ�
		}elsif($www[7] =~ m/!E0024/){

			$PL_VALUES[15] = $PL_VALUES[16];
			$PL_VALUES[17] = $PL_VALUES[18];

		#���肩�����ʎ�
		}elsif($www[7] =~ m/!E0025/){
			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";

			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && ($PL_VALUES[28] eq $NP_VALS[28])){

					&REPAIR(\@NP_VALS);

					if($NP_VALS[25] ne "1"){

						$NP_VALS[15] = $NP_VALS[15] + int($PL_VALUES[15]/2);
						$NP_VALS[1]="$DATE!$PL_VALUES[3]�͕��肩�����ʎ����s�g�I";

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

		}else{&ERROR("�V�X�e���G���[");}

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
	/^����C��1$/ && do{$PL_VALUES[9]='2hy!0';last CUSTOM;};
	/^����C��2$/ && do{$PL_VALUES[10]='2hy!0';last CUSTOM;};
	/^����C��3$/ && do{$PL_VALUES[11]='2hy!0';last CUSTOM;};
	/^����C��4$/ && do{$PL_VALUES[38]='2hy!0';last CUSTOM;};
	/^����C��1$/ && do{$PL_VALUES[41]='';last CUSTOM;};
	/^����C��2$/ && do{$PL_VALUES[42]='';last CUSTOM;};
	/^����C��3$/ && do{$PL_VALUES[43]='';last CUSTOM;};
	/^�����N�A�b�v$/ && do{my($wk,$wl) = split(/!/,$PL_VALUES[9]);
		&ERROR('�����𖞂����Ă���܂���') if ($wl < ($WEAPON_RANKUP * $WEAPON_LVUP) || length($FORM{'wname'}) != length($wk)+1);
#
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);

		if((length($FORM{'wname'}) - length($wk)) >= 2){&ERROR("�����G���[�ł��B");}

		if ($FORM{'wname'} =~ m/^$wk/){
			$PL_VALUES[9]="$FORM{'wname'}!0!$WAEnt!$WA03!$WA04!$WA05!$WA06!$WA07!$WA08!$WA09!$WA10!$WA11!$WA12!$WA13!$WA14!$WA15!$WA16!$WA17!$WA18!$WA19!$WA20!$WA21!$WA22!$WA23!$WA24!$WA25!$WA26!$WA27!$WA28!$WA29!$WA30!$WA31!$WA32!$WA33!$WA34!$WA35!$WA36!$WA37!$WA38!$WA39!$WA40!$WA41!$WA42";
		}
	last CUSTOM;};
	/^���ꃉ���N�A�b�v$/ && do{my($sk,$sl) = split(/!/,$PL_VALUES[41]);
		&ERROR('�����𖞂����Ă���܂���') if ($sl < ($WEAPON_RANKUP * $WEAPON_LVUP) || length($FORM{'sname'}) != length($sk)+1);
		if ($FORM{'sname'} =~ m/^$sk/){
			local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[41]);
			$PL_VALUES[41]="$FORM{'sname'}!0!$WAEnt";
		}
	last CUSTOM;};
	/^����$/ && do{
		if ($FORM{'soubi'} eq "B" && $PL_VALUES[10]){($PL_VALUES[9],$PL_VALUES[10])=($PL_VALUES[10],$PL_VALUES[9]);}
	 elsif ($FORM{'soubi'} eq "C" && $PL_VALUES[11]){($PL_VALUES[9],$PL_VALUES[11])=($PL_VALUES[11],$PL_VALUES[9]);}
	 elsif ($FORM{'soubi'} eq "D" && $PL_VALUES[38]){($PL_VALUES[9],$PL_VALUES[38])=($PL_VALUES[38],$PL_VALUES[9]);}
	last CUSTOM;};

	/^�������ёւ�$/ && do{
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

	/^������ёւ�$/ && do{
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


	/^\��\���q�Ɏg�p$/ && do{
		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}
		
		if($HC[1] < 2){&ERROR("�v���l������܂���B");}
		$HC[1] = $HC[1] - 2;
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		#&ERROR("�v���l������܂���B");
		if ($FORM{'sorte'} eq "1"){
			if($FORM{'sorter'} eq "0"){
				($PL_VALUES[10],$PL_VALUES[55])=($PL_VALUES[55],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "1"){
				($PL_VALUES[10],$PL_VALUES[56])=($PL_VALUES[56],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "2"){
				($PL_VALUES[10],$PL_VALUES[57])=($PL_VALUES[57],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "3"){
				if($PL_VALUES[29] < 200){&ERROR("���x��������܂���B");}
				($PL_VALUES[10],$PL_VALUES[58])=($PL_VALUES[58],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "4"){
				if($PL_VALUES[29] < 500){&ERROR("���x��������܂���B");}
				($PL_VALUES[10],$PL_VALUES[59])=($PL_VALUES[59],$PL_VALUES[10]);
			}elsif($FORM{'sorter'} eq "5"){
				if($PL_VALUES[29] < 1000){&ERROR("���x��������܂���B");}
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
				if($PL_VALUES[29] < 200){&ERROR("���x��������܂���B");}
				($PL_VALUES[11],$PL_VALUES[58])=($PL_VALUES[58],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "4"){
				if($PL_VALUES[29] < 500){&ERROR("���x��������܂���B");}
				($PL_VALUES[11],$PL_VALUES[59])=($PL_VALUES[59],$PL_VALUES[11]);
			}elsif($FORM{'sorter'} eq "5"){
				if($PL_VALUES[29] < 1000){&ERROR("���x��������܂���B");}
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
				if($PL_VALUES[29] < 200){&ERROR("���x��������܂���B");}
				($PL_VALUES[38],$PL_VALUES[58])=($PL_VALUES[58],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "4"){
				if($PL_VALUES[29] < 500){&ERROR("���x��������܂���B");}
				($PL_VALUES[38],$PL_VALUES[59])=($PL_VALUES[59],$PL_VALUES[38]);
			}elsif($FORM{'sorter'} eq "5"){
				if($PL_VALUES[29] < 1000){&ERROR("���x��������܂���B");}
				($PL_VALUES[38],$PL_VALUES[60])=($PL_VALUES[60],$PL_VALUES[38]);
			}
		}


	last CUSTOM;};


	/^����q�Ɏg�p$/ && do{
		@HC=split(/!/,$PL_VALUES[50]);
		if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
		if($HC[1] eq ""){$HC[1] = 0;}
		if($HC[2] eq ""){$HC[2] = 0;}
		
		if($HC[1] < 2){&ERROR("�v���l������܂���B");}
		$HC[1] = $HC[1] - 2;
		$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		#&ERROR("�v���l������܂���B");
		if ($FORM{'sorts'} eq "1"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[41],$PL_VALUES[61])=($PL_VALUES[61],$PL_VALUES[41]);
			}elsif($FORM{'sortsr'} eq "2"){
				if($PL_VALUES[29] < 300){&ERROR("���x��������܂���B");}
				($PL_VALUES[41],$PL_VALUES[62])=($PL_VALUES[62],$PL_VALUES[41]);
			}elsif($FORM{'sortsr'} eq "3"){
				if($PL_VALUES[29] < 800){&ERROR("���x��������܂���B");}
				($PL_VALUES[41],$PL_VALUES[63])=($PL_VALUES[63],$PL_VALUES[41]);
			}
		}
		elsif ($FORM{'sorts'} eq "2"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[42],$PL_VALUES[61])=($PL_VALUES[61],$PL_VALUES[42]);
			}elsif($FORM{'sortsr'} eq "2"){
				if($PL_VALUES[29] < 300){&ERROR("���x��������܂���B");}
				($PL_VALUES[42],$PL_VALUES[62])=($PL_VALUES[62],$PL_VALUES[42]);
			}elsif($FORM{'sortsr'} eq "3"){
				if($PL_VALUES[29] < 800){&ERROR("���x��������܂���B");}
				($PL_VALUES[42],$PL_VALUES[63])=($PL_VALUES[63],$PL_VALUES[42]);
			}
		}
		elsif ($FORM{'sorts'} eq "3"){
			if($FORM{'sortsr'} eq "1"){
				($PL_VALUES[43],$PL_VALUES[61])=($PL_VALUES[61],$PL_VALUES[43]);
			}elsif($FORM{'sortsr'} eq "2"){
				if($PL_VALUES[29] < 300){&ERROR("���x��������܂���B");}
				($PL_VALUES[43],$PL_VALUES[62])=($PL_VALUES[62],$PL_VALUES[43]);
			}elsif($FORM{'sortsr'} eq "3"){
				if($PL_VALUES[29] < 800){&ERROR("���x��������܂���B");}
				($PL_VALUES[43],$PL_VALUES[63])=($PL_VALUES[63],$PL_VALUES[43]);
			}
		}

	last CUSTOM;};

	/^���o��$/ && do{
		&ERROR("�V�X�e���G���[") if !$PL_VALUES[46];
		local($WN_Y,$WLV_Y) = split(/!/,$PL_VALUES[46]);
		@WN_sY=split(/\,/,$WEAPON_LIST{"$WN_Y"});

		if (!$PL_VALUES[10] && ($WN_sY[11] == 0 || $WN_sY[11] == 9)){$PL_VALUES[10]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[11] && ($WN_sY[11] == 0 || $WN_sY[11] == 9)){$PL_VALUES[11]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[38] && ($WN_sY[11] == 0 || $WN_sY[11] == 9)){$PL_VALUES[38]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[41] && $WN_sY[11] != 0 && $WN_sY[11] != 9){$PL_VALUES[41]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[42] && $WN_sY[11] != 0 && $WN_sY[11] != 9){$PL_VALUES[42]=$PL_VALUES[46];$PL_VALUES[46]="";}
		elsif (!$PL_VALUES[43] && $WN_sY[11] != 0 && $WN_sY[11] != 9){$PL_VALUES[43]=$PL_VALUES[46];$PL_VALUES[46]="";}

	last CUSTOM;};

	/^�ݒ�$/ && do{
		#0�Ŋ�������@1�ŕ��킾���Ŕ���
		$PL_VALUES[45] = $FORM{'AtSet'};
	last CUSTOM;};

	/^�w��$/ && do{
		my@www=split(/\,/,$WEAPON_LIST{"$FORM{'buyw'}"});
#		if(length($FORM{'buyw'}) == 2){&ERROR("���̕���͔����܂���B");}

		if($www[6] == 2){
			$PL_VALUES[18]=0;
			#�����L���O�p �A�C�e���l�����@0�̓A�C�e���l���@1��MVP�@2�͐}�ӓo�^ 3�͕s���J�E���g
			@RC=split(/!/,$PL_VALUES[47]);
			if($RC[3] eq ""){$RC[3] = 0;}
			$RC[3] = $RC[3] + 1;
			$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";
			&ERROR("���̕���͔����܂���B");

		}
		if($www[6] == 8 && $PL_VALUES[5]){
			$PL_VALUES[18]=0;
			#�����L���O�p �A�C�e���l�����@0�̓A�C�e���l���@1��MVP�@2�͐}�ӓo�^ 3�͕s���J�E���g
			@RC=split(/!/,$PL_VALUES[47]);
			if($RC[3] eq ""){$RC[3] = 0;}
			$RC[3] = $RC[3] + 1;
			$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";
			&ERROR("���̕���͔����܂���B");

		}
		$PL_VALUES[8]-=$www[5];
		if (!$PL_VALUES[10] && $www[11] == 0){$PL_VALUES[10]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[11] && $www[11] == 0){$PL_VALUES[11]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[38] && $www[11] == 0){$PL_VALUES[38]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[41] && $www[11] != 0){$PL_VALUES[41]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[42] && $www[11] != 0){$PL_VALUES[42]="$FORM{'buyw'}!0";}
		elsif (!$PL_VALUES[43] && $www[11] != 0){$PL_VALUES[43]="$FORM{'buyw'}!0";}
	last CUSTOM;};

	/^�`�F���W$/ && do{
		&ERROR('ERROR','����������Ȃ����U�߂��I') if $PL_VALUES[8] < 100000;
		$PL_VALUES[8]-=100000;
		$PL_VALUES[27]=$FORM{'icon'};
		$PL_VALUES[40]=$FORM{'icon2'};
		$PL_VALUES[13]=$FORM{'MsColor'};
		$PL_VALUES[3]=$FORM{'MsName'};
	last CUSTOM;};

	/^Custom$/ && do{&ERROR('�n���x������܂���') if $PL_VALUES[24] < 210;
		$PL_VALUES[8]-=20000;$PL_VALUES[23]++;$PL_VALUES[27]=$FORM{'icon'};$PL_VALUES[40]=$FORM{'icon2'};
		$PL_VALUES[13]=$FORM{'MsColor'};

	require "./$LOG_FOLDER/$CLASS_DATA";
	my@plclass=split(/\,/,$VCLASS_LIST{"$FORM{'MsType'}"});
		unless($plclass[12] <= $PL_VALUES[12] && $plclass[13] >= $PL_VALUES[12]){
			&ERROR('ERROR','ALI���[�߂��I');
		}
		if($plclass[6] > $PL_VALUES[19]){&ERROR('ERROR','STR���[�߂��I');}
		if($plclass[7] > $PL_VALUES[20]){&ERROR('ERROR','VIT���[�߂��I');}
		if($plclass[8] > $PL_VALUES[21]){&ERROR('ERROR','AGI���[�߂��I');}
		if($plclass[9] > $PL_VALUES[22]){&ERROR('ERROR','DEX���[�߂��I');}
		if($plclass[10] > $PL_VALUES[16]){&ERROR('ERROR','HP���[�߂��I');}
		if($plclass[11] > $PL_VALUES[18]){&ERROR('ERROR','MP���[�߂��I');}
		if($plclass[14] > $PL_VALUES[24]){&ERROR('ERROR','�n���x���[�߂��I');}
		if($plclass[15]){
			local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
			local($WN_S,$WLV_S) = split(/!/,$PL_VALUES[41]);
			my@wwa=split(/\,/,$WEAPON_LIST{"$WN_A"});
			my@wws=split(/\,/,$WEAPON_LIST{"$WN_S"});
			if($plclass[5]==4){
				if($wwa[7] !~ m/$plclass[15]/i && $wws[7] !~ m/$plclass[15]/i){&ERROR('ERROR','���킾�[�߂��I');}
			}elsif($plclass[5]==1 && $PL_VALUES[4] == 219){
				if($wwa[12] !~ m/e011/){&ERROR('ERROR','���킾�[�߂��I');}
			}else{
				if($plclass[15] ne $wwa[0] && $plclass[15] ne $wws[0]){&ERROR('ERROR','���킾�[�߂��I');}
			}
		}

		if($plclass[16]){
			if($PL_VALUES[4] !~ /$plclass[16]/i){&ERROR('ERROR','�N���X���[�߂��I');}
		}
		if($plclass[20]){
			if($plclass[20] < $PL_VALUES[24]){&ERROR('ERROR','�n���x�������[�߂��I');}
		}
		if($plclass[21]){
			if($plclass[21] > $PL_VALUES[32]){&ERROR('ERROR','�w�����[�߂��I');}
		}
		$PL_VALUES[24]-=110;$PL_VALUES[24]=890 if($PL_VALUES[24] > 890);
		$PL_VALUES[4]=$FORM{'MsType'};
		$PL_VALUES[3]=$FORM{'MsName'};$PL_VALUES[31]=$FORM{'element'};
		if($plclass[17] =~ m/!x/){$PL_VALUES[31]=2;}
		if($plclass[17] =~ m/!y/){$PL_VALUES[31]=4;}
		if($plclass[17] =~ m/!z/){$PL_VALUES[31]=5;}
		if($PL_VALUES[4] =~ /^64$|^65$|^72$|^90$/i){$PL_VALUES[9]="1oa!0";}
	last CUSTOM;};
	/^$STATUS_NAME[4]�A�b�v$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[4]�A�b�v�~�P$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[4]�A�b�v�~�T$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[4]�A�b�v�~�P�O$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[16] > $F_MAX_HP && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]�A�b�v$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]�A�b�v�~�P$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]�A�b�v�~�T$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^$STATUS_NAME[5]�A�b�v�~�P�O$/ && do{
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

		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[18] > $F_MAX_EN && $PL_VALUES[24] < 100;
	last CUSTOM;};

	/^Lv.�A�b�v$/ && do{
		$TIKIM2=int(1000*$PL_VALUES[29]+100000);
		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[8] < $TIKIM2;
		$PL_VALUES[8]-=$TIKIM2;$PL_VALUES[29]++;
		last CUSTOM;
		};
	/^ALI�A�b�v$/ && do{&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[8] < 400000;
		$PL_VALUES[8]-=400000;if($PL_VALUES[12] < 100){$PL_VALUES[12]+=12;}
		if($PL_VALUES[12] > 100){$PL_VALUES[12]=100;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[0]�A�b�v$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[19] < 50){$PL_VALUES[19]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[19]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[1]�A�b�v$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[20] < 50){$PL_VALUES[20]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[20]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[3]�A�b�v$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[22] < 50){$PL_VALUES[22]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[22]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};
	/^$STATUS_NAME[2]�A�b�v$/ && do{
		$TIKIM4=int(($PL_VALUES[19]+$PL_VALUES[20]+$PL_VALUES[21]+$PL_VALUES[22])*2000+100000);
		&ERROR('�����𖞂����Ă��܂���') if $PL_VALUES[8] < $TIKIM4;
		$PL_VALUES[8]-=$TIKIM4;if($PL_VALUES[21] < 50){$PL_VALUES[21]++;}
		if($PL_VALUES[19] > 50){$PL_VALUES[21]=50;}
		if($PL_VALUES[5]){$PL_VALUES[18]=0;}
	last CUSTOM;};

	$FORM{'mahouCheck'} && $PL_VALUES[5] && do{
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
#		&DBM_CONVERT('P');$flagp=1;
		#�n�[�l��
		if ($FORM{'Xmode'} eq "�v���C�n�[�l��"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 1;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 1;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 1;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 1;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!�v���C�n�[�l�����g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "�f�t�n�[�l��"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 1;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 1;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 1;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 1;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!�f�t�n�[�l�����g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;#$flagp=1;
		}
		#�]�V���l��
		if ($FORM{'Xmode'} eq "�v���C�]�V���l��"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 2;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 2;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 2;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 2;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!�v���C�]�V���l�����g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "�f�t�]�V���l��"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 2;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 2;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 2;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 2;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!�f�t�]�V���l�����g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;#$flagp=1;
		}
		#�o�[�T
		if ($FORM{'Xmode'} eq "�v���C�o�[�T"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 3;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 3;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 3;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 3;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!�v���C�o�[�T���g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "�f�t�o�[�T"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 3;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 3;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 3;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 3;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!�f�t�o�[�T���g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;#$flagp=1;
		}
		#�O���[�U
		if ($FORM{'Xmode'} eq "�v���C�O���[�U"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 400;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 4;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 4;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 4;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 4;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 400;
			$PL_VALUES[1]="$DATE!�v���C�O���[�U���g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;
		}
		if ($FORM{'Xmode'} eq "�f�t�O���[�U"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 600;
	
			@CC=split(/!/,$CL_VALUES[46]);
			#�����̏ꍇ
			if ($PL_VALUES[6] eq "1" && $PL_VALUES[28] eq ""){
				$CC[0] = 4;
				$CC[1] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[2]){
				$CC[2] = 4;
				$CC[3] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#�������̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[3]){
				$CC[4] = 4;
				$CC[5] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			#��O�����̏ꍇ
			}elsif ($PL_VALUES[6] eq "-1" && $PL_VALUES[28] eq $CL_VALUES[4]){
				$CC[6] = 4;
				$CC[7] = time + 960;
				$CL_VALUES[46] = "$CC[0]!$CC[1]!$CC[2]!$CC[3]!$CC[4]!$CC[5]!$CC[6]!$CC[7]!";
			}
#			&REPAIR(\@PL_VALUES);
			$PL_VALUES[17] = $PL_VALUES[17] - 600;
			$PL_VALUES[1]="$DATE!�f�t�O���[�U���g�p���܂����B";

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;#$flagp=1;
		}
		if ($FORM{'Xmode'} eq "�}�[�V�[���C��"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
#			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
#			&ERROR('MP������܂���B') if $PL_VALUES[17] < 400;
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 600;

			#�񕜗ʌv�Z�@���j�b�g�G�������g��v��30
			$PL_LP = 0.2;
			if($PL_VALUES[31] eq "3"){$PL_LP = 0.3;}

			&DBM_INPORT(P);

#			#�Ώېl���ɂ���āA�񕜗ʂ�ϓ�
#			#�J�E���g����
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
						$NP_VALS[1]="$DATE!$PL_VALUES[3]�̓}�[�V�[���C�����s�g�I";

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
			$PL_VALUES[1]="$DATE!�}�[�V�[���C�����g�p���܂����B";

			if($HoushoFlg == 1){
				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] eq ""){$HC[0] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}
				#���ݍv���_+45
				$HC[0] = $HC[0] + 45;
				$HC[2] = $HC[2] + 45;
	
				#���g�������̏ꍇ+20
				if($PL_VALUES[6] eq "1"){
					#���ݍv���_+20
					$HC[0] = $HC[0] + 20;
					$HC[2] = $HC[2] + 20;
				}elsif($PL_VALUES[6] eq "-1"){
				#���g�������̏ꍇ+12
					#���ݍv���_+12
					$HC[0] = $HC[0] + 12;
					$HC[2] = $HC[2] + 12;
				}
				#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
				if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
		
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			$flagc=1;#$flagp=1;
		}
		if ($FORM{'Xmode'} eq "�}�[�e�B���C�Y"){

			&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
#			&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
			&REPAIR(\@PL_VALUES);
			&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
			&ERROR('MP������܂���B') if $PL_VALUES[17] < 1500;

			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && ($PL_VALUES[28] eq $NP_VALS[28])){

					&REPAIR(\@NP_VALS);

					if($NP_VALS[25] eq "1"){

#						$NP_VALS[15] = $NP_VALS[16];
						$NP_VALS[25] = 0;
						if($NP_VALS[15] <= 0){$NP_VALS[15] = 1;}
						$NP_VALS[1]="$DATE!$PL_VALUES[3]�̓}�[�e�B���C�Y���s�g�I";

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
			$PL_VALUES[1]="$DATE!�}�[�e�B���C�Y���g�p���܂����B$PL_VALUES[3]�͐퓬�s�\\";

			if($HoushoFlg == 1){
				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] eq ""){$HC[0] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}
				#���ݍv���_+80
				$HC[0] = $HC[0] + 80;
				$HC[2] = $HC[2] + 80;
	
				#���g�������̏ꍇ+40
				if($PL_VALUES[6] eq "1"){
					#���ݍv���_+40
					$HC[0] = $HC[0] + 40;
					$HC[2] = $HC[2] + 40;
				}elsif($PL_VALUES[6] eq "-1"){
				#���g�������̏ꍇ+20
					#���ݍv���_+20
					$HC[0] = $HC[0] + 20;
					$HC[2] = $HC[2] + 20;
				}
				#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
				if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
		
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}

			#�v���l���Z
			if($NewHoushoFlg == 1){

				@HC=split(/!/,$PL_VALUES[50]);
				if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
				if($HC[1] eq ""){$HC[1] = 0;}
				if($HC[2] eq ""){$HC[2] = 0;}

				$HC[1] = $HC[1] + 5;
				$HC[2] = $HC[2] + 5;
				#�����̏ꍇ�A�v���_+5
				if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 5;}
				
				if($HC[1] > 9999){$HC[1] = 9999;}
				
				$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			}
			
			$flagc=1;#$flagp=1;
		}

	last CUSTOM;};

	/^�ύX$/ && do{$PL_VALUES[7]="$FORM{'com'}";
	last CUSTOM;};
	/^�A�C�R���`�F���W$/ && do{
		$PL_VALUES[36]="$FORM{'unitColor'}";
	last CUSTOM;};
#	/^�q�ɓ���ւ�$/ && do{
#		###38�͑����X���b�g�Ƃ��Ă�����������̂ő��ϐ��Ń����s�N�@by304 20090212
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
	/^�S��$/ && do{
		if($PL_VALUES[5]){
		$BOMEIM=int($PL_VALUES[8]/10);$BOMEIM='30000' if $BOMEIM < 30000;
		$PL_VALUES[8]-=$BOMEIM;
		}
		$PL_VALUES[5]="$FORM{'boumeiC'}";$PL_VALUES[28]='';$PL_VALUES[0]=$PL_VALUES[6]=0;

		#�J�̓V�X�e��	�S���̏ꍇ�́A���ݍv���_���N���A����
		if($HoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			
			#���ݍv���_���N���A
			$HC[0] = 0;

#			#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
#			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}

#			#�݌v�v���_�̌v�Z
#			$HC[2] = $HC[2] + 100;

			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		#�V�^�J�̓V�X�e��
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

		#�~�ϑ[�uorz
#				&ERROR("$PL_VALUES[5]��$NC_Name��00��$NC_VALUES[39]");
#		&DBM_INPORT(C);
#		while (($NC_Name,$NC_Value) =each %C) {
#				&ERROR("$NC_Name����$NC_VALUES[39]");
#
#			if($NC_Name eq $PL_VALUES[5]){
#
#				@NC_VALUES = split(/\s/,$NC_Value);
#				$PL_VALUES[39] = $NC_VALUES[39];
#			}
#
#		}

	last CUSTOM;};
	/^����$/ && do{$PL_VALUES[28]="$FORM{'inunit'}";last CUSTOM;};
	/^����$/ && do{$PL_VALUES[28]="";$PL_VALUES[6]="0";last CUSTOM;};
	/^�����쐬$/ && do{&ERROR('���������L������Ă��܂���') if !$FORM{'uname'};
		if($FORM{'uname'} eq "$CL_VALUES[2]" || $FORM{'uname'} eq "$CL_VALUES[3]" || $FORM{'uname'} eq "$CL_VALUES[4]"){&ERROR('�����̕��������ɑ��݂��܂��B');}
		&ERROR("�������Ɂu�������v���܂߂鎖�͏o���܂���B") if $FORM{'uname'} =~ /������$/ ;
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		$flagc=1;$PL_VALUES[8]-=$MAKE_TEAM;
		UNIT:for ($i=2;$i <= 4; $i++){if (!$CL_VALUES[$i]){$CL_VALUES[$i]="$FORM{'uname'}";last UNIT;}}
	last CUSTOM;};
	/^�����ĕ�$/ && do{&ERROR('���������L������Ă��܂���') if !$FORM{'suname'};
		if($FORM{'suname'} eq "$CL_VALUES[2]" || $FORM{'suname'} eq "$CL_VALUES[3]" || $FORM{'suname'} eq "$CL_VALUES[4]"){&ERROR('�����̕��������ɑ��݂��܂��B');}
		&ERROR("�������Ɂu�������v���܂߂鎖�͏o���܂���B") if $FORM{'suname'} =~ /������$/ ;
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		$flagc=1;
		$PL_VALUES[8]-=$NAME_TEAM;
		if($CL_VALUES[2] eq $PL_VALUES[28]){

			&DBM_INPORT(P);
			dbmopen (%P,"$DBM_P",0666);
			foreach $key (keys %P){
				@VS_VALUES = split(/\s/,$P{$key});
				#�����̕ύX�O�����̃����o�[��S���A�ύX�㕔���ɕғ�����
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
				#�����̕ύX�O�����̃����o�[��S���A�ύX�㕔���ɕғ�����
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
				#�����̕ύX�O�����̃����o�[��S���A�ύX�㕔���ɕғ�����
				if($VS_VALUES[5] eq $PL_VALUES[5] && $VS_VALUES[28] eq $PL_VALUES[28] ){
					&REPAIR(\@VS_VALUES);
					$VS_VALUES[28] = "$FORM{'suname'}";
				}
				$P{"$key"}="@VS_VALUES";
			}

			dbmclose %P;
			$CL_VALUES[4]=$PL_VALUES[28]="$FORM{'suname'}";


		}else{&ERROR('���������݂��܂���B');}
	last CUSTOM;};
	/^����$/ && do{
		&DBM_INPORT(P);
#20090531�@304������@�����ɂ���Ă̓G���[����������̂ŕ���
#		my$checkcname=substr("$FORM{'cname'}",0,8);
#		while (my($key,$value) = each %P){
#			my@VS_VALUE = split(/\s/,$value);
#			if($FORM{'cname'} eq "$VS_VALUE[5]"){
#				&ERROR('�����̍������ɑ��݂��܂��B');
#			}
#			&ERROR('�����悤�ȍ����������ɑ��݂��܂��B') if "$VS_VALUE[5]" =~ m/\^$checkcname/;
#		}
		&DBM_INPORT('C');
		my@C=%C;
		my$C=@C/2;
		&ERROR('���[�߂��I') if $C >= $COUNTRY_MAX;
#		&ERROR('���[�߂��I') if $C > 12;
		&ERROR('�����̍������ɑ��݂��܂��B') if $C{"$FORM{'cname'}"};
		&ERROR('�����̍Ō�Ɂu��v���܂߂鎖�͏o���܂���B') if $FORM{'cname'} =~ /�$/i ;
		&ERROR("�����Ɂu$NONE_NATIONALITY�v���܂߂鎖�͏o���܂���B") if $FORM{'cname'} =~ /$NONE_NATIONALITY$/ ;
		&ERROR("���̍����Ō������邱�Ƃ͏o���܂���B") if $FORM{'cname'} eq "�t�H�[�`�����g�p�I";
		&ERROR(noName) if !$FORM{'cname'};@CL_VALUES='';$Moto="$PL_VALUES[5]" if $PL_VALUES[5];
		&DBM_INPORT(R);@R_VALUES = split(/\s/,$R{"server"});$R_VALUES[155]++;$flagr=1;
		$PL_VALUES[8]-=$MAKE_COUNTRY;$PL_VALUES[5]="$FORM{'cname'}";$PL_VALUES[28]='';$PL_VALUES[32]++;
		if($PL_VALUES[32] > $PL_VALUES[35]*10){$PL_VALUES[32]=$PL_VALUES[35]*10;}
		$PL_VALUES[0]='220';$PL_VALUES[6]='1';

		#�J�̓V�X�e��	�����̏ꍇ�́A���ݍv���_���N���A����
		if($HoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			
			#���ݍv���_���N���A
			$HC[0] = 0;

			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		#�V�^�J�̓V�X�e��
#		if($NewHoushoFlg == 1){
		
#			@HC=split(/!/,$PL_VALUES[50]);
#			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[1]=0;$HC[2] = 0;}
#			if($HC[1] eq ""){$HC[1] = 0;}
#			if($HC[2] eq ""){$HC[2] = 0;}

#			$HC[1] = 0;
			
#			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";
		
#		}
				
		$CL_VALUES[0]='#'.$FORM{'cl'};$CL_VALUES[1]=30000;$CL_VALUES[7]=time;$CL_VALUES[39]=$PL_VALUES[39];
		$CL_VALUES[11]="$YOUSAI_HP!$YOUSAI_HP!$DATE";$CL_VALUES[12]="1!1!1!$FORM{'cname'}�h�q�v��";$flagc=1;
		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
		$HISTORY="$FORM{'pname'} ��<B class=rb1>$FORM{'cname'}</B>�������B�ō��w���҂�$FORM{'pname'}���A�C�B" if !$Moto;
		$HISTORY="$FORM{'pname'} ��<B class=rb1>$FORM{'cname'}</B>�������B$Moto�ɑ΂��ēƗ���錾�B" if $Moto;
#		$HISTORY="$CON��$FORM{'pname'} ��<B class=rb1>$FORM{'cname'}</B>�������B�ō��w���҂�$FORM{'pname'}���A�C�B" if !$Moto;
#		$HISTORY="$CON��$FORM{'pname'} ��<B class=rb1>$FORM{'cname'}</B>�������B$Moto�ɑ΂��ēƗ���錾�B" if $Moto;
	last CUSTOM;};
	/^���$/ && do{
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		&ERROR('�����E�����ȊO�͎g�p�ł��܂���B') if $PL_VALUES[6] eq "0";
		&ERROR('�퓬�s�\\���͎g�p�ł��܂���B') if $PL_VALUES[25] eq "1";
		&ERROR('MP������܂���B�I�[�u���������ہAMP��800����܂��B') if $PL_VALUES[17] < 800;

		require "./$LOG_FOLDER/$HASH_DATA";
#		local($WN_A,$WLV_A) = split(/!/,$PL_VALUES[9]);
#		local($WN_B,$WLV_B) = split(/!/,$PL_VALUES[10]);
#		local($WN_C,$WLV_C) = split(/!/,$PL_VALUES[11]);
#		local($WN_D,$WLV_D) = split(/!/,$PL_VALUES[38]);
	
#		@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
#		@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});@WN_sD=split(/\,/,$WEAPON_LIST{"$WN_D"});

		$a=$FORM{'TSet'};$b=$FORM{'OSet'};
#		&ERROR("$a����$b");
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
			#���ݍv���_+100
			$HC[0] = $HC[0] + 100;
			$HC[2] = $HC[2] + 100;

			#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}
	
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		#�v���l���Z
		if($NewHoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] ne $HoushoKey){$PL_VALUES[50] = "";$HC[0] = $HoushoKey;$HC[1]=0;$HC[2] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}

			$HC[1] = $HC[1] + 10;
			$HC[2] = $HC[2] + 10;
			#�����̏ꍇ�A�v���_+10
			if($PL_VALUES[6] == 1){$HC[1] = $HC[1] + 1;$HC[2] = $HC[2] + 10;}
			
			if($HC[1] > 9999){$HC[1] = 9999;}
			
			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

		}

		if($WN_sO[7] =~ m/!87|!88|!89|!8a|!8b|!8c/){

			#�I�[�u�_���[�W���v�Z
			$OD = 0;
			require "./$LOG_FOLDER/$CLASS_DATA";
			@PL_CLASS=split(/\,/,$VCLASS_LIST{"$PL_VALUES[4]"});

			if($PL_CLASS[2] < 0){$PL_CLASS[2]=int($PL_CLASS[2]/2-0.5);}if($PL_CLASS[2] > 0){$PL_CLASS[2]=int($PL_CLASS[2]/2+0.5);}
			$VIT = int($PL_VALUES[20] * $PL_CLASS[2]);
			$LV = $PL_VALUES[29];
			if($LV > 200){$LV = 200;}
			$EL = 1;#������n��
			$OName="";
			if($WN_sO[7] =~ m/!87/){$OName="�T�����C�V���^��";$OName2="���̃I�[�u�F";}
			elsif($WN_sO[7] =~ m/!88/){$OName="�T�����A�X���f";$OName2="�ł̃I�[�u�F";}
			elsif($WN_sO[7] =~ m/!89/){$OName="�T�����]�V���l��";$OName2="���̃I�[�u�F";}
			elsif($WN_sO[7] =~ m/!8a/){$OName="�T�����O���[�U";$OName2="���̃I�[�u�F";}
			elsif($WN_sO[7] =~ m/!8b/){$OName="�T�����n�[�l��";$OName2="���̃I�[�u�F";}
			elsif($WN_sO[7] =~ m/!8c/){$OName="�T�����o�[�T";$OName2="��n�̃I�[�u�F";}


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

#20181111 UPDATE �I�[�u�_���[�W�������������
#			$OD = int($VIT * $LV * $PL_VALUES[15] / 40000 * $EL * (($OL + 51) / 100));
			$OD = int($VIT * $LV * $PL_VALUES[15] / 40000 * $EL * (($OL + 101) / 100) + int(rand(20000)));

			#�^�[�Q�b�g�����擾
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
			#�I�����̕������擾���Ȃ��Ƃʂ��
			
			$TTT = "";
			while (($C_Name,$C_Value) =each %C) {
				@C_VALUES = split(/\s/,$C_Value);

#				&ERROR("$C_Name");

				#����
				if($C_Name eq $TCON){

					#�������擾
					if($TTeam eq ""){$TTT = "";}
					elsif($TTeam eq "8"){$TTT = $C_VALUES[8];}
					elsif($TTeam eq "9"){$TTT = $C_VALUES[9];}
					elsif($TTeam eq "10"){$TTT = $C_VALUES[10];}

				}

			}

#$OD
#				&ERROR("$TCON������$TTT");

			&DBM_INPORT(P);
			dbmopen (%P,"$DBM_P",0666);
			foreach $key (keys %P){
				@VS_VALUES = split(/\s/,$P{$key});
				if($VS_VALUES[5] eq $TCON && ($TTT eq $VS_VALUES[28] || ($TTT eq "" && $VS_VALUES[28] eq ""))){
#				&ERROR("$VS_VALUES[5]");
					&REPAIR(\@VS_VALUES);
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]��$OName�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15] = int($VS_VALUES[15] - $OD);
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}
				$P{"$key"}="@VS_VALUES";
			}
	
			dbmclose %P;

			if($TTT eq ""){$TTT ="�{��";}

#		$testes = $CL_VALUES[45];
#		$CL_VALUES[45] = time + 1200;
			$message0="<b class=rb3>$PL_VALUES[5]</b>��";
			$message0.="<b class=rb3>$TCON��$TTT</b>��";
			$message0.="$OName2$OName��������܂����B";

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
	/^�v�ǉ���$/ && do{
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		&ERROR('�v�ǖ��̍Ō�Ɂu��v���܂߂鎖�͏o���܂���B') if $FORM{'yoname'} =~ /�$/i ;
		&ERROR(noName) if !$FORM{'yoname'};&ERROR('�������܂���B') if $CL_VALUES[1] < $NAME_YOSAI;
		$CL_VALUES[1]-=$NAME_YOSAI;@Y_ST=split(/!/,$CL_VALUES[12]);
		$CL_VALUES[12]="$Y_ST[0]!$Y_ST[1]!$Y_ST[2]!$FORM{'yoname'}";$flagc=1;$flagp=0;
	last CUSTOM;};
	/^���U$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && do{$flagc=1;$flagp=0;
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		$CL_VALUES[2]='' if $FORM{'delunit'} eq "$CL_VALUES[2]";
		$CL_VALUES[3]='' if $FORM{'delunit'} eq "$CL_VALUES[3]";
		$CL_VALUES[4]='' if $FORM{'delunit'} eq "$CL_VALUES[4]";
	last CUSTOM;};
#	/^���$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time && do{
#		&DBM_INPORT(P);
#		&DBM_INPORT(C);
#		&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
#
#		$M_AITEX0="$CL_VALUES[6]";
#		$M_AITEX1="$CL_VALUES[8]";
#		$M_AITEX2="$CL_VALUES[9]";
#		$M_AITEX3="$CL_VALUES[10]";
#		&ERROR('�헪�������́A���錾���s�����Ƃ͂ł��܂���B') if !$C{"$M_AITEX0"} && !$C{"$M_AITEX1"} && !$C{"$M_AITEX2"} && !$C{"$M_AITEX3"};
#
#		$flagc=1;$flagp=1;
#		$CL_VALUES[7]=time;
#		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
#		$HISTORY="$CON��<B class=rb3>$PL_VALUES[5]</B>������錾���܂����B";
##		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>������錾���܂����B";
#	last CUSTOM;};
	/^���錾$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && $CL_VALUES[7] > time && do{
		&DBM_INPORT(P);
		&DBM_INPORT(C);
		&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};

		$M_AITEX0="$CL_VALUES[6]";
		$M_AITEX1="$CL_VALUES[8]";
		$M_AITEX2="$CL_VALUES[9]";
		$M_AITEX3="$CL_VALUES[10]";
		&ERROR('�헪�������́A���錾���s�����Ƃ͂ł��܂���B') if !$C{"$M_AITEX0"} && !$C{"$M_AITEX1"} && !$C{"$M_AITEX2"} && !$C{"$M_AITEX3"};
#		&ERROR("$FORM{'TeiSet'}");
		$flagc=1;$flagp=1;

		if ($FORM{'TeiSet'} eq "1"){
			&ERROR('�I���������͊��ɖŖS���Ă��܂��B') if !$C{"$M_AITEX0"};
			$aite=$CL_VALUES[6];

			if($CL_VALUES[6] eq $CL_VALUES[8]){
				$CL_VALUES[8]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[6] eq $CL_VALUES[9]){
				$CL_VALUES[9]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[6] eq $CL_VALUES[10]){
				$CL_VALUES[10]="�o���_�[�����𐒂߂���";
			}

			$CL_VALUES[6] = "�o���_�[�����𐒂߂���";

		}elsif ($FORM{'TeiSet'} eq "2"){
			&ERROR('�I���������͊��ɖŖS���Ă��܂��B') if !$C{"$M_AITEX1"};
			$aite=$CL_VALUES[8];

			if($CL_VALUES[8] eq $CL_VALUES[6]){
				$CL_VALUES[6]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[8] eq $CL_VALUES[9]){
				$CL_VALUES[9]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[8] eq $CL_VALUES[10]){
				$CL_VALUES[10]="�o���_�[�����𐒂߂���";
			}

			$CL_VALUES[8] = "�o���_�[�����𐒂߂���";

		}elsif ($FORM{'TeiSet'} eq "3"){
			&ERROR('�I���������͊��ɖŖS���Ă��܂��B') if !$C{"$M_AITEX2"};
			$aite=$CL_VALUES[9];

			if($CL_VALUES[9] eq $CL_VALUES[6]){
				$CL_VALUES[6]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[9] eq $CL_VALUES[8]){
				$CL_VALUES[8]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[9] eq $CL_VALUES[10]){
				$CL_VALUES[10]="�o���_�[�����𐒂߂���";
			}

			$CL_VALUES[9] = "�o���_�[�����𐒂߂���";

		}elsif ($FORM{'TeiSet'} eq "4"){
			&ERROR('�I���������͊��ɖŖS���Ă��܂��B') if !$C{"$M_AITEX3"};
			$aite=$CL_VALUES[10];

			if($CL_VALUES[10] eq $CL_VALUES[6]){
				$CL_VALUES[6]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[10] eq $CL_VALUES[8]){
				$CL_VALUES[8]="�o���_�[�����𐒂߂���";
			}elsif($CL_VALUES[10] eq $CL_VALUES[9]){
				$CL_VALUES[9]="�o���_�[�����𐒂߂���";
			}

			$CL_VALUES[10] = "�o���_�[�����𐒂߂���";

		}

		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}

#		$HISTORY="$CON��<B class=rb3>$PL_VALUES[5]</B>��<B class=rb2>$aite</B>�ɒ���錾���܂����B";
		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>��<B class=rb2>$aite</B>�ɒ���錾���܂����B";
	last CUSTOM;};
	/^����$/ && $PL_VALUES[5] && $PL_VALUES[6] == 1 && $CL_VALUES[7] < time && do{
		&DBM_INPORT(P);
		&DBM_INPORT(C);
		&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
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
#		$HISTORY="$CON��<B class=rb3>$PL_VALUES[5]</B>���헪�������B$JIKANSA����ɐN�U�J�n�B" if $CL_VALUES[13];
#		$HISTORY2="$CON��<B class=rb3>$PL_VALUES[5]</B>��$FORM{'mname'}�𔭓��B<B class=rb2>$CL_VALUES[6]$TEKI_1$TEKI_2$TEKI_3</B>�֐N�U�J�n�B";
		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>���헪�������B$JIKANSA����ɐN�U�J�n�B" if $CL_VALUES[13];
		$HISTORY2="<B class=rb3>$PL_VALUES[5]</B>��$FORM{'mname'}�𔭓��B<B class=rb2>$CL_VALUES[6]$TEKI_1$TEKI_2$TEKI_3</B>�֐N�U�J�n�B";

		#�J�̓V�X�e��	��������ON�̏ꍇ�A�v���_+100	�����́AONOFF�֌W�Ȃ���+100
		if($HoushoFlg == 1){

			@HC=split(/!/,$PL_VALUES[50]);
			if($HC[0] eq ""){$HC[0] = 0;}
			if($HC[1] eq ""){$HC[1] = 0;}
			if($HC[2] eq ""){$HC[2] = 0;}
			
			#���ݍv���_+100
			$HC[0] = $HC[0] + 100;

			#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
			if($HC[0] > $HC[1]){$HC[1] = $HC[0];}

			#�݌v�v���_�̌v�Z
			$HC[2] = $HC[2] + 100;

			$PL_VALUES[50] = "$HC[0]!$HC[1]!$HC[2]!";

			&DBM_INPORT(P);
			foreach $key (keys %P){
				@NP_VALS = split(/\s/,$P{$key});
				if($PL_VALUES[5] eq $NP_VALS[5] && $NP_VALS[26] >= time-1200){

					&REPAIR(\@NP_VALS);

					@HNC=split(/!/,$NP_VALS[50]);

					#���ݍv���_+100
					$HNC[0] = $HNC[0] + 100;

					#���ݍv���_���ő�v���_�̏ꍇ�͋L�^
					if($HNC[0] > $HNC[1]){$HNC[1] = $HNC[0];}
		
					#�݌v�v���_�̌v�Z
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
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		@Y_HP=split(/!/,$CL_VALUES[11]);
		@Y_ST=split(/!/,$CL_VALUES[12]);$flagc=1;
		&DBM_INPORT(P);

		$YO_HP=int($Y_HP[1]*0.3)-37000;
		$YO_STR=int($Y_ST[0]*400)+9600;
		$YO_VIT=int($Y_ST[1]*400)+9600;
		$YO_AGI=int($Y_ST[2]*400)+9600;

		&ERROR('�������܂���B') if ($FORM{'Cmode'} ne "�񕜏�" && $FORM{'Cmode'} ne "�񕜑�" && $PL_VALUES[6] eq "-1" && $CL_VALUES[1] < 150000);
		if ($FORM{'Cmode'} eq "�񕜏�"){$Y_HP[0]+=int($Y_HP[1]*0.25);$CL_VALUES[1]-=6000;}
		if ($FORM{'Cmode'} eq "�񕜑�"){$Y_HP[0]+=int($Y_HP[1]*0.8);$CL_VALUES[1]-=30000;}
		if ($FORM{'Cmode'} eq "HP����"){$Y_HP[1]+=5000;$CL_VALUES[1]-=$YO_HP;}
		if ($FORM{'Cmode'} eq "�U���͋���"){$Y_ST[0]++;$CL_VALUES[1]-=$YO_STR;}
		if ($FORM{'Cmode'} eq "�h��͋���"){$Y_ST[1]++;$CL_VALUES[1]-=$YO_VIT;}
		if ($FORM{'Cmode'} eq "�����͋���"){$Y_ST[2]++;$CL_VALUES[1]-=$YO_AGI;}
		if ($FORM{'Cmode'} eq "�����ύX"){$CL_VALUES[47]=$FORM{'Zsentaku'};$CL_VALUES[1]-=50000;}
		$CL_VALUES[11]="$Y_HP[0]!$Y_HP[1]!$Y_HP[2]";
		$CL_VALUES[12]="$Y_ST[0]!$Y_ST[1]!$Y_ST[2]!$Y_ST[3]";
	last CUSTOM;};
	$FORM{'cardCheck'} && $PL_VALUES[6] != 0 && $PL_VALUES[5] && do{
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		&DBM_INPORT(P);$flagc=1;$flagp=0;
		if ($FORM{'Emode'} eq "�J�[�h�j��"){$CL_VALUES[15]='';}

		#�t�H�[�`�����̏ꍇ�A�ȉ��̌��ʂɃ����_���ŐU��ւ� (�t�[���@�}�W�V����)
		$Card_F = 0;
		if($FORM{'Emode'} eq '�t�H�[�`����'){
			$Card_F = 1;
			if(int(rand(100)) > 90){
				$FORM{'Emode'} = "�}�W�V����";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�v���G�X�e�X";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�t�[��";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�����@�[�Y";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�`�����I�b�g";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�n�[�~�b�g";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�G���y���[";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�W���X�e�B�X";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�G���v���X";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�f�X";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�X�^�[";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�f�r��";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�T��";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "�^���[";
			}elsif(int(rand(100)) > 90){
				$FORM{'Emode'} = "���[��";
			}else{
				$FORM{'Emode'} = "�W���b�W�����g";
			}
		}
#		&ERROR("$FORM{'Emode'}��$FORM{'chisa'}");
		if($CL_VALUES[15] || $MENTE){
			dbmopen (%P,"$DBM_P",0666);
		foreach $key (keys %P){
			@VS_VALUES = split(/\s/,$P{$key});
		#�t�[��
			if ($FORM{'Emode'} eq "�t�[��"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}" && $VS_VALUES[0] < 30 && ($DATE-$VS_VALUES[26]) > 1200){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓t�[���̃J�[�h�𔭓��I";
				$HOUTIDATE="$key<>$VS_VALUES[0]<>$VS_VALUES[1]<>$VS_VALUES[2]<>$VS_VALUES[3]<>$VS_VALUES[4]<>$VS_VALUES[5]<>$VS_VALUES[6]<>$VS_VALUES[7]<>$VS_VALUES[8]<>$VS_VALUES[9]<>$VS_VALUES[10]<>$VS_VALUES[11]<>$VS_VALUES[12]<>$VS_VALUES[13]<>$VS_VALUES[14]<>$VS_VALUES[15]<>$VS_VALUES[16]<>$VS_VALUES[17]<>$VS_VALUES[18]<>$VS_VALUES[19]<>$VS_VALUES[20]<>$VS_VALUES[21]<>$VS_VALUES[22]<>$VS_VALUES[23]<>$VS_VALUES[24]<>$VS_VALUES[25]<>$VS_VALUES[26]<>$VS_VALUES[27]<>$VS_VALUES[28]<>$VS_VALUES[29]<>$VS_VALUES[30]<>$VS_VALUES[31]<>$VS_VALUES[32]<>$VS_VALUES[33]<>$VS_VALUES[34]<>$VS_VALUES[35]<>$VS_VALUES[36]<>$VS_VALUES[37]<>$VS_VALUES[38]<>$VS_VALUES[39]<>$VS_VALUES[40]<>$VS_VALUES[41]<>$VS_VALUES[42]<>$VS_VALUES[43]<>$VS_VALUES[44]<>$VS_VALUES[45]<>$VS_VALUES[46]<>$VS_VALUES[47]<>$VS_VALUES[48]<>$VS_VALUES[49]<>$VS_VALUES[50]<>$VS_VALUES[51]<>$VS_VALUES[52]<>$VS_VALUES[53]<>$VS_VALUES[54]<>$VS_VALUES[55]<>$VS_VALUES[56]<>$VS_VALUES[57]<>$VS_VALUES[58]<>$VS_VALUES[59]<>$VS_VALUES[60]<>$VS_VALUES[61]<>$VS_VALUES[62]<>$VS_VALUES[63]<>$VS_VALUES[64]<>$VS_VALUES[65]<>$VS_VALUES[66]<>$VS_VALUES[67]<>$VS_VALUES[68]<>$VS_VALUES[69]<>$VS_VALUES[70]<>$VS_VALUES[71]<>$VS_VALUES[72]<>$VS_VALUES[73]<>$VS_VALUES[74]<>$VS_VALUES[75]<>$VS_VALUES[76]<>$VS_VALUES[77]<>$VS_VALUES[78]<>$VS_VALUES[79]<>\n";
				if(!open(OUT,">$LOG_FOLDER2/$key.cgi")){&ERROR('Error',"�o�b�N�A�b�v���s�B�u$key�v���̃��j�b�g�����Ǘ��l�ɕ񍐂��ĉ������B");}
				print OUT $HOUTIDATE;close(OUT);
				chmod(0666,"$LOG_FOLDER2/$key.cgi");
				delete $P{"$key"};
				}
			}
		#�}�W�V����
			if ($FORM{'Emode'} eq "�}�W�V����"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓}�W�V�����̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=20000+int(rand(20000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�v���G�X�e�X
			if ($FORM{'Emode'} eq "�v���G�X�e�X"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓v���G�X�e�X�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						if(($DATE-$VS_VALUES[26]) < 1200){
							$VS_VALUES[15]+=int($VS_VALUES[16]*0.3);
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�G���v���X
			if ($FORM{'Emode'} eq "�G���v���X"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓G���v���X�̃J�[�h�𔭓��I";
					if(($DATE-$VS_VALUES[26]) < 1200){
						$VS_VALUES[25]=0;
					}
				}$P{"$key"}="@VS_VALUES";}
		#�G���y���[
			if ($FORM{'Emode'} eq "�G���y���["){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓G���y���[�̃J�[�h�𔭓��I";
					if(($DATE-$VS_VALUES[26]) < 1200){
						$VS_VALUES[17]+=1000;
					}
				}$P{"$key"}="@VS_VALUES";}
		#�����@�[�Y
			if ($FORM{'Emode'} eq "�����@�[�Y"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓����@�[�Y�̃J�[�h�𔭓��I";
					$VS_VALUES[25]=1;
				}$P{"$key"}="@VS_VALUES";}
		#�`�����I�b�g
			if ($FORM{'Emode'} eq "�`�����I�b�g"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓`�����I�b�g�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=20000+int(rand(15000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�n�[�~�b�g
			if ($FORM{'Emode'} eq "�n�[�~�b�g"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓n�[�~�b�g�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=1000+int(rand(60000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�W���X�e�B�X
			if ($FORM{'Emode'} eq "�W���X�e�B�X"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓W���X�e�B�X�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=20000+int(rand(22000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�f�X
#			if ($FORM{'Emode'} eq "�f�X"){
#				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
#				&REPAIR(\@VS_VALUES);
#				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓f�X�̃J�[�h�𔭓��I";

#					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
#						if($VS_VALUES[15] <= ($VS_VALUES[16]/2)){
#							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
#							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
#							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
#							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
#						}
#					}
#				}$P{"$key"}="@VS_VALUES";}
			if ($FORM{'Emode'} eq "�f�X"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓f�X�̃J�[�h�𔭓��I";
					if($VS_VALUES[0] <= 99 && ($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16])){
						$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
						($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
#					}else{
#						$VS_VALUES[15]=$VS_VALUES[16];$VS_VALUES[25]=0;
					}
				}$P{"$key"}="@VS_VALUES";}
		#�e���p�����X
			if ($FORM{'Emode'} eq "�e���p�����X"){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓e���p�����X�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						if(($DATE-$VS_VALUES[26]) < 1200){
							$VS_VALUES[15]+=int($VS_VALUES[16]*0.6);
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�f�r��
			if ($FORM{'Emode'} eq "�f�r��"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓f�r���̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=int(rand(65000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�^���[
			if ($FORM{'Emode'} eq "�^���["){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓^���[�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=8000+int(rand(5000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�X�^�[
			if ($FORM{'Emode'} eq "�X�^�["){
				if($PL_VALUES[5] eq $VS_VALUES[5]){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓X�^�[�̃J�[�h�𔭓��I";
					if(($DATE-$VS_VALUES[26]) < 1200){
						$VS_VALUES[17]+=500;
					}
				}$P{"$key"}="@VS_VALUES";}
		#���[��
			if ($FORM{'Emode'} eq "���[��"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓��[���̃J�[�h�𔭓��I";
					if($VS_VALUES[0] >= 200){
						$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
						($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
					}else{
						$VS_VALUES[15]=$VS_VALUES[16];$VS_VALUES[25]=0;
					}
				}$P{"$key"}="@VS_VALUES";}
		#�T��
			if ($FORM{'Emode'} eq "�T��"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}" || $VS_VALUES[5] eq $PL_VALUES[5]){
				&REPAIR(\@VS_VALUES);$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓T���̃J�[�h�𔭓��I";
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
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
		#�W���b�W�����g
			if ($FORM{'Emode'} eq "�W���b�W�����g"){
				if($VS_VALUES[5] eq "$FORM{'chisa'}"){
				&REPAIR(\@VS_VALUES);
				$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓W���b�W�����g�̃J�[�h�𔭓��I";
					if($VS_VALUES[25] == 0 || $VS_VALUES[15] == $VS_VALUES[16]){
						$VS_VALUES[15]-=30000+int(rand(30000));
						if($VS_VALUES[15] <= 0){
							$VS_VALUES[15]=0;$VS_VALUES[25]=1;
							unless($VS_VALUES[6]==1){$VS_VALUES[0]-=10;}
							if($VS_VALUES[0] < 0){$VS_VALUES[0]=0;}
							($VS_VALUES[1].="$VS_VALUES[3]&nbsp;�퓬�s\�\\�B");
						}
					}
				}$P{"$key"}="@VS_VALUES";}
			#�f�o�b�O1
				if ($FORM{'Emode'} eq "�f�o�b�O1"){
					$VS_VALUES[8]=1000000;$VS_VALUES[16]=80000;$VS_VALUES[18]=4000;
					$VS_VALUES[19]=50;$VS_VALUES[20]=50;$VS_VALUES[21]=50;$VS_VALUES[22]=50;$VS_VALUES[29]=100;
					$VS_VALUES[24]=1000;
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓f�o�b�O���[�h�𔭓��I";
					$P{"$key"}="@VS_VALUES";
				}
			#�f�o�b�O2
				if ($FORM{'Emode'} eq "�f�o�b�O2"){
					$VS_VALUES[15]=100;
					$VS_VALUES[1]="$DATE!$PL_VALUES[5]�̓f�o�b�O���[�h�𔭓��I";
					$P{"$key"}="@VS_VALUES";
				}
			}
			dbmclose %P;

			dbmopen (%CLA,"$DBM_C",0666);
			while (my($key,$value) = each %CLA){
				my@VL_VALUE = split(/\s/,$value);
#				$x.=$key;
#				if ($FORM{'Emode'} eq '�t�H�[�`����'){if("$key" eq "$FORM{'chisa'}"){$VL_VALUE[5]="";$VL_VALUE[6]="�t�H�[�`�����g�p�I";$VL_VALUE[7]=$DATE;$VL_VALUE[8]="";$VL_VALUE[9]="";$VL_VALUE[10]="";$VL_VALUE[14]="";$VL_VALUE[37]=$DATE+300;}$CLA{"$key"}="@VL_VALUE";}
				if ($FORM{'Emode'} eq '�n���O�h�}��'){if("$key" eq "$FORM{'chisa'}"){$VL_VALUE[1]-=30000+int(rand(80000));if($VL_VALUE[1] < 0){$VL_VALUE[1]=0;}}$CLA{"$key"}="@VL_VALUE";}
			}
			dbmclose %CLA;

#			&ERROR("�t�H�[�`��������$x");

			if($Card_F eq "1"){
				$Effect_F="($FORM{'Emode'})";
				$FORM{'Emode'}="�t�H�[�`����";
			}else{$Effect_F="";}

			$message="<b class=rb3>$PL_VALUES[5]</b>��";
			$message.="<b class=rb3>$FORM{'chisa'}</b>��" if $CL_VALUES[15] =~ m/a|b|g|h|j|k|l|m|n|p|q|s|t|u/;
			$message.="$FORM{'Emode'}�̃J�[�h$Effect_F�𔭓����܂����B";

			dbmopen (%DH,"$DBM_H",0666);
				$DH{"$DATE"}="$message";
			dbmclose %DH;

			if ($FORM{'Emode'} eq '�n�C�G���t�@���g'){$CL_VALUES[5]="";$CL_VALUES[7]=$DATE;$CL_VALUES[8]="";$CL_VALUES[9]="";$CL_VALUES[10]="";$CL_VALUES[14]="";}
			if ($FORM{'Emode'} eq '�X�g�����O�X'){$CL_VALUES[1]+=30000+int(rand(80000));if($CL_VALUES[1] > 200000){$CL_VALUES[1]=200000;}}
			if ($FORM{'Emode'} eq '���[���h'){$CL_VALUES[38]=$DATE+3600;}
		}
		$CL_VALUES[15]='';

	last CUSTOM;};

	/^����$/ && $PL_VALUES[5] && $PL_VALUES[6] && $CL_VALUES[7] && do{
		&DBM_INPORT(C);&ERROR('�������݂��܂���B') if !$C{"$PL_VALUES[5]"};
		if ($FORM{'main'} and $FORM{'main'} ne '����� '){$CL_VALUES[6]="$FORM{'main'}";$CNAME[0]=$FORM{'main'};$c++;}
		if ($FORM{'u1'} and $FORM{'u1'} ne '����� '){$CL_VALUES[8]="$FORM{'u1'}";$CNAME[1]=$FORM{'u1'};}
		if ($FORM{'u2'} and $FORM{'u2'} ne '����� '){$CL_VALUES[9]="$FORM{'u2'}";$CNAME[2]=$FORM{'u2'};}
		if ($FORM{'u3'} and $FORM{'u3'} ne '����� '){$CL_VALUES[10]="$FORM{'u3'}";$CNAME[3]=$FORM{'u3'};}
		$flagc=1;$flagp=0;$CL_VALUES[14]="0";
		$CL_FRAG="$CL_VALUES[7]";$CL_VALUES[1]-=$FORM{'dmmy'};
		if($CL_FRAG > time){$CL_VALUES[7]+=1800*$FORM{'kikan'};}
		else{$CL_VALUES[7]=time+1800*$FORM{'kikan'};$CL_VALUES[5]="����J�n";}

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
#		$HISTORY="$CON��<B class=rb3>$PL_VALUES[5]</B>���A<B class=rb2>$CNAME[0]$TEKI_1$TEKI_2$TEKI_3</B>�ɉ���J�n�B";
		$HISTORY="<B class=rb3>$PL_VALUES[5]</B>���A<B class=rb2>$CNAME[0]$TEKI_1$TEKI_2$TEKI_3</B>�ɉ���J�n�B";
	last CUSTOM;};
	/^�����A�C$/ && $PL_VALUES[5] && !$PL_VALUES[6] && do{&DBM_INPORT(P);
		while (my($key,$value) = each %P){my@VS_VALUE = split(/\s/,$value);
#			if($FORM{'team'} eq ""){&ERROR('�G���[');}
			if($FORM{'team'} eq "$VS_VALUE[28]" && $VS_VALUE[6] == -1){
				&ERROR('�ʂ̐l�������ɏA�C���Ă��܂��B');
			}
		}
		if($FORM{'team'} ne ""){$PL_VALUES[6]='-1';$PL_VALUES[28]="$FORM{'team'}";}
	last CUSTOM;};
	/^�����A�C$/ && $PL_VALUES[5] && $PL_VALUES[6] == 0 && do{&DBM_INPORT(P);
		while (my($key,$value) = each %P){my@VS_VALUE = split(/\s/,$value);
			if($PL_VALUES[5] eq "$VS_VALUE[5]" && $VS_VALUE[6] == 1){&ERROR('�ʂ̐l�������ɏA�C���Ă��܂��B');}
		}
		$PL_VALUES[6]='1';$PL_VALUES[28]='';$PL_VALUES[0]='220';
		if ($PL_VALUES[39] eq "1"){$CON = $CONTINENT_A;}else{$CON = $CONTINENT_B;}
#		$HISTORY="$CON��$FORM{'pname'} �̑����A�C�� <B class=rb1>$PL_VALUES[5]</B>�c����F�B$FORM{'pname'}�ɑS�w�����ϔC�B";
		$HISTORY="$FORM{'pname'} �̑����A�C�� <B class=rb1>$PL_VALUES[5]</B>�c����F�B$FORM{'pname'}�ɑS�w�����ϔC�B";
	last CUSTOM;};
	/^�X�L������$/ && do{&DBM_INPORT(P);
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
	/^�������$/ && do{&DBM_INPORT(P);
		require "./$LOG_FOLDER/$HASH_DATA";
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);

		if($PL_VALUES[8] >= 5000000){
			$PL_VALUES[8] = $PL_VALUES[8] - 5000000;
			$WAEnt = 0;

			$PL_VALUES[9] = "$WN_A!$WLV_A!$WAEnt!$WA03!$WA04!$WA05!$WA06!$WA07!$WA08!$WA09!$WA10!$WA11!$WA12!$WA13!$WA14!$WA15!$WA16!$WA17!$WA18!$WA19!$WA20!$WA21!$WA22!$WA23!$WA24!$WA25!$WA26!$WA27!$WA28!$WA29!$WA30!$WA31!$WA32!$WA33!$WA34!$WA35!$WA36!$WA37!$WA38!$WA39!$WA40!$WA41!$WA42";

		}
		
	last CUSTOM;};
	/^�����$/ && do{&DBM_INPORT(P);
		require "./$LOG_FOLDER/$HASH_DATA";
		local($WN_A,$WLV_A,$WAEnt,$WA03,$WA04,$WA05,$WA06,$WA07,$WA08,$WA09,$WA10,$WA11,$WA12,$WA13,$WA14,$WA15,$WA16,$WA17,$WA18,$WA19,$WA20,$WA21,$WA22,$WA23,$WA24,$WA25,$WA26,$WA27,$WA28,$WA29,$WA30,$WA31,$WA32,$WA33,$WA34,$WA35,$WA36,$WA37,$WA38,$WA39,$WA40,$WA41,$WA42) = split(/!/,$PL_VALUES[9]);

		if($WAEnt eq ""){$WAEnt = 0;}
		$EntCost = ($WAEnt + 1) * 100000;
		if($PL_VALUES[8] >= $EntCost && $WAEnt < 100){
			$PL_VALUES[8] = $PL_VALUES[8] - $EntCost;
			$WAEnt = $WAEnt + 1;

			#�������A��m���Ń��Z�b�g���ꂸ�ɕt�^���ꂽ�G���`�����g��+1
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
	&ERROR('����������܂���B') if $PL_VALUES[8] < 0 || $CL_VALUES[1] < 0;
	if($flagr){dbmopen (%R,"$DBM_R",0666);$R{"server"}="@R_VALUES";dbmclose %R;}
	if($flagp){dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;}
	if($flagc){dbmopen (%CL,"$DBM_C",0666);$CL{"$PL_VALUES[5]"}="@CL_VALUES";dbmclose %CL;}
	if($HISTORY){dbmopen (%DH,"$DBM_H",0666);$DH{"$DATE"}="$HISTORY";dbmclose %DH;}
	if($HISTORY2){$DATESA=$DATE+$JIKANSA*60;dbmopen (%DH,"$DBM_H",0666);$DH{"$DATESA"}="$HISTORY2";dbmclose %DH;}
	&UNLOCK;
}


1;

sub BATTLE3{
		print "<font color=#f7e957>$FORM{'pname'} は レベルが上がった</font><br>";
		$PL_VALUES[30]=0;
		$PL_VALUES[29]++;
		
		#アビリティシステム
		if($AbiSys == 1){

			if($PL_VALUES[53] eq ""){$PL_VALUES[53]=0;}
			$PL_VALUES[53]=$PL_VALUES[53]+10;
			$LvChk = $PL_VALUES[29] % 5;
			if($LvChk == 0){$PL_VALUES[53] = $PL_VALUES[53] + 20;}
			if($PL_VALUES[53]>9999){$PL_VALUES[53]=9999;}

		}
		
		sub BONUS{"&nbsp;&nbsp;&nbsp;<font color=#f7e957>$_[0]がわずかにアップ。</font><br>";}

		$C=$PL_VALUES[23];$C=4 if $C > 4;
		$StatusMax=('20','30','35','40','50')[$C];

		$BoAt=9+$PL_CLASS[1];
		$BoDe=11+$PL_CLASS[2];
		$BoSp=11+$PL_CLASS[3];
		$BoAg=11+$PL_CLASS[4];

		if (rand(18) < $BoAt && $PL_VALUES[19] < $StatusMax){print &BONUS('攻撃力');$PL_VALUES[19]++;}
		if (rand(22) < $BoDe && $PL_VALUES[20] < $StatusMax){print &BONUS('防御力');$PL_VALUES[20]++;}
		if (rand(20) < $BoSp && $PL_VALUES[21] < $StatusMax){print &BONUS('スピード');$PL_VALUES[21]++;}
		if (rand(20) < $BoAg && $PL_VALUES[22] < $StatusMax){print &BONUS('命中力');$PL_VALUES[22]++;}

		if($PL_WB[7] =~ m/!E0005/ || $PL_WC[7] =~ m/!E0005/ || $PL_WD[7] =~ m/!E0005/){
	
			if ($PL_VALUES[25] eq "0"){$PL_VALUES[17] = $PL_VALUES[17] + int($PL_VALUES[18] * 0.4);}
			if ($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}
			print "<font color=\"#f7e957\">MPチャージ！$PL_VALUES[3]のMPが回復しました。</font><br>\n";
	
		}


}


1;

sub BATTLE3{
		print "<font color=#f7e957>$FORM{'pname'} �� ���x�����オ����</font><br>";
		$PL_VALUES[30]=0;
		$PL_VALUES[29]++;
		
		#�A�r���e�B�V�X�e��
		if($AbiSys == 1){

			if($PL_VALUES[53] eq ""){$PL_VALUES[53]=0;}
			$PL_VALUES[53]=$PL_VALUES[53]+10;
			$LvChk = $PL_VALUES[29] % 5;
			if($LvChk == 0){$PL_VALUES[53] = $PL_VALUES[53] + 20;}
			if($PL_VALUES[53]>9999){$PL_VALUES[53]=9999;}

		}
		
		sub BONUS{"&nbsp;&nbsp;&nbsp;<font color=#f7e957>$_[0]���킸���ɃA�b�v�B</font><br>";}

		$C=$PL_VALUES[23];$C=4 if $C > 4;
		$StatusMax=('20','30','35','40','50')[$C];

		$BoAt=9+$PL_CLASS[1];
		$BoDe=11+$PL_CLASS[2];
		$BoSp=11+$PL_CLASS[3];
		$BoAg=11+$PL_CLASS[4];

		if (rand(18) < $BoAt && $PL_VALUES[19] < $StatusMax){print &BONUS('�U����');$PL_VALUES[19]++;}
		if (rand(22) < $BoDe && $PL_VALUES[20] < $StatusMax){print &BONUS('�h���');$PL_VALUES[20]++;}
		if (rand(20) < $BoSp && $PL_VALUES[21] < $StatusMax){print &BONUS('�X�s�[�h');$PL_VALUES[21]++;}
		if (rand(20) < $BoAg && $PL_VALUES[22] < $StatusMax){print &BONUS('������');$PL_VALUES[22]++;}

		if($PL_WB[7] =~ m/!E0005/ || $PL_WC[7] =~ m/!E0005/ || $PL_WD[7] =~ m/!E0005/){
	
			if ($PL_VALUES[25] eq "0"){$PL_VALUES[17] = $PL_VALUES[17] + int($PL_VALUES[18] * 0.4);}
			if ($PL_VALUES[17] > $PL_VALUES[18]){$PL_VALUES[17] = $PL_VALUES[18];}
			print "<font color=\"#f7e957\">MP�`���[�W�I$PL_VALUES[3]��MP���񕜂��܂����B</font><br>\n";
	
		}


}


1;

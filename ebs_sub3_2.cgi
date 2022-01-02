sub CNTRY_LIST{

	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}

$CookieValue = $ENV{'HTTP_COOKIE'};
$CookieValue =~ s/\+/ /g;
$CookieValue =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C",hex($1))/eg;

	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$key =~ s/ //g;$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}


	$CO_NAME=$FORM{'CNTRY'};
	$FORM{'con'}=$FORM{'con2'} if $FORM{'con'} eq "";
	($FORM{'CNTRY'}='',$CL_VALUES[0]='#000000') if $FORM{'CNTRY'} eq "$NONE_NATIONALITY";
	&HEADER;
	&LOCK;&DBM_INPORT(P);&DBM_INPORT(C);&UNLOCK;
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
#	@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
	@CL_VALUES = split(/\s/,$C{"$FORM{'CNTRY'}"});
	@GL_VALUES = split(/\s/,$C{"$PL_VALUES[5]"});
	require "./$LOG_FOLDER/_hash.data";
	require "./$LOG_FOLDER/$CLASS_DATA";

#	&ERROR("$FORM{'con2'}ああ$CO_NAME");

	sub TR {local($WN_A,$WLV_A) = split(/!/,$VALUES[9]);$WLV_A=int($WLV_A/$WEAPON_LVUP);
			local($WN_S,$WLV_S) = split(/!/,$VALUES[41]);$WLV_S=int($WLV_S/$WEAPON_LVUP);
			if($VALUES[41] ne ""){$HYLV="(LV$WLV_S)";}else{$HYLV="";}
			if ($FORM{'CNTRY'} eq "$PL_VALUES[5]" || $COOKIE{'pass'} eq $MASTERPASS){
				@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
				@WN_sS=split(/\,/,$WEAPON_LIST{"$WN_S"});
				@ALY_CLASS=split(/\,/,$VCLASS_LIST{"$VALUES[4]"});
				$CLASS_PL=$ALY_CLASS[0];
				$LV_PL=$VALUES[29];
			}else{$WN_sA[0]='????????';$CLASS_PL='????';$WN_sS[0]='????????';$HYLV="";
			$LV_PL="<font color=#143dca>↑</font>" if $PL_VALUES[29] <= $VALUES[29];
			$LV_PL="<font color=#dc143c>↓</font>" if $PL_VALUES[29] > $VALUES[29];
			}

		if ((($FORM{'CNTRY'} eq "$GL_VALUES[6]") || ($FORM{'CNTRY'} eq "$GL_VALUES[8]") || ($FORM{'CNTRY'} eq "$GL_VALUES[9]") || ($FORM{'CNTRY'} eq "$GL_VALUES[10]")) && ($FORM{'CNTRY'} ne '') && ($GL_VALUES[7] > time) || (($FORM{'CNTRY'} ne "$PL_VALUES[5]") && ($CL_VALUES[7] > time)) || $WW_FRAG==1){ $SENJI="&nbsp;<font color=#808080>不明</font>&nbsp;"; }
		elsif(LOGIN_CHECK($Key)){ $SENJI="<font color=#dc143c>参戦中</font>"; }
		else{ $SENJI="<font color=#143dca>休戦中</font>";}
			"<tr><td nowrap style=\"color:$VALUES[13];\">$Key</td>
			<td>".&RANK($VALUES[0],$VALUES[5],$VALUES[6])."</td>
			<td><img src=$IMG_FOLDER2/$VALUES[27].gif width=32 height=32></td>
			<td align=center>".&STATUS_CONVERT("$VALUES[19]",'s')."</td>
			<td align=center>".&STATUS_CONVERT("$VALUES[20]",'s')."</td>
			<td align=center>".&STATUS_CONVERT("$VALUES[21]",'s')."</td>
			<td align=center>".&STATUS_CONVERT("$VALUES[22]",'s')."</td>
			<td align=center>".&STATUS_CONVERT("$VALUES[24]",'j')."</td>
			<td align=center>".&STATUS_CONVERT("$VALUES[12]",'l')."</td>
			<td align=center>".&STATUS_CONVERT("$VALUES[31]",'e')."</td>
			<td align=center><b>$LV_PL</b></td>
			<td><b>$CLASS_PL</b></td>
			<td><b>".$WN_sA[0]."(LV$WLV_A)</b></td>
			<td><b>".$WN_sS[0].$HYLV."</b></td>
			<td align=center>$SENJI</td></tr>"
	}


	print << "	-----END-----";
	<script language="JavaScript">
	var timID;
	function cota(na,ma){fma.CNTRY.value=na;c=1;kikan(ma);}
	function cotb(nb,mb){fmb.CNTRY.value=nb;c=2;kikan(mb);}
	function kikan(ms){s = ms;clearTimeout(timID);
	if(s>0){s--;timID=setTimeout('kikan(s)',1000);}else if(c==1){fma.goa.click();}else if(c==2){fmb.gob.click();}
	}
	</script>
	<b style=\"font-size:13px;\">どの国の情報を見ますか？</b><br>


	-----END-----
#			<b style="font-size:13px;">$CONTINENT_A</b><br>
#			<b style="font-size:13px;">天宮シャングリラ</b><br>

		foreach my $C_Name ( sort keys %C ) {
			@C_VALUES = split(/\s/,$C{$C_Name});

				if($FORM{'CNTRY'} eq "$C_Name"){$RLO='0';}else{$RLO='0';}
					print "<input type=submit value=\"$C_Name\"";
					print "onClick=\"cota('$C_Name','$RLO');\" STYLE=\" background:$C_VALUES[0];color:black\">\n";
				}
		print "<input type=submit value=\"$NONE_NATIONALITY\"";
		print "onClick=\"cota('$NONE_NATIONALITY','0');\" STYLE=\" background:#808080;color:white\">\n";
#ゼテギネア大陸
#		while (($C_Name,$C_Value) =each %C) {
#			@C_VALUES = split(/\s/,$C_Value);

#			if ($C_VALUES[39] eq "1"){
#				if($FORM{'CNTRY'} eq "$C_Name"){$RLO='5';}else{$RLO='2';}
#					print "<input type=submit value=\"$C_Name\"";
#					print "onClick=\"cota('$C_Name','$RLO');\" STYLE=\" background:$C_VALUES[0];color:black\">\n";
#				}
#		}
#		print "<input type=submit value=\"$NONE_NATIONALITY\"";
#		print "onClick=\"cota('$NONE_NATIONALITY','3');\" STYLE=\" background:#808080;color:white\">\n";

#ガリシア大陸
#		print "<br><b style=\"font-size:13px;\">$CONTINENT_B</b><br>";
#		while (($C_Name,$C_Value) =each %C) {
#			@C_VALUES = split(/\s/,$C_Value);

#			if ($C_VALUES[39] eq "2"){
#				if($FORM{'CNTRY'} eq "$C_Name"){$RLO='5';}else{$RLO='2';}
#					print "<input type=submit value=\"$C_Name\"";
#					print "onClick=\"cotb('$C_Name','$RLO');\" STYLE=\" background:$C_VALUES[0];color:black\">\n";
#			}

#		}
#		print "<input type=submit value=\"$NONE_NATIONALITY\"";
#		print "onClick=\"cotb('$NONE_NATIONALITY','3');\" STYLE=\" background:#808080;color:white\">\n";

	print << "	-----END-----";
	<form action=$MAIN_SCRIPT method=POST name=fma target=Sub onSubmit="">
	<input type=hidden name="cmd" value="CO_LIST">
	<input type=hidden name="CNTRY">
	<input type=hidden name="con" value="1">
	<input type=submit name="goa" style="display:none;">
	</form>
	-----END-----
#	<form action=$MAIN_SCRIPT method=POST name=fmb target=Sub onSubmit="">
#	<input type=hidden name="cmd" value="CO_LIST">
#	<input type=hidden name="CNTRY">
#	<input type=hidden name="con" value="2">
#	<input type=submit name="gob" style="display:none;">
#	</form>

	if($CO_NAME){

	print "<table border=1 cellspacing=1 cellpadding=1 bordercolor=#484848 style=\"font-size:15px;background:black;border:2px solid $CL_VALUES[0];\">";
	print "<tr><td colspan=15 bgcolor=$CL_VALUES[0]>";
	print "<table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:35px;\"><tr><td>$CO_NAME";
#所持カード
	if($CL_VALUES[15]){
		require "./$LOG_FOLDER/$CARD_DATA";
		my@vcard=split(/\,/,$VACARD_LIST{"$CL_VALUES[15]"});
		print "<span style=\"font-size:15px;\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src=$IMG_FOLDER6/card.gif>&nbsp;</span>";
		print "<span style=\"font-size:15px;\">$vcard[1]&nbsp;&nbsp;&nbsp;</span>";
	}

	print "<span style=\"font-size:15px;\">&nbsp;&nbsp;滅ぼした国&nbsp;</span>";

	$DECLT=int($CL_VALUES[13]/10);$DECL=$CL_VALUES[13]-$DECLT*10;
	for ($h=1;$h<=$DECLT;$h++){print "<img src=\"$IMG_FOLDER2/1000.gif\" width=\"32\" height=\"32\">";}
	for ($h=1;$h<=$DECL;$h++){print "<img src=\"$IMG_FOLDER2/1000.gif\" width=\"16\" height=\"16\">";}


	print "</td></tr></table></td></tr>";
	print "<tr><td>Name</td><td>Rank</td><td>&nbsp;</td><td>$STATUS_NAME[0]</td><td>$STATUS_NAME[1]</td><td>$STATUS_NAME[2]</td><td>$STATUS_NAME[3]</td><td>熟</td><td>ALI</td><td>ELE</td><td>Lv.</td><td>$STATUS_NAME[6]</td><td>Weapon</td><td>SWeapon</td><td>状況</td></tr>";


	foreach $Key (sort {$P{$b} <=> $P{$a}} keys %P){
		@VALUES = split(/\s/,$P{$Key});
		if(($TIME[2] =~ /^6$|^7$|^8$|^9$|^10$|^11$|^12$|^13$|^14$|^15$|^16$|^17$/i) && ($VALUES[4] =~ /^64$|^71$|^72$/i)){
		if($VALUES[4] == 71){$VALUES[4]=210;}
		if($VALUES[4] == 72){$VALUES[4]=211;}
		if($VALUES[4] == 64){$VALUES[4]=65;}
	}

#	if($FORM{'con'} eq "$VALUES[39]"){

		if ($FORM{'CNTRY'} eq "$VALUES[5]" && !$VALUES[28] && ($VALUES[6] == 1 || $VALUES[6] == 0)){print &TR;}

			if ($FORM{'CNTRY'} && $FORM{'CNTRY'} eq "$VALUES[5]" && $VALUES[28]){
				($UNIT_A.= &TR,$uflag_A=1) if $VALUES[28] eq $CL_VALUES[2] && $VALUES[6] != -1;
				($UNIT_B.= &TR,$uflag_B=1) if $VALUES[28] eq $CL_VALUES[3] && $VALUES[6] != -1;
				($UNIT_C.= &TR,$uflag_C=1) if $VALUES[28] eq $CL_VALUES[4] && $VALUES[6] != -1;
				($LEADER_A.= &TR,$lflag_A=1) if $VALUES[28] eq $CL_VALUES[2] && $VALUES[6] == -1;
				($LEADER_B.= &TR,$lflag_B=1) if $VALUES[28] eq $CL_VALUES[3] && $VALUES[6] == -1;
				($LEADER_C.= &TR,$lflag_C=1) if $VALUES[28] eq $CL_VALUES[4] && $VALUES[6] == -1;
			}

		}
		$plys++;
#	}

	if ($FORM{'CNTRY'}){
	print "<tr><td colspan=15 bgcolor=$CL_VALUES[0]><table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:25px;\">";
	print "<tr><td>&nbsp;<b>第一部隊</b>&nbsp;";
	print $CL_VALUES[2] ? "$CL_VALUES[2]</td></tr></table>":!$CL_VALUES[2] ? '未結成</td></tr></table>':'</td></tr></table></td></tr>';
	print $lflag_A ? "$LEADER_A":!$lflag_A ? "<tr><td colspan=15>隊長不在</td></tr>":'\n';
	print $uflag_A ? "$UNIT_A":!$uflag_A ? "<tr><td colspan=15>NoPlayer</td></tr>":'';
	print "<tr><td colspan=15 bgcolor=$CL_VALUES[0]><table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:25px;\">";
	print "<tr><td>&nbsp;<b>第二部隊</b>&nbsp;";
	print $CL_VALUES[3] ? "$CL_VALUES[3]</td></tr></table>":!$CL_VALUES[3] ? '未結成</td></tr></table>':'</td></tr></table></td></tr>';
	print $lflag_B ? "$LEADER_B":!$lflag_B ? "<tr><td colspan=15>隊長不在</td></tr>":'\n';
	print $uflag_B ? "$UNIT_B":!$uflag_B ? "<tr><td colspan=15>NoPlayer</td></tr>":'';
	print "<tr><td colspan=15 bgcolor=$CL_VALUES[0]><table height=\"100%\" width=\"100%\" border=0 cellspacing=0 cellpadding=0  bgcolor=\"black\" style=\"color:$CL_VALUES[0];font-size:25px;\">";
	print "<tr><td>&nbsp;<b>第三部隊</b>&nbsp;";
	print $CL_VALUES[4] ? "$CL_VALUES[4]</td></tr></table>":!$CL_VALUES[4] ? '未結成</td></tr></table>':'</td></tr></table></td></tr>';
	print $lflag_C ? "$LEADER_C":!$lflag_C ? "<tr><td colspan=15>隊長不在</td></tr>":'\n';
	print $uflag_C ? "$UNIT_C":!$uflag_C ? "<tr><td colspan=15>NoPlayer</td></tr>":'';
	}

	print "</table><br><br><br><br>";
}
	&FOOTER;
	exit;
}


1;

sub bukilist{
	print <<"	-----END-----";
HTTP/1.1 200 OK
Content-Type: text/html

<script language="JavaScript"><!--
	document.write ('<html><head>');
	document.write ('<title>Tactics Ogre de Endless Battle 304 Edition Class Edit</title></head>');
	document.write ('<frameset rows="50,*" border="0" framespacing="0">');
	document.write ('<frame name="Main" frameborder="NO" src="$MAIN_SCRIPT?bukilist1">');
	document.write ('<frame name="Sub" frameborder="NO" src="$MAIN_SCRIPT?bukilist2">');
	document.write ('</frameset>');
	document.write ('</html>');
// --></script>
<noscript>JavaScript�Ή��u���E�U�ł��V�щ������B</noscript>
	-----END-----
}
sub bukilist1{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	&HEADER;
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	-----END-----

	require "./$LOG_FOLDER/$HASH_DATA";
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT name="FM" method="POST" target=Sub>
	<script language="JavaScript">
		function Move(){parent.Sub.location.replace("$BACKFR");}
	</script>
	
		<input type=hidden name=cmd>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
	<select name="classlf">
	-----END-----

	foreach $Key (sort{$a cmp $b} keys %WEAPONEF_LIST){
		my@change = split(/\,/,$WEAPONEF_LIST{$Key});
		$change[0]='��' if $Key eq '00';
		$change[0]='��' if $Key eq '01';
		$change[0]='��n' if $Key eq '02';
		$change[0]='��' if $Key eq '03';
		$change[0]='�_��' if $Key eq '04';
		$change[0]='�Í�' if $Key eq '05';
		$change[0]='���\\�ω�' if $Key eq '6d';
		$change[0]='�u���X�g�U��' if $Key eq '6e';
		print "<option value=\"$Key\">$change[0]\n";
	}
	print << "	-----END-----";
	</select>
	<input type=submit name="custom" value="change" onClick="document.FM.cmd.value='bukilist2';Move()">
	</form>
	</td></tr></table>
	</body>
	-----END-----
}
sub bukilist2{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	&HEADER;

	require "./$LOG_FOLDER/$HASH_DATA";

	my@vijunu=split(/\,/,$WEAPONEF_LIST{"$FORM{'classlf'}"});
	$toku = "$vijunu[0]";

	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
	<tr><td style="background-color:$TABLE_COLOR2;padding:3px;" colspan="12"><b>$toku</b></td></tr>
	-----END-----
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@vistge = split(/\,/,$WEAPON_LIST{$Key});
		my@WN_sA_ef = split(/!/,$vistge[7]);
		$tokusyu='';
		foreach $j (@WN_sA_ef){
			@vijunu=split(/\,/,$WEAPONEF_LIST{"$j"});
			$tokusyu .= "$vijunu[0]&nbsp;"if $j;
		}
		print "<tr bgcolor=\"$TABLE_COLOR3\"><td>$Key</td><td style=\"white-space: nowrap;\"><img src=\"$IMG_FOLDER4/$vistge[9].gif\">&nbsp;$vistge[0]</td><td>".&STATUS_CONVERT($vistge[1]*((99*0.003)+1)*$vistge[3]/500,'s')."<br>(".&STATUS_CONVERT($vistge[1]*$vistge[3]/500,'s').")</td><td>".int($vistge[1]*((99*0.003)+1)*$vistge[3])."<br>(".$vistge[1]*$vistge[3].")</td><td>".&STATUS_CONVERT($vistge[2]/4,'s')."</td><td>($vistge[2])</td><td>$vistge[3]</td><td>$vistge[4]</td><td>$vistge[5]<br>(".int($vistge[5]/2).")</td><td>$tokusyu</td><td>".int($vistge[1]*$vistge[3]/$vistge[4])."</td></tr>" if $vistge[7] =~ m/$FORM{'classlf'}/;
	}
	print "</table>";
	print "</body>";
}

sub classlist{
	print <<"	-----END-----";
HTTP/1.1 200 OK
Content-Type: text/html

<script language="JavaScript"><!--
	document.write ('<html><head>');
	document.write ('<title>Tactics Ogre de Endless Battle 304 Edition Class Edit</title></head>');
	document.write ('<frameset rows="$UPPER_FRAME,*" border="0" framespacing="0">');
	document.write ('<frame name="Main" frameborder="NO" src="$MAIN_SCRIPT?classlist1">');
	document.write ('<frame name="Sub" frameborder="NO" src="$MAIN_SCRIPT?classlist2">');
	document.write ('</frameset>');
	document.write ('</html>');
// --></script>
<noscript>JavaScript�Ή��u���E�U�ł��V�щ������B</noscript>
	-----END-----
}

sub classlist1{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	&HEADER;
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	-----END-----

	require "./$LOG_FOLDER/$CLASS_DATA";
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT name="FM" method="POST" target=Sub>
	<script language="JavaScript">
		function Move(){parent.Sub.location.replace("$BACKFR");}
	</script>
	
		<input type=hidden name=cmd>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
	<select name="classlf">
	-----END-----

	foreach $Key (sort{$a <=> $b} keys %VCLASS_LIST){
		my@change = split(/\,/,$VCLASS_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n";
	}
	print << "	-----END-----";
	</select>
	<input type=submit name="custom" value="change" onClick="document.FM.cmd.value='classlist2';Move()">
	</form>
	</td></tr></table>
	</body>
	-----END-----
	print "<script language=\"JavaScript\">location.href='#top';\n</script>\n" if $BANNER_DISPLAY;

}

sub classlist2{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;
	require "./$LOG_FOLDER/$CLASS_DATA";

	&HEADER;

	foreach $Key (sort{$a <=> $b} keys %VCLASS_LIST){
		my@ALY_CLASS = split(/\,/,$VCLASS_LIST{$Key});
	if($Key == $FORM{'classlf'}){

print << "-----END-----";
	<table border=1 width=100%><tr><td>Edit</td><td>�v���r���[</td></tr>
	<tr><td>

	<table cellspacing=0 cellpadding=3 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr><td style="background-color:$TABLE_COLOR2;padding:3px;" colspan="4"><b>$ALY_CLASS[0]</b></td></tr>
	<tr><td colspan="2">�N���X���c<input type=text size="15" name="para0" value="$ALY_CLASS[0]"></td><td>�U���c<input type=text size="1" name="para1" value="$ALY_CLASS[1]"></td><td>�h��c<input type=text size="1" name="para2" value="$ALY_CLASS[2]"></td><td>����c<input type=text size="1" name="para3" value="$ALY_CLASS[3]"></td><td>�����c<input type=text size="1" name="para4" value="$ALY_CLASS[4]"></td></tr>
	<tr><td colspan="2">
-----END-----

	my@mnu=('��������CC�\\','�����t','����K�v','���j������L��','��������K�v','�镐��','������','��','��','�w��','�w������');
	print "<select name=\"para5\">";
	for ($ca=0;$ca<=10;$ca++){
		print "<option value=$ca";
		print " selected" if $ALY_CLASS[5] == $ca;
		print ">$mnu[$ca]\n";
	}
	print "</select>";

print << "-----END-----";
	</td><td>STR�c<input type=text size="1" name="para6" value="$ALY_CLASS[6]"></td><td>VIT�c<input type=text size="1" name="para7" value="$ALY_CLASS[7]"></td><td>AGI�c<input type=text size="1" name="para8" value="$ALY_CLASS[8]"></td><td>DEX�c<input type=text size="1" name="para9" value="$ALY_CLASS[9]"></td></tr>
	<tr><td>HP�c<input type=text size="5" name="para10" value="$ALY_CLASS[10]"></td><td>MP�c<input type=text size="4" name="para11" value="$ALY_CLASS[11]"></td><td colspan="2">ALI�c<input type=text size="1" name="para12" value="$ALY_CLASS[12]">�`<input type=text size="1" name="para13" value="$ALY_CLASS[13]"></td><td colspan="2">�n���x�c<input type=text size="5" name="para14" value="$ALY_CLASS[14]"></td></tr>


	</table>

	</td><td>
-----END-----

		if($ALY_CLASS[13] <= 35){$ALI[$key]='C';}
		elsif($ALY_CLASS[12] > 35 && $ALY_CLASS[13] <= 71){$ALI[$key]='N';}
		elsif($ALY_CLASS[12] > 71){$ALI[$key]='L';}
		elsif($ALY_CLASS[12] >= 0 && $ALY_CLASS[13] <= 71){$ALI[$key]='N�C';}
		elsif($ALY_CLASS[12] > 35){$ALI[$key]='L�N';}
		else{$ALI[$key]='L�N�C';}

		if($ALY_CLASS[5]){
			if($ALY_CLASS[10] > 0){$ALI[$key] = $ALI[$key]."�AHP�c$ALY_CLASS[10]";
				if($ALY_CLASS[10] < 80000){$ALI[$key] = $ALI[$key].'�ȏ�';}
			}
			if($ALY_CLASS[11] > 0){$ALI[$key] = $ALI[$key]."�AMP�c$ALY_CLASS[11]";
				if($ALY_CLASS[11] < 4000){$ALI[$key] = $ALI[$key].'�ȏ�';}
			}
			if($ALY_CLASS[6] > 0){$ALI[$key] = $ALI[$key].'�ASTR�c'.&STATUS_CONVERT("$ALY_CLASS[6]",'s');
				if($ALY_CLASS[6] < 50){$ALI[$key] = $ALI[$key].'�ȏ�';}
			}
			if($ALY_CLASS[7] > 0){$ALI[$key] = $ALI[$key].'�AVIT�c'.&STATUS_CONVERT("$ALY_CLASS[7]",'s');
				if($ALY_CLASS[7] < 50){$ALI[$key] = $ALI[$key].'�ȏ�';}
			}
			if($ALY_CLASS[8] > 0){$ALI[$key] = $ALI[$key].'�AAGI�c'.&STATUS_CONVERT("$ALY_CLASS[8]",'s');
				if($ALY_CLASS[8] < 50){$ALI[$key] = $ALI[$key].'�ȏ�';}
			}
			if($ALY_CLASS[9] > 0){$ALI[$key] = $ALI[$key].'�ADEX�c'.&STATUS_CONVERT("$ALY_CLASS[9]",'s');
				if($ALY_CLASS[9] < 50){$ALI[$key] = $ALI[$key].'�ȏ�';}
			}
			if($ALY_CLASS[14] > 0){
				if($ALY_CLASS[14] >= 1100){$AMA=$ALY_CLASS[14]-1000;$AMA="+$AMA"}
				$ALI[$key] = $ALI[$key].'�A�n���x�c'.&STATUS_CONVERT("$ALY_CLASS[14]",'j')."$AMA�ȏ�";
			}
			if($ALY_CLASS[21]){$ALI[$key] = $ALI[$key].'�A�w���c'.&STATUS_CONVERT("$ALY_CLASS[21]",'z').'�ȏ�';}
			if($ALY_CLASS[20]){$ALY_CLASS[20]-=200;$ALI[$key] = $ALI[$key]."�A�n���x��D�ɂȂ��Ă���̌��j����$ALY_CLASS[20]�ȉ�";}
			if($ALY_CLASS[15]){
				if($ALY_CLASS[15] =~ /!1b/i){$ALY_CLASS[15]="�e";}
				if($ALY_CLASS[15] =~ /!6e/i){$ALY_CLASS[15]="�u���X�g�U��";}
				$ALI[$key] = $ALI[$key]."�A�����c$ALY_CLASS[15]";
			}
		}
$HOSEI[$key]='�␳�c';
if($ALY_CLASS[1]){if($ALY_CLASS[1]>0){$ALY_CLASS[1]="+$ALY_CLASS[1]"};$HOSEI[$key] = $HOSEI[$key]."�U$ALY_CLASS[1]&nbsp;";}
if($ALY_CLASS[2]){if($ALY_CLASS[2]<0){$ALY_CLASS[2]=int($ALY_CLASS[2]/2-0.5);}if($ALY_CLASS[2]>0){$ALY_CLASS[2]=int($ALY_CLASS[2]/2+0.5);$ALY_CLASS[2]="+$ALY_CLASS[2]"};$HOSEI[$key] = $HOSEI[$key]."�h$ALY_CLASS[2]&nbsp;";}
if($ALY_CLASS[3]){if($ALY_CLASS[3]>0){$ALY_CLASS[3]="+$ALY_CLASS[3]"};$HOSEI[$key] = $HOSEI[$key]."��$ALY_CLASS[3]&nbsp;";}
if($ALY_CLASS[4]){if($ALY_CLASS[4]>0){$ALY_CLASS[4]="+$ALY_CLASS[4]"};$HOSEI[$key] = $HOSEI[$key]."��$ALY_CLASS[4]&nbsp;";}
if($ALY_CLASS[17]){
	$tokuarray='';
	@tokuclass = split(/!/,$ALY_CLASS[17]);
	foreach $j(@tokuclass){$tokuarray .= $VCLTO_LIST{"$j"}."&nbsp";}
	$HOSEI[$key] .= "$tokuarray";
}
if(!$ALY_CLASS[1] && !$ALY_CLASS[2] && !$ALY_CLASS[3] && !$ALY_CLASS[4] && !$ALY_CLASS[17]){$HOSEI[$key] = '����'}

print << "-----END-----";
	<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr>
	<td style="background-color:$TABLE_COLOR2;padding:3px;"><b>$ALY_CLASS[0]</b></td>
	<td align="right" style="background-color:$TABLE_COLOR2;"></td></tr>
	<tr>
	<td width="300" colspan="2" style="padding:5px;">

	<table style="font-size:12px;">
		<tr><td><b>�N���X�`�F���W����</b></td><td rowspan="3"><img src="$IMG_FOLDER5/$ALY_CLASS[18]" style="border:none;width:64;height:64;" align="right"></td></tr>
		<tr><td style="padding-left:10px;">�A���C�������g�c$ALI[$key]</td></tr>
		<tr><td style="padding-left:10px;padding-top:10px;padding-bottom:10px;padding-top:10px;">$HOSEI[$key]</td></tr>
		<tr><td colspan="2">$ALY_CLASS[19]</td></tr>
	</table>

	</td>
	</tr></table>

	</td></tr></table>
-----END-----

		}
	}


	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub vamity{
	print <<"	-----END-----";
HTTP/1.1 200 OK
Content-Type: text/html

<script language="JavaScript"><!--
	document.write ('<html><head>');
	document.write ('<title>Tactics Ogre de Endless Battle 304 Edition Class Edit</title></head>');
	document.write ('<frameset rows="219,*" border="0" framespacing="0">');
	document.write ('<frame name="Main" frameborder="NO" src="$MAIN_SCRIPT?vamity1">');
	document.write ('<frame name="Sub" frameborder="NO" src="$MAIN_SCRIPT?vamity2">');
	document.write ('</frameset>');
	document.write ('</html>');
// --></script>
<noscript>JavaScript�Ή��u���E�U�ł��V�щ������B</noscript>
	-----END-----
}

sub vamity1{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	&HEADER;

	require "./$LOG_FOLDER/$CLASS_DATA";
	require "./$LOG_FOLDER/$HASH_DATA";
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT name="FM" method="POST" target=Sub>
	<script language="JavaScript">
		function Move(){parent.Sub.location.replace("$BACKFR");}
	</script>
		<input type=hidden name=cmd>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
	<table border=0 cellpadding=0 cellspacing=0 bgcolor="$TABLE_COLOR1" align=center style="border:3px solid $TABLE_BORDER;font-size:12px;">
	<tr>
		<td>name�c<input type=text size="15" name="pname" value="���@�i�E���["> code�c<input type=text size="20" name="pcode" value="�}�O�i�������B"></td>
		<td>name�c<input type=text size="15" name="vsname" value="�ؓ�"> code�c<input type=text size="20" name="vcode" value="��Ǐ�����"></td>
	</tr>
	<tr>
		<td>element�c<select name="pelement"><option value="0">��<option value="1">��<option value="2">��n<option value="3">��<option value="4">�_��<option value="5">�Í�</select> icon�c<input type=text size="2" name="icon1" value="703"></td>
		<td>element�c<select name="velement"><option value="0">��<option value="1">��<option value="2">��n<option value="3">��<option value="4">�_��<option value="5">�Í�</select> icon�c<input type=text size="2" name="icon2" value="759"></td>
	</tr>
	<tr><td>
	-----END-----

	print "class�c<select name=\"class1\">\n";
	foreach $Key (sort{$a <=> $b} keys %VCLASS_LIST){
		my@change = split(/\,/,$VCLASS_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n";
	}
	print "</select>\n";
	print "</td><td>\n";
	print "class�c<select name=\"class2\">\n";
	foreach $Key (sort{$a <=> $b} keys %VCLASS_LIST){
		my@change = split(/\,/,$VCLASS_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n";
	}
	print "</select>\n";
	print "</td></tr>\n";
	print "<tr><td>\n";
	print "weapon1�c<select name=\"weapon1\">\n";
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@change = split(/\,/,$WEAPON_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n" if $change[7] !~ m/!12|!13|!14|!15|!16|!17|!19|!1d|!1k/;
	}
	print "</select>\n";
	print "Lv<input type=text size=\"1\" name=\"lv0\" value=\"99\">\n";
	print "</td><td>\n";
	print "weapon1�c<select name=\"weapon2\">\n";
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@change = split(/\,/,$WEAPON_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n" if $change[7] !~ m/!12|!13|!14|!15|!16|!17|!19|!1d|!1k/;
	}
	print "</select>\n";
	print "Lv<input type=text size=\"1\" name=\"lv1\" value=\"99\">\n";
	print "</td></tr>\n";

	print "<tr><td>\n";
	print "weapon2�c<select name=\"sub_weapon1\">\n";
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@change = split(/\,/,$WEAPON_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n" if $change[7] =~ m/!12|!13|!14|!15|!16|!17|!19|!1c/;
	}
	print "</select>\n";
	print "Lv<input type=text size=\"1\" name=\"sub_lv1\" value=\"99\">\n";
	print "</td><td>\n";
	print "weapon2�c<select name=\"sub_weapon2\">\n";
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@change = split(/\,/,$WEAPON_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n" if $change[7] =~ m/!12|!13|!14|!15|!16|!17|!19|!1c/;
	}
	print "</select>\n";
	print "Lv<input type=text size=\"1\" name=\"sub_lv2\" value=\"99\">\n";
	print "</td></tr>\n";

	print "<tr><td>\n";
	print "weapon3�c<select name=\"sub_weapon3\">\n";
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@change = split(/\,/,$WEAPON_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n" if $change[7] =~ m/!12|!13|!14|!15|!16|!17|!19|!2q|!2r/;
	}
	print "</select>\n";
	print "Lv<input type=text size=\"1\" name=\"sub_lv3\" value=\"99\">\n";
	print "</td><td>\n";
	print "weapon3�c<select name=\"sub_weapon4\">\n";
	foreach $Key (sort{$a cmp $b} keys %WEAPON_LIST){
		my@change = split(/\,/,$WEAPON_LIST{$Key});
		print "<option value=\"$Key\">$change[0]\n" if $change[7] =~ m/!12|!13|!14|!15|!16|!17|!19|!2q|!2r/;
	}
	print "</select>\n";
	print "Lv<input type=text size=\"1\" name=\"sub_lv4\" value=\"99\">\n";
	print "</td></tr>\n";

	print << "	-----END-----";
	<tr>
		<td>���c<select name="pmode"><option value="1">�ʏ�U��<option value="2">�ˌ�<option value="3">�h��<option value="4">�q�b�g�A���h�A�E�F�C<option value="5">�_��<option value="6">�̂Đg<option value="7">���؂�<option value="8">�_�u���A�^�b�N</select></td>
		<td>���c<select name="vmode"><option value="1">�ʏ�U��<option value="2">�ˌ�<option value="3">�h��<option value="4">�q�b�g�A���h�A�E�F�C<option value="5">�_��<option value="6">�̂Đg<option value="7">���؂�<option value="8">�_�u���A�^�b�N</select></td>
	</tr>
	<tr>
		<td>STR�c<input type=text size="1" name="pstr" value="50"> VIT�c<input type=text size="1" name="pvit" value="50"> AGI�c<input type=text size="1" name="pagi" value="50"> DEX�c<input type=text size="1" name="pdex" value="50"></td>
		<td>STR�c<input type=text size="1" name="vstr" value="50"> VIT�c<input type=text size="1" name="vvit" value="50"> AGI�c<input type=text size="1" name="vagi" value="50"> DEX�c<input type=text size="1" name="vdex" value="50"></td>
	</tr>
	<tr>
		<td colspan="2" align="center"><input type=submit name="custom" value="change" onClick="document.FM.cmd.value='vamity3';Move()"></td>
	</tr>
	</form>
	</td></tr></table>
	</body>
	-----END-----
	print "<script language=\"JavaScript\">location.href='#top';\n</script>\n" if $BANNER_DISPLAY;

}
sub vamity2{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	&HEADER;


	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub vamity3{


	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	require './vabattle.pl';

	local($PL_WN) = "$FORM{'weapon1'}";
	local($PL_WLV) = "$FORM{'lv0'}"*100;
	local($PL_WB) = "$FORM{'sub_weapon1'}";
	local($PL_LVB) = "$FORM{'sub_lv1'}"*100;
	local($PL_WC) = "$FORM{'sub_weapon3'}";
	local($PL_LVC) = "$FORM{'sub_lv3'}"*100;
	local($VS_WN) = "$FORM{'weapon2'}";
	local($VS_WLV) = "$FORM{'lv1'}"*100;
	local($VS_WB) = "$FORM{'sub_weapon2'}";
	local($VS_LVB) = "$FORM{'sub_lv2'}"*100;
	local($VS_WC) = "$FORM{'sub_weapon4'}";
	local($VS_LVC) = "$FORM{'sub_lv4'}"*100;
	$PL_VALUES[4] = "$FORM{'class1'}";
	$VS_VALUES[4] = "$FORM{'class2'}";
	$PL_VALUES[27] = "$FORM{'icon1'}";
	$VS_VALUES[27] = "$FORM{'icon2'}";
	$PL_VALUES[15]=80000;
	$PL_VALUES[16]=80000;
	$PL_VALUES[17]=4000;
	$VS_VALUES[15]=80000;
	$VS_VALUES[16]=80000;
	$PL_VALUES[36]=0;
	$PL_VALUES[36]=0;
	$PL_VALUES[19] = "$FORM{'pstr'}";
	$PL_VALUES[20] = "$FORM{'pvit'}";
	$PL_VALUES[21] = "$FORM{'pagi'}";
	$PL_VALUES[22] = "$FORM{'pdex'}";
	$VS_VALUES[19] = "$FORM{'vstr'}";
	$VS_VALUES[20] = "$FORM{'vvit'}";
	$VS_VALUES[21] = "$FORM{'vagi'}";
	$VS_VALUES[22] = "$FORM{'vdex'}";
	$PL_VALUES[3] = "$FORM{'pcode'}";
	$VS_VALUES[3] = "$FORM{'vcode'}";
	$PL_VALUES[13] = '#FFFFFF';
	$VS_VALUES[13] = '#FFFFFF';
	$PL_VALUES[31] = "$FORM{'pelement'}";
	$VS_VALUES[31] = "$FORM{'velement'}";
	$FORM{'mode'} = $FORM{'pmode'};
	$VsMsnNo = $FORM{'vmode'};
	&vabattle2;

	&vabattle3;

	&vabattle3_1;

	&vabattle4;

	&vabattle4_1;

	&vabattle5;

	&vabattle5_1;

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

		$hpcolor="$IMG_FOLDER1/hp.gif";
		$dmgcolor="$IMG_FOLDER1/dmg.gif";
		$zencolor="$IMG_FOLDER1/zen.gif";

	if($MENTE==1){
		$hpcolor="$IMG_FOLDER1/hp1.gif";
		$dmgcolor="$IMG_FOLDER1/dmg1.gif";
		$zencolor="$IMG_FOLDER1/zen1.gif";
	}

	$Pl_BfrHP=$PL_VALUES[15];
	$Vs_AtPoint=$PL_VALUES[15] if $PL_VALUES[15] < $Vs_AtPoint;
	$Vs_BfrHP=$VS_VALUES[15];
	$Pl_AtPoint=$VS_VALUES[15] if $VS_VALUES[15] < $Pl_AtPoint;

	$PL_VALUES[15]=$PL_VALUES[15]-$Vs_AtPoint;
	$Pl_width_per=$PL_VALUES[16]/150;
	$Pl_width_hp=int($PL_VALUES[15]/$Pl_width_per);
	$Pl_width_zen=int(($PL_VALUES[16]-$Pl_BfrHP)/$Pl_width_per);
	$Pl_width_dmg=int($Vs_AtPoint/$Pl_width_per);
	$VS_VALUES[15]=$VS_VALUES[15]-$Pl_AtPoint;
	$Vs_width_per=$VS_VALUES[16]/150;
	$Vs_width_hp=int($VS_VALUES[15]/$Vs_width_per);
	$Vs_width_zen=int(($VS_VALUES[16]-$Vs_BfrHP)/$Vs_width_per);
	$Vs_width_dmg=int($Pl_AtPoint/$Vs_width_per);

	$PL_HPTAG="<img src=\"$hpcolor\" hspace=0 height=7 width=$Pl_width_hp>" if $Pl_width_hp;
	$PL_HPTAG.="<img src=\"$dmgcolor\" hspace=0 height=7 width=$Pl_width_dmg>" if $Pl_width_dmg;
	$PL_HPTAG.="<img src=\"$zencolor\" hspace=0 height=7 width=$Pl_width_zen>" if $Pl_width_zen;

	$VS_HPTAG="<img src=\"$hpcolor\" hspace=0 height=7 width=$Vs_width_hp>" if $Vs_width_hp;
	$VS_HPTAG.="<img src=\"$dmgcolor\" hspace=0 height=7 width=$Vs_width_dmg>" if $Vs_width_dmg;
	$VS_HPTAG.="<img src=\"$zencolor\" hspace=0 height=7 width=$Vs_width_zen>" if $Vs_width_zen;


	&vabattle6_1;

	&vabattle6_2;

	&MESSAGE('m','PL','VS') if $PL_message;
	&MESSAGE('m','VS','PL') if $VS_message;

	$STDN=20;
	if($VS_W[7] =~ m/!6u/){$STDN+=$vwl;}

	if ($PLURAMI){print "<font color=#4aa1af>$PL_VALUES[3]�����݂̈ꌂ�I$VS_VALUES[3]�𓹘A��ɂ����I�I</font><br>\n";}
	if ($PLCONFORM){print "<font color=#ff4d4d>�A�V�F�����I�I����̃G�������g���g�p�҂̃G�������g�Ɏʂ����I�I</font><br>\n";}
	if ($PLTRANS){
		print "<font color=#ff4d4d>�g�����X�t�@�[�I</font><br>\n";
		require "boserifu.data";
		my$sl=@teniseki;
		my$sw=@teniseki[int(rand($sl))];			
		print "$FORM{'pname'}$sw<br>\n";
	}
	if ($VSMIGAWARI){
		print "<font color=#ffffbb>���o�C�o���I�I���𗎂Ƃ����҂̍��𑦍��ɌĂі߂��E�E�E</font><br>\n";
	}

	$hatustd=0;
	if ($PL_VALUES[29] > 102 && $VS_VALUES[15] > 0 && $PL_W[7] !~ m/!4b/ && $PL_sB[7] !~ m/!4b/ && $PL_sC[7] !~ m/!4b/){
		if($VS_W[7] =~ m/!22/ && $PL_VALUES[19] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>�I�I�G����$STATUS_NAME[0]�_�E���U���I�I<br>$PL_VALUES[3]�͍U���͒ቺ</font><br>\n";
			$PL_VALUES[19]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[67]++;}$R_VALUES[126]++;
		}
		if($VS_W[7] =~ m/!23/ && $PL_VALUES[20] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>�I�I�G����$STATUS_NAME[1]�_�E���U���I�I<br>$PL_VALUES[3]�͖h��͒ቺ</font><br>\n";
			$PL_VALUES[20]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[68]++;}$R_VALUES[127]++;
		}
		if($VS_W[7] =~ m/!24/ && $PL_VALUES[21] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>�I�I�G����$STATUS_NAME[2]�_�E���U���I�I<br>$PL_VALUES[3]�͉��͒ቺ</font><br>\n";
			$PL_VALUES[21]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[69]++;}$R_VALUES[128]++;
		}
		if($VS_W[7] =~ m/!25/ && $PL_VALUES[22] > 44){
			if(rand(255) < $STDN){print "<font color=#8000ff>�I�I�G����$STATUS_NAME[3]�_�E���U���I�I<br>$PL_VALUES[3]�͖����͒ቺ</font><br>\n";
			$PL_VALUES[22]--;$PL_VALUES[29]=$PL_VALUES[29]-3;$hatustd=1;$R_VALUES[70]++;}$R_VALUES[129]++;
		}
	}

	if ($PL_VALUES[29] > 102 && $VS_W[7] =~ m/!2j/ && $PL_VALUES[16]==80000){
		if(rand(100) > 98){print "<font color=#8000ff>�I�I�G����HP�_�E���U���I�I<br>$PL_VALUES[3]�͍ő�HP�ቺ</font><br>\n";
		$PL_VALUES[16]=int($PL_VALUES[16]*0.99);$PL_VALUES[29]=$PL_VALUES[29]-3;$PL_VALUES[30]=int($PL_VALUES[30]/2);$R_VALUES[130]++;
		}$R_VALUES[131]++;
	}
	if($hatustd == 1){print "<font color=#8000ff>���x���ቺ</font><br>\n";
		$PL_VALUES[30]=int($PL_VALUES[30]/3);
		if($PL_VALUES[29] < 100){$PL_VALUES[29]=100;}
	}

	&vabattle7;

	print "</td></tr></table>\n</body>\n</html>\n";

}
sub result{
	print <<"	-----END-----";
HTTP/1.1 200 OK
Content-Type: text/html

<script language="JavaScript"><!--
	document.write ('<html><head>');
	document.write ('<title>Tactics Ogre de Endless Battle 304 Edition Class Edit</title></head>');
	document.write ('<frameset rows="50,*" border="0" framespacing="0">');
	document.write ('<frame name="Main" frameborder="NO" src="$MAIN_SCRIPT?result1">');
	document.write ('<frame name="Sub" frameborder="NO" src="$MAIN_SCRIPT?result2">');
	document.write ('</frameset>');
	document.write ('</html>');
// --></script>
<noscript>JavaScript�Ή��u���E�U�ł��V�щ������B</noscript>
	-----END-----
}

sub result1{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;

	&HEADER;
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	-----END-----

	require "./$LOG_FOLDER/$CLASS_DATA";
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT name="FM" method="POST" target=Sub>
	<script language="JavaScript">
		function Move(){parent.Sub.location.replace("$BACKFR");}
	</script>
	
		<input type=hidden name=cmd>
		<input type=hidden name=pname value=$FORM{'pname'}>
		<input type=hidden name=pass value=$FORM{'pass'}>
		<input type=text size="7" name="kea" value="50">
	<input type=submit name="custom" value="change" onClick="document.FM.cmd.value='result2';Move()">
	</form>
	</td></tr></table>
	</body>
	-----END-----
	print "<script language=\"JavaScript\">location.href='#top';\n</script>\n" if $BANNER_DISPLAY;

}

sub result2{
	@pair = split(/\;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/\,/, $DUMMY{'EB'});
		foreach (@pairs) {my($key, $value) = split(/\:/, $_);$COOKIE{"$key"} = $value;}
	&DBM_INPORT(P);&DBM_INPORT(C);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});

	&ERROR('���[�߂��I') if $COOKIE{'pass'} ne $MASTERPASS;
	require "./$LOG_FOLDER/$HASH_DATA";

	&HEADER;
	foreach $key (0..$FORM{'kea'}){
		my@al=keys %WEAPON_LIST;$alw=@al;
		$alw=int rand($alw);$gw=@al[$alw];$gw='a' if !$gw;
		@q=split(/\,/,$WEAPON_LIST{"$gw"});
		if ($q[8] > rand(100)){
			if($q[8] < 1){
				$text .= "$key : <b><font color=\"#f7e957\">$q[0]</font></b><br>\n";
			}elsif($q[8] < 26){
				$text .= "$key : <b><font color=\"#f88888\">$q[0]</font></b><br>\n";
			}else{
				$text .= "$key : $q[0]<br>\n";
			}
			$kakutoku++;
		}
		$sikou++;
	}
	$kakuritu=sprintf("%.5f",$kakutoku/$sikou)*100;
	print "<table border=0 cellpadding=5 cellspacing=0 bgcolor=\"$TABLE_COLOR1\" align=center style=\"border:3px solid $TABLE_BORDER;\">\n";
	print "<tr><td>\n";
	print "���s��:$FORM{'kea'} ����l����:$kakuritu%\n";
	print "</td></tr>\n";
	print "<tr><td>\n";
	print "$text\n";
	print "</td></tr></table>\n";
	&FOOTER;
	print "</td></tr></table></form></body>";
}
1;

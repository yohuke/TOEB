$MHOST[0] = '';
$addr = $ENV{'REMOTE_ADDR'};
$host = $ENV{'REMOTE_HOST'};
if (($host eq $addr) || ($host eq '')) {$host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;}
my $MFLAG=0;
  foreach (@MHOST) {
    $_ =~ s#\~#.*#g;
    if ($host =~ m#$_#i || $addr =~ m#$_#i) {$MFLAG=1;}
  }
unless ($MFLAG) {&ERROR('管理モードへのアクセスは禁止です。');
}

if ( !open(DB,"$pass") ) { &ERROR('ファイルが開けませんでした。'); }
@lines = <DB>;
close(DB);
$password = shift(@lines);
chop($password) if ($password =~ /\n$/);
($header, $password) = split(/:/, $password);
if ($password =~ /^\$1\$/) {
  $salt = 3;
} else {
  $salt = 0;
}
if ($header ne 'crypt_password' || $password eq '') {
  $start = 1;
  &PASSWORD;
}

if ($FORM{'papost'} eq 'pcode') {
  &PASSWORD;
}elsif($FORM{'admin'} eq 'change' && crypt($FORM{'pwd'}, substr($password,$salt,2)) eq $password) {
  &PASSWORD;
}elsif($FORM{'admin'} eq 'main' && crypt($FORM{'pwd'}, substr($password,$salt,2)) eq $password) {
  &MAINTENANCE2;
}
sub PASSWORD {
  $psold = $FORM{'password_old'};
  $pas1 = $FORM{'password'};
  $pas2 = $FORM{'password2'};

  &HEADER;

  if ($start == 1 && $pas1 eq '') {
    print "管理者パスワードをこのページで設定\します。<P>\n";
  } elsif ($pas1 =~ /\W/) {
    print "<FONT COLOR=red>新パスワードに英数字以外の文字が含まれています。</FONT><P>\n";
  } elsif ( $pas1 ne '' && $pas1 ne $pas2 ){
    print "<FONT COLOR=red>確認のために入力された新パスワードが一致しません。</FONT><P>\n";
  } elsif ( $start != 1 && $psold eq '' ) {
    print "<FONT COLOR=red>旧パスワードも入力して下さい。</FONT><P>\n";
  } elsif ( $start != 1 && (crypt($psold, substr($password, $salt, 2) ) ne $password) ){
    print "<FONT COLOR=red>旧パスワードが認証されませんでした。</FONT><P>\n";
  } else {
    $now = time;
    ($p1, $p2) = unpack("C2", $now);
    $wk = $now / (60 * 60 * 24 * 7) + $p1 + $p2 - 8;
    @saltset = ('a'..'z', 'A'..'Z', '0'..'9', '.', '/');
    $nsalt = $saltset[$wk % 64] . $saltset[$now % 64];
    $pwd = crypt($FORM{'password'}, $nsalt);

    if ( !open(DB,">$pass") ) { &ERROR('ファイルが開けませんでした。'); }
    print DB "crypt_password:$pwd\n";
    close(DB);
    print "<FONT COLOR=blue SIZE=+3>管理者パスワードが設定\されました。<BR><A HREF=\"$MAIN_SCRIPT?MAINTE\">[ＮＥＸＴ]</A>をクリックして下さい。</FONT><P>再度変更する場合は下記フォームで再入力しなおして下さい。<P>\n";
  }
  print "<FORM method=\"POST\" action=\"$MAIN_SCRIPT\"><input type=hidden name=\"cmd\" value=\"MAINTE\">\n";
  print "<INPUT type=\"hidden\" name=\"papost\" value=\"pcode\">\n";
  if ($start != 1) {
    print "旧パスワード <INPUT type=\"password\" name=\"password_old\" size=\"8\" maxlength=\"8\"><BR>\n";
  }
  print <<"_HTML_";
新パスワード <INPUT type="password" name="password" size="8" maxlength="8">（半角英数８文字以内）<BR>
新パスワード <INPUT type="password" name="password2" size="8" maxlength="8">（確認のため上と同じパスをもう一度）<P>
<INPUT type="submit" value="     登録     ">
</FORM><P>
</BODY>
</HTML>
_HTML_
  exit;
}

sub MAINTENANCE{
	@tm=times(); $cpu=$tm[0]+$tm[1];
	$syori=int($cpu*1000)/1000;

	&HEADER;
	print << "	-----END-----";
	<table width=100% height=100%><tr><td align=center>
		<table border=0 cellpadding=0 cellspacing=0 align=center
		 style="border:1px outset #909090;font-size:16px;">
		<form action="$MAIN_SCRIPT" method="POST"><input type=hidden name="cmd" value="MAINTE">
		<tr><td style="background-color:#404040;" colspan=2>
		&nbsp;Maintenance Mode ～ $syori s</td></tr>
		<tr><td bgcolor=#909090 align=center><b style="color:#000000;">管理者モード：
		<SELECT NAME="admin">
		<OPTION value="main">メンテナンス
		<OPTION value="change">パスワード変更</SELECT></b></td>
		<td bgcolor=#909090><b style="color:#000000;">管理者パスワード</b>
		<input type="password" name="pwd" style="height:21px; color:#ffffff; font-size:16px; background:#000000; border:1 inset #c0c0c0;">
		<input type="submit" value=Login>
		</td></tr></form></table>
	<form action="$MAIN_SCRIPT" method="POST">
	<input type="submit" value="戻る">
	</form>
	</td></tr></table>
		
	-----END-----
}
sub MAINTENANCE2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	&HEADER;
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT method=POST name=mainte>
	<input type=hidden name="cmd"><input type=hidden name="pwd" value="$FORM{'pwd'}">
	<table width=100% height=100%><tr><td align=center>

	<table class=font9 cellspacing=2 cellpadding=3 bgcolor="#909090">
		<tr><td bgcolor=#404040 colspan=3><b>メンテナンス</b></td></tr>
		<tr><td bgcolor=#404040 align=center>ログイン履歴</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">過去200件のログイン履歴を表\示します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" $STYLE_B2 onClick="mainte.cmd.value='LGIN_RIREKI'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>クッキー期限</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">参加者の削除期限を表\示</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='COOKIES'"></td>
		</tr>
		<tr><td valign=top colspan=3 style="line-height:0px;">&nbsp;</td></tr>
		<tr><td bgcolor=#404040 align=center>破損PLデータ抽出</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">破損しているプレイヤーデータの一覧を抽出・修正します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" $STYLE_B2 onClick="mainte.cmd.value='XPL_LIST';"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>破損COデータ抽出</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">破損している国データの一覧を抽出・修正します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" $STYLE_B2 onClick="mainte.cmd.value='XCO_LIST';"></td>
		</tr>
		<tr><td valign=top colspan=3 style="line-height:0px;">&nbsp;</td></tr>
		<tr><td bgcolor=#404040 align=center>PLパラメータ</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">参加者のパラメータを調整します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='MASTER'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>PLデータ削除</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">プレイヤーデータを削除します。<br>不正や荒らし対策時にのみ使用してください。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" $STYLE_B2 onClick="mainte.cmd.value='PL_DEL';"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>国パラメータ</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">各国のデータを調整します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='COUNTRY'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>国データ削除</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">国を削除します。<br>不正や荒らし対策時にのみ使用してください。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" $STYLE_B2 onClick="mainte.cmd.value='CO_DEL';"></td>
		</tr>
		<tr><td valign=top colspan=3 style="line-height:0px;">&nbsp;</td></tr>
		<tr><td bgcolor=#404040 align=center>PLデータ出力</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">手動でPLデータのバックアップを取ります。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='BACKUP'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>PLデータ復元</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">自動バックアップからPLデータを復元します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='DATAUP'"></td>
		</tr>
		<tr><td valign=top colspan=3 style="line-height:0px;">&nbsp;</td></tr>
		<tr><td bgcolor=#404040 align=center>DBM→PL_DATE分離</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">DBMからPLデータを分離展開します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='PUSHHITO'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>PL_DATE→DBM復元</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">分離展開したPLデータをDBMに復元します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='OPENHITO'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>DBM→CO_DATE分離</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">DBMからCOデータを分離展開します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='PUSHKUNI'"></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>CO_DATE→DBM復元</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">分離展開したCOデータをDBMに復元します。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" onClick="mainte.cmd.value='OPENKUNI'"></td>
		</tr>
		<tr><td valign=top colspan=3 style="line-height:0px;">&nbsp;</td></tr>
		<tr><td bgcolor=#404040 align=center>歴史編纂</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">歴史データを書き換えます。</td>
			<td style="border:1px solid #404040;"><input type=submit value="GO" $STYLE_B2 onClick="mainte.cmd.value='HISTORY_EDIT';"></td>
		</tr>
		<tr><td valign=top colspan=3 style="line-height:0px;">&nbsp;</td></tr>
		<tr><td bgcolor=#404040 align=center>武器データ</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">武器リストを表\示します</td>
			<td style="border:1px solid #404040;"><a href="$MAIN_SCRIPT?bukilist" target=_blank>表\示</a></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>クラスデータ</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">クラスリストを表\示します</td>
			<td style="border:1px solid #404040;"><a href="$MAIN_SCRIPT?classlist" target=_blank>表\示</a></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>ダメージ計算</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">ダメージ計算を表\示します</td>
			<td style="border:1px solid #404040;"><a href="$MAIN_SCRIPT?vamity" target=_blank>表\示</a></td>
		</tr>
		<tr><td bgcolor=#404040 align=center>武器入手</td>
			<td style="border:1px solid #404040;font-size:12px;color:#000000;">戦闘回数における入手武器</td>
			<td style="border:1px solid #404040;"><a href="$MAIN_SCRIPT?result" target=_blank>表\示</a></td>
		</tr>

	</table></form>
	<form action=$MAIN_SCRIPT method=POST>
	<input type=submit value=戻る>
	</form>
	</td></tr></table>

	-----END-----
  exit;
}

sub LGIN_RIREKI2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	&HEADER;
	&DBM_INPORT(L);

	print << "	-----END-----";
	<table width=100% height=100%><tr><td align=center>
	<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;">
		<tr><td bgcolor=#404040 colspan=8><b>メンテナンス－最終ログイン履歴</b></td></tr>
		
	-----END-----

	foreach $t(sort {$b <=> $a} keys %L){$lc++;
		if ($lc <= 150){
			@lgn=split(/!/,$L{"$t"});
			print "<tr style=\"color:#000000;\"><td nowrap>$lc</td><td nowrap>".&DATE_DECORD($t);
			print "</td><td nowrap>$lgn[0]</td><td nowrap>$lgn[1]</td><td nowrap>$lgn[2]</td><td nowrap>$lgn[3]</td><td nowrap>$lgn[4]</td><td nowrap>$lgn[5]</td>";
		}
	}
	print << "	-----END-----";
	<form action="$MAIN_SCRIPT" method="POST">
	<input type=hidden name="cmd" value="MAINTE">
	<input type=hidden name="admin" value="main">
	<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=6>
	<input type=submit value=戻る>
	</td></tr></table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub XPL_LIST2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	&HEADER;
	&DBM_INPORT(P);
print << "-----END-----";
	<script language="JavaScript">
		function syusei(nm){
			fm1.plname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=SYUSEI>
	<input type=hidden name="plname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
	</form>
	<table width=100% height=100%><tr><td align=center>
	<table class=font9 cellspacing=3 cellpadding=3 bgcolor="#909090">
		<tr><td bgcolor=#404040 colspan=3><b>メンテナンス－PLエラーデータ抽出・修正</b></td></tr>
-----END-----
	while (my($key,$val) = each %P){
		@VALS = split(/\s/,$val);$ER='';
		$ER.= "&nbsp;[Unit name]" if $key eq '';
		$ER.= "&nbsp;[MSType Undefined]" if $VALS[4] eq '';
		$ER.= "&nbsp;[Weapon Undefined]" if $VALS[9] eq '';
		$ER.= "&nbsp;[Character Undefined]" if $VALS[12] eq '';
		$ER.= "&nbsp;[Color Undefined]" if $VALS[13] eq '';
		$ER.= "&nbsp;[HP Undefined]" if $VALS[16] eq '';
		$ER.= "&nbsp;[EN Undefined]" if $VALS[18] eq '';
		$ER.= "&nbsp;[AT Undefined]" if $VALS[19] eq '';
		$ER.= "&nbsp;[AT Incorrect]" if $VALS[19] > 50 || $VALS[19] < 0;
		$ER.= "&nbsp;[GD Undefined]" if $VALS[20] eq '';
		$ER.= "&nbsp;[GD Incorrect]" if $VALS[20] > 50 || $VALS[20] < 0;
		$ER.= "&nbsp;[SP Undefined]" if $VALS[21] eq '';
		$ER.= "&nbsp;[SP Incorrect]" if $VALS[21] > 50 || $VALS[21] < 0;
		$ER.= "&nbsp;[HIT Undefined]" if $VALS[22] eq '';
		$ER.= "&nbsp;[HIT Incorrect]" if $VALS[22] > 50 || $VALS[22] < 0;
		$ER.= "&nbsp;[EXP Incorrect]" if $VALS[30] < 0;
		$ER.= "&nbsp;[ELE Incorrect]" if $VALS[31] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[32] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[33] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[34] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[35] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[36] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[37] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[38] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[39] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[40] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[41] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[42] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[43] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[44] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[45] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[46] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[47] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[48] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[49] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[50] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[51] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[52] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[53] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[54] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[55] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[56] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[57] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[58] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[59] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[60] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[61] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[62] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[63] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[64] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[65] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[66] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[67] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[68] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[69] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[70] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[71] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[72] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[73] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[74] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[75] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[76] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[77] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[78] < 0;
		$ER.= "&nbsp;[CON Incorrect]" if $VALS[79] < 0;
		if ($ER){$c++;$c = sprintf("%03d", $c);
			print "<tr><td nowrap>$c <b>$key</b></td><td nowrap>$ER</td><td><a href=\"javascript:syusei('$key')\">修正</a></td></tr>";
		}
	}
print "<tr><td colspan=3><br><br>エラーデータはありませんでした。<br><br></td></tr>" if !$c;
print "<tr><td colspan=3 style=\"font-size:12px;color:#000000;\">未定義（Undefined）の項目や<br>不正確（Incorrect）な数値のある項目の一覧です。<br>修正の文字をクリックで自動修正できます。
	<form action=$MAIN_SCRIPT method=POST>
	<input type=hidden name=\"cmd\" value=\"MAINTE\">
	<input type=hidden name=\"admin\" value=\"main\">
	<input type=hidden name=\"pwd\" value=\"$FORM{'pwd'}\">
	<input type=submit value=戻る>
	</form>
</td></tr></table>";
	&FOOTER;
	print "</td></tr></table></body>";

}

sub SYUSEI2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%P,"$DBM_P",0666);
		@VALS = split(/\s/,$P{"$FORM{'plname'}"});
		$VALS[4]='0' if $VALS[4] eq '';
		$VALS[9]='a' if $VALS[9] eq '';
		$VALS[12]='0'  if $VALS[12] eq '';
		$VALS[13]='ffffff'  if $VALS[13] eq '';
		$VALS[16]='5000'  if $VALS[16] eq '';
		$VALS[18]='200'  if $VALS[18] eq '';
		$VALS[19]='5' if $VALS[19] eq '';$VALS[19]='50' if $VALS[19] > 50;$VALS[19]='0' if $VALS[19] < 0;
		$VALS[20]='5' if $VALS[20] eq '';$VALS[20]='50' if $VALS[20] > 50;$VALS[20]='0' if $VALS[20] < 0;
		$VALS[21]='5' if $VALS[21] eq '';$VALS[21]='50' if $VALS[21] > 50;$VALS[21]='0' if $VALS[21] < 0;
		$VALS[22]='5' if $VALS[22] eq '';$VALS[22]='50' if $VALS[22] > 50;$VALS[22]='0' if $VALS[22] < 0;
		$VALS[30]='0'  if $VALS[30] < 0;
		$VALS[31]='0'  if $VALS[31] < 0;
		$VALS[32]='0'  if $VALS[32] < 0;
		$VALS[33]='0'  if $VALS[33] < 0;
		$VALS[34]='0'  if $VALS[34] < 0;
		$VALS[35]='0'  if $VALS[35] < 0;
		$VALS[36]='0'  if $VALS[36] < 0;
		$VALS[37]='0'  if $VALS[37] < 0;
		$VALS[38]='0'  if $VALS[38] < 0;
		$VALS[39]='0'  if $VALS[39] < 0;
		$VALS[40]='0'  if $VALS[40] < 0;
		$VALS[41]='0'  if $VALS[41] < 0;
		$VALS[42]='0'  if $VALS[42] < 0;
		$VALS[43]='0'  if $VALS[43] < 0;
		$VALS[44]='0'  if $VALS[44] < 0;
		$VALS[45]='0'  if $VALS[45] < 0;
		$VALS[46]='0'  if $VALS[46] < 0;
		$VALS[47]='0'  if $VALS[47] < 0;
		$VALS[48]='0'  if $VALS[48] < 0;
		$VALS[49]='0'  if $VALS[49] < 0;
		$VALS[50]='0'  if $VALS[50] < 0;
		$VALS[51]='0'  if $VALS[51] < 0;
		$VALS[52]='0'  if $VALS[52] < 0;
		$VALS[53]='0'  if $VALS[53] < 0;
		$VALS[54]='0'  if $VALS[54] < 0;
		$VALS[55]='0'  if $VALS[55] < 0;
		$VALS[56]='0'  if $VALS[56] < 0;
		$VALS[57]='0'  if $VALS[57] < 0;
		$VALS[58]='0'  if $VALS[58] < 0;
		$VALS[59]='0'  if $VALS[59] < 0;
		$VALS[60]='0'  if $VALS[60] < 0;
		$VALS[61]='0'  if $VALS[61] < 0;
		$VALS[62]='0'  if $VALS[62] < 0;
		$VALS[63]='0'  if $VALS[63] < 0;
		$VALS[64]='0'  if $VALS[64] < 0;
		$VALS[65]='0'  if $VALS[65] < 0;
		$VALS[66]='0'  if $VALS[66] < 0;
		$VALS[67]='0'  if $VALS[67] < 0;
		$VALS[68]='0'  if $VALS[68] < 0;
		$VALS[69]='0'  if $VALS[69] < 0;
		$VALS[70]='0'  if $VALS[70] < 0;
		$VALS[71]='0'  if $VALS[71] < 0;
		$VALS[72]='0'  if $VALS[72] < 0;
		$VALS[73]='0'  if $VALS[73] < 0;
		$VALS[74]='0'  if $VALS[74] < 0;
		$VALS[75]='0'  if $VALS[75] < 0;
		$VALS[76]='0'  if $VALS[76] < 0;
		$VALS[77]='0'  if $VALS[77] < 0;
		$VALS[78]='0'  if $VALS[78] < 0;
		$VALS[79]='0'  if $VALS[79] < 0;

		$P{"$FORM{'plname'}"}="@VALS";
	dbmclose %P;
}
sub XCO_LIST2 {
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	&HEADER;
	&DBM_INPORT(C);
print << "-----END-----";
	<script language="JavaScript">
		function syusei(nm){
			fm1.coname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=CNSYUSEI>
	<input type=hidden name="coname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
	</form>
	<table width=100% height=100%><tr><td align=center>
	<table class=font9 cellspacing=3 cellpadding=3 bgcolor="#909090">
		<tr><td bgcolor=#404040 colspan=3><b>メンテナンス－国エラーデータ抽出・修正</b></td></tr>
-----END-----
	while (my($key,$val) = each %C){
		@VALS = split(/\s/,$val);$ER='';
		$ER.= "&nbsp;[Color Undefined]" if $VALS[0] eq '';
		$ER.= "&nbsp;[Money Undefined]" if $VALS[1] eq '';
		$ER.= "&nbsp;[YOUSAI DATA Undefined]" if $VALS[11] eq '' || $VALS[12] eq '';
		if ($ER){$c++;$c = sprintf("%03d", $c);
			print "<tr><td nowrap>$c <b>$key</b></td><td nowrap>$ER</td><td><a href=\"javascript:syusei('$key')\">修正</a></td></tr>";
		}
	}
print "<tr><td colspan=3><br><br>エラーデータはありませんでした。<br><br></td></tr>" if !$c;
print "<tr><td colspan=3 style=\"font-size:12px;color:#000000;\">未定義（Undefined）の項目や<br>不正確（Incorrect）な数値のある項目の一覧です。<br>修正の文字をクリックで自動修正できます。	
	<form action=$MAIN_SCRIPT method=POST>
	<input type=hidden name=\"cmd\" value=\"MAINTE\">
	<input type=hidden name=\"admin\" value=\"main\">
	<input type=hidden name=\"pwd\" value=\"$FORM{'pwd'}\">
	<input type=submit value=戻る>
	</form></td></tr></table>";
	&FOOTER;
	print "</td></tr></table></body>";


}
sub CNSYUSEI2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

		dbmopen (%C,"$DBM_C",0666);
		@VALS = split(/\s/,$C{"$FORM{'coname'}"});
		$VALS[0]='ffffff' if $VALS[0] eq '';
		$VALS[1]='0' if $VALS[1] eq '';
		$VALS[11]="$YOUSAI_HP!$YOUSAI_HP!$DATE"  if $VALS[11] eq '';
		$VALS[12]="1!1!1!$FORM{'coname'}防衛要塞"  if $VALS[12] eq '';
		$C{"$FORM{'coname'}"}="@VALS";
	dbmclose %C;
}

sub HISTORY_EDIT2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	$c=0;
	&HEADER;
print << "-----END-----";
	<script language="JavaScript">
		function syusei(nm,his){
		com=prompt('歴史の変更（半角記号不可）',his);
		if(com != null){
			if (com.length > 300){alert('150文字までです。（'+com.length+'文字）');return false;}
			fm1.hiskey.value=nm;
			fm1.hisval.value=com;
			fm1.sbm1.click();
		}
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=HISTORY_EDIT2>
	<input type=hidden name="hiskey">
	<input type=hidden name="hisval">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
	</form>
	<table width=100% height=100%><tr><td align=center>
	<table class=font9 cellspacing=3 cellpadding=3 bgcolor="#909090">
		<tr><td bgcolor=#404040 colspan=3><b>メンテナンス－歴史データ編纂</b></td></tr>
-----END-----
	dbmopen (%H,"$DBM_H",0666);
		foreach $Key (sort {$b <=> $a} keys %H){$c++;
			print "<tr><td style=\"color:#000000;\"><b>".&DATE_DECORD($Key)."</b></td><td>$H{$Key}</td><td><a href=\"javascript:syusei('$Key','$H{$Key}')\">修正</a></td></tr>\n";
		}
	dbmclose %H;
print << "-----END-----";
	<form action="$MAIN_SCRIPT" method="POST">
	<input type=hidden name="cmd" value="MAINTE">
	<input type=hidden name="admin" value="main">
	<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=3>
	<input type=submit value=戻る>
	</td></tr></form></table>

-----END-----
	&FOOTER;
	print "</td></tr></table></body>";
}
sub HISTORY_EDIT3{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%H,"$DBM_H",0666);
		$H{"$FORM{'hiskey'}"}="$FORM{'hisval'}";
	dbmclose %H;
}
sub PL_DEL2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	&HEADER;
	print << "	-----END-----";
	<script language="JavaScript">
		function checkRiyou (){
			if(document.del.pwd.value == '') {window.alert("PASSが未入力です。");return false 
			}else {if (confirm('登録を抹消します。\\n復元できませんがよろしいですか？') == true){return true;}else{return false}	}
	</script>
		<table width=100% height=100%><tr><td align=center>
		<table bgcolor="#909090" border=0 style="font-size:12px;">
			<tr><td colspan=2 bgcolor=#646464 align=center><img src=\"$IMG_FOLDER1/w.gif\"></td></tr>
			<tr><td colspan=2 style="color:#000000;">プレイヤー登録データを個別削除します。<br>
			削除したデータは復元する事が出来ません。<br><br></td></tr>
			<tr><td align=right style="height:21px; color:#ffffff; font-size:16px;">削除対象パイロットネーム<br>
					管理用パスワード</td>
				<td style="height:21px; color:#ffffff; font-size:16px;">
					<form action=$MAIN_SCRIPT method=POST target=_top name=del onSubmit="return checkRiyou()">
					<input type=hidden name=cmd value=PL_DEL2>
					<input type=text size=20 name=pname $STYLE_L><br>
					<input type=password size=15 name=pwd $STYLE_L>
					</td></tr>
			<tr><td colspan=3 align=center>
				<input type=submit value=\"削除\"></div></form>
	<form action="$MAIN_SCRIPT" method="POST">
	<input type=hidden name="cmd" value="MAINTE">
	<input type=hidden name="admin" value="main">
	<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=3>
	<input type=submit value=戻る>
	</td></tr>
			
		</table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";
	&LOCK;
		@LL=();
		dbmopen (%LLL,"$DBM_L",0666);
			foreach $t (keys %LLL){$LL{"$t"}=$LLL{"$t"};	}
		dbmclose %LLL;
		@PP=();
		dbmopen (%PPP,"$DBM_P",0666);
			foreach $t (keys %PPP){$PP{"$t"}=$PPP{"$t"};	}
		dbmclose %PPP;

	use File::Copy;
	move("$DBM_P.dir", "$DBM_P.old");
	move("$DBM_L.dir", "$DBM_L.old");
	move("$DBM_P.pag", "$DBM_P.bac");
	move("$DBM_L.pag", "$DBM_L.bac");

		dbmopen (%LLL,"$DBM_L",0666);
			foreach $t (keys %LL){$LLL{"$t"}=$LL{"$t"};	}
		dbmclose %LLL;
		dbmopen (%PPP,"$DBM_P",0666);
			foreach $t (keys %PP){$PPP{"$t"}=$PP{"$t"};	}
		dbmclose %PPP;
	&UNLOCK;
}
sub PL_DEL3{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%P,"$DBM_P",0666);
		delete $P{"$FORM{'pname'}"};
	dbmclose %P;
}

sub CO_DEL2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	&HEADER;
	print << "	-----END-----";
	<script language="JavaScript">
		function checkRiyouc (){
			if (document.del.cname.value == '') {window.alert("IDが未入力です。");return false 
			}else if(document.del.pwd.value == '') {window.alert("PASSが未入力です。");return false 
			}else {if (confirm('登録を抹消します。\\n復元できませんがよろしいですか？') == true){return true;}else{return false}	}	
		}
	</script>
		<table width=100% height=100%><tr><td align=center>
		<table bgcolor="#909090" border=0 style="font-size:12px;">
			<tr><td colspan=2 bgcolor=#646464 align=center><img src=\"$IMG_FOLDER1/w.gif\"></td></tr>
			<tr><td colspan=2 style="color:#000000;">国登録データを個別削除します。<br>
			削除したデータは復元する事が出来ません。<br><br></td></tr>
			<tr><td align=right style="height:21px; color:#ffffff; font-size:16px;">削除対象国名<br>
					管理用パスワード</td>
				<td style="height:21px; color:#ffffff; font-size:16px;">
					<form action=$MAIN_SCRIPT method=POST target=_top name=del onSubmit="return checkRiyouc()">
					<input type=hidden name=cmd value=CO_DEL2>
					<input type=text size=20 name=cname $STYLE_L><br>
					<input type=password size=15 name=pwd $STYLE_L>
					</td></tr>
			<tr><td colspan=3 align=center>
	<input type=submit value=\"削除\"></div></form>
	<form action="$MAIN_SCRIPT" method="POST">
	<input type=hidden name="cmd" value="MAINTE">
	<input type=hidden name="admin" value="main">
	<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=3>
	<input type=submit value=戻る>
	</td></tr>
			
		</table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";

}
sub CO_DEL3{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%C,"$DBM_C",0666);
	delete $C{"$FORM{'cname'}"};
	dbmclose %C;
}
sub MASTER2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(P);
print << "-----END-----";
	<script language="JavaScript">
		function syusei(nm){
			fm1.plname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=SYUSEI3>
	<input type=hidden name="plname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
        </form>
<table width=100% height=100%><tr><td align=left>
《検索機能\:<a href="http://www12.big.or.jp/~kazu777/">kazu777</a>》
<form onSubmit="return seek_str(this.strings.value);">
検索文字を入力してください。
<input name=strings type=text size=15 onChange="n = 0;">
<input type=submit value="検索">
</form>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040 colspan=79><b>メンテナンス－パラメータ\表\示－プレイヤー選択</b></td></tr>
<tr><td>選択</td><td>NO.</td><td>$c</td><td>ユニット[key]</td><td>階級データ[0]</td><td>戦歴[1]</td><td>PASS[2]</td><td>コード[3]</td><td>クラス[4]</td><td>所属国[5]</td><td>国内ランク[6]</td><td>コメント[7]</td><td>資金[8]</td><td>武器[9]</td><td>\予\備1[10]</td><td>\予\備2[11]</td><td>ALI[12]</td><td>色[13]</td><td>RISK[14]</td><td>HP[15]</td><td>MAXHP[16]</td><td>MP[17]</td><td>MP[18]</td><td>STR[19]</td><td>VIT[20]</td><td>AGI[21]</td><td>DEX[22]</td><td>改造回数[23]</td><td>熟練[24]</td><td>修理状態[25]</td><td>時間[26]</td><td>画像[27]</td><td>部隊[28]</td><td>LV[29]</td><td>EXP[30]</td><td>ELE[31]</td><td>指揮[32]</td><td>ON狩り[33]</td><td>ONマイナス[34]</td><td>指揮修正[35]</td><td>戦闘画像[36]</td><td>内乱[37]</td><td>装備スロット4の予定[38]</td><td>大陸フラグ[39]</td><td>顔ぐら[40]</td><td>特殊1[41]</td><td>特殊2[42]</td><td>特殊3[43]</td><td>空き変数[44]</td><td>空き変数[45]</td><td>空き変数[46]</td><td>空き変数[47]</td><td>空き変数[48]</td><td>空き変数[49]</td><td>空き変数[50]</td><td>空き変数[51]</td><td>空き変数[52]</td><td>空き変数[53]</td><td>空き変数[54]</td><td>空き変数[55]</td><td>空き変数[56]</td><td>空き変数[57]</td><td>空き変数[58]</td><td>空き変数[59]</td><td>空き変数[60]</td><td>空き変数[61]</td><td>空き変数[62]</td><td>空き変数[63]</td><td>空き変数[64]</td><td>空き変数[65]</td><td>空き変数[66]</td><td>空き変数[67]</td><td>空き変数[68]</td><td>空き変数[69]</td><td>空き変数[70]</td><td>空き変数[71]</td><td>空き変数[72]</td><td>空き変数[73]</td><td>空き変数[74]</td><td>空き変数[75]</td><td>空き変数[76]</td><td>空き変数[77]</td><td>空き変数[78]</td><td>空き変数[79]</td></tr>

-----END-----
	require "./$LOG_FOLDER/_hash.data";

while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
&REPAIR(\@VALS);
$ET++;

#武器表示分け
local($WN_A,$WLV_A) = split(/!/,$VALS[9]);
local($WN_B,$WLV_B) = split(/!/,$VALS[10]);
local($WN_C,$WLV_C) = split(/!/,$VALS[11]);
@WN_sA=split(/\,/,$WEAPON_LIST{"$WN_A"});
@WN_sB=split(/\,/,$WEAPON_LIST{"$WN_B"});
@WN_sC=split(/\,/,$WEAPON_LIST{"$WN_C"});
#クラス表示分け
require "./$LOG_FOLDER/$CLASS_DATA";
my@plclass=split(/\,/,$VCLASS_LIST{"$VALS[4]"});

print "<tr><td><a href=javascript:syusei(\"$key\")>修正</a></td><td>$ET</td><td>$c </td><td>$key</td><td>$VALS[0]</td><td>$VALS[1]</td><td>$VALS[2]</td><td>$VALS[3]</td><td>$plclass[0]</td><td>$VALS[5]</td><td>$VALS[6]</td><td>$VALS[7]</td><td>$VALS[8]</td><td>".$WN_sA[0]."</td><td>".$WN_sB[0]."</td><td>".$WN_sC[0]."</td><td>$VALS[12]</td><td>$VALS[13]</td><td>$VALS[14]</td><td>$VALS[15]</td><td>$VALS[16]</td><td>$VALS[17]</td><td>$VALS[18]</td><td>$VALS[19]</td><td>$VALS[20]</td><td>$VALS[21]</td><td>$VALS[22]</td><td>$VALS[23]</td><td>$VALS[24]</td><td>$VALS[25]</td><td>$VALS[26]</td><td>$VALS[27]</td><td>$VALS[28]</td><td>$VALS[29]</td><td>$VALS[30]</td><td>$VALS[31]</td><td>$VALS[32]</td><td>$VALS[33]</td><td>$VALS[34]</td><td>$VALS[35]</td><td>$VALS[36]</td><td>$VALS[37]</td><td>$VALS[38]</td><td>$VALS[39]</td><td>$VALS[40]</td><td>$VALS[41]</td><td>$VALS[42]</td><td>$VALS[43]</td><td>$VALS[44]</td><td>$VALS[45]</td><td>$VALS[46]</td><td>$VALS[47]</td><td>$VALS[48]</td><td>$VALS[49]</td><td>$VALS[50]</td><td>$VALS[51]</td><td>$VALS[52]</td><td>$VALS[53]</td><td>$VALS[54]</td><td>$VALS[55]</td><td>$VALS[56]</td><td>$VALS[57]</td><td>$VALS[58]</td><td>$VALS[59]</td><td>$VALS[60]</td><td>$VALS[61]</td><td>$VALS[62]</td><td>$VALS[63]</td><td>$VALS[64]</td><td>$VALS[65]</td><td>$VALS[66]</td><td>$VALS[67]</td><td>$VALS[68]</td><td>$VALS[69]</td><td>$VALS[70]</td><td>$VALS[71]</td><td>$VALS[72]</td><td>$VALS[73]</td><td>$VALS[74]</td><td>$VALS[75]</td><td>$VALS[76]</td><td>$VALS[77]</td><td>$VALS[78]</td><td>$VALS[79]</td></tr>";
}

print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=79>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub SYUSEI5{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(P);
dbmopen (%P,"$DBM_P",0666);
@VALS = split(/\s/,$P{"$FORM{'plname'}"});
dbmclose %P;
print << "-----END-----";
	<script language="JavaScript">
		function tyousei(nm){
			fm1.plname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>

<tr><td bgcolor=#404040 colspan=79>

<form action=$MAIN_SCRIPT method=POST name=fm1 style="visibility:hidden;">
	<input type=hidden name="cmd" value=TYOUSEI>
	<input type=hidden name="plname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
</td></tr>
<tr><td bgcolor=#404040 colspan=79><b>メンテナンス－<a href=javascript:tyousei(\"$FORM{plname}\")>パラメータ修正</a></b></td></tr>
<tr><td>ユニット[key]</td><td>階級データ[0]</td><td>戦歴[1]</td><td>PASS[2]</td><td>コード[3]</td><td>クラス[4]</td><td>所属国[5]</td><td>国内ランク[6]</td><td>コメント[7]</td><td>資金[8]</td><td>武器[9]</td><td>\予\備1[10]</td><td>\予\備2[11]</td><td>ALI[12]</td><td>色[13]</td><td>RISK[14]</td><td>HP[15]</td><td>MAXHP[16]</td><td>MP[17]</td><td>MP[18]</td><td>STR[19]</td><td>VIT[20]</td><td>AGI[21]</td><td>DEX[22]</td><td>改造回数[23]</td><td>熟練[24]</td><td>修理状態[25]</td><td>時間[26]</td><td>画像[27]</td><td>部隊[28]</td><td>LV[29]</td><td>EXP[30]</td><td>ELE[31]</td><td>指揮[32]</td><td>ON狩り[33]</td><td>ONマイナス[34]</td><td>指揮修正[35]</td><td>戦闘画像[36]</td><td>内乱[37]</td><td>装備スロット4[38]</td><td>大陸フラグ[39]</td><td>顔ぐら[40]</td><td>特殊1[41]</td><td>特殊2[42]</td><td>特殊3[43]</td><td>空き変数[44]</td><td>空き変数[45]</td><td>空き変数[46]</td><td>空き変数[47]</td><td>空き変数[48]</td><td>空き変数[49]</td><td>空き変数[50]</td><td>空き変数[51]</td><td>空き変数[52]</td><td>空き変数[53]</td><td>空き変数[54]</td><td>空き変数[55]</td><td>空き変数[56]</td><td>空き変数[57]</td><td>空き変数[58]</td><td>空き変数[59]</td><td>空き変数[60]</td><td>空き変数[61]</td><td>空き変数[62]</td><td>空き変数[63]</td><td>空き変数[64]</td><td>空き変数[65]</td><td>空き変数[66]</td><td>空き変数[67]</td><td>空き変数[68]</td><td>空き変数[69]</td><td>空き変数[70]</td><td>空き変数[71]</td><td>空き変数[72]</td><td>空き変数[73]</td><td>空き変数[74]</td><td>空き変数[75]</td><td>空き変数[76]</td><td>空き変数[77]</td><td>空き変数[78]</td><td>空き変数[79]</td></tr>
	
<tr><td>

</td><td>
<input type=text name="para0" value="$VALS[0]"></td><td><input type=text name="para1" value="$VALS[1]"></td><td><input type=text name="para2" value="$VALS[2]"></td><td><input type=text name="para3" value="$VALS[3]"></td><td><input type=text name="para4" value="$VALS[4]"></td><td><input type=text name="para5" value="$VALS[5]"></td><td><input type=text name="para6" value="$VALS[6]"></td><td><input type=text name="para7" value="$VALS[7]"></td><td><input type=text name="para8" value="$VALS[8]"></td><td><input type=text name="para9" value="$VALS[9]"></td><td><input type=text name="para10" value="$VALS[10]"></td>
<td><input type=text name="para11" value="$VALS[11]"></td><td><input type=text name="para12" value="$VALS[12]"></td><td><input type=text name="para13" value="$VALS[13]"></td><td><input type=text name="para14" value="$VALS[14]"></td><td><input type=text name="para15" value="$VALS[15]"></td><td><input type=text name="para16" value="$VALS[16]"></td><td><input type=text name="para17" value="$VALS[17]"></td><td><input type=text name="para18" value="$VALS[18]"></td><td><input type=text name="para19" value="$VALS[19]"></td><td><input type=text name="para20" value="$VALS[20]"></td>
<td><input type=text name="para21" value="$VALS[21]"></td><td><input type=text name="para22" value="$VALS[22]"></td><td><input type=text name="para23" value="$VALS[23]"></td><td><input type=text name="para24" value="$VALS[24]"></td><td><input type=text name="para25" value="$VALS[25]"></td><td><input type=text name="para26" value="$VALS[26]"></td><td><input type=text name="para27" value="$VALS[27]"></td><td><input type=text name="para28" value="$VALS[28]"></td><td><input type=text name="para29" value="$VALS[29]"></td><td><input type=text name="para30" value="$VALS[30]"><td><input type=text name="para31" value="$VALS[31]"></td><td><input type=text name="para32" value="$VALS[32]"></td><td><input type=text name="para33" value="$VALS[33]"></td><td><input type=text name="para34" value="$VALS[34]"></td><td><input type=text name="para35" value="$VALS[35]"></td><td><input type=text name="para36" value="$VALS[36]"></td><td><input type=text name="para37" value="$VALS[37]"></td><td><input type=text name="para38" value="$VALS[38]"></td><td><input type=text name="para39" value="$VALS[39]">
</td><td><input type=text name="para40" value="$VALS[40]"></td><td><input type=text name="para41" value="$VALS[41]"></td><td><input type=text name="para42" value="$VALS[42]"></td><td><input type=text name="para43" value="$VALS[43]"></td><td><input type=text name="para44" value="$VALS[44]"></td><td><input type=text name="para45" value="$VALS[45]"></td><td><input type=text name="para46" value="$VALS[46]"></td><td><input type=text name="para47" value="$VALS[47]"></td><td><input type=text name="para48" value="$VALS[48]"></td><td><input type=text name="para49" value="$VALS[49]"></td>
</td><td><input type=text name="para50" value="$VALS[50]"></td><td><input type=text name="para51" value="$VALS[51]"></td><td><input type=text name="para52" value="$VALS[52]"></td><td><input type=text name="para53" value="$VALS[53]"></td><td><input type=text name="para54" value="$VALS[54]"></td><td><input type=text name="para55" value="$VALS[55]"></td><td><input type=text name="para56" value="$VALS[56]"></td><td><input type=text name="para57" value="$VALS[57]"></td><td><input type=text name="para58" value="$VALS[58]"></td><td><input type=text name="para59" value="$VALS[59]"></td>
</td><td><input type=text name="para60" value="$VALS[60]"></td><td><input type=text name="para61" value="$VALS[61]"></td><td><input type=text name="para62" value="$VALS[62]"></td><td><input type=text name="para63" value="$VALS[63]"></td><td><input type=text name="para64" value="$VALS[64]"></td><td><input type=text name="para65" value="$VALS[65]"></td><td><input type=text name="para66" value="$VALS[66]"></td><td><input type=text name="para67" value="$VALS[67]"></td><td><input type=text name="para68" value="$VALS[68]"></td><td><input type=text name="para69" value="$VALS[69]"></td>
</td><td><input type=text name="para70" value="$VALS[70]"></td><td><input type=text name="para71" value="$VALS[71]"></td><td><input type=text name="para72" value="$VALS[72]"></td><td><input type=text name="para73" value="$VALS[73]"></td><td><input type=text name="para74" value="$VALS[74]"></td><td><input type=text name="para75" value="$VALS[75]"></td><td><input type=text name="para76" value="$VALS[76]"></td><td><input type=text name="para77" value="$VALS[77]"></td><td><input type=text name="para78" value="$VALS[78]"></td><td><input type=text name="para79" value="$VALS[79]"></td>
</form><td>↓</td></tr>
        
-----END-----

print "<tr><td>$FORM{'plname'}</td><td>$VALS[0]</td><td>$VALS[1]</td><td>$VALS[2]</td><td>$VALS[3]</td><td>$VALS[4]</td><td>$VALS[5]</td><td>$VALS[6]</td><td>$VALS[7]</td><td>$VALS[8]</td><td>$VALS[9]</td><td>$VALS[10]</td><td>$VALS[11]</td><td>$VALS[12]</td><td>$VALS[13]</td><td>$VALS[14]</td><td>$VALS[15]</td><td>$VALS[16]</td><td>$VALS[17]</td><td>$VALS[18]</td><td>$VALS[19]</td><td>$VALS[20]</td><td>$VALS[21]</td><td>$VALS[22]</td><td>$VALS[23]</td><td>$VALS[24]</td><td>$VALS[25]</td><td>$VALS[26]</td><td>$VALS[27]</td><td>$VALS[28]</td><td>$VALS[29]</td><td>$VALS[30]</td><td>$VALS[31]</td><td>$VALS[32]</td><td>$VALS[33]</td><td>$VALS[34]</td><td>$VALS[35]</td><td>$VALS[36]</td><td>$VALS[37]</td><td>$VALS[38]</td><td>$VALS[39]</td><td>$VALS[40]</td><td>$VALS[41]</td><td>$VALS[42]</td><td>$VALS[43]</td><td>$VALS[44]</td><td>$VALS[45]</td><td>$VALS[46]</td><td>$VALS[47]</td><td>$VALS[48]</td><td>$VALS[49]</td><td>$VALS[50]</td><td>$VALS[51]</td><td>$VALS[52]</td><td>$VALS[53]</td><td>$VALS[54]</td><td>$VALS[55]</td><td>$VALS[56]</td><td>$VALS[57]</td><td>$VALS[58]</td><td>$VALS[59]</td><td>$VALS[60]</td><td>$VALS[61]</td><td>$VALS[62]</td><td>$VALS[63]</td><td>$VALS[64]</td><td>$VALS[65]</td><td>$VALS[66]</td><td>$VALS[67]</td><td>$VALS[68]</td><td>$VALS[69]</td><td>$VALS[70]</td><td>$VALS[71]</td><td>$VALS[72]</td><td>$VALS[73]</td><td>$VALS[74]</td><td>$VALS[75]</td><td>$VALS[76]</td><td>$VALS[77]</td><td>$VALS[78]</td><td>$VALS[79]</td><td><a href=javascript:tyousei(\"$FORM{plname}\")>決定</a></td></tr>";


print << "-----END-----";

<form action=$MAIN_SCRIPT method=POST>
<input type=hidden name="cmd" value="MASTER">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=38>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}
sub SYUSEI4{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(P);
	open(IN,"$LOG_FOLDER2/$FORM{'plname'}.cgi")|| &error('オープンエラー','指定されたファイルが開けません。');
	@PLVALS=<IN>;
	close(IN);
    foreach(@PLVALS){($NAME,$PLVALS2[0],$PLVALS2[1],$PLVALS2[2],$PLVALS2[3],$PLVALS2[4],$PLVALS2[5],$PLVALS2[6],$PLVALS2[7],$PLVALS2[8],$PLVALS2[9],$PLVALS2[10],$PLVALS2[11],$PLVALS2[12],$PLVALS2[13],$PLVALS2[14],$PLVALS2[15],$PLVALS2[16],$PLVALS2[17],$PLVALS2[18],$PLVALS2[19],$PLVALS2[20],$PLVALS2[21],$PLVALS2[22],$PLVALS2[23],$PLVALS2[24],$PLVALS2[25],$PLVALS2[26],$PLVALS2[27],$PLVALS2[28],$PLVALS2[29],$PLVALS2[30],$PLVALS2[31],$PLVALS2[32],$PLVALS2[33],$PLVALS2[34],$PLVALS2[35],$PLVALS2[36],$PLVALS2[37],$PLVALS2[38],$PLVALS2[39],$PLVALS2[40],$PLVALS2[41],$PLVALS2[42],$PLVALS2[43],$PLVALS2[44],$PLVALS2[45],$PLVALS2[46],$PLVALS2[47],$PLVALS2[48],$PLVALS2[49],$PLVALS2[50],$PLVALS2[51],$PLVALS2[52],$PLVALS2[53],$PLVALS2[54],$PLVALS2[55],$PLVALS2[56],$PLVALS2[57],$PLVALS2[58],$PLVALS2[59],$PLVALS2[60],$PLVALS2[61],$PLVALS2[62],$PLVALS2[63],$PLVALS2[64],$PLVALS2[65],$PLVALS2[66],$PLVALS2[67],$PLVALS2[68],$PLVALS2[69],$PLVALS2[70],$PLVALS2[71],$PLVALS2[72],$PLVALS2[73],$PLVALS2[74],$PLVALS2[75],$PLVALS2[76],$PLVALS2[77],$PLVALS2[78],$PLVALS2[79])=split(/<>/);
    &ERROR('エラー！！') if $NAME ne "$FORM{'plname'}";
}
 dbmopen (%P,"$DBM_P",0666);
 @VALS = split(/\s/,$P{"$FORM{'plname'}"});
 dbmclose %P;
print << "-----END-----";
	<script language="JavaScript">
		function syuuhuku(nm){
			fm1.plname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>

<tr><td bgcolor=#404040 colspan=38>

<form action=$MAIN_SCRIPT method=POST name=fm1 style="visibility:hidden;">
	<input type=hidden name="cmd" value=SYUUHUKU>
	<input type=hidden name="plname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
</td></tr>
<tr><td bgcolor=#404040 colspan=38><b><a href=javascript:syuuhuku(\"$FORM{plname}\")>メンテナンス－パラメータ復元</a></b></td></tr>
<tr><td>ＮＯ．</td><td>$c </td><td>名前</td><td>階級データ</td><td>戦歴</td><td>PASS</td><td>コード</td><td>クラス</td><td>所属国</td><td>国内ランク</td><td>コメント</td><td>資金</td><td>武器</td><td>\予\備１</td><td>\予\備２</td><td>ALI</td><td>色</td><td>RISK</td><td>ＨＰ</td><td>ＭＡＸＨＰ</td><td>ＭＰ</td><td>ＭＡＸＭＰ</td><td>STR</td><td>VIT</td><td>AGI</td><td>ＨＩＴ</td><td>改造回数</td><td>熟練</td><td>修理状態</td><td>時間</td><td>画像</td><td>部隊</td><td>ＬＶ</td><td>ＥＸ</td><td>ELE</td><td>指揮</td><td>ON狩り</td><td>修正</td></tr>
	
<tr><td>変更</td><td>$c </td><td>

</td><td>
<input type=text name="para0" value="$PLVALS2[0]"></td><td><input type=text name="para1" value="$PLVALS2[1]"></td><td><input type=text name="para2" value="$PLVALS2[2]"></td><td><input type=text name="para3" value="$PLVALS2[3]"></td><td><input type=text name="para4" value="$PLVALS2[4]"></td><td><input type=text name="para5" value="$PLVALS2[5]"></td><td><input type=text name="para6" value="$PLVALS2[6]"></td><td><input type=text name="para7" value="$PLVALS2[7]"></td><td><input type=text name="para8" value="$PLVALS2[8]"></td><td><input type=text name="para9" value="$PLVALS2[9]"></td><td><input type=text name="para10" value="$PLVALS2[10]"></td>
<td><input type=text name="para11" value="$PLVALS2[11]"></td><td><input type=text name="para12" value="$PLVALS2[12]"></td><td><input type=text name="para13" value="$PLVALS2[13]"></td><td><input type=text name="para14" value="$PLVALS2[14]"></td><td><input type=text name="para15" value="$PLVALS2[15]"></td><td><input type=text name="para16" value="$PLVALS2[16]"></td><td><input type=text name="para17" value="$PLVALS2[17]"></td><td><input type=text name="para18" value="$PLVALS2[18]"></td><td><input type=text name="para19" value="$PLVALS2[19]"></td><td><input type=text name="para20" value="$PLVALS2[20]"></td>
<td><input type=text name="para21" value="$PLVALS2[21]"></td><td><input type=text name="para22" value="$PLVALS2[22]"></td><td><input type=text name="para23" value="$PLVALS2[23]"></td><td><input type=text name="para24" value="$PLVALS2[24]"></td><td><input type=text name="para25" value="$PLVALS2[25]"></td><td><input type=text name="para26" value="$PLVALS2[26]"></td><td><input type=text name="para27" value="$PLVALS2[27]"></td><td><input type=text name="para28" value="$PLVALS2[28]"></td><td><input type=text name="para29" value="$PLVALS2[29]"></td><td><input type=text name="para30" value="$PLVALS2[30]"><td><input type=text name="para31" value="$PLVALS2[31]"></td><td><input type=text name="para32" value="$PLVALS2[32]"></td><td><input type=text name="para33" value="$PLVALS2[33]"></td><td><input type=text name="para34" value="$PLVALS2[34]"></td><td><input type=text name="para35" value="$PLVALS2[35]"></td>
<td><input type=text name="para36" value="$PLVALS2[36]"></td><td><input type=text name="para37" value="$PLVALS2[37]"></td><td><input type=text name="para38" value="$PLVALS2[38]"></td><td><input type=text name="para39" value="$PLVALS2[39]"></td><td><input type=text name="para40" value="$PLVALS2[40]"></td><td><input type=text name="para41" value="$PLVALS2[41]"></td><td><input type=text name="para42" value="$PLVALS2[42]"></td><td><input type=text name="para43" value="$PLVALS2[43]"></td><td><input type=text name="para44" value="$PLVALS2[44]"></td><td><input type=text name="para45" value="$PLVALS2[45]"></td><td><input type=text name="para46" value="$PLVALS2[46]"></td><td><input type=text name="para47" value="$PLVALS2[47]"></td><td><input type=text name="para48" value="$PLVALS2[48]"></td><td><input type=text name="para49" value="$PLVALS2[49]"></td>
<td><input type=text name="para50" value="$PLVALS2[50]"></td><td><input type=text name="para51" value="$PLVALS2[51]"></td><td><input type=text name="para52" value="$PLVALS2[52]"></td><td><input type=text name="para53" value="$PLVALS2[53]"></td><td><input type=text name="para54" value="$PLVALS2[54]"></td><td><input type=text name="para55" value="$PLVALS2[55]"></td><td><input type=text name="para56" value="$PLVALS2[56]"></td><td><input type=text name="para57" value="$PLVALS2[57]"></td><td><input type=text name="para58" value="$PLVALS2[58]"></td><td><input type=text name="para59" value="$PLVALS2[59]"></td>
<td><input type=text name="para60" value="$PLVALS2[60]"></td><td><input type=text name="para61" value="$PLVALS2[61]"></td><td><input type=text name="para62" value="$PLVALS2[62]"></td><td><input type=text name="para63" value="$PLVALS2[63]"></td><td><input type=text name="para64" value="$PLVALS2[64]"></td><td><input type=text name="para65" value="$PLVALS2[65]"></td><td><input type=text name="para66" value="$PLVALS2[66]"></td><td><input type=text name="para67" value="$PLVALS2[67]"></td><td><input type=text name="para68" value="$PLVALS2[68]"></td><td><input type=text name="para69" value="$PLVALS2[69]"></td>
<td><input type=text name="para70" value="$PLVALS2[70]"></td><td><input type=text name="para71" value="$PLVALS2[71]"></td><td><input type=text name="para72" value="$PLVALS2[72]"></td><td><input type=text name="para73" value="$PLVALS2[73]"></td><td><input type=text name="para74" value="$PLVALS2[74]"></td><td><input type=text name="para75" value="$PLVALS2[75]"></td><td><input type=text name="para76" value="$PLVALS2[76]"></td><td><input type=text name="para77" value="$PLVALS2[77]"></td><td><input type=text name="para78" value="$PLVALS2[78]"></td><td><input type=text name="para79" value="$PLVALS2[79]"></td>
</td></form><td>↓</td></tr>
        
-----END-----

print "<tr><td>☆</td><td>$c </td><td>$FORM{'plname'}</td><td>$VALS[0]</td><td>$VALS[1]</td><td>$VALS[2]</td><td>$VALS[3]</td><td>$VALS[4]</td><td>$VALS[5]</td><td>$VALS[6]</td><td>$VALS[7]</td><td>$VALS[8]</td><td>$VALS[9]</td><td>$VALS[10]</td><td>$VALS[11]</td><td>$VALS[12]</td><td>$VALS[13]</td><td>$VALS[14]</td><td>$VALS[15]</td><td>$VALS[16]</td><td>$VALS[17]</td><td>$VALS[18]</td><td>$VALS[19]</td><td>$VALS[20]</td><td>$VALS[21]</td><td>$VALS[22]</td><td>$VALS[23]</td><td>$VALS[24]</td><td>$VALS[25]</td><td>$VALS[26]</td><td>$VALS[27]</td><td>$VALS[28]</td><td>$VALS[29]</td><td>$VALS[30]</td><td>$VALS[31]</td><td>$VALS[32]</td><td>$VALS[33]</td><td>$VALS[34]</td><td>$VALS[35]</td><td>$VALS[36]</td><td>$VALS[37]</td><td>$VALS[38]</td><td>$VALS[39]</td><td>$VALS[40]</td><td>$VALS[41]</td><td>$VALS[42]</td><td>$VALS[43]</td><td>$VALS[44]</td><td>$VALS[45]</td><td>$VALS[46]</td><td>$VALS[47]</td><td>$VALS[48]</td><td>$VALS[49]</td><td>$VALS[50]</td><td>$VALS[51]</td><td>$VALS[52]</td><td>$VALS[53]</td><td>$VALS[54]</td><td>$VALS[55]</td><td>$VALS[56]</td><td>$VALS[57]</td><td>$VALS[58]</td><td>$VALS[59]</td><td>$VALS[60]</td><td>$VALS[61]</td><td>$VALS[62]</td><td>$VALS[63]</td><td>$VALS[64]</td><td>$VALS[65]</td><td>$VALS[66]</td><td>$VALS[67]</td><td>$VALS[68]</td><td>$VALS[69]</td><td>$VALS[70]</td><td>$VALS[71]</td><td>$VALS[72]</td><td>$VALS[73]</td><td>$VALS[74]</td><td>$VALS[75]</td><td>$VALS[76]</td><td>$VALS[77]</td><td>$VALS[78]</td><td>$VALS[79]</td><td>
<a href=javascript:syuuhuku(\"$FORM{plname}\")>復元</a></td></tr>";


print << "-----END-----";

<form action=$MAIN_SCRIPT method=POST>
<input type=hidden name="cmd" value="DATAUP">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=38>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub TYOUSEI2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%P,"$DBM_P",0666);
		@VALS = split(/\s/,$P{"$FORM{'plname'}"});
                $VALS[0]=$FORM{'para0'};
                $VALS[1]=$FORM{'para1'};
                $VALS[2]=$FORM{'para2'};
                $VALS[3]=$FORM{'para3'};
                $VALS[4]=$FORM{'para4'};
                $VALS[5]=$FORM{'para5'};
                $VALS[6]=$FORM{'para6'};
                $VALS[7]=$FORM{'para7'};
                $VALS[8]=$FORM{'para8'};
                $VALS[9]=$FORM{'para9'};
                $VALS[10]=$FORM{'para10'};
                $VALS[11]=$FORM{'para11'};
                $VALS[12]=$FORM{'para12'};
                $VALS[13]=$FORM{'para13'};
                $VALS[14]=$FORM{'para14'};
                $VALS[15]=$FORM{'para15'};
                $VALS[16]=$FORM{'para16'};
                $VALS[17]=$FORM{'para17'};
                $VALS[18]=$FORM{'para18'};
                $VALS[19]=$FORM{'para19'};
                $VALS[20]=$FORM{'para20'};
                $VALS[21]=$FORM{'para21'};
                $VALS[22]=$FORM{'para22'};
                $VALS[23]=$FORM{'para23'};
                $VALS[24]=$FORM{'para24'};
                $VALS[25]=$FORM{'para25'};
                $VALS[26]=$FORM{'para26'};
                $VALS[27]=$FORM{'para27'};
                $VALS[28]=$FORM{'para28'};
                $VALS[29]=$FORM{'para29'};
                $VALS[30]=$FORM{'para30'};
                $VALS[31]=$FORM{'para31'};
                $VALS[32]=$FORM{'para32'};
                $VALS[33]=$FORM{'para33'};
                $VALS[34]=$FORM{'para34'};
                $VALS[35]=$FORM{'para35'};
                $VALS[36]=$FORM{'para36'};
                $VALS[37]=$FORM{'para37'};
                $VALS[38]=$FORM{'para38'};
                $VALS[39]=$FORM{'para39'};
                $VALS[40]=$FORM{'para40'};
                $VALS[41]=$FORM{'para41'};
                $VALS[42]=$FORM{'para42'};
                $VALS[43]=$FORM{'para43'};
                $VALS[44]=$FORM{'para44'};
                $VALS[45]=$FORM{'para45'};
                $VALS[46]=$FORM{'para46'};
                $VALS[47]=$FORM{'para47'};
                $VALS[48]=$FORM{'para48'};
                $VALS[49]=$FORM{'para49'};
                $VALS[50]=$FORM{'para50'};
                $VALS[51]=$FORM{'para51'};
                $VALS[52]=$FORM{'para52'};
                $VALS[53]=$FORM{'para53'};
                $VALS[54]=$FORM{'para54'};
                $VALS[55]=$FORM{'para55'};
                $VALS[56]=$FORM{'para56'};
                $VALS[57]=$FORM{'para57'};
                $VALS[58]=$FORM{'para58'};
                $VALS[59]=$FORM{'para59'};
                $VALS[60]=$FORM{'para60'};
                $VALS[61]=$FORM{'para61'};
                $VALS[62]=$FORM{'para62'};
                $VALS[63]=$FORM{'para63'};
                $VALS[64]=$FORM{'para64'};
                $VALS[65]=$FORM{'para65'};
                $VALS[66]=$FORM{'para66'};
                $VALS[67]=$FORM{'para67'};
                $VALS[68]=$FORM{'para68'};
                $VALS[69]=$FORM{'para69'};
                $VALS[70]=$FORM{'para70'};
                $VALS[71]=$FORM{'para71'};
                $VALS[72]=$FORM{'para72'};
                $VALS[73]=$FORM{'para73'};
                $VALS[74]=$FORM{'para74'};
                $VALS[75]=$FORM{'para75'};
                $VALS[76]=$FORM{'para76'};
                $VALS[77]=$FORM{'para77'};
                $VALS[78]=$FORM{'para78'};
                $VALS[79]=$FORM{'para79'};
                $VALS[80]=$FORM{'para80'};
		$P{"$FORM{'plname'}"}="@VALS";
	dbmclose %P;
}

sub BACKUP2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(P);
print << "-----END-----";

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040><b>メンテナンス－バックアップデータ出力</b></td></tr>
<tr><td><font color=BLUE>出力を試みました。警告メッセージが出ない場合、成功です。</font></td></tr>

-----END-----
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);$ET++;

$VALS="$key<>$VALS[0]<>$VALS[1]<>$VALS[2]<>$VALS[3]<>$VALS[4]<>$VALS[5]<>$VALS[6]<>$VALS[7]<>$VALS[8]<>$VALS[9]<>$VALS[10]<>$VALS[11]<>$VALS[12]<>$VALS[13]<>$VALS[14]<>$VALS[15]<>$VALS[16]<>$VALS[17]<>$VALS[18]<>$VALS[19]<>$VALS[20]<>$VALS[21]<>$VALS[22]<>$VALS[23]<>$VALS[24]<>$VALS[25]<>$VALS[26]<>$VALS[27]<>$VALS[28]<>$VALS[29]<>$VALS[30]<>$VALS[31]<>$VALS[32]<>$VALS[33]<>$VALS[34]<>$VALS[35]<>$VALS[36]<>$VALS[37]<>$VALS[38]<>$VALS[39]<>$VALS[40]<>$VALS[41]<>$VALS[42]<>$VALS[43]<>$VALS[44]<>$VALS[45]<>$VALS[46]<>$VALS[47]<>$VALS[48]<>$VALS[49]<>$VALS[50]<>$VALS[51]<>$VALS[52]<>$VALS[53]<>$VALS[54]<>$VALS[55]<>$VALS[56]<>$VALS[57]<>$VALS[58]<>$VALS[59]<>$VALS[60]<>$VALS[61]<>$VALS[62]<>$VALS[63]<>$VALS[64]<>$VALS[65]<>$VALS[66]<>$VALS[67]<>$VALS[68]<>$VALS[69]<>$VALS[70]<>$VALS[71]<>$VALS[72]<>$VALS[73]<>$VALS[74]<>$VALS[75]<>$VALS[76]<>$VALS[77]<>$VALS[78]<>$VALS[79]<>$VALS[80]<>\n";
        if(!open(OUT,">$LOG_FOLDER2/$key.cgi")){ &ERROR("$key UserData Directry open error"); }
	print OUT $VALS;
	close(OUT);
        chmod(0666,"$LOG_FOLDER2/$key.cgi");

}

print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub DATAUP2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(P);
print << "-----END-----";
	<script language="JavaScript">
		function hukugen(nm){
			fm1.plname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=HUKUGEN>
	<input type=hidden name="plname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">

        </form>
<table width=100% height=100%><tr><td align=left>
《検索機能\:<a href="http://www12.big.or.jp/~kazu777/">kazu777</a>》
<form onSubmit="return seek_str(this.strings.value);">
検索文字を入力してください。
<input name=strings type=text size=15 onChange="n = 0;">
<input type=submit value="検索">
</form>

	<form action=$MAIN_SCRIPT method=POST>
	ID直接入力<input type="text" name="plname" SIZE="20">
	<input type=hidden name="cmd" value=HUKUGEN>
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit value="復元">
    </form>

<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040 colspan=37><b>プレイヤー選択</b></td></tr>
<tr><td>ＮＯ．</td><td>$c </td><td>ユニット</td><td>選択</td></tr>


-----END-----
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);$ET++;
print "<tr><td>$ET</td><td>$c </td><td>$key</td>
<td><a href=javascript:hukugen(\"$key\")>復元</a></td></tr>";
}

print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=37>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub COUNTRY2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(C);
print << "-----END-----";
	<script language="JavaScript">
		function hensyu(nm){
			fm1.cname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=HENSYU>
	<input type=hidden name="cname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
        </form>
<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040 colspan=79><b>メンテナンス－パラメータ\表\示－国家選択</b></td></tr>
<tr><td>ＮＯ．</td><td>選択</td><td>$c </td><td>国名</td><td>カラー</td><td>\予\算</td><td>部隊１</td><td>部隊２</td><td>部隊３</td><td>作戦名</td><td>目標国</td><td>作戦時間</td><td>部隊１目標国</td><td>部隊２目標国</td><td>部隊３目標国</td><td>要塞（ＨＰ）</td><td>要塞ステータス</td><td>滅ぼした国</td><td>最終戦略発動</td><td>タロットカード</td><td>マジシャン</td><td>プリエステス</td><td>エンプレス</td><td>エンペラー</td><td>ハイエロファント</td><td>ラヴァーズ</td><td>チャリオット</td><td>ストレングス</td><td>ハーミット</td><td>フォーチュン</td><td>ジャスティス</td><td>ハングドマン</td><td>デス</td><td>テンパランス</td><td>デビル</td><td>タワー</td><td>スター</td><td>ムーン</td><td>サン</td><td>ジャッジメント</td><td>ワールド</td><td>選択[41]</td><td>大陸(1：ゼテギネア2：ガリシア)[43]</td><td>オーブ再使用[44]</td><td>空き[45]</td><td>空き[46]</td><td>空き[47]</td><td>空き[48]</td><td>空き[49]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[60]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[70]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[50]</td><td>空き×[77]</td><td>空き×[78]</td><td>空き×[79]</td></tr>

-----END-----
require "./$LOG_FOLDER/$CARD_DATA";
while (my($key,$val) = each %C){
@VALS = split(/\s/,$val);$ET++;
my@vcard=split(/\,/,$VACARD_LIST{"$VALS[15]"});
print "<tr><td>$ET</td><td><a href=\"javascript:hensyu('$key')\">修正</a></td><td>$c </td><td>$key</td><td>$VALS[0]</td><td>$VALS[1]</td><td>$VALS[2]</td><td>$VALS[3]</td><td>$VALS[4]</td><td>$VALS[5]</td><td>$VALS[6]</td><td>$VALS[7]</td><td>$VALS[8]</td><td>$VALS[9]</td><td>$VALS[10]</td><td>$VALS[11]</td><td>$VALS[12]</td><td>$VALS[13]</td><td>$VALS[14]</td><td>$vcard[1]</td><td>$VALS[16]</td><td>$VALS[17]</td><td>$VALS[18]</td><td>$VALS[19]</td><td>$VALS[20]</td><td>$VALS[21]</td><td>$VALS[22]</td><td>$VALS[23]</td><td>$VALS[24]</td><td>$VALS[25]</td><td>$VALS[26]</td><td>$VALS[27]</td><td>$VALS[28]</td><td>$VALS[29]</td><td>$VALS[30]</td><td>$VALS[31]</td><td>$VALS[32]</td><td>$VALS[33]</td><td>$VALS[34]</td><td>$VALS[35]</td><td>$VALS[36]</td><td>$VALS[37]</td><td>$VALS[38]</td><td>$VALS[39]</td><td>$VALS[40]</td><td>$VALS[41]</td><td>$VALS[42]</td><td>$VALS[43]</td><td>$VALS[44]</td><td>$VALS[45]</td><td>$VALS[46]</td><td>$VALS[47]</td><td>$VALS[48]</td><td>$VALS[49]</td><td>$VALS[50]</td><td>$VALS[51]</td><td>$VALS[52]</td><td>$VALS[53]</td><td>$VALS[54]</td><td>$VALS[55]</td><td>$VALS[56]</td><td>$VALS[57]</td><td>$VALS[58]</td><td>$VALS[59]</td><td>$VALS[60]</td><td>$VALS[61]</td><td>$VALS[62]</td><td>$VALS[63]</td><td>$VALS[64]</td><td>$VALS[65]</td><td>$VALS[66]</td><td>$VALS[67]</td><td>$VALS[68]</td><td>$VALS[69]</td><td>$VALS[70]</td><td>$VALS[71]</td><td>$VALS[72]</td><td>$VALS[73]</td><td>$VALS[74]</td><td>$VALS[75]</td><td>$VALS[76]</td><td>$VALS[77]</td><td>$VALS[78]</td><td>$VALS[79]</td></tr>";
}

print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=41>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}
sub HENSYU2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(C);
dbmopen (%C,"$DBM_C",0666);
@VALS = split(/\s/,$C{"$FORM{'cname'}"});
dbmclose %C;
print << "-----END-----";
	<script language="JavaScript">
		function kaizan(nm){
			fm1.cname.value=nm;
			fm1.sbm1.click();
		}
		
	</script>

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>

<tr><td bgcolor=#404040 colspan=79>

<form action=$MAIN_SCRIPT method=POST name=fm1 style="visibility:hidden;">
	<input type=hidden name="cmd" value=KAIZAN>
	<input type=hidden name="cname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
</td><td>
<tr><td bgcolor=#404040 colspan=79><b>メンテナンス－パラメータ修正</b></td></tr>
<tr><td>ＮＯ．</td><td>$c </td><td>国名</td><td>カラー</td><td>\予\算</td><td>部隊１</td><td>部隊２</td><td>部隊３</td><td>作戦名</td><td>目標国</td><td>作戦時間</td><td>部隊１目標国</td><td>部隊２目標国</td><td>部隊３目標国</td><td>要塞（ＨＰ）</td><td>要塞ステータス</td><td>滅ぼした国</td><td>最終戦略発動</td><td>タロットカード</td><td>マジシャン</td><td>プリエステス</td><td>エンプレス</td><td>エンペラー</td><td>ハイエロファント</td><td>ラヴァーズ</td><td>チャリオット</td><td>ストレングス</td><td>ハーミット</td><td>フォーチュン</td><td>ジャスティス</td><td>ハングドマン</td><td>デス</td><td>テンパランス</td><td>デビル</td><td>タワー</td><td>スター</td><td>ムーン</td><td>サン</td><td>ジャッジメント</td><td>ワールド</td><td>フォーチュン！</td><td>選択</td><td>大陸(1：ゼテギネア2：ガリシア)[43]</td><td>オーブ再使用[44]</td><td>空き[45]</td><td>空き[46]</td><td>空き[47]</td><td>空き[48]</td><td>空き[49]</td><td>空き×[50]</td><td>空き変数[51]</td><td>空き変数[52]</td><td>空き変数[53]</td><td>空き変数[54]</td><td>空き変数[55]</td><td>空き変数[56]</td><td>空き変数[57]</td><td>空き変数[58]</td><td>空き変数[59]</td><td>空き変数[61]</td><td>空き変数[62]</td><td>空き変数[63]</td><td>空き変数[64]</td><td>空き変数[65]</td><td>空き変数[66]</td><td>空き変数[67]</td><td>空き変数[68]</td><td>空き変数[69]</td><td>空き変数[71]</td><td>空き変数[72]</td><td>空き変数[73]</td><td>空き変数[74]</td><td>空き変数[75]</td><td>空き変数[76]</td><td>空き変数[77]</td><td>空き変数[78]</td><td>空き変数[79]</td></tr>
	
<tr><td>変更</td><td>$c </td><td>

</td><td>
<input type=text name="para0" value="$VALS[0]"></td><td><input type=text name="para1" value="$VALS[1]"></td><td><input type=text name="para2" value="$VALS[2]"></td><td><input type=text name="para3" value="$VALS[3]"></td><td><input type=text name="para4" value="$VALS[4]"></td><td><input type=text name="para5" value="$VALS[5]"></td><td><input type=text name="para6" value="$VALS[6]"></td><td><input type=text name="para7" value="$VALS[7]"></td><td><input type=text name="para8" value="$VALS[8]"></td><td><input type=text name="para9" value="$VALS[9]"></td><td><input type=text name="para10" value="$VALS[10]"></td>
<td><input type=text name="para11" value="$VALS[11]"></td><td><input type=text name="para12" value="$VALS[12]"></td><td><input type=text name="para13" value="$VALS[13]"></td><td><input type=text name="para14" value="$VALS[14]"></td><td><input type=text name="para15" value="$VALS[15]"></td><td><input type=text name="para16" value="$VALS[16]"></td><td><input type=text name="para17" value="$VALS[17]"></td><td><input type=text name="para18" value="$VALS[18]"></td><td><input type=text name="para19" value="$VALS[19]"></td><td><input type=text name="para20" value="$VALS[20]"></td><td><input type=text name="para21" value="$VALS[21]"></td><td><input type=text name="para22" value="$VALS[22]"></td><td><input type=text name="para23" value="$VALS[23]"></td><td><input type=text name="para24" value="$VALS[24]"></td><td><input type=text name="para25" value="$VALS[25]"></td><td><input type=text name="para26" value="$VALS[26]"></td><td><input type=text name="para27" value="$VALS[27]"></td>
<td><input type=text name="para28" value="$VALS[28]"></td><td><input type=text name="para29" value="$VALS[29]"></td><td><input type=text name="para30" value="$VALS[30]"></td><td><input type=text name="para31" value="$VALS[31]"></td><td><input type=text name="para32" value="$VALS[32]"></td><td><input type=text name="para33" value="$VALS[33]"></td><td><input type=text name="para34" value="$VALS[34]"></td><td><input type=text name="para35" value="$VALS[35]"></td><td><input type=text name="para36" value="$VALS[36]"></td><td><input type=text name="para37" value="$VALS[37]"></td><td><input type=text name="para38" value="$VALS[38]"></td>
<td><input type=text name="para39" value="$VALS[39]"></td><td><input type=text name="para40" value="$VALS[40]"></td><td><input type=text name="para41" value="$VALS[41]"></td><td><input type=text name="para42" value="$VALS[42]"></td><td><input type=text name="para43" value="$VALS[43]"></td><td><input type=text name="para44" value="$VALS[44]"></td><td><input type=text name="para45" value="$VALS[45]"></td><td><input type=text name="para46" value="$VALS[46]"></td><td><input type=text name="para47" value="$VALS[47]"></td><td><input type=text name="para48" value="$VALS[48]"></td><td><input type=text name="para49" value="$VALS[49]"></td>
<td><input type=text name="para50" value="$VALS[50]"></td><td><input type=text name="para51" value="$VALS[51]"></td><td><input type=text name="para52" value="$VALS[52]"></td>
<td><input type=text name="para53" value="$VALS[53]"></td><td><input type=text name="para54" value="$VALS[54]"></td><td><input type=text name="para55" value="$VALS[55]"></td>
<td><input type=text name="para56" value="$VALS[56]"></td><td><input type=text name="para57" value="$VALS[57]"></td><td><input type=text name="para58" value="$VALS[58]"></td>
<td><input type=text name="para59" value="$VALS[59]"></td>
<td><input type=text name="para60" value="$VALS[60]"></td><td><input type=text name="para61" value="$VALS[61]"></td><td><input type=text name="para62" value="$VALS[62]"></td>
<td><input type=text name="para63" value="$VALS[63]"></td><td><input type=text name="para64" value="$VALS[64]"></td><td><input type=text name="para65" value="$VALS[65]"></td>
<td><input type=text name="para66" value="$VALS[66]"></td><td><input type=text name="para67" value="$VALS[67]"></td><td><input type=text name="para68" value="$VALS[68]"></td>
<td><input type=text name="para69" value="$VALS[69]"></td>
<td><input type=text name="para70" value="$VALS[70]"></td><td><input type=text name="para71" value="$VALS[71]"></td><td><input type=text name="para72" value="$VALS[72]"></td>
<td><input type=text name="para73" value="$VALS[73]"></td><td><input type=text name="para74" value="$VALS[74]"></td><td><input type=text name="para75" value="$VALS[75]"></td>
<td><input type=text name="para76" value="$VALS[76]"></td><td><input type=text name="para77" value="$VALS[77]"></td><td><input type=text name="para78" value="$VALS[78]"></td>
<td><input type=text name="para79" value="$VALS[79]"></td>
</td></form><td>↓</td></tr>
        
-----END-----

print "<tr><td>☆</td><td>$c </td><td>$FORM{'cname'}</td><td>$VALS[0]</td><td>$VALS[1]</td><td>$VALS[2]</td><td>$VALS[3]</td><td>$VALS[4]</td><td>$VALS[5]</td><td>$VALS[6]</td><td>$VALS[7]</td><td>$VALS[8]</td><td>$VALS[9]</td><td>$VALS[10]</td><td>$VALS[11]</td><td>$VALS[12]</td><td>$VALS[13]</td><td>$VALS[14]</td><td>$VALS[15]</td><td>$VALS[16]</td><td>$VALS[17]</td><td>$VALS[18]</td><td>$VALS[19]</td><td>$VALS[20]</td><td>$VALS[21]</td><td>$VALS[22]</td><td>$VALS[23]</td><td>$VALS[24]</td><td>$VALS[25]</td><td>$VALS[26]</td><td>$VALS[27]</td><td>$VALS[28]</td><td>$VALS[29]</td><td>$VALS[30]</td><td>$VALS[31]</td><td>$VALS[32]</td><td>$VALS[33]</td><td>$VALS[34]</td><td>$VALS[35]</td><td>$VALS[36]</td><td>$VALS[37]</td><td>$VALS[38]</td><td>$VALS[39]</td><td>$VALS[40]</td><td>$VALS[41]</td><td>$VALS[42]</td><td>$VALS[43]</td><td>$VALS[44]</td><td>$VALS[45]</td><td>$VALS[46]</td><td>$VALS[47]</td><td>$VALS[48]</td><td>$VALS[49]</td><td>$VALS[50]</td><td>$VALS[51]</td><td>$VALS[52]</td><td>$VALS[53]</td><td>$VALS[54]</td><td>$VALS[55]</td><td>$VALS[56]</td><td>$VALS[57]</td><td>$VALS[58]</td><td>$VALS[59]</td><td>$VALS[60]</td><td>$VALS[61]</td><td>$VALS[62]</td><td>$VALS[63]</td><td>$VALS[64]</td><td>$VALS[65]</td><td>$VALS[66]</td><td>$VALS[67]</td><td>$VALS[68]</td><td>$VALS[69]</td><td>$VALS[70]</td><td>$VALS[71]</td><td>$VALS[72]</td><td>$VALS[73]</td><td>$VALS[74]</td><td>$VALS[75]</td><td>$VALS[76]</td><td>$VALS[77]</td><td>$VALS[78]</td><td>$VALS[79]</td><td><a href=\"javascript:kaizan('$FORM{'cname'}')\">決定</a></td></tr>";


print << "-----END-----";

<form action=$MAIN_SCRIPT method=POST>
<input type=hidden name="cmd" value="COUNTRY">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=79>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}
sub KAIZAN2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%C,"$DBM_C",0666);
		@VALS = split(/\s/,$C{"$FORM{'cname'}"});
                $VALS[0]=$FORM{'para0'};
                $VALS[1]=$FORM{'para1'};
                $VALS[2]=$FORM{'para2'};
                $VALS[3]=$FORM{'para3'};
                $VALS[4]=$FORM{'para4'};
                $VALS[5]=$FORM{'para5'};
                $VALS[6]=$FORM{'para6'};
                $VALS[7]=$FORM{'para7'};
                $VALS[8]=$FORM{'para8'};
                $VALS[9]=$FORM{'para9'};
                $VALS[10]=$FORM{'para10'};
                $VALS[11]=$FORM{'para11'};
                $VALS[12]=$FORM{'para12'};
                $VALS[13]=$FORM{'para13'};
                $VALS[15]=$FORM{'para14'};
                $VALS[15]=$FORM{'para15'};
                $VALS[16]=$FORM{'para16'};
                $VALS[17]=$FORM{'para17'};
                $VALS[18]=$FORM{'para18'};
                $VALS[19]=$FORM{'para19'};
                $VALS[20]=$FORM{'para20'};
                $VALS[21]=$FORM{'para21'};
                $VALS[22]=$FORM{'para22'};
                $VALS[23]=$FORM{'para23'};
                $VALS[24]=$FORM{'para24'};
                $VALS[25]=$FORM{'para25'};
                $VALS[26]=$FORM{'para26'};
                $VALS[27]=$FORM{'para27'};
                $VALS[28]=$FORM{'para28'};
                $VALS[29]=$FORM{'para29'};
                $VALS[30]=$FORM{'para30'};
                $VALS[31]=$FORM{'para31'};
                $VALS[32]=$FORM{'para32'};
                $VALS[33]=$FORM{'para33'};
                $VALS[34]=$FORM{'para34'};
                $VALS[35]=$FORM{'para35'};
                $VALS[36]=$FORM{'para36'};
                $VALS[37]=$FORM{'para37'};
                $VALS[38]=$FORM{'para38'};
                $VALS[39]=$FORM{'para39'};
                $VALS[40]=$FORM{'para40'};
                $VALS[41]=$FORM{'para41'};
                $VALS[42]=$FORM{'para42'};
                $VALS[43]=$FORM{'para43'};
                $VALS[44]=$FORM{'para44'};
                $VALS[45]=$FORM{'para45'};
                $VALS[46]=$FORM{'para46'};
                $VALS[47]=$FORM{'para47'};
                $VALS[48]=$FORM{'para48'};
                $VALS[49]=$FORM{'para49'};
                $VALS[50]=$FORM{'para50'};
                $VALS[51]=$FORM{'para51'};
                $VALS[52]=$FORM{'para52'};
                $VALS[53]=$FORM{'para53'};
                $VALS[54]=$FORM{'para54'};
                $VALS[55]=$FORM{'para55'};
                $VALS[56]=$FORM{'para56'};
                $VALS[57]=$FORM{'para57'};
                $VALS[58]=$FORM{'para58'};
                $VALS[59]=$FORM{'para59'};
                $VALS[60]=$FORM{'para60'};
                $VALS[61]=$FORM{'para61'};
                $VALS[62]=$FORM{'para62'};
                $VALS[63]=$FORM{'para63'};
                $VALS[64]=$FORM{'para64'};
                $VALS[65]=$FORM{'para65'};
                $VALS[66]=$FORM{'para66'};
                $VALS[67]=$FORM{'para67'};
                $VALS[68]=$FORM{'para68'};
                $VALS[69]=$FORM{'para69'};
                $VALS[70]=$FORM{'para70'};
                $VALS[71]=$FORM{'para71'};
                $VALS[72]=$FORM{'para72'};
                $VALS[73]=$FORM{'para73'};
                $VALS[74]=$FORM{'para74'};
                $VALS[75]=$FORM{'para75'};
                $VALS[76]=$FORM{'para76'};
                $VALS[77]=$FORM{'para77'};
                $VALS[78]=$FORM{'para78'};
                $VALS[79]=$FORM{'para79'};
		$C{"$FORM{'cname'}"}="@VALS";
	dbmclose %C;
}

sub COOKIES2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}


&HEADER;
&DBM_INPORT(P);
print << "-----END-----";
	<script language="JavaScript">
		function del(nm){
			fm1.plname.value=nm;
			fm1.sbm1.click();
                        alert('本当に削除してよろしいですか？');
		}
		
	</script>
	<form action=$MAIN_SCRIPT method=POST name=fm1 style="position:absolute;visibility:hidden;">
	<input type=hidden name="cmd" value=DEL>
	<input type=hidden name="plname">
	<input type=hidden name="pwd" value="$FORM{'pwd'}">
	<input type=submit name="sbm1">
        </form>
<table width=100% height=100%><tr><td align=center>
《検索機能\:<a href="http://www12.big.or.jp/~kazu777/">kazu777</a>》
<form onSubmit="return seek_str(this.strings.value);">
検索文字を入力してください。
<input name=strings type=text size=15 onChange="n = 0;">
<input type=submit value="検索">
</form>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040 colspan=5><center><b>削除期限</b></center></td></tr>
<tr><td>ＮＯ．</td><td>ユニット</td><td>削除期限</td><td>最終ログイン</td><td>　</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
push(@tmp1, $VALS[26]);
$PNAME[$i]=$key;

if($VALS[24] < 100){$PLIMIT[$i]=int(($COOKIE_KEEP2*24*60*60-(time-$VALS[26]))/(24*60*60));
}else{$PLIMIT[$i]=int(($COOKIE_KEEP*24*60*60-(time-$VALS[26]))/(24*60*60));}
$PTIME[$i]=$VALS[26];

$i++;
}

@PNAME = @PNAME[sort {$tmp1[$a] <=> $tmp1[$b]} 0 .. $#tmp1];
@PLIMIT = @PLIMIT[sort {$tmp1[$a] <=> $tmp1[$b]} 0 .. $#tmp1];
@PTIME = @PTIME[sort {$tmp1[$a] <=> $tmp1[$b]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     $k=$j+1;
print "<tr><td>$k</td><td><font>$PNAME[$j]</font></td><td><font color=BLACK>【$PLIMIT[$j]日】</font></td>";
print "<td>".&DATE_DECORD($PTIME[$j]);
print "</td><td><a href=\"javascript:del('$PNAME[$j]')\">削除</a></td>";

print "</tr>";
$j++;
}

print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td colspan=5>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub OPENHITO2 {
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
$BU="_2";
$UPDBM_P="$DBM_P$BU";
print << "-----END-----";

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040><b>メンテナンス－PL_DATE→DBM復元</b></td></tr>
<tr><td><font color=BLUE>分離展開したPLデータをDBMに復元しました。警告メッセージが出ない場合、成功です。</font></td></tr>

-----END-----
opendir(DIR,"$LOG_FOLDER2");
@kkk = sort(grep { m/.*\.hit/ } readdir(DIR));
closedir(DIR);

foreach(@kkk){
if(!open(OPEN,"./$LOG_FOLDER2/$_")){ &ERROR('UserData Directry open error'); }
@LOGS = <OPEN>;
close(OUT);

($id,$dmy) = split(/\./);

dbmopen (%A,"$UPDBM_P",0666);
$A{"$id"}="@LOGS";
dbmclose %A;
}
print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://melcha.zone.ne.jp/ebs/dl/\">44NET FACTORY</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub OPENKUNI2 {
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
$BU="_2";
$UPDBM_C="$DBM_C$BU";
print << "-----END-----";

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040><b>メンテナンス－CO_DATE→DBM復元</b></td></tr>
<tr><td><font color=BLUE>分離展開したCOデータをDBMに復元しました。警告メッセージが出ない場合、成功です。</font></td></tr>

-----END-----
opendir(DIR,"$LOG_FOLDER2");
@kkk = sort(grep { m/.*\.kun/ } readdir(DIR));
closedir(DIR);

foreach(@kkk){
if(!open(OPEN,"./$LOG_FOLDER2/$_")){ &ERROR('UserData Directry open error'); }
@LOGS = <OPEN>;
close(OUT);

($id,$dmy) = split(/\./);

dbmopen (%A,"$UPDBM_C",0666);
$A{"$id"}="@LOGS";
dbmclose %A;
}
print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://melcha.zone.ne.jp/ebs/dl/\">44NET FACTORY</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub PUSHHITO2 {
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(P);
print << "-----END-----";

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040><b>メンテナンス－DBM→PL_DATE分離</b></td></tr>
<tr><td><font color=BLUE>DBMからPLデータを分離展開しました。警告メッセージが出ない場合、成功です。</font></td></tr>

-----END-----
while(my($key,$val) = each %P){
@VALUESA = split(/\s/,$val);
if(!open(OUT,"> ./$LOG_FOLDER2/$key.hit")){ &ERROR("$key UserData Directry open error"); }
print OUT "@VALUESA";
close(OUT);
}
print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://melcha.zone.ne.jp/ebs/dl/\">44NET FACTORY</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub PUSHKUNI2 {
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

&HEADER;
&DBM_INPORT(C);
print << "-----END-----";

<table width=100% height=100%><tr><td align=center>
<table cellspacing=2 cellpadding=3 bgcolor="#909090" style="font-size:16px;" border=1>
<tr><td bgcolor=#404040><b>メンテナンス－DBM→CO_DATE分離</b></td></tr>
<tr><td><font color=BLUE>DBMからCOデータを分離展開しました。警告メッセージが出ない場合、成功です。</font></td></tr>

-----END-----
while(my($key,$val) = each %C){
@VALUESA = split(/\s/,$val);
if(!open(OUT,"> ./$LOG_FOLDER2/$key.kun")){ &ERROR("$key UserData Directry open error"); }
print OUT "@VALUESA";
close(OUT);
}
print << "-----END-----";

<form action="$MAIN_SCRIPT" method="POST">
<input type=hidden name="cmd" value="MAINTE">
<input type=hidden name="admin" value="main">
<input type=hidden name="pwd" value="$FORM{'pwd'}"><tr><td>
<input type=submit value=戻る>
</td></tr></table>
-----END-----
	print "<BR><center>データ調整：EDIT BY <a href=\"http://melcha.zone.ne.jp/ebs/dl/\">44NET FACTORY</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub DEL2{
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	dbmopen (%P,"$DBM_P",0666);
		delete $P{"$FORM{'plname'}"};
	dbmclose %P;
	rename "$LOG_FOLDER2/$FORM{'plname'}.cgi", "$LOG_FOLDER2/$FORM{'plname'}.bak";
}

sub HEADER2 {
	if(crypt($FORM{'pwd'}, substr($password,$salt,2)) ne $password){&ERROR('パスワードが違います！！');exit;}

	$BG_MAIN="bgcolor=\"$BG_MAIN\"" if $BG_MAIN !~ /\./;
	$BG_MAIN="background=\"$BG_MAIN\"" if $BG_MAIN =~ /\./;
	print "Content-type: text/html\n\n";
	print << "	-----END-----";
	<!--美乳-->
	<!DOCTYPE HTML PUBLIC -//IETF//DTD HTML//EN>
	<html><head>
	<meta http-equiv="Content-Type" content="text/html; charset=x-sjis">
	<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
	<title>ENDLESS BATTLE</title>
<SCRIPT LANGUAGE="JavaScript">
<!--
var Nsc4 = (document.layers);
var Ie4 = (document.all);

var win = this;
var n   = 0;

function seek_str(str) {
var txt, i, found;
  if (str == ""){
    alert("検索文字を入力して下さい。");
    return false;
  }
  if (Nsc4) {
    if (!win.find(str)){
      while(win.find(str, false, true)){
        n++;
      }
    }else{
      n++;
    }
    if (n == 0){alert(str + " は見つかりませんでした。");}
  }
  if (Ie4) {
    txt = win.document.body.createTextRange();
    for (i = 0; i <= n && (found = txt.findText(str)) != false; i++) {
      txt.moveStart("character", 1);
      txt.moveEnd("textedit");
    }
    if (found) {
      txt.moveStart("character", -1);
      txt.findText(str);
      txt.select();
      txt.scrollIntoView();
      n++;
    }else{
      if (n > 0) {
        n = 0;
        seek_str(str);
      }else{
        alert(str + " は見つかりませんでした。");
      }
    }
  }
  return false;
}
//-->
</script>
        </head>
	<body $BG_MAIN text="$FONT_COLOR" style=\"margin:0px 0px 0px 0px;\" oncontextmenu="return false;">
	-----END-----
}

1;

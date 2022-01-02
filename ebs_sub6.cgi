$to='l';$o=time;

sub ENTRY2 {
	require './vaback.pl';
	&backplayerlist;

	if ($CountPl >= $ENTRY_MAX){&ERROR('登録が込み合っています。再アクセスして下さい。');}
	&DBM_INPORT(C);
	require "./$LOG_FOLDER/$HASH_DATA";
	&HEADER;
	print << "	-----END-----";
	<script language="JavaScript">
		function changeImg(){
			num=document.entry.imgSelect.selectedIndex;
			document.msImg.src="$IMG_FOLDER2/"+ num +".gif";
		}
		function changeImg2(){
			num2=document.entry.imgSelect2.selectedIndex;
			document.msImg2.src="$IMG_FOLDER7/"+ num2 +".gif";
		}

		function checkRiyou (){
			if (document.entry.pname.value == '') {window.alert("ユニット名が未入力です。");return false 
			}else if(document.entry.msname.value == '') {window.alert("コードネームが未入力です。");return false 
			}else if(document.entry.pass.value == '') {window.alert("パスワードが未入力です。");return false 
			}else if(document.entry.pname.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
				window.alert("だーめっ！");return false ;
			}else if(document.entry.msname.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
				window.alert("だーめっ！");return false ;
			}else if(document.entry.pass.value.match('[&! ?=.,*<>"\\'/･ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝｧｨｩｪｫｯ№㏍℡㊤㊥㊦㊧㊨㈱㈲㈹㍾㍽㍼㍻①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳≡∑∫∮√⊥∠∟⊿∵∩∪纊鍈蓜炻棈兊夋奛奣寬﨑嵂ⅠⅡⅢⅣⅤⅥⅦⅧⅩ]') != null) {
				window.alert("だーめっ！");return false ;
			}else {if (confirm('登録を開始します。') == true){return true;}else{return false}	}	
		}
	</script>
	<style type="text/css">
		.td1{text-align:center;background-color:$TABLE_COLOR2;font-weight:bold;font-size:16px;}
	</style>
	<table width=100% height=100%><tr><td align=center>
	<div align=center style="font-size:55px;font-family:'細明朝体','ＭＳ Ｐ明朝';color:#505050;filter:alpha(opacity=100,finishopacity=0,style=2);height:60px;background-color:#fff0f0;"><b>新規登録</b></div>
	</td></tr><tr><td align=center>
	<form action=$MAIN_SCRIPT method=POST name=entry>
	<input type=hidden name=cmd value=KAKUNIN>    
	<img src=\"$IMG_FOLDER2/0.gif\" name=\"msImg\">
	<table cellspacing=1 style="font-size:10pt;" bgcolor="$TABLE_COLOR1">
	<tr><td class=td1>ユニット名</td>
	    <td><input type=text name=pname size=30 maxlength=15 $STYLE_L>
	    <font style="font-size:12px;">ユニット名、コードネームは好きな名前を入れてください</font></td></tr>
	<tr><td class=td1>コードネーム</td><td><input type=text name=msname size=30 maxlength=20 $STYLE_L></td></tr>
	<tr><td class=td1>パスワード</td><td><input type=password maxlength=8 name=pass size=15 $STYLE_L>
	    <font style="font-size:12px;">パスワードは<b>半角</b>のみ８文字まで(忘れないようにしてください）</font></td></tr>

	<tr><td class=td1>キャラクタアイコン</td><td><select name=imgSelect2 onChange=\"changeImg2()\">
	-----END-----
	foreach (0..$ICON2){
		print "<option value=\"$_\">アイコンNo.$_\n";
		}
	print << "	-----END-----";
	</select>&nbsp;&nbsp;<img src=\"$IMG_FOLDER7/0.gif\" name=\"msImg2\"></td></tr>


    <tr><td class=td1>ユニットアイコン</td><td><select name=imgSelect onChange=\"changeImg()\">
	-----END-----
	foreach (0..$ICON){
		print "<option value=\"$_\">アイコンNo.$_\n";
		}
	require "./$LOG_FOLDER/$CLASS_DATA";
	@ALY_CLASS1=split(/\,/,$VCLASS_LIST{"0"});
	@ALY_CLASS2=split(/\,/,$VCLASS_LIST{"1"});
	@ALY_CLASS3=split(/\,/,$VCLASS_LIST{"93"});
	@ALY_CLASS4=split(/\,/,$VCLASS_LIST{"44"});
	print << "	-----END-----";
	</select></td></tr>
#	<tr><td class=td1>クラス選択</td><td><select name=type>
#	<option value=0>$ALY_CLASS1[0]<option value=1>$ALY_CLASS2[0]<option value=93>$ALY_CLASS3[0]<option value=44>$ALY_CLASS4[0]</select></td></tr>
#	<tr><td class=td1>エレメント選択</td><td><select name=element>
#	<option value=0>風<option value=1>炎<option value=2>大地<option value=3>水</select></td></tr>
	<tr><td class=td1>武器</td><td><select name=w>
	-----END-----
	while (my($wkey,$wvalue) =each %WEAPON_LIST) {
		my@w=split(/,/,$wvalue);print "<option value=$wkey>$w[0]\n" if $w[6]==7;
	}

	print "</select></tr><tr><td class=td1>色</td><td>\n";

	print "<select name=cl>";
	foreach (@COLOR){
		print "<option value=\"$_\"";
		print " style=\"color:#$_\">■$_\n";
	}
	print "</select>";

#	print "<tr><td class=td1>大陸選択</td><td><select name=continent>";
#	if(50 <= int(rand(100))){
#		print "<option value=0>$CONTINENT_A<option value=1 selected>$CONTINENT_B</select></td></tr>";
#	}else{
#		print "<option value=0 selected>$CONTINENT_A<option value=1>$CONTINENT_B</select></td></tr>";
#	}

	print "</td></tr><tr><td class=td1>国籍<td>\n";
	print "<select size=1 name=\"kuni\">\n";
	my $KUNIFRAG=1;
#	while (($key,$value) =each %C) {
#		@C_VALUES = split(/\s/,$value);
#	if ($C_VALUES[7] <= time){print "<option value=$key>$key\n";$KUNIFRAG=0;}
#	}
#	if($KUNIFRAG){print "<option value=\"\">$NONE_NATIONALITY";}
	print "<option value=\"\">$NONE_NATIONALITY";
	print << "	-----END-----";
		</select></td></tr>
			<tr><td colspan=2 align="center"> 
			<input type=submit value=登録 onClick="return checkRiyou()">
			<input type=reset value=リセット>
		    </td></tr></table></form></td></tr><tr><td align=center>
	-----END-----
	&FOOTER;
	print "</td></tr></table></body>";
}

#登録内容確認画面生成ルーチン
sub KAKUNIN2 {
	require './vaback.pl';
	&backplayerlist;

	$BACKUPFLG=0;
	open(IN,"$LOG_FOLDER2/$FORM{'pname'}.cgi")|| $BACKUPFLG++;;
	close(IN);
	if($BACKUPFLG!=1){&ERROR('同じ名前の登録が既に存在します','別の名前で登録して下さい。');}

	&LOCK;
	&DBM_INPORT(P);
	&UNLOCK;
	if($P{"$FORM{'pname'}"}){&ERROR('同じ名前の登録が既に存在します','別の名前で登録して下さい。'); }
	if($FORM{'pname'} eq 'durante'){&ERROR('同じ名前の登録が既に存在します','別の名前で登録して下さい。'); }
	if (!$FORM{'pname'} && !$FORM{'msname'} && !$FORM{'pass'}) { &ERROR('空白の項目があります。'); }
	if (length($FORM{'pname'}) >= 30 or length($FORM{'msname'}) >= 30){&ERROR('文字数がオーバーしています。');}
	if (length($FORM{'w'}) >= 2){&ERROR('その武器では登録できません');} 

	&HEADER;
	print << "	-----END-----";
	<style type="text/css">
		.td1{text-align:center;background-color:$TABLE_COLOR2;font-weight:bold;font-size:16px;}
	</style>
	<script language="JavaScript">
	function checkEntry(){if(confirm('登録名＆パスワードはメモしましたか？') == true){return true;}else{return false}
	}
	</script>
	<table width=100% height=100%><tr><td align=center>
	<div align=center style="font-size:55px;font-family:'細明朝体','ＭＳ Ｐ明朝';color:#505050;filter:alpha(opacity=100,finishopacity=0,style=2);height:60px;background-color:#fff0f0;"><b>新規登録</b></div>
	</td></tr><tr><td align=center>
	<table cellspacing=1 style="font-size:10pt;" bgcolor="$TABLE_COLOR1"><tr><td class=td1>名前</td>
	<td>$FORM{'pname'}<font style="font-size:12px;">（忘れないようにメモしておいてください）</font></td></tr>
	<tr><td class=td1>あなたのパスワード</td>
	<td>$FORM{'pass'}<font style="font-size:12px;">（忘れないようにメモしておいてください）</font></td></tr>
	<tr><td class=td1>国籍</td>
	<td>$FORM{'kuni'}</td></tr>
	<tr><td class=td1>アイコン</td>
	<td><img src=\"$IMG_FOLDER2/$FORM{'imgSelect'}.gif\"><font color=\"$FORM{'cl'}\">$FORM{'msname'}</font>
	</td></tr></table>
	<form action=$MAIN_SCRIPT method=POST target=\"_top\">
	<input type=hidden name=cmd value=RESIST>
	<input type=hidden name=pname value=$FORM{'pname'}>
	<input type=hidden name=msname value=$FORM{'msname'}>
	<input type=hidden name=msImg value=$FORM{'imgSelect'}>
	<input type=hidden name=msImg2 value=$FORM{'imgSelect2'}>
	<input type=hidden name=pass value=$FORM{'pass'}>
	<input type=hidden name=kuni value=$FORM{'kuni'}>
	<input type=hidden name=type value=$FORM{'type'}>
	<input type=hidden name=element value=$FORM{'element'}>
	<input type=hidden name=w value=$FORM{'w'}>
	<input type=hidden name=continent value=$FORM{'continent'}>
	<input type=hidden name=cl value=$FORM{'cl'}>
	<p align=center><input type=submit value=登録 onClick=\"return checkEntry()\">
	</form>
	<form action="$MAIN_SCRIPT?ENTRY" method=POST>
	<input type=submit value=作り直す></form>
	</td></tr><tr><td align=center>
	-----END-----
	&FOOTER;
	print "</td></tr></table></body>";
}
sub RESIST2 {
	require './vaback.pl';
	&backplayerlist;

	$ST5=(int(rand(10)+1)*100)+1000;$ST6=(int(rand(10))*5)+100;
	$ST1=int rand(5)+3;$ST2=int rand(5)+3;$ST3=int rand(5)+3;$ST4=int rand(5)+3;
		if ($FORM{'type'} == 0){$ST5+=2500;$ST1+=2;$ST6+=40;}
		 elsif ($FORM{'type'} == 1){$ST5+=2000;$ST2+=2;$ST6+=60;}
		 elsif ($FORM{'type'} == 93){$ST5+=2300;$ST2+=2;$ST6+=50;}
		 elsif ($FORM{'type'} == 44){$ST5+=1900;$ST1+=2;$ST6+=70;}

		$FORM{'continent'} = $FORM{'continent'} +1;
#		&ERROR("$FORM{'continent'}","あ$FORM{'imgSelect2'}");

	&LOCK;
	$pwd=crypt "$FORM{'pass'}",eb;
	dbmopen (%PL,"$DBM_P",0666);
		$PL{"$FORM{'pname'}"} = ("0 $DATE $pwd $FORM{'msname'} $FORM{'type'} $FORM{'kuni'} 0 noComment 0 $FORM{'w'}!0   50 $FORM{'cl'} 0 $ST5 $ST5 $ST6 $ST6 $ST1 $ST2 $ST3 $ST4 0 0 0 $DATE $FORM{'msImg'}  1 0 $FORM{'element'} 0 0 0 0 0 0  $FORM{'continent'} $FORM{'msImg2'}                    ");
	dbmclose (%PL);
	&UNLOCK;
	SET_COOKIE:{
		my @gmt = gmtime(time + $COOKIE_KEEP*24*60*60);
		$gmt[0] = sprintf("%02d", $gmt[0]);	$gmt[1] = sprintf("%02d", $gmt[1]);
		$gmt[2] = sprintf("%02d", $gmt[2]);	$gmt[3] = sprintf("%02d", $gmt[3]);	$gmt[5] += 1900;
		$gmt[4] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$gmt[4]];
		$gmt[6] = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$gmt[6]];
		my $date_gmt = "$gmt[6], $gmt[3]\-$gmt[4]\-$gmt[5] $gmt[2]:$gmt[1]:$gmt[0] GMT";
		my $cook = "pname:$FORM{'pname'},pass:$FORM{'pass'}";$SCKIE="Set-Cookie: EB=$cook; expires=$date_gmt\n";
	}
	print "HTTP/1.0 302 Moved Temporarily\n$SCKIE";
	print "Location: ./$MAIN_SCRIPT" . "\n\n";


}
sub PASSCHAN4 {
	&HEADER;
	@pair = split(/;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/,/, $DUMMY{EB});
		foreach (@pairs) {my($key, $value) = split(/:/, $_);$COOKIE{$key} = $value;}
	$NEWDATE=time;
	print << "	-----END-----";
	<script language="JavaScript">
		function checkRiyou (){
			if (document.pac.pname.value == '') {window.alert("IDが未入力です。");return false 
			}else if(document.pac.pass_old.value == '') {window.alert("旧パスワードが未入力です。");return false 
			}else if(document.pac.pass.value == '') {window.alert("新パスワードが未入力です。");return false 
			}else if(document.pac.pass2.value == '') {window.alert("確認用パスワードが未入力です。");return false 
			}else if(document.pac.pass.value != document.pac.pass2.value) {window.alert("確認のために入力された新パスワードが一致しません。");return false 
			}else {if (confirm('パスワードを変更します。') == true){return true;}else{return false}	}	
		}
	</script>
		<table width=100% height=100%><tr><td align=center>
		<table bgcolor=#000000 border=0 style="font-size:16px;">
			<tr><td colspan=2 bgcolor=#646464 align=center><img src=\"$IMG_FOLDER1/w.gif\"></td></tr>
			<tr><td colspan=2 bgcolor=#000000>パスワードを変更します。<br>
			忘れると再発行できませんので、変更したパスワードは忘れないようにしておいてください。<br><br></td></tr>
			<tr><td align=right style="height:21px; color:#ffffff; font-size:21px;">ユニットネーム<br>
					  旧パスワード<br>新パスワード<br>新パスワード</td>
				<td style="height:21px; color:#ffffff; font-size:16px;">
					<form action=$MAIN_SCRIPT method=POST target=_top name=pac onSubmit="return checkRiyou()">
					<input type=hidden name=cmd value=PASSCHAN>
					<input type=text size=20 name=pname value="$COOKIE{'pname'}" $STYLE_L><br>
					<input type=password size=15 name=pass_old $STYLE_L><br>
					<input type=password size=15 name=pass  maxlength="8" $STYLE_L>（半角英数８文字以内）<br>
					<input type=password size=15 name=pass2 maxlength="8" $STYLE_L>（確認のため上と同じパスをもう一度）<br>
					<input type=hidden name="scheck" value="$NEWDATE">
					</td></tr>
			<tr><td colspan=3><br><br><div align=center>変更しますか？<br><input type=submit value=\"変更\"></div>
			</td></tr>
			
		</table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub PASSCHAN3{
	&DBM_CONVERT('P',"$FORM{pname}");
	$psold = $FORM{'pass_old'};
	$pas1 = $FORM{'pass'};
	$pas2 = $FORM{'pass2'};
	if (($FORM{'scheck'} + 300) < time || $FORM{'scheck'} > time) {
		&ERROR('TimeOut','ボタンを押すのが遅すぎます。');
	} elsif ($pas1 =~ /\W/) {
		&ERROR('PwdError','新パスワードに英数字以外の文字が含まれています。');
	} elsif ( $pas1 ne '' && $pas1 ne $pas2 ){
		&ERROR('PwdError','確認のために入力された新パスワードが一致しません。');
	} elsif ( $psold eq '' ) {
		&ERROR('PwdError','旧パスワードも入力して下さい。');
	} elsif ( crypt ($psold,eb) ne "$PL_VALUES[2]" ){
		&ERROR('PwdError','旧パスワードが認証されませんでした。');
	} else {
	$PL_VALUES[2]=crypt "$pas1",eb;

	&LOCK;
	dbmopen (%P,"$DBM_P",0666);
	$P{"$FORM{'pname'}"}="@PL_VALUES";
	dbmclose %P;
	&UNLOCK;

	SET_COOKIE:{
		my @gmt = gmtime(time + $COOKIE_KEEP*24*60*60);
		$gmt[0] = sprintf("%02d", $gmt[0]);	$gmt[1] = sprintf("%02d", $gmt[1]);
		$gmt[2] = sprintf("%02d", $gmt[2]);	$gmt[3] = sprintf("%02d", $gmt[3]);	$gmt[5] += 1900;
		$gmt[4] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$gmt[4]];
		$gmt[6] = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$gmt[6]];
		my $date_gmt = "$gmt[6], $gmt[3]\-$gmt[4]\-$gmt[5] $gmt[2]:$gmt[1]:$gmt[0] GMT";
		my $cook = "pname:$FORM{'pname'},pass:$pas1";$SCKIE="Set-Cookie: EB=$cook; expires=$date_gmt\n";
	}
	print "HTTP/1.0 302 Moved Temporarily\n$SCKIE";
	print "Location: ./$MAIN_SCRIPT" . "\n\n";
	}
}
sub DELETE4 {
	&HEADER;
	@pair = split(/;/, $ENV{'HTTP_COOKIE'});
		foreach (@pair) {my($key, $value) = split(/=/, $_);$DUMMY{$key} = $value;}
	@pairs = split(/,/, $DUMMY{EB});
		foreach (@pairs) {my($key, $value) = split(/:/, $_);$COOKIE{$key} = $value;}
	$NEWDATE=time;
	print << "	-----END-----";
	<script language="JavaScript">
		function checkRiyou (){
			if (document.del.pname.value == '') {window.alert("IDが未入力です。");return false 
			}else if(document.del.pass.value == '') {window.alert("PASSが未入力です。");return false 
			}else {if (confirm('登録を抹消します。') == true){return true;}else{return false}	}	
		}
	</script>
		<table width=100% height=100%><tr><td align=center>
		<table bgcolor=#000000 border=0 style="font-size:12px;">
			<tr><td colspan=2 bgcolor=#646464 align=center><img src=\"$IMG_FOLDER1/w.gif\"></td></tr>
			<tr><td colspan=2 bgcolor=#000000>登録データを削除します。<br>
			削除したデータは復元する事が出来ません。<br><br></td></tr>
			<tr><td align=right style="height:21px; color:#ffffff; font-size:16px;">ユニットネーム<br>
					パスワード</td>
				<td style="height:21px; color:#ffffff; font-size:16px;">
					<form action=$MAIN_SCRIPT method=POST target=_top name=del onSubmit="return checkRiyou()">
					<input type=hidden name=cmd value=DELETE>
					<input type=text size=20 name=pname value="$COOKIE{'pname'}" $STYLE_L><br>
					<input type=password size=15 name=pass maxlength=8 $STYLE_L>
					<input type=hidden name="scheck" value="$NEWDATE">
					</td></tr>
			<tr><td colspan=3><br><br>削除しますか？<div align=center>
				<input type=submit value=\"削除\"></div>
			</td></tr>
			
		</table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub DELETE3{
		&ERROR('TimeOut','ボタンを押すのが遅すぎます。') if (($FORM{'scheck'} + 60) < time || $FORM{'scheck'} > time);
	$FlagE=0;
	&LOCK;
		dbmopen (%P,"$DBM_P",0666);
			@PL_VALUES = split(/\s/,$P{"$FORM{'pname'}"});
			$FlagE=1 if ($P{"$FORM{'pname'}"} && crypt("$FORM{'pass'}",eb) eq "$PL_VALUES[2]" && $FORM{'pass'} && $PL_VALUES[2]);
			delete $P{"$FORM{'pname'}"} if $FlagE==1;
		dbmclose %P;
	&UNLOCK;
	&ERROR('Error',"パスワードが間違っているか、COOKIEデータが破損している可能\性があります。\\n削除処理を中断します。") if $FlagE==0;
	rename "$LOG_FOLDER2/$FORM{'pname'}.cgi", "$LOG_FOLDER2/$FORM{'pname'}.bak";
	SET_COOKIE:{
		my @gmt = gmtime(time + $COOKIE_KEEP*24*60*60);
		$gmt[0] = sprintf("%02d", $gmt[0]);	$gmt[1] = sprintf("%02d", $gmt[1]);
		$gmt[2] = sprintf("%02d", $gmt[2]);	$gmt[3] = sprintf("%02d", $gmt[3]);	$gmt[5] += 1900;
		$gmt[4] = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$gmt[4]];
		$gmt[6] = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$gmt[6]];
		my $date_gmt = "$gmt[6], $gmt[3]\-$gmt[4]\-$gmt[5] $gmt[2]:$gmt[1]:$gmt[0] GMT";
		my $cook = "";$SCKIE="Set-Cookie: EB=$cook; expires=$date_gmt\n";
	}
	print "HTTP/1.0 302 Moved Temporarily\n$SCKIE";
	print "Location: ./$MAIN_SCRIPT" . "\n\n";


}

1;

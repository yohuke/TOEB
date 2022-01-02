############################# 個人図鑑 (txt式)#############################
#
#●このファイルを　zukan.cgi　でアップロード。ebs.cgiと同じフォルダ（階層）
#
#● zukan　という名前のフォルダをアップロード
#
#●ebs.cgiに追加
#
#	sub ZUKAN		{require 'zukan.cgi';&ZUKAN2;}
#	sub ETURAN		{require 'zukan.cgi';&ETURAN2;}
#	sub TOUROKU		{require 'zukan.cgi';&TOUROKU2;&ZUKAN;}
#
#
#●ボタン追加
#
#	＜sub3の場合＞
#
#	<td><input type=submit value="●●" $STYLE_B1 onClick="document.FM.cmd.value='ZUKAN';Move()"></td>
#
#	＜sub5の場合＞
#
#	$sp.= "<input type=\"submit\" value=\"●●\" $STYLE_B1 onClick=\"document.Ms.cmd.value='ZUKAN';\">";
#
#●登録時に武器はなくなりません。
#　なくすなら下の方のコメントアウトを2ヶ所外してください。
#
# このスクリプトに関しての質問等は、
# 迷惑がかかりますので他サイト様で質問しないよう願います。
# http://www4.plala.or.jp/at-s/ebs/
#<input type=submit value='戻る' $STYLE_B1 onClick="document.BM.target='Main';document.BM.cmd.value='MAIN_FRAME';parent.Sub.location.replace('$MAIN_SCRIPT?LOGO');">
####################################################################

@w_yobi=(9,10,11,38,41,42,43,46);	# $PL_VALUESの番号（登録可）
#@dame=('zzzz',"100a","102a","103a","104a","109a","116a","200a","231a","231aa","231aaa","231aaaa","269","270","273a","274a","275a","276a","277a","278a");		# 登録させない武器
@dame=('2fi',"2fj","102a","2hg","2hh","2hi","2hj","2hk","2hl","2ho","2hy","2ia","4gj","6ga","6gaa","6gab","6gac","6gad","6gae","1025a","1026a","1027a","1028a","1028aa","1031a","1031aa","1029a","1030a","1032a","1032aa","2gl","2gn","2go","2he","2hf","2ht");
$Z_DIR="hhhzukan304";		# 保存するディレクトリ（フォルダ）

require "./$LOG_FOLDER/$HASH_DATA";

######################## 設定ここまで ##############################

sub READ {
	open(IN,"<$_[0]");
	while (<IN>){
		chomp;
		push @ZUKAN,$_;
	}
	close(IN);
}
sub RADIO{
	my $radio='';
	$radio.="<input type=radio name=$_[0] value=$_[1]";
       	$radio.=" checked" if !$_[2];
	$radio.=">\n";
	return $radio;
}
sub JOUHOU {
	my $exp=$_[1]%$WEAPON_LVUP;
	my $lv=int($_[1]/$WEAPON_LVUP);
	my $name=(split /\,/,$WEAPON_LIST{"$_[0]"})[0];
	$namet=(split /\,/,$WEAPON_LIST{"$_[0]"})[7];

	#性能変化装備を取り扱う
	if($namet =~ m/!61/){
		@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
		$name=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
	}
	if($namet =~ m/!62/){
		@array=(ubag,ubah,ubai,ubaj,ubak,ubal);
		$name=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
	}
	if($namet =~ m/!63/){
		@array=(ubao,ubap,ubaq,ubar,ubas,ubat);
		$name=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
	}

	return "<b>$name</b>&nbsp;Lv.$lv/exp.$exp<br>\n";
}

sub ZUKAN2 {
	&ERROR('ディレクトリが見つかりません') unless (-e $Z_DIR);
	$LOG="$Z_DIR/$FORM{'pname'}\.txt";
	@ZUKAN=();
	&LOCK;
	&DBM_CONVERT('P',"$FORM{'pname'}");
	&READ($LOG) if (-e $LOG);
	&UNLOCK;
	&ERROR('パスワードエラー') if $PL_VALUES[2] ne crypt($FORM{'pass'},eb);
	my $num1=@ZUKAN;
	#my $num2=(keys %WEAPON_LIST)-@dame;
	$num2="？？？";
	my $yobi='';my $zflag=0;my @wep;
	my (%check_zukan,%check_dame);
	@check_zukan{@ZUKAN}=();
	@check_dame{@dame}=();
	foreach (@w_yobi){
		next if !$PL_VALUES[$_];
		@wep=split /!/,$PL_VALUES[$_];

		if($wep[0] eq "u"){
#		if($wep[7] =~ m/!61/){
			@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
			$wep[0]=$array[$PL_VALUES[31]];
#			$wep=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
		}
		if($wep[0] eq "ua"){
#		if($wep[7] =~ m/!62/){
			@array=(ubag,ubah,ubai,ubaj,ubak,ubal);
			$wep[0]=$array[$PL_VALUES[31]];
#			$wep=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
		}
		if($wep[0] eq "1ea"){
#		if($wep[7] =~ m/!63/){
			@array=(ubao,ubap,ubaq,ubar,ubas,ubat);
			$wep[0]=$array[$PL_VALUES[31]];
#			$wep=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
		}

		next if exists $check_zukan{$wep[0]};
		next if exists $check_dame{$wep[0]};
		$yobi.=&RADIO('touroku',$_,$zflag);
		$yobi.=&JOUHOU(@wep);
		$zflag++;
	}
	if ($zflag){
		$yobi.="<input type=submit value='登録' $STYLE_B1 onClick=\"document.BM.target='Sub';document.BM.cmd.value='TOUROKU';return checkZK()\">\n";
	}
	$yobi ||='登録できる武器がありません。';
	&HEADER;
	&JScfm(checkZK,"図鑑に登録します。よろしいですか？") if $zflag;
$Sort="<select size=1 name=\"sortlist\" $STYLE_B1>";
$Sort .="<option value=A01>全て</option>";
$Sort .="<option value=A02>武器</option>";
$Sort .="<option value=A03>防具</option>";
$Sort .="<option value=A33>道具</option>";
$Sort .="<option value=A10>剣</option>";
$Sort .="<option value=A11>斧</option>";
$Sort .="<option value=A12>槌</option>";
$Sort .="<option value=A13>爪</option>";
$Sort .="<option value=A14>扇</option>";
$Sort .="<option value=A15>杖</option>";
$Sort .="<option value=A16>槍</option>";
$Sort .="<option value=A17>人形</option>";
$Sort .="<option value=A18>鞭</option>";
$Sort .="<option value=A19>弓</option>";
$Sort .="<option value=A20>吹き矢</option>";
$Sort .="<option value=A21>銃</option>";
$Sort .="<option value=A22>刀</option>";
$Sort .="<option value=A23>突剣</option>";
$Sort .="<option value=A24>魔法</option>";
$Sort .="<option value=A25>特殊</option>";
$Sort .="<option value=A26>必殺技</option>";
$Sort .="<option value=A27>頭防具</option>";
$Sort .="<option value=A28>体防具</option>";
$Sort .="<option value=A29>盾</option>";
$Sort .="<option value=A30>装飾品</option>";
$Sort .="<option value=A31>その他</option>";
$Sort .="<option value=A32>本</option>";
$Sort .= "</select>";
	print <<"-----END-----";
<form action=$MAIN_SCRIPT name="BM" method="POST">
<input type=hidden name=cmd>
<input type=hidden name=pname value=$FORM{'pname'}>
<input type=hidden name=pass value=$FORM{'pass'}>
<table bordercolor=$TABLE_BORDER border=1 cellspacing=0 cellpadding=2 style="font-size:13px;">
<tr><th bgcolor=$TABLE_COLOR2>装備図鑑</th></tr>
<tr><td valign=top>$yobi</td></tr>
<tr><td align=right>
$Sort<b>（$num1/$num2）</b>&nbsp;
<input type=submit value='閲覧' $STYLE_B1 onClick="document.BM.target='Sub';document.BM.cmd.value='ETURAN'">
</td></tr>
</table>
</form>
-----END-----
	&FOOTER;
}
sub ETURAN2 {
	$LOG="$Z_DIR/$FORM{'pname'}\.txt";
	@ZUKAN=();
	&LOCK;
	&DBM_CONVERT('P',"$FORM{'pname'}");
	&READ($LOG) if (-e $LOG);
	&UNLOCK;
#	&ERROR($FORM{"sortlist"});
	&ERROR('パスワードエラー') if $PL_VALUES[2] ne crypt($FORM{'pass'},eb);
	sub KOUKA {
		my @W=split /\,/,$WEAPON_LIST{"$_[0]"};
		my $ritu=$W[2] > 100 ? 1 : $W[2]/100;

		my $point="???";

#		return;
	@COLOR = ('#5000CC','#5000CC','#8000ff','#a000e5','#bf00cc','#df00a6','#ff0080','#f7e957','#f7e957','#f7e957','#f7e957','#ff0080','#ff0080','#ff0080');

	@STATUS = ('G','F','E','D','C','B','A','H','S','SS','SSS','ACE','NT','Max');

	if($BattleLevel eq "1"){
		#最上段の武器
#		if($W[11] eq "0" && $W[14] =~ m/A02/){
#			$W[1] = int($W[1] * 0.97);
##			$W[2] = int($W[2] * 0.97);
#		}
		#技
#		if($W[11] eq "5"){
#			$W[1]-=50;
#		}
		#魔法
		if($W[11] eq "1" || $W[11] eq "2" || $W[11] eq "3"){
			$W[1] = int($W[1]*0.9);
#			$W[2] = int($W[2]*0.95);
		}
		#特殊
		if($W[11] eq "6" || $W[11] eq "7" || $W[11] eq "8"){
			$W[1] = int($W[1]*0.93);
#			$W[2] = int($W[2]*0.97);
		}
	}

#	$c = int(($W[1]*$W[3]-50)/100);
#	if($c < 0){$c = 0;}
#	if($c > 10){$c = 13;}
	$c = &STATUS_CONVERT($W[1]*$W[3]/500,'s');

#	$d = int($W[2]/20);
	$d = &STATUS_CONVERT($W[2]/4,'s');
#	if($d < 0){$d = 0;}
#	if($d > 10){$d = 13;}
#		my $kougeki=$STATUS[$c];
#		my $meichuu=$STATUS[$d];
		my $kouka;
		my $eres;
		my $estr;
		my $eint;
		my $eini;
		my $edex;
		my $eagi;
		my $BMsg;

		#盾
		if($W[7]=~ m/!12/){
			$eres=int($W[1]);
		#指輪
		}elsif ($W[7] =~ m/!13/){
			$estr=int($W[10]);
			$edex=int($W[1]);
		#オーブ
		}elsif ($W[7] =~ m/!14/){
			$eini=int($W[10]);
		#杖・扇
		}elsif ($W[7] =~ m/!15|!19/){
			$eint=int($W[10]);
		#靴
		}elsif ($W[7] =~ m/!16/){
			$eagi=int($W[1]);
		#装飾品
		}elsif ($W[7] =~ m/!17/){
			$eagi=int($W[1]);
			$edex=int($W[10]);
		#体防具1
		}elsif ($W[7] =~ m/!1s/){
			$eres=int($W[1]);
		#頭防具1
		}elsif ($W[7] =~ m/!1t/){
			$eres=int($W[1]);
		#頭防具2
		}elsif ($W[7] =~ m/!E0003/){
			$eres=int($W[1]);
			$estr=int(3);
			$eagi=int(1);
		#体防具2
		}elsif ($W[7] =~ m/!1u/){
			$eres=int($W[1]);
			$edex=int($W[1]/3);
		#頭防具3
		}elsif ($W[7] =~ m/!1v/){
			$eres=int($W[1]);
			$eagi=int($W[10]);
		#体防具3
		}elsif ($W[7] =~ m/!1w/){
			$eres=int($W[1]);
			$eint=int($W[10]);
		#頭防具4
		}elsif ($W[7] =~ m/!1x/){
			$eres=int($W[1]);
			$eint=int($W[10]);
		}

		if($eres > 0){
			$BMsg .= " RES+$eres"
		}
		if($estr > 0){
			$BMsg .= " STR+$estr"
		}
		if($eint > 0){
			$BMsg .= " INT+$eint"
		}
		if($eini > 0){
			$BMsg .= " Ini+$eini"
		}
		if($edex > 0){
			$BMsg .= " DEX+$edex"
		}
		if($eagi > 0){
			$BMsg .= " AGI+$eagi"
		}

		if ($W[7]){
			$kouka.="片手&nbsp;" if $W[7] =~ m/!10/;
			$kouka.="両手&nbsp;" if $W[7] =~ m/!11/;
			$kouka.="盾&nbsp;" if $W[7] =~ m/!12/;
			$kouka.="指輪&nbsp;" if $W[7] =~ m/!13/;
			$kouka.="オーブ&nbsp;" if $W[7] =~ m/!14/;
			$kouka.="杖&nbsp;" if $W[7] =~ m/!15/;
			$kouka.="靴&nbsp;" if $W[7] =~ m/!16/;
			$kouka.="装飾品&nbsp;" if $W[7] =~ m/!17/;
			$kouka.="魔法&nbsp;" if $W[7] =~ m/!18/;
			$kouka.="扇&nbsp;" if $W[7] =~ m/!19/;
			$kouka.="弓&nbsp;" if $W[7] =~ m/!1a/;
			$kouka.="銃&nbsp;" if $W[7] =~ m/!1b/;
			$kouka.="魔道書&nbsp;" if $W[7] =~ m/!1c/;
			$kouka.="合成&nbsp;" if $W[7] =~ m/!1d/;
			$kouka.="槍&nbsp;" if $W[7] =~ m/!1e/;
			$kouka.="鞭&nbsp;" if $W[7] =~ m/!1f/;
			$kouka.="吹き矢&nbsp;" if $W[7] =~ m/!1g/;
			$kouka.="召喚&nbsp;" if $W[7] =~ m/!1h/;
			$kouka.="ドラゴンブレス&nbsp;" if $W[7] =~ m/!1k/;
			$kouka.="魔獣スペシャル&nbsp;" if $W[7] =~ m/!1l/;
			$kouka.="財宝&nbsp;" if $W[7] =~ m/!1m/;
			$kouka.="消耗品&nbsp;" if $W[7] =~ m/!1n/;
			$kouka.="携帯品&nbsp;" if $W[7] =~ m/!1o/;
			$kouka.="ドール&nbsp;" if $W[7] =~ m/!1p/;
			$kouka.="補助&nbsp;" if $W[7] =~ m/!1q/;
			$kouka.="竜言語&nbsp;" if $W[7] =~ m/!1r/;
			$kouka.="体防具&nbsp;" if $W[7] =~ m/!1s|!1u|!1w|!E0001/;
			$kouka.="頭防具&nbsp;" if $W[7] =~ m/!1t|!1v|!1x|!E0003/;
			$kouka.="道具&nbsp;" if $W[14] =~ m/A33/;
		}else{$kouka="&nbsp;";}

		my $kouka1;
		if ($W[7]){
			$kouka1.="<img src=\"$IMG_FOLDER1/d0.gif\">&nbsp;" if $W[7] =~ m/!00/;
			$kouka1.="<img src=\"$IMG_FOLDER1/d1.gif\">&nbsp;" if $W[7] =~ m/!01/;
			$kouka1.="<img src=\"$IMG_FOLDER1/d2.gif\">&nbsp;" if $W[7] =~ m/!02/;
			$kouka1.="<img src=\"$IMG_FOLDER1/d3.gif\">&nbsp;" if $W[7] =~ m/!03/;
			$kouka1.="<img src=\"$IMG_FOLDER1/d4.gif\">&nbsp;" if $W[7] =~ m/!04/;
			$kouka1.="<img src=\"$IMG_FOLDER1/d5.gif\">&nbsp;" if $W[7] =~ m/!05/;
		}else{$kouka1="&nbsp;";}

		my $kouka2;
		if ($W[7]){
			$kouka2.="渾身&nbsp;" if $W[7] =~ m/!20/;
			$kouka2.="必殺&nbsp;" if $W[7] =~ m/!21/;
			$kouka2.="攻↓&nbsp;" if $W[7] =~ m/!22/;
			$kouka2.="防↓&nbsp;" if $W[7] =~ m/!23/;
			$kouka2.="避↓&nbsp;" if $W[7] =~ m/!24/;
			$kouka2.="命↓&nbsp;" if $W[7] =~ m/!25/;
			$kouka2.="防↑&nbsp;" if $W[7] =~ m/!26/;
			$kouka2.="避↑&nbsp;" if $W[7] =~ m/!27/;
			$kouka2.="怒り&nbsp;" if $W[7] =~ m/!28/;
			$kouka2.="恨み&nbsp;" if $W[7] =~ m/!29/;
			$kouka2.="呪い&nbsp;" if $W[7] =~ m/!2a/;
			$kouka2.="毒&nbsp;" if $W[7] =~ m/!2b/;
			$kouka2.="麻痺&nbsp;" if $W[7] =~ m/!2c/;
			$kouka2.="睡眠&nbsp;" if $W[7] =~ m/!2d/;
			$kouka2.="石化&nbsp;" if $W[7] =~ m/!2e/;
			$kouka2.="魅了&nbsp;" if $W[7] =~ m/!2f/;
			$kouka2.="ノックバック&nbsp;" if $W[7] =~ m/!2g/;
			$kouka2.="方向転換&nbsp;" if $W[7] =~ m/!2h/;
			$kouka2.="MHP↓&nbsp;" if $W[7] =~ m/!2j/;
			$kouka2.="MP↓&nbsp;" if $W[7] =~ m/!2k/;
			$kouka2.="パワーダウン&nbsp;" if $W[7] =~ m/!2o/;
			$kouka2.="パワーアップ&nbsp;" if $W[7] =~ m/!2p/;
			$kouka2.="パワーダウン付与&nbsp;" if $W[7] =~ m/!2q/;
			$kouka2.="パワーアップ付与&nbsp;" if $W[7] =~ m/!2r/;
			$kouka2.="エレメントブレイク&nbsp;" if $W[7] =~ m/!2s/;
			$kouka2.="SP_short&nbsp;" if $W[7] =~ m/!30/;
			$kouka2.="SP_middle&nbsp;" if $W[7] =~ m/!31/;
			$kouka2.="SP_long&nbsp;" if $W[7] =~ m/!32/;
			$kouka2.="渾身無効&nbsp;" if $W[7] =~ m/!40/;
			$kouka2.="必殺無効&nbsp;" if $W[7] =~ m/!41/;
			$kouka2.="怒り無効&nbsp;" if $W[7] =~ m/!42/;
			$kouka2.="恨み無効&nbsp;" if $W[7] =~ m/!43/;
			$kouka2.="呪い無効&nbsp;" if $W[7] =~ m/!44/;
			$kouka2.="毒無効&nbsp;" if $W[7] =~ m/!45/;
			$kouka2.="麻痺無効&nbsp;" if $W[7] =~ m/!46/;
			$kouka2.="睡眠無効&nbsp;" if $W[7] =~ m/!47/;
			$kouka2.="石化無効&nbsp;" if $W[7] =~ m/!48/;
			$kouka2.="魅了無効&nbsp;" if $W[7] =~ m/!49/;
			$kouka2.="状態異常無効&nbsp;" if $W[7] =~ m/!4a/;
			$kouka2.="レジスト&nbsp;" if $W[7] =~ m/!4b/;
			$kouka2.="超神聖&nbsp;" if $W[7] =~ m/!50/;
			$kouka2.="オウガシリーズ&nbsp;" if $W[7] =~ m/!51/;
			$kouka2.="暗黒魔導器&nbsp;" if $W[7] =~ m/!52/;
			$kouka2.="狩人必須装備&nbsp;" if $W[7] =~ m/!53/;
			$kouka2.="剣道具&nbsp;" if $W[7] =~ m/!54/;
			$kouka2.="お菓子&nbsp;" if $W[7] =~ m/!55/;
			$kouka2.="冥界四武具&nbsp;" if $W[7] =~ m/!56/;
			$kouka2.="少年の魂&nbsp;" if $W[7] =~ m/!57/;
			$kouka2.="少女の魂&nbsp;" if $W[7] =~ m/!58/;
			$kouka2.="即死&nbsp;" if $W[7] =~ m/!60/;
			$kouka2.="属性ブレス&nbsp;" if $W[7] =~ m/!61/;
			$kouka2.="属性上位ブレス&nbsp;" if $W[7] =~ m/!62/;
			$kouka2.="コッレクティオ&nbsp;" if $W[7] =~ m/!63/;
			$kouka2.="シャイニング&nbsp;" if $W[7] =~ m/!64/;
			$kouka2.="ドラッグイーター&nbsp;" if $W[7] =~ m/!65/;
			$kouka2.="パンプキンボム&nbsp;" if $W[7] =~ m/!66/;
			$kouka2.="かぼちゃうぉーず&nbsp;" if $W[7] =~ m/!67/;
			$kouka2.="アシェルム&nbsp;" if $W[7] =~ m/!68/;
			$kouka2.="ワードオブペイン&nbsp;" if $W[7] =~ m/!69/;
			$kouka2.="対魔法&nbsp;" if $W[7] =~ m/!6a/;
			$kouka2.="ライフブレイク&nbsp;" if $W[7] =~ m/!6b/;
			$kouka2.="説得&nbsp;" if $W[7] =~ m/!6c/;
			$kouka2.="命名権&nbsp;" if $W[7] =~ m/!6f/;
			$kouka2.="エンジェルナイト召喚&nbsp;" if $W[7] =~ m/!6g/;
			$kouka2.="Special&nbsp;" if $W[7] =~ m/!6h/;
			$kouka2.="魔法のラッパ&nbsp;" if $W[7] =~ m/!6i/;
			$kouka2.="ヒーリング&nbsp;" if $W[7] =~ m/!6j/;
			$kouka2.="ヒーリングオール&nbsp;" if $W[7] =~ m/!6k/;
			$kouka2.="リザレクション&nbsp;" if $W[7] =~ m/!6l/;
			$kouka2.="チャージスペル&nbsp;" if $W[7] =~ m/!6m/;
			$kouka2.="オーヴァードライヴ&nbsp;" if $W[7] =~ m/!6n/;
			$kouka2.="回復&nbsp;" if $W[7] =~ m/!6o/;
			$kouka2.="マスタバの結界&nbsp;" if $W[7] =~ m/!6p/;
			$kouka2.="マーチングバトン&nbsp;" if $W[7] =~ m/!6q/;
			$kouka2.="武芸指南書&nbsp;" if $W[7] =~ m/!6r/;
			$kouka2.="decrease&nbsp;" if $W[7] =~ m/!6s/;
			$kouka2.="トランスファー&nbsp;" if $W[7] =~ m/!6t/;
			$kouka2.="手加減&nbsp;" if $W[7] =~ m/!6u/;
			$kouka2.="リバイバル&nbsp;" if $W[7] =~ m/!6v/;
			$kouka2.="必殺技&nbsp;" if $W[7] =~ m/!6w/;
			$kouka2.="メルトダウン&nbsp;" if $W[7] =~ m/!6x/;
			$kouka2.="オールサモンズ&nbsp;" if $W[7] =~ m/!6y/;
			$kouka2.="ヒーリングプラス&nbsp;" if $W[7] =~ m/!6z/;
			$kouka2.="テレポート&nbsp;" if $W[7] =~ m/!70/;
			$kouka2.="ゼテギネア大陸限定ドロップ&nbsp;" if $W[7] =~ m/!71/;
			$kouka2.="ガリシア大陸限定ドロップ&nbsp;" if $W[7] =~ m/!72/;
			$kouka2.="LvUP時MP回復&nbsp;" if $W[7] =~ m/!73/;
			$kouka2.="リジェネレイト&nbsp;" if $W[7] =~ m/!74/;
			$kouka2.="恐怖&nbsp;" if $W[7] =~ m/!75/;
			$kouka2.="ヒーリングプラス&nbsp;" if $W[7] =~ m/!76/;
			$kouka2.="ネクロマンシー&nbsp;" if $W[7] =~ m/!77/;
			$kouka2.="マーシーレイン&nbsp;" if $W[7] =~ m/!78/;
			$kouka2.="マーティライズ&nbsp;" if $W[7] =~ m/!79/;
			$kouka2.="1500ヒール&nbsp;" if $W[7] =~ m/!80/;
			$kouka2.="リキュバレイト&nbsp;" if $W[7] =~ m/!81/;
			$kouka2.="MP100チャージ&nbsp;" if $W[7] =~ m/!82/;
			$kouka2.="デフハーネラ&nbsp;" if $W[7] =~ m/!83/;
			$kouka2.="デフゾショネル&nbsp;" if $W[7] =~ m/!84/;
			$kouka2.="デフバーサ&nbsp;" if $W[7] =~ m/!85/;
			$kouka2.="デフグルーザ&nbsp;" if $W[7] =~ m/!86/;
			$kouka2.="サモンイシュタル&nbsp;" if $W[7] =~ m/!87/;
			$kouka2.="サモンアスモデ&nbsp;" if $W[7] =~ m/!88/;
			$kouka2.="サモンゾショネル&nbsp;" if $W[7] =~ m/!89/;
			$kouka2.="サモングルーザ&nbsp;" if $W[7] =~ m/!8a/;
			$kouka2.="サモンハーネラ&nbsp;" if $W[7] =~ m/!8b/;
			$kouka2.="サモンバーサ&nbsp;" if $W[7] =~ m/!8c/;
			$kouka2.="部隊攻撃&nbsp;" if $W[7] =~ m/!8d/;
			$kouka2.="ジャンプウォール&nbsp;" if $W[7] =~ m/!8e/;
			$kouka2.="テレポート&nbsp;" if $W[7] =~ m/!8f/;
			$kouka2.="補助魔法&nbsp;" if $W[7] =~ m/!8g/;
			$kouka2.="竜言語&nbsp;" if $W[7] =~ m/!8h/;
			$kouka2.="マーシーレイン&nbsp;" if $W[7] =~ m/!8i/;
			$kouka2.="マーティライズ&nbsp;" if $W[7] =~ m/!8j/;
			$kouka2.="スタンスローター&nbsp;" if $W[7] =~ m/!8k/;
			$kouka2.="スランバーミスト&nbsp;" if $W[7] =~ m/!8l/;
			$kouka2.="ポイズンクラウド&nbsp;" if $W[7] =~ m/!8m/;
			$kouka2.="ペトロクラウド&nbsp;" if $W[7] =~ m/!8n/;
			$kouka2.="キュアリーフ[HP4000回復]&nbsp;" if $W[7] =~ m/!E0015/;
			$kouka2.="キュアシード[HP12000回復]&nbsp;" if $W[7] =~ m/!E0016/;
			$kouka2.="キュアペースト[HP36000回復]&nbsp;" if $W[7] =~ m/!E0017/;
			$kouka2.="キュアエキス[HP全回復]&nbsp;" if $W[7] =~ m/!E0018/;
			$kouka2.="マジックリーフ[MP150回復]&nbsp;" if $W[7] =~ m/!E0019/;
			$kouka2.="マジックシード[MP400回復]&nbsp;" if $W[7] =~ m/!E0020/;
			$kouka2.="マジックペースト[MP900回復]&nbsp;" if $W[7] =~ m/!E0021/;
			$kouka2.="マジックエキス[MP1500回復]&nbsp;" if $W[7] =~ m/!E0022/;
			$kouka2.="賢者の果実[HP25000&nbsp;MP800回復]&nbsp;" if $W[7] =~ m/!E0023/;
			$kouka2.="天使の果実[HPMP全回復]&nbsp;" if $W[7] =~ m/!E0024/;
			$kouka2.="腐りかけた果実[自身の所属する部隊全員のHP回復&nbsp;自身は戦闘不能\]&nbsp;" if $W[7] =~ m/!E0025/;
			$kouka2.="竜の巣[能\動戦闘時自動消費&nbsp;戦闘中の水・風属性ダメージ+20％]&nbsp;" if $W[7] =~ m/!E0026/;
			$kouka2.="オベロンの涙[能\動戦闘時自動消費&nbsp;戦闘中の炎・大地属性ダメージ+20％]&nbsp;" if $W[7] =~ m/!E0027/;
			$kouka2.="蛮族の角笛[能\動戦闘時自動発動&nbsp;戦闘中の水・風属性ダメージ+5％]&nbsp;" if $W[7] =~ m/!E0028/;
			$kouka2.="サンゴの竪琴[能\動戦闘時自動消費&nbsp;戦闘中の炎・大地属性ダメージ+5％]&nbsp;" if $W[7] =~ m/!E0029/;
			$kouka2.="リバイブストーン[石化効果を受けた際に自動消費&nbsp;石化無効化]&nbsp;" if $W[7] =~ m/!E0030/;
			$kouka2.="アンチドーテ[毒効果を受けた際に自動消費&nbsp;毒無効化]&nbsp;" if $W[7] =~ m/!E0031/;
			$kouka2.="パラブリージア[麻痺効果を受けた際に自動消費&nbsp;麻痺無効化]&nbsp;" if $W[7] =~ m/!E0032/;
			$kouka2.="アウェイキング[眠り効果を受けた際に自動消費&nbsp;眠り無効化]&nbsp;" if $W[7] =~ m/!E0033/;
			$kouka2.="精霊の果実[状態異常効果を受けた際に自動消費&nbsp;状態異常無効化]&nbsp;" if $W[7] =~ m/!E0034/;
			$kouka2.="祝福の聖石[能\動戦闘で戦闘不能\時自動消費&nbsp;戦闘不能\回復]&nbsp;" if $W[7] =~ m/!E0035/;
			$kouka2.="至福の聖石[能\動戦闘で戦闘不能\時自動消費&nbsp;戦闘不能\完全回復]&nbsp;" if $W[7] =~ m/!E0036/;
			$kouka2.="完全回避アップ&nbsp;" if $W[7] =~ m/!E0037/;
			$kouka2.="魔法強化&nbsp;" if $W[7] =~ m/!E0038/;
			$kouka2.="L・N恐怖付与&nbsp;" if $W[7] =~ m/!E0039/;

			$kouka2.="フラグ&nbsp;" if $W[7] =~ m/!zc/;
			$kouka2.="デスペナルティ&nbsp;" if $W[7] =~ m/!zd/;
			$kouka2.="ダミーコード&nbsp;" if $W[7] =~ m/!xx/;
#			$kouka2.="&nbsp;" if $W[7] =~ m/!8s/;
		}else{$kouka2="&nbsp;";}

		$kouka2.=$BMsg;

		if($kouka eq ""){$kouka = "　";}
		if($kouka1 eq ""){$kouka1 = "　";}
		if($kouka2 eq ""){$kouka2 = "　";}

		$icon = "<img src=\"$IMG_FOLDER4/$W[9].gif\">";

		if($W[9] eq ""){$icon = "　";}

		return ($icon,$W[0],$c,$d,$W[3],$W[4],$W[5],$kouka,$kouka1,$kouka2,$W[14]);
	}
	my @data=map {[&KOUKA($_)]} @ZUKAN;
	@data=sort {$b->[0] <=> $a->[0] || $a->[1] cmp $b->[1]} @data;

	my $HEAD="<table bgcolor=$TABLE_COLOR1 border bordercolor=$TABLE_BORDER cellpadding=2 cellspacing=0 style=\"font-size:13px;\">\n<tr bgcolor=$TABLE_COLOR1><th nowrap>アイコン</th><th width=220>武器名</th><th nowrap>攻撃</th><th nowrap>命中</th><th nowrap>回</th><th nowrap>消費MP</th><th nowrap>価格</th><th>種類</th><th>属性</th><th>特殊効果</th></tr>\n";
	&HEADER;
	my $i=0;
	foreach (@data){
		@wep=@{$_};
		print $HEAD if $i%20 == 0;
		if($wep[10] =~ m/$FORM{"sortlist"}/){
		print "<tr><td align=center>$wep[0]</td><td>$wep[1]</td><td align=center>$wep[2]</td><td align=center>$wep[3]</td><td align=right>$wep[4]</td><td align=right>$wep[5]</td><td align=right>$wep[6]</td><td>$wep[7]</td><td align=center>$wep[8]</td><td>$wep[9]</td></tr>\n";
		}
		$i++;
		print "</table>\n" if $i%20 == 0;
	}
	print "</table>\n" if $i%20 != 0;


	#ここで、集めた数をカウントする
#コレクトランキング用
		#ランキング用 アイテム収集数　0はアイテム獲得　1はMVP　2はアイテム収集
#	&LOCK;
#	&DBM_CONVERT('P',"$FORM{'pname'}");
#	&UNLOCK;
		@RC=split(/!/,$PL_VALUES[47]);
		if($RC[2] eq ""){$RC[2] = 0;}
		if($RC[2] ne $i){
			$RC[2] = $i;
			$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";

			&LOCK;
			dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;# 登録時武器をなくす
			&UNLOCK;

		}
	print <<"-----END-----";
<form action=$MAIN_SCRIPT method=POST target=Sub>
<input type=hidden name=cmd value=ZUKAN>
<input type=hidden name=pname value=$FORM{'pname'}>
<input type=hidden name=pass value=$FORM{'pass'}>
<input type=submit value='戻る' $STYLE_B1>
</form>
-----END-----
	&FOOTER;
}

sub TOUROKU2 {
	$LOG="$Z_DIR/$FORM{'pname'}\.txt";
	@ZUKAN=();
	&LOCK;
	&DBM_CONVERT('P',"$FORM{'pname'}");
	&READ($LOG) if (-e $LOG);
	&UNLOCK;
	&ERROR('パスワードエラー') if $PL_VALUES[2] ne crypt($FORM{'pass'},eb);
	&ERROR('登録エラー') if !$PL_VALUES[$FORM{'touroku'}];
	my $wid=(split /!/,$PL_VALUES[$FORM{'touroku'}])[0];
#	my $wid=(split /!/,$PL_VALUES[$FORM{'touroku'}])[0];
#	my $widt=(split /\,/,$WEAPON_LIST{"$wid"})[7];
#@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
#&ERROR("$widあ$array[$PL_VALUES[31]]");
	#性能変化装備を取り扱う
	if($wid eq "u"){
		@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
#		$wid=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
		$wid=$array[$PL_VALUES[31]];
	}
	if($wid eq "ua"){
		@array=(ubag,ubah,ubai,ubaj,ubak,ubal);
#		$wid=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
		$wid=$array[$PL_VALUES[31]];
	}
	if($wid eq "1ea"){
		@array=(ubao,ubap,ubaq,ubar,ubas,ubat);
#		$wid=(split /\,/,$WEAPON_LIST{"$array[$PL_VALUES[31]]"})[0];
		$wid=$array[$PL_VALUES[31]];
	}

	my (%check_zukan,%check_dame);
	@check_zukan{@ZUKAN}=();
	@check_dame{@dame}=();
	&ERROR('すでに登録されています。') if exists $check_zukan{$wid};
	&ERROR('この武器は登録できません。') if exists $check_dame{$wid};

	my $xxx=@ZUKAN;
#	&ERROR($xxx);
#コレクトランキング用
		@RC=split(/!/,$PL_VALUES[47]);
		if($RC[2] eq ""){$RC[2] = 0;}
		$RC[2] = $xxx + 1;
		$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";

#		&LOCK;
#		dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;# 登録時武器をなくす
#		&UNLOCK;


#	$PL_VALUES[$FORM{'touroku'}]='';# 登録時武器をなくす
	push @ZUKAN,$wid;
	my %temp=();
	foreach (@ZUKAN){
		next if $_ eq '' || !$WEAPON_LIST{$_} || exists $check_dame{$_};
		$temp{$_}=1;
	}
	@ZUKAN=keys %temp;
	&LOCK;
	dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;# 登録時武器をなくす →20090621　304　ランキング数登録用に変更
	open(OUT,">$LOG");print OUT "$_\n" for @ZUKAN;close(OUT);
	&UNLOCK;
}

1;


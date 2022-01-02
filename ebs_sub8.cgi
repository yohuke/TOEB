sub BALANCE{

	&HEADER;
	&DBM_INPORT(P);&DBM_INPORT(C);
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
		<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>勢力図</b></center></td></tr>
		
	-----END-----
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>国名</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>総帥</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>人口比率</td><td nowrap bgcolor=\"$TABLE_COLOR2\">人口</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>滅ぼした国</td></tr>";

$i=0;
while (my($key,$val) = each %C){
@VALS = split(/\s/,$val);
$CNAME[$i]=$key;
$CCOLOR[$i]=$VALS[0];
$METUC[$i]=$VALS[13];
$i++;
}
$count=$i-1;$NONCOUNT=0;$METUBOU=0;
while (my($key2,$val2) = each %P){
@VALS = split(/\s/,$val2);$ET++;
   $j=0;$kuni=0;
   foreach(0..$count) {
   
   	if($VALS[5] eq "$CNAME[$j]"){
		$COUNTER[$j]++;$kuni=1;
		if($VALS[6]==1){$SOUSUI[$j]=$key2;}
	}
   $j++;
   }
   if($VALS[5] eq ''){$NONCOUNT++;}elsif($kuni==0){$METUBOU++;}
}
$k=0;
foreach(0..$count) {
$BAR[$k]=$COUNTER[$k]*3;$WARIAI=int($COUNTER[$k]/$ET*100);
if($SOUSUI[$k] eq ''){$SOUSUI[$k]="<font color=black>不在</font>";}
if($COUNTER[$k] eq ''){$COUNTER[$k]="0";}
	$DECLT=int($METUC[$k]/10);$DECL=$METUC[$k]-$DECLT*10;
	for ($h=1;$h<=$DECLT;$h++){$METUP[$k].="<img src=\"$IMG_FOLDER2/1000.gif\" width=\"16\" height=\"16\">";}
	for ($h=1;$h<=$DECL;$h++){$METUP[$k].="<img src=\"$IMG_FOLDER2/1000.gif\" width=\"8\" height=\"8\">";}
print "<tr><td nowrap align=center bgcolor=$CCOLOR[$k]><font color=BLACK>$CNAME[$k]</font></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$SOUSUI[$k]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[$k]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[$k]名</td><td nowrap bgcolor=\"$TABLE_COLOR1\">$METUP[$k]</td></tr>";
$k++;
}
$NONBAR=$NONCOUNT*3;$NONWARIAI=int($NONCOUNT/$ET*100);
$BOUBAR=$METUBOU*3;$BOUWARIAI=int($METUBOU/$ET*100);
#print "<tr><td nowrap align=center>$NONE_NATIONALITY</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gbez.gif\" hspace=0 height=7 width=$NONBAR></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$NONWARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$NONCOUNT名</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td></tr>";
#print "<tr><td nowrap align=center bgcolor=BLACK>亡国</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gbez.gif\" hspace=0 height=7 width=$BOUBAR></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$BOUWARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$METUBOU名</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td></tr>";
print "<tr><td nowrap align=center>$NONE_NATIONALITY</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td><td nowrap bgcolor=\"$TABLE_COLOR1\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$NONWARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$NONCOUNT名</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td></tr>";
print "<tr><td nowrap align=center bgcolor=BLACK>亡国</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td><td nowrap bgcolor=\"$TABLE_COLOR1\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$BOUWARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$METUBOU名</td><td nowrap bgcolor=\"$TABLE_COLOR1\">　</td></tr>";

	print << "	-----END-----";
 	</table>
	-----END-----
	print "<BR>勢力図\表\示：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a>";
	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub BALANCE5{

	&HEADER;
	&DBM_INPORT(P);&DBM_INPORT(C);
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
		<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=4><center><b>勢力図</b></center></td></tr>
		
	-----END-----
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>武器名</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>割合</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>人口比率</td></tr>";

	require "./$LOG_FOLDER/_hash.data";
$i=0;
while (my($key,$val) = each %WEAPON_LIST){
	@VALS = split(/\s/,$val);
	$awn[$i]=$key;
	$i++;
}

$count=$i-1;$NONCOUNT=0;
while (my($key2,$val2) = each %P){
	@VALS = split(/\s/,$val2);$ET++;
	   $j=0;$kuni=0;
	   foreach(0..$count) {
		local($WN_A,$WLV_A) = split(/!/,$VALS[9]);
		local($WN_B,$WLV_B) = split(/!/,$VALS[10]);
		local($WN_C,$WLV_C) = split(/!/,$VALS[11]);
		local($WN_D,$WLV_D) = split(/!/,$VALS[38]);
		local($WN_S,$WLV_S) = split(/!/,$VALS[41]);
		local($WN_T,$WLV_T) = split(/!/,$VALS[42]);
		local($WN_U,$WLV_U) = split(/!/,$VALS[43]);
	   	if($WN_A eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   	if($WN_B eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   	if($WN_C eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   	if($WN_D eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   	if($WN_S eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   	if($WN_T eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   	if($WN_U eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   $j++;
	   }
}

$k=0;
foreach(0..$count) {
$BAR[$k]=$COUNTER[$k]*3;$WARIAI=int($COUNTER[$k]/$ET*100);
@wname_sa=split(/\,/,$WEAPON_LIST{"$awn[$k]"});
print "<tr><td nowrap align=center bgcolor=\"$TABLE_COLOR1\"><font color=#dddddd>$wname_sa[0]</font></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[$k]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[$k]名</td></tr>" if $COUNTER[$k];
$k++;
}



	print << "	-----END-----";
 	</table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";
}

sub BALANCE2{

	&HEADER;
	&DBM_INPORT(R);
	@R_VALUES = split(/\s/,$R{"server"});

	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
	<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=2><center><b>304 Edition系譜</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>戦闘回数</b></center></td><td><center><b>$R_VALUES[0]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>勝利</b></center></td><td><center><b>$R_VALUES[1]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>敗北</b></center></td><td><center><b>$R_VALUES[2]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ON狩り</b></center></td><td><center><b>$R_VALUES[3]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>滅亡国数</b></center></td><td><center><b>$R_VALUES[4]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ダメージ</b></center></td><td><center><b>$R_VALUES[5]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被ダメージ</b></center></td><td><center><b>$R_VALUES[6]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>武器獲得数</b></center></td><td><center><b>$R_VALUES[7]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>goth</b></center></td><td><center><b>$R_VALUES[8]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>経験値</b></center></td><td><center><b>$R_VALUES[9]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>建国数</b></center></td><td><center><b>$R_VALUES[155]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>戦略数</b></center></td><td><center><b>$R_VALUES[156]</b></center></td></tr>

	<tr bgcolor="$TABLE_COLOR1"><td><center><b>国費</b></center></td><td><center><b>$R_VALUES[66]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>攻↓</b></center></td><td><center><b>$R_VALUES[67] $R_VALUES[126]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>防↓</b></center></td><td><center><b>$R_VALUES[68] $R_VALUES[127]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>避↓</b></center></td><td><center><b>$R_VALUES[69] $R_VALUES[128]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>命↓</b></center></td><td><center><b>$R_VALUES[70] $R_VALUES[129]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>怒り</b></center></td><td><center><b>$R_VALUES[10] $R_VALUES[11]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>渾身</b></center></td><td><center><b>$R_VALUES[71] $R_VALUES[103]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被渾身</b></center></td><td><center><b>$R_VALUES[72] $R_VALUES[104]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>必殺</b></center></td><td><center><b>$R_VALUES[73] $R_VALUES[105]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被必殺</b></center></td><td><center><b>$R_VALUES[74] $R_VALUES[106]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>呪い</b></center></td><td><center><b>$R_VALUES[75] $R_VALUES[107]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被呪い</b></center></td><td><center><b>$R_VALUES[76] $R_VALUES[108]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>恨み</b></center></td><td><center><b>$R_VALUES[77] $R_VALUES[109]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>麻痺</b></center></td><td><center><b>$R_VALUES[78] $R_VALUES[110]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被麻痺</b></center></td><td><center><b>$R_VALUES[79] $R_VALUES[111]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>毒</b></center></td><td><center><b>$R_VALUES[80]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被毒</b></center></td><td><center><b>$R_VALUES[81]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>睡眠</b></center></td><td><center><b>$R_VALUES[82] $R_VALUES[112]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被睡眠</b></center></td><td><center><b>$R_VALUES[83] $R_VALUES[113]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>石化</b></center></td><td><center><b>$R_VALUES[84] $R_VALUES[114]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被石化</b></center></td><td><center><b>$R_VALUES[85] $R_VALUES[115]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>魅了</b></center></td><td><center><b>$R_VALUES[86] $R_VALUES[116]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被魅了</b></center></td><td><center><b>$R_VALUES[87] $R_VALUES[117]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>パワーダウン</b></center></td><td><center><b>$R_VALUES[88] $R_VALUES[118]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被パワーダウン</b></center></td><td><center><b>$R_VALUES[89] $R_VALUES[119]</b></center></td></tr>

	<tr bgcolor="$TABLE_COLOR1"><td><center><b>トランスファー</b></center></td><td><center><b>$R_VALUES[19]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>リバイバル</b></center></td><td><center><b>$R_VALUES[20]</b></center></td></tr>

	<tr bgcolor="$TABLE_COLOR1"><td><center><b>パワーアップ</b></center></td><td><center><b>$R_VALUES[21] $R_VALUES[23]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被パワーアップ</b></center></td><td><center><b>$R_VALUES[22] $R_VALUES[24]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>vs 304</b></center></td><td><center><b>$R_VALUES[25]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>バトルビューグル</b></center></td><td><center><b>$R_VALUES[26] $R_VALUES[35]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>メルトダウン</b></center></td><td><center><b>$R_VALUES[27]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ヒーリング</b></center></td><td><center><b>$R_VALUES[28]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ヒーリングオール</b></center></td><td><center><b>$R_VALUES[29]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>リザレクション</b></center></td><td><center><b>$R_VALUES[30]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>亡命成功</b></center></td><td><center><b>$R_VALUES[31]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>亡命失敗</b></center></td><td><center><b>$R_VALUES[32]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>内乱成功</b></center></td><td><center><b>$R_VALUES[33]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>内乱失敗</b></center></td><td><center><b>$R_VALUES[34]</b></center></td></tr>

	<tr bgcolor="$TABLE_COLOR1"><td><center><b>説得</b></center></td><td><center><b>$R_VALUES[90]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被説得</b></center></td><td><center><b>$R_VALUES[91]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>MP↓</b></center></td><td><center><b>$R_VALUES[92] $R_VALUES[120]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被MP↓</b></center></td><td><center><b>$R_VALUES[93] $R_VALUES[121]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>自爆</b></center></td><td><center><b>$R_VALUES[94]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被自爆</b></center></td><td><center><b>$R_VALUES[95]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>回転</b></center></td><td><center><b>$R_VALUES[96] $R_VALUES[122]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被回転</b></center></td><td><center><b>$R_VALUES[97] $R_VALUES[123]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ノックバック</b></center></td><td><center><b>$R_VALUES[98] $R_VALUES[124]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被ノックバック</b></center></td><td><center><b>$R_VALUES[99] $R_VALUES[125]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>クリティカル</b></center></td><td><center><b>$R_VALUES[100]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>即死</b></center></td><td><center><b>$R_VALUES[101]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被即死</b></center></td><td><center><b>$R_VALUES[102]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>HP↓</b></center></td><td><center><b>$R_VALUES[130] $R_VALUES[131]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>LF</b></center></td><td><center><b>$R_VALUES[132] $R_VALUES[133]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>シャイニング</b></center></td><td><center><b>$R_VALUES[134] $R_VALUES[135]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被シャイニング</b></center></td><td><center><b>$R_VALUES[136] $R_VALUES[137]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>エレメントブレイク</b></center></td><td><center><b>$R_VALUES[157]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>被エレメントブレイク</b></center></td><td><center><b>$R_VALUES[158]</b></center></td></tr>


	<tr bgcolor="$TABLE_COLOR1"><td><center><b>通常攻撃</b></center></td><td><center><b>$R_VALUES[138] $R_VALUES[146]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>突撃</b></center></td><td><center><b>$R_VALUES[139] $R_VALUES[147]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>防御</b></center></td><td><center><b>$R_VALUES[140] $R_VALUES[148]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ヒットアンドアウェイ</b></center></td><td><center><b>$R_VALUES[141] $R_VALUES[149]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>狙撃</b></center></td><td><center><b>$R_VALUES[142] $R_VALUES[150]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>捨て身</b></center></td><td><center><b>$R_VALUES[143] $R_VALUES[151]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>見切り</b></center></td><td><center><b>$R_VALUES[144] $R_VALUES[152]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ダブルアタック</b></center></td><td><center><b>$R_VALUES[145] $R_VALUES[153]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>トロフィー率</b></center></td><td><center><b>$R_VALUES[154]</b></center></td></tr>

	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ウインドショット</b></center></td><td><center><b>$R_VALUES[159]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>スパークスフィア</b></center></td><td><center><b>$R_VALUES[160]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>エイクオブソ\ーン</b></center></td><td><center><b>$R_VALUES[161]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>メイルシュトロム</b></center></td><td><center><b>$R_VALUES[162]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>バニッシュ</b></center></td><td><center><b>$R_VALUES[163]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>プリティキッス</b></center></td><td><center><b>$R_VALUES[164]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>コッレクティオ</b></center></td><td><center><b>$R_VALUES[165]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>アビス</b></center></td><td><center><b>$R_VALUES[166]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>コルヌリコルヌ</b></center></td><td><center><b>$R_VALUES[167]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>にぎりがくさい剣</b></center></td><td><center><b>$R_VALUES[168]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ゲルゲの吹き矢</b></center></td><td><center><b>$R_VALUES[169]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ブルークロス</b></center></td><td><center><b>$R_VALUES[170]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>エアリアルクライ</b></center></td><td><center><b>$R_VALUES[171]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>スーパーノヴァ</b></center></td><td><center><b>$R_VALUES[172]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>アースクエイク</b></center></td><td><center><b>$R_VALUES[173]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>アイスレクイエム</b></center></td><td><center><b>$R_VALUES[174]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>スターティアラ</b></center></td><td><center><b>$R_VALUES[175]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>デッドスクリーム</b></center></td><td><center><b>$R_VALUES[176]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>バックラー</b></center></td><td><center><b>$R_VALUES[177]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ラウンドシールド</b></center></td><td><center><b>$R_VALUES[178]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>むずがゆい小手</b></center></td><td><center><b>$R_VALUES[179]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ビビッドリング</b></center></td><td><center><b>$R_VALUES[180]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>知性の指輪</b></center></td><td><center><b>$R_VALUES[181]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>死者の指輪</b></center></td><td><center><b>$R_VALUES[182]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>言霊の指輪</b></center></td><td><center><b>$R_VALUES[183]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>地脈の指輪</b></center></td><td><center><b>$R_VALUES[184]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>烙印の指輪</b></center></td><td><center><b>$R_VALUES[185]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>加護の指輪</b></center></td><td><center><b>$R_VALUES[186]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>暗黒の護符</b></center></td><td><center><b>$R_VALUES[187]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>雷鳴の指輪</b></center></td><td><center><b>$R_VALUES[188]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>風のオーブ</b></center></td><td><center><b>$R_VALUES[189]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>炎のオーブ</b></center></td><td><center><b>$R_VALUES[190]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>大地のオーブ</b></center></td><td><center><b>$R_VALUES[191]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>水のオーブ</b></center></td><td><center><b>$R_VALUES[192]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>光のオーブ</b></center></td><td><center><b>$R_VALUES[193]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>闇のオーブ</b></center></td><td><center><b>$R_VALUES[194]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>雪のオーブ</b></center></td><td><center><b>$R_VALUES[195]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>雷のオーブ</b></center></td><td><center><b>$R_VALUES[196]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>バトルファン</b></center></td><td><center><b>$R_VALUES[197]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ライトメイス</b></center></td><td><center><b>$R_VALUES[198]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>リプルズロッド</b></center></td><td><center><b>$R_VALUES[199]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ガンバンテイン</b></center></td><td><center><b>$R_VALUES[200]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>死者の杖</b></center></td><td><center><b>$R_VALUES[201]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ヘムロック</b></center></td><td><center><b>$R_VALUES[202]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>カルディア</b></center></td><td><center><b>$R_VALUES[203]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>属性魔導書</b></center></td><td><center><b>$R_VALUES[204]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>精霊の護符</b></center></td><td><center><b>$R_VALUES[205]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>天使のブローチ</b></center></td><td><center><b>$R_VALUES[206]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ロザリオ</b></center></td><td><center><b>$R_VALUES[207]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>アミュレット</b></center></td><td><center><b>$R_VALUES[208]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>素手</b></center></td><td><center><b>$R_VALUES[209]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>腐ったカボチャ</b></center></td><td><center><b>$R_VALUES[210]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>満月の石</b></center></td><td><center><b>$R_VALUES[211]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ブラッドスペル</b></center></td><td><center><b>$R_VALUES[212]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>バトルブーツ</b></center></td><td><center><b>$R_VALUES[213]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>ワープシューズ</b></center></td><td><center><b>$R_VALUES[214]</b></center></td></tr>
	<tr bgcolor="$TABLE_COLOR1"><td><center><b>三つ編み</b></center></td><td><center><b>$R_VALUES[215]</b></center></td></tr>

	<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=2><center><b>2008/3/26より記録開始</b></center></td></tr>
	</table>
	-----END-----
	&FOOTER;
	print "</td></tr></table></form></body>";
}

sub BALANCE3{

	&HEADER;
	&DBM_INPORT(P);
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
		<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=4><center><b>エレメント比率</b></center></td></tr>
		
	-----END-----
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>属性</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>比率</td><td nowrap bgcolor=\"$TABLE_COLOR2\">人数</td></tr>";

while (my($key2,$val2) = each %P){
	@VALS = split(/\s/,$val2);$ET++;
	   foreach(0..$count) {
	   	if($VALS[31] == 0){$COUNTER[0]++;}
	   	if($VALS[31] == 1){$COUNTER[1]++;}
	   	if($VALS[31] == 2){$COUNTER[2]++;}
	   	if($VALS[31] == 3){$COUNTER[3]++;}
	   	if($VALS[31] == 4){$COUNTER[4]++;}
	   	if($VALS[31] == 5){$COUNTER[5]++;}
	   }
}
$BAR[0]=$COUNTER[0]*3;$WARIAI[0]=int($COUNTER[0]/$ET*100);
$BAR[1]=$COUNTER[1]*3;$WARIAI[1]=int($COUNTER[1]/$ET*100);
$BAR[2]=$COUNTER[2]*3;$WARIAI[2]=int($COUNTER[2]/$ET*100);
$BAR[3]=$COUNTER[3]*3;$WARIAI[3]=int($COUNTER[3]/$ET*100);
$BAR[4]=$COUNTER[4]*3;$WARIAI[4]=int($COUNTER[4]/$ET*100);
$BAR[5]=$COUNTER[5]*3;$WARIAI[5]=int($COUNTER[5]/$ET*100);
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center><img src=\"$IMG_FOLDER3/d0.gif\" width=\"16\" height=\"16\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[0]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI[0] ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[0]名</td></tr>" if $COUNTER[0];
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center><img src=\"$IMG_FOLDER3/d1.gif\" width=\"16\" height=\"16\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[1]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI[1] ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[1]名</td></tr>" if $COUNTER[1];
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center><img src=\"$IMG_FOLDER3/d2.gif\" width=\"16\" height=\"16\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[2]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI[2] ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[2]名</td></tr>" if $COUNTER[2];
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center><img src=\"$IMG_FOLDER3/d3.gif\" width=\"16\" height=\"16\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[3]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI[3] ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[3]名</td></tr>" if $COUNTER[3];
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center><img src=\"$IMG_FOLDER3/d4.gif\" width=\"16\" height=\"16\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[4]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI[4] ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[4]名</td></tr>" if $COUNTER[4];
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center><img src=\"$IMG_FOLDER3/d5.gif\" width=\"16\" height=\"16\"></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[5]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI[5] ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[5]名</td></tr>" if $COUNTER[5];




	print << "	-----END-----";
 	</table>
	-----END-----
	print "<BR>勢力図\表\示：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a>";
	&FOOTER;
	print "</td></tr></table></form></body>";
}
sub BALANCE4{
	&HEADER;
	&DBM_INPORT(P);
	print << "	-----END-----";
	<table width=100% height=100%><tr><td nowrap align=center>
	<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
		<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=4><center><b>流行クラス</b></center></td></tr>
		
	-----END-----
	print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>クラス名</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>比率</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center nowrap colspan=2>人口比率</td></tr>";

	require "./$LOG_FOLDER/class.data";
$i=0;
while (my($key,$val) = each %VCLASS_LIST){
	@VALS = split(/\s/,$val);
	$awn[$i]=$key;
	$i++;
}

$count=$i-1;$NONCOUNT=0;
while (my($key2,$val2) = each %P){
	@VALS = split(/\s/,$val2);$ET++;
	   $j=0;$kuni=0;
	   foreach(0..$count) {
	   	if($VALS[4] eq "$awn[$j]"){$COUNTER[$j]++;$kuni=1;}
	   $j++;
	   }
}

$k=0;
foreach(0..$count) {
$BAR[$k]=$COUNTER[$k]*3;$WARIAI=int($COUNTER[$k]/$ET*100);
@wname_sa=split(/\,/,$VCLASS_LIST{"$awn[$k]"});
print "<tr><td nowrap align=center bgcolor=\"$TABLE_COLOR1\"><font color=#dddddd>$wname_sa[0]</font></td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER1/gber.gif\" hspace=0 height=7 width=$BAR[$k]></td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$WARIAI ％</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=\"right\">$COUNTER[$k]名</td></tr>" if $COUNTER[$k];
$k++;
}

	print "</table>";
	print "<BR>勢力図\表\示：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a>";
	&FOOTER;
	print "</td></tr></table></form></body>";
}

sub CHOICE{

	&HEADER;
	print << "	-----END-----";
	<form action=$MAIN_SCRIPT method=POST name=choice>
	<script language="JavaScript">
		function Move(){parent.Sub.location.replace("$BACKFR");}
	</script>

	<input type=hidden name="cmd">
	<table width=100% height=70%><tr><td nowrap align=center>
	<table class=font9 cellspacing=2 cellpadding=3 bgcolor="$TABLE_BORDER">
	<tr><td nowrap bgcolor=$TABLE_COLOR2 colspan=3><center><b>勢力図</b></center></td></tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>栄枯盛衰</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">国家別人口比率</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='BALANCE';Move()"></td>
</tr>
<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>四元素説</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">エレメント比率</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='BALANCE3';Move()"></td>
</tr>
<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>趣味爆発</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">クラス数</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='BALANCE4';Move()"></td>
</tr>
<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>流行武器</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">武器</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='BALANCE5';Move()"></td>
</tr>
	-----END-----
if($COOKIE{'pass'} eq $MASTERPASS){
	print << "	-----END-----";
<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>連日連夜</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">304鯖系譜</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='BALANCE2';Move()"></td>
</tr>
<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>流行武器</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">武器</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='BALANCE5';Move()"></td>
</tr>
<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>セキュリティチェック</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">配列3番目</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING15';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>現在貢献</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">現在貢献値の高い人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING17';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>累計貢献</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">累計貢献値の高い人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING19';Move()"></td>
</tr>


	-----END-----
}

	print << "	-----END-----";
	<tr><td nowrap bgcolor=$TABLE_COLOR2 colspan=3><center><b>ランキング</b></center></td></tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>長者番付</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">貯金好きな人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>天下無双</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">戦闘好きな人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING3';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>臥薪嘗胆</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">撃破数多い人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING5';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>質実剛健</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">レベル高い人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING7';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>宝物探索</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">トレジャーを集める人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING9';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>悠悠自適</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">図鑑登録数が多い人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING13';Move()"></td>
</tr>

<tr><td nowrap bgcolor=$TABLE_COLOR2 align=center>英雄誕生</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;font-size:12px;">MVPを取った人々</td>
<td nowrap style="border:1px solid $TABLE_COLOR2;"><input type=submit name="custom" value="見る" onClick="document.choice.cmd.value='RANKING11';Move()"></td>
</tr>

	</table></form>
	</td></tr></table>

	-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";

}


sub RANKING2{

&HEADER;
&DBM_INPORT(P);
print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>資金力ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>資金</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $VALS[8]);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]="$VALS[8]";
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

print << "-----END-----";

</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub CRSP{
		if($_[0] =~ /^2$|^7$|^8$|^59$/i){$VALS[19]*=16;}
		elsif($_[0] =~ /^10$|^12$|^17$|^18$|^60$/i){$VALS[19]*=17;}
		elsif($_[0] =~ /^9$|^13$|^19$|^21$|^24$|^27$|^30$|^44$|^45$|^46$|^47$|^73$|^75$|^91$/i){$VALS[19]*=18;}
		elsif($_[0] =~ /^0$|^1$|^3$|^20$|^22$|^25$|^34$|^38$|^40$|^41$|^48$|^49$|^56$|^57$|^70$|^74$|^82$|^83$|^86$|^88$|^93$/i){$VALS[19]*=19;}
		elsif($_[0] =~ /^28$|^29$|^32$|^35$|^51$|^61$|^69$|^71$|^77$|^79$|^80$|^85$/i){$VALS[19]*=21;}
		elsif($_[0] =~ /^14$|^23$|^31$|^33$|^52$|^58$|^72$|^87$/i){$VALS[19]*=22;}
		elsif($_[0] =~ /^55$|^62$|^66$/i){$VALS[19]*=23;}
		elsif($_[0] =~ /^53$|^63$|^78$/i){$VALS[19]*=24;}
		else{$VALS[19]*=20;}

		if($_[0] =~ /^4$|^7$|^8$|^10$|^12$|^17$|^18$|^21$|^22$|^34$|^38$|^39$|^40$|^41$|^43$|^44$|^45$|^46$|^47$|^48$|^49$|^73$|^74$|^75$|^76$|^77$|^80$|^82$/i){$VALS[19]*=1.25;}

		if($_[0] eq "21"){$VALS[20]-=10;}
		elsif($_[0] =~ /^20$|^82$/i){$VALS[20]-=8;}
		elsif($_[0] =~ /^76$|^77$/i){$VALS[20]-=7;}
		elsif($_[0] =~ /^27$|^41$|^74$|^81$/i){$VALS[20]-=6;}
		elsif($_[0] =~ /^12$|^16$|^24$|^61$|^73$|^75$|^80$|^88$/i){$VALS[20]-=5;}
		elsif($_[0] =~ /^10$|^11$|^38$|^39$|^40$|^48$|^49$|^54$|^63$|^86$|^89$/i){$VALS[20]-=4;}
		elsif($_[0] =~ /^4$|^7$|^8$|^13$|^17$|^18$|^25$|^44$|^46$|^47$|^56$/i){$VALS[20]-=3;}
		elsif($_[0] =~ /^0$|^2$|^19$|^43$|^45$|^60$|^62$|^69$|^70$|^83$|^87$|^93$/i){$VALS[20]-=2;}
		elsif($_[0] =~ /^1$|^34$|^79$|^84$/i){$VALS[20]-=1;}
		elsif($_[0] eq "57"){$VALS[20]+=1;}
		elsif($_[0] =~ /^26$|^91$/i){$VALS[20]+=2;}
		elsif($_[0] =~ /^50$|^55$|^92$/i){$VALS[20]+=3;}
		elsif($_[0] =~ /^6$|^9$|^31$|^35$|^51$|^52$|^71$/i){$VALS[20]+=5;}
		elsif($_[0] =~ /^59$|^67$|^72$/i){$VALS[20]+=7;}
		elsif($_[0] =~ /^3$|^15$|^53$/i){$VALS[20]+=10;}
		elsif($_[0] =~ /^36$|^64$/i){$VALS[20]+=12;}
		elsif($_[0] eq "30"){$VALS[20]+=14;}
		elsif($_[0] =~ /^22$|^90$/i){$VALS[20]+=16;}

		if($_[0] eq "53"){$VALS[21]-=7;}
		elsif($_[0] =~ /^55$|^58$|^59$|^64$|^77$|^78$/i){$VALS[21]-=5;}
		elsif($_[0] =~ /^14$|^15$|^19$|^29$|^36$|^62$|^76$/i){$VALS[21]-=4;}
		elsif($_[0] =~ /^3$|^6$|^7$|^12$|^17$|^18$|^22$|^43$|^63$|^66$|^67$|^75$/i){$VALS[21]-=3;}
		elsif($_[0] =~ /^4$|^5$|^8$|^11$|^16$|^21$|^30$|^35$|^41$|^44$|^46$|^52$|^61$|^73$|^74$|^80$|^83$|^90$/i){$VALS[21]-=2;}
		elsif($_[0] =~ /^23$|^33$|^34$|^38$|^40$|^47$|^48$|^50$|^68$|^84$|^87$|^91$/i){$VALS[21]-=1;}
		elsif($_[0] =~ /^26$|^54$|^71$/i){$VALS[21]+=1;}
		elsif($_[0] =~ /^57$|^72$|^93$/i){$VALS[21]+=2;}
		elsif($_[0] =~ /^86$|^89$/i){$VALS[21]+=3;}
		elsif($_[0] =~ /^9$|^13$|^20$|^25$|^32$|^37$|^81$|^88$/i){$VALS[21]+=4;}
		elsif($_[0] =~ /^2$|^27$|^56$|^60$/i){$VALS[21]+=5;}
		elsif($_[0] eq "24"){$VALS[21]+=7;}

		if($_[0] eq "78"){$VALS[22]-=5;}
		elsif($_[0] =~ /^53$|^59$/i){$VALS[22]-=3;}
		elsif($_[0] =~ /^42$|^55$/i){$VALS[22]-=2;}
		elsif($_[0] =~ /^11$|^35$|^36$|^83$/i){$VALS[22]-=1;}
		elsif($_[0] =~ /^3$|^5$|^13$|^14$|^16$|^23$|^30$|^32$|^51$|^58$|^66$|^85$|^90$/i){$VALS[22]+=1;}
		elsif($_[0] =~ /^0$|^1$|^18$|^20$|^25$|^37$|^45$|^49$|^52$|^61$|^62$|^64$|^68$|^70$|^73$|^76$|^79$|^80$|^82$|^87$|^91$/i){$VALS[22]+=2;}
		elsif($_[0] =~ /^12$|^17$|^34$|^46$|^47$|^48$|^54$|^63$|^69$|^71$|^72$|^77$|^81$|^86$|^92$/i){$VALS[22]+=3;}
		elsif($_[0] =~ /^4$|^7$|^8$|^22$|^24$|^31$|^33$|^38$|^40$|^43$|^44$|^57$|^74$|^75$/i){$VALS[22]+=4;}
		elsif($_[0] =~ /^2$|^9$|^10$|^19$|^21$|^27$|^28$|^39$|^41$|^56$|^60$/i){$VALS[22]+=5;}
		elsif($_[0] =~ /^29$|^89$/i){$VALS[22]+=6;}
		elsif($_[0] eq "88"){$VALS[22]+=7;}

		if($_[0] eq "65"){$VALS[19]*=2;$VALS[20]+=100;$VALS[21]+=20;$VALS[22]-=50;}
}

sub RANKING4{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>戦闘力ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>総合戦闘\能\力</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);

&CRSP('$VALS[4]');

$POINT=int(($VALS[16]/4+$VALS[18]*6)*1.2+$VALS[19]*16+$VALS[20]*200+$VALS[21]*125+$VALS[22]*200+$VALS[29]*20);

# $POINT=int(($VALS[16]/4+$VALS[18]*6)*1.2+$VALS[19]*200+$VALS[20]*200+$VALS[21]*200+$VALS[22]*200+$VALS[29]*20);
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

$VALS[19]=$PL_VALUES[19];$VALS[20]=$PL_VALUES[20];$VALS[21]=$PL_VALUES[21];$VALS[22]=$PL_VALUES[22];
&CRSP('$PL_VALUES[4]');
$PL_VALUES[19]=$VALS[19];$PL_VALUES[20]=$VALS[20];$PL_VALUES[21]=$VALS[21];$PL_VALUES[22]=$VALS[22];

$PL_POINT=int(($PL_VALUES[16]/4+$PL_VALUES[18]*6)*1.2+$PL_VALUES[19]*16+$PL_VALUES[20]*200+$PL_VALUES[21]*125+$PL_VALUES[22]*200+$PL_VALUES[29]*20);

#$PL_POINT=int(($PL_VALUES[16]/4+$PL_VALUES[18]*6)*1.2+$PL_VALUES[19]*200+$PL_VALUES[20]*200+$PL_VALUES[21]*200+$PL_VALUES[22]*200+$PL_VALUES[29]*20);
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}


sub RANKING6{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>撃破数ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>撃破数</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
$POINT=$VALS[23]*110+$VALS[24];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

$PL_POINT=$PL_VALUES[23]*110+$PL_VALUES[24];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}


sub RANKING8{

&HEADER;
&DBM_INPORT(P);
print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>Lv.ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>レベル</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
$POINT=$VALS[29];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

print << "-----END-----";

</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub RANKING10{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>トレジャー獲得ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>獲得数</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[47]);
if($RC[0] eq ""){$RC[0] = 0;}
$POINT=$RC[0];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

@RCP=split(/!/,$PL_VALUES[47]);
if($RCP[0] eq ""){$RCP[0] = 0;}
$PL_POINT=$RCP[0];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub RANKING12{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>MVP獲得ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>獲得数</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[47]);
if($RC[1] eq ""){$RC[1] = 0;}
$POINT=$RC[1];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

@RCP=split(/!/,$PL_VALUES[47]);
if($RCP[1] eq ""){$RCP[1] = 0;}
$PL_POINT=$RCP[1];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub RANKING14{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>図鑑登録数ランキング</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>登録数</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[47]);
if($RC[2] eq ""){$RC[2] = 0;}
$POINT=$RC[2];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

@RCP=split(/!/,$PL_VALUES[47]);
if($RCP[2] eq ""){$RCP[2] = 0;}
$PL_POINT=$RCP[2];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}
sub RANKING16{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>カウント</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>カウント</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[47]);
if($RC[3] eq ""){$RC[3] = 0;}
$POINT=$RC[3];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}

$PL_POINT=$PL_VALUES[23]*110+$PL_VALUES[24];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub RANKING18{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>現在貢献値</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>カウント</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[50]);
if($RC[0] ne "A002"){$RC[1] = 0;}
if($RC[1] eq ""){$RC[1] = 0;}
$POINT=$RC[1];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}
@HC=split(/!/,$PL_VALUES[50]);
if($HC[0] ne "A002"){$HC[1] = 0;}
if($HC[1] eq ""){$HC[1] = 0;}
$PL_POINT=$HC[1];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub RANKING20{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>累計貢献値</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>カウント</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[50]);
if($RC[0] ne "A002"){$RC[2] = 0;}
if($RC[2] eq ""){$RC[2] = 0;}

$POINT=$RC[2];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}
@HC=split(/!/,$PL_VALUES[50]);
if($HC[0] ne "A002"){$HC[2] = 0;}
if($HC[2] eq ""){$HC[2] = 0;}

$PL_POINT=$HC[2];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}

sub RANKING22{

&HEADER;
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
		
	&DBM_INPORT(P);
	@PL_VALUES = split(/\s/,$P{"$COOKIE{'pname'}"});
	&ERROR('COOKIEが無効になっています。') if !$COOKIE{'pname'};
	&ERROR('PwdError','パスワードが間違っている恐れがあります。') if crypt ($COOKIE{'pass'},eb) ne "$PL_VALUES[2]";

print << "-----END-----";

<table width=100% height=70%><tr><td nowrap align=center>
<table bgcolor="$TABLE_BORDER" style="font-size:16px;">
<tr bgcolor="$TABLE_COLOR3"><td nowrap colspan=6><center><b>累計貢献値</b></center></td></tr>
<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>No.</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>ユニットネーム</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>所属国</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center>カウント</td><td nowrap bgcolor=\"$TABLE_COLOR2\" align=center colspan=2>コードネーム</td></tr>

-----END-----
$i=0;@tmp1 =();
while (my($key,$val) = each %P){
@VALS = split(/\s/,$val);
@RC=split(/!/,$VALS[50]);
if($RC[2] eq ""){$RC[2] = 0;}
$POINT=$RC[2];
if($VALS[5] ne "バランスの集い"){
push(@tmp1, $POINT);
$PNAME[$i]=$key;
if($VALS[5] eq ''){$PCOUNTRY[$i]="$NONE_NATIONALITY";}else{$PCOUNTRY[$i]="$VALS[5]";}
$PMONEY[$i]=$POINT;
$MSNAME[$i]="$VALS[3]";
$MSGIF[$i]="$VALS[27]";
$i++;
}
}
@PNAME = @PNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PCOUNTRY = @PCOUNTRY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@PMONEY = @PMONEY[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSNAME = @MSNAME[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];
@MSGIF = @MSGIF[sort {$tmp1[$b] <=> $tmp1[$a]} 0 .. $#tmp1];

$j=0;$count=$i-1;
foreach(0..$count) {
     if($j >= 20) { last; }
     $k=$j+1;
print "<tr><td nowrap bgcolor=\"$TABLE_COLOR2\" align=right>$k</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$PNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>【$PCOUNTRY[$j]】</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=right>$PMONEY[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\" align=center>$MSNAME[$j]</td><td nowrap bgcolor=\"$TABLE_COLOR1\"><img src=\"$IMG_FOLDER2/$MSGIF[$j].gif\" width=\"32\" height=\"32\" style=\"filter:fliph();\"></td></tr>";

$j++;
}
@HC=split(/!/,$PL_VALUES[50]);
if($HC[0] eq ""){$HC[0] = 0;}
if($HC[1] eq ""){$HC[1] = 0;}
if($HC[2] eq ""){$HC[2] = 0;}
$PL_POINT=$HC[2];
if($PL_VALUES[5] eq ''){$COUNTRY="$NONE_NATIONALITY";}else{$COUNTRY="$PL_VALUES[5]";}
print << "-----END-----";
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1" align=right></td><td nowrap bgcolor="$TABLE_COLOR1" align=center></td><td nowrap bgcolor="$TABLE_COLOR1"></td></tr>
<tr><td nowrap bgcolor="$TABLE_COLOR2" align=right>--</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$COOKIE{'pname'}</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>【$COUNTRY】</td><td nowrap bgcolor="$TABLE_COLOR1" align=right>$PL_POINT</td><td nowrap bgcolor="$TABLE_COLOR1" align=center>$PL_VALUES[3]</td><td nowrap bgcolor="$TABLE_COLOR1"><img src="$IMG_FOLDER2/$PL_VALUES[27].gif" width="32" height="32" style="filter:fliph();"></td></tr>
</table>
-----END-----
	print "<BR><center>ランキング：EDIT BY <a href=\"http://members.jcom.home.ne.jp/masimaro/\">MASIMARO</a></center>";
&FOOTER;
print "</td></tr></table></form></body>";
}
1;

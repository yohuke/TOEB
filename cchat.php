<?
/*********php5 only*********
  * 簡易チャット
  *               by ToR
  * http://php.s3.to/
  * 2001/07/26 公開
  * 2001/08/25 NameCheck追加
  *************へ***********/
//   /へ    ／ /
//  ιへ ＼/／/      無数部屋チャット Version ：2.4
//     γ⌒ ⌒ヽ
//    ﾉ/彡从川ﾍﾍﾍ    Modified：Feb.16.2012
//   ((从σ σ从ﾉ    Modified by Clare Harmolare
//   )))>" ヮ人ゝ    
//  (((( ｀-´ヽ))   http://ogre.s1.xrea.com/
// (((| |^γ^/ /
////////////////////////////////////////////////////
//　<概要>
//  無数に部屋数を設定できるチャットです（物理的限界はあります）
//  ログ保存行数や表示行数を参加人数に応じて変化させるので、
//  サーバに負担をかけず、動作も軽く、転送量も少ないです。
//
//  <XREA.COMでの設置方法>  ※（）内はパーミッション
//   shared_html
//      |
//      |-- cchat.php (604)
//      |-- log（707）任意のディレクトリ
//            |
//            |-- log.txt (606) 空のファイル
//            |-- log.htm (606) 空のファイル
//  ※cchat.phpはバイナリモード、それ以外はアスキーモードで転送する事。
//  チャットのURLはhttp://〜/cchat.phpとなります。
//
//  <利用方法>
//  http://〜/cchat.php?room=○○○
//  としてアクセスする。○○○の部分は任意の文字列（半角英数字）。
//  この○○○の部分変えることにより無限に部屋を増やせます。
//  TOEBに使う場合は、〜/cchat.php?room=○○○@toebで、タイトルが国別簡易チャットとなります。
////////////////////ユーザ設定//////////////////////

$ddir		= './log/';	//ログディレクトリ
$ena		= 'log';	//ログ＆メンバーファイル名
$exta		= '.txt';	//メンバーファイル拡張子
$extb		= '.htm';	//ログファイル拡張子
$admn		= "管直人";	//管理人用キャップパス
define(LINE, 6);		//一人当たりの表示行数
define(LINEALL, 36);		//限界表示行数
define(MAX, 18);		//一人当たりのログ保存行数
define(MAXALL, 600);		//限界のログ保存行数
define(ROM, 1);			//見学者表示 0-無し,1-カウントのみ
define(KUGIRI, 1);		//行間の区切り線 0-無し,1-無し(行間を少し空ける),2-有り
define(SEPA,"：");		//メンバー区切り文字
define(REFRESH, 40);		//自動更新秒数、転送量が膨大になるので、20未満は推奨しません。
define(TERM, 120);              //この時間内に更新が無いと退室とみなす（秒）

//////////////////ユーザ設定はここまで//////////////

$room = htmlspecialchars($_GET['room'], ENT_QUOTES);
$room = preg_replace( '/\./',  '', $room);
$room = preg_replace( '/\//',  '', $room);
if ( preg_match ('/([[:alnum:]]+)@([[:alnum:]]+)/', $room, $regs)) {
define(ACT_KEY, "$regs[1]");
define(MODO_KEY, "$regs[2]");
} elseif ( preg_match ('/([[:alnum:]]+)/', $room, $regs)) {
define(ACT_KEY, "$regs[1]");
define(MODO_KEY, "frame");
} else {
    die("Illegal Access : $room");
}
$enc = urlencode (ACT_KEY);
define(MEMBER, "$ddir$ena$exta");	//メンバーファイル
define(CHATLOG, "$ddir$ena$extb");	//ログファイル

if(KUGIRI==0){
 $kgyo = "<BR>";		//区切り線
 $gyok = "";			//行間
}elseif(KUGIRI==1){
 $kgyo = "<BR>";		//区切り線
 $gyok = "line-height: 11pt;";	//行間
}else{
 $kgyo = "<hr size=1>";		//区切り線
 $gyok = "";			//行間
}

header('Content-Type: text/html; charset=EUC-JP');
if(preg_match ('/frame/', MODO_KEY)){
?>
<HTML><HEAD><TITLE>ルーム名「<?echo ACT_KEY;?>」</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=EUC-JP">
</HEAD>
<frameset rows="75,*">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@form" frameborder="NO" name="frame1">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main" frameborder="NO" name="frame2">
</frameset>
<noframes>このページを見るにはフレーム対応のブラウザが必要です。</noframes>
<?
die("</HTML>");
}

if(preg_match ('/toeb/', MODO_KEY)){
?>
<HTML><HEAD><TITLE>国別簡易チャット</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=EUC-JP">
</HEAD>
<frameset rows="75,*">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@torm" frameborder="NO" name="frame1">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main" frameborder="NO" name="frame2">
</frameset>
<noframes>このページを見るにはフレーム対応のブラウザが必要です。</noframes>
<?
die("</HTML>");
}

$name = htmlspecialchars($_POST['name'], ENT_QUOTES, 'EUC-JP');
if($name){
  session_start();
  $_SESSION['name'] = $name;
}

foreach($_POST as $key=>$val){$$key=$val;}

function DatePrint($now){
  $addr = getenv("REMOTE_ADDR");
  $host = @gethostbyaddr($addr);
  $n_date = " <font class=tm>(".gmdate("m/d(D) H:i",$now+9*3600);
  $n_date .=")</font>";

  return $n_date;
}


function MemUpdate($name="",$id){
  $mem_arr = file(MEMBER);
  $now = time();
  $hua = getenv( "HTTP_USER_AGENT" );
  $addr = getenv("REMOTE_ADDR");
  $host = @gethostbyaddr($addr);
  $enc = urlencode (ACT_KEY);

  $fp = fopen(MEMBER, "w");
  foreach($mem_arr as $mem_data){
    list($m_name,$m_ip,$m_id,$m_time,$country,$u_agent) = explode("\t", $mem_data);    if(($now-$m_time) < TERM){
      if($m_id != $id){
        fputs($fp, $mem_data);
      }
    }
  }
  fputs($fp, "$name\t$host\t$id\t$now\t$enc\t$hua\n");
  fclose($fp);
}
function MemDump(){
  $mem_cnt = 0;
  $mems_cnt = 0;
  $rom_cnt = 0;
  $now = time();
  $hua = getenv( "HTTP_USER_AGENT" );
  $mem_arr = file(MEMBER);
  $enc = urlencode (ACT_KEY);
  foreach($mem_arr as $mem_data){
    list($m_name,$m_ip,$m_id,$m_time,$country,$u_agent) = explode("\t", $mem_data);
    if(($now-$m_time) < TERM){
      if($m_name){$mems_cnt++;}
      if($m_name && $enc == $country){ 
        $mem_lst .= "&nbsp;".$m_name.SEPA;
        $mem_cnt++;
      }elseif(ROM==2){
        $mem_lst .= "&nbsp;".$m_ip.SEPA;
      }elseif(ROM==1 && $enc == $country){
        $rom_cnt++;
	$rom_cnt-=$mems_cnt;
	if($rom_cnt < 0){
	   $rom_cnt = 0;
	}
      }
    }
  }
  return array($mem_cnt,$mem_lst,$rom_cnt,$mems_cnt);
}

if(preg_match ('/(form|torm|main)/', MODO_KEY)){
?>
<html><head><title>無数部屋チャット</title>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=EUC-JP">
<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
<?
}
if(preg_match ('/main/', MODO_KEY)){

$id = session_id();
$msg = htmlspecialchars($_POST['msg'], ENT_QUOTES, 'EUC-JP');
if($msg){
  $name = str_replace("◆", "◇", $name);
  $name = str_replace("★", "☆", $name);
}
if(strstr($name,"#")){
  $pass = substr($name, strpos($name,"#")+1);
  if($pass == "$admn"){
    $name2 = substr($name, 0, strpos($name,"#"));
    $name = $name2."★";
  }else{
    $pass = str_replace('&#44;',',',$pass);
    $salt = substr($pass."H.", 1, 2);
    $salt = preg_replace('/[^\.-z]/', '/./', $salt);
    $salt = strtr($salt,":;<=>?@[\\]^_`","ABCDEFGabcdef");
    $name2 = substr($name, 0, strpos($name,"#"));
    $name = $name2."◆".substr(crypt($pass,$salt),-8);
  }
}
MemUpdate($name,$id);
$mem_arr = MemDump();

?>
<META HTTP-EQUIV="refresh" CONTENT="<?echo REFRESH;?>; URL=<?echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main">
<style type="text/css">
	body	{color: #362936;font-size: 10pt;}
	.tm	{color: #888888;font-size: 8pt;<?echo $gyok;?>}
<?
}
if(preg_match ('/(form|torm)/', MODO_KEY)){
?>
<SCRIPT LANGUAGE="JavaScript">
<!--
function autoclear() {
  document.s.msg.value="";
  document.s.msg.focus();
}
-->
</SCRIPT>
<style type="text/css">
	body	{color: #362936;font-size: 10pt;}
	.tm	{color: #362936;}
	input	{
	font-family: "ＭＳ Ｐゴシック", "Osaka";font-size: 10pt;
	border: 1px #666666 solid;
	color: #000066;
	}
<?
}
if(preg_match ('/(form|torm|main)/', MODO_KEY)){
?>
</style></head>
<body bgcolor="#FBF7EF">
<?
}

if(preg_match ('/form/', MODO_KEY)){
?>
＜＜<a href="http://ogre.s1.xrea.com/" target=_blank class=tm>無数部屋チャット Ver2.4</a>＞＞
[ <a href="?room=<?echo ACT_KEY;?>@main" target="frame2" class=tm>リロード</a> ]   [ <a href="?room=<?echo ACT_KEY;?>" target="_blank" class=tm>新規ウィンドウ</a> ]…「名前#パス」入力でトリップ付。「clear」で自分の全発言を消去。<br>
<?
}

if(preg_match ('/torm/', MODO_KEY)){
?>
＜＜<a href="http://ogre.s1.xrea.com/" target=_blank class=tm>国別簡易チャット Ver2.4</a>＞＞
[ <a href="?room=<?echo ACT_KEY;?>@main" target="frame2" class=tm>リロード</a> ]   [ <a href="?room=<?echo ACT_KEY;?>@toeb" target="_blank" class=tm>新規ウィンドウ</a> ]…「名前#パス」入力でトリップ付。「clear」で自分の全発言を消去。<br>
<?
}

if(preg_match ('/(form|torm)/', MODO_KEY)){
?>
<form action="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main" target="frame2" method="post" name="s" onSubmit="setTimeout(&quot;autoclear()&quot;,100);">
<b>名前:</b><input name="name" type="text" size="15" maxlength="15" value="<?echo $name;?>">
<b> : </b><input name="msg" type="text" size="60" value="">
<input name="submit" type="submit" value=" Send / Reload ">
</form>
<SCRIPT LANGUAGE="JavaScript">
<!--
document.s.msg.focus();
// -->
</SCRIPT>
<?
die("</body></html>");
}
if(preg_match ('/main/', MODO_KEY)){
echo "[ ".gmdate("H:i:s",time()+9*3600)." ] ";
  if(strstr($mem_arr[1],"◆")){
    $mem_arr[1] = substr($mem_arr[1], 0, strpos($mem_arr[1],"◆"));
    $mem_arr[1] = $mem_arr[1]."◆";
  }
  if(strstr($mem_arr[1],"★")){
    $mem_arr[1] = substr($mem_arr[1], 0, strpos($mem_arr[1],"★"));
    $mem_arr[1] = $mem_arr[1]."★";
  }
echo "&nbsp;参加者($mem_arr[0])：$mem_arr[1]&nbsp;&nbsp;&nbsp;&nbsp;";
if(ROM!=0) echo "見学者：$mem_arr[2]人&nbsp;&nbsp;&nbsp;&nbsp;利用者：$mem_arr[3]人";
echo "　 Refresh";echo REFRESH;echo "秒<hr size=1>";

$tmax = $mem_arr[3] * MAX + MAX;
if($tmax > MAXALL) $tmax = MAXALL;
$lines = file(CHATLOG);		//ファイルを配列に読み込む
if ($msg && $name){ 	
  if($msg == 'clear'){
    $fp = fopen (CHATLOG , "w");
    for($i = 0; $i < $tmax; $i++)
	if(!strpos($lines[$i], "-$enc-->$name<")){
    fputs($fp, $lines[$i]);
	}
    fclose ($fp);
    $lines = file(CHATLOG);
    $msg = "All Clear (^-^)v";
  }
  $msg = htmlspecialchars ($msg, ENT_QUOTES, 'EUC-JP');//タグ不可
  if(get_magic_quotes_gpc())  $msg = stripslashes($msg);
  $msg = nl2br($msg);  //改行文字の前に<br>を代入する。
  $msg = preg_replace( '/\n/',  '', $msg);  //\nを文字列から消す。
  $name = htmlspecialchars ($name, ENT_QUOTES, 'EUC-JP');
  $date = DatePrint(time());
  $msg = "<B><!--$enc-->$name</B> > $msg $date$kgyo\n";
  $fp = fopen (CHATLOG , "w");		//書き込みモードでオープン
  fputs ($fp, "$msg");			//先頭に書き込む
  for($i = 0; $i < $tmax; $i++)		//いままでの分を追記
    fputs($fp, $lines[$i]);
  fclose ($fp);
  echo $msg;
}
$tline = $mem_arr[0] * LINE + LINE;
if($tline > LINEALL) $tline = LINEALL;
for($i = 0; $i < $tmax; $i++)
     if(strpos($lines[$i], "<!--$enc-->")){$j++;
	if($j <= $tline){echo $lines[$i];}
     }
die("</body></html>");
}
?>


<?
/*********php5 only*********
  * �ʰץ���å�
  *               by ToR
  * http://php.s3.to/
  * 2001/07/26 ����
  * 2001/08/25 NameCheck�ɲ�
  *************��***********/
//   /��    �� /
//  �ɤ� ��/��/      ̵����������å� Version ��2.4
//     �â� �ޡ�
//    ��/��к��͎͎�    Modified��Feb.16.2012
//   ((к�� ��к��    Modified by Clare Harmolare
//   )))>" ��͡�    
//  (((( ��-����))   http://ogre.s1.xrea.com/
// (((| |^��^/ /
////////////////////////////////////////////////////
//��<����>
//  ̵����������������Ǥ������åȤǤ���ʪ��Ū�³��Ϥ���ޤ���
//  ����¸�Կ���ɽ���Կ��򻲲ÿͿ��˱������Ѳ�������Τǡ�
//  �����Ф���ô�򤫤�����ư���ڤ���ž���̤⾯�ʤ��Ǥ���
//
//  <XREA.COM�Ǥ�������ˡ>  ���ʡ���ϥѡ��ߥå����
//   shared_html
//      |
//      |-- cchat.php (604)
//      |-- log��707��Ǥ�դΥǥ��쥯�ȥ�
//            |
//            |-- log.txt (606) ���Υե�����
//            |-- log.htm (606) ���Υե�����
//  ��cchat.php�ϥХ��ʥ�⡼�ɡ�����ʳ��ϥ��������⡼�ɤ�ž���������
//  ����åȤ�URL��http://��/cchat.php�Ȥʤ�ޤ���
//
//  <������ˡ>
//  http://��/cchat.php?room=������
//  �Ȥ��ƥ����������롣����������ʬ��Ǥ�դ�ʸ�����Ⱦ�ѱѿ����ˡ�
//  ���Ρ���������ʬ�Ѥ��뤳�Ȥˤ��̵�¤����������䤻�ޤ���
//  TOEB�˻Ȥ����ϡ���/cchat.php?room=������@toeb�ǡ������ȥ뤬���̴ʰץ���åȤȤʤ�ޤ���
////////////////////�桼������//////////////////////

$ddir		= './log/';	//���ǥ��쥯�ȥ�
$ena		= 'log';	//�������С��ե�����̾
$exta		= '.txt';	//���С��ե������ĥ��
$extb		= '.htm';	//���ե������ĥ��
$admn		= "��ľ��";	//�������ѥ���åץѥ�
define(LINE, 6);		//����������ɽ���Կ�
define(LINEALL, 36);		//�³�ɽ���Կ�
define(MAX, 18);		//���������Υ���¸�Կ�
define(MAXALL, 600);		//�³��Υ���¸�Կ�
define(ROM, 1);			//���ؼ�ɽ�� 0-̵��,1-������ȤΤ�
define(KUGIRI, 1);		//�Դ֤ζ��ڤ��� 0-̵��,1-̵��(�Դ֤򾯤�������),2-ͭ��
define(SEPA,"��");		//���С����ڤ�ʸ��
define(REFRESH, 40);		//��ư�����ÿ���ž���̤�����ˤʤ�Τǡ�20̤���Ͽ侩���ޤ���
define(TERM, 120);              //���λ�����˹�����̵�����༼�Ȥߤʤ����á�

//////////////////�桼������Ϥ����ޤ�//////////////

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
define(MEMBER, "$ddir$ena$exta");	//���С��ե�����
define(CHATLOG, "$ddir$ena$extb");	//���ե�����

if(KUGIRI==0){
 $kgyo = "<BR>";		//���ڤ���
 $gyok = "";			//�Դ�
}elseif(KUGIRI==1){
 $kgyo = "<BR>";		//���ڤ���
 $gyok = "line-height: 11pt;";	//�Դ�
}else{
 $kgyo = "<hr size=1>";		//���ڤ���
 $gyok = "";			//�Դ�
}

header('Content-Type: text/html; charset=EUC-JP');
if(preg_match ('/frame/', MODO_KEY)){
?>
<HTML><HEAD><TITLE>�롼��̾��<?echo ACT_KEY;?>��</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=EUC-JP">
</HEAD>
<frameset rows="75,*">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@form" frameborder="NO" name="frame1">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main" frameborder="NO" name="frame2">
</frameset>
<noframes>���Υڡ����򸫤�ˤϥե졼���б��Υ֥饦����ɬ�פǤ���</noframes>
<?
die("</HTML>");
}

if(preg_match ('/toeb/', MODO_KEY)){
?>
<HTML><HEAD><TITLE>���̴ʰץ���å�</TITLE>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=EUC-JP">
</HEAD>
<frameset rows="75,*">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@torm" frameborder="NO" name="frame1">
<frame src="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main" frameborder="NO" name="frame2">
</frameset>
<noframes>���Υڡ����򸫤�ˤϥե졼���б��Υ֥饦����ɬ�פǤ���</noframes>
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
<html><head><title>̵����������å�</title>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=EUC-JP">
<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
<?
}
if(preg_match ('/main/', MODO_KEY)){

$id = session_id();
$msg = htmlspecialchars($_POST['msg'], ENT_QUOTES, 'EUC-JP');
if($msg){
  $name = str_replace("��", "��", $name);
  $name = str_replace("��", "��", $name);
}
if(strstr($name,"#")){
  $pass = substr($name, strpos($name,"#")+1);
  if($pass == "$admn"){
    $name2 = substr($name, 0, strpos($name,"#"));
    $name = $name2."��";
  }else{
    $pass = str_replace('&#44;',',',$pass);
    $salt = substr($pass."H.", 1, 2);
    $salt = preg_replace('/[^\.-z]/', '/./', $salt);
    $salt = strtr($salt,":;<=>?@[\\]^_`","ABCDEFGabcdef");
    $name2 = substr($name, 0, strpos($name,"#"));
    $name = $name2."��".substr(crypt($pass,$salt),-8);
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
	font-family: "�ͣ� �Х����å�", "Osaka";font-size: 10pt;
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
���<a href="http://ogre.s1.xrea.com/" target=_blank class=tm>̵����������å� Ver2.4</a>���
[ <a href="?room=<?echo ACT_KEY;?>@main" target="frame2" class=tm>�����</a> ]   [ <a href="?room=<?echo ACT_KEY;?>" target="_blank" class=tm>����������ɥ�</a> ]�ġ�̾��#�ѥ������Ϥǥȥ�å��ա���clear�פǼ�ʬ����ȯ����õ<br>
<?
}

if(preg_match ('/torm/', MODO_KEY)){
?>
���<a href="http://ogre.s1.xrea.com/" target=_blank class=tm>���̴ʰץ���å� Ver2.4</a>���
[ <a href="?room=<?echo ACT_KEY;?>@main" target="frame2" class=tm>�����</a> ]   [ <a href="?room=<?echo ACT_KEY;?>@toeb" target="_blank" class=tm>����������ɥ�</a> ]�ġ�̾��#�ѥ������Ϥǥȥ�å��ա���clear�פǼ�ʬ����ȯ����õ<br>
<?
}

if(preg_match ('/(form|torm)/', MODO_KEY)){
?>
<form action="<? echo $PHP_SELF;?>?room=<?echo ACT_KEY;?>@main" target="frame2" method="post" name="s" onSubmit="setTimeout(&quot;autoclear()&quot;,100);">
<b>̾��:</b><input name="name" type="text" size="15" maxlength="15" value="<?echo $name;?>">
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
  if(strstr($mem_arr[1],"��")){
    $mem_arr[1] = substr($mem_arr[1], 0, strpos($mem_arr[1],"��"));
    $mem_arr[1] = $mem_arr[1]."��";
  }
  if(strstr($mem_arr[1],"��")){
    $mem_arr[1] = substr($mem_arr[1], 0, strpos($mem_arr[1],"��"));
    $mem_arr[1] = $mem_arr[1]."��";
  }
echo "&nbsp;���ü�($mem_arr[0])��$mem_arr[1]&nbsp;&nbsp;&nbsp;&nbsp;";
if(ROM!=0) echo "���ؼԡ�$mem_arr[2]��&nbsp;&nbsp;&nbsp;&nbsp;���Ѽԡ�$mem_arr[3]��";
echo "�� Refresh";echo REFRESH;echo "��<hr size=1>";

$tmax = $mem_arr[3] * MAX + MAX;
if($tmax > MAXALL) $tmax = MAXALL;
$lines = file(CHATLOG);		//�ե������������ɤ߹���
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
  $msg = htmlspecialchars ($msg, ENT_QUOTES, 'EUC-JP');//�����Բ�
  if(get_magic_quotes_gpc())  $msg = stripslashes($msg);
  $msg = nl2br($msg);  //����ʸ��������<br>���������롣
  $msg = preg_replace( '/\n/',  '', $msg);  //\n��ʸ���󤫤�ä���
  $name = htmlspecialchars ($name, ENT_QUOTES, 'EUC-JP');
  $date = DatePrint(time());
  $msg = "<B><!--$enc-->$name</B> > $msg $date$kgyo\n";
  $fp = fopen (CHATLOG , "w");		//�񤭹��ߥ⡼�ɤǥ����ץ�
  fputs ($fp, "$msg");			//��Ƭ�˽񤭹���
  for($i = 0; $i < $tmax; $i++)		//���ޤޤǤ�ʬ���ɵ�
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


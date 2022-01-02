#!/usr/local/bin/perl
#            へ
####/へ####／ /#####################################
#  ιへ ＼/／/
#     γ⌒ ⌒ヽ     Tactics Ogre de Endless Battle
#    ﾉ/彡从川ﾍﾍﾍ
#   ((从σ σ从ﾉ    Version ：4.16.4
#   )))>" ヮ人ゝ    Modified：Dec.31.2002
#  (((( ｀-´ヽ))   Modified by Clare Harmolare
# (((| |^γ^/ /     http://ogre.s1.xrea.com/
####################################################
use lib '.';
require 'ebs_sub1.cgi';

if ($DIRECT_LINK && $SUB ne 'MY_LIST' && $SUB ne 'C_LIST') {
$href = $ENV{'HTTP_REFERER'};
if ($href eq '' || $href =~ m#bookmark#i || $href =~ m#unknown#i) {$href = 'boknot';}
my $REF_FLAG=0;
  foreach (@OK_LINK) {
    $_ =~ s#\~#.*#g;
    if ($href =~ m#$_#i || $SUB eq 'LOGO') {$REF_FLAG=1;}
    }
  unless ($REF_FLAG) {&ERROR('直リンクは禁止です','トップページからのアクセスお願いします。');
  }
}
if ($BLACKCHECK && $SUB ne 'MY_LIST' && $SUB ne 'C_LIST') {
$addr = $ENV{'REMOTE_ADDR'};
$host = $ENV{'REMOTE_HOST'};
if (($host eq $addr) || ($host eq '')) {$host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;}
  foreach (@DENYHOST) {
    $_ =~ s#\~#.*#g;
    if ($host =~ m#$_#i || $addr =~ m#$_#i) {$BLACKFLAG=1;}
  }
  if ($BLACKFLAG) {&ERROR('だーめっ！');}
}
#&ERROR('だーめっ！111');

if ($PROXYCHECK && $SUB ne 'MY_LIST' && $SUB ne 'C_LIST') {
$addr = $ENV{'REMOTE_ADDR'};
$host = $ENV{'REMOTE_HOST'};
if (($host eq $addr) || ($host eq '')) {$host = gethostbyaddr(pack('C4',split(/\./,$addr)),2) || $addr;}
 if (($KYOKA eq "") || ($host !~ /$KYOKA/)) {
 $agent  = $ENV{'HTTP_USER_AGENT'};
 $accept_lan  = $ENV{'HTTP_ACCEPT_LANGUAGE'};
  if ($IP_JP !=0 && ($host !~ /jp$/i) && ($addr ne $host || $IP_JP==1 && $addr eq $host)) {$IP_JP_FRAG=1;}
  if ($HAITERU==1 && (($ENV{'HTTP_VIA'} ne "") || ($agent=~ /via|squid|delegate|httpd|proxy|cache/i) || ($ENV{'HTTP_CACHE_INFO'} ne ""))) {$PROXY_FRAG=1;}
  if ($HAITERU==2 && (($ENV{'HTTP_VIA'} ne "") || ($agent=~ /via|squid|delegate|httpd|proxy|cache/i) || ($ENV{'HTTP_CACHE_CONTROL'} ne "") || ($ENV{'HTTP_PROXY_CONNECTION'} ne "") || ($ENV{'HTTP_CACHE_INFO'} ne ""))) {$PROXY_FRAG=1;}
  if ($BAREBARE && ($host =~ /squid|^firewall|^fw.|anonymizer|proxy|cache|delegate|^dns|keeper|^mail|^www|^ns\d{0,2}\.|us$|uk$|edu$|com$|org$|net$|at$|au$|ca$|ch$|de$|dk$|fi$|fr$|it$|il$|kr$|nl$|pt$|tw$/i)) {$PROXY_HOST=1;}
  if ($YAHOOBB==0){
   if ($IP_JP_FRAG){&ERROR('アクセス制限中','海外からのアクセスは禁止です。');}
   if ($PROXY_FRAG){&ERROR('アクセス制限中','プロクシ経由のアクセス禁止です。Proxy変数が出ています。');}
   if ($PROXY_HOST){&ERROR('アクセス制限中','プロクシ経由のアクセス禁止です。いかにも Proxyといったホスト名です。');}
  }else{
   if ($IP_JP_FRAG && ($PROXY_FRAG || ($host !~ /com$|net$|org$/i))){&ERROR('アクセス制限中','Proxy経由のアクセスは禁止です。');}
  }
   if ($BENKYOSHIRO && ($host =~ /.ac.jp$|.ed.jp$|edu$/i)) {&ERROR('アクセス制限中','学校・教育機関からのアクセスは禁止です。勉強しなさい（笑');}
   if ($SHIGOTOSHIRO && ($host =~ /.co.jp$|.go.jp$|.gr.jp$|.or.jp$|com$|gov$|int$|org$|mil$/i)) {&ERROR('アクセス制限中','会社・政府機関からのアクセスは禁止です。仕事しなさい（笑');}
   if ($FIRE_WALL && (($host =~ /^firewall|^fw.|delegate/i) || ($agent =~ /delegate/i))) {&ERROR('アクセス制限中','ファイアウォール内からのアクセスは禁止です。');}
   if ($JP_ONLY==1 && ($accept_lan !~ /ja/i)) {&ERROR('アクセス制限中','Sorry, Only in Japanese.');}
   if ($JP_ONLY==2 && (($accept_lan !~ /ja/i) || ($accept_lan =~ /zh|ko/i))) {&ERROR('アクセス制限中','Sorry, Only in Japanese.');}
 }
}
!$SUB && ($SUB='TOP');
&$SUB;

sub LOGIN		{require 'ebs_sub2.cgi';&LOGIN2;}
sub MY_LIST		{require 'ebs_sub2.cgi';&MY_LIST2;}
sub LOG0		{require 'ebs_sub2.cgi';&LOG01;}
sub C_LIST		{require 'ebs_sub2.cgi';&C_LIST2;}
sub WEAPON		{require 'ebs_sub2.cgi';&WEAPON_LIST;}
sub ICON		{require 'ebs_sub2.cgi';&ICON_LIST;}

sub MAIN_FRAME		{require "./$LOG_FOLDER/$HASH_DATA";require 'ebs_sub3.cgi';&STATUS;}
sub CO_LIST		{require 'ebs_sub3_2.cgi';&CNTRY_LIST;}
sub TOP 		{require 'ebs_sub3_3.cgi';&FRAME;}
sub CUSTOM		{require "./$LOG_FOLDER/$HASH_DATA";require "./$LOG_FOLDER/$ABI_DATA";require 'ebs_sub3_3.cgi';&CUSTOMIZE;require 'ebs_sub3.cgi';if($FORM{'Cflag'} eq "ON"){&HEADER;&FOOTER;}else{&STATUS;}}

sub BATTLE_1	{require 'ebs_sub4.cgi';&BATTLE1;}
sub BATTLE_2	{require 'ebs_sub4_2.cgi';&BATTLE2;}
sub BATTLE_3	{require 'ebs_sub4_3.cgi';&BATTLE3;}
sub BATTLE_4	{require 'ebs_sub4_4.cgi';&BATTLE4;}
sub BATTLE_5	{require 'ebs_sub4_5.cgi';&BATTLE5;}
sub BATTLE_6	{require 'ebs_sub4_6.cgi';&BATTLE6;}

sub EQUIPMENT	{require 'ebs_sub5.cgi';&EQUIP;}
sub MISSION		{require 'ebs_sub5.cgi';&MISSION2;}
sub MAKE_C		{require 'ebs_sub5.cgi';&MAKE_C2;}
sub MAKE_T		{require 'ebs_sub5.cgi';&MAKE_T2;}
sub CUSTOMING	{require 'ebs_sub5_2.cgi';&CUSTOMING2;}
sub HIS			{require 'ebs_sub5_3.cgi';&HISTORY;}
sub COM			{require 'ebs_sub5_3.cgi';&COMMENT;}
sub SPC			{require 'ebs_sub5_3.cgi';&SPECIAL;}
sub BOSS		{require 'ebs_sub5_3.cgi';&BOSS2;}
sub MAHOU		{require 'ebs_sub5_3.cgi';&MAHOU2;}
sub CARD		{require 'ebs_sub5_3.cgi';&TAROT;}
sub CHICON		{require 'ebs_sub5_3.cgi';&CHICON2;}
sub DEFM		{require 'ebs_sub5_3.cgi';&DEFM2;}
sub ICONEX		{require 'ebs_sub5_3.cgi';&ICONEX2;}
sub WEAPONFORCE	{require 'ebs_sub5_3.cgi';&WEAPONFORCE2;}

sub JYUKU	{require 'ebs_sub5_3.cgi';&JYUKU2;}

sub ABISET	{require 'ebs_sub5_4.cgi';&ABISET2;}
sub KOUKENSET	{require 'ebs_sub5_5.cgi';&KOUKENSET2;}
sub SKLSET	{require 'ebs_sub5_6.cgi';&SKLSET2;}

sub KAKUNIN		{require 'ebs_sub6.cgi';&KAKUNIN2;}
sub RESIST		{require 'ebs_sub6.cgi';&RESIST2;}
sub DELETE		{require 'ebs_sub6.cgi';&DELETE3;}
sub ENTRY		{require 'ebs_sub6.cgi';&ENTRY2;}
sub DELETE2		{require 'ebs_sub6.cgi';&DELETE4;}
sub PASSCHAN		{require 'ebs_sub6.cgi';&PASSCHAN3;}
sub PASSCHAN2		{require 'ebs_sub6.cgi';&PASSCHAN4;}

sub MAINTE		{require 'ebs_sub7.cgi';&MAINTENANCE;}
sub LGIN_RIREKI		{require 'ebs_sub7.cgi';&LGIN_RIREKI2;}
sub XPL_LIST		{require 'ebs_sub7.cgi';&XPL_LIST2;}
sub XCO_LIST		{require 'ebs_sub7.cgi';&XCO_LIST2;}
sub HISTORY_EDIT	{require 'ebs_sub7.cgi';&HISTORY_EDIT2;}
sub HISTORY_EDIT2	{require 'ebs_sub7.cgi';&HISTORY_EDIT3;&HISTORY_EDIT2;}
sub SYUSEI		{require 'ebs_sub7.cgi';&SYUSEI2;&XPL_LIST2;}
sub CNSYUSEI		{require 'ebs_sub7.cgi';&CNSYUSEI2;&XCO_LIST2;}
sub PL_DEL		{require 'ebs_sub7.cgi';&PL_DEL2;}
sub PL_DEL2		{require 'ebs_sub7.cgi';&PL_DEL3;&MAINTENANCE2;}
sub CO_DEL		{require 'ebs_sub7.cgi';&CO_DEL2;}
sub CO_DEL2		{require 'ebs_sub7.cgi';&CO_DEL3;&MAINTENANCE2;}
sub MASTER		{require 'ebs_sub7.cgi';&MASTER2;}
sub SYUSEI3		{require 'ebs_sub7.cgi';&SYUSEI5;}
sub TYOUSEI		{require 'ebs_sub7.cgi';&TYOUSEI2;&SYUSEI5;}
sub BACKUP		{require 'ebs_sub7.cgi';&BACKUP2;}
sub DATAUP		{require 'ebs_sub7.cgi';&DATAUP2;}
sub HUKUGEN		{require 'ebs_sub7.cgi';&SYUSEI4;}
sub SYUUHUKU		{require 'ebs_sub7.cgi';&TYOUSEI2;&SYUSEI4;}
sub COUNTRY		{require 'ebs_sub7.cgi';&COUNTRY2;}
sub HENSYU		{require 'ebs_sub7.cgi';&HENSYU2;}
sub KAIZAN		{require 'ebs_sub7.cgi';&KAIZAN2;&HENSYU2;}
sub COOKIES		{require 'ebs_sub7.cgi';&COOKIES2;}
sub DEL			{require 'ebs_sub7.cgi';&DEL2;&COOKIES2;}
sub PUSHHITO		{require 'ebs_sub7.cgi';&PUSHHITO2;}
sub OPENHITO		{require 'ebs_sub7.cgi';&OPENHITO2;}
sub PUSHKUNI		{require 'ebs_sub7.cgi';&PUSHKUNI2;}
sub OPENKUNI		{require 'ebs_sub7.cgi';&OPENKUNI2;}
sub bukilist		{require 'ebs_sub7_2.cgi';&bukilist;}
sub bukilist1		{require 'ebs_sub7_2.cgi';&bukilist1;}
sub bukilist2		{require 'ebs_sub7_2.cgi';&bukilist2;}
sub classlist		{require 'ebs_sub7_2.cgi';&classlist;}
sub classlist1		{require 'ebs_sub7_2.cgi';&classlist1;}
sub classlist2		{require 'ebs_sub7_2.cgi';&classlist2;}
sub vamity		{require 'ebs_sub7_2.cgi';&vamity;}
sub vamity1		{require 'ebs_sub7_2.cgi';&vamity1;}
sub vamity2		{require 'ebs_sub7_2.cgi';&vamity2;}
sub vamity3		{require 'ebs_sub7_2.cgi';&vamity3;}
sub result		{require 'ebs_sub7_2.cgi';&result;}
sub result1		{require 'ebs_sub7_2.cgi';&result1;}
sub result2		{require 'ebs_sub7_2.cgi';&result2;}

sub BALANCE		{require 'ebs_sub8.cgi';&BALANCE;}
sub BALANCE2		{require 'ebs_sub8.cgi';&BALANCE2;}
sub BALANCE3		{require 'ebs_sub8.cgi';&BALANCE3;}
sub BALANCE4		{require 'ebs_sub8.cgi';&BALANCE4;}
sub BALANCE5		{require 'ebs_sub8.cgi';&BALANCE5;}
sub RANKINGS		{require 'ebs_sub8.cgi';&CHOICE;}
sub RANKING		{require 'ebs_sub8.cgi';&RANKING2;}
sub RANKING3		{require 'ebs_sub8.cgi';&RANKING4;}
sub RANKING5		{require 'ebs_sub8.cgi';&RANKING6;}
sub RANKING7		{require 'ebs_sub8.cgi';&RANKING8;}
sub RANKING9		{require 'ebs_sub8.cgi';&RANKING10;}
sub RANKING11		{require 'ebs_sub8.cgi';&RANKING12;}
sub RANKING13		{require 'ebs_sub8.cgi';&RANKING14;}
sub RANKING15		{require 'ebs_sub8.cgi';&RANKING16;}
sub RANKING17		{require 'ebs_sub8.cgi';&RANKING18;}
sub RANKING19		{require 'ebs_sub8.cgi';&RANKING20;}
sub RANKING21		{require 'ebs_sub8.cgi';&RANKING22;}

sub ZUKAN		{require 'wzukan.cgi';&ZUKAN2;}
sub ETURAN		{require 'wzukan.cgi';&ETURAN2;}
sub TOUROKU		{require 'wzukan.cgi';&TOUROKU2;&ZUKAN;}

sub Kaigi{
	print "HTTP/1.0 302 Moved Temporarily\n";
	print "Location: ./kaigisitu.cgi" . "\n\n";
}

sub DENGON{
	print "HTTP/1.0 302 Moved Temporarily\n";
	print "Location: ./nph-miniogre.cgi" . "\n\n";
}

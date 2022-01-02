############# ☆ Tactics Ogre de Endless Battle 304 Edition ☆ #############
#
#           _,ィ､ _r､__
#         .ﾍｰ  i｀/　｀i_         config ver1.73
#      /ヾ、ヽ i /　　／ヽ        (last update : 2008/7/14)
#    ｨ､〉>  ￣￣　￣ ｀く_ゝ、
#   },>/ 　　　　 ､　　 ヽ_／ヽ   Modified by Clare Harmolare & Vana & 304
#  ┌!/ /   ｉ「i ヽ  ヽ  ヽ  }
#   Ｙ /  l ハ | l l   l   ',_ゝ  Clare Harmolare - http://ogre.s1.xrea.com/
# 　｜｜  ﾊ/  ﾍl  ll   l    l     vana - http://www.usamimi.info/~antique/
#　 l ｜ /_    l   lﾍ  l    l     304 - ないよー／(^o^)＼ 
#   l ｜//7ﾍ  　 テ=,Vl|    l
#　 ｜ V| Lﾉ  　 {_ ハト    |
# 　｜ ||    .        |ｿ    ﾘ
#    l |ヽ   ._      ｲ||   /
#　  ｜レl＼       ／ﾉ||　｜
#     l  レ ' -┬ '／ ﾚ 　｜
#
##--> Explanation
# ---------------------------------------------------------------------------
#  ひんひん……
# ---------------------------------------------------------------------------
#

#$VER		= 'Version 3.19e';
$VER		= 'Version 1.01a';

$MAIN_SCRIPT	= './nph-battle.cgi';
$HASH_DATA	= '_hash.data';
$KOUKEN_DATA	= 'kouken.data';
$CLASS_DATA	= 'class.data';
$CARD_DATA	= 'card.data';

$WEAPONRAIN_DATA	= '_weaponrainforcement.data';

$CRIMENTE = '0';	#クリスマスメンテナンス
$MENTE		= '0'; #1でメンテナンスモード
$MASTERPASS	= ''; #パスワード
#$MASTERNAME	= 'ヴァナ・ルー'; #イヤーッ！
$MASTERNAME	= '30x'; #／(^o^)＼ 

$WorldWar = '1';		#世界大戦フラグ　1：発動　1以外：不発動		ガリシア側で不具合が発生する
$melchan = '0';			#メルフィ強制表示　1：ON　1以外：OFF
$BattleSort = '2';		#戦闘画面のプレイヤーリスト表示順序　0：Default　1：文字列sort　2：数値でsort

$BattleLevel = '1';		#戦闘力設定　0：通常　1：特殊・魔法7％低下

$ShanFlg = '1';			#シャングリライベント実施　未実装／(^o^)＼ 	ebs4は2大陸時、要注意　世界大戦に注目
$HoushoFlg = '0';		#褒章システム起動　0：起動しない　1：起動
$MVPCALC = '1';			#MVPトロフィー判定　0：通常　1：新型計算

$AbiSys = '0';			#アビリティシステム　PL変数52を使用する PL変数53はアビリティポイントとする　0：なし　1：有り
$ABI_FLG = "A011";		#アビリティキー
$LimitAbiSys = '0';		#リミットアビリティシステム　CL変数52を使用する　CL変数53はリミットポイントとする　0：なし　1：有り
$ChainSys = '0';		#チェインシステム　PL変数54を使用する　※アビリティシステム使用が条件　0：なし　1：有り
$ChainKey = "A001";		#チェインシステム起動キー　チェインシステムに必要　前回実施時と異なるキーをセットした場合、前回分のカウントをクリアする
$ABI_DATA	= '_abi.data';

$CONV_DATA	= '_conv.data';

$NewHoushoFlg = '1';	#新型褒章システム起動　0：起動しない　1：起動
$HoushoKey = "A002";	#新型褒章システム用のキー　前回実施時と異なるキーをセットした場合、貢献値をクリアする

$MemoryFlg = '0';		#記憶の書システム　0：起動しない　1：起動
$MemoryKey = "A001";	#記憶の書システム用のキー　前回実施時と異なるキーをセットした場合、VALUES[56]をクリアする

$WeaponReinForcement = '0';	#武器強化システム　0：起動しない　1：起動

$EntSetting = '1';	#エンチャント付与機能　0：付与しない　1：付与する

$NoSetFlg = '0';		#セット効果無効化　0：セット効果発動　1：セット効果不発動

##管理者(タグ可)
$OWNER_NAME	='30x';
#$OWNER_EMAIL	='ffteb002@yahoo.co.jp';
$OWNER_EMAIL	='xxx';

##大陸名
$CONTINENT_A = "ゼテギネア大陸";	#大陸名1
$CONTINENT_B = "ガリシア大陸";		#大陸名2
$CONTINENT_C = "天宮シャングリラ";	#イベント用

## パスワードの記録ファイルの設定
$pass		= './testes.txt';#必ず名称変更すること

$ICON		= '182';	#最大アイコン数、0から始まり最後のアイコンの数字を記入
$ICON2 = '193';			#キャラクタ絵

#$LOG_FOLDER	= 'arisite';	#ログフォルダ名
#$LOG_FOLDER2	= 'vtbacklog';	#バックアップ用ログフォルダ名
$LOG_FOLDER	= 'testeslog';	#ログフォルダ名
$LOG_FOLDER2	= 'testesbacklog';	#バックアップ用ログフォルダ名

##各種ログファイル名（拡張子不要）
$DB_ID1	= 'hoge';
$DB_ID2 = 'kyantry';
$DB_ID3 = 'shishutory';
$DB_ID4 = 'regein';
$DB_ID5 = 'rireki';

##画像フォルダのパスftp://s500.xrea.com/public_html/ffteb2/img1/xxtitle.gif
$IMG_FOLDER1 = 'http://yohuke.sakura.ne.jp/TOEB/img1';	#ボタン画像
$IMG_FOLDER2 = 'http://yohuke.sakura.ne.jp/TOEB/img2';	#ユニット画像
$IMG_FOLDER3 = 'http://yohuke.sakura.ne.jp/TOEB/img3';	#属性画像
$IMG_FOLDER4 = 'http://yohuke.sakura.ne.jp/TOEB/img4';	#武器画像
$IMG_FOLDER5 = 'http://yohuke.sakura.ne.jp/TOEB/classimage';	#クラス画像
$IMG_FOLDER6 = 'http://yohuke.sakura.ne.jp/TOEB/card';	#タロットカード画像
$IMG_FOLDER7 = 'http://yohuke.sakura.ne.jp/TOEB/img5';	#キャラクタ画像


##リンク
#$YOUR_HOME	= '';	#終了ボタン戻り先
#$YOUR_HOME2	= 'http://w7.oroti.com/~anti/';	#TOPのHOME
#$YOUR_BBS	= 'http://w7.oroti.com/~anti/frame/';	#BBS
#$YOUR_BBS2	= '';
#$YOUR_CHAT	= 'http://cgi40.plala.or.jp/anti/vtoeb/vchat.php';	#CHAT
#$YOUR_CHAT2	= '';
#$YOUR_CHAT3	= '';
#$YOUR_RULES	= 'http://w7.oroti.com/~anti/manual/ma1.html';	#RULES
#$YOUR_CCHAT	= '';

$YOUR_HOME	= '';	#終了ボタン戻り先
$YOUR_HOME2	= 'http://yohuke.sakura.ne.jp/TOEB/index.html';	#TOPのHOME
$YOUR_BBS	= 'https://jbbs.shitaraba.net/game/39710/';	#BBS ffteb2.s500.xrea.com/public_html/ffteb2/
$YOUR_BBS2	= '';
#$YOUR_CHAT	= 'http://ffteb.sakura.ne.jp/vtoeb/vchat.php';	#CHAT sakura
#$YOUR_CHAT	= 'http://cgi42.plala.or.jp/~metal007/owata/vchat.php';	#CHAT plala
$YOUR_CHAT	= 'http://yohuke.sakura.ne.jp/TOEB/cchat.php';	#CHAT plala
#$YOUR_CHAT2	= 'http://cgi42.plala.or.jp/~metal007/owata/vchat2.php';	#CHAT
#$YOUR_CHAT2	= '';
$YOUR_CHAT3	= '';
$YOUR_RULES	= 'http://yohuke.sakura.ne.jp/TOEB/ma1.html';	#RULES
$YOUR_CCHAT	= '';
$YOUR_WIKI = 'https://w.atwiki.jp/304toeb/pages/1.html';
$YOUR_TOR = 'http://yohuke.sakura.ne.jp/TOEB/menu.html';

##各種設定
$COOKIE_KEEP	= '20';		#クッキー保持日数
$COOKIE_KEEP3	= '360';		#この時間（分）以上放置でユニット交代が可能となる
$HOUCHI		= '3';		#放置ユニットの国外退去
$HP_REPAIR	= '0.12';	#1秒間でのHP回復量％
$HP_REPAIR2	= '10';		#1秒間でのHP回復量ハンデ
$EN_REPAIR	= '2';		#1秒間でのEN回復量
$YO_REPAIR	= '30';		#1秒間での要塞回復量
$RISK_REPAIR	= '0.2';	#1秒間でのRISK回復量
$HISTORY_MAX	= '50';		#歴史表示件数（この件数以上は削除されていきます）

$COUNTRY_MAX	= '8';		#最大国存在数(無国籍は含まない)　
#$COUNTRY_MAX2	= '6';		#最大国存在数(無国籍は含まない)　

$ENTRY_MAX	= '500';	#最大登録数
$MAKE_COUNTRY	= '120000';	#建国に必要な費用
$MAKE_TEAM	= '50000';	#部隊作成に必要な費用
$W_MAKE_COUNTRY	= '30000';	#戦争時、建国に必要な費用
$W_MAKE_TEAM	= '10000';	#戦争時、部隊作成に必要な費用
$NAME_TEAM	= '20000';	#部隊名変更に必要な費用
$NAME_YOSAI	= '10000';	#要塞名変更に必要な費用
$YOUSAI_HP	= '300000';	#建国時の初期要塞HP
$WEAPON_RANKUP	= '10';		#武器のランクアップレベル
$WEAPON_LVUP	= '100';	#武器のレベルアップに必要な経験値
$MAX_WEAPONLV	= '99';		#武器レベルの最高値
$GET_MONEY	= '10';		#戦闘後の収入（１～２０くらいの値で設定）

$MAX_HP		= '80000';	#HP上限設定
$MAX_EN		= '4000';	#EN上限設定
$F_MAX_HP	= '10000';	#熟練度FのHP上限設定
$F_MAX_EN	= '1000';	#熟練度FのEN上限設定
$YOUSAI_MAX_HP	= '600000';	#要塞のHP上限設定
$YOUSAI_MAX_ST	= '200';	#要塞のST上限設定

$SATELLITE_FLAG	= '0';		#DataImport/DateExportの許可（1＝許可/0＝不許可）

##選択色（#）は要らない
@COLOR=(
'ffffff',
'dddddd',
'bbbbbb',
#黄色
'ffff88',
'ddff77',
'bbff66',
'99ff55',

'ddffdd',
'bbffbb',
'99ff99',
'77ff77',

'ffffdd',
'ffffbb',
'ffff99',
'ffff77',

'ffdddd',
'ffbbbb',
'ff9999',
'ff7777',
'ff4477',

'ffdd77',
'ffbb66',
'ff8855',

'ffddff',
'ffbbff',
'ff99ff',
'ff77ff',

'ddddff',
'bbbbff',
'9999ff',
'7777ff',

'ddffff',
'bbffff',
'99ffff',
'77ffff',

'ccccbb',
'cccc99',
'cccc77',
'ccdd77',
'ccaa66',
'cc9955',

'd1aeb6',
'd2aea8',
'd3ad9a',
'd6bda3',
'b2bdaa',
'9db4a8',
'9cb5b7',
'9ab6c6',
'9aa8bb',
'9999b0',
'aca0b2',
'bea7b4'

);

##直リン防止
$DIRECT_LINK='1';		#機能を使う？　1=使う/0=使わん
# アクセスを許可するURLをhttp://以下から記述(追加すれば無限)
# ブックマーク・URL直打ち許可の場合はnotと記述。
#$OK_LINK[0] = 'http://w7.oroti.com/~anti/';
#$OK_LINK[1] = 'http://www4.plala.or.jp/anti/';
#$OK_LINK[2] = 'http://cgi40.plala.or.jp/anti/vtoeb/';
$OK_LINK[3] = 'http://yohuke.sakura.ne.jp/TOEB/';
##ブラックリスト
$BLACKCHECK='0';		#機能を使う？　1=使う/0=使わん
# ブラックリスト、IPアドレスでの指定可。(追加すれば無限)
#$DENYHOST[0] = '58.0.254.202';
#$DENYHOST[1] = 'fnttkyo016010.tkyo.fnt.ftth.ppp.infoweb.ne.jp';
#$DENYHOST[2] = '221.30.136.5';
#$DENYHOST[3] = 'softbank221030136005.bbtec.net.';
#$DENYHOST[4] = '218.228.172.';
#$DENYHOST[5] = '218.228.173.';
#$DENYHOST[6] = 'user.ucatv.ne.jp';
#$DENYHOST[7] = '.medias.ne.jp';
#$DENYHOST[8] = 'zaqdb730631.zaq.ne.jp';# durante
#$DENYHOST[9] = '219.115.6.49';# durante
#$DENYHOST[10] = '207.138.99.34';# durante
#$DENYHOST[11] = 's02.a027.ap.plala.or.jp';# durante
#$DENYHOST[12] = 'baicb85d6e1.bai.ne.jp';

#$DENYHOST[0] = 'opt-115-30-175-149.client.pikara.ne.jp';
#$DENYHOST[1] = '.client.pikara.ne.jp';
#$DENYHOST[2] = '.hrs.mesh.ad.jp';


##プロクシチェック
$PROXYCHECK= 1;		#機能を使う？　1=使う/0=使わん
$IP_JP= 1;		# .JPの人だけ通す。 0=いいえ/1=はい/2=ホスト名が無い（IPアドレスだけの）人も許可。
$YAHOOBB= 1;		# 上記を1や2とした場合でも、プロクシ変数を吐いていなければ通す？（一部、ホスト名にJPが付かないプロバイダがあるので…） 1=はい/0=いいえ
$HAITERU= 1;		# 上記を1とした場合は必ず拒否レベル（1か2を）設定する事。プロクシ変数を吐いている人のアクセスを拒否。 0=拒否しない/1=軽く拒否/2=厳密に拒否
$BAREBARE= 1;		# プロクシっぽいホスト名の人のアクセスを拒否。 1=拒否する/0=拒否しない
$BENKYOSHIRO= 0;	# 学校・教育機関からのアクセスを拒否。 1=拒否する/0=拒否しない
$SHIGOTOSHIRO= 0;	# 会社・政府機関からのアクセスを拒否。 1=拒否する/0=拒否しない
$FIRE_WALL= 0;		# ファイアウォール内からのアクセスを拒否。 1=拒否する/0=拒否しない
			# （一部の学校や会社からのアクセスを拒否するにはこのチェックを入れなきゃ駄目。
			# でも、一部の CATVインターネットの人も弾いてしまうので注意！）
$JP_ONLY= 2;		# 日本語をサポートしていないブラウザの人を拒否。
# 0=拒否しない、1=日本語に非対応なら拒否、2=中国語、韓国語を表示可能なら拒否(藁
# 指定ホストのプロクシ制限を回避。ホスト名を|で区切って複数指定可。
# 例：$KYOKA = "catv.ne.jp|uhyo.co.jp|210.233.|navy.mil";
$KYOKA = "133.101.244.|211.124.7.|zaq.ne.jp|kyoto-su.ac.jp|iij4u.or.jp|95.133.|95.132.";

##その他設定
#$UPPER_FRAME='210';	#上部フレームの幅。広告が無い場合210が最適。
$UPPER_FRAME='330';	#上部フレームの幅。広告が無い場合210が最適。
$BANNER_DISPLAY='0';	#広告が入る場合、擬似的に非表示。（1=非表示/0=表示）
$CONFIG_DISPLAY='1';	#TOP画面下部フレームに最大登録人数等のデータ公開（1=公開/0=非公開）
$SPECIAL_ICON='1';	#特殊アイコンの条件（1=Lv200以上且つ熟練度1000以上/0=使用しない）
$S_ICON_NUMBER='588';	#特殊アイコン設定、500.gifから連番で付けた時の最後の番号を記述。
$ICON_SPECIAL='1';	#特殊アイコンの条件（1=Lv300以上且つ熟練度1000以上/0=使用しない）
$ICON_S_NUMBER='797';	#特殊アイコン設定、700.gifから連番で付けた時の最後の番号を記述。
$CICON_SPECIAL='1';	#特殊顔アイコンの条件（1=Lv300以上且つ熟練度1000以上/0=使用しない）
$CICON_S_NUMBER='836';	#特殊顔アイコン設定、700.gifから連番で付けた時の最後の番号を記述。
$NAIRAN_MODE = '1';	#内乱コマンド（1=許可/0=禁止）

#$BACKFR='http://www4.plala.or.jp/anti/back.html';		#通常時下部フレーム 
#$BACKFR='http://cgi42.plala.or.jp/~metal007/TOEB/back.html';		#通常時下部フレーム
$BACKFR='http://yohuke.sakura.ne.jp/TOEB/back.html';		#通常時下部フレーム

##HTMLカスタム
$LINK		= '#D9DBD7';	#リンクの色
$HOVER		= '#D9DBD7';	#リンクにマウスカーソルが乗った時の色

$BG_TOP		= '#373333';	#TOPページの背景色。16進数で色指定するか、画像の場合はURLを入力。
$BG_MAIN	= 'bgo.gif';	#通常時の背景色。16進数で色指定するか、画像の場合はURLを入力。
$BG_STATUS	= '#373333';	#ステータス表示部の背景色
$FONT_COLOR	= '#D9DBD7';	#文字色。16進数で指定。

$TABLE_COLOR1 = '#373333';	#テーブル表示部の色。2色指定。
$TABLE_COLOR2 = '#706666';
$TABLE_COLOR3 = '#373333';	#勢力図などのタイトルの帯の色
$TABLE_BORDER = '#595555';	#テーブル境界線色。
$TABLE_COLOR4 = '#000000';

$BG_BUTTON	= '#484444';	#フォームボタンの背景色
$FC_BUTTON	= '#B3AD9D';	#フォームボタンの文字色

$BG_LIST	= '#484444';	#プルダウンメニューやテキストフォームの背景色
$FC_LIST	= '#DFE1DD';	#プルダウンメニューやテキストフォームの文字色

$BG_SOLID	= '#1A2114';

##アイコン著作権表示
$COPYRIGHT_ICON	='QUEST / SQUARE ENIX';

##世界観の設定
#●各種パラメータの表示名。順番に（攻撃力,防御力,すばやさ,命中率,HP,EN,成長タイプ）
@STATUS_NAME=('STR','VIT','AGI','DEX','HP','MP','Class');

#●改造の表示名。ファンタジー系だと"訓練"など。
$CUSTOM_NAME='鍛練';	

#●階級名。ファンタジー系だと"国王"など。階級を増やしたり減らす事は出来ません。
@CLASS_NAME=('傭兵','二等兵','一等兵','上等兵','兵長','伍長','軍曹','曹長','二等准尉','一等准尉','少尉','中尉','大尉','少佐','中佐','大佐','准将','少将','中将','大将','上級大将','元帥','総帥');

#●無国籍の名称。
$NONE_NATIONALITY	= '無国籍';

@DELE=('デフハーネラ','デフゾショネル','デフバーサ','デフグルーザ');

1;

############# �� Tactics Ogre de Endless Battle 304 Edition �� #############
#
#           _,�B� _r�__
#         .Ͱ  i�M/�@�Mi_         config ver1.73
#      /�S�A�R i /�@�@�^�R        (last update : 2008/7/14)
#    ���r>  �P�P�@�P �M��_�T�A
#   },>/ �@�@�@�@ ��@�@ �R_�^�R   Modified by Clare Harmolare & Vana & 304
#  ��!/ /   ���ui �R  �R  �R  }
#   �x /  l �n | l l   l   ',_�T  Clare Harmolare - http://ogre.s1.xrea.com/
# �@�b�b  �/  �l  ll   l    l     vana - http://www.usamimi.info/~antique/
#�@ l �b /_    l   l�  l    l     304 - �Ȃ���[�^(^o^)�_ 
#   l �b//7�  �@ �e=,Vl|    l
#�@ �b V| L�  �@ {_ �n�g    |
# �@�b ||    .        |�    �
#    l |�R   ._      �||   /
#�@  �b��l�_       �^�||�@�b
#     l  �� ' -�� '�^ � �@�b
#
##--> Explanation
# ---------------------------------------------------------------------------
#  �Ђ�Ђ�c�c
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

$CRIMENTE = '0';	#�N���X�}�X�����e�i���X
$MENTE		= '0'; #1�Ń����e�i���X���[�h
$MASTERPASS	= ''; #�p�X���[�h
#$MASTERNAME	= '���@�i�E���['; #�C���[�b�I
$MASTERNAME	= '30x'; #�^(^o^)�_ 

$WorldWar = '1';		#���E���t���O�@1�F�����@1�ȊO�F�s����		�K���V�A���ŕs�����������
$melchan = '0';			#�����t�B�����\���@1�FON�@1�ȊO�FOFF
$BattleSort = '2';		#�퓬��ʂ̃v���C���[���X�g�\�������@0�FDefault�@1�F������sort�@2�F���l��sort

$BattleLevel = '1';		#�퓬�͐ݒ�@0�F�ʏ�@1�F����E���@7���ቺ

$ShanFlg = '1';			#�V�����O�����C�x���g���{�@�������^(^o^)�_ 	ebs4��2�嗤���A�v���Ӂ@���E���ɒ���
$HoushoFlg = '0';		#�J�̓V�X�e���N���@0�F�N�����Ȃ��@1�F�N��
$MVPCALC = '1';			#MVP�g���t�B�[����@0�F�ʏ�@1�F�V�^�v�Z

$AbiSys = '0';			#�A�r���e�B�V�X�e���@PL�ϐ�52���g�p���� PL�ϐ�53�̓A�r���e�B�|�C���g�Ƃ���@0�F�Ȃ��@1�F�L��
$ABI_FLG = "A011";		#�A�r���e�B�L�[
$LimitAbiSys = '0';		#���~�b�g�A�r���e�B�V�X�e���@CL�ϐ�52���g�p����@CL�ϐ�53�̓��~�b�g�|�C���g�Ƃ���@0�F�Ȃ��@1�F�L��
$ChainSys = '0';		#�`�F�C���V�X�e���@PL�ϐ�54���g�p����@���A�r���e�B�V�X�e���g�p�������@0�F�Ȃ��@1�F�L��
$ChainKey = "A001";		#�`�F�C���V�X�e���N���L�[�@�`�F�C���V�X�e���ɕK�v�@�O����{���ƈقȂ�L�[���Z�b�g�����ꍇ�A�O�񕪂̃J�E���g���N���A����
$ABI_DATA	= '_abi.data';

$CONV_DATA	= '_conv.data';

$NewHoushoFlg = '1';	#�V�^�J�̓V�X�e���N���@0�F�N�����Ȃ��@1�F�N��
$HoushoKey = "A002";	#�V�^�J�̓V�X�e���p�̃L�[�@�O����{���ƈقȂ�L�[���Z�b�g�����ꍇ�A�v���l���N���A����

$MemoryFlg = '0';		#�L���̏��V�X�e���@0�F�N�����Ȃ��@1�F�N��
$MemoryKey = "A001";	#�L���̏��V�X�e���p�̃L�[�@�O����{���ƈقȂ�L�[���Z�b�g�����ꍇ�AVALUES[56]���N���A����

$WeaponReinForcement = '0';	#���틭���V�X�e���@0�F�N�����Ȃ��@1�F�N��

$EntSetting = '1';	#�G���`�����g�t�^�@�\�@0�F�t�^���Ȃ��@1�F�t�^����

$NoSetFlg = '0';		#�Z�b�g���ʖ������@0�F�Z�b�g���ʔ����@1�F�Z�b�g���ʕs����

##�Ǘ���(�^�O��)
$OWNER_NAME	='30x';
#$OWNER_EMAIL	='ffteb002@yahoo.co.jp';
$OWNER_EMAIL	='xxx';

##�嗤��
$CONTINENT_A = "�[�e�M�l�A�嗤";	#�嗤��1
$CONTINENT_B = "�K���V�A�嗤";		#�嗤��2
$CONTINENT_C = "�V�{�V�����O����";	#�C�x���g�p

## �p�X���[�h�̋L�^�t�@�C���̐ݒ�
$pass		= './testes.txt';#�K�����̕ύX���邱��

$ICON		= '182';	#�ő�A�C�R�����A0����n�܂�Ō�̃A�C�R���̐������L��
$ICON2 = '193';			#�L�����N�^�G

#$LOG_FOLDER	= 'arisite';	#���O�t�H���_��
#$LOG_FOLDER2	= 'vtbacklog';	#�o�b�N�A�b�v�p���O�t�H���_��
$LOG_FOLDER	= 'testeslog';	#���O�t�H���_��
$LOG_FOLDER2	= 'testesbacklog';	#�o�b�N�A�b�v�p���O�t�H���_��

##�e�탍�O�t�@�C�����i�g���q�s�v�j
$DB_ID1	= 'hoge';
$DB_ID2 = 'kyantry';
$DB_ID3 = 'shishutory';
$DB_ID4 = 'regein';
$DB_ID5 = 'rireki';

##�摜�t�H���_�̃p�Xftp://s500.xrea.com/public_html/ffteb2/img1/xxtitle.gif
$IMG_FOLDER1 = 'http://yohuke.sakura.ne.jp/TOEB/img1';	#�{�^���摜
$IMG_FOLDER2 = 'http://yohuke.sakura.ne.jp/TOEB/img2';	#���j�b�g�摜
$IMG_FOLDER3 = 'http://yohuke.sakura.ne.jp/TOEB/img3';	#�����摜
$IMG_FOLDER4 = 'http://yohuke.sakura.ne.jp/TOEB/img4';	#����摜
$IMG_FOLDER5 = 'http://yohuke.sakura.ne.jp/TOEB/classimage';	#�N���X�摜
$IMG_FOLDER6 = 'http://yohuke.sakura.ne.jp/TOEB/card';	#�^���b�g�J�[�h�摜
$IMG_FOLDER7 = 'http://yohuke.sakura.ne.jp/TOEB/img5';	#�L�����N�^�摜


##�����N
#$YOUR_HOME	= '';	#�I���{�^���߂��
#$YOUR_HOME2	= 'http://w7.oroti.com/~anti/';	#TOP��HOME
#$YOUR_BBS	= 'http://w7.oroti.com/~anti/frame/';	#BBS
#$YOUR_BBS2	= '';
#$YOUR_CHAT	= 'http://cgi40.plala.or.jp/anti/vtoeb/vchat.php';	#CHAT
#$YOUR_CHAT2	= '';
#$YOUR_CHAT3	= '';
#$YOUR_RULES	= 'http://w7.oroti.com/~anti/manual/ma1.html';	#RULES
#$YOUR_CCHAT	= '';

$YOUR_HOME	= '';	#�I���{�^���߂��
$YOUR_HOME2	= 'http://yohuke.sakura.ne.jp/TOEB/index.html';	#TOP��HOME
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

##�e��ݒ�
$COOKIE_KEEP	= '20';		#�N�b�L�[�ێ�����
$COOKIE_KEEP3	= '360';		#���̎��ԁi���j�ȏ���u�Ń��j�b�g��オ�\�ƂȂ�
$HOUCHI		= '3';		#���u���j�b�g�̍��O�ދ�
$HP_REPAIR	= '0.12';	#1�b�Ԃł�HP�񕜗ʁ�
$HP_REPAIR2	= '10';		#1�b�Ԃł�HP�񕜗ʃn���f
$EN_REPAIR	= '2';		#1�b�Ԃł�EN�񕜗�
$YO_REPAIR	= '30';		#1�b�Ԃł̗v�ǉ񕜗�
$RISK_REPAIR	= '0.2';	#1�b�Ԃł�RISK�񕜗�
$HISTORY_MAX	= '50';		#���j�\�������i���̌����ȏ�͍폜����Ă����܂��j

$COUNTRY_MAX	= '8';		#�ő卑���ݐ�(�����Ђ͊܂܂Ȃ�)�@
#$COUNTRY_MAX2	= '6';		#�ő卑���ݐ�(�����Ђ͊܂܂Ȃ�)�@

$ENTRY_MAX	= '500';	#�ő�o�^��
$MAKE_COUNTRY	= '120000';	#�����ɕK�v�Ȕ�p
$MAKE_TEAM	= '50000';	#�����쐬�ɕK�v�Ȕ�p
$W_MAKE_COUNTRY	= '30000';	#�푈���A�����ɕK�v�Ȕ�p
$W_MAKE_TEAM	= '10000';	#�푈���A�����쐬�ɕK�v�Ȕ�p
$NAME_TEAM	= '20000';	#�������ύX�ɕK�v�Ȕ�p
$NAME_YOSAI	= '10000';	#�v�ǖ��ύX�ɕK�v�Ȕ�p
$YOUSAI_HP	= '300000';	#�������̏����v��HP
$WEAPON_RANKUP	= '10';		#����̃����N�A�b�v���x��
$WEAPON_LVUP	= '100';	#����̃��x���A�b�v�ɕK�v�Ȍo���l
$MAX_WEAPONLV	= '99';		#���탌�x���̍ō��l
$GET_MONEY	= '10';		#�퓬��̎����i�P�`�Q�O���炢�̒l�Őݒ�j

$MAX_HP		= '80000';	#HP����ݒ�
$MAX_EN		= '4000';	#EN����ݒ�
$F_MAX_HP	= '10000';	#�n���xF��HP����ݒ�
$F_MAX_EN	= '1000';	#�n���xF��EN����ݒ�
$YOUSAI_MAX_HP	= '600000';	#�v�ǂ�HP����ݒ�
$YOUSAI_MAX_ST	= '200';	#�v�ǂ�ST����ݒ�

$SATELLITE_FLAG	= '0';		#DataImport/DateExport�̋��i1������/0���s���j

##�I��F�i#�j�͗v��Ȃ�
@COLOR=(
'ffffff',
'dddddd',
'bbbbbb',
#���F
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

##�������h�~
$DIRECT_LINK='1';		#�@�\���g���H�@1=�g��/0=�g���
# �A�N�Z�X��������URL��http://�ȉ�����L�q(�ǉ�����Ζ���)
# �u�b�N�}�[�N�EURL���ł����̏ꍇ��not�ƋL�q�B
#$OK_LINK[0] = 'http://w7.oroti.com/~anti/';
#$OK_LINK[1] = 'http://www4.plala.or.jp/anti/';
#$OK_LINK[2] = 'http://cgi40.plala.or.jp/anti/vtoeb/';
$OK_LINK[3] = 'http://yohuke.sakura.ne.jp/TOEB/';
##�u���b�N���X�g
$BLACKCHECK='0';		#�@�\���g���H�@1=�g��/0=�g���
# �u���b�N���X�g�AIP�A�h���X�ł̎w��B(�ǉ�����Ζ���)
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


##�v���N�V�`�F�b�N
$PROXYCHECK= 1;		#�@�\���g���H�@1=�g��/0=�g���
$IP_JP= 1;		# .JP�̐l�����ʂ��B 0=������/1=�͂�/2=�z�X�g���������iIP�A�h���X�����́j�l�����B
$YAHOOBB= 1;		# ��L��1��2�Ƃ����ꍇ�ł��A�v���N�V�ϐ���f���Ă��Ȃ���Βʂ��H�i�ꕔ�A�z�X�g����JP���t���Ȃ��v���o�C�_������̂Łc�j 1=�͂�/0=������
$HAITERU= 1;		# ��L��1�Ƃ����ꍇ�͕K�����ۃ��x���i1��2���j�ݒ肷�鎖�B�v���N�V�ϐ���f���Ă���l�̃A�N�Z�X�����ہB 0=���ۂ��Ȃ�/1=�y������/2=�����ɋ���
$BAREBARE= 1;		# �v���N�V���ۂ��z�X�g���̐l�̃A�N�Z�X�����ہB 1=���ۂ���/0=���ۂ��Ȃ�
$BENKYOSHIRO= 0;	# �w�Z�E����@�ւ���̃A�N�Z�X�����ہB 1=���ۂ���/0=���ۂ��Ȃ�
$SHIGOTOSHIRO= 0;	# ��ЁE���{�@�ւ���̃A�N�Z�X�����ہB 1=���ۂ���/0=���ۂ��Ȃ�
$FIRE_WALL= 0;		# �t�@�C�A�E�H�[��������̃A�N�Z�X�����ہB 1=���ۂ���/0=���ۂ��Ȃ�
			# �i�ꕔ�̊w�Z���Ђ���̃A�N�Z�X�����ۂ���ɂ͂��̃`�F�b�N�����Ȃ���ʖځB
			# �ł��A�ꕔ�� CATV�C���^�[�l�b�g�̐l���e���Ă��܂��̂Œ��ӁI�j
$JP_ONLY= 2;		# ���{����T�|�[�g���Ă��Ȃ��u���E�U�̐l�����ہB
# 0=���ۂ��Ȃ��A1=���{��ɔ�Ή��Ȃ狑�ہA2=������A�؍����\���\�Ȃ狑��(�m
# �w��z�X�g�̃v���N�V����������B�z�X�g����|�ŋ�؂��ĕ����w��B
# ��F$KYOKA = "catv.ne.jp|uhyo.co.jp|210.233.|navy.mil";
$KYOKA = "133.101.244.|211.124.7.|zaq.ne.jp|kyoto-su.ac.jp|iij4u.or.jp|95.133.|95.132.";

##���̑��ݒ�
#$UPPER_FRAME='210';	#�㕔�t���[���̕��B�L���������ꍇ210���œK�B
$UPPER_FRAME='330';	#�㕔�t���[���̕��B�L���������ꍇ210���œK�B
$BANNER_DISPLAY='0';	#�L��������ꍇ�A�[���I�ɔ�\���B�i1=��\��/0=�\���j
$CONFIG_DISPLAY='1';	#TOP��ʉ����t���[���ɍő�o�^�l�����̃f�[�^���J�i1=���J/0=����J�j
$SPECIAL_ICON='1';	#����A�C�R���̏����i1=Lv200�ȏ㊎�n���x1000�ȏ�/0=�g�p���Ȃ��j
$S_ICON_NUMBER='588';	#����A�C�R���ݒ�A500.gif����A�Ԃŕt�������̍Ō�̔ԍ����L�q�B
$ICON_SPECIAL='1';	#����A�C�R���̏����i1=Lv300�ȏ㊎�n���x1000�ȏ�/0=�g�p���Ȃ��j
$ICON_S_NUMBER='797';	#����A�C�R���ݒ�A700.gif����A�Ԃŕt�������̍Ō�̔ԍ����L�q�B
$CICON_SPECIAL='1';	#�����A�C�R���̏����i1=Lv300�ȏ㊎�n���x1000�ȏ�/0=�g�p���Ȃ��j
$CICON_S_NUMBER='836';	#�����A�C�R���ݒ�A700.gif����A�Ԃŕt�������̍Ō�̔ԍ����L�q�B
$NAIRAN_MODE = '1';	#�����R�}���h�i1=����/0=�֎~�j

#$BACKFR='http://www4.plala.or.jp/anti/back.html';		#�ʏ펞�����t���[�� 
#$BACKFR='http://cgi42.plala.or.jp/~metal007/TOEB/back.html';		#�ʏ펞�����t���[��
$BACKFR='http://yohuke.sakura.ne.jp/TOEB/back.html';		#�ʏ펞�����t���[��

##HTML�J�X�^��
$LINK		= '#D9DBD7';	#�����N�̐F
$HOVER		= '#D9DBD7';	#�����N�Ƀ}�E�X�J�[�\������������̐F

$BG_TOP		= '#373333';	#TOP�y�[�W�̔w�i�F�B16�i���ŐF�w�肷�邩�A�摜�̏ꍇ��URL����́B
$BG_MAIN	= 'bgo.gif';	#�ʏ펞�̔w�i�F�B16�i���ŐF�w�肷�邩�A�摜�̏ꍇ��URL����́B
$BG_STATUS	= '#373333';	#�X�e�[�^�X�\�����̔w�i�F
$FONT_COLOR	= '#D9DBD7';	#�����F�B16�i���Ŏw��B

$TABLE_COLOR1 = '#373333';	#�e�[�u���\�����̐F�B2�F�w��B
$TABLE_COLOR2 = '#706666';
$TABLE_COLOR3 = '#373333';	#���͐}�Ȃǂ̃^�C�g���̑т̐F
$TABLE_BORDER = '#595555';	#�e�[�u�����E���F�B
$TABLE_COLOR4 = '#000000';

$BG_BUTTON	= '#484444';	#�t�H�[���{�^���̔w�i�F
$FC_BUTTON	= '#B3AD9D';	#�t�H�[���{�^���̕����F

$BG_LIST	= '#484444';	#�v���_�E�����j���[��e�L�X�g�t�H�[���̔w�i�F
$FC_LIST	= '#DFE1DD';	#�v���_�E�����j���[��e�L�X�g�t�H�[���̕����F

$BG_SOLID	= '#1A2114';

##�A�C�R�����쌠�\��
$COPYRIGHT_ICON	='QUEST / SQUARE ENIX';

##���E�ς̐ݒ�
#���e��p�����[�^�̕\�����B���ԂɁi�U����,�h���,���΂₳,������,HP,EN,�����^�C�v�j
@STATUS_NAME=('STR','VIT','AGI','DEX','HP','MP','Class');

#�������̕\�����B�t�@���^�W�[�n����"�P��"�ȂǁB
$CUSTOM_NAME='�b��';	

#���K�����B�t�@���^�W�[�n����"����"�ȂǁB�K���𑝂₵���茸�炷���͏o���܂���B
@CLASS_NAME=('�b��','�񓙕�','�ꓙ��','�㓙��','����','�ޒ�','�R��','����','�񓙏y��','�ꓙ�y��','����','����','���','����','����','�卲','�y��','����','����','�叫','�㋉�叫','����','����');

#�������Ђ̖��́B
$NONE_NATIONALITY	= '������';

@DELE=('�f�t�n�[�l��','�f�t�]�V���l��','�f�t�o�[�T','�f�t�O���[�U');

1;

############################# �l�}�� (txt��)#############################
#
#�����̃t�@�C�����@zukan.cgi�@�ŃA�b�v���[�h�Bebs.cgi�Ɠ����t�H���_�i�K�w�j
#
#�� zukan�@�Ƃ������O�̃t�H���_���A�b�v���[�h
#
#��ebs.cgi�ɒǉ�
#
#	sub ZUKAN		{require 'zukan.cgi';&ZUKAN2;}
#	sub ETURAN		{require 'zukan.cgi';&ETURAN2;}
#	sub TOUROKU		{require 'zukan.cgi';&TOUROKU2;&ZUKAN;}
#
#
#���{�^���ǉ�
#
#	��sub3�̏ꍇ��
#
#	<td><input type=submit value="����" $STYLE_B1 onClick="document.FM.cmd.value='ZUKAN';Move()"></td>
#
#	��sub5�̏ꍇ��
#
#	$sp.= "<input type=\"submit\" value=\"����\" $STYLE_B1 onClick=\"document.Ms.cmd.value='ZUKAN';\">";
#
#���o�^���ɕ���͂Ȃ��Ȃ�܂���B
#�@�Ȃ����Ȃ牺�̕��̃R�����g�A�E�g��2�����O���Ă��������B
#
# ���̃X�N���v�g�Ɋւ��Ă̎��ⓙ�́A
# ���f��������܂��̂ő��T�C�g�l�Ŏ��₵�Ȃ��悤�肢�܂��B
# http://www4.plala.or.jp/at-s/ebs/
#<input type=submit value='�߂�' $STYLE_B1 onClick="document.BM.target='Main';document.BM.cmd.value='MAIN_FRAME';parent.Sub.location.replace('$MAIN_SCRIPT?LOGO');">
####################################################################

@w_yobi=(9,10,11,38,41,42,43,46);	# $PL_VALUES�̔ԍ��i�o�^�j
#@dame=('zzzz',"100a","102a","103a","104a","109a","116a","200a","231a","231aa","231aaa","231aaaa","269","270","273a","274a","275a","276a","277a","278a");		# �o�^�����Ȃ�����
@dame=('2fi',"2fj","102a","2hg","2hh","2hi","2hj","2hk","2hl","2ho","2hy","2ia","4gj","6ga","6gaa","6gab","6gac","6gad","6gae","1025a","1026a","1027a","1028a","1028aa","1031a","1031aa","1029a","1030a","1032a","1032aa","2gl","2gn","2go","2he","2hf","2ht");
$Z_DIR="hhhzukan304";		# �ۑ�����f�B���N�g���i�t�H���_�j

require "./$LOG_FOLDER/$HASH_DATA";

######################## �ݒ肱���܂� ##############################

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

	#���\�ω���������舵��
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
	&ERROR('�f�B���N�g����������܂���') unless (-e $Z_DIR);
	$LOG="$Z_DIR/$FORM{'pname'}\.txt";
	@ZUKAN=();
	&LOCK;
	&DBM_CONVERT('P',"$FORM{'pname'}");
	&READ($LOG) if (-e $LOG);
	&UNLOCK;
	&ERROR('�p�X���[�h�G���[') if $PL_VALUES[2] ne crypt($FORM{'pass'},eb);
	my $num1=@ZUKAN;
	#my $num2=(keys %WEAPON_LIST)-@dame;
	$num2="�H�H�H";
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
		$yobi.="<input type=submit value='�o�^' $STYLE_B1 onClick=\"document.BM.target='Sub';document.BM.cmd.value='TOUROKU';return checkZK()\">\n";
	}
	$yobi ||='�o�^�ł��镐�킪����܂���B';
	&HEADER;
	&JScfm(checkZK,"�}�ӂɓo�^���܂��B��낵���ł����H") if $zflag;
$Sort="<select size=1 name=\"sortlist\" $STYLE_B1>";
$Sort .="<option value=A01>�S��</option>";
$Sort .="<option value=A02>����</option>";
$Sort .="<option value=A03>�h��</option>";
$Sort .="<option value=A33>����</option>";
$Sort .="<option value=A10>��</option>";
$Sort .="<option value=A11>��</option>";
$Sort .="<option value=A12>��</option>";
$Sort .="<option value=A13>��</option>";
$Sort .="<option value=A14>��</option>";
$Sort .="<option value=A15>��</option>";
$Sort .="<option value=A16>��</option>";
$Sort .="<option value=A17>�l�`</option>";
$Sort .="<option value=A18>��</option>";
$Sort .="<option value=A19>�|</option>";
$Sort .="<option value=A20>������</option>";
$Sort .="<option value=A21>�e</option>";
$Sort .="<option value=A22>��</option>";
$Sort .="<option value=A23>�ˌ�</option>";
$Sort .="<option value=A24>���@</option>";
$Sort .="<option value=A25>����</option>";
$Sort .="<option value=A26>�K�E�Z</option>";
$Sort .="<option value=A27>���h��</option>";
$Sort .="<option value=A28>�̖h��</option>";
$Sort .="<option value=A29>��</option>";
$Sort .="<option value=A30>�����i</option>";
$Sort .="<option value=A31>���̑�</option>";
$Sort .="<option value=A32>�{</option>";
$Sort .= "</select>";
	print <<"-----END-----";
<form action=$MAIN_SCRIPT name="BM" method="POST">
<input type=hidden name=cmd>
<input type=hidden name=pname value=$FORM{'pname'}>
<input type=hidden name=pass value=$FORM{'pass'}>
<table bordercolor=$TABLE_BORDER border=1 cellspacing=0 cellpadding=2 style="font-size:13px;">
<tr><th bgcolor=$TABLE_COLOR2>�����}��</th></tr>
<tr><td valign=top>$yobi</td></tr>
<tr><td align=right>
$Sort<b>�i$num1/$num2�j</b>&nbsp;
<input type=submit value='�{��' $STYLE_B1 onClick="document.BM.target='Sub';document.BM.cmd.value='ETURAN'">
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
	&ERROR('�p�X���[�h�G���[') if $PL_VALUES[2] ne crypt($FORM{'pass'},eb);
	sub KOUKA {
		my @W=split /\,/,$WEAPON_LIST{"$_[0]"};
		my $ritu=$W[2] > 100 ? 1 : $W[2]/100;

		my $point="???";

#		return;
	@COLOR = ('#5000CC','#5000CC','#8000ff','#a000e5','#bf00cc','#df00a6','#ff0080','#f7e957','#f7e957','#f7e957','#f7e957','#ff0080','#ff0080','#ff0080');

	@STATUS = ('G','F','E','D','C','B','A','H','S','SS','SSS','ACE','NT','Max');

	if($BattleLevel eq "1"){
		#�ŏ�i�̕���
#		if($W[11] eq "0" && $W[14] =~ m/A02/){
#			$W[1] = int($W[1] * 0.97);
##			$W[2] = int($W[2] * 0.97);
#		}
		#�Z
#		if($W[11] eq "5"){
#			$W[1]-=50;
#		}
		#���@
		if($W[11] eq "1" || $W[11] eq "2" || $W[11] eq "3"){
			$W[1] = int($W[1]*0.9);
#			$W[2] = int($W[2]*0.95);
		}
		#����
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

		#��
		if($W[7]=~ m/!12/){
			$eres=int($W[1]);
		#�w��
		}elsif ($W[7] =~ m/!13/){
			$estr=int($W[10]);
			$edex=int($W[1]);
		#�I�[�u
		}elsif ($W[7] =~ m/!14/){
			$eini=int($W[10]);
		#��E��
		}elsif ($W[7] =~ m/!15|!19/){
			$eint=int($W[10]);
		#�C
		}elsif ($W[7] =~ m/!16/){
			$eagi=int($W[1]);
		#�����i
		}elsif ($W[7] =~ m/!17/){
			$eagi=int($W[1]);
			$edex=int($W[10]);
		#�̖h��1
		}elsif ($W[7] =~ m/!1s/){
			$eres=int($W[1]);
		#���h��1
		}elsif ($W[7] =~ m/!1t/){
			$eres=int($W[1]);
		#���h��2
		}elsif ($W[7] =~ m/!E0003/){
			$eres=int($W[1]);
			$estr=int(3);
			$eagi=int(1);
		#�̖h��2
		}elsif ($W[7] =~ m/!1u/){
			$eres=int($W[1]);
			$edex=int($W[1]/3);
		#���h��3
		}elsif ($W[7] =~ m/!1v/){
			$eres=int($W[1]);
			$eagi=int($W[10]);
		#�̖h��3
		}elsif ($W[7] =~ m/!1w/){
			$eres=int($W[1]);
			$eint=int($W[10]);
		#���h��4
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
			$kouka.="�Ў�&nbsp;" if $W[7] =~ m/!10/;
			$kouka.="����&nbsp;" if $W[7] =~ m/!11/;
			$kouka.="��&nbsp;" if $W[7] =~ m/!12/;
			$kouka.="�w��&nbsp;" if $W[7] =~ m/!13/;
			$kouka.="�I�[�u&nbsp;" if $W[7] =~ m/!14/;
			$kouka.="��&nbsp;" if $W[7] =~ m/!15/;
			$kouka.="�C&nbsp;" if $W[7] =~ m/!16/;
			$kouka.="�����i&nbsp;" if $W[7] =~ m/!17/;
			$kouka.="���@&nbsp;" if $W[7] =~ m/!18/;
			$kouka.="��&nbsp;" if $W[7] =~ m/!19/;
			$kouka.="�|&nbsp;" if $W[7] =~ m/!1a/;
			$kouka.="�e&nbsp;" if $W[7] =~ m/!1b/;
			$kouka.="������&nbsp;" if $W[7] =~ m/!1c/;
			$kouka.="����&nbsp;" if $W[7] =~ m/!1d/;
			$kouka.="��&nbsp;" if $W[7] =~ m/!1e/;
			$kouka.="��&nbsp;" if $W[7] =~ m/!1f/;
			$kouka.="������&nbsp;" if $W[7] =~ m/!1g/;
			$kouka.="����&nbsp;" if $W[7] =~ m/!1h/;
			$kouka.="�h���S���u���X&nbsp;" if $W[7] =~ m/!1k/;
			$kouka.="���b�X�y�V����&nbsp;" if $W[7] =~ m/!1l/;
			$kouka.="����&nbsp;" if $W[7] =~ m/!1m/;
			$kouka.="���Օi&nbsp;" if $W[7] =~ m/!1n/;
			$kouka.="�g�ѕi&nbsp;" if $W[7] =~ m/!1o/;
			$kouka.="�h�[��&nbsp;" if $W[7] =~ m/!1p/;
			$kouka.="�⏕&nbsp;" if $W[7] =~ m/!1q/;
			$kouka.="������&nbsp;" if $W[7] =~ m/!1r/;
			$kouka.="�̖h��&nbsp;" if $W[7] =~ m/!1s|!1u|!1w|!E0001/;
			$kouka.="���h��&nbsp;" if $W[7] =~ m/!1t|!1v|!1x|!E0003/;
			$kouka.="����&nbsp;" if $W[14] =~ m/A33/;
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
			$kouka2.="�Ӑg&nbsp;" if $W[7] =~ m/!20/;
			$kouka2.="�K�E&nbsp;" if $W[7] =~ m/!21/;
			$kouka2.="�U��&nbsp;" if $W[7] =~ m/!22/;
			$kouka2.="�h��&nbsp;" if $W[7] =~ m/!23/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!24/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!25/;
			$kouka2.="�h��&nbsp;" if $W[7] =~ m/!26/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!27/;
			$kouka2.="�{��&nbsp;" if $W[7] =~ m/!28/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!29/;
			$kouka2.="��&nbsp;" if $W[7] =~ m/!2a/;
			$kouka2.="��&nbsp;" if $W[7] =~ m/!2b/;
			$kouka2.="���&nbsp;" if $W[7] =~ m/!2c/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!2d/;
			$kouka2.="�Ή�&nbsp;" if $W[7] =~ m/!2e/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!2f/;
			$kouka2.="�m�b�N�o�b�N&nbsp;" if $W[7] =~ m/!2g/;
			$kouka2.="�����]��&nbsp;" if $W[7] =~ m/!2h/;
			$kouka2.="MHP��&nbsp;" if $W[7] =~ m/!2j/;
			$kouka2.="MP��&nbsp;" if $W[7] =~ m/!2k/;
			$kouka2.="�p���[�_�E��&nbsp;" if $W[7] =~ m/!2o/;
			$kouka2.="�p���[�A�b�v&nbsp;" if $W[7] =~ m/!2p/;
			$kouka2.="�p���[�_�E���t�^&nbsp;" if $W[7] =~ m/!2q/;
			$kouka2.="�p���[�A�b�v�t�^&nbsp;" if $W[7] =~ m/!2r/;
			$kouka2.="�G�������g�u���C�N&nbsp;" if $W[7] =~ m/!2s/;
			$kouka2.="SP_short&nbsp;" if $W[7] =~ m/!30/;
			$kouka2.="SP_middle&nbsp;" if $W[7] =~ m/!31/;
			$kouka2.="SP_long&nbsp;" if $W[7] =~ m/!32/;
			$kouka2.="�Ӑg����&nbsp;" if $W[7] =~ m/!40/;
			$kouka2.="�K�E����&nbsp;" if $W[7] =~ m/!41/;
			$kouka2.="�{�薳��&nbsp;" if $W[7] =~ m/!42/;
			$kouka2.="���ݖ���&nbsp;" if $W[7] =~ m/!43/;
			$kouka2.="�􂢖���&nbsp;" if $W[7] =~ m/!44/;
			$kouka2.="�Ŗ���&nbsp;" if $W[7] =~ m/!45/;
			$kouka2.="��ზ���&nbsp;" if $W[7] =~ m/!46/;
			$kouka2.="��������&nbsp;" if $W[7] =~ m/!47/;
			$kouka2.="�Ή�����&nbsp;" if $W[7] =~ m/!48/;
			$kouka2.="��������&nbsp;" if $W[7] =~ m/!49/;
			$kouka2.="��Ԉُ햳��&nbsp;" if $W[7] =~ m/!4a/;
			$kouka2.="���W�X�g&nbsp;" if $W[7] =~ m/!4b/;
			$kouka2.="���_��&nbsp;" if $W[7] =~ m/!50/;
			$kouka2.="�I�E�K�V���[�Y&nbsp;" if $W[7] =~ m/!51/;
			$kouka2.="�Í�������&nbsp;" if $W[7] =~ m/!52/;
			$kouka2.="��l�K�{����&nbsp;" if $W[7] =~ m/!53/;
			$kouka2.="������&nbsp;" if $W[7] =~ m/!54/;
			$kouka2.="���َq&nbsp;" if $W[7] =~ m/!55/;
			$kouka2.="���E�l����&nbsp;" if $W[7] =~ m/!56/;
			$kouka2.="���N�̍�&nbsp;" if $W[7] =~ m/!57/;
			$kouka2.="�����̍�&nbsp;" if $W[7] =~ m/!58/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!60/;
			$kouka2.="�����u���X&nbsp;" if $W[7] =~ m/!61/;
			$kouka2.="������ʃu���X&nbsp;" if $W[7] =~ m/!62/;
			$kouka2.="�R�b���N�e�B�I&nbsp;" if $W[7] =~ m/!63/;
			$kouka2.="�V���C�j���O&nbsp;" if $W[7] =~ m/!64/;
			$kouka2.="�h���b�O�C�[�^�[&nbsp;" if $W[7] =~ m/!65/;
			$kouka2.="�p���v�L���{��&nbsp;" if $W[7] =~ m/!66/;
			$kouka2.="���ڂ��Ⴄ���[��&nbsp;" if $W[7] =~ m/!67/;
			$kouka2.="�A�V�F����&nbsp;" if $W[7] =~ m/!68/;
			$kouka2.="���[�h�I�u�y�C��&nbsp;" if $W[7] =~ m/!69/;
			$kouka2.="�Ζ��@&nbsp;" if $W[7] =~ m/!6a/;
			$kouka2.="���C�t�u���C�N&nbsp;" if $W[7] =~ m/!6b/;
			$kouka2.="����&nbsp;" if $W[7] =~ m/!6c/;
			$kouka2.="������&nbsp;" if $W[7] =~ m/!6f/;
			$kouka2.="�G���W�F���i�C�g����&nbsp;" if $W[7] =~ m/!6g/;
			$kouka2.="Special&nbsp;" if $W[7] =~ m/!6h/;
			$kouka2.="���@�̃��b�p&nbsp;" if $W[7] =~ m/!6i/;
			$kouka2.="�q�[�����O&nbsp;" if $W[7] =~ m/!6j/;
			$kouka2.="�q�[�����O�I�[��&nbsp;" if $W[7] =~ m/!6k/;
			$kouka2.="���U���N�V����&nbsp;" if $W[7] =~ m/!6l/;
			$kouka2.="�`���[�W�X�y��&nbsp;" if $W[7] =~ m/!6m/;
			$kouka2.="�I�[���@�[�h���C��&nbsp;" if $W[7] =~ m/!6n/;
			$kouka2.="��&nbsp;" if $W[7] =~ m/!6o/;
			$kouka2.="�}�X�^�o�̌��E&nbsp;" if $W[7] =~ m/!6p/;
			$kouka2.="�}�[�`���O�o�g��&nbsp;" if $W[7] =~ m/!6q/;
			$kouka2.="���|�w�쏑&nbsp;" if $W[7] =~ m/!6r/;
			$kouka2.="decrease&nbsp;" if $W[7] =~ m/!6s/;
			$kouka2.="�g�����X�t�@�[&nbsp;" if $W[7] =~ m/!6t/;
			$kouka2.="�����&nbsp;" if $W[7] =~ m/!6u/;
			$kouka2.="���o�C�o��&nbsp;" if $W[7] =~ m/!6v/;
			$kouka2.="�K�E�Z&nbsp;" if $W[7] =~ m/!6w/;
			$kouka2.="�����g�_�E��&nbsp;" if $W[7] =~ m/!6x/;
			$kouka2.="�I�[���T�����Y&nbsp;" if $W[7] =~ m/!6y/;
			$kouka2.="�q�[�����O�v���X&nbsp;" if $W[7] =~ m/!6z/;
			$kouka2.="�e���|�[�g&nbsp;" if $W[7] =~ m/!70/;
			$kouka2.="�[�e�M�l�A�嗤����h���b�v&nbsp;" if $W[7] =~ m/!71/;
			$kouka2.="�K���V�A�嗤����h���b�v&nbsp;" if $W[7] =~ m/!72/;
			$kouka2.="LvUP��MP��&nbsp;" if $W[7] =~ m/!73/;
			$kouka2.="���W�F�l���C�g&nbsp;" if $W[7] =~ m/!74/;
			$kouka2.="���|&nbsp;" if $W[7] =~ m/!75/;
			$kouka2.="�q�[�����O�v���X&nbsp;" if $W[7] =~ m/!76/;
			$kouka2.="�l�N���}���V�[&nbsp;" if $W[7] =~ m/!77/;
			$kouka2.="�}�[�V�[���C��&nbsp;" if $W[7] =~ m/!78/;
			$kouka2.="�}�[�e�B���C�Y&nbsp;" if $W[7] =~ m/!79/;
			$kouka2.="1500�q�[��&nbsp;" if $W[7] =~ m/!80/;
			$kouka2.="���L���o���C�g&nbsp;" if $W[7] =~ m/!81/;
			$kouka2.="MP100�`���[�W&nbsp;" if $W[7] =~ m/!82/;
			$kouka2.="�f�t�n�[�l��&nbsp;" if $W[7] =~ m/!83/;
			$kouka2.="�f�t�]�V���l��&nbsp;" if $W[7] =~ m/!84/;
			$kouka2.="�f�t�o�[�T&nbsp;" if $W[7] =~ m/!85/;
			$kouka2.="�f�t�O���[�U&nbsp;" if $W[7] =~ m/!86/;
			$kouka2.="�T�����C�V���^��&nbsp;" if $W[7] =~ m/!87/;
			$kouka2.="�T�����A�X���f&nbsp;" if $W[7] =~ m/!88/;
			$kouka2.="�T�����]�V���l��&nbsp;" if $W[7] =~ m/!89/;
			$kouka2.="�T�����O���[�U&nbsp;" if $W[7] =~ m/!8a/;
			$kouka2.="�T�����n�[�l��&nbsp;" if $W[7] =~ m/!8b/;
			$kouka2.="�T�����o�[�T&nbsp;" if $W[7] =~ m/!8c/;
			$kouka2.="�����U��&nbsp;" if $W[7] =~ m/!8d/;
			$kouka2.="�W�����v�E�H�[��&nbsp;" if $W[7] =~ m/!8e/;
			$kouka2.="�e���|�[�g&nbsp;" if $W[7] =~ m/!8f/;
			$kouka2.="�⏕���@&nbsp;" if $W[7] =~ m/!8g/;
			$kouka2.="������&nbsp;" if $W[7] =~ m/!8h/;
			$kouka2.="�}�[�V�[���C��&nbsp;" if $W[7] =~ m/!8i/;
			$kouka2.="�}�[�e�B���C�Y&nbsp;" if $W[7] =~ m/!8j/;
			$kouka2.="�X�^���X���[�^�[&nbsp;" if $W[7] =~ m/!8k/;
			$kouka2.="�X�����o�[�~�X�g&nbsp;" if $W[7] =~ m/!8l/;
			$kouka2.="�|�C�Y���N���E�h&nbsp;" if $W[7] =~ m/!8m/;
			$kouka2.="�y�g���N���E�h&nbsp;" if $W[7] =~ m/!8n/;
			$kouka2.="�L���A���[�t[HP4000��]&nbsp;" if $W[7] =~ m/!E0015/;
			$kouka2.="�L���A�V�[�h[HP12000��]&nbsp;" if $W[7] =~ m/!E0016/;
			$kouka2.="�L���A�y�[�X�g[HP36000��]&nbsp;" if $W[7] =~ m/!E0017/;
			$kouka2.="�L���A�G�L�X[HP�S��]&nbsp;" if $W[7] =~ m/!E0018/;
			$kouka2.="�}�W�b�N���[�t[MP150��]&nbsp;" if $W[7] =~ m/!E0019/;
			$kouka2.="�}�W�b�N�V�[�h[MP400��]&nbsp;" if $W[7] =~ m/!E0020/;
			$kouka2.="�}�W�b�N�y�[�X�g[MP900��]&nbsp;" if $W[7] =~ m/!E0021/;
			$kouka2.="�}�W�b�N�G�L�X[MP1500��]&nbsp;" if $W[7] =~ m/!E0022/;
			$kouka2.="���҂̉ʎ�[HP25000&nbsp;MP800��]&nbsp;" if $W[7] =~ m/!E0023/;
			$kouka2.="�V�g�̉ʎ�[HPMP�S��]&nbsp;" if $W[7] =~ m/!E0024/;
			$kouka2.="���肩�����ʎ�[���g�̏������镔���S����HP��&nbsp;���g�͐퓬�s�\\]&nbsp;" if $W[7] =~ m/!E0025/;
			$kouka2.="���̑�[�\\���퓬����������&nbsp;�퓬���̐��E�������_���[�W+20��]&nbsp;" if $W[7] =~ m/!E0026/;
			$kouka2.="�I�x�����̗�[�\\���퓬����������&nbsp;�퓬���̉��E��n�����_���[�W+20��]&nbsp;" if $W[7] =~ m/!E0027/;
			$kouka2.="�ؑ��̊p�J[�\\���퓬����������&nbsp;�퓬���̐��E�������_���[�W+5��]&nbsp;" if $W[7] =~ m/!E0028/;
			$kouka2.="�T���S�̒G��[�\\���퓬����������&nbsp;�퓬���̉��E��n�����_���[�W+5��]&nbsp;" if $W[7] =~ m/!E0029/;
			$kouka2.="���o�C�u�X�g�[��[�Ή����ʂ��󂯂��ۂɎ�������&nbsp;�Ή�������]&nbsp;" if $W[7] =~ m/!E0030/;
			$kouka2.="�A���`�h�[�e[�Ō��ʂ��󂯂��ۂɎ�������&nbsp;�Ŗ�����]&nbsp;" if $W[7] =~ m/!E0031/;
			$kouka2.="�p���u���[�W�A[��჌��ʂ��󂯂��ۂɎ�������&nbsp;��ზ�����]&nbsp;" if $W[7] =~ m/!E0032/;
			$kouka2.="�A�E�F�C�L���O[������ʂ��󂯂��ۂɎ�������&nbsp;���薳����]&nbsp;" if $W[7] =~ m/!E0033/;
			$kouka2.="����̉ʎ�[��Ԉُ���ʂ��󂯂��ۂɎ�������&nbsp;��Ԉُ햳����]&nbsp;" if $W[7] =~ m/!E0034/;
			$kouka2.="�j���̐���[�\\���퓬�Ő퓬�s�\\����������&nbsp;�퓬�s�\\��]&nbsp;" if $W[7] =~ m/!E0035/;
			$kouka2.="�����̐���[�\\���퓬�Ő퓬�s�\\����������&nbsp;�퓬�s�\\���S��]&nbsp;" if $W[7] =~ m/!E0036/;
			$kouka2.="���S����A�b�v&nbsp;" if $W[7] =~ m/!E0037/;
			$kouka2.="���@����&nbsp;" if $W[7] =~ m/!E0038/;
			$kouka2.="L�EN���|�t�^&nbsp;" if $W[7] =~ m/!E0039/;

			$kouka2.="�t���O&nbsp;" if $W[7] =~ m/!zc/;
			$kouka2.="�f�X�y�i���e�B&nbsp;" if $W[7] =~ m/!zd/;
			$kouka2.="�_�~�[�R�[�h&nbsp;" if $W[7] =~ m/!xx/;
#			$kouka2.="&nbsp;" if $W[7] =~ m/!8s/;
		}else{$kouka2="&nbsp;";}

		$kouka2.=$BMsg;

		if($kouka eq ""){$kouka = "�@";}
		if($kouka1 eq ""){$kouka1 = "�@";}
		if($kouka2 eq ""){$kouka2 = "�@";}

		$icon = "<img src=\"$IMG_FOLDER4/$W[9].gif\">";

		if($W[9] eq ""){$icon = "�@";}

		return ($icon,$W[0],$c,$d,$W[3],$W[4],$W[5],$kouka,$kouka1,$kouka2,$W[14]);
	}
	my @data=map {[&KOUKA($_)]} @ZUKAN;
	@data=sort {$b->[0] <=> $a->[0] || $a->[1] cmp $b->[1]} @data;

	my $HEAD="<table bgcolor=$TABLE_COLOR1 border bordercolor=$TABLE_BORDER cellpadding=2 cellspacing=0 style=\"font-size:13px;\">\n<tr bgcolor=$TABLE_COLOR1><th nowrap>�A�C�R��</th><th width=220>���햼</th><th nowrap>�U��</th><th nowrap>����</th><th nowrap>��</th><th nowrap>����MP</th><th nowrap>���i</th><th>���</th><th>����</th><th>�������</th></tr>\n";
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


	#�����ŁA�W�߂������J�E���g����
#�R���N�g�����L���O�p
		#�����L���O�p �A�C�e�����W���@0�̓A�C�e���l���@1��MVP�@2�̓A�C�e�����W
#	&LOCK;
#	&DBM_CONVERT('P',"$FORM{'pname'}");
#	&UNLOCK;
		@RC=split(/!/,$PL_VALUES[47]);
		if($RC[2] eq ""){$RC[2] = 0;}
		if($RC[2] ne $i){
			$RC[2] = $i;
			$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";

			&LOCK;
			dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;# �o�^��������Ȃ���
			&UNLOCK;

		}
	print <<"-----END-----";
<form action=$MAIN_SCRIPT method=POST target=Sub>
<input type=hidden name=cmd value=ZUKAN>
<input type=hidden name=pname value=$FORM{'pname'}>
<input type=hidden name=pass value=$FORM{'pass'}>
<input type=submit value='�߂�' $STYLE_B1>
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
	&ERROR('�p�X���[�h�G���[') if $PL_VALUES[2] ne crypt($FORM{'pass'},eb);
	&ERROR('�o�^�G���[') if !$PL_VALUES[$FORM{'touroku'}];
	my $wid=(split /!/,$PL_VALUES[$FORM{'touroku'}])[0];
#	my $wid=(split /!/,$PL_VALUES[$FORM{'touroku'}])[0];
#	my $widt=(split /\,/,$WEAPON_LIST{"$wid"})[7];
#@array=(ubaa,ubab,ubac,ubad,ubae,ubaf);
#&ERROR("$wid��$array[$PL_VALUES[31]]");
	#���\�ω���������舵��
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
	&ERROR('���łɓo�^����Ă��܂��B') if exists $check_zukan{$wid};
	&ERROR('���̕���͓o�^�ł��܂���B') if exists $check_dame{$wid};

	my $xxx=@ZUKAN;
#	&ERROR($xxx);
#�R���N�g�����L���O�p
		@RC=split(/!/,$PL_VALUES[47]);
		if($RC[2] eq ""){$RC[2] = 0;}
		$RC[2] = $xxx + 1;
		$PL_VALUES[47] = "$RC[0]!$RC[1]!$RC[2]!$RC[3]!$RC[4]!$RC[5]!$RC[6]!$RC[7]!$RC[8]!$RC[9]!$RC[10]!";

#		&LOCK;
#		dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;# �o�^��������Ȃ���
#		&UNLOCK;


#	$PL_VALUES[$FORM{'touroku'}]='';# �o�^��������Ȃ���
	push @ZUKAN,$wid;
	my %temp=();
	foreach (@ZUKAN){
		next if $_ eq '' || !$WEAPON_LIST{$_} || exists $check_dame{$_};
		$temp{$_}=1;
	}
	@ZUKAN=keys %temp;
	&LOCK;
	dbmopen (%PL,"$DBM_P",0666);$PL{"$FORM{'pname'}"}="@PL_VALUES";dbmclose %PL;# �o�^��������Ȃ��� ��20090621�@304�@�����L���O���o�^�p�ɕύX
	open(OUT,">$LOG");print OUT "$_\n" for @ZUKAN;close(OUT);
	&UNLOCK;
}

1;


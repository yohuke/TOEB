sub vatimeheader{
#	$a = time;
#	&ERROR("$FORM{'nt'}��$a");
	&ERROR('TimeOut1','���j�b�g�I�����x�����܂��B') if (($FORM{'nt'} + 40) < time);
}
sub vatimeheader2{
#	$a = time;
#	&ERROR("$FORM{'nt'}��$a");
	&ERROR('TimeOut2','���j�b�g�I�����x�����܂��B') if (($FORM{'scheck'} + 40) < time);
}
sub vatimeheader3{
	$calx = time;
}
1;
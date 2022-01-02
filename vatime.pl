sub vatimeheader{
#	$a = time;
#	&ERROR("$FORM{'nt'}と$a");
	&ERROR('TimeOut1','ユニット選択が遅すぎます。') if (($FORM{'nt'} + 40) < time);
}
sub vatimeheader2{
#	$a = time;
#	&ERROR("$FORM{'nt'}と$a");
	&ERROR('TimeOut2','ユニット選択が遅すぎます。') if (($FORM{'scheck'} + 40) < time);
}
sub vatimeheader3{
	$calx = time;
}
1;
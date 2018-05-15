long giaiThua(int n){
	long gt =1;
	for(int i =2; i<=n;i++)
		gt = gt*i;
	return gt;
}
int tongChan(int n){
	if(n==0)
		return 0;
	else
		if(n%2==0)
			return n + tongChan(n-1);
		else
			return tongChan(n-1);
}
int tongLe(int n){
	if(n==0)
		return 0;
	else
		if(n%2!=0)
			return n + tongLe(n-1);
		else
			return tongLe(n-1);
}
long luyThua(int x, int n){
	if(n==0)
		return 1;
	else
		return x*luyThua(x,n-1);
}
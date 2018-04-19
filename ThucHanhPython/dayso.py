#Nhap 1 so N 
#a. In ra man hinh day so vua nhap
n = input("N= ")
tong =0
print"Day so vua nhap la:"
for i in range(n+1):
	print "%d" %i
#b. Tinh tong cac phan tu chan cua day
print"tong cac phan tu chan cua day la:"
for i in range(n+1):
	if(i%2 == 0):
		tong+=i
print"%d" %tong


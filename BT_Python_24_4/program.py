from HinhChuNhat import HinhChuNhat
N = input("Nhap N: ")
hcn = []
for i in range(N):
	ten = str(input("Ten: "))
	dai = input("Dai: ")
	rong = input("Rong: ")
	h = HinhChuNhat(ten,dai,rong)
	hcn.append(h)

for i in hcn:
	i.toString()
	print "Chu vi: %d" %i.getCV()
	print "Dien tich: %d" %i.getDT()
m = 0
for i in hcn:
	if(i.getDT() > m):
		m = i.getDT()
		t = i.getTen()
print "Hinh %s co dien tich lon nhat: %d" %(t,m)
file = open("hcn.txt","w+")
for i in hcn:
	file.write("Ten: %s\tdai: %d\tRong: %d\tChu vi: %d\tDien tich: %d\t" %(i.getTen(),i.getDai(),i.getRong(),i.getCV(),i.getDT()))
	file.write("\n")
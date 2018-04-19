class SinhVien:
	def __init__(self,mssv,hoten,makhoa):
		self.mssv = mssv
		self.hoten = hoten
		self.makhoa = makhoa
	def showthongtin(self):
		print"%3s%10s%5s" %(self.mssv,self.hoten,self.makhoa)
class Khoa:
	def __init__(self,makhoa,tenkhoa):
		self.makhoa = makhoa
		self.tenkhoa = tenkhoa
	def showthongtin(self):
		print "%3s%10s" %(self.makhoa,self.tenkhoa)
sv1 = SinhVien("001","Mai A","01")
sv2 = SinhVien("002","Tran B","01")
sv3 = SinhVien("003","Van C","03")
sv4 = SinhVien("004","Thi K","001")

dsSV=[]
dsSV.append(sv1)
dsSV.append(sv2)
dsSV.append(sv3)
dsSV.append(sv4)

k1 = Khoa("01","CNTT")
k2 = Khoa("02","KToan")
k3 = Khoa("03","CKhi")
k4 = Khoa("04","Nuoi")

khoa = []
khoa.append(k1)
khoa.append(k2)
khoa.append(k3)
khoa.append(k4)
#In ra man hinh bang sinh vien:

print "Bang Sinh Vien:\nMSSV\tHoTen\tMaKhoa"
for i in dsSV:
	i.showthongtin()

#in ra man hinh bang khoa:

print "\nBang Khoa:\nMaKhoa\tTenKhoa"
for i in khoa:
	i.showthongtin()
#in ra man hinh danh sach sinh vien khoa CNTT
for i in khoa:
	if(i.tenkhoa=="CNTT"):
		s = i.makhoa
print "\nDanh sach sinh vien khoa CNTT:\n"
print "MSSV\tHoTen\tMaKhoa"
for i in dsSV:
	if(i.makhoa == s):
		i.showthongtin()

	
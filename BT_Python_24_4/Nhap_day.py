N = input("Nhap N: ")
a=[]
for i in range(N):
	a.append(input("a[%d]= " %i))
print "cac phan tu chan:\n"
for i in a:
	if(i %2 == 0):
		print i
a.sort()
print "Day Sap xep: "
for i in a:
	print i

fileData = open('day.txt','w+')
for i in a:
	fileData.write(str(i))
	fileData.write("\n")
fileData.close()
a = input("a= ")
b = input("b= ")
kq=0
s = str (raw_input("Phep toan(+,-,*,/,%,**): "))
if(s == "+"):
	kq = a+b
elif(s == "-"):
	kq = a-b
elif(s == "*"):
	kq = a*b
elif(s == "/"):
	kq = a/b
elif(s == "%"):
	kq = a%b
else:
	kq = a**b

print "%d %s %d = %d" %(a,s,b,kq)

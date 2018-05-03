echo "Chuong trinh tinh tong tu 1 den $1"
index=0
tong=0
while [ $index -lt $1 ] 
do
	index=$(($index+1))
	tong=$(($tong+$index))
done
echo "Tong tu 1-$1: $tong"
exit 0
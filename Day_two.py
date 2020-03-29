# Task 1

l=1999
n=2000
if l<n:
	print("Year is a leap year")
else:
	print("Year is not a leap year")

l=2000
n=1999
if l<n:
	print("Year is a leap year")
elif l==n:
	print("Year is undefined")
else:
	print("Year is not a leap year")

l=2000
n=2000
if l<n:
	print("Year is  a leap year")
elif l==n:
	print("Year is undefined")
else:
	print("Year is not a leap year")

year=2000
if year%4!=0:
	print("Year is not a leap year")
elif year%100==0:
	if year%400==0:
		print("Year is a leap year")
	else:
		print("Year is not a leap year")
else:
	print("Year is a leap year")

year=1999
if year%4!=0:
	print("Year is not a leap year")
elif year%100==0:
	if year%400==0:
		print("Year is a leap year")
	else:
		print("Year is not a leap year")
else:
	print("Year is a leap year")


d=365
y="2000"
y="1999"
if y=="2000":
	if d<=365:
		print("Year is not a leap year")
elif d<=366:
	print("Year is  a leap year")
else:
	print("Year is undefined")
if y=="1999":
	if d<=365:
		print("Year is not a leap year")
elif d<=366:
	print("Year is  a leap year")
else:
	print("Year is undefined")

# Task 2

n=5
nn=55
nnn=555
print(n*nn*nnn)

# Task 3 Check even/odd using modulus operator:
a=8
if(a%2==0):
	print("This number is even")
else:
	print("This number is odd")

a=9
if(a%2==0):
	print("This number is even")
else:
	print("This number is odd")









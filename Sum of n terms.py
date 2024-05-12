a=int(input ("Enter the starting value :"))
n=int(input("Enter the number of terms :"))
d=int(input("Enter the common difference :"))
tval=0
Sum=0
print("The terms of the following AP is :")
for i in range (0,n):
    tval=a+i*d
    print(tval)
    Sum=Sum+tval
print("The sum of the terms of the AP is :")
print(Sum)

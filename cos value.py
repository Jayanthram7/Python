angle=int(input("Enter the angle:"))
x=angle*3.14/180

sum,i=1,2
tsum=0
fact=1

def fact(i):
    fact=1
    for n in range (1,i+1):
        fact=fact*n
    return fact


for i in range(2,20,i+2):
    sum=sum-(x**i/fact(i))-(x**(i+2)/fact(i+2))

print(sum)
      

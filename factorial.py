num=int(input("Enter a number :"))
fact=1

if num<0:
    print("please enter a positive number")

elif num==0:
    print("The factorial of 0 is 1")

for i in range(1,num+1):
    fact=fact*i
print("The factorial of",num,"is :",fact)

#Program to display the fibonacci sequence up to the n-th term

n=int(input("how many terms :"))

n1=0
n2=1
count=0

if n<=0:
    print("please enter a positive integer")

elif n==1:
    print("The fibonacci series upto ",n,":")
    print(n1)

else:
    print("fibonacci sequence")
    while count<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1

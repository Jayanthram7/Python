def Factorial(n):
    k=1
    for i in range(n):
        k=k*i
        return k
a=int(input("Enter the number which has to be checked for Krishnamuruthy's condition : "))
K=a
b=len(str(a))
k=0
for j in range(b):
    n=a%10
    a=a//10
    k=k+Factorial(n)
if k==a:
    print("It is a krishnamuruthy number ")
else:
    print("It is not a krishnamuruthy  number : ")
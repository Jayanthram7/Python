n=int(input("Enter the number of fibonacci series to be generated : "))
a=0
b=1
fib=0
print(a)
print(b)
for i in range(n-2):
   


    fib=a+b
    
    a=b
    b=fib
    print(fib)

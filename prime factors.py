l1=[]
def primeFactors(n):
    while n%2==0:
        l1.append(2)
        n=n/2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            l1.append(i)
            n=n/i
    if n>2:
        l1.append(n)
n=int(input("Enter the number whose Prime factors you want to find : "))
primeFactors(n)
print(l1)
lenn=len(l1)
print(l1[lenn-1])
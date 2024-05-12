# Prime Factors 
l1=[]
def primefactors(n):
    if n==2:
        l1.append(2)
        n=n/2
    for i in range(3,int(n**0.5),2):
        if n%i==0:
            l1.append(i)
            n=n/i
    if n>2:
        l1.append(n)

n=int(input("Enter the number whose prime factors you want to find : "))
primefactors(n)
l1.sort()
for k in l1:
    print(int(k))


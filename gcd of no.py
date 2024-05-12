def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
m=int(input("enter the no: "))
n=int(input("enter the no: "))
print(gcd(m,n))

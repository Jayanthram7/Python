a=[1,2,3,4,5,6,7,8,9,10,11]
n=len(a)
print(a)
print("Length of array : ",n)
l1=[]

i=0
while(i<(n//2)):
    t=a[i]
    a[i]=a[n-1-i]
    a[n-1-i]=t
    i=i+1
    
print("The Reversed array is : ")
for i in a:
    l1.append(i)
print(l1)

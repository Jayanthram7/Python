"""
n=int(input("Enter the number of elements in an array :"))
i=0
l1=[]
for i in range(0,n):
    j=int(input("Enter a number :"))
    l1.append(j)
"""

l1= [1,2,3,4,5,6,7,8]
n=len(l1)

minn=l1[0]
for i in range (0,n):
    if l1[i]<minn:
        minn=l1[i]
print(minn)
        
        
    
    

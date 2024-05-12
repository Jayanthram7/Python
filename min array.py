n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input("Enter the element : ")))
minn=l1[0]
for j in range(len(l1)):
    if l1[j]<l1[0]:
        minn=l1[j]
print(minn)


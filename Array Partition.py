n=int(input("Enter the number of elements in the list : "))
l1=[]
l2=[]
l3=[]
for i in range(n):
    l1.append(int(input("Enter the element : ")))
print(l1)

ind=int(input("Enter the value Where you want the array to be split : "))

for j in range(0,len(l1)):
    if l1[j]<ind:
        l2.append(l1[j])
    else:
        l3.append(l1[j])
l2.sort()
l3.sort()
print("Elements lesser than ",ind," are ",l2)
print("Elements greater than ",ind,"are",l3)

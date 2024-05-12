n=int(input("No of Elements in the array : "))
l1=[]
l2=[]
for i in range(n):
    l1.append(int(input("Enter the element : ")))
print(l1)

if l1[0]>=l1[1]:
    l2.append(l1[0])
if l1[n-1]>l1[n-2]:
    l2.append(l1[n-1])

for j in range(1,len(l1)-1):
    if l1[j]>l1[j-1] and l1[j]>l1[j+1] :
        l2.append(l1[j])


print("The peak elements are : ",l2)

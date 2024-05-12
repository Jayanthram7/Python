#Program to find least common multiple of 3 Numbers
l1=[]
l2=[]
l3=[]
l4=[1]
n=int(input("Enter First number : "))
n2=int(input("Enter Second number : "))
n3=int(input("Enter Third number : "))

print("")

for i in range(1,10000000):
    if n%i==0:
        l1.append(i)
        
for j in range(1,10000000):
    if n2%j==0:
        l2.append(j)



for y in range(1,10000000):
    if n3%y==0:
        l3.append(y)


l1.remove(1)
l2.remove(1)
l3.remove(1)


print("Multiples of ",n,"is",l1)
print("Multiples of ",n2,"is",l2)
print("Multiples of ",n3,"is",l3)

print("")

for m in range(len(l1)):
    for k in range(len(l2)):
        for d in range(len(l3)):
            if l1[m]==l2[k]==l3[d]:
                l4.append(l1[m])
            
if len(l4)>=2:               
    print("The LCM of [",n,",",n2,",",n3,"] , is : ",l4[1])
else:
    print("The LCM of [",n,",",n2,",",n3,"] , is : ",l4[0])



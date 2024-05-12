n=int(input("Enter the number of words : "))
l1=[]
l2=[]
for i  in range(n):
    l1.append(str(input("Enter the word : ")))

for j in l1:
    if j[0] in j[1:]:
        l2.append(j)

print(l2)


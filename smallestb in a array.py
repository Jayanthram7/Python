n=int(input("no of terms in the list"))
li=[]
i=0
while i<n:
    a=int(input("elements of the list"))
    li.append(a)
    i=i+1
print(li)

mi=li[0]
j=1
while j<n:
    if li[j]<mi:
        mi=li[j]
    j=j+1
print("smallest no in the array", mi)


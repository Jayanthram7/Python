l1=list(map(int,input().split()))

print(l1)
minn=l1[0]
for j in range(len(l1)):
    if l1[j]<minn:
        minn=l1[j]
print(minn)
maxx=l1[0]
for k in range(len(l1)):
    if l1[k]>maxx:
        maxx=l1[k]
print(maxx)



n=0
a=[2,8,23,23,23,23,23,26]
for i in range(a):
    if i<a[n]:
        i=i+1
    else:
        a[n]=i
        max=max+a[n]
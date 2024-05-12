a=[[1,2,3],[4,5,6],[7,8,9]]
n=len(a)

for i in range(n):
    minn=a[i][0]
    col=0

    for j in range(n):
        if a[i][j]<minn:
            minn=a[i][j]
            col=j

    maxx=a[0][col]
    for k in range(n):
        if a[k][col]>maxx:
            maxx=a[k][col]

    if minn==maxx:
        print("Saddle point of matrix is ",minn)

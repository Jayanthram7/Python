def saddle(mat,n):
    for i in range (n):
        min_row=mat[i][0]
        colfind=0
        for j in range (1,n):
            if (min_row > mat[i][j]):
                min_row=mat[i][j]
                colifind=j


    k=0
    for k in range(n):
        if (min_row<mat[k][colfind]):
            break
        k+=1
    if (k==n):
        print("value of saddle point",min_row)
        return True
    return False
mat=[[1,2,3],[4,5,6],[7,8,9]]
n=3
if (saddle(mat,n)==False):
    print('no saddle point')

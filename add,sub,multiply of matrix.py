a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[9,8,7],
   [6,5,4],
   [3,8,1]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]]
def add():
    for i in range (len(a)):
        for j in range (len(b[0])):
            c[i][j]=a[i][j]+b[i][j]
    for r in c :
        print(r)
add()


def sub():
    for i in range (len(a)):
        for j in range (len(b[0])):
            c[i][j]=a[i][j]-b[i][j]
    for r in c :
        print(r)
sub()



def multiply():
     for i in range (len(a)):
        for j in range (len(b[0])):
            for k in range(len(b)):
                 c[i][j]+=a[i][j]*b[i][j]
     for r in c :
            print(r)

multiply()

n=int(input())
l1=[]
l2=[]
l3=[]
for i in range(n):
    l1.append(str(input()))

for j in l1:
    l2=[]
    for k in j:
        l2.append(k)
        print(l2)
        print(len(l2))
        if len(l2)==10 and  l2[0]=='9' or len(l2)==10 and l2[0]=='8' or len(l2)==10 and l2[0]=='7' :
        
        
            print("YES")
        else:
            print("NO")
  

    
        
    


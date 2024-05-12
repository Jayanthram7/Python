n=int(input("enter the no of elements in array: "))
lst=[]
i=0
while i<n:
    n1=int(input("enter the element"))
    lst.append(n1)
    i=i+1
print(lst)


b=int(input("enetr the no to be found"))
for k in range(0,n):
          if lst[k]==b:
              print("the index of given no is : ",k)

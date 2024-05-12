"""
n=int(input("Enter the number of elements in the list : "))
l1=[]
multiply=1

for i in range(n):
    element=int(input("Enter the element : "))
    l1.append(element)
    multiply=multiply*element
print(multiply)
    
"""

n= int(input("Enter the no.of elements in the list : "))
l1=[]
multiply=1
for i in range(n):
    l1.append(int(input("Enter the element : ")))
print("The list is : ",l1)

for j in range(len(l1)):
    multiply=multiply*l1[j]
    
print("The Value we get when all elements in the list are multiplied is : ",multiply)
               

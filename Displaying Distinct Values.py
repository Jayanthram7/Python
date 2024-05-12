#User input of array
n=int(input("Enter the No.of elements in the array : "))
array1=[]
for i in range(n):
    array1.append(int(input("Enter the element : ")))


#Removing Duplicate Values from the array    
new_list=[]

for i in array1:
    if i not in new_list:
        new_list.append(i)

print(new_list)

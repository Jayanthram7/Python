n=int(input("No of Students in class : "))
count=0
for i in range(n):
    mark=int(input("Enter the mark of the student : "))
    if mark>+50:
        count=count+1
print(count,"students have passed the examination out of ",n)

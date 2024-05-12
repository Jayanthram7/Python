n=int(input("Enter the number whose smallest divisor you want to find :"))
i=3
list1=[]
if n%2==0:
    print("The smallest divisor of the number ",n," is 2")
else:
    print("The factors the number given are :")
    for i in range (3,100): 
        x=n%i
        if x==0:
            list1.append(i)
            print(i)
            i=i+2
        elif x!=0:
            i=i+2

    print("The smallest divisor of the number ",n,"is = ",min(list1))
    

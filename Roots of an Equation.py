print("An Equation is of the form :")
print("ax^2 +bx +c = 0")
print("Compare the above equation and enter the following to find the roots of the equation :")
a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))

disc=(b**2)-(4*a*c)

sol1= -b+(disc**0.5)/(2*a)
sol2= -b-(disc**0.5)/(2*a)

print("The solution for the Equation is :",sol1," ",sol2)

print("Enter a String :",end="")
text =input()
textlength =len(text)
print("The following is the ASCII values for the given input :")
for char in text :
    if char==" ":
        print(" ")
    else:
        ascii =ord(char)
        
        print(char,"\t","-","\t",ascii)

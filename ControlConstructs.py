##-------------Control Constructs------------
###------Conditional Control constructs-------

####--------if control construct-----

a=int(input("Enter the Number"))
if a%5==0:
    print("Number is divisible by 5")


####--------if else control construct-----

a=int(input("Enter the Number:"))
if a%2==0:
    print("Number is even")
else:
    print ("Number is odd")


####--------if elif else control construct-----

course=input("Enter the Course Name:")
if course=="MCP1":
    print("Fullstack Development course")
elif course=="MCP2":
    print("Fullstack Testing Course")
else:
    print ("Invalid Course")


####--------match control construct-----

a=int(input("Enter the first Number"))
b=int(input("Enter the secont Number"))
ch=int(input("Enter your choice"))
match ch:
    case 1:print("Addition ",a+b)
    case 2:print("Substraction ",a-b)
    case 3:print("Multiplication ",a*b)
    case 4:print("Division ",a/b)
    case 5:print("Remainder ",a%b)
    case _:print("Invalid Input")
print("Program Stopped")


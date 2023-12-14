'''a=10
b=20
avg=(a+b)/2
print(avg)
print(type(a))
print(type(b))
print(type(avg))'''

###------Taking input from user------
##Example 1
a=input("Enter the first Number:")#10
b=input("Enter the second Number:")#20
c=(a+b)
print(c)#1020

'''By default input function will take the inputs as String type variables
So to convert string into other types we need to use
functions like int(),float(),boo(),complex().'''

##Example 2
a=int(input("Enter the first Number:"))#10
b=int(input("Enter the second Number:"))#20
c=(a+b)/2
print(c)#15.0

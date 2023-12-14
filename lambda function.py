###--------Lambda function----------
''' lambda function is also known as "Annonymus function" or the function which don't have any name.
>lambda function takes any number of inputs but only 1 expression
>Syntax:-- lambda input : expression'''

##Ex 1: program to find square of the given number
##--Treditional way-----
def sq(num):
    return num*num
num =int (input("Enter the number :"))
res = sq(num)
print(res)

##----Using lambda function------
num =int(input("Enter the number"))
sq =lambda num : num*num
print (sq(num))


##Ex 2: Program to add 2 numbers
##--Treditional way-----
n1 =int(input("Enter the first number"))
n1 =int(input("Enter the second number"))
def add(a,b):
    return a+b
res = add(n1,n2)
print (res)

##----Using lambda function------
n1 =int(input("Enter the first number"))
n1 =int(input("Enter the second number"))
add = lambda a,b : a+b
print(add(n1,n2))

##Ex 3: Program to substracting 2 numbers
##--Treditional way-----
n1 =int(input("Enter the first number"))
n1 =int(input("Enter the second number"))
def add(a,b):
    return a-b
res = add(n1,n2)
print (res)

##----Using lambda function------
n1 =int(input("Enter the first number"))
n1 =int(input("Enter the second number"))
add = lambda a,b : a-b
print(add(n1,n2))


####-----------in and not in operators--------
##Ex 1:
lst=[10,20,30,40,50]
print(10 in lst)#True
print(20.5 in lst)#False
print(30 not in lst)#False
print(45 not in lst)#True

##Ex 2:
st="KodNest"
print('e' in st)
print('w' in st)


###-------------filter() function---------------
''' filter() is used to filter the values from the given iterable object based on the given expression and
returns the new iterable object.
>filter() takes 2 arguments: function expression (lambda function) as first argument and name of the
iterable object as second argument.
>function expression should be a lambda function and it should return only true or false values.
> Syntax:- filter(function expression, input)'''

#Ex 1:
lst = [10,2,3,5,8,6]
even =filter (lambda i:i%2==0,lst)
print(even)#<filter object at 0x0000023E5D0A3C70>

#Ex 2:
lst = [10,2,3,5,8,6]
even =list( filter (lambda num:num%2==0,lst))
print(even)#[10, 2, 8, 6]


#EX 3:
st = "Technologies"
vowels="aeiou"
res="".join(filter(lambda i: i in vowels,st))#filter object can be converted to string using join()
print(res)#eooie


####------------------map()   function------------
'''map() is used to map the expression to all the elelments in the given iterable object.
>>map() takes 2 arguments: function expression(lambda function) as first argument and name of
the iterable object as second argument.
>syntax:- map(function expression,input)'''

#EX 1:
lst=[1,2,3,4,5,6]

res=map(lambda i:i+2,lst)
print(res)#<map object at 0x0000023C33F17B20>

res1=list(map(lambda i:i+2,lst))
print(res1)#[3,4,5,6,7,8]

res2=list(map(lambda i:i*i,lst))
print(res2)#[1,4,9,16,25,36]










 

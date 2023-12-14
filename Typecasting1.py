# float to int
a = 10.58
print(a)#10.58
print(type(a))#<class 'float'>
b= int(a)
print(b)#10
print(type(b))


# bool to int
a = True
print(a)#True
print(type(a))#<class 'bool'>
b= int(a)
print(b)#1
print(type(b))#<class 'int'>

# bool to int
a = False
print(a)#False
print(type(a))#<class 'bool'>
b= int(a)
print(b)#0
print(type(b))#<class 'int'>

# str to int
a = "Kodnest"
print(a)#Kodnest
print(type(a))#<class 'str'>
'''b= int(a)#ValueErroe:invalid literal for int() with base10:"KodNest"
print(b)
print(type(b))'''

# complex to int
a = (10+5j)
print(a)#(10+5j)
print(type(a))#<class 'complex'>
'''b= int(a)#TypeError: int() argument must be a string,
         #a bytes-like object or a real number, not 'complex'
print(b)
print(type(b))'''







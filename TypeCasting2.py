### int to float
a = 10
print(a)#10
print(type(a))#<class 'int'>

b= float(a)
print(b)#10.0
print(type(b))#<class 'float'>

### bool to float
a = True
print(a)#True
print(type(a))#<class 'bool'>

b= float(a)
print(b)#1.0
print(type(b))#<class 'float'>

### bool to float
a = False
print(a)#False
print(type(a))#<class 'bool'>

b= float(a)
print(b)#0.0
print(type(b))#<class 'float'>

### str to float
a = "KodNest"
print(a)#KodNest
print(type(a))#<class 'str'>

'''b= float(a) ##ValueError: could not convert string to float:'KodNest'
print(b)
print(type(b))'''

### complex to float
a = 10+5j
print(a)#(10+5j)
print(type(a))#<class 'complex'>

'''b= float(a)  ##TypeError: float() argument must be a string or real number, not 'complex'
print(b)
print(type(b))'''



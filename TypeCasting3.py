### int to complex
a = 10
print(a)#10
print(type(a))#<class 'int'>
b= complex(a)
print(b)#(10+0j)
print(type(b))#<class 'complex'>

### float to complex
a = 10.56
print(a)#10.56
print(type(a))#<class 'float'>
b= complex(a)
print(b)#(10.56+0j)
print(type(b))#<class 'complex'>

### bool to complex
a = True
print(a)#True
print(type(a))#<class 'bool'>
b= complex(a)
print(b)#(1+0j)
print(type(b))#<class 'complex'>

### bool to complex
a = False
print(a)#False
print(type(a))#<class 'bool'>
b= complex(a)
print(b)#0j
print(type(b))#<class 'complex'>

### str to complex
a = "KodNest"
print(a)#KodNest
print(type(a))#<class 'str'>
'''b= complex(a)##ValueError: complex() arg is a malformed string
print(b)
print(type(b))'''

### int to bool
a = 10
print(a)#10
print(type(a))#<class 'int'>
b = bool(a)
print(b)#True
print(type(b))##<class 'bool'>

### int to bool
a = -10
print(a)#-10
print(type(a))#<class 'int'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### int to bool
a = 0
print(a)#0
print(type(a))#<class 'int'>
b = bool(a)
print(b)#False
print(type(b))#<class 'bool'>

### float to bool
a = 10.568
print(a)#10.568
print(type(a))#<class 'float'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### float to bool
a = -10.89
print(a)#-10.89
print(type(a))#<class 'float'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### float to bool
a = 0.00
print(a)#0.00
print(type(a))#<class 'float'>
b = bool(a)
print(b)#False
print(type(b))#<class 'bool'>

### str to bool
a = "KodNest"
print(a)#KodNest
print(type(a))#<class 'str'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### str to bool
a = ""
print(a)
print(type(a))#<class 'str'>
b = bool(a)
print(b)#False
print(type(b))#<class 'bool'>

### str to bool
'''a = null
print(a)
print(type(a))
b = bool(a)#NameError: name 'null' is not defined
print(b)
print(type(b))'''

### complex to bool
a = 10+5j
print(a)#(10+5j)
print(type(a))#<class 'complex'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### complex to bool
a = -(10+5j)
print(a)#-(10+5j)
print(type(a))#<class 'complex'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### str to bool
a = 0+0j
print(a)
print(type(a))#<class 'complex'>
b = bool(a)
print(b)#False
print(type(b))#<class 'bool'>



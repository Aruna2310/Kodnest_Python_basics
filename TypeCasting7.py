####-----------complex values-----------------------------
###String type complex value to --- complex
a = "10+5j"
print(a)#10+5j
print(type(a))#<class 'str'>
b = complex(a)
print(b)#(10+5j)
print(type(b))#<class 'complex'>

### string type complex value to---- int
a = "10+5j"
print(a)#10+5j
print(type(a))#<class 'str'>
'''b = int(a)#ValueError: invalid literal for int() with base 10: '10+5j'
print(b)
print(type(b))'''

### String type complex value to --- float
a = "10+5j"
print(a)#10+5j
print(type(a))#<class 'str'>
'''b = float(a)#ValueError: could not convert string to float: '10+5j'
print(b)
print(type(b))'''

### String type complex value to --- bool
a = "10+5j"
print(a)#10+5j
print(type(a))#<class 'str'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### String type complex value to --- str
a = "10+5j"
print(a)#10+5j
print(type(a))#<class 'str'>
b = str(a)
print(b)#10+5j
print(type(b))#<class 'str'>


####-----------Boolean values-------------------------------
### String type boolean value to --- bool
a = "True"
print(a)#True
print(type(a))#<class 'str'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

a = "False"
print(a)#False
print(type(a))#<class 'str'>
b = bool(a)
print(b)#False
print(type(b))#<class 'bool'>


###String type boolean value to --- int
a = "True"
print(a)#True
print(type(a))#<class 'str'>
'''b = int(a)#ValueError: invalid literal for int() with base 10: 'True'
print(b)
print(type(b))'''

a = "False"
print(a)#False
print(type(a))#<class 'str'>
'''b = int(a)#ValueError: invalid literal for int() with base 10: 'False'
print(b)
print(type(b))'''


###String type boolean value to --- float
a = "True"
print(a)#True
print(type(a))#<class 'str'>
'''b = float(a)#ValueError: could not convert string to float: 'True'
print(b)
print(type(b))'''

a = "False"
print(a)#False
print(type(a))#<class 'str'>
'''b = float(a)#ValueError: could not convert string to float: 'False'
print(b)
print(type(b))'''


###String type boolean value to --- complex
a = "True"
print(a)#True
print(type(a))#<class 'str'>
'''b = complex(a)#ValueError: complex() arg is a malformed string
print(b)
print(type(b))'''

a = "False"
print(a)#False
print(type(a))#<class 'str'>
'''b = complex(a)#ValueError: complex() arg is a malformed string
print(b)
print(type(b))'''


### String type boolean value to ------ str
a = "True"
print(a)#True
print(type(a))#<class 'str'>
b = str(a)
print(b)#True
print(type(b))#<class 'str'>

a = "False"
print(a)#False
print(type(a))#<class 'str'>
b = str(a)
print(b)#False
print(type(b))#<class 'str'>






####int values
### string type int value to ---- int
a = "10"
print(a)#10
print(type(a))#<class 'str'>
b = int(a)
print(b)
print(type(b))#<class 'int'>

### String type int value to --- float
a = "10"
print(a)#10
print(type(a))#<class 'str'>
b = float(a)
print(b)#10.0
print(type(b))#<class 'float'>

### String type int value to --- bool
a = "10"
print(a)#10
print(type(a))#<class 'str'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### String type int value to --- complex
a = "10"
print(a)#10
print(type(a))#<class 'str'>
b = complex(a)
print(b)#(10+0j)
print(type(b))#<class 'complex'>

### String type int value to --- string
a = "10"
print(a)#10
print(type(a))#<class 'str'>
b = str(a)
print(b)#10
print(type(b))#<class 'str'>

#######-----------float vaues-------------
###String type float value to --- float
a = "10.56"
print(a)#10.56
print(type(a))#<class 'str'>
b = float(a)
print(b)#10.56
print(type(b))#<class 'float'>

### string type float value to---- int
a = "10.56"
print(a)#10.56
print(type(a))#<class 'str'>
b = int(a)##ValueError: invalid literal for int() with base 10: '10.56'
print(b)
print(type(b))

### String type float value to --- bool
a = "10.56"
print(a)#10.56
print(type(a))#<class 'str'>
b = bool(a)
print(b)#True
print(type(b))#<class 'bool'>

### String type float value to --- complex
a = "10.56"
print(a)#10.56
print(type(a))#<class 'str'>
b = complex(a)
print(b)#(10.56+0j)
print(type(b))#<class 'complex'>

### String type float value to --- str
a = "10.56"
print(a)#10.56
print(type(a))#<class 'str'>
b = str(a)
print(b)#10.56
print(type(b))#<class 'str'>



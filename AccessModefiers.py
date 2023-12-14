####------Access Modefiers/Specifiers---------
'''Access Modefiers are used to restrict the access of variables or methods
in Python.
>In Python there are 3 access specifiers
1)public
2)private
3)Protecte'
>Even though Python provides Access modifiers and rules,these rules are not
restricted.Due to no proper restriction for private variables and constructors
gets inherited inside the child classes Python does not supports proper security
or encapsulation like Java'''


##-------------public access specifier--------------
'''Bydefault the data members are public
>data members which are declared as public inside the class are accessible
anywhere inside the program and project'''
###Ex:1
##class Demo:
##    def __init__(self):
##        self.x=10#public variable
##        self.y=20#public variable
##d=Demo()
##print(d.x)#10
##print(d.y)#20
##
###Ex:2
##class Demo:
##    def __init__(self):
##        self.x=10#public variable
##        self.y=20#public variable
##class Test:
##    def display(self):
##        d1=Demo()
##        print("Inside Test class")
##        print(d1.x)#accessing inside another class
##        print(d1.y)#accessing inside another class
##d=Demo()
##print(d.x)#10#accessing outside the class
##print(d.y)#20#accessing outside the class
##t=Test()
##t.display()


##--------------protected access specifier-------------
'''the data members which are declaired as protected should be prefixed with '_'
>If the data members are declared as protected,they should be accessible only
by the child classes in Python'''
#Ex:1
class Demo:
    def __init__(self):
        self._x=10#protected variable
        self._y=20#protected variable
d=Demo()
print(d._x)#10
print(d._y)#20

#Ex:2:Without Parent child relationship accessible
class Demo:
    def __init__(self):
        self._x=10#protected variable
        self._y=20#protected variable
class Test:
    def display(self):
        d1=Demo()
        print("Inside Test class")
        print(d1._x)#accessing inside another class
        print(d1._y)#accessing inside another class
d=Demo()
print(d._x)#Accessed outside the class
print(d._y)#Accessed outside the class
t=Test()
t.display()


#Ex:3:With Parent child relationship accessible
class Demo:
    def __init__(self):
        self._x=10#protected variable
        self._y=20#protected variable
class Test(Demo):
    def display(self):
        d1=Demo()
        print("Inside Test class")
        print(d1._x)#accessing inside child class
        print(d1._y)#accessing inside child class
d=Demo()
print(d._x)#accessing outside child class
print(d._y)#accessing outside child class
t=Test()
t.display()


###-------------private access specifier--------------
'''The data members which are declared as private should be prefixed with '__'
>If the data member is declared as private then that variable should not be
accessed out the class.
>while accessing the private variable we should follow below syntax:
[referencevariable._classname__private variable name]
using this syntax user can access the private variable outside the class.
>The process of accessing the private variable outside the class is known as
"Data Mangling"in Python'''

#Ex:1
class Demo:
    def __init__(self):
        self.__x=10#private variable
        self.__y=20#private variable
d=Demo()
print(d.__x)#Error
print(d.__y)#Error


#Ex:2
class Demo:
    def __init__(self):
        self.__x=10#private variable
        self.__y=20#private variable
d=Demo()
print(d._Demo__x)#10
print(d._Demo__y)#20


#Ex:3:Without Parent child relationship accessible
class Demo:
    def __init__(self):
        self.__x=10#private variable
        self.__y=20#private variable
class Test:
    def display(self):
        d1=Demo()
        print("Inside Test class")
        print(d1._Demo__x)#accessing inside another class#10
        print(d1._Demo__y)#accessing inside another class#20
d=Demo()
print(d._Demo__x)#Accessed outside the class#10
print(d._Demo__y)#Accessed outside the class#20
t=Test()
t.display()

































    

###----Magic Methods / Dunder Methods in Python------
'''In Python there are few methods which are prefixed with __ and suffixed
   with __.Any methods which are prefixed and suffixed with __ are called as
   "Magic methods or Dunder Methods".
   >Magic methods are specially used for operator overriding in Python.'''

##Ex 1:
class Demo:
    def __init__(self,radius):
        self.radius=radius
def main():
    d1=Demo(10)
    d2=Demo(20)
    #print(d1+d2)#TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo'
main()


##Ex 2:
class Demo:
    def __init__(self,radius):
        self.radius=radius
    def __add__(self,other):
        return self.radius+other.radius
    def __sub__(self,other):
        return self.radius-other.radius
    def __gt__(self,other):
        return self.radius>other.radius
    def __lt__(self,other):
        return self.radius<other.radius
    def __truediv__(self,other):
        return self.radius/other.radius
    def __mul__(self,other):
        return self.radius*other.radius
def main():
    d1=Demo(10)
    d2=Demo(20)
    print(d1+d2)#30
    print(d1-d2)#-10
    print(d1>d2)#False
    print(d1<d2)#True
    print(d1/d2)#0.5
    print(d1*d2)#200
main()


##Ex 3:__str__() Magic Method
'''When ever a class is created, bydefault few magic methods gets added to the
class. For eg:__init__(), __str__() etc.
>When the object refernce is printed, by default __str__() Magic mathod is
called and prints the address of the reference variable.'''

class Demo:
    def __init__(self):
        self.name = "KodNest"
d=Demo()
print(d)#<__main__.Demo object at 0x000001A309AA0650>


##Ex 4:
''' Bydefault  __str__() Magic method returns the address of the given object
We can override the __str__() according to the user requirements as shown below'''
class Demo:
    def __init__(self):
        self.name = "KodNest"
    def __str__(self):
        return "Name ="+self.name
d=Demo()
print(d)#Name =KodNest










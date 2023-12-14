#####------Static--------

##Static variables----

##EX:1 
'''Static variables can be created directly inside the class, outside the method.
>They can be accessed either by using name of the class or the object reference'''

class Demo:
    a=10
    b=20
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fun(self):
        print("Python is Fun")
d=Demo(100,200)
d.fun()       #Python is Fun
print(d.x)    #100
print(d.y)    #200
print(d.a)    #10
print(d.b)    #20
#print(Demo.x)#Error:instance variables can't be accessed using class name
#print(Demo.y)#Error:instance variables can't be accessed using class name
print(Demo.a) #10
print(Demo.b) #20

##EX:2 Various methods to create Static Variables

class Student:
    institute =" Static variable created directly inside the class outside the method"
    def __init__(self):
        Student.course="Static variable created inside the constructor"
    @staticmethod
    def play():
        Student.game ="static variable created inside the static method"
    @classmethod
    def class_method(cls):
        Student.need ="Static variaable created inside the class method using class name"
        cls.eat ="Static variaable created inside the class method using cls keyword"

print(Student.institute)#Static variable created directly inside the class outside the method
s =Student()
print(Student.course)#Static variable created inside the constructor
Student.play()
print(Student.game)#static variable created inside the static method
Student.class_method()
print(Student.need)#Static variaable created inside the class method using class name"
print(Student.eat)#Static variaable created inside the class method using cls keyword

'''Note: Static variables, static methods and class methods can be accesed directly using the class
name. If the static variable is created inside the static method, class method and __init__() method,
then memory for the static variable will be created once after the methods are called.'''

        







        
        

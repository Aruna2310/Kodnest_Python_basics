###-------Inheritance in Python-----
'''Inheritance is a process of acquiring the properties or behavior of the
parent class inside the child class
Parent class--Super class
Child class---sub class'''

class Parent:
    def __init__(self):
        self.x=10
        self.y=20
    def fun(self):
        print("Inside the Parent class")
class Child(Parent):
    pass
c=Child()
print(c.x)#10
print(c.y)#20
c.fun()#Inside the Parent class

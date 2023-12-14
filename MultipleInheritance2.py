####----Does constructor gets inherited in Python?--------
#Constructors get inherited in Python

class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
class Child(Parent):
    pass
c=Child()#Inside Parent Constructor

#####-----Inherited, Overriden and Specialized Methods----
'''Inherited method- methods which are inherited from the Parent class and used
as it is in the child class.
>Overriden Methods- methods which are inherited from the Parent class and modified
inside the child class.
.>Specialized Methods- methods which are present only inside the child class but
not present in the Parent class.'''

class Parent:
    def be_kind(self):
        print("Be Kind to Animals")
    def cook(self):
        print("Parent cook Veg Beriyani")
class Child(Parent):
    def cook(self):
        print("Child cook Pulav")
    def play(self):
        print("Child Plays Cricket")
c=Child()
c.be_kind()#Be Kind to Animals(Inheritted Method)
c.cook()#Child cook Pulav(Overriden Method)
c.play()#Child Plays Cricket(Specialized Method)


'''--In Python inside constructor bydefault there is not super(). If we want call
the Parent class Constructor then we need to call explicitly using:
super.__init__()'''

#Ex1:
class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
class Child(Parent):
    def __init__(self):
        print ("Inside Child Constructor")
c=Child()#Inside Child Constructor

#Ex2:
class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructor")
c=Child()#Inside Parent constructor
         #Inside Child Constructor

'''>Inside Child class constructor we can call Parent class constructor
    any number of time
>Call to the Parent calss constructor need not to be the first statement'''

#Ex3:
class Parent:
    def __init__(self):
        print("Inside Parent Constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print ("Inside Child Constructor")
        super().__init__()
c=Child()#Inside Parent Constructor     
         #Inside Child Constructor
         #Inside Parent Constructor





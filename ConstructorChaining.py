####-------Constructor Chaining------
'''Constructor Chaining is a process of calling Parent class constructor from
child class.
>Inside Child class constructor we can call Parent class constructor any number
of times.that is super().__init__() statement can be present as any number of
times inside the child class.
>Call to the Parent calss constructor need not to be the first statement'''

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


#####---------Method Chaining-----------
'''Method chaining is the Process of calling the Parent method from the chlid
class method using super()'''

class Parent:
    def cook(self):
        print("Parent cooks Beriyani")
class Child(Parent):
    def cook(self):
        super().cook()
        print("Child cooks Maggie")
        super().cook()
c=Child()
c.cook()#Parent cooks Beriyani
        #Child cooks Maggie
        #Parent cooks Beriyani

#Ex:2
class Parent:
    def cook(self):
        print("Parent cooks Beriyani")
    def fun(self):
        print("Inside Parent fun method")
class Child(Parent):
    def cook(self):
        super().cook()
        print("Child cooks Maggie")
        super().fun()
c=Child()
c.cook()#Parent cooks Beriyani
        #Child cooks Maggie
        #Inside Parent fun method


####-----Method chaining in Multilevel Inheritance------
class GreatGrandParent:
    def cook(self):
        print("GreatGrandParent cooks Beriyani")
class GrandParent(GreatGrandParent):
    def cook(self):
        print("GrandParent cooks VegBeriyani")
class Parent(GrandParent):
    def cook(self):
        print("Parent cooks Pulav")
class Child(Parent):
    def cook(self):
        print("Child cooks Maggie")
        super(Child,self).cook()
        super(Parent,self).cook()
        super(GrandParent,self).cook()
c=Child()
c.cook()#Child cooks Maggie
        #Parent cooks Pulav
        #GrandParent cooks VegBeriyani
        #GreatGrandParent cooks Beriyani
        


































    




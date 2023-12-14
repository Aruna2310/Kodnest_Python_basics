#####-------Abstraction in Python------
'''Note:
1)we have to attach @abstractmethod decorator to the abstract method inside
the class.
2)The class which have abstract method should inherit from "ABC" class.
3)"ABC" class and @abstractmethod decorator is present inside the "abc" module.
hence we have to import both "ABC" class and @abstractmethod decorator from the
abc module
4)Abstract methods must be attached with pass keyword inside the method body to
tell the method is not having any statements inside it.'''

from abc import ABC,abstractmethod
class Player(ABC):
    @abstractmethod
    def plays(self):
        pass     
class Football(Player):
    def plays(self):
        print("Player plays football")
class Cricket(Player):
    def plays(self):
        print("Player plays cricket")
class Tennis(Player):
    def plays(self):
        print("Player plays Tennis")
class Playground:
    def players(self,ref):
        ref.plays()
p=Playground()
p.players(Football())
p.players(Cricket())
p.players(Tennis())


###Ex:2
from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class BasicCalculator(Calculator):
    def add(self,a,b):
        print("Addition using basic calculator=",a+b)
    def sub(self,a,b):
        print("Addition using basic calculator=",a-b)
class AdvancedCalculator(Calculator):
    def add(self,a,b):
        print("Addition using advanced calculator=",a+b)
    def sub(self,a,b):
        print("Substraction using advanced calculator=",a-b)
class Calculate:
    def cal(self,ref,a,b):
        ref.add(a,b)
        ref.sub(a,b)
def main():
    b=BasicCalculator()
    a=AdvancedCalculator()
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    c=Calculate()
    c.cal(b,n1,n2)
    c.cal(a,n1,n2)
main()

####----------Rules of Abstraction in Python---------------

##Rule 1:
'''In Python,we can not create the object of abstract classes'''

from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def display(self):
        pass
class Child(Parent):
    def display(self):
        print("Inside Child class")
#p=Parent()#Error:can't instantiate abstract class Parent with abstract method
        

##Rule 2:
'''In Python,we can not create the object of abstract classes even though the
class is having both anstract method and concrete methods.'''

from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def display(self):
        pass
    def fun(self):#concrete method
        print("Inside fun function")
class Child(Parent):
    def display(self):
        print("Inside Child class")
#p=Parent()#Error:can't instantiate abstract class Parent with abstract method


##Rule 3:
'''In Python,we can make a class as abstract class even if that class is not having
any abstract methods.
>In Python,Object of abstract class can be created if that class is having only
concrete method'''

from abc import ABC,abstractmethod
class Parent(ABC):
    def fun(self):#concrete method
        print("Inside fun function")
class Child(Parent):
    def display(self):
        print("Inside Child class")
p=Parent()
p.fun()#Inside fun function


##Rule 4:
'''In Python,Child classes must override all the abstract methods of Parent class'''

from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def fun(self):#abstract method
        pass
class Child(Parent):
    pass
c=Child()#Error:Can't instantiate abstract class Child with abstract method fun.
c.fun()











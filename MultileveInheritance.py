###----Multilevel Inheritance----------
class Parent1:
    def fun(self):
        print("Inside fun method")
    def fun1(self):
        print("Inside fun1 method")
class Parent2(Parent1):
    def fun2(self):
        print("Inside fun2 method")
class Child(Parent2):
    pass
c=Child()
c.fun()#Inside fun method
c.fun1()#Inside fun1 method
c.fun2()#Inside fun2 method

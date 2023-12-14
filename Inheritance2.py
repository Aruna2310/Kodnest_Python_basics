class Parent1:
    def __init__(self):
        self.x=100
        self.y=200
    def fun(self):
        print("Inside the fun method of Parent1")
    def fun1(self):
        print("Inside the fun1 method of Parent1")
class Parent2:
    def __init__(self):
        self.x=10
        self.y=20
    def fun(self):
        print("Inside the fun method of Parent2")
class Child(Parent2):
    pass
c=Child()
print(c.x)#10
print(c.y)#20
c.fun()#Inside the fun method of Parent2

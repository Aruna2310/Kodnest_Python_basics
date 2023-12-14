####-----Multiple Inheritance--------
'''Note:Python allows multiple Inheritance.
Multiple inheritance is a process in which a child class inheriting the property
and behavior of multiple parent classes'''

class Parent1:
    def __init__(self):
        self.x=10
    def fun(self):
        print("fun() in Parent1")
class Parent2:
    def __init__(self):
        self.x=200
    def fun1(self):
        print("fun1() in Parent2")
class Child(Parent1,Parent2):
    pass
c=Child()
print(c.x)         #10
c.fun()            #fun() in Parent1
c.fun1()           #fun1() in Parent2
print(Child.__mro__)##(<class '__main__.Child'>, <class '__main__.Parent1'>,
                    #<class '__main__.Parent2'>, <class 'object'>)

###----Method Resolution Order (MRO)---------
''' To Avoid the Dimond Shape Problem, Python follows "MRO" technique
>MRO internally works on "Linearization Algorithm
>To find MRO of a class we can use: classname.__mro__'''

class Child(Parent2,Parent1):
    pass
c=Child()
print(c.x)           #200
c.fun()              #fun() in Parent1
c.fun1()             #fun1() in Parent2
print(Child.__mro__) #(<class '__main__.Child'>, <class '__main__.Parent2'>,
                     #<class '__main__.Parent1'>, <class 'object'>)

'''In Python Instance variables are created inside the constructor of the class
##In python we have a inbuilt constructor,__init__().'''

class Fan:
    def __init__(self,color,cost,brandname):
        self.color=color
        self.cost=cost
        self.brandname=brandname
    def starts(self):
        print("Fan Starts")
    def stops(self):
        print("Fan Stops")
    def rotates(self):
        print("Fan rotates")
fan1=Fan("Brown",5000,"Bajaj")
print(fan1.color)
print(fan1.cost)
print(fan1.brandname)
fan1.starts()
fan1.stops()
fan1.rotates()

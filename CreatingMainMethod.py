###Creating Main Method
class Dog:
    def __init__(self,name,color,breed):
        self.name=name
        self.color=color
        self.breed=breed
    def barks(self):
        print("Dog barks")
    def eat(self):
        print("Dog eats Pedegree")
def main():
    d1=Dog("Tiger","Brown","Indie")
    d1.barks()
    d1.eat()
    print(d1.name,"",d1.color,"",d1.breed)
main()

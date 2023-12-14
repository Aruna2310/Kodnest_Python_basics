class Parent:
    def be_kind(self):
        print("Be kind to Animals")
    def cook(self):
        print("Parent cook veg biriyani")
class Child(Parent):
    def cook(self):
        print("child cooks Maggie")
    def play(self):
        print("child plays circket")
c=Child()
c.be_kind()
c.cook()
c.play()

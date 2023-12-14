####----------PolyMorphism in Python-------
###----Without using PolyMorphism------
class SecurityForce:
    def plan(self):
        print("Security Force Plans for Protecting the Nation")
    def attack(self):
        print("Security Force attacks using Weapons")
class ArmyForce(SecurityForce):
    def plan(self):
        print("Army Force Plans for Protecting Land")
    def attack(self):
        print("Army Force attacks using Tanks")
class NavyForce(SecurityForce):
    def plan(self):
        print("Navy Force Plans for Protecting ocean")
    def attack(self):
        print("Navy Force attacks using Ships")
class AirForce(SecurityForce):
    def plan(self):
        print("Air Force Plans for Protecting Airattack")
    def attack(self):
        print("Air Force attacks using jets")
def main():
    af=AirForce()
    af.plan()
    af.attack()
    nf=NavyForce()
    nf.plan()
    nf.attack()
    am=ArmyForce()
    am.plan()
    am.attack()
main()

'''In the above program Polymorphism or code flexibility is not achieved because
1)The statements inside the method of parent class is not used in any of the
child classes.
2)Inside the main(),plan() and attack() is called multiple times,Which clearly
shows that the same line of code is written multiple times in the program which
is not the good approach of coding.

To avoid two problems we need to achieve Polymorphism in the code.'''










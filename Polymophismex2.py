####----------PolyMorphism in Python-------
###------- With PolyMorphism------
'''Note:Polymorphism is a process of one method taking multiple forms during
execution.By using the Polymorphism, we can  achieve code reduction and
code reusability in the Program.'''

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
class BattleField:
    def safety(self,sf):
        sf.plan()
        sf.attack()
'''def main():
    am=ArmyForce()
    nf=NavyForce()
    af=AirForce()
    b=BattleField()
    b.safety(am)
    b.safety(nf)
    b.safety(af)
main()'''

def main():
    b=BattleField()
    b.safety(ArmyForce())
    b.safety(NavyForce())
    b.safety(AirForce())
main()

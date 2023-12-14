####--------Duck Typing in Python---------
'''In the below example we have used the object reference and performed
type checking.Based on the type checking we can call particular method present
inside that class.
>This Process of performing the typechecking of the object during the execution
time is known as Duck Typing.
>Duck typing can be performed only in the Dynamically Typed langauges.'''

class Addition:
    def add(self,x,y):
        print("Addition =",(x+y))
class Substraction:
    def sub(self,x,y):
        print("Substraction =",(x-y))
class Multiplication:
    def multiply(self,x,y):
        print("Product =",(x*y))
class Division:
    def div(self,x,y):
        print("Division =",(x/y))
class Calculate:
    def calculator(self,ref,x,y):
        if type(ref).__name__=="Addition":
            ref.add(x,y)
        elif type(ref).__name__=="Substraction":
            ref.sub(x,y)
        elif type(ref).__name__=="Multiplication":
            ref.multiply(x,y)
        elif type(ref).__name__=="Division":
            ref.div(x,y)
def main():
    a=Addition()
    s=Substraction()
    m=Multiplication()
    d=Division()
    x=int(input("Enter the 1st number "))
    y=int(input("Enter the 2nd number "))
    c=Calculate()
    c.calculator(a,x,y)
    c.calculator(s,x,y)
    c.calculator(m,x,y)
    c.calculator(d,x,y)
main()
    

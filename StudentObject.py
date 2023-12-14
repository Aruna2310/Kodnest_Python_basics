class Student:
    def __init__(self,roll_no,name,course):
        self.roll_no=roll_no
        self.name=name
        self.course=course
    def eat(self):
        print("Student eats food")
    def study(self):
        print("Student Studies")
st=Student(101,"Ravi","Python")
print(st.roll_no)
print(st.name)
print(st.course)
st.eat()
st.study()


## creating instance variables without creating __init__() constructor
'''In Python, Instance variables can be created either inside the constructor
(__init__()) or after the object creation using object reference'''

class Student:
    def study(self):
        print("Student Studies")
s1=Student()
s1.name="Raj"
s1.course="Python"
s1.study()
print(s1.name,"",s1.course)

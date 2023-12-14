###--------------Arguments In Python--------------

## Psitional Araguments
def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department?")

greet("Jenny","cs")#Hi Jenny
                            #Are you from cs department?
greet("cs","jenny")#Error



##Keyword Arguments
def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department?")

greet(name="Jenny",dept="cs")#Hi Jenny
                                              #Are you from cs department?
greet(dept="cs",name="Jenny")#Hi Jenny
                                               #Are you from cs department?

#Ex:2
def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department?")

greet("Jenny",dept="cs")


##Default Arguments
def greet(name,subject,dept="cs"):
    print(f"Hi {name}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")

greet("Jenny","Python")

##Arbitory / valuable lenth Arguments
def add(*num):
    c=0
    for i in num:
        c=c+i
    print(f"sum is {c}")
add(5,7,9)

#1)Arbitory Positional Arguments(*args)
#Ex:1
def add(*num):
    c=0
    for i in num:
        c=c+i
    print(f"sum is {c}")

add(1,2)
add(6,4,5)
add(1,3,4,56,23,8)


#Ex:2
def add(*num, name):
    print(num)
    print(name)
    c=0
    for i in num:
        c=c+i
    print(f"sum is {c}")

add(1,2,name="jenny")


#Ex:3
def add(a,*num):
    print(num)
    print(a)
    c=0
    for i in num:
        c=c+i
    print(f"sum is {c}")

add(1,2,5)


#Ex:4
def multiply(*args):
    m=1
    for nums in args:
        m=m*nums
    print(f"Product ={m}")

multiply(2,3,-6,8)
multiply(2,5,8,9,6,4)


#2)Arbitory keyword Arguments(**kwargs)

#Ex:1
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

info_person(name="Ram",age=30,dept="EC")
info_person(name="Shyam",dept="EC")

#Ex:2
def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)

info_person(1,2,name="Ram",age=30,dept="EC")
info_person(8,7,5,name="Shyam",dept="cs")






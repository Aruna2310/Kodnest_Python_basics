##-------Constructor Overloading---------
'''##Note::Python does not supports Constructor overloading.But only the recently created
method will be considered during execution'''
class Demo:
    def __init__(self):
        print("Inside __init__()")
    def __init__(self,a):
        print("Inside __init__(a)")
    def __init__(self,a,b):
        print("Inside __init__(a,b)")
    def __init__(self,a,b,c):
        print("Inside __init__(a,b,c)")
d=Demo()       #Error
d=Demo(10)     #Error
d=Demo(10,20)  #Error
d=Demo(10,20,30) #Inside __init__(a,b,c)



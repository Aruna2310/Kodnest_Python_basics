###-------Method Overloading----------
'''#Note:Method overloading is not supported in Python.But only the recently created
method will be considered while execution'''

class Demo:
    def disp(self):
        print("disp started")
    def disp(self,x):
        print("disp x started")
    def disp(self,x,y):
        print("disp x y started")
    def disp(self,x,y,z):
        print("disp x y z started")
d=Demo()
#d.disp()        #Error
#d.disp(10)      #Error
#d.disp(10,20)   #Error
d.disp(10,20,30) #disp x y z started




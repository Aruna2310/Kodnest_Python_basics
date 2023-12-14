###-----Exception Handling In Python----------------

##------ User Defined Exception Handler--------
## Example 1:
class Demo:
    def fun(self):
        try:
            a=10
            b=0
            c=a/b
            print(c)
        except:
            print("Inside Except Block")
d=Demo()
print("Program Starts")
d.fun()
print("Program Strops")


##Example 2:UDEH in multiple method cells
class Alpha:
    def alpha(self):
        try:
            print("Connection 3 Started")
            a=10
            b=0
            c=a/b
            print(c)
            print("Connection 3 Stopped")
        except:
            print("Inside Except Block")
class Beta:
    def beta(self):
        print("Connection 2 Started")
        a=Alpha()
        a.alpha()
        print("Connection 2 Stopped")
class Gamma:
    def gamma(self):
        print("Connection 1 Started")
        b=Beta()
        b.beta()
        print("Connection 1 Stopped")
g = Gamma()
g.gamma()


## Ex:3 Program using Single Except Block
''' If the program contains single except block, then the same exception message will be displayed
for all the different types of exceptions in the program as shown below'''

def calculate():
    try:
        n =int(input("Enter the numerator"))
        d =int(input("Enter the denomenator"))
        res = n/d
        print(res)
    except:
        print("Inside Except block")
calculate()


##Ex:4 Program using Multiple Except Blocks
''' If the programmer wants to display different exception messages for different exceptions then
programmer needs to make use of multiple except blocks in the code as shown below'''

class Demo:
    def fun(self):
        try:
            a=int(input("Enter the numerator"))
            b=int(input("Enter the denominator"))
            c=a/b
            print(c)
        except ZeroDivisionError:
            print("Don't Enter denominator as 0")
        except ValueError:
            print("Please enter only numbers")
        except NameError:
            print("Given variable name is not correct")
        except:
            print("Bugs found")
d = Demo()
d.fun()


###--------Creating UserDefinedExceptionHandler------------
#To create UserDefinedExceptionHandler we should inherrit from the base 'Exception' class
# to throw the exceptions we need to use "raise" keyword
#Ex 1:
class InvalidAgeError(Exception):
    pass
class DrivingLicense:
    def issue(self,age):
        if(age>10):
            print("you are eligible for driving license")
        else:
            print("you are not eligible for driving license")
            raise InvalidAgeError
d= DrivingLicense()
age=int(input("Enter the age"))
d.issue(age)

#Ex 2: Nested try-except Blocks
class InvalidPinError(Exception):
    pass

def verify():
    userpin=int(input("Please  Enter the PIN : "))
    pin=1234
    if(pin==userpin):
        print("Please Collect the cash")
    else:
        print("Invalid PIN")
        raise InvalidPinError

try:
    verify()
except:
    print("Worng Pin!! 2 attempts remaining, Try again!")
    try:
        verify()
    except:
        print("Worng Pin!! 1 attempt remaining, Try again!")
        try:
            verify()
        except:
            print("Card Blocked")
    
        
    
        


            
        
            
        
     











     














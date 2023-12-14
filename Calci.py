def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
add(10,20)

if __name__=='__main__()':
    sub(10,20)
    div(10,20)

#Note:If we don't want some functions to be imperted to another module then those functions
# must be put inside " if __name__=='__main__()': "

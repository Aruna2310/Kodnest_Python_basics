####----------Decorators in Python--------
'''Decorators are used to add extra functionalities to the existing function without changing the actual
code of the existing function.
>Decorators should be added above the existing function as @decor.'''

##EX 1:
def decor(function):
    def inner(name):
        if name == 'Mahesh':
            print(name,"likes veg Biriyani")
        else:
            function(name)
    return inner

@decor
def biriyani(name):
    print (name,"likes Non-veg Biriyani")
biriyani("Shakti")#Shakti likes Non-veg Biriyani
biriyani("Nataraj")#Nataraj likes Non-veg Biriyani
biriyani("Mahesh")#Mahesh likes veg Biriyani

'''In the above example,@decor is added to the biriyani(). During the execution,
internally biriyani(name) will be passed as an argument to decor().
inner() will collect the arguments passed in the the biriyani() eg:name.
Once the inner() completes its execution, it has to return the control to the outer function i.e decor().'''

##EX 2:
def smartdiv(function):
    def inner(a,b):
        if b==0:
            print ("b should not be Zero")
        else:
            return function(a,b)
    return inner

@smartdiv
def div(a,b):
    return a/b
print(div(10,20))#0.5
print(div(10,0))#b should not be Zero
                    # None


















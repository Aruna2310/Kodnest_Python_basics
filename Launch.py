####--------Modules in python---------
##-----importing the modules from different file in the same folder(Project)


#Ex 1: import module-name
''' once the module is imoprted as 'import Calci' then we need call the methods using module name as
shown below'''
import Calci
Calci.add(10,20)
Calci.sub(10,20)
Calci.multiply(10,20)
Calci.div(10,20)


#Ex 2:from module-name import  *
''' once the module is imoprted as 'from Calci import * ' then we need call the methods directly using
the name of the methods as shown below'''
from Calci import *
add(10,20)
sub(10,20)
multiply(10,20)
div(10,20)


#Ex 3: Aliasing a module name
''' Aliasing can be done by using the 'as' keyword followed by the alternate module name
>Once the module is aliased then the methods present inside the module should be called using the
aliased name'''
import Calci as a
a.add(10,20)
a.sub(10,20)
a.multiply(10,20)
a.div(10,20)


#Ex 4:Importing Selected instructions from different module
'''Here we are importing only add and sub functions from Calci Module.We are getting Error while
calling multiply() and div() because multiply() and div() are not imported from Calci'''
from Calci import add,sub
add(10,20)#30
sub(10,20)#-10
multiply(10,20)#NameError: name 'multiply' is not defined
div(10,20)##NameError: name 'div' is not defined


#Note:If we want to avoid to  import some functions from the importing module then those functions
# must be called inside " if __name__=='__main__()': "
















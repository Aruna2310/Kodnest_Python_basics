
##-------Tuple Data Type ( )---------------
'''tuple is a ordered collection of datatype which allows both homogeneous and
heterogeneous typedata and also it allows duplicate values.
---tuple in python is immutable in nature that is we can not modify tuple once
it is created and there is no predefined fuctions of tuple'''

####---------Creating tuple---------------
##Homogeneous type of data
tup=(10,20,30,40,50)
print(tup)#(10, 20, 30, 40, 50)
print(type(tup))#<class 'tuple'>


##Heterogeneous type data
tup1=(10,20.5,True,'k',(9+5j))
print(tup1)#(10, 20.5, True, 'k', (9+5j))
print(type(tup1))#<class 'tuple'>


##Duplicate data allowed
tup2=(10,20,20,30,30,30,40)
print(tup2)#(10, 20, 20, 30, 30, 30, 40)
print(type(tup2))#<class 'tuple'>

##we can delete the tuple from the memory
del tup
print(tup)#name 'tup' is not defined.

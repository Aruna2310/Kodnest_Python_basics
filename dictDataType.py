######---------dict Data Type----------------
'''Dict is a an ordered collection of datatype which allows both homogeneous and
heterogeneous type data(key:value pairs).
duplicate keys and values are allowed but the old value of the key will be
overrriden by the new value
-keys will act like index positions in dict'''

###Creating Dictionary
d={1:'one',2:'two',3:'three'}
print(d)      #{1: 'one', 2: 'two', 3: 'three'}
print(type(d))#<class 'dict'>

#Different types of keys are allowed in dict
d1={'one':1,9+10j:'Raj',10.5:'ten',True:'k'}
print(d1)      #{'one': 1, (9+10j): 'Raj', 10.5: 'ten', True: 'k'}
print(type(d1))#<class 'dict'>


#Different types of values are allowed in dict
d2={'one':1,9+10j:'Raj',10.5:True,True:9.1}
print(d2)      #{'one': 1, (9+10j): 'Raj', 10.5: True, True: 9.1}
print(type(d2))#<class 'dict'>


#Duplicate keys are not allowed in dict
d3={1:'one',1:'two',2:'raj',1:"Python"}
print(d3)      #{1: 'Python', 2: 'raj'}
print(type(d3))#<class 'dict'>
'''Note:Using duplicate keys will not give complile time error,but the old value
of the key will be overrriden by the new value'''


#Duplicate values are allowed in dict
d3={1:"Python",2:"Python",3:"python"}
print(d3)      #{1: 'Python', 2: 'Python', 3: 'python'}
print(type(d3))#<class 'dict'>'''

'''-------Accessing the elements from the dict---------'''
dt={1:'one',2:'two',3:'three'}

#-----direct Approach-----------
print(dt[3])#three


#---using for loop:only keys----
for i in dt:
    print(i,end=' ')#1 2 3 

print()
#---using for loop :only values----
for i in dt:
    print(dt[i],end=' ')#one two three 

print()
#---using for loop:both keys and values----
for i in dt:
    print(i,":",dt[i])#1 : one 2 : two 3 : three


print()
####-------using inbuilt methods---------
#only keys
for i in dt.keys():
    print(i,end=' ')#1 2 3 

print()
#only values
for i in dt.values():
    print(i,end=' ')#one two three 

print()
#keys and values
for i in dt.items():
    print(i)       #(1, 'one')(2, 'two')(3, 'three')

print()
'''--------Adding elements to the dict--------'''
#Update():Adds one or more items to the dict

dt.update({'name':'Raj','age':25})
print(dt)#{1:'one', 2:'two', 3:'three', 'name':'Raj', 'age':25}


print()
'''--------deleteing elements to the dict--------'''

#deleting using key
del dt[3]
print(dt)#{1:'one', 2:'two', 'name':'Raj', 'age':25}


#pop():delets the items using specified key       
dt.pop(2)
print(dt)#{1:'one', 'name':'Raj', 'age':25}


#popitem():delets last items from the dict
dt.popitem()
print(dt)#{1:'one', 'name':'Raj'}

#clear():clears all the items from the dict
dt.clear()
print(dt)#{}

#delets the complete datastructure or object from the memory
del dt 
print(dt)#NameError:








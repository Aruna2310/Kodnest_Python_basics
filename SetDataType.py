###----------Set Data Type  { } ----------
'''Set is a unordered collection of datatype which allows both homogeneous and
heterogeneous type data but it does not allow duplicate values.
--set does not have any index position'''

##Homogeneous type of data
s={10,20,30,40,50}
print(s)#{50, 20, 40, 10, 30}
print(type(s))#<class 'set'>


##Heterogeneous type of data
s1={10,20.5,True,'Code',(9+5j)}
print(s1)#{True, 20.5, 'Code', (9+5j), 10}
print(type(s1))#<class 'set'>


##Duplicates are not allowed
s2={10,20,20,30,30,30,40}
print(s2)#{40, 10, 20, 30}
print(type(s2))#<class 'set'>


###---------Accessing elelments from the set------
s={10,20,30,40,50}
'''set does not have index position so we can not access directly with index values'''

#print(s[3])#TypeError:'set' object is not subscriptable

#Accessing the elements using for loop
for i in s:
    print(i,end=' ')#50 20 40 10 30

print()
#Accessing the elements after converting set into list
s3=list(s)
print("After converting set to list: ",s3[2])#After converting set to list:40


###-------Adding elements to set-------------------
#add()
s.add(200)
print("Using add:",s)#Using add: {50, 20, 40, 10, 30, 200}

#update()
s.update({11,12})
print("Using update:",s)#Using update: {50, 20, 40, 10, 11, 12, 30, 200}


###------------Removing elements from set-----------
'''pop():removes the first element from the set'''
s.pop()
print("Using pop:",s)#Using pop: {20, 40, 10, 11, 12, 30, 200}

#s.pop(3)
#print(s)##TypeError:set.pop() takes no arguements

'''remove():we can remove the specified element from the set'''
s.remove(11)
print("Using remove:",s)#Using remove: {20, 40, 10, 12, 30, 200}

'''clear():clears all the elements from the set'''
s.clear()
print("Using clear:",s)#Using clear: set()

'''del keyword:deletes complete datastructure from the memory'''
del s
print(s)#name 's' is not defined












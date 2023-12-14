####-----Adavanced DataTypes-----
###----List data type---
'''List is a ordered collection of datatype which allows both homogeneous and
heterogeneous typedata and also it allows duplicate values.'''

##Storing homogeneous data
lst=[10,20,30,40,50]
print (lst)
print(type(lst))


##Storing heterogeneous data
lst1=[10,20.5,True,'k',10+5j]
print (lst1)
print(type(lst1))


##Duplicates are allowed
lst2=[10,20,20,30,40,40,50]
print (lst2)
print(type(lst2))


####Accssing the elements from list
lst3=[10,20,30,40,50]
print(lst3[3])#40

for i in lst3:
   print(i,end=' ')#[10 20 30 40 50]


###Adding Elements to the list

##append()   
lst.append(100)
print("Using append:",lst)#Using append: [10, 20, 30, 40, 50, 100]

'''lst.append(200,300)
print("Using append:",lst)'''#TypeError:list.append()takes exactly one argument

lst.append([200,300])
print("Using append:",lst)#Using append: [10, 20, 30, 40, 50, 100, [200, 300]]


##extend()
lst.extend([400])
print("Using extend:",lst)#Using extend: [10, 20, 30, 40, 50, 100, [200, 300], 400]

'''lst.extend(500)
print("Using extend:",lst)'''#TypeError: 'int' object is not iterable

lst.extend([11,12,13,14])
print("Using extend:",lst)#Using extend: [10, 20, 30, 40, 50, 100, [200, 300], 200, 11, 12, 13, 14]


##insert():insets element at the specified index position
lst2=[10,20,20,30,40,40,50]
lst2.insert(3,True)
print("Using insert:",lst2)#Using insert: [10, 20, 20, True, 30, 40, 40, 50]

'''lst2.insert(3,True,5,10+5j)
print("Using insert:",lst2)'''#TypeError: insert expected 2 arguments, got 4


###Removing elements from list:-
lst4=[10, 20, 30, 40, 50, 100, [200, 300], 200, 11, 12, 13, 14]

##remove(): 
lst4.remove(100)#removes the specified element from the list
print("Using remove:",lst4)#Using remove: [10, 20, 30, 40, 50, [200, 300], 200, 11, 12, 13, 14]


##pop(): 
lst4.pop()#removes the last element from the list
print("Using pop:",lst4)#Using pop: [10, 20, 30, 40, 50, [200, 300], 200, 11, 12, 13]

lst4.pop(5)#removes the element from the specified index
print("Using pop:",lst4)#Using pop: [10, 20, 30, 40, 50, 200, 11, 12, 13]


##clear():Clears all the element from the list
lst4.clear()
print(lst4)#[]

##del keyword
del lst4[5]#deletes the element from the specified index
print(lst4)#[10, 20, 30, 40, 50,11, 12, 13]

del lst4 #deletes the list datastructure from the memory
print(lst4)#Error:name 'lst4' is not defined




####----------Adding elements to the list----------------
lst=[10,20,30,40,50]
print(lst)

lst.append(100)
print("Using apprnd:",lst)#[10, 20, 30, 40, 50, 100]

lst.extend([200])    
print("Using append:",lst)#[10, 20, 30, 40, 50, 100, 200]

#lst.append(200,300) 
#print("Using append:",lst) #Error

lst.extend([11,22,33])
print("using extend",lst)#using extend [10, 20, 30, 40, 50, 100, 200, 11, 22, 33]

lst.append([200,300])
print("Using append",lst)#Using append [10, 20, 30, 40, 50, 100, 200, 11, 22, 33, [200, 300]]

lst.insert(3,700)
print("Using insert:",lst)

#push(55)
#print(lst) #Error:list object has no attribute push




####---------Removing the elements from the list------------------
lst1=[10,20,30,40,50]
print(lst1)

lst1.remove(30)
print("Using remove:",lst1)#[10, 20, 40, 50]

lst1.pop()    
print("Using pop:",lst1)#[10, 20, 40]

lst1.pop(1) 
print("Using pop:",lst1) #[10, 40]

del lst1 [1]
print("using del",lst1)#[10]

lst1.clear()
print("Using clear",lst1)#[]

del lst1   # deletes "lst1" datastructure from the memory 
print(lst1)#name 'lst' is not defined

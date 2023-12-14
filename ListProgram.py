##Ex 1: Creating new list from the original list
def even(lst1):
    for i in lst1:
     if(i%2==0):
        new_lst.append(i)
        
lst =[10,2,3,5,8,6]
new_lst=[]
even(lst)
print(lst)#[10,2,3,5,8,6]
print(new_lst)#[10, 2, 8, 6]

lst = [10,2,3,5,8,6]
even =list( filter (lambda num:num%2==0,lst))
print(lst)#[10,2,3,5,8,6]
print(even)#[10, 2, 8, 6]


##EX 2: Print the vowels in the given string using filter ()
st = "Technologies"
vowels="aeiou"
res=list(filter(lambda i: i in vowels,st))#converting filter object to list using list()
print(res)#['e', 'o', 'o', 'i', 'e']

res=str(filter(lambda i: i in vowels,st))#using str(), filter object can't be coverted to String
print(res)#<filter object at 0x0000028BE0B83A00>

res="".join(filter(lambda i: i in vowels,st))#filter object can be converted to string using join()
print(res)#eooie


##------List Comprehension-------
'''Syntax: [i for i in List-name]
'''
#Ex 1: Normal Method
lst=[10,20,30,40]
dup_lst=[]
for i in lst:
    dup_lst.append(i)
print(lst)#[10,20,30,40]
print(dup_lst)#[10,20,30,40]

#Ex 2: Using List Comprehension
lst=[10,20,30,40]
dup_lst=[i for i in lst]
print(lst)#[10,20,30,40]
print(dup_lst)#[10,20,30,40]


##-------List Slicing ----------
''' creating new list from the existing list is called as list slicing.
>Syntax: [start index:end index:steps]
>end index will always consider an elements (end index-1)'''

#Ex 1:
lst =[10,20,30,40,50,60]
print(lst)
print(lst[2::])#[30, 40, 50, 60]
print(lst[:4:])#[10, 20, 30, 40]
print(lst[1:5:2])#[20, 40]
print(lst[5::-1])#[60, 50, 40, 30, 20, 10]
    









    

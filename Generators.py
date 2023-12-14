###----------Generators in Python------

##---yield keyword----
#Ex 1:
def disp():
    yield 10
    yield 20
    yield 30
res=disp()
print(res.__next__())#10
print(res.__next__())#20
print(res.__next__())#30
#print(res.__next__())#Error:StopIteration

#Ex 2:
def disp():
    yield 10
    yield 20
    yield 30
res=disp()
while True:
    try:
        print(res.__next__())
    except:
        break

##--iter() and next()-----
#Ex 1:
lst=[10,20,30,40,50]
itr=iter(lst)
print(next(itr))#10
print(next(itr))#20
print(next(itr))#30
print(next(itr))#40
print(next(itr))#50
#print(next(itr))#Error:StopIteration


#Ex 2:
lst=[10,20,30,40,50]
itr=iter(lst)
while True:
    try:
        print(next(itr))
    except:
        break











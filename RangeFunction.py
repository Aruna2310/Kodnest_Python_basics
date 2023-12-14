#####------range ()------------
###range(start,stop,step):
##for start default value is 0
##for stop value will be (n-1)
##for step default is +1

#1-------with 2 arguments-----
for i in range(1,10):
          print(i,end=' ')#1 2 3 4 5 6 7 8 9 

#2----------with 3 arguments--------
print()
for i in range(5,15,2):
          print(i,end=' ')#5 7 9 11 13

#3
print()
for i in range(10,0,-1):
          print(i,end=' ')#10 9 8 7 6 5 4 3 2 1

#4
print()
for i in range(50,1,-5):
          print(i,end=' ')#50 45 40 35 30 25 20 15 10 5 

#5
print()
for i in range(10,0,-2):
          print(i,end=' ')#10 8 6 4 2

#6-------with 1 argument-----------
print()
for i in range(10):
    print(i,end=' ')#0 1 2 3 4 5 6 7 8 9 

#7
print()
##for i in range():
##   print(i)    #ERROR//TypeError: range expected at least 1 argument, got 0.

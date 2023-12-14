####-----Star Pattern1--------

for i in range(1,6):
    for j in range (1,6):
        print("*",end=' ')
    print()

####------Star Pattern2--------
for i in range(1,6):
    for j in range (1,i+1):
        print("*",end=' ')
    print()

#OR
for i in range(1,6):
    for j in range (i):
        print("*",end=' ')
    print()
        

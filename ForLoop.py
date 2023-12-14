###-------Looping Control Constructs-------

#####---For Loop-----
for i in "KodNest":
    print(i)

###--Note---
'''By default print() will have 'Newline or /n' as argument to the end statement,
hence the output will be printed in the next line.'''
# print (i, end='/n')

'''we can modify the output by passing different argument to end statement in
print()'''
    
for i in "KodNest":
    print(i,end=' ')#K o d N e s t

for i in "KodNest":
    print(i,end='@')#K@o@d@N@e@s@t@



#####---while loop--------
###Printing 1-10
i=1
while (i<=10):
    print(i,end=' ')
    i+=1 

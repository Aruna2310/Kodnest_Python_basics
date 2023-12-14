####-----File Handling in Python-------
'''We can perform 3 operations on txt Documents in python.
>read mode
>write mode
>append mode'''

##Reading the data from txt file
f1=open("Demo1.txt","r")
print(f1.read())

## Writing in the txt file
f2 =open("Demo2.txt","w")
f2.write("We are learning file handling in Python")
f2.close()# to see out put we need to open txt file.


##appending the data into the txt file
f1=open("Demo1.txt","a")
f1.write("JS can be called as programming langauge")
f1.close()

##WAPP to copy all the test from one file to another file
f1=open("Demo1.txt","r")
f2=open("Demo2.txt","w")
for i in f1:
    f2.write(i)
f2.close()

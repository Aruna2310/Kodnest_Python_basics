##------Inbuilt methods in string---------

s="I work Harder and Smarter"

####upper():will convert the string into uppercase
print(s.upper())#I WORK HARDER AND SMARTER

####lower():will convert the string into lower case
print(s.lower())#i work harder and smarter

####swapcase():will swap the uppercase chatacter into lower case and
#lowercase character into uppercase
print(s.swapcase())#i WORK hARDER AND sMARTER

s1="code with kodnest"

####capitalize():will convert the first character of the first word in the string
#into uppercase
print(s1.capitalize())#Code with kodnest

####title():will convert first character of all the words in a string into lowercase
print(s1.title())#Code With Kodnest


###Strings in Python are immutable in nature

s="Hello World"
s.lower()
print(s)#Hello World
print(s.lower())#hello world
print(s)#Hello World
s1=s.lower()
print(s1)#hello world


###----split() in Python-----
'''1)splict () in string used to chop or splict the string based on the given character
   2)if no arguments are passed to splict function,then it will cut the string
   where ever the space character is present
   3)splict() returns list of string'''

s="Hello World"
s=s.split()
print(s)#['Hello', 'World']

s1="Hello World"
s1=s1.split(" ")
print(s1)#['Hello', 'World']

s2="Python Programming Langauge"
s2=s2.split("o")
print(s2)#['Pyth', 'n Pr', 'gramming Langauge']

###-----------string comparision(==) in Python-------------

###Checking if the string values are equal or not
s1="Hello"
s2="Hello"
if(s1==s2):
    print("Strings are equal")
else :
    print("Strings are not equal")


s1="Hello"
s2="World"
if(s1==s2):
    print("Strings are equal")
else :
    print("Strings are not equal")


###Checking if references are equal or not

s1="Hello"
s2="Hello"
if(id(s1)==id(s2)):
    print("references are equal")
else:
    print("references are equal")


s1="Hello"
s2="hello"
if(id(s1)==id(s2)):
    print("references are equal")
else:
    print("references are equal")


###---Indexing in Python-----
s="Hello World"
print(s[2])#l
print(s[-5])#W


###---slicing of strings in python------
'''String slicing is a process of slicing the portion of the strings based on the
given start,stop and step values.

syntax 1:slice[stop]
syntax 2:slice[start:stop]
syntax 3:slice[start:stop:step]'''

s="Hello World"
print(s[2:8])##llo Wo
print(s[:10:2])##HloWr
print(s[-1:-5:-1])##dlro
print(s[-3:-10:-1])##roW oll
print(s[-1::-1])##dlroW olleH

















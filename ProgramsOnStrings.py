###----Program to count vowels----
s="Code With Kodnest"
s=s.lower()
count=0
for i in s :
    if(i=='a'or i=='e'or i=='i' or i=='o' or i=='u'):
        count+=1
print("Vowel count is",count)



###----Program to count vowels,consonants and special symbols----
s=input("Enter the string :")
#s="#Code With @Kodnest"
s=s.lower()
vowelcount=0
consonantcount=0
specialcount=0
for i in s :
    if(i>='a' and i<='z'):
        if(i=='a'or i=='e'or i=='i' or i=='o' or i=='u'):
            vowelcount+=1
        else:
            consonantcount+=1
    else:
        specialcount+=1
print("Number of vowels :",vowelcount)
print("Number of consonants :",consonantcount)
print("Number of specialsymbols :",specialcount)



####-----To Check the given string is palindrome or not-----

s=input("Enter the String")
s=s.lower()
s1=s[-1: :-1]
print("S=",s)
print("s1=",s1)
if(s==s1):
    print("String is Palindrome")
else:
    print("string is not Palindrome")






    

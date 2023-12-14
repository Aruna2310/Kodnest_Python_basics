s=input("Enter the String: ")
s=s.upper()
s1=s[-1::-1]
print("s=",s)
print("s1=",s1)
if(s==s1):
    print("Given String is Palindrome")
else:
    print("Given String is not Palindrome")

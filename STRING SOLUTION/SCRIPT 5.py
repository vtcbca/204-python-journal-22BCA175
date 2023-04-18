s=input("Enter any string:")

half=int(len(s)/2)

f=s[:half]
s=s[half:]

if f==s:
    print("String is Symmetrical.")
else:
    print("String is not Symmetrical.")

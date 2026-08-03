## 18. Check whether a character is uppercase or lowercase.
char=input("Enter the character = ")
if len(char) != 1:
    print("Please enter only one character")
elif 'a' <= char <= 'z':
    print("This character is lowercase =",char)
elif  'A' <= char <= 'Z':
    print("This character is uppercase =",char)
else:
    print("Invalid character") 
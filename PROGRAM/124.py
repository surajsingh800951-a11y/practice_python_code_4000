## 124. Check whether a character is an alphabet, digit, or special character.
char=input("Enter the character = ")
if len(char) == 1:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        print("Alphabet =",char)
    elif '0' <= char <= '9':
        print("Digit =",char)
    else:
        print("Special character")
else:
    print("Please enter the only one character")  

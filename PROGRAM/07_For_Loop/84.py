# 84. Reverse a string using a for loop.
string=input("Enter your name = ")
#for i in string[: :-1]:  # Shortcut Method
for i in range(len(string)-1,-1,-1):
    print(string[i])
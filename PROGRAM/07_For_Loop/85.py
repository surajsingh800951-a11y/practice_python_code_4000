# 85. Count the occurrence of a given character.
string=input("Enter your name = ")
char=str(input("Enter any one character = "))
count=0
for i in string:
    if i == char:
        count+=1
print("Count the occurrence",char,"=",count)
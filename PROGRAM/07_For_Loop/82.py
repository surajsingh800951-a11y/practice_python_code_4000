# 82. Count digits in a string.
string=input("Enter your name = ")
count=0
for i  in string:
    if '0' <= i <= '9':
    #if i.isdigit():   #  i.isdigit() => Function method
        count+=1
print("Count digits =",count)
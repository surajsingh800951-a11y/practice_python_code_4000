# 81. Count lowercase letters in a string.
string=str(input("Enter your name = "))
count=0
for i in string:
    if 'a' <= i <= 'z': #if i.islower(): =  Function method
    #if i.islower():
        count+=1
print("Count lowercase letters =",count)
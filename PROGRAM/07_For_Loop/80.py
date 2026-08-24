# 80. Count uppercase letters in a string.
string=str(input("Enter a string = "))
count=0
for i in string:
    if 'A' <= i <= 'Z':  #if i.isupper(): =  Function method
    #if i.isupper():
        count+=1
print("Count uppercase =",count) 

# if i.isupper():
# i uppercase letter hai?

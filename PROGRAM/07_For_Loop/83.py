# 83. Count spaces in a string.
string=(input("Enter your name = "))
count=0
for i in string:
    if i == " ": 
    #if i.isspace():  # Function Method 
        count+=1
print("Count spaces =",count)
    
        
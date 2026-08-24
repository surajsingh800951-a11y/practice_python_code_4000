# 83. Count spaces in a string.
string=(input("Enter a string = "))
count=0
for i in string:
    if i == " ": 
    #if i.isspace():  # Function Method 
        count+=1
print("Count spaces =",count)
    
        
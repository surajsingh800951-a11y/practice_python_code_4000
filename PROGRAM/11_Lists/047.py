# 47. Print all elements of a list using negative indexing.
listt=[21,56,48,65,75,32,56,58,69]

#print(listt[::-1]) # Using Slicing


n=len(listt)+1
for i in range(-1,-n,-1): # Using loop
    print(listt[i])
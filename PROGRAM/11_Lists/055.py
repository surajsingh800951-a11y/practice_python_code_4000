# 61. Take an index and value from the user and insert the value at that index.
listt=[12,4,5,35,67,2,4,6]
index=int(input("Enter index number = "))
value=int(input("Enter a value = "))
if index <= len(listt):
    listt.insert(index,value)
    print(listt)
else:
    print("Please Correct index number")


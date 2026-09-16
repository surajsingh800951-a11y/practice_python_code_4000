# 85. Check whether a value exists before using remove().
listt=[12,3,4,3,4,3]
n=int(input("Enter a value = "))
if n in listt:
    listt.remove(n)
    print(listt)
else:
    print("Value not found")
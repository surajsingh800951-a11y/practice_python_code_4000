# 52. Create an empty list and add 5 numbers using append().
listt=[]
# listt.append(10)
# listt.append(89)
# listt.append(50)   # Normal
# listt.append(30)
# listt.append(20)
# print(listt)

for i in range(5):
    n=int(input("Enter number = "))  # Using For loop
    listt.append(n)
print(listt)


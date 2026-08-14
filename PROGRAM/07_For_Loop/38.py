# 38. Take 5 numbers from the user and find the smallest number.
smal=int(input("Enter a number = "))
for i in range(4):
    n=int(input("Enter a number = "))
    if smal > n:
        smal=n
print("Smallest =",smal)
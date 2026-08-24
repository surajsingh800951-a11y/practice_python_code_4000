# 37. Take 5 numbers from the user and find the largest number
larg=int(input("Enter a number = "))
for i in range(4):
    n=int(input("Enter a number = "))
    if n > larg:
        larg=n
print("Largest = ",larg)        
    
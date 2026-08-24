# 51. Print a rectangle star pattern.
'''
*************
*************
*************
*************
'''
n=int(input("Enter a number = "))
for i in range(n):
    for j in range(n*2):
        print("*",end=" ")
    print()
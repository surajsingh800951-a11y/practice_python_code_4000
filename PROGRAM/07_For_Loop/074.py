# 74. Print a same-alphabet triangle.
'''
A
BB
CCC
DDDD
EEEEE
'''
n=int(input("Enter a number = "))
for i in  range(n):
    for j in range(i+1):
        print(chr(65+i),end="")
    print()
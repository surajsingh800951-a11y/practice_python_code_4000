# 73. Print a reverse alphabet triangle.
'''
ABCDE
ABCD
ABC
AB
A
'''
n=int(input("Enter a number = "))
for i  in range(n,0,-1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()
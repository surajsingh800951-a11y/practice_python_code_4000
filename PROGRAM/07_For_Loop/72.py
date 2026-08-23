# 72. Print an alphabet triangle.
'''
A
AB
ABC
ABCD
ABCDE
'''
n=int(input("Enter a number = ")) # 5
for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()

# 75. Print an alphabet pyramid.
'''
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
'''
n=int(input("Enter a number = "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i*2-1):
        print(chr(65+k),end="")
    print()
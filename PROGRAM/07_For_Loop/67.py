# 67. Print a number diamond pattern.
'''
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1
'''
n=int(input("Enter a number = "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i*2):
        print(k,end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i*2):
        print(k,end="")
    print()
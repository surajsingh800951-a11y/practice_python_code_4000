# 65. Print a number pyramid.
'''
    1
   123
  12345
 1234567
123456789
'''
#n=int(input("Enter a number = "))
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i*2):
        print(k,end="")
    print()
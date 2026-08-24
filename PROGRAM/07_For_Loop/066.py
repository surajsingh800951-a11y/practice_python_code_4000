# 66. Print a reverse number pyramid.
'''
123456789
 1234567
  12345
   123
    1
'''
n=int(input("Enter a number = ")) # Example : 5 
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i*2):
        print(k,end="")
    print() 


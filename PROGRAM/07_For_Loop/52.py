# 52. Print a pyramid star pattern.
'''
    *
   * *
  * * * 
 * * * * 
* * * * * 
'''
n=int(input("Enter a number = "))
for i in range(n):
    for j in range(1,n,-1):
        print(" ",end="")
for k in range(1,n+1):
    for s in range(k):
        print("*",end="")
    print()   
        
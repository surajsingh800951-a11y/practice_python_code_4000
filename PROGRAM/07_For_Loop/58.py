# 58. Print a diamond star pattern.
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    * 
'''
n=int(input("Enter a number = "))
for i in range(1,n+2,1): # 7  => 7+2= 9 => 9-1=8 ==> 7
    if i < n+1:
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print()
    else:
        for i in range(n-1,0,-1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(1,2*i):
                print("*",end="")
            print()

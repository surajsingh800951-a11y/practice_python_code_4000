# 53. Print an inverted pyramid pattern.
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
n=int(input("Enter a number = ")) #5 -4=1
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()    
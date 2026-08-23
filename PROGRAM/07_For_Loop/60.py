# 60. Print this reverse number triangle:
'''
5
54
543
5432
54321
'''
#n=int(input("Enter a number = "))
n=5
for i in range(1,n+1):
    for j in range(n,n-i,-1): #  0 -1
        print(j,end="")
    print()
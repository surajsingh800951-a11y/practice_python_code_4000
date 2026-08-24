# 63. Print this reverse sequence pattern:
'''
54321
5432
543
54
5
'''
#=int(input("Enter a number = "))
n=5
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j,end="")
    print()
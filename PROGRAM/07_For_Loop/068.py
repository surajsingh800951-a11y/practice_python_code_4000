# 68. Print this pattern:
'''
1
23
456
78910
'''
n=4
s=1
for i in range(1,n+1):
    for j in range(i):
        print(s,end="")
        s+=1
    print()
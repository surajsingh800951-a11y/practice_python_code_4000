# 157. Print factorial values from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1 = 120
n=int(input("Enter a number = "))
for i in range(1,n+1):
    total=1
    for j in range(i,0,-1):# 5 ,0,-1
        total=total*j # 5 = 1*5 =5*4 =20*3 =60*2 =120*1 =120
    print("Factorial values",i,"=",total)
    
# 155. Print the series 2, 4, 8, 16, 32....
n=int(input("Enter number of terms = "))
m=1 # 1 , 2 , 4 , 8
for i in range(1,n+1):
    print(m*2,end=" ,")
    m=m*2
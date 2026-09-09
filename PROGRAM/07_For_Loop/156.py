# 156. Print the first n terms of 1, 2, 4, 8....
n=int(input("Enter number of terms = "))
m=1
for i in range(1,n+1):
    print(m,end=" ,")
    m=m*2
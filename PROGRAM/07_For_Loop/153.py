# 153. Print the series 1, 11, 111, 1111....
n=int(input("Enter number of terms = "))
m="1"
for i in range(1,n+1):
    print(m,end=",")
    m+="1"
    
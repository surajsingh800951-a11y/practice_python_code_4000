# 154. Find the sum of the series 1 + 11 + 111 + 1111....
n=int(input("Enter number of terms = "))
m="1"
total=0
for i in range(0,n):
    total+=int(m)
    m+="1"
print("Sum of the series 1 + 11 + 111 + 1111.... =",total)

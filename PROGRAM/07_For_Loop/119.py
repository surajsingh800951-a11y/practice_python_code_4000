# 119. Print digits in ascending order.
n = input("Enter a number = ")
for i in range(10):
    for j in str(n):
        if str(i) == j:
            print(j)
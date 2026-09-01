# 120. Print digits in descending order.
n=input("Enter a number = ")
for i in range(10,-1,-1):
    for j in n:
        if str(i) == j:
            print(j)
    
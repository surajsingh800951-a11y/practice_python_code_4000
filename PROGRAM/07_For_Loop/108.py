# 108. Print digits in reverse order.
n=int(input("Enter a number = "))
#n=87453
for i in range(len(str(n))):
    digit= n % 10 
    n=n//10
    print(digit)
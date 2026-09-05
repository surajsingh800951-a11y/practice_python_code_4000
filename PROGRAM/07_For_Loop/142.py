# 142. Find the HCF/GCD of two numbers.
# 141. Find the prime factorization of a number.
n = int(input("Enter a number = "))
for i in range(2, n + 1):
    while n % i == 0:
        print(i, end=" ")
        n = n // i
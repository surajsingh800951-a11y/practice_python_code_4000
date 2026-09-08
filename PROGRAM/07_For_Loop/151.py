# 151. Find the sum 1² + 2² + 3² + ... + n²
n=int(input("Enter number of terms = "))
total=0
for i in range(1,n+1):
    total+=i ** 2
print("Sum 1² + 2² + 3² + ... + n² =",total)
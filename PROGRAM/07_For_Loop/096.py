# 96. Reverse a number.
# n =input("Enter a number = ")
# reverse=""    # reverse=n[::-1] Function method
# for i in n:    
#     reverse=i+reverse
# print("Reverse =",reverse)

      # Logic base 

n =int(input("Enter a number = "))
rev=0
for i in range(len(str(n))):
    digit=n % 10
    rev=rev*10+digit
    n= n//10
print(rev)
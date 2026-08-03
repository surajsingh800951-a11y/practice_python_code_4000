## 19. Check whether a number is divisible by 2, 3, both, or neither.
num=int(input("Enter the number = "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3 =",num)
elif num % 2 == 0:
    print("Divisible by 2 only =",num)
elif num % 3 == 0:
    print("Divisible by 3 only =",num)
else:
    print("Divisible by neither 2 nor 3 =",num)
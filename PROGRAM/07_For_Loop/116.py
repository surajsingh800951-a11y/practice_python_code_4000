# 116. Check whether all digits are even.
n=input("Enter a number = ")
for i in n:
    if int(i) % 2 != 0:
        print("All digits are not even")
        break
else:
    print("All digit are even")
        
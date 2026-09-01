# 117. Check whether all digits are odd.
n=input("Enter a number = ")
for i in n:
    if int(i) % 2 == 0:
        print("All digits are not odd")
        break
else:
    print("All digits are odd")
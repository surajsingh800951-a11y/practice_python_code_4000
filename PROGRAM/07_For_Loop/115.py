# 115. Check whether any digit is repeated.
n=input("Enter a number = ")
done=""
for i in n:
    if i in done:
        print("Digit is repeated")
        break
    done+=i
else:
    print("Digit is not repeated")
        
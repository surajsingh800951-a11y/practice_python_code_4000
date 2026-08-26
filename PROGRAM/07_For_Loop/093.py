# 93. Print common characters between two strings.
string=input("Enter a first string = ")
string_2=input("Enter a Second string = ")
done=""
for i in string:
    for j in string_2:
        if i == j and i not in done:
            print("Common characters between two strings =",i)
            done+=i
# 86. Print the frequency of every character.
string=input("Enter a string = ")
for i in string:
    count = 0
    for j in string:
        if i == j:
            count += 1
    print(i, "=", count)
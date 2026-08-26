# 90. Find the first non-repeating character.
string=input("Enter a string = ")
done=""
for i in string:
    count=0
    for j in string:
        if i == j:
            count+=1
    if count == 1:
        print(i)
        break

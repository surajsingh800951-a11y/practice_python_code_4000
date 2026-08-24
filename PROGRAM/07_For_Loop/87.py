# 87. Print duplicate characters.
string=input("Enter a string = ")
done=""
for i in string:
    count=0
    for j in string:
        if i == j:
            count+=1
    if count > 1 and i not in done :
        print(i)
        done +=i

# 91. Find the most frequent character.
string=input("Enter a string = ")
max_count=0
most=""
for i in string:
    count=0
    for j in string:
        if i == j:
            count+=1
    if count > max_count:
        max_count=count
        most=i
print("most frequent character =",most)
print("Frequency =",max_count)

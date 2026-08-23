# 78. Count vowels in a string.
string=str(input("Enter your name = "))
count=0
for i in string:
    if 'a' == i or 'o' == i or 'u' == i or 'i' == i or 'e' == i:
        count+=1
print("Count vowels =",count)
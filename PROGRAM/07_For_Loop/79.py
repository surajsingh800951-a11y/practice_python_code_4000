# 79. Count consonants in a string.
string=str(input("Enter your name = "))
count=0
for i in string:
    if (i >='a'and i<='z') or (i>='A' and i<='Z'):  # if i.isalpha() and i not in "aeiou": 
        if 'a' != i and 'o' != i and 'u' != i and 'i' != i and 'e' != i:  
            count+=1
print("Count consonants =",count)


# isalpha()       → character alphabet hai?
# i not in aeiou  → vowel nahi hai?

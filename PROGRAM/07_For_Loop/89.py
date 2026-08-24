# 89. Find the first repeating character.
string=input("Enter a string = ")
done=""
for i in string:
    if i in done :
        print(i)
        break
    done+=i
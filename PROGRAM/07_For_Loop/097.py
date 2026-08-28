# 97. Check whether a number is a palindrome.
num=int(input("Enter a number = "))
n=num
rev=0
for i in range(len(str(num))):
    digit=num % 10 
    rev=rev*10+digit
    num=num//10
if(n == rev):
    print("Number is a palindrome")
else:
    print("Number is a not palindrome")
        
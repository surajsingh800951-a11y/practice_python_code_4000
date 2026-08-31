# 113. Find the second-smallest digit.
n=int(input("Enter a number = "))
#n=98741
prev=0
curr=9
for i in range(len(str(n))):
    digit = n % 10
    n = n // 10
    if digit < curr :
        prev=curr
        curr=digit
    elif digit < prev and prev != curr :
        prev=digit      
print("Second-smallest digit =",prev)
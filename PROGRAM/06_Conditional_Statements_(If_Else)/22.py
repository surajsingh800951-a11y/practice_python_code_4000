## 22. Find the largest among four numbers.
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
d=int(input("Enter the fourth number = "))
if a >= b and a >= c and a >= d:
    print("Largest number = ",a)
elif b >= a and b >= c and b >= d:
    print("Largest number = ",b)      # Simple and essay
elif c >= a and c >= b and c >= d:
    print("Largest number = ",c)
else:
    print("Largest number = ",d)
    # if a < b:  
#     if b < c:
#         if c < d:
#             print("Largest number = ",d)
#         else:
#             print("Largest number = ",c)
#     elif b < d:
#         print("Largest number = ",d)
#     else:
#         print("Largest number = ",b)
# elif a < c:
#     if c < d:
#         print("Largest number = ",d)
#     else:
#         print("Largest number = ",c)
# elif a < d:
#     print("Largest number = ",d)
# else:
#     print("Largest number =",a)
            

# 9. Write a program to create a shallow copy of a list of electricity bills using copy().

a=[12,2,3,[75,4,5,3,3]]

b=a.copy()  # [12,2,50,[75,4,5,3,3]]
b[3][2]=50
print("Original=",a)
print()
print("Copy list",b)
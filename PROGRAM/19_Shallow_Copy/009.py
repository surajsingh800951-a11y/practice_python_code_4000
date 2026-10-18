# 9. Write a program to create a shallow copy of a list of electricity bills using copy().

electricity_bills = [
    ["Suraj", 1250],
    ["Ravi", 980],
    ["Amit", 1450],
    ["Pankaj", 1100]
]

e_b_copy = electricity_bills.copy()

print("Original List =", electricity_bills)
print("Shallow Copy =", e_b_copy)
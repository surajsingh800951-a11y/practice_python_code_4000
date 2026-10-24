# 22. Write a program to create a shallow copy of a list of employee data using slicing [:].

employee = [
    ["Suraj", "E101", 25000],
    ["Surya", "E102", 30000],
    ["Shivam", "E103", 28000],
    ["Rahul", "E104", 32000]
]

employee_copy = employee[:]

print("Original List =", employee)
print("Shallow Copy =", employee_copy)
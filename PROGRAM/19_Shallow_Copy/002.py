# 2. Write a program to create a shallow copy of a list of employee data using copy().
employee=[
    ["Suraj Singh","ID",20],
    ["Surya Singh","ID",23],
    ["Shivam Yadav","ID",24]
    ]
employee_copy=employee.copy()
employee_copy[2][2]=30
print(employee_copy[2])
print("Original List =",employee)
print("Shallow Copy =",employee_copy)
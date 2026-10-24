# 21. Write a program to create a shallow copy of a list of student records using slicing [:].
student = [
    ["Suraj", 20],
    ["Surya", 21],
    ["Shivam", 19],
    ["Rahul", 22]
]

student_copy = student[:]

print("Original List =", student)
print("Shallow Copy =", student_copy)
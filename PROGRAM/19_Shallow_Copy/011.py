# 11. Write a program to create a shallow copy of a list of exam results using copy().
exam_results = [
    ["Suraj", 85],
    ["Surya", 78],
    ["Shivam", 92],
    ["Rahul", 74]
]

e_r_copy = exam_results.copy()

print("Original List =", exam_results)
print("Shallow Copy =", e_r_copy)
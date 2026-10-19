# 21. Write a program to create a shallow copy of a list of student records using slicing [:].
delivery_addresses = [
    ["Suraj", "Varanasi"],
    ["Rahul", "Lucknow"],
    ["Amit", "Delhi"],
    ["Shivam", "Kanpur"]
]

d_a_copy = delivery_addresses.copy()

print("Original List =", delivery_addresses)
print("Shallow Copy =", d_a_copy)
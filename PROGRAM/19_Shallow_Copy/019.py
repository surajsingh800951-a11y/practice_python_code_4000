# 19. Write a program to create a shallow copy of a list of user ages using copy().
user_ages = [
    ["Suraj", 20],
    ["Surya", 23],
    ["Shivam", 24],
    ["Rahul", 21]
]

u_a_copy = user_ages.copy()

print("Original List =", user_ages)
print("Shallow Copy =", u_a_copy)
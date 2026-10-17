# 7. Write a program to create a shallow copy of a list of cricket scores using copy().
cricket_score=[
    ["Virat",85],
    ["Surya",86],
    ["Hardik",99],
    ["Vaibhav",86]
]

c_s_copy=cricket_score.copy()

print("Original List =",cricket_score)
print("Shallow Copy =",c_s_copy)
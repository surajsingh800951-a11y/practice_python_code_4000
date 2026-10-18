# 18. Write a program to create a shallow copy of a list of recipe ingredients using copy().
recipe_ingredients = [
    ["Flour", 500],
    ["Sugar", 200],
    ["Milk", 1],
    ["Butter", 100]
]

r_i_copy = recipe_ingredients.copy()

print("Original List =", recipe_ingredients)
print("Shallow Copy =", r_i_copy)
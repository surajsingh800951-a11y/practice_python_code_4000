# 14. Write a program to create a shallow copy of a list of product inventory using copy().
product_inventory = [
    ["Laptop", 10],
    ["Mouse", 25],
    ["Keyboard", 15],
    ["Monitor", 8]
]

p_i_copy = product_inventory.copy()

print("Original List =", product_inventory)
print("Shallow Copy =", p_i_copy)
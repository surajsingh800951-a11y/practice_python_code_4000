# 16. Write a program to create a shallow copy of a list of restaurant orders using copy().
restaurant_orders = [
    ["Pizza", 2],
    ["Burger", 3],
    ["Pasta", 1],
    ["Sandwich", 4]
]

r_o_copy = restaurant_orders.copy()

print("Original List =", restaurant_orders)
print("Shallow Copy =", r_o_copy)
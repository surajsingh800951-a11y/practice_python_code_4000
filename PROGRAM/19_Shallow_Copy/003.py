# 3. Write a program to create a shallow copy of a list of shopping cart items using copy().
cart=[
    ["Laptop",1,55000],
    ["Mouse",2,500],
    ["Keyboard",1,1000]
]
cart_copy=cart.copy()

cart_copy[0][2]=56000

print("Original List",cart)
print("Shallow Copy",cart_copy)

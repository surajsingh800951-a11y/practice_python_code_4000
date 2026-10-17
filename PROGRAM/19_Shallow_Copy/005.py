# 5. Write a program to create a shallow copy of a list of temperature readings using copy().
temperature = [
    ["Delhi", 35],
    ["Varanasi", 32],
    ["Lucknow", 30]
]
t_copy=temperature.copy()
t_copy[2][0]="Mumbai"
print("Original Listt =",temperature)
print("Shallow Copy =",t_copy)
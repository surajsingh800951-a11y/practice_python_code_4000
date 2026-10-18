# 15. Write a program to create a shallow copy of a list of traffic signals using copy().
traffic_signals = [
    ["Signal 1", "Red"],
    ["Signal 2", "Green"],
    ["Signal 3", "Yellow"],
    ["Signal 4", "Red"]
]

t_s_copy = traffic_signals.copy()


print("Original List =", traffic_signals)
print("Shallow Copy =", t_s_copy)
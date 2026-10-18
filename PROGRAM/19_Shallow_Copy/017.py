# 17. Write a program to create a shallow copy of a list of game scores using copy().

game_scores = [
    ["Player 1", 85],
    ["Player 2", 92],
    ["Player 3", 78],
    ["Player 4", 88]
]

g_s_copy = game_scores.copy()

g_s_copy[3][1]=100

print("Original List =", game_scores)
print("Shallow Copy =", g_s_copy)
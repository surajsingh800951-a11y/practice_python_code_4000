# 13. Write a program to create a shallow copy of a list of stock prices using copy().
stock_prices = [
    ["TCS", 3500],
    ["INFY", 1800],
    ["RELIANCE", 2900],
    ["HDFC", 1700]
]

s_p_copy=stock_prices.copy()

s_p_copy[0][1]=4000

print("Original List =",stock_prices)
print("Shallow Copy =",s_p_copy)
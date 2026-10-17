# 4. Write a program to create a shallow copy of a list of bank transactions using copy().
bank_transactions= [
    ["TXN001", "Deposit", 5000],
    ["TXN002", "Withdraw", 2000],
    ["TXN003", "Deposit", 3500]
]

b_t_copy=bank_transactions.copy()

b_t_copy[2][2]=3566

print("Original List",bank_transactions)
print("Shallow Copy",b_t_copy)
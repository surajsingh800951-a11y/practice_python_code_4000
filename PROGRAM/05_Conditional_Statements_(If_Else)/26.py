## 26. Calculate discount based on purchase amount.
amount=int(input("Enter the amount = "))
discount=0
if amount <= 0:
    print("Invalid Amount")
elif 1 <= amount < 1000:
    discount=amount*5/100  # 5% Discount 
    print("Discount =",discount)
elif 1000 <= amount <= 5000:
    discount=amount*10/100 # 10% Discount
    print("Discount =",discount)
else:
    discount=amount*20/100 # 20% Discount 
    print("Discount =",discount)

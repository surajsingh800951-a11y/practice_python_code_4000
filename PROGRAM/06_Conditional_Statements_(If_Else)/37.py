# Q37. Shopping Mall  
#       Agar shopping ₹5000 ya usse zyada hai → Free Gift.  
#       Agar ₹2000–4999 hai → 10% Discount.  
#       Agar ₹2000 se kam hai → Koi offer nahi.

shop=int(input("Please enter shopping amount = "))
dis=0
if shop <= 0:
    print("Please confirm the total amount of your shopping.")
elif shop >= 5000:
    print("Free Gift")
elif shop >=2000:
    dis = shop*10/100
    print("10% Discount =",dis)
else:
    print("Koi offer nhi hai")
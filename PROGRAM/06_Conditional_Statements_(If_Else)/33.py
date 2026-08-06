#  Q33. Mobile Recharge  
#       Agar balance ₹299 ya usse zyada hai → 28 days recharge.  
#       Agar balance ₹199–298 hai → 14 days recharge.  
#       Agar ₹199 se kam hai → Recharge nahi ho sakta.


balance=int(input("Enter the balance = "))
if balance <= 0:
    print("Enter a valid balance")
elif balance >= 299:
    print("28 days recharge")
elif balance >= 199:
    print("14 days recharge")
else:
    print("Recharge nahi ho sakta")
# Q32. ATM Withdrawal  
#       Agar balance ₹5000 ya usse zyada hai → Paise nikal sakte ho.  
#       Agar balance ₹1000–4999 hai → Sirf ₹1000 nikal sakte ho.  
#       Agar balance ₹1000 se kam hai → Insufficient Balance.


amount=int(input("Please enter amount = "))
if amount >= 5000:
    print("Paise nikal sakte ho")
elif amount >= 1000:
    print("Sirf ₹1000 nikal sakte ho")
else:
    print("Insufficient Balance ( Aparyapt shesharashi )")
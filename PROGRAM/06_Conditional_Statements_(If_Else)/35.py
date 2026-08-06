# Q35. Petrol Pump  
#       Agar paise ₹500 ya usse zyada hain → Full tank.  
#       Agar paise ₹100–499 hain → Jitna petrol mile utna bharwao.  
#       Agar ₹100 se kam hain → Petrol nahi milega.

amount=int(input("Please enter the amount = "))
if amount <= 0:
    print("Please enter a valid ammount")
elif amount >= 500 :
    print("Full tank")
elif amount >= 100:
    print("Jitna petrol mile utna bharwao")
else :
    print("Petrol nahi milega")
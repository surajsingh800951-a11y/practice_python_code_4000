# Q40. Ice Cream Shop  
#       Agar paise ₹100 hain → Chocolate Ice Cream.  
#       Agar paise ₹50–99 hain → Vanilla Ice Cream.  
#       Agar paise ₹50 se kam hain → Ice Cream nahi milegi.
paise=int(input("Enter the amount = "))
if paise <=0:
    print("Invalid Amount")
elif paise >= 100:
    print("Chocolate Ice cream")
elif 50 <= paise < 100:
    print("Vanilla Ice Cream")
else:
    print("Ice Cream nahi milegi")
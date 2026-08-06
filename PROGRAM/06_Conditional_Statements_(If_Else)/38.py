# Q38. Bus Ticket  
#       Age 60 ya usse zyada → Senior Citizen Discount.  
#       Age 5–59 → Full Ticket.  
#       Age 5 se kam → Free Ticket.

age= int(input("Enter your age = "))
if age < 0:
    print("Invalid age")
elif age >= 60:
    print("Senior Citizen Discount")
elif age >=5:
    print("Full Ticket")
else:
    print("Free Ticket")
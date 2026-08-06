# Q31. Movie Ticket  
#       Agar age 18 ya usse zyada hai → Movie dekh sakta hai.  
#       Agar age 12–17 hai → Parent ke saath dekh sakta hai.  
#       Agar age 12 se kam hai → Entry nahi milegi.



age=int(input("Please enter your age = "))
if age <= 0:
    print("Please enter a valid age")
elif age >= 18:
    print("Movie dekh sakte hai")
elif age >= 12:
    print("Parents ke saath dekh sakte hai")
else:
    print("Sorry Entry nahi milegi")

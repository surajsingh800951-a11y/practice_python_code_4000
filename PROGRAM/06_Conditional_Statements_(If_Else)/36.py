# Q36. School Result  
#       Marks 90–100 → Grade A  
#       Marks 60–89 → Grade B  
#       Marks 35–59 → Grade C  
#       Marks 35 se kam → Fail

marks=int(input("Enter the marks = "))
if marks > 100:
    print("Enter marks out of 100")
elif 90 <= marks <= 100:
    print("Grade A")
elif 60 <= marks < 90:
    print("Grade B")
elif 35 <= marks < 60:
    print("Grade C")
else:
    print("Fail")
## 25. Calculate electricity bill based on units (simple slabs).
units=int(input("Please Enter the units = "))
bill=0
if units < 0:
    print("Invalid units")
elif 0 <= units <= 100:
    bill=units*5
    print("Electricity Bill =",bill)
elif 101 <= units <= 200:
    bill=units*7
    print("Electricity Bill =",bill)
elif units < 0:
    print("Invalid units")
else:
    bill=units*10
    print("Electricity Bill =",bill)
    

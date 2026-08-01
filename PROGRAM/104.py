## 104. Check whether a year is a leap year.
year=int(input("Please enter the year = "))
if (year % 4 == 0 and year % 100 != 0) or year % 400==0:
    print("This is a leap year",year)
else:
    print("This is a not leap year",year)
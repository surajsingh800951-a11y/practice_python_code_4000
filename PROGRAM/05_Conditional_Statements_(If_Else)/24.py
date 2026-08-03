## 24. Check whether a year is a century year.
year=int(input("Enter the year = "))
if year % 100 == 0:
    print("This is a Century Year")
else:
    print("This is not a century Year")
    
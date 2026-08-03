## 17. Check whether a person is a child, teenager, adult, or senior citizen.
age=int(input("Enter your Age = "))
if age < 0:
    print("Invalid Age")
elif 0 <= age <= 12:
    print("Child")
elif 13 <= age < 20:
    print("Teenager")
elif 20 <= age < 60:
    print("Adult")
else:
    print("Senior Citizen")

## 16. Calculate grade based on marks.
marks=int(input("Enter your marks = "))
if 90 <= marks <= 100:
    print("Grade = A")
elif 80 <= marks < 90:
    print("Grade = B")
elif 70 <= marks < 80:
    print("Grade = C")
elif 60 <= marks < 70:
    print("Grade = D")
else:
    print("Grade = F")

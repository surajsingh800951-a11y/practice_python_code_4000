# 30. Print numbers from 1 to 100 divisible by 3 but not by 5.
for i in range(1,101):
    if i % 3 ==0 and i % 5 !=0:
        print("Divisible by 3 but not by 5 =",i)
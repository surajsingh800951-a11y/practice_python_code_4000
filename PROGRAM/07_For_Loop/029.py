# 29. Print numbers from 1 to 100 divisible by 2 but not by 3.
for i in range(1,101):
    if i % 2 ==0 and i % 3 !=0:
        print("Divisible by 2 but not by 3 =",i)
# 47. Take 10 numbers and count positive, negative, and zero values.
n_v=0
p_v=0
z_v=0
for i in range(10):
    num=int(input("Enter a number = "))
    if num > 0:
        p_v+=1
    elif num < 0:
        n_v+=1
    else:
        z_v+=1
print(n_v,"Negative number")
print(p_v,"Positive number")
print(z_v,"Zero number")

num=0
num1=1234
while num1>0:
    num = num * 10 + num1 % 10
    num1= int(num1 / 10)
print(num)
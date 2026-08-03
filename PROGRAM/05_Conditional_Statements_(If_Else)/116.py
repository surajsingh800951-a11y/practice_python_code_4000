## 116. Create a simple calculator (+, -, *, /).
num1=int(input("Enter the first number = "))
opr=input("Please select an operator ( + , - , * , / , % ) = ")
num2=int(input("Enter the second number = "))
if opr == '+' :
    print("Addition =",num1+num2)
elif opr == '-':
    print("Subtraction =",num1-num2)
elif opr == '*':
    print("Multiplication =",num1*num2)
elif opr == '%':
    if num2 != 0:
        print("Modulus =",num1%num2)
    else:
        print("Cannot divide by zero")
elif opr == '/':
    if num2 != 0:
        print("Division =",num1/num2)
    else:
        print("Cannot divide by zero")
else:
    print("Please enter the Correct Operator")
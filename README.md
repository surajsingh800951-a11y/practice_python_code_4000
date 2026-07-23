# 🐍 Python Practice Questions

😊 Welcome to my Python Practice Repository.

👨‍💻 Here I upload Python programs while learning Python from basic to advanced 🎯.

## 1. Create a variable name and store your name in it, then print it.
```python
name="Suraj Singh"
print(name)
```
## 2. Store 10 and 20 in two variables a and b, then print their sum.
```python
a=10 
b=20
sum=a+b
print("Sum two number =",sum)
```
## 3 .Create a variable age and store your age, then print it.
```python
age=20
print("age =",age)
```
## 4. Create an integer variable and print its data type.
```python
num=20
print(type(num))
```
## 5. Create a string variable and print its data type.
```python
name="Suraj Singh"
print(type(name))
```
## 6. Create a float variable and print its data type.
```python
num=2.25
print(type(num))
```
## 7. Create a boolean variable and print its data type.
```python
old=False
print(type(old))
```
## 8. Take two numbers from the user and find their addition.
```python
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
add=a+b
print("Sum two number = ",add)
```
## 9. Take a number from the user and find its square.
```python
num=int(input("Enter the number = "))
square=num**2 
print("Square = ",square)
```
## 10. Take two numbers and find their subtraction.
```python
num1=int(input("Enter the first number = "))
num2=int(input("Enter the Second number = "))
sub=num1-num2
print("Subtraction = ",sub)
```
## 11. Take two numbers and find their multiplication.
```python
num1=int(input("Enter the first number = "))
num2=int(input("Enter the second number = "))
mul=num1*num2
print("Multiplication = ",mul)
```
## 12.Take two numbers and find their division.
```python
num1=int(input("Enter the first number = "))
num2=int(input("Enter the second number = "))
div=num1/num2
print("Division = ",(div))
```
## 13. Store your name and age in variables and print a sentence.
```python
name="Suraj Singh"
age=22
print("My name is",name,"\nI am",age,"years old")
#print(f"My name is {name}\nI am {age} years old") # f = formatted string isase hum variable ki value sidhe string ke andar  likh sakte hai
```
## 14. Convert an integer into a float.
```python
num=int(input("Enter the integer number = "))
print(float(num))
```
## 15. Convert a float into an integer.
```python
num=float(input("Enter the float number = "))
print(num)
print(int(num))
```
## 16. Convert a float into an integer.
```python
num=float(input("Enter the float number = "))
print(num)
print(int(num))
```
## 17. Check whether a number is even or odd.
```python
num=int(input("Enter the number = "))
if num % 2 ==0:
    print("Even Number")
else:
    print("Odd Number")
```
## 18. Take three numbers and find their average.
```python
num1=int(input("Enterr the first number = " ))
num2=int(input("Enter the second number = "))
num3=int(input("Enter the third number = "))
ave=(num1+num2+num3)/3
print("Three Number average =",ave)
```
## 19. Convert Celsius temperature into Fahrenheit.
```python
c=int(input("Enter the celsius value = "))
f=(c*9/5)+32
print("Fahrenheit =",f)
```
# Tuple Question (20 -- 29)

## 20. Create a tuple of five numbers.
```python
t1 = (10, 20, 30, 10, 50)
print(t1)
```
## 21. Print the first and last elements.
```python
tupple = (10, 20, 30, 40, 50)
print("First element =", tupple[0])
print("Last element =", tupple[-1])
```
## 22. Find the length of a tuple.
```python
tuple= (30, 80, 40, 10, 30)
print("Length =", len(tuple))
```
## 23. Count how many times 10 appears.
```python
tupple= (10, 20, 30, 10, 50,40,45,77,8,34,67)
num=int(input("Enter the number "))
print("appears =", tupple.count(num), "times")
```
## 24. Find the index of 30.
```python 
tupple = (14, 80, 30, 10, 50)
print("Index number=", tupple.index(30))
```
## 25. Concatenate two tuples.
```python
tupple_1= (13, 27, 30, 18, 50,67,34,9)
tupple_2 = (60,45,67,34,54,70)
tupple_3 = tupple_1 + tupple_2
print("combine tupple =", tupple_3)
```
## 26. Repeat a tuple three times.
```python
tupple=(12,23)
print("Reapet tuple",tupple*5)
```
## 27. Convert a list to a tuple.
```python
listt=[10,20,30,34,56,23,45]
tupple=tuple(list)
print(tupple)
```
## 28. Convert a tuple to a list and add a new element.
```python
tupple= (10, 20, 30)
listt=list(tupple)
listt.append(40)
print(listt)
```
## 29. Find the maximum, minimum, and sum of a tuple.
```python
tupple=(10,20,30,40,50)
print("maximum =",max(tupple))
print("nminimum =",min(tupple))
print("Sum =",sum(tupple))
```
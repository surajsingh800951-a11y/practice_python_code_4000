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
# List Question (30 --64 )

# 30. Create a list of 5 integers and print it.
```python
listt=[10,20,30,40,50]
print("Print five integers number ",listt)
```
## 31. Create a list of 5 names and print it.
```python
name=["Suraj","Sangram","Shivam","Dileep","Prince"]
print("Print five name ",name)
```
## 32. Print the first element of a list.
```python
listt=[12,32,45,65,76,76,4,54,34,66]
#index[0, 1, 2,  3, 4,5, 6, 7, 8, 9]
print("Print first element ",listt[0])
```
## 34. Print the middle element of a list.
```python
# listt=[12,32,45,65,76,6,14,54,34,66]
# #index[0, 1, 2,  3, 4,5, 6, 7, 8, 9]
# n=len(listt)
# if n%2==0:
#     mid=n//2  #floor division
#     print("Print middle element ",listt[mid-1], listt[mid])
# else:
#     mid=n//2
#     print("Print middle element ",listt[mid])

listt=[12,32,45,65,76,6,14,54,34,66]
#index[0, 1, 2,  3, 4,5, 6, 7, 8, 9]
n=len(listt)//2
print("Print middle element ",listt[n])
```
## 35. Print the length of a list using len().
```python
listt=[12,32,45,65,76,76,4,54,34,66]
print("lenght ",len(listt))
```
## 36. Add an element to the end of a list using append().
```python
listt=[12,32,45,65,76,76,4,54,34]
listt.append(9)
print(listt)
```
## 37. Insert an element at index 2 using insert().
```python
listt=[12,34,54,34,34,54]
listt.insert(2,40)
print(listt)
```
## 38. Add multiple elements to a list using extend().
```python
listt1=[12,32,45,65,7,78,65,45,54]
listt1.extend([12,22,32,43,23])
print(listt1)
```
## 39. Concatenate two lists using the + operator.
```python
listt1=[12,32,34,22,66]
listt2=[12,3,75,78,54,7]
combine=listt1+listt2
print("Concatenate two list ",combine)
```
## 40. Remove an element by value using remove().
```python
listt=[12,3,42,43,67,2,75,23]
listt.remove(12)
print(listt)
```
## 41. Remove the last element using pop().
```python
listt=[12,23,42,55,67,2,5,11]
listt.pop() 
print(listt)
```
## 42. Remove an element at a specific index using pop(index).
```python
listt=[12,32,45,64,23,78,34]
listt.pop(2)
print(listt)
```
## 43. Delete an element using del.
```python
listt=[12,32,42,54,67,46,23]
del listt[:]
print(listt)
```
## 44. Clear all elements from a list using clear().
```python
listt=[12,32,53,56,75,87,98,35,67,98]
listt.clear()
print(listt)
```
## 45. Count how many times an element appears using count().
```python 
listt=[12,32,44,23,5,3,23,12,5,23]
n=int(input("please enter value "))
print("appears",listt.count(n),"times")
```
## 46. Find the index of an element using index().
```python
listt=[12,43,5,54,65,34,21,76,12,65]
index=listt.index(12)
print("index =",index)
```
## 47. Copy one list into another using copy().
```python
list1=[12,34,2,44,3,32,3,4]
list2=list1.copy()
print(list2)
```
## 48. Reverse a list using reverse().
```python
listt=[12,43,5,54,65,34]
listt.reverse()
print(listt)
```
## 49. Sort a list in ascending order using sort().
```python
listt=[12,23,4,2,3,43,45,23,23,4]
listt.sort()
print(listt)
```
## 50. Check whether an element exists in a list.
```python
listt=[12,33,43,56,34,65,5]
num=10
#num=int(input("Enter the value ")) # User 
if num in listt:
    print("Element exists in the list")
else:
    print("Element does not exist in the list") 
 ```   
## 51. Replace the third element with a new value.
```python
listt=[12,23,43,56,12,45,23,53,43]
listt[2]=20
print(listt)
```
## 52. Print all elements using a for loop.
```python
listt=[12,3,3,53,64,67,46,3,4,3,54]
for i in listt:
    print(i)
```
## 53. Find the largest element in a list.
```python
larg=0
listt=[12,32,5,3,23,56,2,7,90,5]
for i in listt :
    if i > larg :
        larg=i
print("Largest Element",larg)
```
## 54. Find the smallest element in a list.
```python
listt=[12,32,5,3,23,56,2,7,90,5]
smal=listt[0]
for i in listt :
    if i < smal :
        smal=i
print("Smallest Element",smal)
```
## 55. Find the sum of all elements.
```python
listt=[12,34,1,42,53,54,6,78,5,65]
sum=0
for i in  listt:
    sum+=i # sum=sum+i
print("Sum all elements",sum)
```
## 56. Find the average of all elements.
```python
listt=[12,34,1,42,53,54,6,78,5,65]
n=0
sum=0
for i in  listt:
    sum+=i # sum=sum+i
    n+=1 # n=n+1
ave=sum/n
print("Average all elements",ave)    
```
## 57. Create a list of numbers from 1 to 10.
```python
listt=[]
for i in range(1,11):
     listt.append(i)
print(listt)
```
## 58. Print only the even numbers from a list.
```python
listt=[12,23,56,58,52,36,68,59,74,25,36,59,54,35]
print("Only Even number")
for i in listt:
    if i % 2 == 0:
        print(i)
```
## 59. Print only the odd numbers from a list.
```python
listt=[12,23,56,58,52,36,68,59,74,25,36,59,54,35]
print("Only Odd number")
for i in listt:
    if i % 2 != 0:
        print(i)
```
## 60. Create a copy of a list without using copy().
```python
listt1=[]
listt2=[14,15,19,52,56,45,54]
for i in listt2:
    listt1.append(i)
print("Copy list",listt1)
```
## 61. Sort a list in descending order.
```python
listt=[12,34,54,65,67,32,54,65,23,54,34,43,3]
listt.sort(reverse=True)
print(listt)
```
## 62. Reverse a list without using reverse().
```python
listt=[12,45,48,45,35,65,89,78,1,5]
listt=listt[::-1] # slicing
print(listt)
```
## 63. Remove duplicate elements from a list.
```python
listt1=[1,34,23,65,67,34,1,34,65,23,45,98,23]
listt2=[]
for i in listt1:
    if i not in listt2:
        listt2.append(i)
print(listt2)
```
## 64. Merge three lists into one list.
```python
listt1=[14,25,35]
listt2=[12,56]
listt3=[15,2,36]
listt=listt1+listt2+listt3
print("Three list merge ",listt)
```

    




        




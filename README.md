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
# Type Conversion (65 -- 75)
     
## 65. Write a program to add an integer and a float and display the result.
```python
num=10 # int
f_num=4.5 # float
result=num+f_num
print(result)
```
## 66. Write a program to divide two integers and print the data type of the result.
```python
num=10
b=5
div=num/b
print(type(div))
```
## 67. Write a program to add a boolean value and an integer.
```python
is_bool=False # boolean # true =1, false=0
num=10 # integer
add=is_bool+num
print(add)
```
## 68. Write a program to multiply an integer with a float.
```python
is_num=10
is_float=10.5
is_multiply=is_num*is_float
print(is_multiply)
```
## 69. Write a program to add two numbers of different data types (int and float).
```python
num=10
f_num=10.5  #float
add=num+f_num
print(add)
```
## 70. Write a program to divide two integers and print the data type of the result.
```python
num=10 
num1=2
divide=num/num1
print(type(divide))
```
## 71.  Write a program to compare an integer and a float using the == operator.
```python
num=12
f_num=10.5
result=num == f_num
print(result)
```
## 72. Write a program to subtract a float from an integer.
```python
num=10
f_num=10.5
subtract=num-f_num
print(subtract)
```
## 73. Write a program to perform arithmetic operations between True and False.
```python
a=False
b=True
add=a+b
sub=a-b
mul=a*b
div=a/b
equal=a==b
print("Addition",add)
print("Subtraction",sub)
print("Division",div)
print("Multiplication",mul)
print("Equal",equal)
```
## 74. Write a program to add a float and a boolean.
```python
f_num=20.5 # float number
b_num=True # boolien Value
add=f_num+b_num
print(add)
```
## 75. Write a program to print the data type of the result after adding an int and a float.
```python
num=12
f_num=20.5 # float value 
result=num+f_num
print("Data type of the result",type(result))

"""num=int(input("Enter the integer value "))
f_num=float(input("Enter the float value "))       #  User 
result=num+f_num
print("Data type of the result",type(result))"""
```
# Type Casting (76 -- 95)

## 76. Write a program to convert a string "100" into an integer.
```python
num="100" # string value 
#print(type(num)) # Output <class 'str'>
print(int(num)) #  Output: 100 (integer)
print(type(int(num))) # Output <class 'int'>
```
## 77. Write a program to convert a string "25.75" into a float.
```python
f_num="25.75" # float value
print(type(f_num)) # Output <class 'str'>
print(float(f_num)) # Output 25.75 float
print(type(float(f_num))) # Output <class 'float'>
```
## 78. Write a program to convert an integer into a string.
```python
num=18 # integer value
print(type(num)) # Output <class 'int'>
print(str(num)) # String Value 18
print(type(str(num))) # Output <class 'str'>
```
## 79. Write a program to convert a float into an integer.
```python
f_num=20.2 # float
print(type(f_num)) # Output <class 'float'>
print(int(f_num)) # 20 integer
print(type(int(f_num))) # Output <class 'int'>
```
## 80. Write a program to convert an integer into a float.
```python
num=26 # integer
print(type(num)) # Output <class 'int'>
print(float(num)) # 26.0 ( Float )
print(type(float(num))) # Output <class 'float'>
```
## 81. Write a program to convert a list into a tuple.
```python
listt=[12,34,2,67,85,89] 
tupple=tuple(listt)
print(tupple)  # Output (12, 34, 2, 67, 85, 89)
print(type(tupple)) # Output <class 'tuple'>
```
## 82. Write a program to convert a tuple into a list.
```python
tupple=(12,34,54,67,86,5)
print(type(tupple)) # Output <class 'tuple'>
listt=list(tupple)
print(listt)  # Output [12, 34, 54, 67, 86, 5]
print(type(listt)) #Output  <class 'list'>
```
## 83. Write a program to convert a list with duplicate elements into a set.
```python
listt=[12,23,12,45,12,54,12]
print(type(listt)) # Output <class 'list'>
sett=set(listt)
print(sett) # Output {12, 45, 54, 23}
print(type(sett)) # Output <class 'set'>
```
## 84. Write a program to convert a string into a list of characters.
```python
my_string="Suraj Singh"
print(type(my_string)) # Output <class 'str'>
my_list=list(my_string)
print(my_list) # Output ['S', 'u', 'r', 'a', 'j', ' ', 'S', 'i', 'n', 'g', 'h']
print(type(my_list)) # Output  <class 'list'>
```
## 85. Write a program to convert a list into a set.
```python
my_list=[12,45,23,54]
print(type(my_list)) # Output <class 'list'>
my_set=set(my_list)
print(my_set) # Output  {12, 45, 54, 23}
print(type(my_set)) # Output <class 'set'>
```
## 86. Write a program to convert a set into a list.
```python 
my_set={ 12,34,56,23,45} 
print(type(my_set))  # Output <class 'set'>
my_list=list(my_set) 
print(my_list) # Output  [34, 23, 56, 12, 45]
print(type(my_list)) # Output  <class 'list'>
```
## 87. Write a program to convert a tuple into a set.
```python
my_tuple=(12,34,23,65,78,56)
print(type(my_tuple)) # Output <class 'tuple'>
my_set=set(my_tuple)
print(my_set)   # Output   {65, 34, 12, 78, 23, 56}
print(type(my_set)) # Output <class 'set'>
```
## 88. Write a program to convert the integer 0 into a boolean.
```python
num=0
print(type(num)) # Output <class 'int'>
my_bool=bool(num)
print(my_bool) # Output  False
print(type(my_bool)) # Output <class 'bool'>
```
## 89. Write a program to convert the integer 1 into a boolean.
```python
num=1
print(type(num)) # Output  <class 'int'>

my_bool=bool(num) 
print(my_bool)   # Output  True
print(type(my_bool)) # Output  <class 'bool'>
```
## 90. Write a program to convert an empty string into a boolean.
```python
my_str="" # empty string
print(type(my_str))  # Output <class 'str'>
my_bool=bool(my_str) 
print(my_bool)  # Output True
print(type(my_bool)) # Output <class 'bool'>
```
## 91. Write a program to convert a non-empty string into a boolean.
```python
my_string="S" 
print(type(my_string)) # Output <class 'str'>
my_bool=bool(my_string) 
print(my_bool) # Output True
print(type(my_bool)) # Output <class 'bool'>
```
## 92. Write a program to take a number as a string from the user and convert it into an integer.
```python
my_string=input("Enter a number ")
print(type(my_string)) # Output <class 'str'>
my_num=int(my_string) 
print(my_num) # Output 123
print(type(my_num)) # Output <class 'int'>
```
## 93. Write a program to take a decimal number as input and convert it into an integer.
```python
num=float(input("Enter the number "))
print(type(num)) # Output <class 'float'>
my_int=int(num)
print(my_int) # Output 12
print(type(my_int)) # Output <class 'int'>
```
## 94. Write a program to convert the string "True" into a boolean and observe the output.
```python
my_str="True"
print(type(my_str)) # Output <class 'str'>
my_bool=bool(my_str)
print(my_bool) # Output True
print(type(my_bool)) # Output <class 'bool'>
```
## 95. Write a program to convert a tuple containing duplicate values into a set. --
```python
my_tuple=(12,34,56,2,4,22,5,2,2,2,34,54,54)
print(type(my_tuple)) # Output <class 'tuple'>
my_set=set(my_tuple)
print(my_set) # Output {34, 2, 4, 5, 12, 22, 54, 56}
print(type(my_set)) # Output <class 'set'>
```
## if / else (96 -- 125)

## 96. Check whether a number is positive or negative
```python
num=int(input("Enter the number "))
if num > 0 :
    print("This number is Positive")
elif num < 0:
    print("This number is Negative")
else:
    print("This number is Zero")    
```
## 97. Check whether a number is even or odd.
```python
num=int(input("Enter the number "))
if num % 2 == 0:
    print("This number is Even")
else:
    print("This number is Odd")
```
## 98. Check whether a person is eligible to vote (age ≥ 18).
```python
age=int(input("Enter the age "))
if age >= 18:
    print("This person is eligible to vote")
else:
    print("This person is not eligible to vote")
```
## 99. Find the greater of two numbers.
```pyhon
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
if num1 > num2 :
    print("First number is Greater")
else:
    print("Second number is Greater")
```
## 100. Find the smaller of two numbers.
```python
num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))
if num1 < num2 :
    print("First number is Smaller")
else:
    print("Second number is Smaller")
```
## 101. Check whether a number is divisible by 5.
```python
num=int(input("Enter the number "))
if num % 5 == 0:
    print("This number is divisiable by 5")
else:
    print("This number is not divisiable by 5")
```
## 102. Check whether a number is divisible by 3 and 5.
```python
num=int(input("Enter the number "))
# if num % 5 ==0:
#     if num % 3 == 0:
#         print("This number is divisible by  3 and 5")
#     else:
#          print("This number is not divisible 3 and 5")
# else:
#     print("This number is not divisible 3 and 5")
    
    
    # Logical Operators --- and ---
    
if num % 5 ==0 and num % 3 == 0:
    print("This number is divisible by  3 and 5")
else:
    print("This number is not divisible 3 and 5")
```
## 103. Check whether a character is a vowel or consonant.
```python
char=input("Enter the any character ")
if char=='a':
    print("Character is vowel = ",char)
elif char=='i':
     print("Character is vowel = ",char)
elif char =='o':
     print("Character is vowel = ",char) 
elif char=='u':
     print("Character is vowel = ",char) 
elif char == 'e':
    print("Character is a vowel = ",char)
else:
     print("Character is a consonant = ",char)
```
## 104. Check whether a year is a leap year.
```python
year=int(input("Please enter the year = "))
if (year % 4 == 0 and year % 100 != 0) or year % 400==0:
    print("This is a leap year",year)
else:
    print("This is a not leap year",year)
```
## 105. Check whether a number is a multiple of 10.
```python
num=int(input("Enter a number "))
if num % 10 == 0:
    print("This number is a multiple of 10 =",num)
else:
    print("This number is not a multiple of 10 =",num)
```
## 106. Find the largest of three numbers.
```python
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if a < b :
    if b < c:
        print("Largest number =",c)
    else:
        print("Largest number =",b)
elif a < c:
    print("Largest number =",c)
else:
    print("Largest number =",a)
```
## 107. Find the smallest of three numbers.
```python
a=int(input("Enter the first number = "))
b=int(input("Enter the second number = "))
c=int(input("Enter the third number = "))
if a < b:
    if a < c:
        print("Smallest number =",a)
    else:
        print("Smallest number =",c)
elif b < c :
    print("Smallest number =",b)
else:
    print("Smallest number =",c)
```
## 108. Check whether a number is a two-digit number.
```python
num=int(input("Enter the number = "))
if num >= 10 and num <= 99:    # if 10 <= num <= 99: Same logic
    print("This number is two digit = ",num) 
else:
    print("This number is not two digit = ",num)
```
## 109. Check whether a number is a three-digit number. 
```python
num=int(input("Enter the number = "))  # only  Positive number
if 100 <= num  <= 999:
    print("This number is three digit = ",num) 
else:
    print("This number is not three digit = ",num) 
```
## 110. Check whether a number is divisible by both 2 and 7.
```python
num=int(input("Enter the number = "))
if num % 2 == 0 and num % 7 == 0:
    print("This number is divisible by both 2 and 7 =",num)
else:
    print("This number is not divisible by both 2 and 7 =",num)
```
## 111. Calculate grade based on marks.
```python
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
```
## 112. Check whether a person is a child, teenager, adult, or senior citizen.
```python
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
```
## 113. Check whether a character is uppercase or lowercase.
```python
char=input("Enter the character = ")
if len(char) != 1:
    print("Please enter only one character")
elif 'a' <= char <= 'z':
    print("This character is lowercase =",char)
elif  'A' <= char <= 'Z':
    print("This character is uppercase =",char)
else:
    print("Invalid character") 
```
## 114. Check whether a number is divisible by 2, 3, both, or neither.
```python
num=int(input("Enter the number = "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3 =",num)
elif num % 2 == 0:
    print("Divisible by 2 only =",num)
elif num % 3 == 0:
    print("Divisible by 3 only =",num)
else:
    print("Divisible by neither 2 nor 3 =",num)
```
## 115. Find whether the entered alphabet is a vowel (using multiple conditions).
```python
char=input("Enter the character = ")
if char =='a' or char == 'u' or char == 'i' or char == 'o' or char == 'e':
    print("This Character is vowel")
else:
    print("This Character is not vowel")
```
## 116. Create a simple calculator (+, -, *, /).
```python
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
```

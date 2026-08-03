## 20. Write a program to convert a tuple containing duplicate values into a set. --
my_tuple=(12,34,56,2,4,22,5,2,2,2,34,54,54)
print(type(my_tuple)) # Output <class 'tuple'>
my_set=set(my_tuple)
print(my_set) # Output {34, 2, 4, 5, 12, 22, 54, 56}
print(type(my_set)) # Output <class 'set'>
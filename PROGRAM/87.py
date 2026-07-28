## 87. Write a program to convert a tuple into a set.
my_tuple=(12,34,23,65,78,56)
print(type(my_tuple)) # Output <class 'tuple'>
my_set=set(my_tuple)
print(my_set)   # Output   {65, 34, 12, 78, 23, 56}
print(type(my_set)) # Output <class 'set'>
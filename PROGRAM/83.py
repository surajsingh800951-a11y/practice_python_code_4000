## 83. Write a program to convert a list with duplicate elements into a set.
listt=[12,23,12,45,12,54,12]
print(type(listt)) # Output <class 'list'>
sett=set(listt)
print(sett) # Output {12, 45, 54, 23}
print(type(sett)) # Output <class 'set'>

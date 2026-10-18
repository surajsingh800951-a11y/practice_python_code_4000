# 10. Write a program to create a shallow copy of a list of library books using copy().
library_books = [
    ["Python Basics", "Suraj"],
    ["C Programming", "Rahul"],
    ["DBMS", "Amit"],
    ["Computer Networks", "Shivam"]
]

l_b_copy=library_books.copy()

print("Original List =",library_books)
print("Shallow Copy =",l_b_copy)
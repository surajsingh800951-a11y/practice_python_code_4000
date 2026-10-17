# 6. Write a program to create a shallow copy of a list of movie ratings using copy().
movie_ratings = [
    ["KGF", 9],
    ["RRR", 8],
    ["Pushpa", 9]
]

m_t_copy=movie_ratings.copy()

print("Original Listt =",movie_ratings)
print("Shallow Copy =",m_t_copy)
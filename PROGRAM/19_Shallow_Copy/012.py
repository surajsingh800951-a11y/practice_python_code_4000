# 12. Write a program to create a shallow copy of a list of social media followers using copy().
social_media_followers = [
    ["Suraj", 1200],
    ["Rahul", 850],
    ["Amit", 1500],
    ["Shivam", 950]
]

s_m_f_copy=social_media_followers.copy()

s_m_f_copy[2][0]="Deelip"

print("Oringinal List =",social_media_followers)
print("Shallow Copy",s_m_f_copy)
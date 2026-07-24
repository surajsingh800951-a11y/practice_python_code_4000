## 34. Print the middle element of a list.
# listt=[12,32,45,65,76,6,14,54,34,66]
# #index[0, 1, 2,  3, 4,5, 6, 7, 8, 9]
# n=len(listt)
# if n%2==0:
#     mid=n//2  #floor division
#     print("middle element ",listt[mid-1], listt[mid])
# else:
#     mid=n//2
#     print("middle element ",listt[mid])

listt=[12,32,45,65,76,6,14,54,34,66]
#index[0, 1, 2,  3, 4,5, 6, 7, 8, 9]
n=len(listt)//2
print("middle element ",listt[n])
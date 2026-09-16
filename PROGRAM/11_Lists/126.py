# 126. Write a program to create a nested list representing employee data organized in groups.
# employee_data=[
#     [
#         ["Suraj",25,3000,"IT"],
#         ["Shivam",26,4000,"IT"]
#     ],
#     [
#     ["Raj",25,3000,"IT"],
#     ["Surya",26,4000,"IT"]
#     ]
# ]
# print(employee_data[1])


employee_data=[ 
    [
        ["Suraj",25,3000,"IT"],
        ["Shivam",26,4000,"IT"] 
    ],
    [
    ["Raj",25,3000,"IT"],
    ["Surya",26,4000,"IT"]  
    ]
]
for i in employee_data:
    for j in i:
        for k in j:
           print(k)
           
        
        
        
        
        
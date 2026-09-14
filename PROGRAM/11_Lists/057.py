# 57. Demonstrate the difference between append() and extend().
listt=[23,25,67,82]
listt.append([2,3,4])  # append() → list ko ek item ki tarah add karta hai.
print(listt)

listt2=[23,25,67,82]
listt2.extend([2,3,4])  # extend() → list ke elements ko alag-alag add karta hai.
print(listt2)
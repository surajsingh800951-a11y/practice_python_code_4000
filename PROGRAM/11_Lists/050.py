# 50. Check whether 50 exists in a list.
listt=[21,56,48,65,75,32,5,58,69]
#print(50 in listt)                # Using Membership Operator

check=False
for i in range(len(listt)):    # Using for loop 
    if listt[i] == 50:
        print("50 exists in a list")
        check=True
        break
if check == False:
    print("50 does not exists in the list")
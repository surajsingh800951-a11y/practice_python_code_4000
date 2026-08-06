# Q34. Restaurant Bill  
#       Agar bill ₹1000 ya usse zyada hai → 20% discount.  
#       Agar bill ₹500–999 hai → 10% discount.  
#       Agar bill ₹500 se kam hai → Koi discount nahi.
dis=0
bill=int(input("Please enter bill = "))
if bill <= 0:
    print("Please enter a valid bill")
elif bill >= 1000:
    dis=bill*20/100
    print("20% discount =",dis)
elif bill >=500:
    dis=bill*10/100
    print("10% discount =",dis)
else:
    print("Koi discount nahi")
  
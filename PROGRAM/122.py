## 122. Check whether a triangle is valid using three angles.
angle1=int(input("Enter the first Angle = "))
angle2=int(input("Enter the second Angle = "))
angle3=int(input("Enter the third Angle = "))
add=angle1+angle2+angle3
if angle1 > 0 and angle2 > 0 and angle3 > 0:
    if add == 180:
        print("This triangle is valid")
    else:
        print("This triangle is not valid")
else:
     print("This triangle is not valid")
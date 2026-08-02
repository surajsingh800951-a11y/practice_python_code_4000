## 123. Find the type of triangle (Equilateral, Isosceles, Scalene).
sides1=int(input("Enter the first sides = "))
sides2=int(input("Enter the second sides = "))
sides3=int(input("Enter the third sides = "))
if sides1+sides2 > sides3 and sides1+sides3 > sides2 and sides2+sides3 > sides1:
    if sides1 == sides2 == sides3 :
        print("Equilateral Triangle")
    elif sides1 == sides2 or sides2 == sides3 or sides1 == sides3 :
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")
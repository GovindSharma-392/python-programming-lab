 #How to calculate body mass index on Python?


height = float(input("enter height (m):"))
weight = int(input("enter weight (kg):"))
 
index  = weight/(height*height)
 
if index <=18:
    print("\n underweight")
elif index > 18 and index <=25 :
    print("\n overweight ")
elif index > 25 and index <=30:
    print("\n obese")
elif index > 30:
    print("\n severely obese ")
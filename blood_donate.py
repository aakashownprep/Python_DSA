# requirement
# 1)hemoglobin==>14 2)age==>18+ 3)weight==>60+

age=int(input("Enter your age:"))
gender=input("enter your gender:")
weight=int(input("Enter your weight:"))
hemoglobin=float(input("enter your hemoglobin:"))

if age>=18:
    if gender=="male":
      if weight>=60:
        if hemoglobin>=14:
            print("you are eligible for blood donation")
        else:
            print("Hemoglobin low level not eligible")
    else:
        print("Weight not matched")
    
elif gender=="female":
    if weight>=45:
        if hemoglobin>=14:
            print("you are eligible for blood donation")
        else:
            print("Hemoglobin low level not eligible")
    else:
        print("Weight not matched")

else:
    print("age is not matched")                    
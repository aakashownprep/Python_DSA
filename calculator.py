def addition():
    a=int(input("enter 1st value for addition:"))
    b=int(input("enter 2nd value for addition:"))
    c=a+b
    print("Addition = ",c)

def substraction():
    a=int(input("enter 1st value for substraction:"))
    b=int(input("enter 2nd value for substraction:"))
    c=a-b
    print("substraction = ",c)   

def multiplication():
    a=int(input("enter 1st value for multiplication:"))
    b=int(input("enter 2nd value for multiplication:"))
    c=a*b
    print("multiplication = ",c)   

print("1.+")
print("2.-")
print("3.*")
choice=input("enter your choice:")
if (choice=="+"):
    addition()
if (choice=="-"):
    substraction
if (choice=="*"):
    multiplication()    
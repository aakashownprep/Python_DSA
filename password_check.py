password="Mypasswor"
print(len(password))
if len(password) >= 10 and any(x.isdigit() for x in password) and any(x.isupper() for x in password) and any(x in "!@#$%&*^" for x in password):
    print("Strong password")
else:
   print("Weak password")

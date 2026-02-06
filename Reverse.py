#123==>321
# to create reverse number example

number=int(input("Enetr any number :"))
reverse_number=0

while number > 0:
    digit=number % 10
    reverse_number=reverse_number*10+digit
    number //=10
print(reverse_number)    

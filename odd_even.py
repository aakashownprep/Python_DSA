a=int(input("Enter starting range :"))
b=int(input("Enter ending range: "))
for i in range(a,b):
    if i % 2==0:
        print("even number :",i)
    if i % 2 != 0: # != not equal
        print("odd number : ",i)    
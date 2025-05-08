
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
n= int(input("enter a option:"))
a=int(input("enter number a:"))
b=int(input("enter number b:"))
if n==1:
    print("addition=",a+b)
elif n==2:
    print("subtraction=",a-b)
elif n==3:
    print("multiplication=",a*b)
elif n==4:
    print("division=",a/b)
else:
    print("select a corect option!!!")
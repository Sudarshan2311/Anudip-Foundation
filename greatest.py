a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
if a>b and a>c:
    print("a is greatest")
elif b>c and b>a:
    print("b is greatest")
else:
    print("c is greatest")
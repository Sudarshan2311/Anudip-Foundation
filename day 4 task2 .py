'''2.  A toy vendor supplies three types of toys: 
Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. 
The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. 
On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, 
and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. 
Assume that the numeric codes 1,2 and 3 are used for b'''


print("select any 1 option:")
print("type 1 for Battery Based Toys: ")
print("type 1 for Key-based Toys: ")
print("type 1 for Electrical Charging Based Toys: ")
option=int(input("type any one option"))
amount=float(input("enter the total amount:"))

if option==1:
    if amount>1000:
        discount=amount*10/100
        print("final cost is :",amount-discount)
    else:
        print("final amount is:",amount)
elif option ==2:
    if amount>100:
        discount=amount*5/100
        print("final cost is :",amount-discount)
    else:
        print("final amount is:",amount)
elif option ==500:
    if amount>100:
        discount=amount*10/100
        print("final cost is :",amount-discount)
    else:
        print("final amount is:",amount)
else:
    print("wrong output slected")  
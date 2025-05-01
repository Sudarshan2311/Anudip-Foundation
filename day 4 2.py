''' Write a program that prompts the user to enter the quantity of items they want
to purchase. Each unit costs $100. If the total cost exceeds $1000, a 10%
discount will be applied. The program should then calculate and display the
final total cost after considering any discount.'''


items=int(input("enter the total numbers of items:"))
cost=100*items

if cost>1000:
    discount=cost*10/100
    print("final price after discount:",cost-discount)
else:
    print("final cost:",cost)
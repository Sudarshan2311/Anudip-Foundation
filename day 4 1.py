'''A company decided to give a bonus of 5% to an employee if his/her year of
service is more than 5 years .Ask users for their salary and year of service and
print the net bonus amount.'''


salary=float(input("enter your salary:"))
service=int(input("enter total year of service:"))


if service>=5:
    bonus = salary*5/100
    print("your bonus is:",bonus)
else:
    print("your service is less so, no bonus!!")
'''I want to calculate the total electricity bill.
The rules are as follows: Installed load: The installed load is the maximum amount of
electricity that your home or business can use at any given time. This is measured in
kilowatts (kW). The higher your installed load, the higher your fixed charges will
be.Energy consumption: The energy consumption is the total amount of electricity that
you use in a billing period. This is measured in units (kWh). The more electricity you
consume, the higher your variable charges will be.Tariff slabs: The tariff slabs are the
different rates per unit of electricity that you are charged. There are currently 4 tariff
slabs in Bangalore:
Up to 50 units: Rs 4.75/unit
51 to 100 units: Rs 5.75/unit
101 to 200 units: Rs 7/unit
Above 200 units: Rs 8/unit
The actual electricity charges that you pay will depend on your installed load, energy
consumption, and the tariff slab that you fall into.'''

amount=0
def bill(unit):
    if unit<=50:
        amount=unit*4.75
    elif 51<unit<=100:
        amount=(50*4.75)+((unit-50)*5.75)
    elif 101<unit<=200:
        amount=(50*4.75)+(50*5.75)+((unit-100)*7)
    elif unit>200:
        amount=(50*4.75)+(50*5.75)+(100*7)+((unit-100)*8)
    else:
        print("enter correct unit")
    print("total amount is:",amount)

unit=float(input("enter total units:"))
bill(unit)
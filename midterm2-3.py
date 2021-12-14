# Auhtor: CMOB 12/14/2021

distance = input("What is the distance? (mi) ")
fuel_efficiency = input("What is the fuel efficiency? (mpg) ")
fuel_price = input("What is the price of fuel? (credits per gallon) ")

gallons = int(distance) / int(fuel_efficiency)

cost = gallons * int(fuel_price)

print("The cost for the trip will be {0} credits".format(cost))

import math

PRICE_PER_CUBIC_METER = 5.0  # eur/m^3

def calculate_water_volume_and_price(diameter, height):
    radius = diameter / 2
    liters_water = 1000 * math.pi * radius * radius * height
    cost = PRICE_PER_CUBIC_METER * liters_water / 1000
    print("You need {:.0f} liters of water to fill the pool.".format(liters_water))
    print("It will cost you {:.2f} euros.".format(cost))

def main():
    number_of_pool = int(input("Enter the number of pools:\n"))

    for i in range(number_of_pool):
        print("{:d}. pool".format(i+1))
        diameter = float(input("Enter the diameter of the pool in meters:\n"))
        height = float(input("Enter the height of the pool in meters:\n"))
        calculate_water_volume_and_price(diameter,height)
        print()

main()
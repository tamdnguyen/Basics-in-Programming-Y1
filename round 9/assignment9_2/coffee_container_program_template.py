# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius, modified by Veera Laine
# Template for Exercise 9.2 Coffee containers

from container import LiquidContainer

def main():
    # Ask the names and volumes of the containers according to the example runs and
    # create three containers: large coffee cup, small coffee cup, and coffee jug.
    line = input("Big coffee cup name and volume: ")
    data = line.split("/")
    big_coffee_cup = LiquidContainer(data[0], float(data[1]), False)

    line = input("Small coffee cup name and volume: ")
    data = line.split("/")
    small_coffee_cup = LiquidContainer(data[0], float(data[1]), False)

    line = input("Coffee jug name and volume: ")
    data = line.split("/")
    coffee_jug = LiquidContainer(data[0], float(data[1]), True)

    print("Created the following containers:")
    # Print here the statuses of the three created coffee containers
    print(big_coffee_cup)
    print(small_coffee_cup)
    print(coffee_jug)

    # Fill the format with the jug name" 
    print("\nFilling {:s}...".format(coffee_jug.get_name()))
    # Fill here the coffee jug
    coffee_jug.fill()
    print("Jug status after filling:")
    # Print here the status of the coffee jug
    print(coffee_jug)

    amount_to_be_served = float(input("\nHow many litres of coffee should be served?\n"))

    # Fill the format. Sould print "Trying to pour [amount to be served] litres from [jug name] into [big cup name] and [small cup name]"
    print("Trying to pour {:f} litres from {:s} into {:s} and {:s}".format(amount_to_be_served,
                                                                           coffee_jug.get_name(),
                                                                           big_coffee_cup.get_name(),
                                                                           small_coffee_cup.get_name())) # This should print
    
    # Pour here the coffee from the jug first to the big cup and then to small cup
    jug_to_big = coffee_jug.pour_to_another(big_coffee_cup, amount_to_be_served)
    jug_to_small = coffee_jug.pour_to_another(small_coffee_cup, amount_to_be_served)
    # Print the amounts of the coffee poured in each container, i.e., fill the format
    print("Managed to pour {:f} litres to {:s}".format(jug_to_big, big_coffee_cup.get_name()))
    print("Managed to pour {:f} litres to {:s}".format(jug_to_small, small_coffee_cup.get_name()))
  
    print("\nCup and jug statuses after pouring:")
    # Print here the statuses of the containers
    print(big_coffee_cup)
    print(small_coffee_cup)
    print(coffee_jug)

    # Check whether both cups got the same amount of coffee, i.e. fill the if clause
    if big_coffee_cup.get_liquid_volume() == small_coffee_cup.get_liquid_volume():
        print("\nBoth were happy for having the same amount of coffee and lived happily everafter.")
    else:
        # Fill the format with the name of the small cup.
        print("\nThe holder of {:s} became angry for having less coffee and flipped their coffee cup!"
              .format(small_coffee_cup.get_name()))
        
        # Flip here the small cup
        small_coffee_cup.flip()
        print("\nThey also flipped the jug!")
        # Flip here the coffee jug
        coffee_jug.flip()
        print("However, it had a lid, so the liquid stayed inside:")
        # Print here the status of the coffee jug
        print(coffee_jug)

        print("\nSo they had to force flip to the jug!")
        # Force flip here the coffee jug
        coffee_jug.force_flip()
        print("Now it's empty and no longer has a lid:")
        # Print here the status of the coffee jug
        print(coffee_jug)
        # Fill the format with the name of the big cup
        print("\nNext they got mad and nicked all the coffee they could from {:s}".format(big_coffee_cup.get_name()))

        # Pour here as much coffee as possible from the large cup to the small cup
        small_steal = big_coffee_cup.pour_to_another(small_coffee_cup, small_coffee_cup.get_total_volume())
        # Fill the format with the stolen amount
        print("{:.2f} litres were stolen.".format(small_steal))
       
        print("\nCup statuses after the theft:")
        # Print here the status of the big and small cup
        print(big_coffee_cup)
        print(small_coffee_cup)

        # Fill the format with the name of the small cup
        print("\nNow finally the holder of {:s} can drink their coffee:".format(small_coffee_cup.get_name()))
        # Empty here the small cup
        small_coffee_cup.flip()
        # Print here the status of the small cup
        print(small_coffee_cup)


main()

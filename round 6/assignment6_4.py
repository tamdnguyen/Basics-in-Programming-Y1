import random


def initialize_doors(number_of_doors):
    index_door_car = random.randint(0, number_of_doors-1)
    list_boolean = [False] * number_of_doors
    list_boolean[index_door_car] = True
    return list_boolean


def remove_wrong_doors(chosen_door, doors):
    # here I use number of the door as a common unit.
    # Therefore, the number of door has the car is its index in the list+1
    number_door_car = doors.index(True) + 1

    # If chosen_door is the door that has the car behind it,
    # the function returns the number (not index) of a randomly chosen door (other doors are opened).
    # The random door is chosen by using function randint like the door with the car was chosen initially.
    # The function is called so many times that it returns a door that is different from chosen_door.
    # The return value is an integer in the interval 1 - number_of_doors. number_of_doors = length of list of booleans
    if chosen_door == number_door_car:
        number_random_door = random.randint(1, len(doors))
        while number_random_door == chosen_door:
            number_random_door = random.randint(1, len(doors))
        return number_random_door

    # If the door chosen_door has a goat behind it,
    # the function returns the number (not index) of the door that has the car behind it.
    else:
        return number_door_car


def print_doors(doors, dont_open):
    # divide into 4 parts:
    # part 1: _   _   _
    # part 2: | | | | | | or |G| |G| |C|
    # part 3: |_| |_| |_|
    # part 4: number of door
    print("{:^3s} ".format("_") * len(doors))

    # As a final hint:
    # you should approach printing the doors by iterating through the indices of the doors list and,
    # for each index value, checking if index + 1 is in the list dont_open.
    # If it is in the list, print the door closed.
    # If it is not in the list, print it with either "C" or "G", depending on whether the boolean is True or False.
    for i in range(len(doors)):
        if i+1 in dont_open:
            print("| | ", end="")
        else:
            if not doors[i]:
                print("|G| ", end="")
            else:
                print("|C| ", end="")
    print()
    print("{:^3s} ".format("|_|") * len(doors))

    for i in range(len(doors)):
        if 10 <= i <= 99:
            print("{:<3d} ".format(i + 1), end="")
        else:
            print("{:^3d} ".format(i+1), end="")
    print()

def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)

    number_of_doors = int(input("How many doors?\n"))
    while number_of_doors < 3 or number_of_doors > 999:
        print("The number of doors must be between 3-999!")
        number_of_doors = int(input("How many doors?\n"))

    # create the list to store the info of doors, the door has the care has boolean value True, others have False
    list_boolean_door = initialize_doors(number_of_doors)
    # create the dont_open door list, which initially has all the doors
    # (i.e. the first time when print_function prints, all doors are in the list so that all doors are closed
    dont_open = []
    for i in range(number_of_doors):
        dont_open.append(i+1)

    # print the doors the first time before ask for the user's guess
    print_doors(list_boolean_door, dont_open)

    # ask for the guess
    guess = int(input("Choose a door 1-{:d}.\n".format(number_of_doors)))
    while guess < 1 or guess > number_of_doors:
        guess = int(input("Choose a door 1-{:d}.\n".format(number_of_doors)))

    print("You chose the door number {:d}.".format(guess))
    print("...")

    # open the wrong doors, keep the final 2 doors
    another_door = remove_wrong_doors(guess, list_boolean_door)

    # change the dont_open list values so that the 2 final doors are kept closed.
    # change all other doors numbers into 0 except for the guess door and another_door.
    for i in range(len(dont_open)):
        if i != guess - 1 and i != another_door - 1:
            dont_open[i] = 0

    print_doors(list_boolean_door, dont_open)

    print("{:d} certainly wrong doors were opened. The door number {:d} was left.".format(number_of_doors - 2, another_door))
    print("Choose {:d} if you want to keep the door you first chose and choose {:d} if you want to change the door.".format(guess, another_door))

    last_guess = int(input())
    while last_guess != guess and last_guess != another_door:
        print(
            "Choose {:d} if you want to keep the door you first chose and choose {:d} if you want to change the door.".format(
                guess, another_door))
        last_guess = int(input())


    # change dont_open values into 0 to open all the doors
    dont_open[guess-1] = 0
    dont_open[another_door-1] = 0

    print_doors(list_boolean_door, dont_open)

    if last_guess == list_boolean_door.index(True) + 1:
        print("Congratulations! The car was behind the door you chose!")
    else:
        print("A goat emerged from the door you chose! The car was behind the other door :(")


main()


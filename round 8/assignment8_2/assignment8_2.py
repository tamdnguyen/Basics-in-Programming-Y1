VITAMIN_DICTIONARY = {'A': 800, 'B1': 1200, 'B2': 1300, 'B3': 15000, 'B5': 5000, 'B6': 1500, 'B12': 2.0,
                      'C': 75000, 'D': 10, 'E': 9000}

def main():
    name = input("Enter the name of the food file.\n")
    vitamin_in_food = {}

    try:
        # read from the file and write the vitamins and their amount into a dictionary
        file = open(name, "r")
        linelist = file.readlines()
        file.close()
        for line in linelist:
            line = line.rstrip()
            data = line.split()
            # skip the line of less or more than 2 parts
            if len(data) != 2:
                pass
            else:
                # try except to print the invalid line
                try:
                    vitamin_in_food[data[0]] = float(data[1])
                except ValueError:
                    print("Invalid amount of vitamin {:s}.".format(data[0]))

        vitamin = input("Enter the vitamin.\n")
        # get the food name, i.e. the name of the file without .txt part
        food_name = name.split(".")

        # check if vitamin not in food or an unknown vitamin
        if vitamin not in vitamin_in_food:
            print("{:s} does not contain any vitamin {:s}.".format(food_name[0], vitamin))
            return 0
        if vitamin not in VITAMIN_DICTIONARY:
            print("{:s} is an unknown vitamin.".format(vitamin))
            return 0

        food_amount = float(VITAMIN_DICTIONARY[vitamin]) / float(vitamin_in_food[vitamin]) * 100
        if food_amount <= 1000:
            print("You have to eat {:s} {:.1f} grams to reach the daily recommendation of the vitamin {:s}.".format(food_name[0], food_amount, vitamin))
        else:
            print("You have to eat {:s} {:.1f} kilos to reach the daily recommendation of the vitamin {:s}.".format(food_name[0], food_amount / 1000, vitamin))
    except OSError:
        print("Error in reading {:s} file.".format(name))

main()


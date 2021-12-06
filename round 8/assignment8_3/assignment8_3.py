BERRY_TYPES = ["blueberry", "lingonberry", "cloudberry", "cranberry", "raspberry", "strawberry"]


# This function read the file contain amount of berries
# and return the dictionary with the berry name along with its amount
def berry_type_amount(filename_amount):
    berry_amount = {}
    try:
        file_amount = open(filename_amount, "r")
        linelist = file_amount.readlines()
        file_amount.close()
        for line in linelist[1:]:
            # skip the empty lines without error message
            if line != "\n":
                line = line.rstrip()
                data = line.split(",")
                # check for the invalid lines below
                # first is A line does not contain exactly three parts separated by a comma. However, the program has to
                # skip empty lines without an error message.
                if len(data) != 3:
                    print("Invalid line: {:s}".format(line))
                else:
                    # The berry name is unknown
                    # (cannot be found in the list BERRY_TYPES containing all the 6 berry types used in this exercise).
                    if data[1] not in BERRY_TYPES:
                        print("Invalid line: {:s}".format(line))
                    else:
                        # The amount of picked berries in kilos cannot be converted to integer.
                        try:
                            # if the berry is already in the dictionary, add to its total amount
                            if data[1] in berry_amount:
                                berry_amount[data[1]] += int(data[2])
                            # if the berry is not in the dictionary, append it and its amount into the dictionary
                            else:
                                berry_amount[data[1]] = int(data[2])
                        except IndexError:
                            print("Invalid line: {:s}".format(line))
                        except ValueError:
                            print("Invalid line: {:s}".format(line))
        print("File read.")
        return berry_amount
    except OSError:
        print("Invalid file: {:s}".format(filename_amount))
        return 0


# This function read the file containing the berry prices, return a dictionary with the berries and their price
def berry_type_price(filename_price):
    berry_price = {}
    try:
        file_price = open(filename_price, "r")
        linelist = file_price.readlines()
        file_price.close()
        for line in linelist[1:]:
            # skip the empty lines without error message
            if line != "\n":
                line = line.rstrip()
                data = line.split(":")
                # check for the invalid lines below
                # first is A line does not contain exactly three parts separated by a comma. However, the program has to
                # skip empty lines without an error message.
                if len(data) != 2:
                    print("Invalid line: {:s}".format(line))
                else:
                    # The berry name is unknown
                    # (cannot be found in the list BERRY_TYPES containing all the 6 berry types used in this exercise).
                    if data[0] not in BERRY_TYPES:
                        print("Invalid line: {:s}".format(line))
                    else:
                        # The price per kilo cannot be converted to decimal number.
                        try:
                            berry_price[data[0]] = float(data[1])
                        except IndexError:
                            print("Invalid line: {:s}".format(line))
                        except ValueError:
                            print("Invalid line: {:s}".format(line))
        print("File read.")
        return berry_price
    except OSError:
        print("Invalid file: {:s}".format(filename_price))
        return 0


def main():
    filename_amount = input("Enter the name of the file containing the berry data:\n")
    berry_amount = berry_type_amount(filename_amount)
    # if invalid berry data file, exit program
    if berry_amount == 0:
        print()
        print("Program ends.")
        return 0

    filename_price = input("Enter the name of the file containing the prices of the berries:\n")
    berry_price = berry_type_price(filename_price)
    # if invalid berry price file, exit program
    if berry_price == 0:
        print()
        print("Program ends.")
        return 0

    # if a file with berry picking data contains berry names that are in the list BERRY_TYPES,
    # but cannot be found in the file containing the berry prices, the program prints and terminates.
    for key in berry_amount:
        if key in BERRY_TYPES and key not in berry_price:
            print("Some of the berry prices are missing from the file '{:s}'.".format(filename_price))
            print()
            print("Program ends.")
            return 0

    # create the list to calculate the sum of berry kgs and the money earned
    total_weight = []
    total_money = []
    # print the table
    print()
    print("Berry type   Picked berries (kg)   Money earned (eur)")
    print("-" * 53)
    for key in berry_amount:
        print("{:12s} {:>19d} {:>20.2f}".format(key, berry_amount[key], berry_amount[key] * berry_price[key]))
        total_weight.append(berry_amount[key])
        total_money.append(berry_amount[key] * berry_price[key])
    print("-" * 53)
    print("{:12s} {:>19d} {:>20.2f}".format("Total", sum(total_weight), sum(total_money)))
    print()
    print()
    print("Program ends.")


main()
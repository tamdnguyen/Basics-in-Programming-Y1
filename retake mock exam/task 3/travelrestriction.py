def restricted(population, case):
    ratio = case / population * 100000
    is_restricted = False

    if ratio > 8:
        is_restricted = True

    return is_restricted, ratio

def main():
    filename = input("Enter the name of the file to be read:\n")
    total = 0

    try:
        file = open(filename, "r")
        linelist = file.readlines()
        file.close()

        # check If the file is empty, the program prints There was no lines in the file..
        if len(linelist) == 0:
            print("There were no countries in the file.")
            return 0

        for line in linelist:
            line = line.strip()
            parts = line.split(",")

            # check the line does not have three fields separated by commas
            if len(parts) != 3:
                print("Incorrect line:", line)
            else:
                try:
                    population = int(parts[1])
                    case = int(parts[2])
                    if restricted(population, case)[0]:
                        print("{:s} ({:.1f} cases per 100000 inhabitants): travel restrictions apply.".
                              format(parts[0], restricted(population, case)[1]))
                        total += 1
                    else:
                        print("{:s} ({:.1f} cases per 100000 inhabitants): no travel restrictions.".
                              format(parts[0], restricted(population, case)[1]))
                except ValueError:
                    print("Incorrect number in line:", line)
        print("Travel restrictions apply to {:d} countries.".format(total))
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))


main()
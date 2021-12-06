def restriction(population, cases):
    restricted = False

    ratio = (cases / population) * 100000
    if ratio > 8:
        restricted = True

    return restricted, ratio


def main():
    filename = input("Enter the name of the file to be read:\n")
    total = 0

    try:
        file = open(filename, "r")
        linelist = file.readlines()
        file.close()

        # check the file is empty
        if len(linelist) == 0:
            print("There were no countries in the file.")
            return 0

        for line in linelist:
            line = line.strip()
            parts = line.split(",")

            # check if there is not 3 parts
            if len(parts) != 3:
                print("Incorrect line: ", line)
            else:
                # check if some of the fields cannot be interpreted as integers.
                # print the restrictions or not
                try:
                    population = int(parts[1])
                    cases = int(parts[2])

                    if restriction(population, cases)[0]:
                        print("{:s} ({:.1f} cases per 100000 inhabitants): travel restrictions apply.".
                                    format(parts[0],restriction(population, cases)[1]))
                        total += 1
                    else:
                        print("{:s} ({:.1f} cases per 100000 inhabitants): no travel restrictions.".
                              format(parts[0],restriction(population, cases)[1]))
                except ValueError:
                    print("Incorrect number in line: ", line)

        print("Travel restrictions apply to {:d} countries.".format(total))
    except OSError:
        print("Error in reading the file '{:s}'. Program ends.".format(filename))


main()




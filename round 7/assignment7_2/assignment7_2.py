def convert_min_to_hour(min):
    hour = min // 60
    minute = min - 60*hour
    converted = str(hour) + " h " + str(minute) + " min"
    return converted


def main():
    name = input("Enter the name of the file containing your exercise diary:\n")

    try:
        filename = open(name, "r")
        sport = input("What sport are you interested in?\n")
        day_count = 0
        total_time = 0
        sport_in_file = False
        print("{:<8s}   {:s}".format("Day", "Time"))

        for line in filename:
            line = line.rstrip()
            data_line = line.split(",")
            if data_line[1] == sport:
                sport_in_file = True
                day_count += 1
                total_time += int(data_line[2])
                print("{:<8s}   {:s} min".format(data_line[0], data_line[2]))

        filename.close()
        if sport_in_file:
            print("-" * 31)
            print("Total exercise time: {:s}".format(convert_min_to_hour(total_time)))
            print("Number of exercise days:", day_count)
        else:
            print("The sport '{:s}' was not found in the file.".format(sport))
    except OSError:
        print("Error in reading the file {:s}. Program ends.".format(name))
    except ValueError:
        print("Incorrect time in the file {:s}. Program ends.".format(name))

main()
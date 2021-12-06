def main():
    line = input("Enter the lengths of the jumps (cm) separated by commas.\n")
    if line == "":
        print("No accepted results.")
    else:
        results = line.split(",")
        max = 0
        for result in results:
            if int(result) > max:
                max = int(result)
        print("The best result is {:d} cm.".format(max))

main()
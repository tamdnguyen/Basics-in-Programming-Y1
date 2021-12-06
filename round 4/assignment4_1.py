# Implement the function convert_DMS_to_decimal_degrees here.
def convert_DMS_to_decimal_degrees():
    degrees = int(input("Enter the degrees:\n"))
    minutes = int(input("Enter the minutes:\n"))
    seconds = float(input("Enter the seconds:\n"))
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    print("In decimal degrees: {:.6f}".format(decimal_degrees))


def main():
    print("Choose an action:")
    print("1. Convert DMS to decimal degrees.")
    print("2. End.")
    choice = int(input())
    while choice != 2:
        print()
        print("LATITUDE:")
        convert_DMS_to_decimal_degrees()
        print("LONGITUDE:")
        convert_DMS_to_decimal_degrees()
        print()
        print("Choose an action:")
        print("1. Convert DMS to decimal degrees.")
        print("2. End.")
        choice = int(input())
    print("\nProgram ends.")


main()
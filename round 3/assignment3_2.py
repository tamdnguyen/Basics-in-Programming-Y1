def main():
    price = float(input("Enter the purchase price of your computer, smart watch or phone.\n"))
    while price <= 0:
        line = input("Incorrect value. Enter again the value of your device.\n")
        price = float(line)
    if price <= 150:
        print("The value of your device is less than or equal to the deductible.")
        print("The compensation is 0.0 eur.")
    else:
        year = int(input("Enter the year of the purchase.\n"))
        while year > 2021:
            line = input("The year is not valid. Enter again the year of the purchase.\n")
            year = int(line)

        year_of_use = 2021 - year
        age_reduction = year_of_use * 25/100
        if age_reduction <= 0.7:
            compensation = price - 150 - age_reduction*price
        else:
            compensation = price - 150 - 0.7*price

        if compensation > 2500:
            print("The compensation is 2500.0 eur.")
        elif compensation < 0:
            print("The compensation is 0.0 eur.")
        else:
            print("The compensation is ", compensation, " eur.")

main()
def main():
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days
    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")

    LIMIT = 500             # euros
    NORMAL_COMMISSION = 6.5 # %
    BONUS_COMMISSION = 13.5   # %

    # Implement your own code here that goes through the list of
    # sales and calculates and prints the commissions based on those sales.
    total_commission = 0

    for sale in sales:
        if sale >= LIMIT:
            commission = BONUS_COMMISSION * sale / 100
        else:
            commission = NORMAL_COMMISSION * sale / 100
        total_commission += commission
        print("{:.2f} eur".format(commission))

    # Write then a command here that prints the total of commissions.
    print("Total commissions {:.2f} eur.".format(total_commission))
main()
def main():
    days_use = int(input("How many days a week do you use contact lenses?\n"))
    daily_lenses = float(input("How much do the daily lenses cost per pair?\n"))
    monthly_lenses = float(input("How much do the monthly lenses cost per pair?\n"))
    contact_solution = float(input("How much does the contact lens solution cost? (euros per 100 ml)\n"))

    cost_daily = days_use*daily_lenses*4
    cost_monthly = monthly_lenses + (contact_solution/20)*days_use*4

    if cost_monthly >= cost_daily:
        print("You should buy daily lenses.")
        print("They cost ", cost_daily, " euros per month, which is ", end="")
        print(cost_monthly-cost_daily, " euros less than monthly lenses.")

    else:
        if (cost_daily - cost_monthly) <= 5.0:
            print("Daily lenses cost ", cost_daily," euros per month, which is ", end="")
            print(cost_daily-cost_monthly, " euros more than monthly lenses.")
            print("If you prefer convenience and health, daily lenses might still be a better option.")
        else:
            print("You should buy monthly lenses.")
            print("They cost ", cost_monthly, " euros per month, which is ", end="")
            print(cost_daily-cost_monthly, " euros less than daily lenses.")

main()
def main():
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment    = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment  = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years                 = float(input("For how many years are you planning to hold the investment?\n"))

    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year', 'Month', 'Start', 'Monthly', 'End', 'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('','','balance','Profit', 'balance','Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('','',e,e,e,e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    # There are 12 months in a year; let's divide the exponential growth to them expecting it to be constant:

    monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1

    # Write your code here
    month_count = 1  #number of month in progress
    start_balance = initial_investment
    monthly_profit = monthly_profit_multiplier*start_balance
    end_balance = start_balance + monthly_profit + per_month_investment
    cumulative_profit = end_balance - initial_investment - month_count*per_month_investment

    year = int(years // 1)
    month = int(((years % 1) * 12) // 1)
    if month == 0:
        month = 12

    for i in range(year):
        for j in range(12):
            month_count += 1
            final_end_balance = end_balance
            final_profit = cumulative_profit
            print('{:>5d} | {:>5d} | {:>10.2f} | {:>10.2f} | {:>10.2f} | {:>10.2f}'.format(i+1, j+1, start_balance, monthly_profit, end_balance, cumulative_profit))

            start_balance = end_balance
            monthly_profit = monthly_profit_multiplier * start_balance
            end_balance = start_balance + monthly_profit + per_month_investment
            cumulative_profit = end_balance - initial_investment - month_count*per_month_investment

            if end_balance < 0:
                print()
                print("Stopped printing as balance cannot go negative.")
                print('{:<22s}{:>8.2f} {:3s}'.format('End balance:', final_end_balance, e))
                print('{:<22s}{:>8.2f} {:3s}'.format('Total profit:', final_profit, e))
                print('{:<22s}{:>8.2f} {:3s}'.format('Total net deposit:', final_end_balance - final_profit, e))
                return 1

        print('-' * 65)
        #         break
        # else:
        #     print(('-' * 65))
        #     continue
        # break

    if year < years:
        for i in range(1):
            for j in range(month):
                month_count += 1
                final_end_balance = end_balance
                final_profit = cumulative_profit
                print('{:>5d} | {:>5d} | {:>10.2f} | {:>10.2f} | {:>10.2f} | {:>10.2f}'.format(year + 1, j + 1,
                                                                                               start_balance,
                                                                                               monthly_profit,
                                                                                               end_balance,
                                                                                               cumulative_profit))
                start_balance = end_balance
                monthly_profit = monthly_profit_multiplier * start_balance
                end_balance = start_balance + monthly_profit + per_month_investment
                cumulative_profit = end_balance - initial_investment - month_count*per_month_investment

                if end_balance < 0:
                    print()
                    print("Stopped printing as balance cannot go negative.")
                    print('{:<22s}{:>8.2f} {:3s}'.format('End balance:', final_end_balance, e))
                    print('{:<22s}{:>8.2f} {:3s}'.format('Total profit:', final_profit, e))
                    print('{:<22s}{:>8.2f} {:3s}'.format('Total net deposit:', final_end_balance - final_profit, e))
                    return 1
            #         break
            # else:
            #     continue
            # break

    print()
    print('{:<22s}{:>8.2f} {:3s}'.format('End balance:', final_end_balance, e))
    print('{:<22s}{:>8.2f} {:3s}'.format('Total profit:', final_profit, e))
    print('{:<22s}{:>8.2f} {:3s}'.format('Total net deposit:', final_end_balance - final_profit, e))




main()
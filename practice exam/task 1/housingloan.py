def main():
    # get information about the user info
    cost_house = int(input("How much costs the house (euros)?\n"))
    savings = int(input("How much savings do you have (euros)?\n"))
    period = int(input("What is the loan period (years)?\n"))

    # get the information about the bank

    # the first bank
    service_fee_1 = float(input("What is the opening costs in bank A (eur)?\n"))
    margin_1 = float(input("What is the loan marginal in bank A (percentage)?\n"))

    # the second bank
    service_fee_2 = float(input("What is the opening costs in bank B (eur)?\n"))
    margin_2 = float(input("What is the loan marginal in bank B (percentage)?\n"))

    # the third bank
    service_fee_3 = float(input("What is the opening costs in bank C (eur)?\n"))
    margin_3 = float(input("What is the loan marginal in bank C (percentage)?\n"))

    # calculating the fees for each bank deal below
    amount_of_loan = cost_house - savings
    total_interest_1 = 1.3 + margin_1
    total_interest_2 = 1.3 + margin_2
    total_interest_3 = 1.3 + margin_3

    single_installment_1 = amount_of_loan * ((1 + total_interest_1 / 100)**period * total_interest_1/100) \
                           / ((1 + total_interest_1/100)**period - 1)
    single_installment_2 = amount_of_loan * ((1 + total_interest_2 / 100) ** period * total_interest_2 / 100) \
                           / ((1 + total_interest_2 / 100) ** period - 1)
    single_installment_3 = amount_of_loan * ((1 + total_interest_3 / 100) ** period * total_interest_3 / 100) \
                           / ((1 + total_interest_3 / 100) ** period - 1)

    total_cost_1 = single_installment_1 * period + service_fee_1 - amount_of_loan
    total_cost_2 = single_installment_2 * period + service_fee_2 - amount_of_loan
    total_cost_3 = single_installment_3 * period + service_fee_3 - amount_of_loan

    # compare the deal and print the best deal
    cost_list = [total_cost_1, total_cost_2, total_cost_3]
    cheapest = min(cost_list)
    bank = cost_list.index(cheapest)

    if bank == 0:
        print("The bank A is the cheapest.")
        print("The costs for {:d} years loan are {:.2f} euros.".format(period, cheapest))
        print("The total payment is {:.2f} euros excluding own funding of {:.2f} euros.".format(amount_of_loan + cheapest, savings))
    elif bank == 1:
        print("The bank B is the cheapest.")
        print("The costs for {:d} years loan are {:.2f} euros.".format(period, cheapest))
        print("The total payment is {:.2f} euros excluding own funding of {:.2f} euros.".format(amount_of_loan + cheapest, savings))
    else:
        print("The bank C is the cheapest.")
        print("The costs for {:d} years loan are {:.2f} euros.".format(period, cheapest))
        print("The total payment is {:.2f} euros excluding own funding of {:.2f} euros.".format(amount_of_loan + cheapest, savings))
main()

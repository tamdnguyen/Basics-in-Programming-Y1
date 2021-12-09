def cost_installment(amount_of_loan, period, total_interest):
    """
    This function calculates the cost of a single installment
    """
    cost = amount_of_loan * ((1 + total_interest / 100) ** period * total_interest / 100) / (
                (1 + total_interest / 100) ** period - 1)

    return cost


def total_cost(installment, service_fee, period, loan):
    """
        This function calculates the total cost of each bank
    """
    return installment * period + service_fee - loan


def print_bank(bank, period, cheapest, total, savings):
    print("The bank {:s} is the cheapest.".format(bank))
    print("The costs for {:d} years loan are {:.2f} euros.".format(period, cheapest))
    print("The total payment is {:.2f} euros excluding own funding of {:.2f} euros.".format(total, savings))


def main():
    # ask for the input from user
    house_cost = int(input("How much costs the house (euros)?\n"))
    savings = int(input("How much savings do you have (euros)?\n"))
    period = int(input("What is the loan period (years)?\n"))

    # information of bank A
    service_fee_a = float(input("What is the opening costs in bank A (eur)?\n"))
    margin_a = float(input("What is the loan marginal in bank A (percentage)?\n"))

    # information of bank B
    service_fee_b = float(input("What is the opening costs in bank B (eur)?\n"))
    margin_b = float(input("What is the loan marginal in bank B (percentage)?\n"))

    # information of bank C
    service_fee_c = float(input("What is the opening costs in bank C (eur)?\n"))
    margin_c = float(input("What is the loan marginal in bank C (percentage)?\n"))

    # calculate to find the best deal
    amount_of_loan = house_cost - savings
    total_interest_a = 1.3 + margin_a
    total_interest_b = 1.3 + margin_b
    total_interest_c = 1.3 + margin_c

    single_installment_a = cost_installment(amount_of_loan, period, total_interest_a)
    single_installment_b = cost_installment(amount_of_loan, period, total_interest_b)
    single_installment_c = cost_installment(amount_of_loan, period, total_interest_c)

    cost_a = total_cost(single_installment_a, service_fee_a, period, amount_of_loan)
    cost_b = total_cost(single_installment_b, service_fee_b, period, amount_of_loan)
    cost_c = total_cost(single_installment_c, service_fee_c, period, amount_of_loan)

    # a bunch of conditions to find which bank offer best deal
    # just 1 cheapest deal
    if cost_a < cost_b and cost_a < cost_c:
        print_bank(bank="A", period=period, cheapest=cost_a, total=cost_a + amount_of_loan, savings=savings)
        return 0
    elif cost_b < cost_a and cost_b < cost_a:
        print_bank(bank="B", period=period, cheapest=cost_b, total=cost_b + amount_of_loan, savings=savings)
        return 0
    elif cost_c < cost_a and cost_c < cost_b:
        print_bank(bank="C", period=period, cheapest=cost_c, total=cost_c + amount_of_loan, savings=savings)
        return 0
    # A and B are cheapest
    elif cost_a == cost_b and cost_a < cost_c:
        print_bank(bank="A", period=period, cheapest=cost_a, total=cost_a + amount_of_loan, savings=savings)
        return 0
    # B and C are cheapest
    elif cost_b == cost_c and cost_b < cost_a:
        print_bank(bank="B", period=period, cheapest=cost_b, total=cost_b + amount_of_loan, savings=savings)
        return 0
    # A and C are cheapest:
    elif cost_a == cost_c and cost_a < cost_b:
        print_bank(bank="A", period=period, cheapest=cost_a, total=cost_a + amount_of_loan, savings=savings)
        return 0
    elif cost_a == cost_b == cost_c:
        print_bank(bank="A", period=period, cheapest=cost_a, total=cost_a + amount_of_loan, savings=savings)
        return 0


main()




def cost_installment(amount_of_loan,period, total_interest):
    cost = amount_of_loan * ((1 + total_interest / 100) ** period * total_interest / 100) / (
                (1 + total_interest / 100) ** period - 1)

    return cost

print(cost_installment(75000, 15, 5.4))
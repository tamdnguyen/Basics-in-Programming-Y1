amount_of_loan = 75000
total_interest = 5.4
period = 15
total = amount_of_loan * ((1 + total_interest / 100)**period * total_interest/100) / ((1 + total_interest/100)**period - 1)

print(total)
def main():
    print("Enter the values of the trades in separated lines. Stop with a negative value.")
    fee = 0.0

    while True:
        line = input("Enter next value of the trade.\n")
        trade_value = float(line)
        if trade_value >= 0:
            if trade_value < 800:
                fee += trade_value*1/100
            else:
                least_fee = trade_value*0.2/100
                if least_fee < 8:
                    fee += 8
                else:
                    fee += least_fee
        else:
            break

    print("The brokerage fees are ", fee, " eur.")

main()



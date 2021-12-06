import math


def calculate_consumption(size, residents):
    electricity_consumption = 2206.0
    increase_resident = 0
    increase_10m2 = 0

    if 30 < size <= 110:
        increase_10m2 = math.ceil((size - 30)/10) * 16 / 100

    if size > 110:
        increase_10m2 = 8 * 16 / 100 + math.ceil((size - 110)/10) * 5 / 100

    if 1 < residents <= 3:
        increase_resident = (residents - 1) * 12 / 100
    elif residents > 3:
        increase_resident = 2 * 12 / 100 + (residents - 3) * 7 / 100

    increase_price = electricity_consumption * (increase_resident + increase_10m2)
    electricity_consumption += increase_price

    return electricity_consumption


def find_cheapest_contract(contracts, consumption):
    prices = []
    for contract in contracts:
        price = contracts[contract]['kWh_price'] * consumption / 100 + contracts[contract]['month_price'] * 12
        prices.append(price)
    cheapest_price = min(prices)
    cheapest_index = prices.index(cheapest_price)
    cheapest_contract = list(contracts.keys())[cheapest_index]
    return cheapest_contract, cheapest_price


def find_ecofriendly_contract(contracts, consumption):
    prices = []
    renewable = []
    # create list contains the renewable rate and prices of each contract
    for contract in contracts:
        price = contracts[contract]['kWh_price'] * consumption / 100 + contracts[contract]['month_price'] * 12
        prices.append(price)
        renewable.append(contracts[contract]['renewable'])

    # find the most renewable contract(s)
    max_renewable = max(renewable)
    min_indices = []
    for i in range(len(renewable)):
        if renewable[i] == max_renewable:
            min_indices.append(i)

    # if more than 1 contract has the same rate
    # choose the contract with the cheapest price
    if len(min_indices) > 1:
        # find the cheapest contract in the list of most renewable contracts
        min_price = float('inf')
        for index in min_indices:
            if prices[index] < min_price:
                min_price = prices[index]
        min_index = prices.index(min_price)
        cheapest_contract = list(contracts.keys())[min_index]
        return cheapest_contract, min_price
    else:
        most_renewable_index = renewable.index(max_renewable)
        annual_cost = prices[most_renewable_index]
        max_contract = list(contracts.keys())[most_renewable_index]
        return max_contract, annual_cost


def print_all_contracts(contracts):
    for contract, contract_info in contracts.items():
        print(contract)
        for key in contract_info:
            print("   {:s}: {:.2f}".format(key, contract_info[key]))


def main():
    # first, ask for file input and create dictionary of contracts
    # inform errors if errors exist
    name = input("Enter the file name.\n")
    contracts = {}
    try:
        filename = open(name, "r")
        linelist = filename.readlines()
        filename.close()
        for line in linelist[1:]:
            if line != "\n":
                try:
                    line = line.rstrip()
                    data = line.split(",")
                    if len(data) != 4:
                        print("Invalid line:", line)
                    else:
                        contracts[data[0]] = {}
                        contracts[data[0]]['kWh_price'] = float(data[1])
                        contracts[data[0]]['month_price'] = float(data[2])
                        contracts[data[0]]['renewable'] = float(data[3]) / 100
                        # check if the dictionary of contract in line is valid or not
                        # by checking the length of list of values (or keys) of that contract must be 3.
                        # If invalid, delete the contract from dictionary

                except IndexError:
                    print("Invalid line:", line)
                    del contracts[data[0]]
                except ValueError:
                    print("Invalid value:", line)
                    del contracts[data[0]]

        # ask for other information and calculate
        print()
        size = int(input("Enter the size of your apartment (m2).\n"))
        residents = int(input("Enter the number of residents.\n"))
        estimate_consumption = int(input("Enter an estimate of your annual electricity consumption (kWh).\n"))

        print()
        print_all_contracts(contracts)

        calculated_consumption = calculate_consumption(size, residents)

        # find the best contract for the calculated consumption
        calculated_cheapest = find_cheapest_contract(contracts, calculated_consumption)[0]
        calculated_min_price = find_cheapest_contract(contracts, calculated_consumption)[1]
        calculated_eco = find_ecofriendly_contract(contracts, calculated_consumption)[0]
        calculated_eco_cost = find_ecofriendly_contract(contracts, calculated_consumption)[1]

        # find the best contract for the estimated consumption
        estimate_cheapest = find_cheapest_contract(contracts, estimate_consumption)[0]
        estimate_min_price = find_cheapest_contract(contracts, estimate_consumption)[1]
        estimate_eco = find_ecofriendly_contract(contracts, estimate_consumption)[0]
        estimate_eco_cost = find_ecofriendly_contract(contracts, estimate_consumption)[1]

        # print the output:
        print()
        print("The best deals according to the calculated consumption ({:d} kwh):".format(
            int(round(calculated_consumption))))
        if calculated_cheapest == calculated_eco:
            print("The cheapest contract is also the most eco-friendly and it is")
            print("{:s} and costs {:.2f} eur/year.".format(calculated_cheapest, calculated_min_price))
        else:
            print("The cheapest contract is {:s} and costs {:.2f} eur/year.".format(calculated_cheapest,
                                                                                    calculated_min_price))
            print("The most eco-friendly contract is {:s} and costs {:.2f} eur/year.".format(calculated_eco,
                                                                                             calculated_eco_cost))
        print()
        print("The best deals according to the user estimated consumption ({:d} kwh):".format(estimate_consumption))
        if estimate_cheapest == estimate_eco:
            print("The cheapest contract is also the most eco-friendly and it is")
            print("{:s} and costs {:.2f} eur/year.".format(estimate_cheapest, estimate_min_price))
        else:
            print("The cheapest contract is {:s} and costs {:.2f} eur/year.".format(estimate_cheapest,
                                                                                    estimate_min_price))
            print("The most eco-friendly contract is {:s} and costs {:.2f} eur/year.".format(estimate_eco,
                                                                                             estimate_eco_cost))
    except OSError:
        print("Error while reading the file. Program ends.")



main()

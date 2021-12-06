class RestaurantBill:
    FOOD_VAT = 14.0
    DRINK_VAT = 24.0

    def __init__(self, table_number, waitress_name):
        self.__table = table_number
        self.__waitress = waitress_name
        self.__food = []
        self.__drinks = []

    def get_table(self):
        return self.__table

    def get_waitress(self):
        return self.__waitress

    def get_food_prices(self):
        return self.__food

    def get_drink_prices(self):
        return self.__drinks

    def add_to_bill(self, price, is_drink):
        if is_drink:
            self.__drinks.append(price)
        else:
            self.__food.append(price)

    def fix_price(self, line, is_drink, new_price):
        if is_drink:
            if new_price < 0 or line < 1 or line > len(self.__drinks):
                return False
            else:
                if new_price == 0.0:
                    del self.__drinks[line - 1]
                else:
                    self.__drinks[line - 1] = new_price
                return True
        else:
            if new_price < 0 or line < 1 or line > len(self.__food):
                return False
            else:
                if new_price == 0.0:
                    del self.__food[line - 1]
                else:
                    self.__food[line - 1] = new_price
                return True

    def calculate_drink_prices(self):
        include_VAT = sum(self.get_drink_prices())
        exclude_VAT = include_VAT / 1.24
        VAT = include_VAT - exclude_VAT

        return exclude_VAT, VAT, include_VAT

    def calculate_food_prices(self):
        include_VAT = sum(self.get_food_prices())
        exclude_VAT = include_VAT / 1.14
        VAT = include_VAT - exclude_VAT

        return exclude_VAT, VAT, include_VAT

    def calculate_total(self):
        drink = sum(self.get_drink_prices())
        food = sum(self.get_food_prices())
        total = drink + food

        return total

    def make_bill(self):
        # create a separate string for food list and drink list
        food_list = ""
        drink_list = ""
        for i in range(len(self.get_food_prices())):
            food = "{:s}{:8.2f}\n".format(" " * 8, self.get_food_prices()[i])
            food_list += food

        for i in range(len(self.get_drink_prices())):
            drink = "{:s}{:8.2f}\n".format(" " * 8, self.get_drink_prices()[i])
            drink_list += drink

        bill = "Table: {:d}\n" \
               "Waitress: {:s}\n" \
               "FOOD:\n" \
               "{:s}" \
               "DRINKS:\n" \
               "{:s}" \
               "------------------------------\n" \
               "Total {:>7.2f}\n" \
               "\n" \
               "           sales     VAT     total\n" \
               "VAT 24 %: {:>7.2f} {:>7.2f} {:>7.2f}\n" \
               "VAT 14 %: {:>7.2f} {:>7.2f} {:>7.2f}".format(self.get_table(), self.get_waitress(), food_list,
                                                             drink_list, self.calculate_total(),
                                                             self.calculate_drink_prices()[0],
                                                             self.calculate_drink_prices()[1],
                                                             self.calculate_drink_prices()[2],
                                                             self.calculate_food_prices()[0],
                                                             self.calculate_food_prices()[1],
                                                             self.calculate_food_prices()[2])

        return bill

    def __str__(self):
        info = "Table: {:d}\n" \
               "Waitress: {:s}\n" \
               "Total sum so far: {:.2f} eur.".format(self.get_table(), self.get_waitress(), self.calculate_total())

        return info

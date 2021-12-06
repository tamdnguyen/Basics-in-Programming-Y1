class RentApartment:
    RENTAL_SERVICE_FEE = 100 # eur per month
    STUDIO_SIZE_LIMIT = 32 # m2
    ONE_BEDROOOM_SIZE_LIMIT = 45 # m2
    STUDIO_PRICE_LEVEL = 25 # eur/m2
    ONE_BEDROOOM_PRICE_LEVEL = 20 # eur/m2
    LARGE_PRICE_LEVEL = 18 # eur/m2
    TRANSFER_TAX = 0.02

    def __init__(self, address, rent, maintenance_charge, size, free_of_debt_price):
        self.__address = address
        self.__rent = rent
        self.__maintenance_charge = maintenance_charge
        self.__size = size
        self.__free_of_debt_price = free_of_debt_price
        self.__rental_service = False
        self.__renovation_costs = 0

    def get_address(self):
        return self.__address

    def get_rent(self):
        return self.__rent

    def get_maintenance_charge(self):
        return self.__maintenance_charge

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__free_of_debt_price

    def get_renovation_costs(self):
        return self.__renovation_costs

    def update_rental_service(self):
        if self.__rental_service:
            self.__rental_service = False
            return self.__rental_service
        else:
            self.__rental_service = True
            return self.__rental_service

    def increase_rent(self, new_rent):
        if new_rent > self.get_rent():
            self.__rent = new_rent
            return True
        else:
            return False

    def add_renovation_costs(self, costs):
        self.__renovation_costs += costs

    def calculate_square_meter_rent(self):
        per_square_meter = self.get_rent() / self.get_size()
        return per_square_meter

    def calculate_rental_income(self):
        # The rental income is determined as follows
        # (monthly_rent - costs_of_month) * 12 / (free_of_debt_price + transfer_tax + renovation_costs) * 100.
        # The amount of the transfer tax is determined by multiplying the free of debt price
        # by the percent of the transfer tax which is 2 % in this exercise.
        # The monthly costs consist of the maintenance charge and the possible use of a rental service.

        transfer_tax = self.get_price() * RentApartment.TRANSFER_TAX
        if self.__rental_service:
            monthly_costs = self.get_maintenance_charge() + RentApartment.RENTAL_SERVICE_FEE
        else:
            monthly_costs = self.get_maintenance_charge()
        rental_income = (self.get_rent() - monthly_costs) * 12 / \
                        (self.get_price() + transfer_tax + self.get_renovation_costs()) * 100
        return rental_income

    def compare_rental_incomes(self, other):
        this_rental_income = self.calculate_rental_income()
        other_rental_income = other.calculate_rental_income()

        if this_rental_income > other_rental_income:
            return 1
        elif this_rental_income == other_rental_income:
            return 0
        else:
            return -1

    def calculate_return_on_equity(self, down_payment, loan_interest):
        if self.__rental_service:
            monthly_costs = self.get_maintenance_charge() + RentApartment.RENTAL_SERVICE_FEE
        else:
            monthly_costs = self.get_maintenance_charge()
        return_on_equity = (self.get_rent() - monthly_costs - loan_interest) * 12 / down_payment * 100
        return return_on_equity

    def check_price_level(self):
        if self.get_size() < 32:
            if self.calculate_square_meter_rent() >= 25:
                return True
            else:
                return False
        if 32 <= self.get_size() < 45:
            if self.calculate_square_meter_rent() >= 20:
                return True
            else:
                return False
        if self.get_size() >= 45:
            if self.calculate_square_meter_rent() >= 18:
                return True
            else:
                return False

    def __str__(self):
        address = self.get_address()
        maintenance_charge = str(self.get_maintenance_charge())
        size = str(self.get_size())
        rent = str(self.get_rent())
        if self.__rental_service:
            rental_service = "in use"
        else:
            rental_service = "not in use"
        info = "Address: {:s}\nMaintenance charge: {:s} eur \nSize: {:s} m2 \nRent: {:s} eur\n" \
               "Rental service: {:s}".format(address, maintenance_charge, size, rent, rental_service)

        return info


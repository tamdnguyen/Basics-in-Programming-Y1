class PostalArea:
    def __init__(self, area_code, number_of_people):
        self.__code = area_code
        self.__people = number_of_people
        self.__positive = 0
        self.__negative = 0
        self.__dead = 0

    def get_code(self):
        return self.__code

    def get_positives(self):
        return self.__positive

    def get_negatives(self):
        return self.__negative

    def get_dead(self):
        return self.__dead

    def change_statistics(self, positive_test, negative_test, deads):
        if self.get_positives() + positive_test < 0:
            self.__positive = 0
        else:
            self.__positive += positive_test

        if self.get_negatives() + negative_test < 0:
            self.__negative = 0
        else:
            self.__negative += negative_test

        if deads >= 0:
            self.__dead += deads

    def calculate_ratio_of_sick(self):
        if self.__people == 0:
            return 0
        else:
            return self.get_positives() / self.__people

    def compare_areas(self, other_area):
        if self.calculate_ratio_of_sick() > other_area.calculate_ratio_of_sick():
            return True
        else:
            return False

    def __str__(self):
        info = "area code: {:s}, people: {:d}, positive: {:d}, negative: {:d}, dead: {:d}".\
            format(self.get_code(), self.__people, self.get_positives(), self.get_negatives(), self.get_dead())

        return info

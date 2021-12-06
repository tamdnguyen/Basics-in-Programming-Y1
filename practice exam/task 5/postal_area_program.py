# The program is divided to functions that helps grading in A+.
# For the sam reason, the user input is not checked.

# Fill the rows that are marked with required method calls.

# Note. The code below does not work.


import postal_area


def create_areas():
    code1 = input("Give the area code of the first area.\n")
    people1 = int(input("Give the number of people living in this area.\n"))
    code2 = input("Give the area code of the second area.\n")
    people2 = int(input("Give the number of people living in this area.\n"))
    #########################################################
    # Task 1/6:
    # Create two postal areas with information given above
    #########################################################
    first = postal_area.PostalArea(code1, people1)      # fill this row for the first postal area
    second = postal_area.PostalArea(code2, people2)     # fill this row for the second postal area

    return first, second


def add_test_results(area):
    positives = int(input("How many people have got a positive corona test result?\n"))
    negatives = int(input("How many people have got a negative corona test result?\n"))
    #########################################################
    # Task 2/6:
    # Add test results given by the user to the
    # the postal area given as parameter.
    # Write the suitable method call below
    ##########################################################
            # Write the method call here
    area.change_statistics(positives, negatives, 0)


def add_dead(area):
    dead = int(input("How many people have died from corona?\n"))
    #########################################################
    # Task 3/6:
    # Add the numbr of deaths given by the user to the
    # postal aera given as parameter.
    # Write the suitable method call below
    # #########################################################
            # Write the method call here
    area.change_statistics(0, 0, dead)


def check_amount_of_sick(area):
    #########################################################
    # Task 4/6:
    # Call the methods that give the portion of sick
    # and the postal area code of the area
    # given in the parameter.
    #########################################################
    amount = area.calculate_ratio_of_sick()        # add method call
    area_code = area.get_code()    # add method call

    # the row below does not need any modifications
    print("{:.2f}% of people living in postal area {:s} have got a positive corona test result.".format(amount*100, area_code))


def which_has_higher_ratio(first_area, second_area):
    #########################################################
    # Task 5/6:
    # Fill the if command statement by calling a method
    # that compares two area objects.
    # Fill also method call that gives the postal area code.
    #########################################################
    area = None
    if first_area.compare_areas(second_area): # write your method call here
        area = first_area
    else:
        area = second_area

    area_code = area.get_code()   # write the method call for postal area code here
    print("Area {:s} has relatively more people that have a corona infection.".format(area_code))


def print_areas(first, second):
    ########################################################
    # Task 6/6:
    # Print the information of the areas using their __str__ method.
    ########################################################
    print("Area information:")
    print(first)              # fill this row for the first postal area
    print(second)             # fill this row for the second postal area


# The main program below does not need modifications.
def main():
    first_area, second_area = create_areas()

    print("******* At the beginning")
    print_areas(first_area, second_area)
    print()

    print("Add test results to the areas.")
    print("For the first area:")
    add_test_results(first_area)
    print("For the second area:")
    add_test_results(second_area)

    print("Add dead.")
    print("For the first area:")
    add_dead(first_area)
    print("For the second area:")
    add_dead(second_area)
    print()

    print("******** After adding the statistics")
    print_areas(first_area, second_area)
    print()

    print("Ratio of sick people:")
    check_amount_of_sick(first_area)
    check_amount_of_sick(second_area)
    print()

    print("Which area has more sick people?")
    which_has_higher_ratio(first_area, second_area)
    print()

    print("****** At the end:")
    print_areas(first_area, second_area)


main()

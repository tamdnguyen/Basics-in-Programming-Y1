BEAN_ROW_SPACING = 50  # cm
BEAN_SEED_SPACING = 15  # cm

RADISH_ROW_SPACING = 20  # cm
RADISH_SEED_SPACING = 4   # cm

CARROT_ROW_SPACING = 30  # cm
CARROT_SEED_SPACING = 2  # cm

def calculate_number_of_seeds(x, y, germination_rate, row_spacing, seed_spacing):
    germination_rate = germination_rate / 100
    seed_number = int((x//row_spacing) * (y//seed_spacing) / germination_rate)
    return seed_number


def main():
    print("This program calculates the number of seeds that you need.")
    width = int(input("Enter the width of the field (cm):\n"))
    height = int(input("Enter the height of the field (cm):\n"))
    print("Which vegetable do you want to grow?")
    print("1. Beans")
    print("2. Radishes")
    print("3. Carrots")
    vegetable = int(input())
    germination_rate = float(input("Enter the germination rate of the seeds (%):\n"))

    if vegetable == 1:
        seed_num_1 = calculate_number_of_seeds(width, height, germination_rate, BEAN_ROW_SPACING, BEAN_SEED_SPACING)
        seed_num_2 = calculate_number_of_seeds(height, width, germination_rate, BEAN_ROW_SPACING, BEAN_SEED_SPACING)

        if seed_num_1 > seed_num_2:
            print("Set the rows perpendicular to the width ({:d} cm) of the field to get maximum harvest.".format(width))
            print("You need {:d} seeds.".format(seed_num_1))
        elif seed_num_1 < seed_num_2:
            print("Set the rows perpendicular to the height ({:d} cm) of the field to get maximum harvest.".format(height))
            print("You need {:d} seeds.".format(seed_num_2))
        else:
            print("Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.")
            print("You need {:d} seeds.".format(seed_num_2))

    elif vegetable == 2:
        seed_num_1 = calculate_number_of_seeds(width, height, germination_rate, RADISH_ROW_SPACING, RADISH_SEED_SPACING)
        seed_num_2 = calculate_number_of_seeds(height, width, germination_rate, RADISH_ROW_SPACING, RADISH_SEED_SPACING)

        if seed_num_1 > seed_num_2:
            print(
                "Set the rows perpendicular to the width ({:d} cm) of the field to get maximum harvest.".format(width))
            print("You need {:d} seeds.".format(seed_num_1))
        elif seed_num_1 < seed_num_2:
            print("Set the rows perpendicular to the height ({:d} cm) of the field to get maximum harvest.".format(
                height))
            print("You need {:d} seeds.".format(seed_num_2))
        else:
            print("Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.")
            print("You need {:d} seeds.".format(seed_num_2))

    elif vegetable == 3:
        seed_num_1 = calculate_number_of_seeds(width, height, germination_rate, CARROT_ROW_SPACING, CARROT_SEED_SPACING)
        seed_num_2 = calculate_number_of_seeds(height, width, germination_rate, CARROT_ROW_SPACING, CARROT_SEED_SPACING)

        if seed_num_1 > seed_num_2:
            print(
                "Set the rows perpendicular to the width ({:d} cm) of the field to get maximum harvest.".format(width))
            print("You need {:d} seeds.".format(seed_num_1))
        elif seed_num_1 < seed_num_2:
            print("Set the rows perpendicular to the height ({:d} cm) of the field to get maximum harvest.".format(
                height))
            print("You need {:d} seeds.".format(seed_num_2))
        else:
            print("Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.")
            print("You need {:d} seeds.".format(seed_num_2))

main()

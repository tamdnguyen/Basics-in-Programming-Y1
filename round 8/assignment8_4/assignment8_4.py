import math


# This is the function to calculate the distance between point A and point B
# point_A, point_B is a list containing coordinates
# e.g. point_A = [100, 250] and point_B = [380, 410]
def find_distance(point_A, point_B):
    distance = math.sqrt((point_A[0] - point_B[0])**2 + (point_A[1] - point_B[1])**2)
    return distance


def is_inside_cell_tower_range(point, cell_tower_list):
    inside_range = False
    for item in cell_tower_list:
        distance = find_distance(point, item[0])
        if distance <= item[1]:
            inside_range = True

    if inside_range:
        return True
    else:
        return False


def find_nearest_tower_in_range(point, cell_tower_list):
    # check If the cell tower list given as a parameter is empty or
    # the point is not inside any cell tower working range, the function returns [-1, -1].
    if not cell_tower_list:
        return [-1, -1]
    if not is_inside_cell_tower_range(point, cell_tower_list):
        return [-1, -1]

    # create a list to contain all the info of the distance to the cell tower
    # this list has the same index for each cell tower as the index in the cell_tower_list
    distance_list = [float('inf')] * len(cell_tower_list)
    for i in range(len(cell_tower_list)):
        distance = find_distance(point, cell_tower_list[i][0])
        # if the point is in the range of the cell tower
        # append the distance into the list of distance
        if distance <= cell_tower_list[i][1]:
            distance_list[i] = distance
    min_distance = min(distance_list)
    min_index = distance_list.index(min_distance)
    nearest_tower = cell_tower_list[min_index][0]

    return nearest_tower


def get_cell_tower_list(filename):
    cell_tower_list = []
    try:
        # first, read file and add data into the list
        file = open(filename, "r")
        linelist = file.readlines()
        file.close()
        for line in linelist[1:]:
            line = line.rstrip()
            coordinate_range = line.split(":")
            # here we need to check for different types of errors
            # A line does not contain exactly two parts separated by a colon.
            if len(coordinate_range) != 2:
                print("Invalid line: {:s}".format(line))
            else:
                coordinates = coordinate_range[0].split(",")
                # The coordinate part of the line does not contain exactly two parts separated by a comma.
                if len(coordinates) != 2:
                    print("Invalid coordinates or radius in line: {:s}".format(line))
                else:
                    # The working range or the coordinates separated by a comma cannot be converted to integer.
                    try:
                        # append the coordinates and the range into the cell_tower_list if no error occurs
                        cell_tower_list.append([[int(coordinates[0]), int(coordinates[1])],
                                                int(coordinate_range[1])])
                    except ValueError:
                        print("Invalid coordinates or radius in line: {:s}".format(line))
        print("File read.")
        return cell_tower_list
    except OSError:
        print("Error in reading the file '{:s}'.".format(filename))
        return 0


def main():
    name = input("Enter the name of the file containing the cell tower information:\n")
    cell_tower_list = get_cell_tower_list(name)

    # check if the cell tower list is invalid or empty, if so then terminate the program
    if cell_tower_list == 0 or len(cell_tower_list) == 0:
        print()
        print("No cell tower information available.")
        print("Program ends.")
        return 0

    # get the input from the users
    print()
    print("Enter coordinates. Stop with an empty line.")
    line = input("Enter the coordinates separated by comma:\n")
    while line != "":
        point = line.split(",")
        # check for different error of point input
        # The user input contains less than two parts separated by a comma.
        if len(point) < 2:
            print("Invalid coordinates! Enter two coordinates separated by comma.")
            line = input("Enter the coordinates separated by comma:\n")
            continue
        # The coordinates cannot be converted to integer.
        try:
            converted_coordinate = [int(point[0]), int(point[1])]
            # The user inputs negative coordinates.
            if converted_coordinate[0] < 0 or converted_coordinate[1] < 0:
                print("Invalid coordinates! Coordinates must be positive integers.")
                line = input("Enter the coordinates separated by comma:\n")
                continue
            # find the best tower
            best_tower = find_nearest_tower_in_range(converted_coordinate, cell_tower_list)
            # check to see if the point is inside the signal range or not
            if best_tower == [-1, -1]:
                print("The place is not inside of any cell tower range.")
                print()
            else:
                print("The place is inside a cellular network range.")
                print("The coordinates of the cell tower with the strongest signal: ({:d}, {:d})".format(best_tower[0],
                                                                                                         best_tower[1]))
                print()

            line = input("Enter the coordinates separated by comma:\n")
        except ValueError:
            print("Invalid coordinates! Enter the coordinates as integers.")
            line = input("Enter the coordinates separated by comma:\n")
            continue

    print("Program ends.")


main()



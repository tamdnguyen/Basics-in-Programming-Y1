def resistors_in_parallel(resistor_list, target):
    for i in range(len(resistor_list)-1):
        for j in range(i+1, len(resistor_list)):
            practical_value = (resistor_list[i]*resistor_list[j]) / (resistor_list[i]+resistor_list[j])
            if practical_value == target:
                if resistor_list[i] > resistor_list[j]:
                    return practical_value, float(resistor_list[i]), float(resistor_list[j])
                elif resistor_list[j] > resistor_list[i]:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])
                else:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])

            elif abs(practical_value - target) <= target*2/100:
                if resistor_list[i] > resistor_list[j]:
                    return practical_value, float(resistor_list[i]), float(resistor_list[j])
                elif resistor_list[j] > resistor_list[i]:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])
                else:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])

    return 0.0, 0.0, 0.0


def resistors_in_series(resistor_list, target):
    for i in range(len(resistor_list) - 1):
        for j in range(i + 1, len(resistor_list)):
            practical_value = (resistor_list[i] + resistor_list[j])
            if practical_value == target:
                if resistor_list[i] > resistor_list[j]:
                    return practical_value, float(resistor_list[i]), float(resistor_list[j])
                elif resistor_list[j] > resistor_list[i]:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])
                else:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])

            elif abs(practical_value - target) <= target * 2 / 100:
                if resistor_list[i] > resistor_list[j]:
                    return practical_value, float(resistor_list[i]), float(resistor_list[j])
                elif resistor_list[j] > resistor_list[i]:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])
                else:
                    return practical_value, float(resistor_list[j]), float(resistor_list[i])

    return 0.0, 0.0, 0.0


def main():
    target = float(input("Enter the desired resistance in ohms.\n"))
    print("Enter the resistances of the resistors in ohms and stop with a negative value.")
    resistor_list = []

    while True:
        resistor = float(input())
        if resistor < 0:
            break
        resistor_list.append(resistor)

    parallel_connection = resistors_in_parallel(resistor_list, target)
    series_connection = resistors_in_series(resistor_list, target)

    error_parallel = abs(target - parallel_connection[0])
    error_series = abs(target - series_connection[0])

    if parallel_connection[0] == series_connection[0] == 0.0 and parallel_connection[1] == series_connection[1] == 0.0:
        print("No suitable resistors.")
        return 0

    if error_series == error_parallel or error_series < error_parallel:
        print("The best combination of resistors is {:.1f} ohm and {:.1f} ohm resistors connected in series.".
              format(series_connection[1], series_connection[2]))
    else:
        print("The best combination of resistors is {:.1f} ohm and {:.1f} ohm resistors connected in parallel.".
              format(parallel_connection[1], parallel_connection[2]))

main()


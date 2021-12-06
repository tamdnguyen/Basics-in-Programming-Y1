# P = 8/27 * ρ * v³ * A
#
# ρ is the air density (kg/m³), v is the wind speed (m/s) and A is the total area of the blades (m²).
p = 1.225
A = 8659


def calculate_powers(velocities_list):
    average_power = [0.0] * len(velocities_list)
    for i in range(len(velocities_list)):
        if 3 <= velocities_list[i] <= 25:
            average_power[i] = 8/27 * p * (velocities_list[i]**3) * A / 1000
        else:
            average_power[i] = 0.0
    return average_power


def calculate_capacity_factor(power_list):
    generated_electric_energy = sum(power_list)
    highest_possible_power = 3450 * len(power_list)
    capacity_factor = generated_electric_energy / highest_possible_power
    return capacity_factor


def main():
    name = input("Enter the name of the file containing wind velocities.\n")

    wind_speed = []
    try:
        filename = open(name, "r")
        linelist = filename.readlines()
        filename.close()
        for line in linelist[1:]:
            try:
                line = line.rstrip()
                data = line.split(",")
                wind_speed.append(float(data[5]))
            except IndexError:
                pass
            except ValueError:
                pass
        power = calculate_powers(wind_speed)
        capacity_factor = calculate_capacity_factor(power)
        max_power = max(power)
        total_electricity = sum(power)
        print("The maximum power of the wind turbine was {:.1f} kW.".format(max_power))
        print("The wind turbine generated {:.1f} kWh of electricity.".format(total_electricity))
        print("The capacity factor of the wind turbine was {:.3f}.".format(capacity_factor))
    except OSError:
        print("Error while reading the '{:s}' file. Program ends.".format(name))


main()

AIR_DENSITY = 1.225 # kg/m3
SPECIFIC_HEAT_CAPACITY_AIR = 1012 # J/(kg*celcius)
COMPUTER_HEATING_RATIO = 0.92
LIGHTS_HEATING_RATIO = 0.90
OVEN_HEATING_RATIO = 0.95
WASHING_MACHINE_HEATING_RATIO = 0.8
ERROR_WITH_WARMING = -99
KWH_PRICE = 9.89 # cents/kWh


def calculate_warming(power, time, device_type, room_size):
    tempature_change = 0

    P = power
    t = time*60
    c = SPECIFIC_HEAT_CAPACITY_AIR
    rho = AIR_DENSITY
    V = room_size

    #check valid input
    if time < 0 or power < 0:
        tempature_change = -99
        return tempature_change

    if device_type == "computer":
        k = COMPUTER_HEATING_RATIO
    elif device_type == "lights":
        k = LIGHTS_HEATING_RATIO
    elif device_type == "oven":
        k = OVEN_HEATING_RATIO
    elif device_type == "washing machine":
        k = WASHING_MACHINE_HEATING_RATIO
    else:
        tempature_change = -99
        return tempature_change

    tempature_change = k * P * t / (c * rho * V)

    return tempature_change

def calculate_costs(power, time):
    return (power / 1000)*(time / 60)*KWH_PRICE

def main():
    total_temperature_heat = 0
    total_cost = 0

    room_size = float(input("Enter the size of the room (m3).\n"))
    device_type = str(input("Enter the device type (computer, lights, oven or washing machine).\n"))
    power = float(input("Enter the power of the device (W).\n"))
    time = int(input("Enter time of use (min).\n"))

    temp = calculate_warming(power, time, device_type, room_size)
    cost = calculate_costs(power, time)
    if temp == -99:
        print("Invalid input.")
    else:
        total_temperature_heat += temp
        total_cost += cost

    answer = str(input("Do you want to enter another device (yes or no)?\n"))

    while answer == "yes":
        device_type = str(input("Enter the device type (computer, lights, oven or washing machine).\n"))
        power = float(input("Enter the power of the device (W).\n"))
        time = int(input("Enter time of use (min).\n"))

        temp = calculate_warming(power, time, device_type, room_size)
        cost = calculate_costs(power, time)
        if temp == -99:
            print("Invalid input.")
        else:
            total_temperature_heat += temp
            total_cost += cost

        answer = str(input("Do you want to enter another device (yes or no)?\n"))

    print("The electric devices heat the room by {:.2f} degrees and it costs {:.2f} cents.".format(total_temperature_heat, total_cost))

main()
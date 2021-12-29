# ROUND 4, Functions

The concept of this round is about function, parameter and return value.

The description of the exercises are given below:
1. [Exercise 1](#exercise-1)
2. [Exercise 2](#exercise-2)
3. [Exercise 3](#exercise-3)
4. [Exercise 4](#exercise-4)


## Exercise 1 <a name="exercise-1"></a>

**Initial preparations**

Given code template

```
# Implement the function convert_DMS_to_decimal_degrees here.

def main():
    print("Choose an action:")
    print("1. Convert DMS to decimal degrees.")
    print("2. End.")
    choice = int(input())
    while choice != 2:
        print()
        print("LATITUDE:")
        convert_DMS_to_decimal_degrees()
        print("LONGITUDE:")
        convert_DMS_to_decimal_degrees()
        print()
        print("Choose an action:")
        print("1. Convert DMS to decimal degrees.")
        print("2. End.")
        choice = int(input())
    print("\nProgram ends.")


main()
```
**Background**

A geographic coordinate system uses latitude and longitude expressed in degrees. Degree is a unit of angle measurement. The angles are specified in the spherical coordinate system, where point (0°N, 0°E) is located at the intersection of the Equator (the 0° parallel of latitude) and the Prime Meridian (the 0° of longitude). The Equator divides the globe into Northern (N) and Southern (S) hemispheres. The Prime Meridian divides the globe into Eastern (E) and Western (W) hemispheres. The latitude value ranges from -90° to 90° and the longitude value ranges from -180° to 180°. The sign of the latitude and longitude values depend on the hemisphere in where the point is located.

The numerical values for latitude and longitude can have a number of different formats. One format to use is a degrees-minutes-seconds (DMS) format. For example, the coordinates expressed in DMS for Aalto University are:

```
LATITUDE: 60° 11' 11.7"N
LONGITUDE: 24° 49' 39.7"E
```

You can also express geographical coordinates in decimal degree format. 
The coordinates above converted to decimal degrees:

```
LATITUDE: 60.186583
LONGITUDE: 24.827694
```

The conversion from DMS to decimal degrees is useful, because decimal degrees are used, for example, in many geographic information systems and web mapping applications. Also, mathematical operations are performed in decimal degree coordinates. Even though many applications also work with DMS format, they have to convert the coordinates back to decimal degrees for the calculations.

**Description of the exercise**

In this exercise you will complete a program that converts the user's coordinates 
(entered as degrees, minutes and seconds) to decimal degrees. 
The main function has been given to you. 
Do not change it in any way. 
Your task is to write a function `convert_DMS_to_decimal_degrees` 
(do not change the name of the function). The function asks the user for degrees, minutes and seconds of one coordinate. Degrees and minutes are entered as integers, and seconds as a decimal number. The function converts the entered degrees, minutes and seconds to decimal degrees and prints the converted coordinate. The conversion from the DMS to decimal degrees is done by using the following formula:

`decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)`

In this exercise, we assume that the given locations are in both the Northern and the Eastern hemispheres to make the calculations simpler. Now, the coordinates can only get positive values, meaning the latitude ranges from 0 to 90° and the longitude ranges from 0 to 180°.
Note: in this type of exercises, the function return values and parameters should be used. The degrees, minutes and seconds should be passed to the function as parameters, the function should return the converted coordinate, and the coordinates should be printed in the main function. However, return values and parameters are not used here so that you can practise writing functions in this exercise before learning about the return command and the use of parameters.

**Output of the program**

The printing of the decimal degrees must be done in the function `convert_DMS_to_decimal_degrees`. Decimal degrees should be printed with the precision of 6 decimals.

Note: Use the output formatting that you have learned in this course (braces and the format method). Do not use any other methods (e.g. Python's round function) to enable the automatic testing of the program. The round function, for example, does not show the trailing zeros in the rounded decimal number which leads to an output with wrong precision.

**Error handling**

Your program does not have to handle errors. You can assume that the user only inputs reasonable 
values. For example, the latitude values are given between 0 and 90° and the longitude values are 
between 0 to 180°. Moreover, the user enters minutes and seconds from the range between 0 and 60.

**Examples of the execution of the program:**

```
[execution of the program begins]
Choose an action:
1. Convert DMS to decimal degrees.
2. End.
1

LATITUDE:
Enter the degrees:
60
Enter the minutes:
11
Enter the seconds:
11.6
In decimal degrees: 60.186556
LONGITUDE:
Enter the degrees:
24
Enter the minutes:
49
Enter the seconds:
41.1
In decimal degrees: 24.828083

Choose an action:
1. Convert DMS to decimal degrees.
2. End.
1

LATITUDE:
Enter the degrees:
69
Enter the minutes:
17
Enter the seconds:
3.5
In decimal degrees: 69.284306
LONGITUDE:
Enter the degrees:
21
Enter the minutes:
15
Enter the seconds:
58.0
In decimal degrees: 21.266111

Choose an action:
1. Convert DMS to decimal degrees.
2. End.
1

LATITUDE:
Enter the degrees:
40
Enter the minutes:
25
Enter the seconds:
56.3
In decimal degrees: 40.432306
LONGITUDE:
Enter the degrees:
116
Enter the minutes:
34
Enter the seconds:
10.8
In decimal degrees: 116.569667

Choose an action:
1. Convert DMS to decimal degrees.
2. End.
2

Program ends.

[execution of the program ends]
```

## Exercise 2 <a name="exercise-2"></a>

**Description of the exercise**

The user is thinking of buying a round swimming pool and has to choose a right pool size so that the water consumption is not too high. Write a program that asks the user for the measurements of the pool and calculates the amount and cost of the water needed to fill the pool.

**Structure of the program**

Write the following function in your program:

- _calculate_water_volume_and_price(diameter, height)_
  - The diameter (m) and height (m) are given as parameters.
  - The function calculates how many liters of water are needed to fill the pool and how much the water costs (in euros). The function then prints the calculated numbers.
  - The function does not return anything.

Use the following constant for the cost of water:

`PRICE_PER_CUBIC_METER = 5.0  # eur/m^3` so the water costs 5.0 euros per cubic meter (m³).
  
In this exercise, you need to use pi (π) to calculate the area of a circle. 
You can use constant `pi` if you import Python's math module into your program. Write
`import math`
in the beginning of your program after which you can use pi by writing
`math.pi`

In addition, write a main function that asks the user for the number of pools to be handled. 
After that, for each pool the program first asks for the measurements and then prints the needed 
water amount and cost. The water volume and cost are calculated and printed in the function 
`calculate_water_volume_and_price` which is called by the main function.

Note: in this type of exercises, function return values should be used and the amount and cost of the water should be printed only in the main function. However, return values are not used here so that you can practise writing functions in this exercise before learning about the return command and the use of return values.

**Output of the program**

The printing of water volume and cost must be done in the function 
`calculate_water_volume_and_price`. The amount of water in liters should be printed with the 
precision of 0 decimals (use the formatting `{:.0f}`). The cost of water is printed in euros with the precision of 2 decimals.

**Error handling**

Your program does not have to handle errors. You can assume that the user only inputs reasonable values. For example, the number of pools is entered as an integer and the measurements are entered as positive decimal numbers.

**Examples of the execution of the program:**

```
[execution of the program begins]
Enter the number of pools:
1
1. pool
Enter the diameter of the pool in meters:
8.0
Enter the height of the pool in meters:
1.0
You need 50265 liters of water to fill the pool.
It will cost you 251.33 euros.


[execution of the program ends]
[execution of the program begins]
Enter the number of pools:
3
1. pool
Enter the diameter of the pool in meters:
2.5
Enter the height of the pool in meters:
1.2
You need 5890 liters of water to fill the pool.
It will cost you 29.45 euros.

2. pool
Enter the diameter of the pool in meters:
5.0
Enter the height of the pool in meters:
1.8
You need 35343 liters of water to fill the pool.
It will cost you 176.71 euros.

3. pool
Enter the diameter of the pool in meters:
10.0
Enter the height of the pool in meters:
0.8
You need 62832 liters of water to fill the pool.
It will cost you 314.16 euros.


[execution of the program ends]
```

## Exercise 3 <a name="exercise-3"></a>

**Description of the exercise**

The user is growing their own food and wants to use all their field area effectively. Write a program that calculates how many seeds are needed to fill the field with a certain species. The program can calculate the number of seeds needed for three different species (bean, radish and carrot). We use the following row and seed spacings in this exercise:

- The row spacing for beans: 50 cm 
- The seed spacing for beans: 15 cm 
- The row spacing for radishes: 20 cm 
- The seed spacing for radishes: 4 cm 
- The row spacing for carrots: 30 cm 
- The seed spacing for carrots: 2 cm

The row spacing means the space needed between rows. The seed spacing means the space needed between seeds in a row. In this program you need to consider the direction of the rows according to the field (vertical/ horizontal), because the plan is to grow as many plants as possible. The germination rate also has an effect on how many seeds are needed.

**Structure of the program**

The constants needed in this program are given to you below. Copy these to the beginning of your program, outside of all the functions:

```
BEAN_ROW_SPACING = 50  # cm
BEAN_SEED_SPACING = 15  # cm

RADISH_ROW_SPACING = 20  # cm
RADISH_SEED_SPACING = 4   # cm

CARROT_ROW_SPACING = 30  # cm
CARROT_SEED_SPACING = 2  # cm
```

In Python constants are usually written in capital letters at the beginning of the program. After defining the constants, don't write the numerical values (for example 50). Instead, refer to the existing variable BEAN_SEED_SPACING. You can also name these constants differently if you like. Write the following function in your program:

- _calculate_number_of_seeds(x, y, germination_rate, row_spacing, seed_spacing)_
  - The function calculates the number of seeds that are needed to fill the field area.
  - The function has the following parameters:
    - x: int - the width of the field (cm)
    - y: int - the height of the field (cm)
    - germination_rate: float - the germination rate in percentages
    - row_spacing: int - the row spacing (cm)
    - seed_spacing: int - the seed spacing (cm)
  - The function returns the following:
    - The number of seeds needed as an integer.
  - Note: You need to calculate the number of seeds so that the rows are perpendicular to the length x of the field!
  - Also, take the germination rate into account in the calculations. For example, if the germination rate is 10.0 % and there is room for 100 plants in the field, 1000 seeds are needed to fill the field area.
    
In addition, write a main function that communicates with the user, asks for the inputs and prints the results. Also, note that all the print- and input-commands must be inside the main function. The main function asks for the width and height of the field first. Then, it asks for the species that the user wants to grow. After that, it asks for the germination rate. All the inputs are given as integers except the germination rate. Finally, the main function prints the right direction of the rows and the number of seeds needed. You can learn more about the execution and output of the program from examples below.
    

**Error handling**

You can assume that the functions you write in the program are only given reasonable values as parameters (for example, the given values are non-negative). You can expect the user to give an integer between 1 - 3 when asked for the species, a decimal number as a germination rate and integer otherwise. The given germination rate value is greater than 0.0 but at most 100.0.

**Output of the program**

Pay close attention that the output of your program is the same as the output in the example executions below. The number of seeds is printed as an integer.

**Tips**

- You are not supposed to calculate anything in the main function. 
All the calculations are executed inside the function `calculate_number_of_seeds`.
- You can call the function `calculate_number_of_seeds` more than once to find out the 
right direction of the rows. Pay attention to how to place the width and height parameters when calling the function to get the desired output.
- Use integer division denoted as `//` when calculating the number of rows and the number of seeds in a row. Integer division is division in which the decimals (remainder) are discarded.
- Use always centimeters as integers to avoid rounding errors.
- If you have a decimal value stored in variable `figure`, you can obtain the corresponding 
- integer value by writing `int(figure)`.


**Examples of the return value of the function:**

```
[Same values as in the 1. example of the execution of the program.]
calculate_number_of_seeds(300, 500, 90.0, 50, 15)
220
calculate_number_of_seeds(500, 300, 90.0, 50, 15)
222
```


**Examples of the execution of the program:**

```
[execution of the program begins]
This program calculates the number of seeds that you need.
Enter the width of the field (cm):
300
Enter the height of the field (cm):
500
Which vegetable do you want to grow?
1. Beans
2. Radishes
3. Carrots
1
Enter the germination rate of the seeds (%):
90.0
Set the rows perpendicular to the height (500 cm) of the field to get maximum harvest.
You need 222 seeds.
[execution of the program ends]
[execution of the program begins]
This program calculates the number of seeds that you need.
Enter the width of the field (cm):
250
Enter the height of the field (cm):
98
Which vegetable do you want to grow?
1. Beans
2. Radishes
3. Carrots
2
Enter the germination rate of the seeds (%):
80.0
Set the rows perpendicular to the width (250 cm) of the field to get maximum harvest.
You need 360 seeds.
[execution of the program ends]
[execution of the program begins]
This program calculates the number of seeds that you need.
Enter the width of the field (cm):
370
Enter the height of the field (cm):
370
Which vegetable do you want to grow?
1. Beans
2. Radishes
3. Carrots
3
Enter the germination rate of the seeds (%):
97.0
Set the rows perpendicular to either the height or to the width of the field to get maximum harvest.
You need 2288 seeds.
[execution of the program ends]
```

## Exercise 4 <a name="exercise-4"></a>

**Description of the task**

Write a program that calculates how much the electrical devices heat the room air and the total cost of the consumed electricity.

**Structure of the program**

Write the following functions in your program:

- _calculate_warming(power, time, device_type, room_size)_
  - Function gets the following values as parameters in the following order:
    - _power: float_ - average power of the device in watts
    - _time: int_ - usage time of the device in minutes
    - _device_type: str_ - device type, which is `computer`, `lights`, `oven` or `washing machine`
    - _room_size: float_ - room size in cubic meters
  - Function calculates the change of the temperature in Celsius degrees according to the equation below and returns it.
  - If the device type is invalid, time or power is negative, the function returns the value -99.
- _calculate_costs(power, time)_
  - Function gets the average power of the device in watts and time in minutes as parameters
  - Function calculates and returns the total cost of the electricity in cents (i.e. the cost of all electricity used, not just the electricity consumed on heating)
  
Write also a main function, which communicates with the users.
  
**Progression of the program**

First the program asks the user for the room size in cubic meters (decimal number), the device type (computer, lights, oven or washing machine), the average power of the device in watts (decimal number) and the usage time of the device in minutes (integer). Next the program asks if the user wants to continue. If the user wants to continue, the program asks for a new device until the user enters another answer than "yes". Finally the program prints the increase of the temperature and the total cost of the consumed electricity in cents.

**Required formula and constants**

A part of the electricity used by devices is transformed into heat, which increases the 
temperature of the room. Assuming that all produced heat remains in the room air and not 
escape e.g. through the ventilation, the change of the temperature can modeled as 
follows: `ΔT = k * P * t / (c * rho * V)`, where k is a specific factor for each device, c a specific heat capacity of air (J/(kg*celsius)), P the average power (W), t time (s), rho air density (kg/m3) and V volume of the room (m3). The factor k describes how much of the energy is converted eventually into heat. The devices used in this task are computer, lights, oven or washing machine and we use k 92 % for computer, 90 % for lights, 95 % for oven and 80 % for washing machine.

The electricity cost of a device is calculated by multiplying the costs per kWh by the average power (kW) and the usage time (h) of the device. The cost per kWh is 9.89 cents in this task.

You will need the following constants in this exercise. You can copy these directly to the start of your code:

```
AIR_DENSITY = 1.225 # kg/m3
SPECIFIC_HEAT_CAPACITY_AIR = 1012 # J/(kg*celcius)
COMPUTER_HEATING_RATIO = 0.92
LIGHTS_HEATING_RATIO = 0.90
OVEN_HEATING_RATIO = 0.95
WASHING_MACHINE_HEATING_RATIO = 0.8
ERROR_WITH_WARMING = -99
KWH_PRICE = 9.89 # cents/kWh
```

**Error handling**

You can assume that the user enters only a positive decimal number for the room size. 
If the user enters an invalid device, negative power or time, the program prints `Invalid input.` 
However, the program prints `Invalid input.` when all the values are asked from the user (i.e. the program does not check the values after each input).

**Output formatting**

The increase of the temperature and the total cost of the consumed electricity are printed with the precision of 2 decimal and make sure that the program output matches the model output below.

**Tips**

- The functions have to be defined in the same way as described. For example, do not change the names of the parameters or their order. Otherwise, A+ does not assess your program correctly.
- Main function communicates with the user i.e. all print-inputs have to be in the main function
- The program calculates the total costs of the electricity, not just the electricity consumed on heating

**Examples of the functions return values:**

```
calculate_warming(80.0, 200, "computer", 200.0)
3.5621521335807054
calculate_warming(2000.0, 120, "oven", 220.0)
50.15876275051882
calculate_warming(100.0, 20, "COMPUTER", 220.0)
-99
calculate_costs(80.0, 120)
1.5824
```


**Examples of the execution of the program:**

```
[execution of the program begins]
Enter the size of the room (m3).
200.0
Enter the device type (computer, lights, oven or washing machine).
oven
Enter the power of the device (W).
3800.0
Enter time of use (min).
100
Do you want to enter another device (yes or no)?
no
The electric devices heat the room by 87.36 degrees and it costs 62.64 cents.
[execution of the program ends]
[execution of the program begins]
Enter the size of the room (m3).
210.0
Enter the device type (computer, lights, oven or washing machine).
computer
Enter the power of the device (W).
100.0
Enter time of use (min).
180
Do you want to enter another device (yes or no)?
yes
Enter the device type (computer, lights, oven or washing machine).
lights
Enter the power of the device (W).
-54.0
Enter time of use (min).
240
Invalid input.
Do you want to enter another device (yes or no)?
yes
Enter the device type (computer, lights, oven or washing machine).
dishwasher
Enter the power of the device (W).
1800.0
Enter time of use (min).
125
Invalid input.
Do you want to enter another device (yes or no)?
yes
Enter the device type (computer, lights, oven or washing machine).
washing machine
Enter the power of the device (W).
2100.0
Enter time of use (min).
130
Do you want to enter another device (yes or no)?
no
The electric devices heat the room by 54.15 degrees and it costs 47.97 cents. 
[execution of the program ends]
```

# ROUND 3, More about control statements

The concept of this round is about the for-loop, range()-function,
and formatted output. 

The description of the exercises are given below:
1. [Exercise 1](#exercise-1)
2. [Exercise 2](#exercise-2)
3. [Exercise 3](#exercise-3)
4. [Exercise 4](#exercise-4)

## Exercise 1 <a name="exercise-1"></a>

Write a simple program to represent bottle recycling. 
The program asks for an integer corresponding to bottle type until the user gives a negative number. 
After that, the program prints the money earned from bottles in euros and cents.

Bottle types and the corresponding integers used in this exercise:
- can: 0
- glass bottle: 1 
- plastic bottle (0.33l): 2 
- plastic bottle (0.5l): 3 
- plastic bottle (1.5l): 4 
- no-deposit bottle: 5

Bottle deposits:
- can: 15 cents 
- glass bottle: 10 cents 
- plastic bottle (0.33l): 10 cents 
- plastic bottle (0.5l): 20 cents 
- plastic bottle (1.5l): 40 cents 
- no-deposit bottle: 0 cents
- 
The values above are written as constants at the beginning of the given code. So, do not write the numerical values in
your code again, but rather refer to the existing variables.

## Exercise 2 <a name="exercise-2"></a>

Write a program that calculates the compensation to be paid for a broken smart device, 
when the user inputs the value of the device and the year of the purchase. The compensation is determined by subtracting the deductible and the age reduction from the value of the device. The deductible is fixed and it is 150 euros. The age reduction is 25 % from the value of the device per each year of use, but it is not more than 70 %. You can assume that the device is broken in year 2021. For example, if the device has been bought in the year 2019, the years of use is two, with the age reduction of 50%. 
The insurance's maximum coverage is 2500 euros.

## Exercise 3 <a name="exercise-3"></a>

There is a time bomb in this exercise, and it can be defused by guessing a right number between 0 and 1000. Write a program in which the user has to defuse the bomb before it explodes.

**Progression of the program**

The program generates a number between 0 and 1000 with a random number generator. 
The user has to guess this number before they run out of guesses 
(if the number is too big, the program prints `The number is smaller.` 
and if the suggested number is too small, the program prints 
`The number is bigger.` If the user enters a number that is less than 0 or greater than 1000, 
the program prints `The number is between 0 and 1000.` 
The program asks for a new guess until the user enters the correct number
or runs out of guesses. The user does not know how many guesses they have left, 
because the program also generates the number of guesses (in range 7 and 20) with a random number generator. 
However, when there is only one guess left, the program prints 
`You have 1 guess left!` If the user enters the right number before running out of guesses, 
the program prints `You found the right number in time!` 
But if the guess limit is reached and the user has not entered the right number, 
the program prints `KABOOM!` and `You didn't find the right number in time` and 
the bomb exploded. At the end, the program reveals the right number.

## Exercise 4 <a name="exercise-4"></a>

**Initial preparations**

Given code template

```
def main():
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment    = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment  = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years                 = float(input("For how many years are you planning to hold the investment?\n"))

    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year','Month','Start','Monthly', 'End', 'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('','','balance','Profit', 'balance','Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('','',e,e,e,e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    # There are 12 months in a year; let's divide the exponential growth to them expecting it to be constant:
	monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1

    # Write your code here

main()
```

**Description of the exercise**

To the code template given above, complete a program that uses the information given by the user to calculate and 
tabulate the monthly profits of their investment.

**Progression of the program**

1. The program asks the user for the essential values (this is ready implemented in the code given above)
2. The program prints a table of the monthly returns. For each month, the program prints

    - Numbers of the month and the year in question 
    - The balance at the beginning of the month ("Start balance")
    - The earned profit/return during the month ("Monthly profit")
    - The balance at the end of the month ("End balance")
    - The total profit cumulated during the whole investment at the end of the month ("Cumulative profit")
    
    The program continues printing the table until

    - The investment time given by the user is fulfilled. (If it would be exceeded, the exceeding part is not printed. For instance 3.8 years is exactly 3 year and 9.6 months, which means we would print 3 years and 9 months of the table.)
or
    - The balance would go below zero (this can occur only if the user gave a negative value to the variable per_month_investment, which in that case means the amount they are withdrawing from their investment each month.

3. The program prints the final balance, final total profits and the net deposit amount according to the example runs.


**Financial mathematics**

(You can skip this chapter in case you want to figure out the principles yourself.)

In this exercise we expect exponential growth to be even. 
The monthly growth can be calculated from the annual one by dividing 
the annual growth evenly for each month. 
This can be calculated using the 
formula `monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1` - this is already implemented for you.

As an example, let’s assume the annual growth/profit to be 8%. 
This means that if the value of the investment is `x` at the beginning of the year, 
it is `x + 0.08 * x` i.e. `1.08 * x` at the end of the year (if we ignore the additional investments / withdrawals).

The monthly profit multiplier in this case is some value `m` for which 
`m ** 12 == 1.08`. This can be calculated as `m = 1.08 ** (1 / 12)` 
i.e. by taking the 12th root of the annual growth multiplier. 
In our example case the value of `m` is about 1.0064 which signifies the monthly growth of 0.64 %. 
Now we can easily calculate the monthly profit. 
f the balance is `y` at the beginning of the month, it is `y + m * y` at the end of it. For instance 1000 euros would become 1006.4 euros with this growth rate.

In addition to the absolute balance, we want to examine the profits themselves as well, so we are using profit multipliers. 
In this case, the formula is otherwise the same except, 
due to adding and subtracting 1's, 
it gets the form `m = (1 + a) ** (1 / 12) - 1` where a is the annual growth rate (eg. 8% ie. 0.08) and m is the monthly one (eg. 0.64% ie. 0.064).

The actual profit depends on the timing of the additional investment / withdrawal. In this exercise we assume the monthly investment / withdrawal to be made at the very end of the month. This means it is added to / subtracted from the balance after it has already grown due to the interest.

Cumulative profit means the total profit at that point.

You can find example computations from the example runs.

**Output formatting**

- The fields "Year" and "Month" are printed in columns of 5 characters wide and all other fields in those of 10 characters.
  - As in the code template above, there are also the characters "space bar, vertical bar, space bar" ie. " | " between all fields.
- In the last 3 printed rows of the program, the text is printed in fields 20 characters wide and the monetary amounts in fields 10 characters wide.
  - There are no spaces between the fields.
- All monetary amounts are printed with the precision of 2 decimals.
- Note that in Python, by default, text is aligned to the left and numbers to the right.
- In the template, the caret (ie. the character ^) aligns to the center. You do not need to use it in your program.

Pay close attention that the output of your program is the same as the output in the example executions below. Line breaks and space bars matter in this exercise!
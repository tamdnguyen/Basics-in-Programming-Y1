import random

def main():
    MIN_NUMBER = 0
    MAX_NUMBER = 1000
    MIN_GUESSES = 7
    MAX_GUESSES = 20

    # Generate the random number and the number of guesses
    seed_number = int(input("Enter a seed:\n"))
    random.seed(seed_number)
    right_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guesses_left = random.randint(MIN_GUESSES, MAX_GUESSES)

    # Implement your code here.
    guess = int(input("Enter your guess:\n"))
    guesses_left -= 1

    while True:
        if guess < 0 or guess > 1000:
            print("The number is between 0 and 1000.")
            if guesses_left == 1:
                print("You have 1 guess left!")
            guess = int(input("Enter the next guess:\n"))
            guesses_left -= 1
        elif guess < right_number:
            print("The number is bigger.")
            if guesses_left == 1:
                print("You have 1 guess left!")
            guess = int(input("Enter the next guess:\n"))
            guesses_left -= 1
        elif guess > right_number:
            print("The number is smaller.")
            if guesses_left == 1:
                print("You have 1 guess left!")
            guess = int(input("Enter the next guess:\n"))
            guesses_left -= 1
        elif guess == right_number:
            print("You found the right number in time!")
            print("The right number was %i." % right_number)
            break

        if guesses_left == 0 and guess != right_number:
            print("KABOOM!")
            print("You didn't find the right number in time and the bomb exploded.")
            print("The right number was %i." % right_number)
            break

main()
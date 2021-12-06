def main():
    age = int(input("Enter your age.\n"))
    weight = float(input("Enter your weight in kilograms.\n"))
    height = float(input("Enter your height in centimeters.\n"))
    answer = str(input("Has your parent or sibling been diagnosed with type 1 or type 2 diabetes? Enter yes or no.\n"))

    score = 0
    bmi = weight / ((height/100)*(height/100))

    # print(bmi)
    # print(score)
    # print()

    if age < 45:
        score += 0
    elif 45 <= age <= 54:
        score += 2
    elif 55 <= age <= 64:
        score += 3
    elif age >= 65:
        score += 4
    # print(score)
    # print()

    if bmi < 25:
        score += 0
    elif 25 <= bmi <= 30:
        score += 1
    elif bmi > 30:
        score += 2
    # print(score)
    # print()

    if answer == "yes":
        score += 5
    # print(score)
    # print()

    if score == 0:
        print("You have a low risk of getting type 2 diabetes.")
    elif 1 <= score < 5:
        print("You have a moderate risk of getting type 2 diabetes.")
    else:
        print("You have a high risk of getting type 2 diabetes.")

    # print(score)
    # print()

main()
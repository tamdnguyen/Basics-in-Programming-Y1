def main():
    speed = input("Enter your speed in km/h:\n")
    speed = int(speed)
    if speed >= 45:
        print("Oh no, better prepare yourself for a fine.")
    else:
        print("You should be all good.")

main()
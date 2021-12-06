def find_median(number1, number2, number3):
    if number1 <= number2 <= number3:
        return number2
    elif number3 <= number2 <= number1:
        return number2
    elif number2 <= number1 <= number3:
        return number1
    elif number3 <= number1 <= number2:
        return number1
    elif number1 <= number3 <= number2:
        return number3
    elif number2 <= number3 <= number1:
        return number3


def median_filter(signal):
    filtered_signal = [0.0] * len(signal)
    for i in range(len(signal)):
        if i == 0 or i == len(signal) - 1:
            filtered_signal[i] = signal[i]
        else:
            filtered_signal[i] = find_median(signal[i-1], signal[i], signal[i+1])
    return filtered_signal


def main():
    signal = []
    print("Enter the data points of the signal. Stop with empty line.")

    while True:
        num = input()

        if num == "":
            break
        else:
            signal.append(float(num))

    print("The original signal is ", signal)
    print("The median filtered signal is", median_filter(signal))


main()
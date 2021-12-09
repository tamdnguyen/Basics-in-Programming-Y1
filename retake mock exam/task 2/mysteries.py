'''
Task 2a
The function gets a speed in km/h (integer) as parameter.
Based on the speed, it should print out if the driver gets a fine (according to old law).
The driver gets a fine if the speed is over 7 km/h speed limit that is 60 km/h,
i.e. when the speed is at least 67 km/h, one gets a fine. The
function does not work correctly, please fix it.
'''
def mystery1(speed):
    print("Your speed was", speed, "km/h.")
    if speed >= 67:
        print("Oh no, better prepare yourself for a fine.")
    elif speed < 0:
        print("Negative speed is not possible.")
    else:
        print("You should be all good.")

'''
Task 2b 
The first parameter of this function is a list of positive integers. The task of
the function is to check whether all the numbers of the lists are divisible with
the number that is given as the second parameter (it is a positive integer, too).
The function does not work correctly, please fix it.
'''
def mystery2(list1, number):
    i = 0
    while i < len(list1):
        if list1[i] % number != 0:
            return False
        else:
            i += 1
    return True

'''
Task 2c 
The following function gets two equally long strings. It should
return a new string with an alternate character from each string,
starting with the first character from the first string,
then the first character form the second string,
then the second character of the first string etc, until the end of strings.
The function dos not work correctly. Fix the function.
'''

def mystery3(str1, str2):
    result = ""
    for i in range(len(str1)):
        result += str1[i] + str2[i]

    return result

'''
Task 2d 
The following function gets two equally long lists that contain integers. It should
sum up all those numbers of the first list that are bigger than those at the same
place in the second list (i.e. with the same index). It does not do that. Fix the function.
'''

def mystery4(list1, list2):
    i = 0
    result = 0
    while i < len(list1):
        if list1[i] > list2[i]:
            result = result + list1[i]
        i += 1

    return result

'''
For testing, you can add your own code below. It will not be used in the grading.
'''

def main():
    print("2a)")
    mystery1(68)
    print()

    print("2b)")
    print("This should work:", mystery2([2,4,6,8], 2))
    print("This should fail:", mystery2([2,3,4,5],2))
    print()

    print("2c)")
    print("Results should be 'abcdefgh'. Your result is following:", mystery3("aceg", "bdfh"))
    print()

    print("2d)")
    print("Result should be 10. Your result is following:", mystery4([1,4,9],[0,5,8]))
    print()


main()




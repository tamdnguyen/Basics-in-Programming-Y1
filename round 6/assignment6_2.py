VOWELS = ['a', 'e', 'i', 'u', 'o', 'y']


def sort_letters(name):
    consonant_list = []
    vowel_list = []

    for character in name:
        character = character.lower()
        if character != " ":
            if character in VOWELS:
                vowel_list.append(character)
            else:
                consonant_list.append(character)

    return consonant_list, vowel_list


def main():
    name = input("Enter your name.\n")
    name = name.strip()

    consonant_list, vowel_list = sort_letters(name)

    if len(consonant_list) >= 3 and len(vowel_list) >= 3:
        nickname = consonant_list[-1].upper() + vowel_list[-1] \
                   + consonant_list[-2] + vowel_list[-2] \
                   + consonant_list[-3] + vowel_list[-3]
        if nickname == name:
            print("Not able to generate a nickname.")
        else:
            print("Your nickname:", nickname)
    elif len(consonant_list) >= 2 and len(vowel_list) >= 2:
        nickname = consonant_list[-1].upper() + vowel_list[-1] \
                   + consonant_list[-2] + vowel_list[-2]
        if nickname == name:
            print("Not able to generate a nickname.")
        else:
            print("Your nickname:", nickname)
    else:
        print("Not able to generate a nickname.")


main()
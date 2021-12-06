def ask_user_input():
    print("""Choose 1-5.
1: Add a new movie and rating.
2: Change the rating of the movie.
3: Print all movies and their ratings.
4: Find all movies with a specific rating.
5: Exit.""")
    new_action = int(input())

    return new_action


def add_new_movie_and_rating(dictionary, movie, rating):
    if movie in dictionary:
        return False
    else:
        dictionary[movie] = rating
        return True


def change_rating(dictionary, movie, rating):
    if movie in dictionary:
        dictionary[movie] = rating
        return True
    else:
        return False


def print_all_movies(dictionary):
    for movie in sorted(dictionary):
        print("{:s} {:d}".format(movie, dictionary[movie]))

    print()


def find_movies_with_rating(dictionary, rating):
    list_movie = []
    for movie in dictionary:
        if dictionary[movie] == rating:
            list_movie.append(movie)

    return list_movie


def main():
    print("Welcome to the database of the movie ratings.\n")
    action = ask_user_input()
    while action > 5:
        print("You chose an invalid number.\n")
        action = ask_user_input()
    dictionary = {}
    while action != 5:
        print()
        if action == 1:
            movie = input("Enter the movie.\n")
            rating = int(input("Enter the rating (4-10).\n"))
            if not add_new_movie_and_rating(dictionary, movie, rating):
                print("{:s} is already in the database. Choose 2 if you want to change the rating of the movie.\n".format(movie))
            else:
                print("{:s} has been added into the database.\n".format(movie))
        elif action == 2:
            movie = input("Enter the movie.\n")
            rating = int(input("Enter the new rating (4-10).\n"))
            if change_rating(dictionary, movie, rating):
                print("The rating of {:s} has been changed.".format(movie))
            else:
                print("{:s} is not in the database. Choose 1 if you want to add the movie.".format(movie))
        elif action == 3:
            print("The movies in the database:")
            print_all_movies(dictionary)
        elif action == 4:
            rating = int(input("Enter the rating.\n"))

            list_movie = find_movies_with_rating(dictionary, rating)
            if len(list_movie) != 0:
                for movie in list_movie:
                    print(movie)
            else:
                print("There are no movies with rating {:d} in the database.".format(rating))
            print()
        action = ask_user_input()
        while action > 5:
            print("You chose an invalid number.\n")
            action = ask_user_input()


main()


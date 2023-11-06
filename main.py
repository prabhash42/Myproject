import myFunctions


def print_menu():
    print("********** Movie Finder App **********")
    print("1. Get Actor or Director Filmography")
    print("2. Show Top Rated Movies by Year")
    print("3. Get Movie Details by Title")
    print("4. Quit")
    print("**************************************")


def get_user_choice():
    try:
        return int(input("Enter an option (1, 2, 3, or 4): "))
    except ValueError:
        return None


def main():
    print("Welcome to the Movie Finder App!")
    print("Discover filmographies, find top rated movies, and explore movie details.\n")

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 1:
            person_id = myFunctions.search_person()
            if person_id:
                myFunctions.get_person_filmography(person_id)
        elif choice == 2:
            myFunctions.show_top_rated_movies_by_year()  # Assuming you have implemented this function
        elif choice == 3:
            myFunctions.get_movie_details_by_title()
        elif choice == 4:
            print("Thank you for using the Movie Finder App. Goodbye!")
            break
        else:
            print("Invalid selection, please choose a valid option.")


if __name__ == "__main__":
    main()

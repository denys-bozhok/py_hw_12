from utilies import greeting, get_menu, all_films_list, get_film_by_name, get_sorted_arr
from database import user, menu_list, films
from errors import *


def main():
    print(greeting.gritting(user["name"]))

    get_menu.get_menu(menu_list[0])

    is_running = True

    while is_running:
        user_choose_of_menu_list = 0

        try:
            user_choose_of_menu_list = int(input("\nPlease enter number of menu list\n"))
        except:
            print(incorrect_data)
            get_menu.get_menu(menu_list[0])

        match(user_choose_of_menu_list):

            case 1:
                shaw_films = True

                while shaw_films:
                    get_menu.get_menu(menu_list[1])

                    user_choose_of_all_films_menu = input("Show list of films or back?\n")

                    if user_choose_of_all_films_menu == "2":
                        get_menu.get_menu(menu_list[0])
                        shaw_films = False

                    elif user_choose_of_all_films_menu == "1":
                        all_films_list.shaw_all_films(films)
                        is_running, shaw_films = False, False

                    else:
                        print(incorrect_data)

            case 2:
                get_film_by_name.get_film_by_name(films, incorrect_data)

                is_running = False

            case 3:
                get_sorted_arr.get_sorted_list(films)

                shaw_films = True

                while shaw_films:
                    i = 0

                    for el in menu_list[3]:
                        print(f"{i + 1}) {el}".upper())
                        i += 1

                    try:
                        choose_type_of_sorted = int(input("\nEnter number of sorted type :\n"))
                    except:
                        print(incorrect_data)

                        continue

                    if choose_type_of_sorted == 1:
                        upper_list = get_sorted_arr.get_sorted_list(films)

                        get_sorted_arr.shaw_choose_of_type_sorted(upper_list)

                        is_running = False
                        shaw_films = False

                    elif choose_type_of_sorted == 2:
                        lower_list = reversed(get_sorted_arr.get_sorted_list(films))

                        get_sorted_arr.shaw_choose_of_type_sorted(lower_list)

                        is_running = False
                        shaw_films = False

                    else:
                        print(f"{incorrect_data}")

            case 4:
                print("Goodbye!".upper())
                is_running = False
            case _:
                pass


if __name__ == "__main__":
    main()

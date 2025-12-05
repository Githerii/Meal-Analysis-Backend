from lib.helpers import (
    banner,
    create_user, list_users, find_user, delete_user, view_user_favorites, add_favorite,
    create_meal, list_meals, find_meal, delete_meal,
    create_ingredient, list_ingredients, find_ingredient, delete_ingredient,
)

def main_menu():
    banner("Meal Analysis CLI")
    print("1. Users")
    print("2. Meals")
    print("3. Ingredients")
    print("0. Exit")
    return input("> ")

def users_menu():
    banner("Users Menu")
    print("1. Create User")
    print("2. List Users")
    print("3. Find User by ID")
    print("4. Delete User")
    print("5. View User Favorites")
    print("6. Add Favorite Meal")
    print("0. Back")
    return input("> ")

def meals_menu():
    banner("Meals Menu")
    print("1. Create Meal")
    print("2. List Meals")
    print("3. Find Meal by ID")
    print("4. Delete Meal")
    print("0. Back")
    return input("> ")

def ingredients_menu():
    banner("Ingredients Menu")
    print("1. Create Ingredient")
    print("2. List Ingredients")
    print("3. Find Ingredient by ID")
    print("4. Delete Ingredient")
    print("0. Back")
    return input("> ")

def main():
    while True:
        choice = main_menu()

        if choice == "1":
            while True:
                c = users_menu()
                if c == "1": create_user()
                elif c == "2": list_users()
                elif c == "3": find_user()
                elif c == "4": delete_user()
                elif c == "5": view_user_favorites()
                elif c == "6": add_favorite()
                elif c == "0": break

        elif choice == "2":
            while True:
                c = meals_menu()
                if c == "1": create_meal()
                elif c == "2": list_meals()
                elif c == "3": find_meal()
                elif c == "4": delete_meal()
                elif c == "0": break

        elif choice == "3":
            while True:
                c = ingredients_menu()
                if c == "1": create_ingredient()
                elif c == "2": list_ingredients()
                elif c == "3": find_ingredient()
                elif c == "4": delete_ingredient()
                elif c == "0": break

        elif choice == "0":
            banner("KWAHERI YA KUONANA!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()

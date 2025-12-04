from db import Base, engine
from helpers import (
    create_user, list_users, find_user_by_id, delete_user, view_user_favorites, add_favorite,
    create_meal, list_meals, find_meal_by_id, delete_meal, view_meal_ingredients, add_ingredient_to_meal,
    create_ingredient, list_ingredients, find_ingredient_by_id, delete_ingredient
)

Base.metadata.create_all(bind=engine)


def main_menu():
    print("\n===== MAIN MENU =====")
    print("1. Users")
    print("2. Meals")
    print("3. Ingredients")
    print("0. Exit")
    return input("> ").strip()


def users_menu():
    print("\n----- USERS MENU -----")
    print("1. Create User")
    print("2. List Users")
    print("3. Find User by ID")
    print("4. Delete User")
    print("5. View User Favorites")
    print("6. Add Favorite Meal")
    print("0. Back")
    return input("> ").strip()


def meals_menu():
    print("\n----- MEALS MENU -----")
    print("1. Create Meal")
    print("2. List Meals")
    print("3. Find Meal by ID")
    print("4. Delete Meal")
    print("5. View Meal Ingredients")
    print("6. Add Ingredient to Meal")
    print("0. Back")
    return input("> ").strip()


def ingredients_menu():
    print("\n----- INGREDIENTS MENU -----")
    print("1. Create Ingredient")
    print("2. List Ingredients")
    print("3. Find Ingredient by ID")
    print("4. Delete Ingredient")
    print("0. Back")
    return input("> ").strip()


def run_users_menu():
    while True:
        choice = users_menu()
        if choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            find_user_by_id()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            view_user_favorites()
        elif choice == "6":
            add_favorite()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def run_meals_menu():
    while True:
        choice = meals_menu()
        if choice == "1":
            create_meal()
        elif choice == "2":
            list_meals()
        elif choice == "3":
            find_meal_by_id()
        elif choice == "4":
            delete_meal()
        elif choice == "5":
            view_meal_ingredients()
        elif choice == "6":
            add_ingredient_to_meal()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def run_ingredients_menu():
    while True:
        choice = ingredients_menu()
        if choice == "1":
            create_ingredient()
        elif choice == "2":
            list_ingredients()
        elif choice == "3":
            find_ingredient_by_id()
        elif choice == "4":
            delete_ingredient()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


def main():
    print("Welcome to the Meal Analysis CLI!")
    while True:
        choice = main_menu()
        if choice == "1":
            run_users_menu()
        elif choice == "2":
            run_meals_menu()
        elif choice == "3":
            run_ingredients_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

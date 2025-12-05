from lib.db.models import User, Meal, Ingredient, MealIngredient, Favorite
from sqlalchemy.orm import joinedload

# Color codes za project CLI
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"

def banner(title):
    """Pretty banner header."""
    width = 60
    print("\n" + CYAN + "=" * width + RESET)
    print(CYAN + f"{title.upper():^{width}}" + RESET)
    print(CYAN + "=" * width + RESET + "\n")

def print_table(headers, rows):
    if not rows:
        print(YELLOW + "No data.\n" + RESET)
        return

    # Determine width of each column
    widths = [
        max(len(str(item)) for item in column)
        for column in zip(headers, *rows)
    ]

    # Header
    header = "   ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))
    print(BOLD + CYAN + header + RESET)

    # Divider
    print(CYAN + "-" * (sum(widths) + 3 * (len(headers) - 1)) + RESET)

    # Rows
    for row in rows:
        print("   ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))))

    print()

def create_user():
    name = input("Enter username: ")
    try:
        user = User.create(name)
        print(GREEN + f"✔ User created: {user.name}" + RESET)
    except Exception as e:
        print(RED + f"✖ Error: {e}" + RESET)

def list_users():
    users = User.get_all()
    banner("Users")

    rows = [(u.id, u.name) for u in users]
    print_table(["ID", "Name"], rows)

def find_user():
    try:
        id_ = int(input("Enter ID: "))
        user = User.find_by_id(id_)
        if user:
            banner(f"User {id_}")
            rows = [(user.id, user.name)]
            print_table(["ID", "Name"], rows)
        else:
            print(YELLOW + "User not found." + RESET)
    except:
        print(RED + "Invalid ID." + RESET)

def delete_user():
    try:
        id_ = int(input("Enter ID to delete: "))
        if User.delete(id_):
            print(GREEN + "✔ User deleted." + RESET)
        else:
            print(YELLOW + "User not found." + RESET)
    except:
        print(RED + "Invalid ID." + RESET)

def view_user_favorites():
    try:
        user_id = int(input("Enter User ID: "))
    except:
        print(RED + "Invalid ID." + RESET)
        return

    banner(f"Favorites for User {user_id}")

    favs = Favorite.find_for_user(user_id)

    if not favs:
        print(YELLOW + "No favorites found." + RESET)
        return

    rows = [(f.meal_id, f.meal.name) for f in favs]
    print_table(["Meal ID", "Meal Name"], rows)

def add_favorite():
    try:
        user_id = int(input("User ID: "))
        meal_id = int(input("Meal ID: "))
        fav = Favorite.create(user_id, meal_id)
        print(GREEN + f"✔ Favorite added" + RESET)
    except:
        print(RED + "Could not add favorite. Check IDs." + RESET)

def create_meal():
    name = input("Meal name: ")
    calories = input("Calories: ")
    calories = int(calories) if calories.isdigit() else None

    try:
        meal = Meal.create(name=name, calories=calories)
        print(GREEN + f"✔ Meal created: {meal.name}" + RESET)
    except Exception as e:
        print(RED + f"✖ Error: {e}" + RESET)

def list_meals():
    meals = Meal.get_all()
    banner("Meals")

    rows = [(m.id, m.name, m.calories) for m in meals]
    print_table(["ID", "Name", "Calories"], rows)

def find_meal():
    try:
        id_ = int(input("Enter Meal ID: "))
        meal = Meal.find_by_id(id_)
        if meal:
            banner(f"Meal {id_}")
            rows = [(meal.id, meal.name, meal.calories)]
            print_table(["ID", "Name", "Calories"], rows)
        else:
            print(YELLOW + "Meal not found." + RESET)
    except:
        print(RED + "Invalid ID." + RESET)

def delete_meal():
    try:
        id_ = int(input("Enter Meal ID to delete: "))
        if Meal.delete(id_):
            print(GREEN + "✔ Meal deleted." + RESET)
        else:
            print(YELLOW + "Meal not found." + RESET)
    except:
        print(RED + "Invalid ID." + RESET)

def create_ingredient():
    name = input("Ingredient name: ")
    try:
        ing = Ingredient.create(name)
        print(GREEN + f"✔ Ingredient created: {ing.name}" + RESET)
    except Exception as e:
        print(RED + f"✖ Error: {e}" + RESET)

def list_ingredients():
    ings = Ingredient.get_all()
    banner("Ingredients")

    rows = [(i.id, i.name) for i in ings]
    print_table(["ID", "Name"], rows)

def find_ingredient():
    try:
        id_ = int(input("Enter Ingredient ID: "))
        ing = Ingredient.find_by_id(id_)
        if ing:
            banner(f"Ingredient {id_}")
            rows = [(ing.id, ing.name)]
            print_table(["ID", "Name"], rows)
        else:
            print(YELLOW + "Ingredient not found." + RESET)
    except:
        print(RED + "Invalid ID." + RESET)

def delete_ingredient():
    try:
        id_ = int(input("Enter Ingredient ID: "))
        if Ingredient.delete(id_):
            print(GREEN + "✔ Ingredient deleted." + RESET)
        else:
            print(YELLOW + "Ingredient not found." + RESET)
    except:
        print(RED + "Invalid ID." + RESET)

def list_meal_ingredients():
    try:
        meal_id = int(input("Enter Meal ID: "))
    except:
        print(RED + "Invalid ID." + RESET)
        return

    banner(f"Ingredients for Meal {meal_id}")

    links = MealIngredient.find_for_meal(meal_id)

    if not links:
        print(YELLOW + "No ingredients found for this meal." + RESET)
        return

    rows = [(mi.ingredient.name, mi.quantity) for mi in links]
    print_table(["Ingredient", "Quantity"], rows)

def add_meal_ingredient():
    try:
        meal_id = int(input("Meal ID: "))
        ingredient_id = int(input("Ingredient ID: "))
        qty = input("Quantity: ")
        qty = int(qty) if qty.isdigit() else None
        MealIngredient.create(meal_id, ingredient_id, qty)
        print(GREEN + "✔ Ingredient linked to meal." + RESET)
    except:
        print(RED + "Failed to add ingredient to meal." + RESET)

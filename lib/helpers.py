from db.models import User, Meal, Ingredient, MealIngredient, Favorite


def prompt_int(message):
    """Ask user for an integer; return None if invalid."""
    try:
        return int(input(message))
    except ValueError:
        print("Invalid number. Please try again.")
        return None


def prompt_nonempty(message):
    """Require non-empty input."""
    val = input(message).strip()
    if not val:
        print("Input cannot be empty.")
        return None
    return val


def create_user():
    name = prompt_nonempty("Enter user name: ")
    if not name:
        return
    
    try:
        user = User.create(name=name)
        print(f"✔ User created: {user}")
    except Exception as e:
        print("Error creating user:", e)


def list_users():
    users = User.get_all()
    if not users:
        print("No users found.")
    else:
        for u in users:
            print(u)


def find_user_by_id():
    id_ = prompt_int("Enter user ID: ")
    if id_ is None:
        return
    user = User.find_by_id(id_)
    print(user if user else "User not found.")


def delete_user():
    id_ = prompt_int("User ID to delete: ")
    if id_ is None:
        return
    
    if User.delete(id_):
        print("✔ User deleted.")
    else:
        print("User not found.")


def view_user_favorites():
    id_ = prompt_int("Enter User ID: ")
    if id_ is None:
        return
    
    favs = Favorite.find_for_user(id_)
    if not favs:
        print("User has no favorite meals.")
        return
    
    print(f"Favorites for user {id_}:")
    for fav in favs:
        print(f" - {fav.meal.name} (Meal ID {fav.meal_id})")


def add_favorite():
    user_id = prompt_int("User ID: ")
    meal_id = prompt_int("Meal ID: ")
    if None in (user_id, meal_id):
        return
    
    try:
        fav = Favorite.create(user_id=user_id, meal_id=meal_id)
        print(f"✔ Favorite added: {fav}")
    except Exception as e:
        print("Error adding favorite:", e)


def create_meal():
    name = prompt_nonempty("Meal name: ")
    if not name:
        return

    calories = input("Calories (press Enter if unknown): ").strip()
    calories = int(calories) if calories.isdigit() else None

    instructions = input("Instructions (optional): ").strip()

    try:
        meal = Meal.create(
            name=name,
            calories=calories,
            instructions=instructions or None
        )
        print(f"✔ Meal created: {meal}")
    except Exception as e:
        print("Error creating meal:", e)


def list_meals():
    meals = Meal.get_all()
    if not meals:
        print("No meals found.")
    else:
        for m in meals:
            print(m)


def find_meal_by_id():
    id_ = prompt_int("Meal ID: ")
    if id_ is None:
        return
    meal = Meal.find_by_id(id_)
    print(meal if meal else "Meal not found.")


def delete_meal():
    id_ = prompt_int("Meal ID to delete: ")
    if id_ is None:
        return
    
    if Meal.delete(id_):
        print("✔ Meal deleted.")
    else:
        print("Meal not found.")


def view_meal_ingredients():
    meal_id = prompt_int("Meal ID: ")
    if meal_id is None:
        return
    
    items = MealIngredient.find_for_meal(meal_id)
    if not items:
        print("This meal has no ingredients.")
        return
    
    print(f"Ingredients for meal {meal_id}:")
    for item in items:
        print(f" - {item.ingredient.name}: {item.quantity}")


def add_ingredient_to_meal():
    meal_id = prompt_int("Meal ID: ")
    ingredient_id = prompt_int("Ingredient ID: ")
    quantity = prompt_int("Quantity: ")
    
    if None in (meal_id, ingredient_id, quantity):
        return

    try:
        mi = MealIngredient.create(meal_id, ingredient_id, quantity)
        print(f"✔ Added ingredient: {mi}")
    except Exception as e:
        print("Error adding ingredient:", e)


def create_ingredient():
    name = prompt_nonempty("Ingredient name: ")
    if not name:
        return

    try:
        ing = Ingredient.create(name=name)
        print(f"✔ Ingredient added: {ing}")
    except Exception as e:
        print("Error creating ingredient:", e)


def list_ingredients():
    ings = Ingredient.get_all()
    if not ings:
        print("No ingredients found.")
        return
    
    for ing in ings:
        print(ing)


def find_ingredient_by_id():
    id_ = prompt_int("Ingredient ID: ")
    if id_ is None:
        return
    
    ing = Ingredient.find_by_id(id_)
    print(ing if ing else "Ingredient not found.")


def delete_ingredient():
    id_ = prompt_int("Ingredient ID to delete: ")
    if id_ is None:
        return
    
    if Ingredient.delete(id_):
        print("✔ Ingredient deleted.")
    else:
        print("Ingredient not found.")

from . import engine, Base, Session
from .models import User, Meal, Ingredient, MealIngredient, Favorite
from faker import Faker

def recreate_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def seed():
    session = Session()
    fake = Faker()

    # create users
    alice = User.create(name="Alice")
    bob = User.create(name="Bob")

    # ingredients
    tomato = Ingredient.create(name="Tomato")
    salt = Ingredient.create(name="Salt")
    rice = Ingredient.create(name="Rice")

    # meals
    soup = Meal.create(name="Tomato Soup", calories=150, instructions="Boil tomatoes, blend, add salt")
    rice_meal = Meal.create(name="Rice With Salt", calories=350, instructions="Cook rice, add salt to taste")

    # meal ingredients
    MealIngredient.create(meal_id=soup.id, ingredient_id=tomato.id, quantity=3)
    MealIngredient.create(meal_id=soup.id, ingredient_id=salt.id, quantity=1)
    MealIngredient.create(meal_id=rice_meal.id, ingredient_id=rice.id, quantity=200)
    MealIngredient.create(meal_id=rice_meal.id, ingredient_id=salt.id, quantity=1)

    # favorites
    Favorite.create(user_id=alice.id, meal_id=soup.id)
    Favorite.create(user_id=bob.id, meal_id=rice_meal.id)

    session.close()

if __name__ == "__main__":
    recreate_db()
    seed()
    print("Seed complete")

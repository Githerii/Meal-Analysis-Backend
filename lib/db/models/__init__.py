from .. import Base, Session

# Import all model classes so they register with SQLAlchemy
from .user import User
from .meal import Meal
from .ingredient import Ingredient
from .meal_ingredient import MealIngredient
from .favorite import Favorite

__all__ = [
    "User",
    "Meal",
    "Ingredient",
    "MealIngredient",
    "Favorite",
    "Base",
    "Session"
]

from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, validates
from . import Base, Session

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    favorites = relationship(
        "Favorite",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User id={self.id} name='{self.name}'>"

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("User name cannot be empty")
        return value.strip()

    @classmethod
    def create(cls, name):
        session = Session()
        obj = cls(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        session.close()
        return obj

    @classmethod
    def get_all(cls):
        session = Session()
        res = session.query(cls).all()
        session.close()
        return res

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        res = session.get(cls, id_)
        session.close()
        return res

    @classmethod
    def delete(cls, id_):
        session = Session()
        obj = session.get(cls, id_)
        if not obj:
            session.close()
            return False
        session.delete(obj)
        session.commit()
        session.close()
        return True

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    calories = Column(Integer)
    image = Column(String(255))
    instructions = Column(Text)

    favorites = relationship(
        "Favorite",
        back_populates="meal",
        cascade="all, delete-orphan"
    )

    meal_ingredients = relationship(
        "MealIngredient",
        back_populates="meal",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Meal id={self.id} name='{self.name}' calories={self.calories}>"

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Meal name cannot be empty")
        return value.strip()

    @classmethod
    def create(cls, name, calories=None, image=None, instructions=None):
        session = Session()
        obj = cls(
            name=name,
            calories=calories,
            image=image,
            instructions=instructions,
        )
        session.add(obj)
        session.commit()
        session.refresh(obj)
        session.close()
        return obj

    @classmethod
    def get_all(cls):
        session = Session()
        res = session.query(cls).all()
        session.close()
        return res

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        res = session.get(cls, id_)
        session.close()
        return res

    @classmethod
    def delete(cls, id_):
        session = Session()
        obj = session.get(cls, id_)
        if not obj:
            session.close()
            return False
        session.delete(obj)
        session.commit()
        session.close()
        return True

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    meal_ingredients = relationship(
        "MealIngredient",
        back_populates="ingredient",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Ingredient id={self.id} name='{self.name}'>"

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Ingredient name cannot be empty")
        return value.strip()

    @classmethod
    def create(cls, name):
        session = Session()
        obj = cls(name=name)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        session.close()
        return obj

    @classmethod
    def get_all(cls):
        session = Session()
        res = session.query(cls).all()
        session.close()
        return res

    @classmethod
    def find_by_id(cls, id_):
        session = Session()
        res = session.get(cls, id_)
        session.close()
        return res

    @classmethod
    def delete(cls, id_):
        session = Session()
        obj = session.get(cls, id_)
        if not obj:
            session.close()
            return False
        session.delete(obj)
        session.commit()
        session.close()
        return True

class MealIngredient(Base):
    __tablename__ = "meal_ingredients"
    __table_args__ = (
        UniqueConstraint("meal_id", "ingredient_id", name="uix_meal_ing"),
    )

    id = Column(Integer, primary_key=True)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity = Column(Integer)

    meal = relationship("Meal", back_populates="meal_ingredients")
    ingredient = relationship("Ingredient", back_populates="meal_ingredients")

    def __repr__(self):
        return f"<MealIngredient meal={self.meal_id} ingredient={self.ingredient_id} qty={self.quantity}>"

    @validates("quantity")
    def validate_quantity(self, key, value):
        if value is not None and value < 1:
            raise ValueError("Quantity must be at least 1")
        return value

    @classmethod
    def create(cls, meal_id, ingredient_id, quantity=None):
        session = Session()
        obj = cls(
            meal_id=meal_id,
            ingredient_id=ingredient_id,
            quantity=quantity,
        )
        session.add(obj)
        session.commit()
        session.refresh(obj)
        session.close()
        return obj

    @classmethod
    def find_for_meal(cls, meal_id):
        session = Session()
        res = session.query(cls).filter_by(meal_id=meal_id).all()
        session.close()
        return res

    @classmethod
    def delete(cls, id_):
        session = Session()
        obj = session.get(cls, id_)
        if not obj:
            session.close()
            return False
        session.delete(obj)
        session.commit()
        session.close()
        return True

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)

    user = relationship("User", back_populates="favorites")
    meal = relationship("Meal", back_populates="favorites")

    def __repr__(self):
        return f"<Favorite user={self.user_id} meal={self.meal_id}>"

    @classmethod
    def create(cls, user_id, meal_id):
        session = Session()
        obj = cls(user_id=user_id, meal_id=meal_id)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        session.close()
        return obj

    @classmethod
    def find_for_user(cls, user_id):
        session = Session()
        res = session.query(cls).filter_by(user_id=user_id).all()
        session.close()
        return res

    @classmethod
    def delete(cls, id_):
        session = Session()
        obj = session.get(cls, id_)
        if not obj:
            session.close()
            return False
        session.delete(obj)
        session.commit()
        session.close()
        return True

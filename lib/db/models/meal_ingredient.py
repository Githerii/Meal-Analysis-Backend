from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .. import Base, Session

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

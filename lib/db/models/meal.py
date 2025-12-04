from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship, validates
from .. import Base, Session

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
        if not value.strip():
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

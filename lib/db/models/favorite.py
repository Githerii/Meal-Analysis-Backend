from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import joinedload

from .. import Base, Session

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
        res = session.query(cls).options(joinedload(cls.meal)).filter_by(user_id=user_id).all()
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

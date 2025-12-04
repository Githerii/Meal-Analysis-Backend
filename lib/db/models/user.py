from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from .. import Base, Session

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
        if not value.strip():
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

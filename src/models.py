from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Text, DateTime,Enum as SQLAEnum,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime, date
from enum import Enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120),nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    user_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    created_at: Mapped[datetime]= mapped_column(DateTime(), default=datetime.utcnow )

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="users", uselist=True)
    


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name": self.user_name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "favorites": [favorite.id for favorite in self.favorites] if self.favorites else []
        }

class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    ability: Mapped[str] = mapped_column(String(100),nullable=True)
    base_experience: Mapped[int] = mapped_column(nullable=True)
    generation: Mapped[str] = mapped_column(String(100),nullable=True)
    created_at: Mapped[datetime]= mapped_column(DateTime(), default=datetime.utcnow )

    favorites: Mapped["Favorites"] = relationship(back_populates="pokemons", uselist=True)

    def serialze(self):
        return {
            "id": self.id,
            "name": self.name,
            "ability":self.name,
            "base_expereince": self.base_experience,
            "generation": self.generation,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "favorites": [favorite.id for favorite in self.favorites] if self.favorites else []
        }
class Item(db.Model):
    __tablename__ = 'item'
    id: Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    atributes: Mapped[str] = mapped_column(String(100),nullable=True)
    category: Mapped[str] = mapped_column(String(100),nullable=True)
    created_at: Mapped[datetime]= mapped_column(DateTime(), default=datetime.utcnow )

    favorites: Mapped[list["Favorites"]] = relationship(back_populates="items", uselist=True)

    def serialze(self):
        return {
            "id": self.id,
            "name": self.name,
            "atributes":self.atributes,
            "category": self.category,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "favorites": [favorite.id for favorite in self.favorites] if self.favorites else []
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id: Mapped[int]= mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    pekemon_id: Mapped[int] = mapped_column(ForeignKey('pokemon.id'))
    item_id: Mapped[int] = mapped_column(ForeignKey('item.id'))

    users: Mapped["User"] = relationship(back_populates = "favorites")
    pokemons: Mapped["Pokemon"] = relationship(back_populates = "favorites")
    items: Mapped["Item"] = relationship(back_populates = "favorites")

    def serialze(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "pokemon_id": self.pekemon_id,
            "item_id": self.item_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

from enum import Enum
from typing import Optional

from sqlalchemy import String, ForeignKey, VARCHAR, BigInteger, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates

from db.base import TimeBasedModel, Base


class User(TimeBasedModel):
    class Type(Enum):
        USER = "USER"
        ADMIN = "ADMIN"
        SUPER_USER = "SUPERUSER"

    first_name: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(VARCHAR(100), nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(VARCHAR(100), nullable=True)
    username: Mapped[Optional[str]] = mapped_column(VARCHAR(100), nullable=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)

    # type: # Mapped[Type] = mapped_column(SQLEnum(Type), default=Type.USER)

    @validates('phone_number')
    def validate_phone_number(self):
        phone_number = self.phone_number
        if len(phone_number) == 13:
            raise ValueError("failed simple email validation")
        return phone_number


association_table = Table(
    "association_table",
    Base.metadata,
    Column("category_id", ForeignKey("category.id"), primary_key=True),
    Column("movie_id", ForeignKey("movie.id"), primary_key=True))


class Category(TimeBasedModel):
    __tablename__ = "category"

    name: Mapped[str] = mapped_column(String(), nullable=False)
    movies: Mapped[list["Movie"]] = relationship("Movie", back_populates="category")


class Movie(TimeBasedModel):
    __tablename__ = "movie"

    title: Mapped[str] = mapped_column(String(), nullable=False)
    rating: Mapped[str] = mapped_column(String())
    genre: Mapped[str] = mapped_column(String())
    cast: Mapped[str] = mapped_column(String())
    awards: Mapped[str] = mapped_column(String())
    plot: Mapped[str] = mapped_column(String())
    video_id: Mapped[str] = mapped_column(String())
    director: Mapped[str] = mapped_column(String(), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"), nullable=False)
    category: Mapped["Category"] = relationship("Category", back_populates="movies")

from sqlalchemy.orm import Mapped

from src.database import Base, UUIDMixin


class User(Base, UUIDMixin):
    __tablename__ = "users"

    name: Mapped[str]

from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db


class Answer(db.Model):
    __tablename__ = 'answers'

    pk: Mapped[int] = mapped_column(primary_key=True)
    answer: Mapped[str] = mapped_column(unique=True)

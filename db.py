from sqlmodel import SQLModel, Field, create_engine
from sqlalchemy import Column, Integer, Identity


# database models
class Book(SQLModel, table=True):
    id: int | None = Field(
        default=None, sa_column=Column(Integer, Identity(start=11), primary_key=True)
    )
    title: str
    author: str
    year: int | None = None
    genre: str | None = None
    pages: int | None = None
    rating: float | None = None


class BookCreate(SQLModel):
    title: str
    author: str
    year: int | None = None
    genre: str | None = None
    pages: int | None = None
    rating: float | None = None


class BookUpdate(SQLModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    genre: str | None = None
    pages: int | None = None
    rating: float | None = None


# init database connection:
DB_USER = "yamahdi"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_PORT = 5432
DB_DATABASE_NAME = "fastpost"

engine = create_engine(
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE_NAME}",
    echo=True,
)


# create db in a function to avoid side effects
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()

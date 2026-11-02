from sqlmodel import SQLModel, Field, create_engine
from sqlalchemy import Column, Integer, Identity
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # env vars and their types
    db_user: str | None = None
    db_passwd: str = ""
    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_database_name: str = "fastpost"

    # Tell Pydantic to read from a .evn file
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


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
DB_USER = settings.db_user
DB_PASSWORD = settings.db_passwd
DB_HOST = settings.db_host
DB_PORT = settings.db_port
DB_DATABASE_NAME = settings.db_database_name

engine = create_engine(
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{
        DB_HOST}:{DB_PORT}/{DB_DATABASE_NAME}",
    echo=True,
)


# create db in a function to avoid side effects
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()

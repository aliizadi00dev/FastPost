from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from . db import Book, engine, create_db_and_tables, BookCreate, BookUpdate
from sqlmodel import Session, select


@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    create_db_and_tables()

    yield
    # on shutdown
    print("FastPost is shutting down!!")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return "Hello to FastPost project"


# READ all books (GET)
@app.get("/books")
def get_books():
    books = []
    with Session(engine) as session:
        statement = select(Book)
        books = session.exec(statement).all()

    return books


# CREATE new book (POST)
@app.post("/books")
def add_book(book: BookCreate):
    with Session(engine) as session:
        db_book = Book.model_validate(book)

        session.add(db_book)
        session.commit()
        session.refresh(db_book)

    return db_book


# READ specific book by ID (GET)
@app.get("/books/{book_id}")
def get_book(book_id: int):
    with Session(engine) as session:
        # we can use shorthand for this: session.get(Book, book_id)
        statement = select(Book).where(Book.id == book_id)
        book = session.exec(statement).one()

    # 1. Cehck if the book exist
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # 2. Return specific book with book_id
    return book


# UPDATE specific book by ID (PATCH)
@app.patch("/books/{book_id}")
def edit_book(book_id: int, updates: BookUpdate):
    with Session(engine) as session:
        book = session.get(Book, book_id)

        # 1. Check if the book exists
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        # 2. Only take fields the client actually sent (exclude unset)
        update_data = updates.model_dump(exclude_unset=True)

        if not update_data:
            raise HTTPException(
                status_code=400, detail="No fields provided to update")

        book.sqlmodel_update(update_data)

        session.add(book)
        session.commit()
        session.refresh(book)

    return book


# DELETE book by ID (DELETE)
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)

        # 1. Check if the book exists
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")

        book_title = book.title
        session.delete(book)
        session.commit()

    return {"message": f"Deleted '{book_title}'", "book": book}

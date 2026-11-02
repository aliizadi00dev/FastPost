from fastapi import FastAPI, HTTPException


app = FastAPI()


# @app.get("/")
# def root():
#     return "Hello to FastLibra project"
#
#
# # Retrieve books
# @app.get("/books")
# def get_books():
#     # Return all books
#     return books
#
#
# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     # 1. Cehck if the book exist
#     if book_id not in books:
#         raise HTTPException(status_code=404, detail="Book not found")
#
#     # 2. Return specific book with book_id
#     return books[book_id]
#
#
# @app.post("/books")
# def add_book(book: Book):
#     # 1. Create automatically new ID for new book
#     new_id = max(books.keys()) + 1
#
#     # 2. Get new book and convert to Python dictionary (Deserialization)
#     books[new_id] = book.model_dump()
#
#     # 3. Return the new book
#     return {"id": new_id, **books[new_id]}
#
#
# @app.patch("/books/{book_id}")
# def edit_book(book_id: int, updates: BookUpdate):
#     # 1. Check if the book exists
#     if book_id not in books:
#         raise HTTPException(status_code=404, detail="Book not found")
#
#     # 2. Only take fields the client actually sent (exclude unset)
#     update_data = updates.model_dump(exclude_unset=True)
#
#     if not update_data:
#         raise HTTPException(status_code=400, detail="No fields provided to update")
#
#     # 3. Apply the partial update
#     books[book_id].update(update_data)
#
#     # 4. Return the updated book
#     return {"id": book_id, **books[book_id]}
#
#
# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     # 1. Check if the book exists
#     if book_id not in books:
#         raise HTTPException(status_code=404, detail="Book not found")
#
#     # 2. Delete the book and return it to show in log message
#     book = books.pop(book_id)
#
#     # 3. Return the deleted book
#     return {"message": f"Deleted '{book['title']}'", "book": book}

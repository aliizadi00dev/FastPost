# FastPost 📚

A simple book management REST API built with **FastAPI** and **PostgreSQL**.

---

## Features

- 📖 List all books
- 🔍 Get a single book by ID
- ➕ Add a new book
- ✏️ Partially update a book (PATCH)
- 🗑️ Delete a book

---

## Requirements

- Python 3.10+
- FastAPI
- PostgreSQL

Install dependencies:

```bash
uv sync
```

---

## Running the App

Open project folder and run these commands:

```bash
# Initialize PostgreSQL database cluster
mkdir ./data
initdb -D ./data

# Create lock file directory for postgres server (just in RAM)
sudo mkdir /run/postgresql
sudo chown -R $USER:$USER /run/postgresql

# Run postgres server
pg_ctl -D ./data -l postgres.log start

# Create database
createdb fastpost

# Optional: You can inspect database by this interactive command:
psql -d fastpost

# Run the project
uv run fastapi dev
# Or:
uv run fastapi dev --port <port-number>

```

- API base URL: <http://127.0.0.1:8000>
- Interactive docs (Swagger UI): <http://127.0.0.1:8000/docs>
- Alternative docs (ReDoc): <http://127.0.0.1:8000/redoc>

---

## Endpoints

| Method | Path          | Description            |
| ------ | ------------- | ---------------------- |
| GET    | `/`           | Welcome message        |
| GET    | `/books`      | Get all books          |
| GET    | `/books/{id}` | Get one book by ID     |
| POST   | `/books`      | Add a new book         |
| PATCH  | `/books/{id}` | Update specific fields |
| DELETE | `/books/{id}` | Delete a book          |

---

## Book Schema

```json
{
  "title": "string",
  "author": "string",
  "year": 1925,
  "genre": "string",
  "pages": 180,
  "rating": 4.4
}
```

---

## Usage Examples

### Get all books

```bash
curl http://127.0.0.1:8000/books
```

### Get a single book

```bash
curl http://127.0.0.1:8000/books/3
```

### Add a new book

```bash
curl -X POST http://127.0.0.1:8000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "genre": "Fiction",
    "pages": 208,
    "rating": 4.3
  }'
```

### Update a book (partial)

```bash
curl -X PATCH http://127.0.0.1:8000/books/3 \
  -H "Content-Type: application/json" \
  -d '{"rating": 4.9, "pages": 350}'
```

### Delete a book

```bash
curl -X DELETE http://127.0.0.1:8000/books/2
```

---

## Possible Improvements

- Add pagination, filtering, and search
- Add authentication
- Write automated tests with `pytest` + `TestClient`

---

## License

MIT — free to use and modify.

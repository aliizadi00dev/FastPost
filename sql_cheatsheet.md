# SQL Cheatsheet

---

## Create table

```SQL
-- CREATE TABLE books ( title VARCHAR(80), author VARCHAR(80), year INTEGER, genre VARCHAR(80), pages INTEGER, rating INTEGER) ;

CREATE TABLE books (
    -- Using SERIAL for an auto-incrementing primary key
    id SERIAL PRIMARY KEY,

    -- VARCHAR with lengths suitable for book titles and names
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,

    -- INTEGER for the publication year
    year INTEGER,

    -- VARCHAR for categories
    genre VARCHAR(100),

    -- INTEGER for the page count
    pages INTEGER,

    -- DECIMAL for ratings to allow for precision (e.g., 4.7)
    -- 2 and 1 means: 2 digits after the decimal point, 3 digits total (e.g., 4.5)
    -- Use (3,1) or (3,2) depending on your preference for scale.
    rating DECIMAL(3,1)
);
```

## Import data from CSV

```Bash
# run in psql
\copy books FROM './sample_data.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
```

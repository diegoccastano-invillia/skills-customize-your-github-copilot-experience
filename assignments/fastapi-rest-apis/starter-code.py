from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Book API",
    description="A small API for managing books.",
    version="1.0.0",
)


class Book(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API"}


# TODO: Add a GET endpoint to list all books.

# TODO: Add a POST endpoint to create a new book.

# TODO: Add a GET endpoint to fetch a single book by id.

# TODO: Add a PUT endpoint to update a book.

# TODO: Add a DELETE endpoint to remove a book.

from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Model representing a book


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


# Book request
class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    rating: int = Field(gt=-1, lt=6)


BOOKS = [
    Book(1, 'Computer science Pro', 'Avijeet',
         'Learn CS fundamentals with ease', 5)
]


# get all books
@app.get("/books")
async def get_all_books():
    return {"data": BOOKS}


# create a book
@app.post("/book/create")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(assign_id_to_book(new_book))
    return {"message": "successfully done"}


# utility function
def assign_id_to_book(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book

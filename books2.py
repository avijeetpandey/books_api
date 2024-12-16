from fastapi import FastAPI

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


BOOKS = [
    Book(1, 'Computer science Pro', 'Avijeet',
         'Learn CS fundamentals with ease', 5)
]

# get all books


@app.get('/books')
async def get_all_books():
    return {"data": BOOKS}

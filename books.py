from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {
        "id": 1,
        "name": "Harry potter",
        "author": "avijeet",
        "category": "sci-fi"
    },
    {
        "id": 2,
        "name": "Dead man's tale",
        "author": "Nitin",
        "category": "sci-fi"
    },
    {
        "id": 3,
        "name": "Pyjama Party",
        "author": "pooja",
        "category": "sci-fi"
    },
    {
        "id": 4,
        "name": "Harry potter",
        "author": "avijeet",
        "category": "sci-fi"
    },
    {
        "id": 5,
        "name": "Harry potter",
        "author": "avijeet",
        "category": "sci-fi"
    }
]


@app.get("/books")
async def get_books():
    return {"data": BOOKS}


@app.get("/book/{id}")
async def get_book_by_id(id):
    # iterating over book and returning
    for book in BOOKS:
        if str(book["id"]) == id:
            print(book["id"])
            return {"data": book}
    return {"message": "book with id not found"}


@app.post("/books")
async def create_book(book=Body()):
    BOOKS.append(book)
    return {"message": "successfully done"}

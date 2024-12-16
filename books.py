from fastapi import Body, FastAPI, HTTPException

app = FastAPI()

# in memory database
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


# fetch all the books
@app.get("/books")
async def get_books():
    return {"data": BOOKS}


# fetch book by id
@app.get("/book/{id}")
async def get_book_by_id(id):
    # iterating over book and returning
    for book in BOOKS:
        if str(book["id"]) == id:
            print(book["id"])
            return {"data": book}
    return {"message": "book with id not found"}


# create book
@app.post("/books")
async def create_book(book=Body()):
    BOOKS.append(book)
    return {"message": "successfully done"}

# update book


@app.put("/book/update/{id}")
async def update_book_by_id(id, updated_book=Body()):
    book_id = int(id)
    for book in BOOKS:
        if book["id"] == book_id:
            book["name"] = updated_book.get("name")
            book["author"] = updated_book.get("author")
            book["category"] = updated_book.get("category")

            # return updated book
            return {
                "message": "info updated",
                "data": book
            }

    return {"message": "unable to update book"}


# delete book
@app.delete("/book/{id}")
async def delete_book_by_id(id):
    book_id = int(id)
    global BOOKS
    for book in BOOKS:
        if book["id"] == book_id:
            BOOKS = [b for b in BOOKS if b["id"] != book_id]
            return {"message": f"Book with ID {book_id} has been deleted."}

    raise HTTPException(status_code=404, detail="Book not found")

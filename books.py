from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {
        "name": "Harry potter",
        "author": "avijeet",
        "category": "sci-fi"
    },
    {
        "name": "Dead man's tale",
        "author": "Nitin",
        "category": "sci-fi"
    },
    {
        "name": "Pyjama Party",
        "author": "pooja",
        "category": "sci-fi"
    },
    {
        "name": "Harry potter",
        "author": "avijeet",
        "category": "sci-fi"
    },
    {
        "name": "Harry potter",
        "author": "avijeet",
        "category": "sci-fi"
    }
]


@app.get("/books")
async def get_books():
    return {"data": BOOKS}

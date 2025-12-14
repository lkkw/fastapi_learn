from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', host="127.0.0.1", port=8000,reload=True)

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Inventory API")


class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    description: str = ""
    price: float = Field(..., gt=0)
    available: bool = True


items_db = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "Portable computer",
        "price": 999.99,
        "available": True,
    },
    {
        "id": 2,
        "name": "Mouse",
        "description": "Wireless mouse",
        "price": 29.99,
        "available": True,
    },
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items_db


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    # TODO: add item validation and persistence logic
    items_db.append(item.model_dump())
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: update the item in the in-memory database
    for index, current_item in enumerate(items_db):
        if current_item["id"] == item_id:
            items_db[index] = item.model_dump()
            return items_db[index]
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: remove item from the in-memory database
    for index, item in enumerate(items_db):
        if item["id"] == item_id:
            deleted_item = items_db.pop(index)
            return {"message": "Item deleted", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")

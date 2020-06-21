from fastapi import APIRouter

items_router = APIRouter()


@items_router.get("/{item_id}")
def read_items(item_id: int):
    return {"item": item_id}

from fastapi import APIRouter

users_router = APIRouter()


@users_router.get("/me")
def get_current_user():
    return {"user": "current_user"}


@users_router.get("/{another_user}")
def get_another_user(another_user: str):
    return {"user": another_user}

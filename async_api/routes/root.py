from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
async def root():
    print(f"reached view: {__name__}")
    return {"message": "hello world"}

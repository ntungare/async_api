from fastapi import APIRouter, Response, status

root_router = APIRouter()


@root_router.get("/")
async def root():
    print(f"reached view: {__name__}")
    return {"message": "hello world"}


@root_router.get("/asdf", status_code=200)
async def asdf(response: Response):
    print(f"reached view: {__name__}")

    print(f"response.status_code: {response.status_code}")
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    print(f"response.status_code: {response.status_code}")

    return {"message": "hello world"}

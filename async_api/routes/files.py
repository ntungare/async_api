from fastapi import APIRouter

files_router = APIRouter()


@files_router.get("/{file_name:path}")
def get_file_name(file_name: str):
    return {"file_name": file_name}

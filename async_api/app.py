from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from async_api.middleware import middleware_1, middleware_2, middleware_3
from async_api.routes import files, graphql, items, models, root, user

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)
app.add_middleware(middleware_class=middleware_1.Middleware1)
app.add_middleware(middleware_class=middleware_2.Middleware2)
app.add_middleware(middleware_class=middleware_3.Middleware3)
app.include_router(router=root.root_router, tags=["root_routes"])
app.include_router(router=items.items_router, tags=["items_routes"], prefix="/items")
app.include_router(router=user.users_router, tags=["users_routes"], prefix="/users")
app.include_router(router=models.models_router, tags=["models_routes"], prefix="/model")
app.include_router(router=files.files_router, tags=["files_routes"], prefix="/files")
app.include_router(router=graphql.graphql_router, tags=["graphql_routes"], prefix="/graphql")

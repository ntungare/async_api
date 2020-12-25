from fastapi import APIRouter

from async_api.schema import graphql_app

graphql_router = APIRouter()

graphql_router.add_route("/", graphql_app)

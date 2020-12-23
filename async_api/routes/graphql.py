from fastapi import APIRouter
from graphene_federation import build_schema
from starlette.graphql import GraphQLApp

from async_api.schema.root import Query

graphql_router = APIRouter()

schema = build_schema(query=Query)

graphql_router.add_route("/", GraphQLApp(schema=schema), methods=["POST"])

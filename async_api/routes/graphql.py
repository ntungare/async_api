from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema
from fastapi import APIRouter

from async_api.resolvers import query_resolvers
from async_api.schema.root import make_schema

graphql_router = APIRouter()

schema = make_federated_schema(make_schema(), query_resolvers)

print(schema)

graphql_router.add_route("/", GraphQL(schema=schema))

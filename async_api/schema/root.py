import os

from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema
from ariadne.contrib.tracing import apollotracing, opentracing
from ariadne.load_schema import load_schema_from_path

from async_api.resolvers import query_resolvers


def get_schema_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.abspath(os.path.join(current_dir, "..", "resources", "graphql"))

    return schema_path


def make_schema() -> str:
    root_dir = get_schema_path()
    schema = load_schema_from_path(root_dir)

    return schema


def make_graphql_app() -> GraphQL:
    base_schema = make_schema()
    schema = make_federated_schema(base_schema, query_resolvers)

    graphql_app = GraphQL(
        schema=schema,
        extensions=[apollotracing.ApolloTracingExtension, opentracing.OpenTracingExtension],
    )

    return graphql_app

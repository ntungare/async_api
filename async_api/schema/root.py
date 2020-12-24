import os

from ariadne.load_schema import load_schema_from_path


def get_schema_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.abspath(os.path.join(current_dir, "..", "resources", "graphql"))

    return schema_path


def make_schema():
    root_dir = get_schema_path()
    schema = load_schema_from_path(root_dir)

    return schema

import re
from unittest import TestCase

from async_api.schema.root import make_schema


class GraphQLTest(TestCase):
    def assert_sdl_is_same(self, actual_sdl: str, expected_sdl: str) -> None:
        space_replaced_actual_sdl = re.sub(r"\s+", " ", actual_sdl).strip()
        space_replaced_expected_sdl = re.sub(r"\s+", " ", expected_sdl).strip()

        self.assertEqual(space_replaced_actual_sdl, space_replaced_expected_sdl)


class SuperBasicTest(GraphQLTest):
    def test_sdls_are_correct(self):
        actual_schema = make_schema()
        expected_schema = """
        type Query {
            bookById(id: ID): Book
        }

        type Book {
            id: ID
            name: String
            pageCount: Int
            author: Author
            characters: [Character]
        }

        type Author {
            id: ID
            firstName: String
            lastName: String
        }

        type Character {
            id: ID
            firstName: String
            lastName: String
        }
        """

        self.assert_sdl_is_same(actual_schema, expected_schema)

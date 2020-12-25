from typing import Dict, List, Optional

from ariadne.objects import ObjectType
from ariadne.resolvers import GraphQLResolveInfo

from async_api.local_data.books_data import authors, characters

book = ObjectType("Book")


@book.field("author")
def resolve_author(obj: Dict[str, str], _info: GraphQLResolveInfo, **_) -> Optional[Dict[str, str]]:
    for author in authors:
        if author.get("id") == obj.get("authorId"):
            return author

    return None


@book.field("characters")
def resolve_characters(obj: Dict[str, str], _info: GraphQLResolveInfo, **_) -> List[Dict[str, str]]:
    possible_characters = []

    for character in characters:
        if character.get("id") in obj.get("characters"):
            possible_characters.append(character)

    return possible_characters

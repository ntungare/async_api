from typing import Dict, List, Optional, Union

from ariadne import QueryType

from async_api.local_data.books_data import book_to_character_ids, books

query = QueryType()


@query.field("bookById")
def resolve_book_by_id(*_, **kwargs) -> Optional[Dict[str, Union[str, List[str]]]]:
    for book in books:
        if book.get("id") == kwargs.get("id"):
            return {**book, "characters": list(book_to_character_ids.get(book.get("id")))}

    return None

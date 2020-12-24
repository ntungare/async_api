from typing import Dict, List, Set

books: List[Dict[str, str]] = [
    {
        "id": "book-1",
        "name": "Harry Potter and the Philosopher's Stone",
        "pageCount": "223",
        "authorId": "author-1"
    },
    {
        "id": "book-2",
        "name": "Moby Dick",
        "pageCount": "635",
        "authorId": "author-2"
    },
    {
        "id": "book-3",
        "name": "Interview with the vampire",
        "pageCount": "371",
        "authorId": "author-3"
    }
]

authors: List[Dict[str, str]] = [
    {
        "id": "author-1",
        "firstName": "Joanne",
        "lastName": "Rowling"
    },
    {
        "id": "author-2",
        "firstName": "Herman",
        "lastName": "Melville"
    },
    {
        "id": "author-3",
        "firstName": "Anne",
        "lastName": "Rice"
    }
]

characters: List[Dict[str, str]] = [
    {
        "id": "character-1",
        "firstName": "Mob",
        "lastName": "Riordan"
    },
    {
        "id": "character-2",
        "firstName": "Percy",
        "lastName": "Seuss"
    },
    {
        "id": "character-3",
        "firstName": "Jane",
        "lastName": "Austin"
    }
]

book_to_character_ids: Dict[str, Set[str]] = {
    "book-1": {"character-1", "character-2"},
    "book-2": {"character-2", "character-3"},
    "book-3": {"character-1", "character-3"},
}

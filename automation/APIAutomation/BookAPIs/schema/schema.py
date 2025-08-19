BOOK_SCHEMA = {
    "type": "object",
    "properties": {
        "book_name": {"type": "string"},
        "isbn": {"type": "string"},
        "aisle": {"type": "string"},
        "author": {"type": "string"}
    },
    "required": ["book_name", "isbn", "aisle", "author"]
}

DELETE_SCHEMA = {
    "type": "object",
    "properties": {
        "msg": {"type": "string"}
    },
    "required": ["msg"]
}
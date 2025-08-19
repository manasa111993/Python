import allure, jsonschema
from BookAPIs.schema.schema import BOOK_SCHEMA


@allure.feature("Library API")
@allure.story("Get Book")
def test_get_book(library_api, book, book_id):
    library_api.add_book(book)
    response = library_api.get_book(book_id)
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    jsonschema.validate(books[0], BOOK_SCHEMA)
    assert books[0]["author"] == book["author"]
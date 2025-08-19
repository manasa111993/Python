import allure, jsonschema
from automation.APIAutomation.BookAPIs.schema.schema import BOOK_SCHEMA


@allure.feature("Library API - Integration Flow")
def test_add_get_delete_flow(library_api, book, book_id):
    # Add
    add_res = library_api.add_book(book)
    assert add_res.status_code == 200
    book_id_generated = book["isbn"] + book["aisle"]
    assert book_id == book_id_generated

    # Get
    get_res = library_api.get_book(book_id)
    assert get_res.status_code == 200
    books = get_res.json()
    jsonschema.validate(books[0], BOOK_SCHEMA)

    # Delete
    del_res = library_api.delete_book(book_id)
    assert del_res.status_code == 200
    assert del_res.json()["msg"] == "book is successfully deleted"

    # Get again → should not exist
    get_again = library_api.get_book(book_id)
    assert get_again.status_code in (200, 404)
    if get_again.status_code == 200:
        assert get_again.json() == []
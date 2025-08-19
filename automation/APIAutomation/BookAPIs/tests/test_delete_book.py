import allure, jsonschema
from BookAPIs.schema.schema import DELETE_SCHEMA


@allure.feature("Library API")
@allure.story("Delete Book")
def test_delete_book(library_api, book, book_id):
    library_api.add_book(book)
    response = library_api.delete_book(book_id)
    assert response.status_code == 200
    data = response.json()
    jsonschema.validate(data, DELETE_SCHEMA)
    assert data["msg"] == "book is successfully deleted"
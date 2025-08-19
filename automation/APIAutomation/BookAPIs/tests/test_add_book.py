import allure


@allure.feature("Library API")
@allure.story("Add Book")
def test_add_book(library_api, book, book_id):
    response = library_api.add_book(book)
    assert response.status_code == 200
    data = response.json()
    assert data["Msg"] in ["successfully added", "Book already exists"]
    book_id_generated = book["isbn"] + book["aisle"]
    assert book_id == book_id_generated
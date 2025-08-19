import pytest, allure, jsonschema
import time


@allure.feature("Library API - Negative Tests")
class TestLibraryNegative:

    @allure.story("Add Book with missing fields")
    @pytest.mark.negative
    def test_add_book_missing_fields(self, library_api):
        payload = {"name": "Bad Book"}  # missing isbn, aisle, author
        response = library_api.add_book(payload)
        assert response.status_code in (400, 404, 500)  # depends on server behavior

    @allure.story("Add Book with invalid aisle type")
    @pytest.mark.negative
    def test_add_book_invalid_datatype(self, library_api):
        payload = {"name": "Bad Book", "isbn": "X123", "aisle": "not_a_number", "author": "QA"}
        response = library_api.add_book(payload)
        assert response.status_code in (400, 500)

    @allure.story("Add Book with empty strings")
    @pytest.mark.negative
    def test_add_book_empty_strings(self, library_api):
        payload = {"name": "", "isbn": "", "aisle": "", "author": ""}
        response = library_api.add_book(payload)
        assert response.status_code in (400, 500)

    @allure.story("Get Book with non-existent ID")
    @pytest.mark.negative
    def test_get_book_non_existent(self, library_api):
        response = library_api.get_book("doesnotexist123")
        assert response.status_code in (200, 404)
        if response.status_code == 200:
            assert response.json() == []  # should return empty list

    @allure.story("Get Book response time")
    def test_get_book_response_time(self, library_api, book_id):
        start = time.time()
        response = library_api.get_book(book_id)
        elapsed = (time.time() - start) * 1000
        assert elapsed < 2000  # under 2 seconds
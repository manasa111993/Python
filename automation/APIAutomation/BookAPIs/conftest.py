import pytest, json, os
from automation.APIAutomation.BookAPIs.apis.library_api import LibraryAPI

BASE_URL = "http://216.10.245.166"   # Rahul Shetty demo server

@pytest.fixture(scope="session")
def library_api():
    return LibraryAPI(BASE_URL)

# Data loader
def load_books_data():
    data_file = os.path.join(os.path.dirname(__file__), "data", "books.json")
    with open(data_file, "r") as f:
        return json.load(f)

# pytest hook for auto-parametrize
def pytest_generate_tests(metafunc):
    if "book" in metafunc.fixturenames:   # check if test expects `book`
        books = load_books_data()
        metafunc.parametrize("book", books)

@pytest.fixture
def book_id(book):
    return book["isbn"] + book["aisle"]
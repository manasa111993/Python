#from BookAPIs.schema.client import APIClient
from automation.APIAutomation.BookAPIs.schema.client import APIClient


class LibraryAPI(APIClient):
    def add_book(self, payload):
        return self.post("/Library/Addbook.php", json=payload)

    def get_book(self, book_id):
        return self.get("/Library/GetBook.php", params={"ID": book_id})

    def delete_book(self, book_id):
        return self.post("/Library/DeleteBook.php", json={"ID": book_id})

import requests

class APIClient:
    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(headers or {"Content-Type": "application/json"})
        self.timeout = timeout

    def _url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, **kwargs):
        return self.session.get(self._url(path), timeout=self.timeout, **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self._url(path), timeout=self.timeout, **kwargs)
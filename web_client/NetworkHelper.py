import requests

class NetworkHelper:
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

        if username and password:
            self.session.auth = (username, password)

    def _get_url(self, endpoint, item_id=None):
        url = f"{self.base_url}/{endpoint}/"
        if item_id:
            url += f"{item_id}/"
        return url

    def _handle_request(self, method, url, data=None):
        try:
            response = self.session.request(method, url, json=data, timeout=5)
            response.raise_for_status()

            if response.status_code == 204:
                return True
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error during {method} {url}: {e}")
            return None


    def get_list(self, endpoint):
        return self._handle_request('GET', self._get_url(endpoint))

    def get_item(self, endpoint, item_id):
        return self._handle_request('GET', self._get_url(endpoint, item_id))

    def create_item(self, endpoint, data):
        return self._handle_request('POST', self._get_url(endpoint), data=data)

    def update_item(self, endpoint, item_id, data):
        return self._handle_request('PUT', self._get_url(endpoint, item_id), data=data)

    def delete_item(self, endpoint, item_id):
        return self._handle_request('DELETE', self._get_url(endpoint, item_id))
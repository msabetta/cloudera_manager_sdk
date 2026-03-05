import requests
from .exceptions import APIError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class ClouderaManagerClient:

    def __init__(self, host, auth=None, api_version="v51", verify_ssl=False, timeout=30, retries=3, backoff=1):
        self.base_url = f"{host.rstrip('/')}/api/{api_version}"
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})

        # gestione retry
        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

        self.verify_ssl = verify_ssl
        self.timeout = timeout
        # gestione autenticazione
        if isinstance(auth, dict):  # token
            self.session.headers.update(auth)
        else:
            self.session.auth = auth

    # def __init__(
    #     self,
    #     host,
    #     username,
    #     password,
    #     api_version="v51",
    #     verify_ssl=False,
    #     timeout=30
    # ):
    #     self.base_url = f"{host.rstrip('/')}/api/{api_version}"
    #     self.session = requests.Session()
    #     self.session.auth = (username, password)
    #     self.session.headers.update({
    #         "Content-Type": "application/json",
    #         "Accept": "application/json"
    #     })
    #
    #     self.verify_ssl = verify_ssl
    #     self.timeout = timeout
    #
    # def request(self, method, endpoint, params=None, data=None):
    #
    #     url = f"{self.base_url}/{endpoint.lstrip('/')}"
    #
    #     response = self.session.request(
    #         method,
    #         url,
    #         params=params,
    #         json=data,
    #         verify=self.verify_ssl,
    #         timeout=self.timeout
    #     )
    #
    #     if not response.ok:
    #         raise APIError(response.status_code, response.text)
    #
    #     if response.text:
    #         return response.json()
    #
    #     return None
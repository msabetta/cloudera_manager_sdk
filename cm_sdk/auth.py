import requests
from requests.auth import HTTPBasicAuth

class AuthManager:
    """
    Gestione autenticazioni avanzate:
    - Basic
    - Token
    - Kerberos
    """

    def __init__(self, method="basic", username=None, password=None, token=None):
        self.method = method
        self.username = username
        self.password = password
        self.token = token

    def get_auth(self):
        if self.method == "basic":
            return HTTPBasicAuth(self.username, self.password)
        elif self.method == "token":
            return {"Authorization": f"Bearer {self.token}"}
        elif self.method == "kerberos":
            from requests_kerberos import HTTPKerberosAuth
            return HTTPKerberosAuth()
        else:
            raise ValueError("Metodo di autenticazione non supportato")
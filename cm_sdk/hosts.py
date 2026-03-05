class HostAPI:

    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client.request("GET", "hosts")

    def get(self, host_id):
        return self.client.request(
            "GET",
            f"hosts/{host_id}"
        )
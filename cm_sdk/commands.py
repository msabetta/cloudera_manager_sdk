class CommandAPI:

    def __init__(self, client):
        self.client = client

    def get(self, command_id):

        return self.client.request(
            "GET",
            f"commands/{command_id}"
        )

    def list(self):

        return self.client.request("GET", "commands")
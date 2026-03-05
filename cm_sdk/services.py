class ServiceAPI:

    def __init__(self, client):
        self.client = client

    def list(self, cluster):

        return self.client.request(
            "GET",
            f"clusters/{cluster}/services"
        )

    def start(self, cluster, service):

        return self.client.request(
            "POST",
            f"clusters/{cluster}/services/{service}/commands/start"
        )

    def stop(self, cluster, service):

        return self.client.request(
            "POST",
            f"clusters/{cluster}/services/{service}/commands/stop"
        )

    def restart(self, cluster, service):

        return self.client.request(
            "POST",
            f"clusters/{cluster}/services/{service}/commands/restart"
        )
class ClusterAPI:

    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client.request("GET", "clusters")

    def get(self, cluster_name):
        return self.client.request(
            "GET",
            f"clusters/{cluster_name}"
        )

    def services(self, cluster_name):
        return self.client.request(
            "GET",
            f"clusters/{cluster_name}/services"
        )
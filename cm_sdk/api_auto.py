class AutoAPI:

    def __init__(self, client, swagger_json):
        self.client = client
        self.swagger = swagger_json

    # -----------------------
    # Metodo GET /clusters
    # -----------------------
    def get_clusters(self):
        """
        Recupera la lista dei cluster dal Cloudera Manager.
        """
        return self.client.get("/clusters")

    # -----------------------
    # Metodo POST /clusters/{clusterName}/services/{serviceName}/commands/restart
    # -----------------------
    def post_clusters_commands_restart(self, clusterName, serviceName):
        """
        Riavvia un servizio specifico in un cluster.

        Parametri:
            clusterName (str): nome del cluster
            serviceName (str): nome del servizio (es. 'hdfs')
        """
        endpoint = f"/clusters/{clusterName}/services/{serviceName}/commands/restart"
        return self.client.post(endpoint)
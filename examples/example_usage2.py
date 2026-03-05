from cm_sdk.client import ClouderaManagerClient
from cm_sdk.auth import AuthManager
from cm_sdk.api_auto import AutoAPI

# configurazione base
host = "https://cloudera-manager.example.com:7183"
username = "admin"
password = "admin"

# autenticazione avanzata (basic in questo esempio)
auth = AuthManager(method="basic", username=username, password=password).get_auth()

swagger_json = {
    "paths": {
        "/clusters": {
            "get": {
                "summary": "Elenca tutti i cluster"
            },
            "post": {
                "summary": "Crea un nuovo cluster"
            }
        },
        "/clusters/{clusterName}/services/{serviceName}/commands/restart": {
            "post": {
                "summary": "Riavvia un servizio specifico"
            }
        }
    }
}

# client con retry automatico
client = ClouderaManagerClient(
    host=host,
    auth=auth,
    retries=5,
    backoff=2  # backoff factor
)

# generazione automatica dei metodi da swagger_json
auto_api = AutoAPI(client, swagger_json)

# chiamata endpoints
clusters = auto_api.get_clusters()
print("Clusters:", clusters)

# riavvio servizio
result = auto_api.post_clusters_services_commands_restart(
    clusterName="Cluster 1",
    serviceName="hdfs"
)
print("Restart result:", result)
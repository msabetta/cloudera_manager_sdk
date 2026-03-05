import json
from cm_sdk.client import ClouderaManagerClient
from cm_sdk.auth import AuthManager
from cm_sdk.api_auto import AutoAPI

# 1) Prendi swagger JSON da file
with open("cm_swagger.json", "r") as f:
    swagger_json = json.load(f)

# 2) Crea client avanzato
host = "https://cloudera-manager.example.com:7183"
auth = AuthManager(method="basic", username="admin", password="admin").get_auth()
client = ClouderaManagerClient(host=host, auth=auth, retries=5, backoff=1)

# 3) Genera API dal file swagger
auto_api = AutoAPI(client, swagger_json)

# 4) Usa API dinamiche
print(auto_api.get_clusters())

result = auto_api.post_clusters_commands_restart(
    clusterName="Cluster 1",
    serviceName="hdfs"
)
print(result)
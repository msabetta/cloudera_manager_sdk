from cm_sdk.client import ClouderaManagerClient
from cm_sdk.clusters import ClusterAPI
from cm_sdk.services import ServiceAPI

host = "https://cloudera-manager.example.com:7183"
username = "admin"
password = "admin"

client = ClouderaManagerClient(host, username, password)

clusters = ClusterAPI(client)
services = ServiceAPI(client)

print("Clusters:")
print(clusters.list())

cluster_name = clusters.list()["items"][0]["name"]

print("Services:")
print(services.list(cluster_name))

print("Restart HDFS")
services.restart(cluster_name, "hdfs")
import asyncio
from cm_sdk.client_async import ClouderaManagerAsyncClient
from cm_sdk.api_auto import AutoAPI

async def main():
    host = "https://cloudera-manager.example.com:7183"

    # client async (basic auth)
    async_client = ClouderaManagerAsyncClient(
        host=host,
        auth=None,  # aiohttp supporta tuple (user, pass) direttamente, vedi doc
        verify_ssl=False
    )

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

    # generazione API dinamiche
    auto_api = AutoAPI(async_client, swagger_json)

    # esempio chiamate async
    clusters = await auto_api.get_clusters()
    print("Clusters (async):", clusters)

    restart_result = await auto_api.post_clusters_services_commands_restart(
        clusterName="Cluster 1",
        serviceName="hdfs"
    )
    print("Restart result (async):", restart_result)

# run
asyncio.run(main())
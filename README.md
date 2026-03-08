# Cloudera Manager Python SDK

SDK Python avanzato per interagire con le API REST di Cloudera Manager in Cloudera Data Platform (CDP).

Questo progetto fornisce una libreria Python modulare per automatizzare operazioni DevOps e amministrative su cluster Hadoop/CDP tramite le API ufficiali di Cloudera Manager.

---

## Features

* Client REST completo per Cloudera Manager
* Autenticazione avanzata

  * Basic Auth
  * Token
  * Kerberos
* Retry automatico su errori HTTP
* Supporto Sync e Async API
* Generazione automatica delle API da Swagger/OpenAPI
* CLI integrata
* Moduli dedicati per:

  * cluster
  * servizi
  * host
  * comandi

---

## Project Structure

```
cloudera_manager_sdk/
│
├── cm_sdk/
│   ├── __init__.py
│   ├── client.py
│   ├── client_async.py
│   ├── auth.py
│   ├── api_auto.py
│   ├── clusters.py
│   ├── services.py
│   ├── hosts.py
│   ├── commands.py
│   ├── exceptions.py
│   └── cli.py
│
├── examples/
│   └── example_usage.py
│
├── requirements.txt
├── setup.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/msabetta/cloudera-manager-sdk.git
cd cloudera-manager-sdk
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the package locally:

```bash
pip install .
```

---

## Dependencies

* Python 3.8+
* requests
* aiohttp
* urllib3
* requests-kerberos (optional)

---

## Basic Usage

### Create Client

```python
from cm_sdk.client import ClouderaManagerClient
from cm_sdk.auth import AuthManager

host = "https://cloudera-manager.example.com:7183"

auth = AuthManager(
    method="basic",
    username="admin",
    password="admin"
).get_auth()

client = ClouderaManagerClient(
    host=host,
    auth=auth,
    retries=3
)
```

---

## Get Clusters

```python
from cm_sdk.api_auto import AutoAPI

api = AutoAPI(client)

clusters = api.get_clusters()
print(clusters)
```

---

## Restart Service

```python
api.post_clusters_commands_restart(
    clusterName="Cluster 1",
    serviceName="hdfs"
)
```

---

## Async Client Example

```python
import asyncio
from cm_sdk.client_async import ClouderaManagerAsyncClient

async def main():

    client = ClouderaManagerAsyncClient(
        host="https://cloudera-manager.example.com:7183"
    )

    clusters = await client.get("clusters")
    print(clusters)

asyncio.run(main())
```

---

## CLI Usage

Dopo l'installazione puoi usare la CLI:

```bash
cm-sdk https://cloudera-manager.example.com:7183 admin admin clusters
```

---

## Automatic API Generation (Swagger)

È possibile generare dinamicamente gli endpoint dalle definizioni Swagger/OpenAPI di Cloudera Manager.

Scaricare il file JSON dalla UI di Cloudera Manager:

```
Support → API Documentation
```

Caricare il JSON:

```python
import json
from cm_sdk.api_auto import AutoAPI

with open("cm_swagger.json") as f:
    swagger = json.load(f)

api = AutoAPI(client, swagger)
```

---

## Error Handling

```python
from cm_sdk.exceptions import APIError

try:
    api.get_clusters()
except APIError as e:
    print(e)
```

---

## Example

Esempi completi si trovano nella directory:

```
examples/
```

---

## Contributing

Pull request e contributi sono benvenuti.

Workflow consigliato:

```
fork -> branch -> pull request
```

---

## License

MIT License

---

## Roadmap

* supporto completo Swagger/OpenAPI
* generator automatico SDK
* monitoring cluster
* metriche e alert
* supporto Terraform-style automation
* gestione deploy cluster

---

## Disclaimer

Questo progetto non è affiliato ufficialmente con Cloudera.

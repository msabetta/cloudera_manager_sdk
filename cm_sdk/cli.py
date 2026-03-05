import sys
from .client import ClouderaManagerClient

def main():
    if len(sys.argv) < 2:
        print("Uso: cm-sdk <HOST> <USER> <PASS> [ENDPOINT]")
        sys.exit(1)

    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]
    endpoint = sys.argv[4] if len(sys.argv) > 4 else "clusters"

    client = ClouderaManagerClient(host, user, password)
    response = client.request("GET", endpoint)
    import json
    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
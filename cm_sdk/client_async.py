import aiohttp
import asyncio
from .exceptions import APIError

class ClouderaManagerAsyncClient:

    def __init__(self, host, auth=None, api_version="v51", verify_ssl=False, timeout=30):
        self.base_url = f"{host.rstrip('/')}/api/{api_version}"
        self.auth = auth
        self.verify_ssl = verify_ssl
        self.timeout = timeout

    async def request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        async with aiohttp.ClientSession(auth=self.auth) as session:
            async with session.request(method, url, json=data, params=params, ssl=self.verify_ssl, timeout=self.timeout) as resp:
                if resp.status >= 400:
                    raise APIError(resp.status, await resp.text())
                if resp.content_type == 'application/json':
                    return await resp.json()
                return await resp.text()

    async def get(self, endpoint, params=None):
        return await self.request("GET", endpoint, params=params)

    async def post(self, endpoint, data=None):
        return await self.request("POST", endpoint, data=data)
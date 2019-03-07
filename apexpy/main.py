import aiohttp
from apexpy import Constants
from apexpy.exceptions import ApiKeyNotProvidedError
import asyncio


class HttpRequest:
    def __init__(self, name: str, api_key: str = None, platform: int = 5):

        if api_key is None and Constants.API_KEY is None:
            raise ApiKeyNotProvidedError

        self.platform = platform
        self.name = name

        self.api_key = api_key if api_key else Constants.API_KEY
        self.headers = {'TRN-Api-KEY': self.api_key}

        self.req_url = f'{Constants.BASE_URL}{self.platform}/{self.name}'

    @staticmethod
    async def _error_handler(resp):
        if resp != Constants.API_OK:
            raise Constants.API_ERROR_MAP.get(resp)

    async def _session(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.req_url) as resp:
                await self._error_handler(resp.status)
                return resp


a = HttpRequest(name='Zodiac', platform=1)

asyncio.run(a._session())


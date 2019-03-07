import aiohttp
from apexpy import Constants
from apexpy import ApiKeyNotProvidedError
import asyncio


class APexRequest:
    def __init__(self, name: str, api_key: str = None, platform: int = 5):
        if api_key is None and Constants.API_KEY is None:
            raise ApiKeyNotProvidedError('')

        self.platform = platform
        self.name = name

        self.api_key = api_key if api_key else Constants.API_KEY
        self.headers = {'TRN-Api-KEY': self.api_key}

        self.req_url = f'{Constants.BASE_URL}/{self.platform}/{self.name}'

    async def session(self):
        pass

    async def _handle_session(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.req_url) as resp:
                print(resp)
                return resp

a = APexRequest(name='Zodiac')

asyncio.run(a.session())


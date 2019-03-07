from apexpy.httprequest import ApexRequest


class ApexPlayer:
    def __init__(self, name, platform, key=None):
        self.key = key
        self.name = name
        self.platform = platform

    async def _populate(self, data):
        print(data['data'].keys())
        print(data['data']['id'])

    async def make(self):
        temp = await ApexRequest(self.name, self.platform, api_key=self.key)._session()
        await self._populate(await temp.json())

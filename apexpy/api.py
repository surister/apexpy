from apexpy.httprequest import ApexRequest


class ApexApi:
    def __init__(self, key=None):

        self.name = self.platform = None
        self.key = key

    async def _populate(self, data):

        # TODO 1
        for k, v in data['data']['metadata'].items():
            setattr(self, k, v)

        print(data['data'].keys())
        print(data['data']['id'])

    async def search(self, name, platform):
        self.name = name
        self.platform = platform

        data = await ApexRequest(self.name, self.platform, api_key=self.key).session()
        await self._populate(await data.json())

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

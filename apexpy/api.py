from apexpy.characters import ApexCharacter
from apexpy.httprequest import ApexRequest
from apexpy.utils import Constants


class ApexApi:
    def __init__(self, key: str = None):

        self.name = self.platform = None
        self.key = key
        self.legends = []  # Game's characters are called 'legends' in this game.

    async def _populate(self, data) -> None:

        self.legends = [ApexCharacter(char_data) for char_data in data['data']['children']]

        for k, v in data['data']['metadata'].items():
            setattr(self, k, v)

        stats = data['data']['stats']

        self.stats = [
            {stats['metadata']['key']: stats['value'], 'rank': stats.get('rank')} for stats in stats
        ]

    async def search(self, name: str, platform: str) -> None:
        self.name = name
        self.platform = Constants.PLATFORM_MAP.get(platform)

        data = await ApexRequest(self.name, self.platform, api_key=self.key).session()
        await self._populate(await data.json())

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

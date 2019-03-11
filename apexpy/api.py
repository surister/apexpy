from apexpy.characters import ApexCharacter
from apexpy.httprequest import ApexRequest
from apexpy.utils import Constants


class ApexApi:
    """
    Represents the Apex api containing all the data requested by :class:`.ApexRequest`.

    Parameters
    ----------
        key : :class:`str`
            The apex legends api key.

    Attributes
    ----------
        name
            :class:`str`
            Player's name
        key
            :class:`str`
            api key
        legends
            List[:class:`.ApexCharacter`]
            Legends' data
        stats
            List[:class:`dict`]
            Player's general stats
        id
            :class:`str`
            Player's id

    """
    def __init__(self, key: str = None):

        self.name = self.platform = None
        self.key = key
        self.legends = []  # Game's characters are called 'legends' in this game.

    async def _populate(self, data) -> None:
        """
        Populates object with data

        :param data:
        :return: :class:`None`
        """

        self.legends = [ApexCharacter(char_data) for char_data in data['data']['children']]

        for k, v in data['data']['metadata'].items():
            setattr(self, k, v)

        stats = data['data']['stats']

        self.stats = [
            {stats['metadata']['key']: stats['value'], 'rank': stats.get('rank')} for stats in stats
        ]

    async def search(self, name: str, platform: str) -> None:
        """
        Creates the :class:`.ApexRequest` object that takes care of the api's communication.
        Automatically sets variables and call the population method.


        :param name: :class:`str`
        :param platform: :class:`str` Three platforms supported are pc, xbox and psn, they are transformed into their numeric code, 5, 2, 1 respectively.

        :return: :class:`None`
        """
        self.name = name
        self.platform = Constants.PLATFORM_MAP.get(platform)

        data = await ApexRequest(self.name, self.platform, api_key=self.key).session()
        await self._populate(await data.json())

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

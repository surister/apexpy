
class ApexCharacter:
    """
    Represents an Apex legend character

    Parameters
    ----------
        data : :class:`dict`
            Every characters data.

    Attributes
    ----------
        raw_data
            :class:`dict`
            Raw data

        name
            :class:`str`
            Character's name

        id
            :class:`str`
            Every character id.

            Wraith -> legend_1,
            Bangalore -> legend_2,
            Caustic -> legend_3,
            Mirage -> legend_4,
            Bloodhound -> legend_5,
            Gibraltar -> legend_6,
            Lifeline -> legend_7,
            Pathfinder -> legend_8
        icon
            :class:`str`
            Character's icon image
        bgimage
            :class:`str`
            Character's background image
        stats
            List[:class:`dict`]
            Character's stats data
    """
    def __init__(self, data):
        metadata = data['metadata']
        stats = data['stats']

        self.raw_data = data

        self.id = data.get('id')

        self.name = metadata.get('legend_name')
        self.icon = metadata.get('icon')
        self.bgimage = metadata.get('bgimage')

        self.stats = [
            {stats['metadata']['key']: stats['value'], 'rank': stats.get('rank')} for stats in stats
        ]

    def __str__(self):
        return f'{self.__class__.__name__}({self.name})'

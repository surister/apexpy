
class ApexCharacter:
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

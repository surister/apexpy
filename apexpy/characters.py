
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
#
#
#
# data = {
#         "id": "legend_1",
#         "type": "",
#         "metadata": {
#           "legend_name": "Wraith",
#           "icon": "https://media.contentapi.ea.com/content/dam/apex-legends/images/2019/01/legends-character-tiles/apex-grid-tile-legends-wraith.png.adapt.crop16x9.png",
#           "bgimage": "https://trackercdn.com/cdn/apex.tracker.gg/legends/wraith-concept-bg-small.jpg"
#         },
#         "stats": [
#           {
#             "metadata": {
#               "key": "Kills",
#               "name": "Kills",
#               "categoryKey": "combat",
#               "categoryName": "Combat",
#               "isReversed": False
#             },
#             "value": 4267.0,
#             "rank": 658,
#             "displayValue": "4,267",
#             "displayRank": "658"
#           },
#           {
#             "metadata": {
#               "key": "KillsPerMatch",
#               "name": "Kills Per Match",
#               "categoryKey": "combat",
#               "categoryName": "Combat",
#               "isReversed": False
#             },
#             "value": 8.85,
#             "rank": 117,
#             "displayValue": "8.85",
#             "displayRank": "117"
#           },
#           {
#             "metadata": {
#               "key": "DamagePerMatch",
#               "name": "Damage Per Match",
#               "categoryKey": "combat",
#               "categoryName": "Combat",
#               "isReversed": False
#             },
#             "value": 1705.78,
#             "rank": 128,
#             "displayValue": "1,705.78",
#             "displayRank": "128"
#           },
#           {
#             "metadata": {
#               "key": "Damage",
#               "name": "Damage",
#               "categoryKey": "combat",
#               "categoryName": "Combat",
#               "isReversed": False
#             },
#             "value": 822184.0,
#             "rank": 926,
#             "displayValue": "822,184",
#             "displayRank": "926"
#           },
#           {
#             "metadata": {
#               "key": "MatchesPlayed",
#               "name": "Matches Played",
#               "categoryKey": "game",
#               "categoryName": "Game",
#               "isReversed": False
#             },
#             "value": 482.0,
#             "percentile": 0.4,
#             "rank": 866,
#             "displayValue": "482",
#             "displayRank": "866"
#           }
#         ]
#       }
#
# a = ApexCharacter(data)
# print(a.id)
# print(a.name)
# print(a.stats)
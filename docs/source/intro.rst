============
Introduction
============

Apexpy it's an asynchronous api wrapper for Apex-legend written in `python 3.6+ <https://www.python.org/>`_

.. note:: This project or its documentation is in no way related to `EA <https://www.ea.com/games/apex-legends>`_
            or the api it wraps `Apex Legends - API tracker <https://apex.tracker.gg/site-api>`_


Apex py is written using aiohttp and wrapps all the data given by the api in to a convenient scheme for your use.

Quick example
-------------

.. code-block:: python

    import asyncio
    from apexpy import ApexApi


    async def main():

        player = ApexApi(key='SecretApiKey')
        await player.search('DiegosaursTTV', 'pc')

        for legend in player.legends:
            print(f'{legend.name} -> {legend.stats}')

        print(player.stats)

    asyncio.run(main())

Output
------
.. code-block:: python

    Wraith -> [{'Kills': 4329.0, 'rank': 658}, {'KillsPerMatch': 8.78, 'rank': 117}, {'DamagePerMatch': 1696.19, 'rank': 128}, {'Damage': 836222.0, 'rank': 926}, {'MatchesPlayed': 493.0, 'rank': 866}]
    Mirage -> [{'Kills': 10324.0, 'rank': 1}, {'Damage': 2062356.0, 'rank': 1}, {'Headshots': 6869.0, 'rank': 4}, {'CarePackageKills': 89.0, 'rank': 2}]
    Lifeline -> [{'Kills': 14.0, 'rank': None}]
    Bloodhound -> [{'Kills': 139.0, 'rank': 32243}]
    Caustic -> [{'Kills': 41.0, 'rank': 7054}]
    Gibraltar -> [{'Kills': 102.0, 'rank': 1915}]
    Bangalore -> [{'Kills': 384.0, 'rank': 27236}, {'Damage': 78092.0, 'rank': 23243}]
    Pathfinder -> [{'Kills': 37.0, 'rank': 27638}, {'Specific2': 17665.0, 'rank': 12108}]
    [{'Level': 392.0, 'rank': None}, {'Kills': 15370.0, 'rank': 1}, {'KillsPerMatch': 31.18, 'rank': None}, {'DamagePerMatch': 6037.87, 'rank': None}, {'Damage': 2976670.0, 'rank': 1}, {'MatchesPlayed': 493.0, 'rank': None}, {'CarePackageKills': 89.0, 'rank': None}]


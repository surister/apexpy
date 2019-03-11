import asyncio
from apexpy import ApexApi


async def main():

    player = ApexApi()

    await player.search('DiegosaursTTV', 'pc')

    for legend in player.legends:
        print(f'{legend.name} -> {legend.id}')

    print(player.stats)

asyncio.run(main())

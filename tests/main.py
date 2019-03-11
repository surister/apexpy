import asyncio
from apexpy import ApexApi


async def main():
    player = ApexApi()
    await player.search('DiegosaursTTV', 'pc')
    # for legend in player.legends:
    #     print(legend.stats)
    print(player.stats)

if __name__ == '__main__':
    asyncio.run(main())

import asyncio
from apexpy import ApexApi


async def main():
    player = ApexApi()
    await player.search('DiegosaursTTV', 5)
    print(player)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

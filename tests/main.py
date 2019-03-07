import asyncio
from apexpy import ApexPlayer

async def main():
    player = await ApexPlayer('Itspikolo', 2).make()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

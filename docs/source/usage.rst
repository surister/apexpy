=================
Using the library
=================


Because both are asynchronous, discord bots and Apexpy go really well together.

This snippet is written in python 3.7 using discord.py (rewrite branch) and shows a way of using Apexpy in Cog.

.. code-block:: python

    from discord.ext.commands import command
    from apexpy import ApexApi

    class ApexLegend:
        def __init__(self, bot):
            self.bot = bot

        @command()
        async def apexsearch(self, ctx, name: str, platform:str) -> None:
            player = ApexApi('secret_key')
            await player.search(name, platform)
            for legend in player.legends:
                await ctx.send(legend.stats)


    def setup(bot):
        bot.add_cog(ApexLegend(bot))

Output:

..  image:: /_static/apexpy-discord.py.png


You make sure you prettify everything, as most of the data is pure object oriented, its manipulation is very easy.


Apexpy can of course, be run as a standalone using asyncio.

.. code-block:: python

    import asyncio
    from apexpy import ApexApi


    async def main():

        player = ApexApi()

        await player.search('DiegosaursTTV', 'pc')

        for legend in player.legends:
            print(f'{legend.name} -> {legend.stats}')

        print(player.stats)

    asyncio.run(main())

For more detailed information of the library, check the api reference.
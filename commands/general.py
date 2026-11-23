from discord.ext import commands


class General(commands.Cog):
      def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def hello(self, ctx):
            await ctx.send(f"hello {ctx.author.mention} hope you have a nice day!")
        
        @commands.command()
        async def hi(self, ctx):
            await ctx.send(f"wazzup {ctx.author.mention} cuh!")
        
        @commands.command()
        async def quote(self, ctx):
            await ctx.send(f"DAILY QUOTE: Time is precious.")


async def setup(bot):
    await bot.add_cog(General(bot))
from discord.ext import commands

class MessageFilter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        bad_words = ["tite", "burat", "gago", "bobo", "tanga", "inutil", "nigga", "tangina", "tanginamo", "8080", "bitch"]

        content = message.content.lower()

        if any(word in content for word in bad_words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} That word is prohibited in this server.")

async def setup(bot):
    await bot.add_cog(MessageFilter(bot))
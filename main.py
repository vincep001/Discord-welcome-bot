import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class MyBot(commands.Bot):

    async def setup_hook(self):

        await self.load_extension('commands.general')
        await self.load_extension('commands.admin')
        await self.load_extension('events.messfilters')

        print("All extension are now connected.")

bot = MyBot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    print(f"{bot.user.name} is now activated.")


@bot.event
async def on_command_error(ctx, error):
    
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command doesn't exist. Type !help to see available commands.")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

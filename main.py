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




bot = commands.Bot(command_prefix='!', intents=intents)
#end of header

admin_role = "Admin"

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now activated.")

#message bad words filters
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
 
    if "tite" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - bad yan, kikissan kita sge ka!")
    if "burat" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - bad yan, kikissan kita sge ka!")
    if "tanginamo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - bad yan, kikissan kita sge ka!")
    if "tangina" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - bad yan, kikissan kita sge ka!")
    if "bobo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - bad yan, kikissan kita sge ka!")

    await bot.process_commands(message)




#chat commands
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hayoo {ctx.author.mention} bibigwasan na kita!")

@bot.command()
async def yo(ctx):
    await ctx.send(f"wazzup {ctx.author.mention}G nigga!")

@bot.command()
async def serverquote(ctx):
    await ctx.send("DAILY QUOTE: Time is precious.")



#administrator commands
@bot.command()
@commands.has_permissions(administrator=True)
async def assign_admin(ctx):
    role = discord.utils.get(ctx.guild.roles, name=admin_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {admin_role}")

    else:
        await ctx.send("walang gantong role obob!")


@bot.command()
@commands.has_permissions(administrator=True)
async def remove_admin(ctx):
    role = discord.utils.get(ctx.guild.roles, name=admin_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} is now removed to {admin_role}")

    else:
        await ctx.send("walang gantong role obob!")

@assign_admin.error
@remove_admin.error
async def admin_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")




@bot.command()
@commands.has_role(admin_role)
async def suntukan(ctx):
    await ctx.send(f"tara suntukan kinginamo {ctx.author.mention}")

@suntukan.error
async def suntukan_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Wala kang permiso na gawin yan hampas lupa!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command doesn't exist. Type !help to see available commands.")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)


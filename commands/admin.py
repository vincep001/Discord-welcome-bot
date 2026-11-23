import discord
from discord.ext import commands

admin_role = "admin"

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def assign_admin(self, ctx):
         role = discord.utils.get(ctx.guild.roles, name=admin_role)

         if role:
            await ctx.author.add_roles(role)
            await ctx.send(f"{ctx.author.mention} is now assigned to {admin_role}")

         else:
              await ctx.send("This role does not exist!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_admin(self, ctx):
         role = discord.utils.get(ctx.guild.roles, name=admin_role)

         if role:
             await ctx.author.remove_roles(role)
             await ctx.send(f"{ctx.author.mention} is now removed from {admin_role}")

         else:
              await ctx.send("This role does not exist!")

    @commands.command()
    @commands.has_role(admin_role)
    async def greetadmin(self, ctx):
        await ctx.send(f"welcome to administrator {ctx.author.mention}")

    @assign_admin.error
    @remove_admin.error
    async def admin_error(self, ctx, error):
          if isinstance(error, commands.MissingPermissions):
                await ctx.send("You don't have permission to use this command.")

    @greetadmin.error
    async def greetadmin_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
              await ctx.send("You don't have permission to use this command.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
            


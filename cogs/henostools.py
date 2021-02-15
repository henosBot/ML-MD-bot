import discord
from discord.ext import commands
import json
from tools.database import database as db

red = discord.Colour.red()

class henostools(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Moderator')
    async def add(self, ctx, user : discord.Member, amount : int):
        await db.save(user, 'score', amount)
        await db.save(user, 'design_count', amount / 10)
        await ctx.send(f"Added {amount} to {user.mention}'s score and {round(amount / 10)} to their dc!")

    @commands.command()
    @commands.has_role('Moderator')
    async def remove(self, ctx, user : discord.Member, amount : int):
        await db.remove(user, 'score', amount)
        await db.remove(user, 'design_count', amount / 10)
        await ctx.send(f"Removed {amount} from {user.mention}'s score and {amount / 10} from their dc!")

    @commands.command()
    @commands.has_role('Moderator')
    async def set(self, ctx, user : discord.Member, amount : int):
        await db.set(user, 'score', amount)
        await db.set(user, 'design_count', round(amount / 10))
        await ctx.send(f"Set {user.mention}'s score as {amount} and {amount / 10} as their dc!")
    
    @commands.command()
    @commands.has_role('Moderator')
    async def logs(self, ctx):
        with open('log.json', 'r') as rf:
            log = json.load(rf)
        msg = 'User: Time:\n'
        for user in list(log):
            msg += f'{str(ctx.guild.get_member(int(user)))}: {log[user]}\n'
        embed = discord.Embed(
          title='Log of cooldown penaltys',
          description=msg,
          colour=red
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(henostools(bot))
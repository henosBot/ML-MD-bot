import discord
from discord.ext import commands
import math

red = discord.Colour.red()

class Damage_Calculator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def dmgcalc(self, ctx, power : int, dmg : int, lvlme : int, lvlopp : int, runelvl : int=10, relic : int=1, other : int=1):
        result = math.floor(math.floor(math.floor(math.floor(power*runelvl+relic)*dmg/50)*(lvlme+5)/50)*(1+max(lvlme-lvlopp, 0)/50)*other)
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Damage_Calculator(bot))
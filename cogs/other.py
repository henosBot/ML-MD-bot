import discord
from discord.ext import commands

red = discord.Colour.red()

class other(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
        title="__Pong__",
        description=f'{round(self.bot.latency * 1000)} ms',
        colour=red
            )
        await ctx.send(embed=embed)

    @commands.command()
    async def embedify(self, ctx, titletag, title, bodytag, body, footertag, footer, colourtag, colour : discord.Colour):
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(
            title=title,
            description=body,
            colour=colour
        )
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def reactify(self, ctx, messageid: int, *reactions):
        await ctx.channel.purge(limit=1)
        message = await ctx.channel.fetch_message(messageid)
        for reaction in reactions:
            await message.add_reaction(reaction)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1000):
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(    
        title='__Clear!__',
        description=f'{ctx.author.mention}, I have cleared some messages for you',
        colour=red
        )
        await embed.set_footer(text=f'Deleting in 30 seconds')
        await ctx.send(embed=embed, delete_after=30)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed=discord.Embed(
        title='__Ban!__',
        description=f'{member.name}#{member.discriminator} was banned from {member.guild.name}',
        colour=red
        )
        await embed.set_footer(text=f'Reason: {reason}')
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed=discord.Embed(
        title='__Kick!__',
        description=f'{member.name}#{member.discriminator} was kicked from {member.guild.name}',
        colour=red
        )
        await embed.set_footer(text=f'Reason: {reason}')
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *,member):
        unbanned_member = discord.Object(id=int(member.id))
        await member.unban(unbanned_member)
        embed=discord.Embed(
        title='__Unban!__',
        description='{member.name}#{member.discriminator} was unbaned from {member.guild.name}',
        colour=red
        )
        await embed.set_footer(text='they can now rejoin')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(other(bot))
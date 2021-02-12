import discord
import json
import datetime
from discord.ext import commands
from discord_slash import SlashCommand, cog_ext
from discord_slash.utils import manage_commands
from tools.database import database as db

class Submissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.slash.get_cog_commands(self)

    def cog_unload(self):
        self.bot.slash.remove_cog_commands(self)
    
    @cog_ext.cog_slash(
        name='new',
        description='Submits a new design',
        guild_ids=[732921652312276992],
        options=[
            manage_commands.create_option(
            name = "Name",
            description = "the name of the design",
            option_type = 3,
            required = True
        ),
            manage_commands.create_option(
                name = "Design",
                description = "enter the id of the message that you sent the design in",
                option_type = 3,
                required = False
        )]
    )
    async def new(self, ctx, name : str, design : int or None):
        await db.save(ctx.author, 'score', 10)
        await db.save(ctx.author, 'design_count', 1)
        embed=discord.Embed(
            title=f'{ctx.author.name} has posted a new {name}',
            description=f'Here it is:\n{design}'
        )
        embed.set_footer(text='Do you like it? 🤔')
        await ctx.send(f'{name} submitted succesfully')
        channel = 747144603077050498
        channel = ctx.guild.get_channel(channel)
        await channel.send('<@&747148925219111002>', embed=embed)
    
    # @new.error
    # async def new_error(self, ctx, error):
    #     if not isinstance(error, commands.CommandOnCooldown):
    #         return
    #     with open('log.json', 'r') as rf:
    #         log = json.load(rf)
    #     log[str(ctx.author.id)] = str(datetime.datetime.now())
    #     with open('log.json', 'w') as wf:
    #         json.dump(log, wf)
    #     await ctx.send(f'{ctx.author.mention} just breached the cooldown :(\nThey received a penalty')
    #     channel = ctx.guild.get_channel(765451801163857951)
    #     await channel.send(f'{ctx.author.mention} just breached the cooldown :(\nThey received a penalty')
    
    @cog_ext.cog_slash(
        name='score',
        description='Sees your, or another user\'s score',
        guild_ids=[732921652312276992],
        options=[
            manage_commands.create_option(
            name = "User",
            description = "the user you want to see the score of",
            option_type = 3,
            required = False
        )]
    )
    async def score(self, ctx, user : discord.Member = None):
        user = user or ctx.author
        await db.open_account(user)
        score = await db.get(user, 'score')
        dc = await db.get(user, 'design_count')
        embed = discord.Embed(
          title=f"{user.name}'s score",
          description=f"__Score:__ {score}\n__Design Count:__ {dc}",
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Submissions(bot))
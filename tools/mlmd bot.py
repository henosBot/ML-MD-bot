import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
status = 'ML:  Monster Designers'

class MLMD_bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('mlmd: ', 'mlmd:', 'Mlmd:', 'Mlmd: ', 'MLMD:', 'MLMD: '),
            intents=intents,
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=status
                )
        )
    
    async def on_ready(self)
        print()
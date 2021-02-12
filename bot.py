import discord
from tools.mlmd_bot import MLMD_bot
from discord_slash import SlashCommand
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv('TOKEN')

bot = MLMD_bot()
bot.slash = SlashCommand(bot, auto_register=True)
bot.set_embed_color(discord.Colour.red())

bot.load_extension('cogs.submissions')

bot.run(token)
import discord
from tools.mlmd_bot import MLMD_bot
from discord_slash import SlashCommand
import dotenv
import os
import jishaku

dotenv.load_dotenv()
token = os.getenv('TOKEN')

bot = MLMD_bot()
bot.slash = SlashCommand(bot, sync_commands=True)
bot.set_embed_color(discord.Colour.red())

bot.remove_command('help')
extentions = [
  'cogs.henostools',
  'cogs.other',
  'cogs.submissions',
  'cogs.dmgcalc',
  'jishaku',
  'cogs.help'
]
for extention in extentions:
    bot.load_extension(extention)

bot.run(token)
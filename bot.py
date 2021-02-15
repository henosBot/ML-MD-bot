import os
print('installing packages')
os.system('pip install -r requirements.txt')

import discord
from tools.mlmd_bot import MLMD_bot
from discord_slash import SlashCommand
import toml
import jishaku

toml = toml.load('secrets.toml')
token = toml['TOKEN']

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
    print(f'Loading extension {extention}')
    bot.load_extension(extention)

os.system('clear')

bot.run(token)
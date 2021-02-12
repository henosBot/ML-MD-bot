import discord
red = discord.Colour.red()

helpdict = {
  1: discord.Embed(
    title='ML: MD bot Help:',
    description='''
    Key: <arg> - required argument, [arg] - optional argument
    Submissions:
    `/new <name> [design]` - Submits a monster/trait/etc.. and updates your score and dc
    `/score [user]` - Shows your current score and dc
    ''',
    colour=red
  ),
  2: discord.Embed(
    title='ML: MD bot Help:',
    description='''
    Key: <arg> - required argument, [arg] - optional argument
    Damage Calculator:
    `mlmd: dmgcalc <power> <pmg> <lvlme> <lvlopp> [runelvl] [relic] [other]` - Calculates the amount of damage a move will deal
    ''',
    colour=red
  ),
  3: discord.Embed(
    title='ML: MD bot Help:',
    description='''
    Key: <arg> - required argument, [arg] - optional argument
    Other:
    `mlmd: ping` - Shows the bots ping
    `mlmd: embedify <title> <body> <footer> <colour>` - Creates an embed
    `mlmd: reacify <mesage> <reactions>` - Adds reactions to a message.
    ''',
    colour=red
  ),
  4: discord.Embed(
    title='ML: MD bot Help:',
    description='''
    Key: <arg> - required argument, [arg] - optional argument
    Moderation:
    `mlmd: clear [amount]` - Clears the amount of messages
    `mlmd: ban <user>` - Bans the User
    `mlmd: unban <user>` - Unbans the user
    ''',
    colour=red
  ),
  5: discord.Embed(
    title='ML: MD bot Help:',
    description='''
    Key: <arg> - required argument, [arg] - optional argument
    modtools:
    `mlmd: add <user> <amount>` - Adds to your score and dc
    `mlmd: remove <user> <amount>` - Removes from your score and dc
    `mlmd: set <user> <amount>` - sets score and dc to the amount
    ''',
    colour=red
  ),
  6: discord.Embed(
    title='ML: MD bot Help:',
    description='''
    Key: <arg> - required argument, [arg] - optional argument
    Help:
    `mlmd: help` - Shows this, use the arrows to change page
    ''',
    colour=red
  ),
}
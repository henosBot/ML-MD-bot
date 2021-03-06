import discord
from discord.ext import commands
from tools.database import database as db
from tools import react_roles

import henostools
import hcolours

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
    
    async def on_ready(self):
        print(f'{self.user} is online!')
        await henostools.sleep('5s')
        print(f'{hcolours.colour.red}Member Count:{hcolours.reset} {len(self.users)}')
    
    async def on_command_error(self, ctx, error):
        if not isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                title='Oh no!',
                description=f'There was a error with the {ctx.command.name} command\n\nError: {error}',
                )
            await ctx.send(embed=embed)
        else:
            await ctx.send('Command not found')
        
    async def on_message(self, message):
        await db.open_account(message.author)
        reason = 'score autorole'
        score = await db.get(message.author, 'score')
        roles = {
            500: 736919708179234867,
            400: 738488304948871309,
            300: 772925251889135627,
            200: 736919360047677450,
            150: 738488670344052798,
            100: 738488853110849566,
            75: 738488995927031898,
            50: 738489190450331799,
            25: 738489281647214612,
            10: 736919165704863755
            }
        levels = [500, 400, 300, 200, 150, 100, 75, 50, 25, 10]
        if score in levels and message.guild.get_role(roles[score]) not in message.author.roles:
            role = message.guild.get_role(roles[score])
        else:
            return await self.process_commands(message)
        embed = discord.Embed(
                title='Level Up!!',
                description=f'{message.author.mention} leveled up to {role.mention}!!',
                )
        embed.set_footer(text='Well Done!')
        channel = message.guild.get_channel(772925251889135627)
        await channel.send(embed=embed)
        await message.author.add_roles(role, reason=reason)
        await self.process_commands(message)
    
    async def on_member_join(self, member):
        channel = 747144549226381382
        channel = self.get_channel(channel)
        try:
            await member.send(
                f'Hi {member.name}, welcome to {member.guild.name}!, use `mlmd: help` to get a list of the commands'
            )
        except:
            pass
        await channel.send(
            f'Hi {member.name}, welcome to {member.guild.name}!, use `mlmd: help` to get a list of the commands'
        )
        if not member.bot:
            await member.add_roles(discord.utils.get(member.guild.roles, name='People'))
    
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 776386350064599072:
            roles = self.get_guild(payload.guild_id)
            member = roles.get_member(payload.user_id)
            roles = roles.roles
            role = discord.utils.get(roles, name=react_roles.colours[payload.emoji.name])
            await member.add_roles(role)
        elif payload.message_id == 776395510370009090:
            roles = self.get_guild(payload.guild_id)
            member = roles.get_member(payload.user_id)
            roles = roles.roles
            role = discord.utils.get(roles, name=react_roles.pingroles[payload.emoji.name])
            await member.add_roles(role)
        elif payload.message_id == 780375320125112360:
            roles = self.get_guild(payload.guild_id)
            member = roles.get_member(payload.user_id)
            roles = roles.roles
            role = discord.utils.get(roles, name=react_roles.otherroles[payload.emoji.name])
            await member.add_roles(role)
        else:
            return

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 776386350064599072:
            roles = self.get_guild(payload.guild_id)
            member = roles.get_member(payload.user_id)
            roles = roles.roles
            role = discord.utils.get(roles, name=react_roles.colours[payload.emoji.name])
            await member.remove_roles(role)
        elif payload.message_id == 776395510370009090:
            roles = self.get_guild(payload.guild_id)
            member = roles.get_member(payload.user_id)
            roles = roles.roles
            role = discord.utils.get(roles, name=react_roles.pingroles[payload.emoji.name])
            await member.remove_roles(role)
        elif payload.message_id == 780375320125112360:
            roles = self.get_guild(payload.guild_id)
            member = roles.get_member(payload.user_id)
            roles = roles.roles
            role = discord.utils.get(roles, name=react_roles.otherroles[payload.emoji.name])
            await member.remove_roles(role)
        else:
            return
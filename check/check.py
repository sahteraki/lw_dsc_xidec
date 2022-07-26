
import discord
from discord.ext import commands



class CheckAuth():   
    async def is_command_management(ctx):
        return ctx.channel.name=='bot_management'
    async def is_channel(ctx):
        return ctx.channel.name=='bot'
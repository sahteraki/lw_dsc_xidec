
from distutils import extension
import command_controller
import os
import discord
from discord.ext import commands
import config
from check.check import CheckAuth


bot=commands.Bot(command_prefix='!')


is_command_management=CheckAuth.is_command_management

@bot.event
async def on_ready():
    print('Ready!')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # await get_context.send('asdasf')

@bot.event
async def on_command_not_found(ctx,command,params):
    await ctx.send('Command not found, Use !help see all commands that are available')
    await ctx.send('------')
    # await get_context.send('asdasf')

@bot.event
async def on_command_error(ctx,error):
    await ctx.send('This command is not available for this channel or wrong, Please check your command and Use !help see all commands that are available')
    await ctx.send('!help')
@bot.event
async def on_command_permission_error(ctx,error):
    await ctx.send('You do not have permission to use this command')
    await ctx.send('!help')





@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx,amount=500):
        print(dir(ctx))
        print(ctx.channel)
        print(type(ctx.channel))
        await ctx.channel.purge(limit=amount)




@bot.command()
@commands.check(is_command_management)
@commands.has_permissions(administrator=True)
async def load(ctx,extension):
 
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.check(is_command_management)
@commands.has_permissions(administrator=True)
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx,*extension:str):
#  if ctx.channel.name=='bot'
    if ctx.channel.name=='bot_management':
        if extension==():
        #get all extensions from cog file
            for file in os.listdir('./cogs'):
                if file.endswith(".py"):
                    extensions=file[:-3]
                    bot.unload_extension(f'cogs.{extensions}')
                    bot.load_extension(f'cogs.{extensions}')
                    await ctx.send('Reloaded %s'%extensions)
        if extension:
            await ctx.send('extension %s reloaded'%extension)
            bot.unload_extension(f'cogs.{extension[0]}')
            bot.load_extension(f'cogs.{extension[0]}')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run(config.Config.bot_token)


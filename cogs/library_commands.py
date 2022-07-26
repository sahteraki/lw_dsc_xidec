
import json
import os
from unicodedata import name
from attr import attr, attrs
import discord
from discord.ext import commands
from check.check import CheckAuth
import command_controller

from main import clear

commands_list=[]

def update_commands_list(commands_list):
    commannds_list=[]
    for file in os.listdir('./commands'):
        if file.endswith(".json"):
            commands_list.append(file[:-5])
    return commands_list

update_commands_list(commands_list)

is_channel=CheckAuth.is_channel
is_command_management=CheckAuth.is_command_management


class LibraryCommands(commands.Cog):
    def __init__(self,bot) :
        self.bot=bot

        
    





        



    @commands.command(name='list',help='Use !list or !commands to usable commands list',aliases=["commands"])
    @commands.check(is_channel)
    async def list_commands_embed(self,ctx):
        commands_list_json=[]
        for file in os.listdir('./commands'):
            if file.endswith(".json"):
                #get the json file and assign it to commandJson
                commandJson=json.load(open(f'./commands/{file}'))
                commands_list_json.append(commandJson)

        descriptions=[]
        for command in commands_list_json:
            descriptions.append(command['commandName'])
        
        emb=discord.Embed(title=":information_source: Here is the list of commands that you can use.\n\nExample Usage: !show OB :arrow_down:",description="\n !show ".join(descriptions),color=0x00ff00)
        #print commands_list_json as dic
        await ctx.send(embed=emb)
        # emb=discord.Embed(title="Commands"
        # # ,description=
        # ,color=0x00ff00)





    @commands.command(name='show',help='!show commandName to see commands')
    @commands.check(is_channel)
    async def cmmnd(self,ctx,*,arg):

        if arg in commands_list:
            for i in commands_list:
                if i == arg:
                    with open(f'commands/{i}.json',encoding='utf-8') as f:
                        data = json.load(f)
                        await ctx.send(':speaking_head:'+ (data['description']).upper())
                        for j in data['content']:
                            await ctx.send(j)

                  



def setup(bot):
    bot.add_cog(LibraryCommands(bot))


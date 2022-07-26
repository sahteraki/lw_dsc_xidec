import main
import json
from check.check import CheckAuth
import os
from unicodedata import name
from attr import attr, attrs
import discord
from discord.ext import commands
import command_controller

from main import clear

commands_list=[]

is_command_management=CheckAuth.is_command_management
is_channel=CheckAuth.is_channel

def update_commands_list(commands_list):
    commannds_list=[]
    for file in os.listdir('./commands'):
        if file.endswith(".json"):
            commands_list.append(file[:-5])
    return commands_list

update_commands_list(commands_list)



class ManagementCommands(commands.Cog):
    def __init__(self,bot) :
        self.bot=bot





    @commands.command(help='Ex: "command name" "command description" "content1,content2"')
    # @commands.check(is_command_management)
    @commands.check(is_command_management)
    @commands.has_permissions(administrator=True)
    async def add(self,ctx,commandName,description=" ",content=""):
        #seperate the content into a list if has ,
        content=content.split(',')
        await command_controller.createCommand(commandName,description,content)
        await ctx.send("Command added")
        commands_list.append(commandName)
        await ctx.send("Command list updated")
        await main.reload(ctx,'management_commands')

    @commands.check(is_command_management)
    @commands.has_permissions(administrator=True)
    @commands.command(name="update",help='Ex:!update "commanName" "description or content" "xxx"')
    async def update_command(self,ctx,commandName,*arg1):
        await command_controller.updateCommands(commandName,*arg1)
        await ctx.send("Command and command list updated")
        #update commands list

        #reload librarry_commands file
        await main.reload(ctx,'management_commands')

    @commands.check(is_command_management)
    @commands.has_permissions(administrator=True)
    @commands.command(name='delete',help='Use!delete,!del,!remove to delete command Ex: !del commandName',aliases=["remove","del"])
    async def delete_command(self,ctx,commandName):
        await  ctx.send("Command deleted and command list updated")
        await command_controller.deleteCommand(commandName)
        #update commands list

        #reload librarry_commands file

        await main.reload(ctx,'management_commands')


    @commands.check(is_command_management)
    @commands.has_permissions(administrator=True)
    @commands.command(name='delete_all',help='!delete_all,!remove_all,!del_all deletes all commands ',aliases=["remove_all","del_all"])
    async def delete_all_commands(self,ctx):
        await ctx.send("All commands deleted and command list updated")
        await command_controller.deleteAllCommands()
  
        #update command list

        #reload librarry_commands file
        await main.reload(ctx,'management_commands')

    @commands.command(name='mlist',help='Use !mlist to see commands list ManagementChannel')
    @commands.check(is_command_management)
    async def mlist_commands_embed(self,ctx):
        commands_list_json=[]
        for file in os.listdir('./commands'):
            if file.endswith(".json"):
                #get the json file and assign it to commandJson
                commandJson=json.load(open(f'./commands/{file}'))
                commands_list_json.append(commandJson)

        descriptions=[]
        for command in commands_list_json:
            descriptions.append(command['commandName'])
        
        emb=discord.Embed(title=":information_source: Here is the list of commands that you can use\nThis command is same as !list and only for management channel \nEx: !mshow OB :arrow_down:"  ,description="\n!mshow".join(descriptions),color=0x00ff00)
        #print commands_list_json as dic
        await ctx.send(embed=emb)
        # emb=discord.Embed(title="Commands"
        # # ,description=
        # ,color=0x00ff00)
    @commands.command(name='mshow',help='!mshow commandName to see commands ManagementChannel')
    @commands.check(is_command_management)
    async def mcmmnd(self,ctx,*,arg):

        if arg in commands_list:
            for i in commands_list:
                if i == arg:
                    with open(f'commands/{i}.json',encoding='utf-8') as f:
                        data = json.load(f)
                        await ctx.send(':speaking_head:'+ (data['description']).upper())
                        for j in data['content']:
                            await ctx.send(j)


def setup(bot):
    bot.add_cog(ManagementCommands(bot))
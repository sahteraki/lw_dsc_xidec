
import json
from json import JSONEncoder
import os

class Command():
    def _init_(self,commandName,description,content):
        self.commandName=commandName
        self.description=description
        self.content=content
    
    def toJSON(self):
        return json.dumps(self,default=lambda o: o.__dict__,sort_keys=True,indent=4)

async def createCommand(commandName,description,content):
    def deleteSpace(commandName):
        if commandName.find(" ")!=-1:
            commandName=commandName.replace(" ","_")
        return commandName
    commandName=deleteSpace(commandName)
    commandName=commandName.lower()

    command= Command()
    command.commandName=commandName
    command.description=description
    command.content=content
    commandJson=json.loads(command.toJSON())

    with open('./commands/%s.json'%commandName,'w',encoding='utf-8') as f:
        json.dump(commandJson,f,indent=4)

async def deleteCommand(commandName):
    commandName=replaceUppercase(commandName)
    commandName=commandName.lower()
    os.remove('./commands/%s.json'%commandName)
async def deleteAllCommands():
    for file in os.listdir('./commands'):
        if file.endswith(".json"):
            os.remove('./commands/%s'%file)

async def updateCommands(commandName,*arg1):
    #get json file where commands folder which is same as commandName and assign it to commandJson
    with open('./commands/%s.json'%commandName,'r',encoding='utf-8') as f:
       commandJson=json.load(f)
       commandName=commandJson['commandName']
       description=commandJson['description']
       content=commandJson['content'] 
       if arg1 and arg1[0]=='description':
            description=description+",\n "+arg1[1]
       if arg1 and arg1[0]=='content':
            for i in range(1,len(arg1)):
                content.append(arg1[i])
    await createCommand(commandName,description,content)









#replace uppercase with lowercase
def replaceUppercase(description):
    return description.lower()



# commandJsonData=json.dumps(command.toJSON())
# # print(commandJsonData)
# print(type(commandJsonData))
# # print(commandJsonData)

# commandJson=json.loads(command.toJSON())
# print(commandJson)
# print(type(commandJson))


#create a json file and write the data into it
# with open('./commands/%s.json'%'yarak','w') as f:
#     json.dump(commandJson,f,indent=4)


#append commandJson to commands.json file start from last character

# with open("commands.json","a") as f:
#     f.write(",\n")
#     f.write(command.toJSON())
#     # json.dump(commandJson,f)
#     f.close()



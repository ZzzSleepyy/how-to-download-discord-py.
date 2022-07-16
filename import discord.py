#download https://code.visualstudio.com #your main coding software 

---------------------------------------------------------------------
#download https://www.python.org/downloads/ #latest version

---------------------------------------------------------------------
#create a file containing python program
#name the file main.py
---------------------------------------------------------------------
#INSIDE THE FILE

#download pip install discord.py in your terminal/command prompt

import discord #imports discord
intents = discord.Intents.default()# optional but this can be handy one day.
bot = commands.Bot(command_prefix='your prefix' ,intents=intents) #runs your prefix from using @bot.commands().


@bot.event
async def on_ready(): #bot will run when it is ready
    await bot.change_presence(status=discord.Status.dnd)# if you want the bot do not disturb or add (status=discord.Status.Online) 
                                                          or (status=discord.Status.Idle)
    print("Your bot is now Online!")# informs you that your bot is online!






bot.run('TOKEN')# ADD YOUR TOKEN HERE.



















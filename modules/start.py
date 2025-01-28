import os, colorama, random
import time as tm
from termcolor import colored

import cffi, pycparser, nacl
from io import BytesIO
from discord import app_commands
import youtube_dl
import DiscordUtils

from datetime import datetime

colorama.init()

try: 
    import discord
    from discord.ext import commands
    from discord.ext.commands import Context
except:
    os.system("python -m pip install discord")
    import discord
    from discord.ext import commands
    

token = ""
prefix = "r."

music = DiscordUtils.Music()

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
client.remove_command("help")

help_menu = f"""
Available commands for the bot :

**{prefix}help** - Show this message.

:green_circle: Activations

**{prefix}hi** - Repeat a few words.
"""


@client.event
async def on_ready():
    os.system("cls")
    print(colored(f"Bot initialized as: {client.user}",'blue'))
    print("")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(S)")
    except Exception as e:
        print(e)
# commands

@client.command()
async def help(ctx):
    print(colored("Bot - HELP MENU RECEIVED",'magenta'))
    if ctx.guild:
        await ctx.message.delete()
    try:
        await ctx.message.reply(help_menu)
    except:
        await ctx.send(help_menu)

@client.command()
async def hi(ctx):
    if ctx.guild:
        
        guild = ctx.guild if ctx.guild else client.get_guild(int(guildid))
        
        time = datetime.now().strftime("%H:%M:%S")
        await ctx.message.reply("Hello!")   
        print(colored(f"{time}", 'white'), colored(f"Bot said Hello to {ctx.message.author}", 'green'), colored(ctx.message.author, 'magenta'))

embed = discord.Embed(
    title=":tools: MAINTENANCE :tools:",
    description="We regret to inform you that the bot service is currently offline due to updates and maintenance.",
    color=discord.Color(int("b8a88e", 16))  # Specifica un colore per l'embed (opzionale)
)

# Aggiungere un campo all'embed (opzionale)
embed.add_field(name="Error value:", value="503", inline=True)
embed.add_field(name="End of maintenance:", value="12/24h", inline=True)

# Aggiungere un'immagine in miniatura all'embed (opzionale)
embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/209/PNG/256/maintenance256_24835.png")

# Aggiungere un footer all'embed (opzionale)
embed.set_footer(text="Powered by bot")
    
@client.tree.command(name="vote", description="vote me on top gg")
async def vote(interaction: discord.Interaction):
    await interaction.response.send_message(embed=embed)
    
os.system("title Bot")
client.run(token)

input()

import requests
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='&', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name="Bypass command is &bypass!"))

@client.command()
async def bypass(ctx, key):
    try:
        linkvertise_link = key
        if linkvertise_link.startswith(("http://", "https://")):
            destination_url = requests.get(f"https://bypass.bot.nu/bypass2?url={linkvertise_link}").json()["destination"]
            await ctx.send(f'`Heres the bypassed url \'{destination_url}\'`')
        else: 
            await ctx.send('`You must put a valid link`')
    except: 
        await ctx.send('`You must put a valid link`')
 



client.run('token')
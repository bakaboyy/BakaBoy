import os
import json
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
from utils.cracker import Crack

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
PROXIES_FILE = 'proxies.json'  # Assuming proxies are stored in proxies.json

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Load proxies from proxies.json
def load_proxies():
    with open(PROXIES_FILE, 'r') as f:
        proxies = json.load(f)
    return proxies

proxies = load_proxies()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send('Starting the cracking process...')
    # Example usage of proxies with requests library
    session = requests.Session()
    session.proxies.update(proxies)  # Update session with proxies

    # You would use the session to make requests here
    # Example:
    # response = session.get('https://example.com')
    # print(response.text)

    # Example using your Crack class with proxies
    Crack(session).start()

    await ctx.send('Cracking process completed.')

@bot.command()
async def commands(ctx):
    commands_list = """
    Available commands:
    /start - Start the cracking process
    /commands - List all available commands
    """
    await ctx.send(commands_list)

bot.run(TOKEN)

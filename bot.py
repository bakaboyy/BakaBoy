import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.cracker import Crack

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def start(ctx):
    await ctx.send('Starting the cracking process...')
    Crack().start()
    await ctx.send('Cracking process completed.')

@bot.command()
async def commands(ctx):
    commands_list = """
    Available commands:
    /start - Start the cracking process
    /commands - List all available commands
    """
    await ctx.send(commands_list)

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
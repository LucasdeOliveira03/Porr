import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv
from phrase import load_phrase


load_dotenv()
info = "counter.json"

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

def loadCounter():
    try:
        with open(info, "r") as file:
            data = json.load(file)
            return data.get("counter", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def saveCounter(value):
    with open(info, "w") as file:
        json.dump({"counter": value}, file)

counter = loadCounter()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def porr(ctx):
    counter = loadCounter()
    counter += 1
    saveCounter(counter)

    phrase = load_phrase(counter)
    
    await ctx.send(phrase)

@bot.command()
async def contagem(ctx):
    counter = loadCounter()
    await ctx.send(f"Nicolas errou {counter} vezes até hoje")

bot.run(os.getenv("TOKEN"))
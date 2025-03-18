import discord
import os
import json
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
conta = "porr_counter.json"

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

def load_counter():
    try:
        with open(conta, "r") as file:
            data = json.load(file)
            return data.get("counter", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def save_counter(value):
    with open(conta, "w") as file:
        json.dump({"counter": value}, file)

counter = load_counter()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def porr(ctx):
    counter = load_counter()
    counter += 1
    save_counter(counter)
    if counter != 1:
        await ctx.send(f"Nicolas errou {counter} vezes até hoje")
    else:
        await ctx.send(f"Nicolas, parabens ao errar pela primeira vez")

@bot.command()
async def contagem(ctx):
    counter = load_counter()
    await ctx.send(f"Nicolas errou {counter} vezes até hoje")

bot.run(os.getenv("TOKEN"))
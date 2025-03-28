import discord
import os
import json
import random
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
info = "porr_counter.json"
phrase = ""

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

def load_phrase(counter):
    N = random.randrange(0, 16)

    match N:
        case 0:
            phrase = f"Nicolas deu mole {counter} vezes. Tá treinando pra errar mais?"
        case 1:
            phrase = f"Mais um vacilo. Já são {counter}, vai querer bater recorde?"
        case 2:
            phrase = f"Putz, Nicolas. {counter} erros já. Bora dobrar esse número?"
        case 3:
            phrase = f"E lá vamos nós… Nicolas já se embolou {counter} vezes."
        case 4:
            phrase = f"Tá difícil, hein? {counter} erros e contando"
        case 5:
            phrase = f"Mais um tropeço pro currículo! {counter} erros registrados."
        case 6:
            phrase = f"Nicolas errou {counter} vezes. Será que chega nos {counter+5} hoje?"
        case 7:
            phrase = f"Nicolas errou {counter} vezes até hoje"
        case 8:
            phrase = f"Opa, mais um erro! Já são {counter}, bora tentar os {counter+2}?"
        case 9:
            phrase = f"De novo? O contador tá em {counter}"
        case 10:
            phrase = f"Nicolas rolou um 1 crítico... de novo. Já são {counter} falhas críticas acumuladas"
        case 11:
            phrase = f"O dado não tá ajudando hoje... {counter} falhas seguidas no teste de inteligência!"
        case 12:
            phrase = f"Nicolas tentou e... falhou! {counter} testes de perícia errados até agora."
        case 13:
            phrase = f"Mais um erro crítico! O contador de falhas já chegou a {counter}."
        case 14:
            phrase = f"O destino não sorriu pra você... Nicolas já errou {counter} vezes."
        case 15:
            phrase = f"Se fosse um teste de acerto, era tudo 1 no dado. {counter} vacilos anotados!"

    return phrase

def load_counter():
    try:
        with open(info, "r") as file:
            data = json.load(file)
            return data.get("counter", 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def save_counter(value):
    with open(info, "w") as file:
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

    phrase = load_phrase(counter)
    
    await ctx.send(phrase)

@bot.command()
async def contagem(ctx):
    counter = load_counter()
    await ctx.send(f"Nicolas errou {counter} vezes até hoje")

bot.run(os.getenv("TOKEN"))
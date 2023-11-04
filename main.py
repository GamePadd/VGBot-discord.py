import discord
import a2s
import datetime
import random
import math
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

PREFIX = "!"
SERVER_ADDRESS_PVE = "212.12.17.122",28015
SERVER_ADDRESS_RUST = "212.12.17.122",30015
SERVER_ADDRESS_ZN = "212.12.17.122",31015

client = commands.Bot(command_prefix=PREFIX, intents=intents) 

@client.event

async def on_ready():
    print("Connected!")
    await client.change_presence(activity=discord.Game('!зн, !пве, !раст'))

@client.command()

async def зрада(ctx):
    CNT = random.randint(0,9000)

    if CNT<=1000:
        CLR = discord.Color.red()
    if CNT>=2000:
        CLR = discord.Color.orange()
    if CNT>=5000:
        CLR = discord.Color.yellow()
    if CNT>=7000:
        CLR = discord.Color.green()

    emb = discord.Embed(title = 'Текущая Зрада', colour = CLR)

    emb.set_footer(text = "Зрадометр 1.0")
    emb.add_field(name = "--------------", value = "", inline=False)
    emb.add_field(name = str(CNT) + "%", value = "", inline=False)
    emb.add_field(name = "--------------", value = "", inline=False)

    await ctx.reply(embed = emb)

@client.command()

async def перемога(ctx):
    CNT = random.randint(0,9000)

    if CNT<=1000:
        CLR = discord.Color.red()
    if CNT>=2000:
        CLR = discord.Color.orange()
    if CNT>=5000:
        CLR = discord.Color.yellow()
    if CNT>=7000:
        CLR = discord.Color.green()

    emb = discord.Embed(title = 'Текущая Перемога', colour = CLR)

    emb.set_footer(text = "Перемометр 1.0")
    emb.add_field(name = "--------------", value = "", inline=False)
    emb.add_field(name = str(-CNT) + "%", value = "", inline=False)
    emb.add_field(name = "--------------", value = "", inline=False)

    await ctx.reply(embed = emb)

@client.command()

async def пве(ctx):
    print(a2s.info(SERVER_ADDRESS_PVE))
    print(a2s.players(SERVER_ADDRESS_PVE))

    CLR = discord.Color.green()

    emb = discord.Embed(title = a2s.info(SERVER_ADDRESS_PVE).server_name, colour = CLR)
    emb.add_field(name = "=======================================", value="", inline=False)

    COUNTER = 0

    for I in a2s.players(SERVER_ADDRESS_PVE):
        emb.add_field(name = "Игрок: " + I.name + " | Счет: " + str(I.score) + " | Время игры: " + str(datetime.timedelta(seconds = math.ceil(I.duration))), value = "",  inline=False)
        emb.set_footer(text = a2s.info(SERVER_ADDRESS_PVE).game)

        COUNTER += 1

    if COUNTER == 0:
        emb.add_field(name = "Сервер пуст",value="",inline=False)
        emb.set_footer(text = a2s.info(SERVER_ADDRESS_RUST).game)
    
    emb.add_field(name = "=======================================", value="", inline=False)

    await ctx.reply(embed = emb)

@client.command()

async def зн(ctx):
    print(a2s.info(SERVER_ADDRESS_ZN))
    print(a2s.players(SERVER_ADDRESS_ZN))

    CLR = discord.Color.green()

    emb = discord.Embed(title = a2s.info(SERVER_ADDRESS_ZN).server_name, colour = CLR)
    emb.add_field(name = "=======================================", value="", inline=False)

    COUNTER = 0

    for I in a2s.players(SERVER_ADDRESS_ZN):
        emb.add_field(name = "Игрок: " + I.name + " | Счет: " + str(I.score) + " | Время игры: " + str(datetime.timedelta(seconds = math.ceil(I.duration))), value = "",  inline=False)
        emb.set_footer(text = a2s.info(SERVER_ADDRESS_ZN).game)

        COUNTER += 1

    if COUNTER == 0:
        emb.add_field(name = "Сервер пуст",value="",inline=False)
        emb.set_footer(text = a2s.info(SERVER_ADDRESS_RUST).game)
    
    emb.add_field(name = "=======================================", value="", inline=False)

    await ctx.reply(embed = emb)

@client.command()

async def раст(ctx):
    print(a2s.info(SERVER_ADDRESS_RUST))
    print(a2s.players(SERVER_ADDRESS_RUST))

    CLR = discord.Color.green()

    emb = discord.Embed(title = a2s.info(SERVER_ADDRESS_RUST).server_name, colour = CLR)
    emb.add_field(name = "=======================================", value="", inline=False)

    COUNTER = 0

    for I in a2s.players(SERVER_ADDRESS_RUST):
        emb.add_field(name = "Игрок: " + I.name + " | Счет: " + str(I.score) + " | Время игры: " + str(datetime.timedelta(seconds = math.ceil(I.duration))), value = "",  inline=False)
        emb.set_footer(text = a2s.info(SERVER_ADDRESS_RUST).game)

        COUNTER += 1

    if COUNTER == 0:
        emb.add_field(name = "Сервер пуст",value="",inline=False)
        emb.set_footer(text = a2s.info(SERVER_ADDRESS_RUST).game)
    
    emb.add_field(name = "=======================================", value="", inline=False)

    await ctx.reply(embed = emb)

token = open("token.txt", "r").readline()
client.run(token)
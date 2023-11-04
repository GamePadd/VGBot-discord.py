import discord
import a2s
import datetime
import random
import sqlite3
import math
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

PREFIX = "!"
SERVER_ADDRESS_PVE = "212.12.17.122",28015
SERVER_ADDRESS_RUST = "212.12.17.122",30015
SERVER_ADDRESS_ZN = "212.12.17.122",31015
SERVER_ADDRESS_BULBA = "",2

client = commands.Bot(command_prefix=PREFIX, intents=intents)

def GetServerInfo(ADDRESS):
    print(a2s.info(ADDRESS))
    print(a2s.players(ADDRESS))

    CLR = discord.Color.purple()

    emb = discord.Embed(title = a2s.info(ADDRESS).server_name, colour = CLR)

    if a2s.info(ADDRESS).game == "Sven Co-op 5.25":
        GameUrl = "https://steamuserimages-a.akamaihd.net/ugc/1809893225284845336/2C844533D5DE76F2B0C8442AB6F84E9A6D660A87/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"
    else:
        GameUrl = ""
    
    emb.add_field(name = "==================================", value="", inline=False)

    COUNTER = 0

    for I in a2s.players(ADDRESS):
        emb.add_field(name = "Игрок: " + I.name + " | Счет: " + str(I.score) + " | Время игры: " + str(datetime.timedelta(seconds = math.ceil(I.duration))), value = "",  inline=False)
        emb.set_footer(text = a2s.info(ADDRESS).game,icon_url=GameUrl)

        COUNTER += 1

    if COUNTER == 0:
        emb.add_field(name = "Сервер пуст",value="",inline=False)
        emb.set_footer(text = a2s.info(ADDRESS).game,icon_url=GameUrl)
    
    emb.add_field(name = "==================================", value="", inline=False)

    return emb

@client.event

async def on_ready():
    print("Бот запущен!")
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
    emb.add_field(name = str(CNT) + "%", value = "", inline=False)

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
    emb.add_field(name = str(-CNT) + "%", value = "", inline=False)

    await ctx.reply(embed = emb)

@client.command()

async def пве(ctx):
    dokl = client.get_channel(1170339560111214683)
    await dokl.send(str(ctx.message.author.mention))
    await dokl.send(embed = GetServerInfo(SERVER_ADDRESS_PVE))

@client.command()

async def зн(ctx):
    dokl = client.get_channel(1170339560111214683)
    await dokl.send(str(ctx.message.author.mention))
    await dokl.send(embed = GetServerInfo(SERVER_ADDRESS_ZN))

@client.command()

async def раст(ctx):
    dokl = client.get_channel(1170339560111214683)
    await dokl.send(str(ctx.message.author.mention))
    await dokl.send(embed = GetServerInfo(SERVER_ADDRESS_RUST))

@client.command()

async def обновить(ctx):
    file = open("update.txt", "r")
    num = int(file.readline())+1
    file.close()

    file = open("update.txt", "w")
    file.write(str(num))
    file.close()

    upd = client.get_channel(1052635054418972773)

    await ctx.send("Обновлено!")

@client.command()
@commands.has_permissions(administrator = True)

async def обновитьБД(ctx):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Участник(
    Ник TEXT,
    Деньги INTEGER               
    )               
    """)

    con.commit()
    con.close()

    print("БД Обновлена")

@client.command()
    
async def рег(ctx):
    con = sqlite3.connect("users.db")
    cursor = con.cursor()
    cursor.execute("SELECT Ник FROM Участник")
    Already = False

    Nick = cursor.fetchall()
    for title in Nick:
        if title[0] == str(ctx.message.author):
            await ctx.reply("Ошибка, вы уже есть в Базе Данных сервера")
            Already=True

    if Already == False:
        cursor.execute("""
        INSERT INTO Участник               
        (Ник, Деньги)               
        VALUES               
        (?,?)               
        """, (str(ctx.message.author), 10))
        await ctx.reply("Вы были успешно добавлены в базу данных!")
    con.commit()
    con.close()

token = open("token.txt", "r").readline()
client.run(token)
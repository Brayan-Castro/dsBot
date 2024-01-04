import discord
import random
from discord.ext import commands
from pathlib import Path
# test commit
token = Path(__file__).with_name("token.txt").open().read()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as: {bot.user}")

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return

    if "engraçado" in message.content.lower():
        for i in range(6):
            await message.channel.send(f"NOSSA {message.author.mention} QUE ENGRAÇADO HAHAHAHAHAHA")

@bot.command(name="hi")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.message.author.name}")

@bot.command(name="r")
async def roll(ctx, args):
    numDice = ""
    maxDice = ""
    prof = ""
    rolls = []
    i = 0
    while args[i] != 'd':
        numDice += args[i]
        i += 1
    
    i += 1

    while True:
        if args[i] == '+' or args[i] == '-':
            break
        maxDice += args[i]
        i += 1

    i += 1

    while i != len(args):
        prof += args[i]
        i += 1

    for nums in range(int(numDice)):
        rolls.append(random.randint(1, int(maxDice)))

    if "+" in args:
        await ctx.reply(f"{rolls} **|** {sum(rolls)} + {prof} = **{sum(rolls) + int(prof)}**")
    elif "-" in args:
        await ctx.reply(f"{rolls} **|** {sum(rolls)} - {prof} = **{sum(rolls) - int(prof)}**")

bot.run(token)
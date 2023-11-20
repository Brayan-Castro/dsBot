import discord
import random
from discord.ext import commands

token = open("token.txt").read()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as: {bot.user}")

@bot.command(name="hi")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.message.author}")

@bot.command(name="r")
async def roll(ctx, arg):
    sumRandom = 0
    rolls = []
    numDice = int(arg[0])

    if arg[3].isdigit():
        maxDice = int(arg[2] + arg[3])
        plusMinus = arg[4]
        if arg[-2].isdigit():
            prof = int(arg[-2] + arg[-1])
        else:
            prof = int(arg[5])
    else:
        maxDice = int(arg[2])
        plusMinus = arg[3]
        prof = int(arg[4])
        if arg[-2].isdigit():
            prof = int(arg[-2] + arg[-1])
        else:
            prof = int(arg[4])
    
    
    for i in range(numDice):
        rolls.append(random.randint(1, maxDice))
        sumRandom += rolls[i]
    
    if plusMinus == "+":
        await ctx.reply(f"{rolls} - {sumRandom} + {prof} = **{sumRandom + prof}**")
    else:
        await ctx.reply(f"{rolls} - {sumRandom} + {prof} = **{sumRandom - prof}**")

bot.run(token)
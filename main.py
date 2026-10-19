import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado.")

@bot.command()
async def oi(ctx:commands.Context):
    await ctx.reply("OIIII")

@bot.command()
async def sixseven(ctx:commands.Context):
    await ctx.reply("67")

bot.run("MTU2MDc1MzY1ODAxMjkwMTQ3OA.GHovRD.drBjIQt4Q6nQFNi9nKlPIXtG175LGh6phWik5c")
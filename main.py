import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado.")

#comando pra uma pessoa específica
@bot.command()
async def oi(ctx:commands.Context):
    if ctx.author.id == 1560753658012901478:
        await ctx.reply("clbc takizawa, seu gay homofóbico")
    else:
        nome = ctx.author.mention
        await ctx.reply(f"Oiiii {nome}")

#=========================== RENAME ALL ==================================
@bot.command()
async def renameall(ctx:commands.Context, *,apelido: str):
    for membro in ctx.guild.members:
        try:
            await membro.edit(nick=apelido)
        except discord.Forbidden:
                continue
    print("Terminei de renomear todos os membros")

    for canaldetexto in ctx.guild.text_channels:
        try:
            await canaldetexto.edit(name=apelido)
        except discord.Forbidden:
            continue
    print("Terminei de renomear todos os canais de texto")

    for canaldevoz in ctx.guild.voice_channels:
        try:
            await canaldevoz.edit(name=apelido)
        except discord.Forbidden:
            continue
    print("Terminei de renomear todos os canais de voz")

    for canal in ctx.guild.categories:
        try:
            await canal.edit(name=apelido)
        except discord.Forbidden:
            continue
    print("Terminei de renomear todas categorias")
    print("Terminei tudo\n")
#===========================================================================
#comando 67
@bot.command()
async def sixseven(ctx:commands.Context):
    arquivo = discord.File("67doente.gif") #Pega o arquivo do gif na pasta
    await ctx.reply(file = arquivo)

@bot.command()
async def goonar(ctx:commands.Context, pessoa: discord.Member):
    if pessoa.id == bot.user.id:
        await ctx.reply("Impossivel pae, eu sou ingoonavel")
    else:
        arquivo = discord.File("goon.jpg")
        await ctx.reply(f"Goonei em {pessoa.mention}", file = arquivo)

@bot.command()
async def goon(ctx:commands.Context):
    arquivo = discord.File("goon.jpg")
    await ctx.reply(file = arquivo)

#============= Comando Clear ==================
@bot.command()
async def clear(ctx:commands.Context, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)
#==============================================

bot.run("token")
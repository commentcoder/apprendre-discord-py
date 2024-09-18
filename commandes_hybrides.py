import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.hybrid_command()
async def ping(ctx):
  await ctx.send("Pong !")

@bot.hybrid_command()
async def soustraire(ctx, a: int, b: int):
  await ctx.send(f"La différence entre {a} et {b} est {a - b}")

@bot.hybrid_command()
async def note(ctx, *, note: str):
  await ctx.send(f"Note : {note} enregistrée !")

@bot.event
async def on_ready():
  await bot.tree.sync()

token = "VOTRE_TOKEN"
bot.run(token=token)

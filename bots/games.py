import random
import discord
from discord.ext import commands

token = ""

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@commands.command()
async def roll(ctx):
  result = random.randint(1, 6)
  await ctx.send(f'{ctx.author.name} lance un dé et obtient : {result}')

@bot.hybrid_command()
async def pileouface(ctx):
  result = random.choice(['pile', 'face'])
  await ctx.send(f'Résulat obtenu : {result}')

@bot.event
async def on_ready():
  await bot.tree.sync()

bot.run(token=token) 

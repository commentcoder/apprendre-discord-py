import discord
from discord.ext import commands

token = ""
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command(name="bonjour_monde", aliases=['hw', 'hello_world'])
async def hello_world(context):
  await context.send("Hello, World!") 


@bot.command()
async def decompte(context, delai: int):
  await context.send("Départ dans ...")
  for i in range(delai, 0, -1):
    await context.send(i)
  await context.send("C'est parti !")


@bot.command(
  description="Répète du texte qu'on lui passe",
  brief="Répète du texte",
  help="Encore plus d'aide",
  hidden=False
)
async def repeter(context, *, message):
  """Répète du texte qu'on lui passe (docstring)"""
  await context.send(message)


if __name__ == '__main__': 
  bot.run(token=token)

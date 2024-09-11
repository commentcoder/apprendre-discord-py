import discord

token = "VOTRE_TOKEN"

client = discord.Client(intents=discord.Intents.all())

client.run(token=token)

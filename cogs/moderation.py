import discord
from discord.ext import commands

class ModerationCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} a été exclu(e).')

async def setup(bot):
  await bot.add_cog(ModerationCog(bot))

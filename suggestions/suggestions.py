import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)

class Suggestions(commands.Cog):
  """Tool for collecting suggestions in a specified channel."""

  def __init__(self, bot):
    self.bot = bot
    self.db = bot.plugin_db.get_partition(self)
    bot.loop.create_task(self.initialize())

  async def initialize(self):
    return

  @commands.group(name="suggestions", invoke_without_command=True)
  @checks.has_permissions(PermissionLevel.ADMIN)
  async def suggestions(self, ctx):
    """"Commands for interacting with the suggestions system."""

    await ctx.send_help(ctx.command)

  @suggestions.command()
  async def channel(self, ctx):
    """Set the collector channel for suggestions."""


  @suggestions.command()
  async def enable(self, ctx):
    """Enable suggestions collection."""

  @suggestions.command()
  async def disable(self, ctx):
    """Disable suggestions collection."""

  @suggestions.command()
  async def blacklist(self, ctx):
    """Prevent a user from submitting suggestions."""

  @suggestions.command()
  async def whitelist(self, ctx):
    """Allow a user to submit suggestions."""

  @suggestions.command()
  async def info(self, ctx):
    """See info about a suggestion."""

  @commands.command()
  async def accept(self, ctx):
    """Mark a submission as accepted."""

  @commands.command()
  async def deny(self, ctc):
    """Mark a submission as denied."""

  @commands.command()
  async def dupe(self, ctx):
    """Mark a submission as a duplicate."""
  
  @commands.command()
  async def onhold(self, ctx):
    """Mark a submission as on-hold."""

  @commands.command()
  async def remove(self, ctx):
    """Deny and remove a suggestion."""

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author.bot:
      return
    
    if self.enabled is False or self.channel is None:
      return

    if message.content.startswith(self.bot.prefix):
      await message.delete()
      return

    if message.author.id in self.blacklist:
      await message.delete()
      return

def setup(bot):
  bot.add_cog(Suggestions(bot))
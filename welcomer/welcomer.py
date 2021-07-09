import ast

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)

class Welcomer(commands.Cog):
  """Tools for managing a welcome message."""

  def __init__(self, bot):
    self.bot = bot
    self.db = bot.plugin_db.get_partition(self)
    self.enabled = False
    self.message = {
      "title": "Welcome to the server!",
      "description": "Make sure you read over our community guidelines."
    }
    bot.loop.create_task(self.initialize())

  async def initialize(self):
    config = await self.db.find_one({"_id": "config"})

    if config is None:
      logger.warning("Welcomer plugin has not been configured.")
    else:
      self.message = config["welcome_message"]
      self.enabled = True

  @commands.group(name="welcomer", aliases=["welcome"], invoke_without_command=True)
  async def welcomer(self, ctx):
    """Create, save, and edit the welcome message."""
    
    await ctx.send_help(ctx.command)

  @welcomer.command()
  @checks.has_permissions(PermissionLevel.ADMIN)
  async def enable(self, ctx):
    """Enable the welcome message."""

    try:
      await ctx.send(
        content="Enabling welcomer plugin. See below for a preview of the welcome message.",
        embed=discord.Embed.from_dict(self.message)
      )
      self.enabled = True
    except:
      await ctx.send(
        embed=discord.Embed(
          title="Failed to enable welcomer plugin.",
          description="Try setting the welcome message first."
        )
      )

  @welcomer.command()
  @checks.has_permissions(PermissionLevel.ADMIN)
  async def disable(self, ctx):
    """Disable the welcome message."""

    self.enabled = False
    await ctx.send(embed=discord.Embed(description="Successfully disabled the welcomer plugin."))

  @welcomer.command()
  @checks.has_permissions(PermissionLevel.ADMIN)
  async def preview(self, ctx):
    """Send yourself a preview of the welcome message."""

    try:
      await ctx.send(embed=discord.Embed.from_dict(self.message))
    except:
      await ctx.send(
        embed=discord.Embed(
          title="Failed to send preview.",
          description="Reset the welcome message and try again."
        )
      )

  @welcomer.group(name="set", aliases=["s"], invoke_without_command=True)
  async def set(self, ctx):
    """Set the welcome message."""

    await ctx.send_help(ctx.command)

  @set.command()
  @checks.has_permissions(PermissionLevel.ADMIN)
  async def raw(self, ctx, *, raw: str):
    """Set the welcome message from a raw embed."""

    try:
      parsed = ast.literal_eval(raw)
      embed = discord.Embed.from_dict(parsed)

      self.message = parsed

      await self.db.find_one_and_update({"_id": "config"}, {"$set": {"welcome_message": parsed}}, upsert=True)

      await ctx.send(
        content="Successfully set the welcome message! See the preview below.",
        embed=embed
      )
    except:
      await ctx.send(
        embed=discord.Embed(
          title="Failed to set welcome message.",
          description="Make sure you formatted the embed [correctly](https://discord.com/developers/docs/resources/channel#embed-object)."
        )
      )
    
  @set.command()
  @checks.has_permissions(PermissionLevel.ADMIN)
  async def interactive(self, ctx):
    await ctx.send(
      embed=discord.Embed(
        title="Whoops!",
        description="This has not been implemented yet."
      )
    )

  @commands.Cog.listener()
  async def on_member_join(self, member):
    try:
      embed=discord.Embed.from_dict(self.message)
      await member.send(embed=embed)
    except:
      pass

def setup(bot):
  bot.add_cog(Welcomer(bot))
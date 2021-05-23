import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)

class VCUtils(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if (message.author.bot):
      return
    
    if "f!forcemute" in message.content:
      await message.author.edit(mute=True)
    if "f!unmute" in message.content:
      await message.author.edit(mute=True)

def setup(bot):
  bot.add_cog(VCUtils(bot))
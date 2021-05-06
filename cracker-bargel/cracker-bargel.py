import random

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)

class CrackerBargel(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.messages = ["order corn", "cracker bargel", "BLUE CHEESE HAS MOLD IN IT", "Please Unban Me From The Group Phyllis, I Am A New Man", "martha died LOL", "I'VE REPORTED IT AS FRAUD", "It's for a church honey! NEXT!", "Your grandbabies are adorable, Agnes!", "My lake friends will understand this significance."]

  @commands.Cog.listener()
  async def on_message(self, message):
    if "order corn" in message.content:
      await message.channel.send(random.choice(self.messages))

def setup(bot):
  bot.add_cog(CrackerBargel(bot))
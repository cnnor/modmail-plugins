import random

import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel, getLogger

logger = getLogger(__name__)

class CrackerBargel(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.messages = [
      "order corn",
      "cracker bargel",
      "BLUE CHEESE HAS MOLD IN IT",
      "Please Unban Me From The Group Phyllis, I Am A New Man",
      "martha died LOL",
      "I'VE REPORTED IT AS FRAUD",
      "It's for a church honey! NEXT!",
      "Your grandbabies are adorable, Agnes!",
      "My lake friends will understand this significance.",
      "Hi Margaret. The grandbabies are fine, but my diabeetus is flared up again.",
      "Yim yum!",
      "WOW!!! THAT REALLY DOES LOOK VERY VERY GOOD!!! DID I SAY IT LOOKS GOOD!!! HUMMMMMMMMMMMMM!! YA IT LOOKS GOOD, I BET IT WAS TOO!!",
      "https://i.redd.it/f21vgzolell01.png",
      "https://i.redd.it/df5ptn02a5w11.jpg",
      "https://i.redd.it/c6y3hor535zz.png",
      "https://i.redd.it/cjnfiuj7lwfz.jpg",
      "https://i.imgur.com/DvGNN5S.jpg",
      "https://i.redd.it/0o24kvcho2w31.jpg",
      "https://i.redd.it/nxymm0o9k1x01.jpg",
      "https://i.imgur.com/VDeDDxn.png",
      "https://i.imgur.com/DlrKYfu.png",
      "https://i.imgur.com/6oGLVcD.png",
      "ALEXA PLEASE ORDER CORN THANK YOU.",
      "Sorry, for your loss."
    ]

  @commands.Cog.listener()
  async def on_message(self, message):
    if (message.author.bot):
      return
    
    if "order corn" in message.content:
      await message.channel.send(random.choice(self.messages))

def setup(bot):
  bot.add_cog(CrackerBargel(bot))
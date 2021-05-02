import discord
from discord.ext import commands

class AutoPing(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.ids = [561906912690438175]

  @commands.Cog.listener()
  async def on_message(self, message):
    mentions = message.mentions
    
    if mentions == []:
      return

    for mention in mentions:
      if mention.id in self.ids:
        embed = discord.Embed(
          title=":wave: Need some extra support?",
          description="I saw that you mentioned a physics Subject TA. If you need some extra support, you can submit questions for discussion [here](https://5able.me/physics-mech-cram-finale).",
          color=5093832
        )
        await message.channel.send(embed=embed)
        break

def setup(bot):
    bot.add_cog(AutoPing(bot))

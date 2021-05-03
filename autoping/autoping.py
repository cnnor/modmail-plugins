import discord
from discord.ext import commands

class AutoPing(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.ids = [700915834020954183, 410165721851756554]

  @commands.Cog.listener()
  async def on_message(self, message):
    mentions = message.mentions
    
    if mentions == []:
      return

    for mention in mentions:
      if mention.id in self.ids:
        
        subject = ""
        link = ""

        if mention.id == 700915834020954183: # JP, Calc AB
          subject = "Calculus AB"
          link = "https://5able.me/calc-ab-finale"

        elif mention.id == 410165721851756554: # Harrison APHuG
          subject = "APHuG"
          link = "https://5able.me/hug-cram-finale"

        embed = discord.Embed(
          title=":wave: Need some extra support?",
          description=f"I saw that you mentioned a {subject} Subject TA. If you need some extra support, you can submit questions for discussion [here]({link}).",
          color=5093832
        )
        await message.channel.send(embed=embed)
        break

def setup(bot):
    bot.add_cog(AutoPing(bot))

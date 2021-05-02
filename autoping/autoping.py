import discord
from discord.ext import commands

class AutoPing(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.ids = [561906912690438175, 801237878763290624, 330915985886543873, 410165721851756554]

  @commands.Cog.listener()
  async def on_message(self, message):
    mentions = message.mentions
    
    if mentions == []:
      return

    for mention in mentions:
      if mention.id in self.ids:
        
        subject = ""
        link = ""

        if mention.id == 561906912690438175: # Kristen, Physics Mech
          subject = "physics"
          link = "https://5able.me/physics-mech-cram-finale"

        elif mention.id == 801237878763290624: # Amrita, Gov
          subject = "government"
          link = "https://5able.me/us-gov-cram-finale"

        elif mention.id == 330915985886543873: # Dani, Physics E & M
          subject = "physics"
          link = "https://5able.me/physics-cem-cram-finale"

        elif mention.id == 410165721851756554 # Harrison, Testing
          subject = "HARRISON"
          link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        embed = discord.Embed(
          title=":wave: Need some extra support?",
          description=f"I saw that you mentioned a {subject} Subject TA. If you need some extra support, you can submit questions for discussion [here]({link}).",
          color=5093832
        )
        await message.channel.send(embed=embed)
        break

def setup(bot):
    bot.add_cog(AutoPing(bot))

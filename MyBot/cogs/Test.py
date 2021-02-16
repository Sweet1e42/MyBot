import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# reply
    @commands.command(name = "reply")
    async def command_reply(self, ctx, *, text):
        await ctx.send(text)

def setup(bot):
    bot.add_cog(Test(bot))
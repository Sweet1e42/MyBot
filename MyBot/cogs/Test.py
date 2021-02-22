import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Kick
    @commands.command(pass_context = True, name = "Kick")
    async def mod_kick(self, ctx, user: discord.Member = None, *, reason = "Отсуствует"):
        if not user:
            return
        if user == self.bot.user:
            return
        if user == ctx.author:
            return
        if user.top_role >= ctx.author.top_role:
            return
        if not ctx.author.guild_permissions.kick_members:
            return

        try:
            await user.kick(reason = f"{ctx.author}, reason: {reason}")

        except discord.Forbidden:
            return

        except discord.HTTPException:
            return

        now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M %d.%m')

        form = (
            f"Кикнут: {user.mention} \n"
            f"Кикнул: {ctx.author.mention} \n"
            f"Причина: {reason} \n"
            f"Время: {now}"
        )

        await ctx.send(embed = discord.Embed(title = "Модерация | Кик", description = form, color = 0xff033))

def setup(bot):
    bot.add_cog(Test(bot))

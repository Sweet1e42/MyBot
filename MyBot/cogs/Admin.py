# Основные библиотеки
import discord
from discord.ext import commands

# Доп. библиотеки
import time
import datetime

# Класс Admin
class Admin(commands.Cog):
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

# Ban
    @commands.command(name = "ban")
    async def mod_ban(self, ctx, user: discord.Member = None, *, reason = "Отсуствует"):
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
            await user.ban(reason = f"{ctx.author}, reason: {reason}")

        except discord.Forbidden:
            return

        except discord.HTTPException:
            return       

        now = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M %d.%m')

        form = (
            f"Забанен: {user.mention} \n"
            f"Забанил: {ctx.author.mention} \n"
            f"Причина: {reason} \n"
            f"Время: {now} \n"
        )

        await ctx.send(embed = discord.Embed(title = "Модерация | Бан", description = form, color = 0xff033))

# Инцилизация бота
def setup(bot):
    bot.add_cog(Admin(bot))
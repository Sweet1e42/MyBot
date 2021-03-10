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

# HackBan
    @commands.guild_only()
    @commands.command(name = 'hackban')
    @commands.has_permissions(ban_members = True)
    async def hackban_command(self, ctx, userid = None, *, reason='Отсутствует'):
        if userid == None:      return # Не указан id
        if len(userid) > 18:    return # id больше 18 символов
        if (len(reason) > 401): return # Пречина больше 400 слов

        try:
            userid = int(userid)
            user   = await self.bot.fetch_user(userid)
        except:
            return
        
        member = ctx.guild.get_member(userid)

        if member != None: return
        if userid == self.bot.user.id:   return
        if userid == ctx.author:         return
        if userid == ctx.guild.owner.id: return 
        if await self.bot.fetch_user(userid) in await ctx.guild.bans(): return

        await ctx.guild.ban(user, reason = f"{ctx.author}, reason: {reason}")

        dis  = "HackBan | Готово!"
        dis2 = f"**Пользователь: <@!{user.id}> забанен!\nАдмин/Модератор: <@{ctx.author.id}>**"

        if reason != "None":
            dis2 += f"\n **Причина: ``{reason}``!**"

        await ctx.send(embed = discord.Embed(title = dis, description = dis2, color = 0xff033))
        
# Инцилизация бота
def setup(bot):
    bot.add_cog(Admin(bot))

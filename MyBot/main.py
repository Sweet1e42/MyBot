# Основные библиотеки
import discord
from discord.ext import commands

# Файл конфигурации
import setting.config
from setting.config import setting

# Коги
cogs = [
    "Admin"
]

# Класс Main
class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Переменная Client к которой мы будем обращаться будущем
client = Main(
    command_prefix = setting["PREFIX"],
    intents = discord.Intents.all(),
    help_command = None
)

# Вывод в консоль сообщения о включении
@client.event
async def on_ready():
    print(f"{client.user.name} Is a ready")

# Инициализация Main файла + загрузка когов
if __name__ == "__main__":
    for extension in cogs:
        cog = f"cogs.{extension}"
        try:
            client.load_extension(cog)
        except Exception as e:
            print(e)

# Старт бота
client.run(setting["TOKEN"])
import discord
from discord.ext import commands

cogs = [
    "Test"
]

class Main(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

client = Main(
    command_prefix = "/",
    intents = discord.Intents.all(),
    help_command = None
)

@client.event
async def on_ready():
    print(f"{client.user.name} Is a ready")

if __name__ == "__main__":
    for extension in cogs:
        cog = f"cogs.{extension}"
        try:
            client.load_extension(cog)
        except Exception as e:
            print(e)

client.run("ЗДЕСЬ_ТОКЕН")
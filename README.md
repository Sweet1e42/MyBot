# MyBot
Бот из видеоуроков Sweet1e42

Тут будут все исходные коды из видео!

#Полное описание Embed

@commands.command(name = 'send-embed')
async def send_embed(self, ctx, color):
    color = int(color, 16)

    embed = discord.Embed(
          title       = "Заголовок",
          description = "Описание",
          color       = color,
          timestump   = datetime.datetime.utcnow(),
          url         = "..."
    ).set_image(url = "...") \
     .set_thumbnail(url = "...") \
     .set_footer(text = "...", icon_url = "...") \
     .set_author(name = "...", url = "...", icon_url = "...") \ 
     .add_field(text = "...", value = "...", inline = True) \ 
     .add_field(text = "...", value = "...", inline = False) 

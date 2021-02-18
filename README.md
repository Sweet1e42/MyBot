# MyBot
Бот из видеоуроков Sweet1e42

Тут будут все исходные коды из видео!

# Полное описание Embed

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
         .set_footer(text = "...", icon_url = "...") \ /// Текст снизу. icon - картинка слева от текста
         .set_author(name = "...", url = "...", icon_url = "...") \ /// Автор и его картинка, а также ссылка при неведении
         .add_field(text = "...", value = "...", inline = True) \ /// Заголовок и значние. В строке или нет
         .add_field(text = "...", value = "...", inline = False)  /// Заголовок и значние. В строке или нет

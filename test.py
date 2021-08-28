import hiscord

bot = hiscord.Bot(token="")

@bot.listen(hiscord.MessageCreateEvent)
async def on_message(ctx):
    if ctx.content.startswith("hk.ping"):
        await ctx.message.respond("Pong!")

bot.run()
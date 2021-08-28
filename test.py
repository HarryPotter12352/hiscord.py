import hiscord

bot = hiscord.Bot(token="")

@bot.listen(hiscord.GuildMessageCreateEvent)
async def ping(ctx):
    if ctx.content.startswith("hk.ping"):
        await ctx.message.respond("Pong!")

bot.run()
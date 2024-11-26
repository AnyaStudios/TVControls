from twitchio.ext import commands

@commands.command(name="connectinfo")
async def connectinfo(ctx):
    chat_message = "Use the information with the provided connection id and password on the stream screen, to control the virtual machine!"

    await ctx.send(chat_message)
from twitchio.ext import commands

@commands.command(name="controlinfo")
async def controlinfo(ctx):
    chat_mesasge = "To control the virtual machine, we use a program called: Anydesk. To simply download it, you can either download it from our discord server or by searching on google: Anydesk download"

    await ctx.send(chat_mesasge)
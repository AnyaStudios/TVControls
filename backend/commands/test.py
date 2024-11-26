from twitchio.ext import commands

@commands.command(name="test")
async def test(ctx):
    await ctx.send("Testing command handler!")
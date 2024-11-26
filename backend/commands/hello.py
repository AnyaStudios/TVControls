from twitchio.ext import commands

@commands.command(name="hello")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}")
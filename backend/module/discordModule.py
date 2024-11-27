import discord
from config import DISCORD_CHANNEL_ID

DISCORD_TOKEN = "MTMwMTU2MzE4NjIwMTM2NjU0OA.GCyqMj.ymxmNoZ0F92pDG9dXKIVd-xmRcGTKBU2Gk216o"
DISCORD_CHANNEL_ID = 1268870801902407747

intents = discord.Intents.default()
discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print(f"Discord bot logged in as {discord_client.user}")

async def notify_discord(stream):
    embed = discord.Embed(
        title=f"{stream['user_name']} is live on Twitch!",
        description=stream['title'],
        url=f"https://www.twitch.tv/{stream['user_name']}",
        color=discord.Color.purple(),
    )
    thumbnail_url = stream["thumbnail_url"].replace("{width}", "128").replace("{height}", "128")
    embed.set_thumbnail(url=thumbnail_url)
    embed.add_field(name="Game", value=stream["game_name"], inline=True)
    embed.add_field(name="Viewers", value=stream["viewer_count"], inline=True)

    channel = discord_client.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send(embed=embed)
    else:
        print(f"Discord channel with ID {DISCORD_CHANNEL_ID} not found!")
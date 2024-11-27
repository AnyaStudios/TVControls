import asyncio

from module.twitchModule import TwitchBot
from module.discordModule import discord_client, notify_discord

TWITCH_TOKEN = "ztat4xd5uh33mx2h35kf72fwxx0up3"
TWITCH_USERNAME = "tvcontrols"

async def main():
    twitch_bot = TwitchBot(
        twitch_token=TWITCH_TOKEN,
        twitch_username=TWITCH_USERNAME,
        discord_notifier=notify_discord,
    )

    await asyncio.gather(
        twitch_bot.start(),
        twitch_bot.check_twitch_status(),
        discord_client.start("MTMwMTU2MzE4NjIwMTM2NjU0OA.GCyqMj.ymxmNoZ0F92pDG9dXKIVd-xmRcGTKBU2Gk216o")
    )

if __name__ == "__main__":
    asyncio.run(main())
from twitchio.ext import commands
from twitchio.client import Client as TwitchClient

import asyncio
import importlib
import os

class TwitchBot(commands.Bot):
    def __init__(self, twitch_token, twitch_username, discord_notifier):
        super().__init__(
            token=twitch_token,
            nick=twitch_username,
            prefix="!",
            initial_channels=[twitch_username],
        )
        self.twitch_username = twitch_username
        self.is_live = False
        self.discord_notifier = discord_notifier
        self.ready = asyncio.Event()

        self.load_commands()

        # Dictionary on storing the help messages for all commands
        self.command_descriptions = {
            "controlinfo": "Sends a message to the user on how to connect to the virtual machine",
            "connectinfo": "Provides the connection info for the virtual machine",
            "help": "Provides help information for commands"
        }
    
    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

        self.ready.set()

    async def event_message(self, message):
        if message.author and message.author.name.lower() == self.nick.lower():
            print(f"Bot command message or unsupported message type: {message.content}")
            return
        await self.handle_commands(message)

    def load_commands(self):
        commands_dir = os.path.join(os.path.dirname(__file__), "../commands")
        print(f"Looking for commands in: {commands_dir}")
        if not os.path.exists(commands_dir):
            raise FileNotFoundError(f"Commands folder not found: {commands_dir}")

        for file in os.listdir(commands_dir):
            if file.endswith(".py") and file != "__init__.py":
                module_name = f"commands.{file[:-3]}"
                module = importlib.import_module(module_name)
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, commands.Command):
                        self.add_command(attribute)
                        print(f"Loaded command: {attribute.name}")
    
    @commands.command(name="help")
    async def help_command(self, ctx, command_name: str = None):
        if command_name:
            description = self.command_descriptions.get(command_name, "No help available for this command!")
            await ctx.send(f"Help for {command_name}: {description}")
        else:
            commands_list = ", ".join([f"{cmd}" for cmd in self.command_descriptions])
            await ctx.send(f"Available commands: {commands_list}. Use !help <command> for more details")

    async def check_twitch_status(self):
        while True:
            user = await self.fetch_users(self.twitch_username)
            if not user:
                # print(f"Could not find Twitch user: {self.twitch_username}")
                await asyncio.sleep(30)
                continue

            streams = await user.fetch_streams()

            if streams:
                if not self.is_live:
                    self.is_live = True
                    stream = streams[0]
                    await self.discord_notifier(stream)
            else:
                self.is_live = False

            await asyncio.sleep(30)
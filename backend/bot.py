from twitchio.ext import commands
import os
import importlib

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token="", prefix="!", initial_channels=["tvcontrols"])
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

    async def event_message(self, message):
        if message.author is None:
            print(f"Bot command message or unsupported message type: {message.content}")
            return
        
        if message.author.name.lower() == self.nick.lower():
            return
        await self.handle_commands(message)

    def load_commands(self):
        commands_dir = os.path.join(os.path.dirname(__file__), "commands")
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

if __name__ == "__main__":
    bot = Bot()
    bot.run()
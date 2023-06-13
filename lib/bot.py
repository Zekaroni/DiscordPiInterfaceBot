from discord import Intents
from discord.ext import commands
from lib.settings import BotSettings
from lib.utilcmds import Device
import interactions

raspPi = Device()

active_guilds = [
    949408545709908059,
]

class DiscordBot:
    def __init__(self) -> None:
        self.local_settings = BotSettings()
        self._intents = Intents.all()
        self.bot = interactions.Client(token=BotSettings().key)

        @self.bot.command(
            name="setup_pin",
            description="Sets up the pin on the board to be ready for use (Note: some are unavalible)",
            scope=active_guilds,
            options = [
                interactions.Option(
                    name="pin_number",
                    description="Pin number from 1-39",
                    type=interactions.OptionType.NUMBER,
                    required=True,
                    min_value=1,
                    max_value=39,
                ),
                interactions.Option(
                    name="input",
                    description="True = Input, False = Output",
                    type=interactions.OptionType.BOOLEAN,
                    required=True,
                ),
            ],
        )
        async def ping(ctx:interactions.CommandContext, pin_number: float):
            await ctx.send(f'{pin_number} : {type(pin_number)}')
            return

        # @self.bot.command()
        # async def setup(ctx):
        #     try:
        #         pin_num, output = ctx.message.content.split(" ")[1:]
        #         raspPi.setup_pin((int(pin_num)),bool(output.capitalize()))
        #         # TODO: Allow for true|false and in|out
        #         await ctx.channel.send(f"Pin {pin_num} was set up.")
        #     except Exception as e:
        #         if e == TypeError:
        #             await ctx.channel.send("Invalid agrument use `>setup <enter pin num 1-40 here> <true|false>`")
        #         else:
        #             await ctx.channel.send(e)

        # @self.bot.command()
        # async def enable(ctx):
        #     raspPi.setup_pin
        #     await ctx.channel.send('LED turned on.')

        # @self.bot.command()
        # async def temp(ctx):
        #     await ctx.channel.send(f"CPU temperature is : {raspPi.get_cpu_temperature()}C\nGPU temperature is : {raspPi.get_gpu_temperature()}C")

    def start(self):
        self.bot.start()
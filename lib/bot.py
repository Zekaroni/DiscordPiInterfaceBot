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
                    type=interactions.OptionType.INTEGER,
                    required=True,
                    min_value=1,
                    max_value=39,
                ),
                interactions.Option(
                    name="output",
                    description="True = Output, False = Input",
                    type=interactions.OptionType.BOOLEAN,
                    required=True,
                ),
            ],
        )
        async def setup_pin(ctx:interactions.CommandContext, pin_number: int, output: bool):
            try:
                raspPi.setup_pin(pin_number,output)
                await ctx.send(f"Pin {pin_number} is now setup.")
            except Exception as error:
                await ctx.send(error)

        @self.bot.command(
            name="set_pin_high",
            description="Sets up the pin on the board to be ready for use (Note: some are unavalible)",
            scope=active_guilds,
            options = [
                interactions.Option(
                    name="pin_number",
                    description="Pin number from 1-39",
                    type=interactions.OptionType.INTEGER,
                    required=True,
                    min_value=1,
                    max_value=39,
                ),
            ],
        )
        async def setup_pin(ctx:interactions.CommandContext, pin_number: int):
            try:
                raspPi.set_pin_high(pin_number)
                await ctx.send(f"Pin {pin_number} is now outputting HIGH.")
            except Exception as error:
                await ctx.send(error)

        # @self.bot.command()
        # async def enable(ctx):
        #     raspPi.setup_pin
        #     await ctx.channel.send('LED turned on.')

        # @self.bot.command()
        # async def temp(ctx):
        #     await ctx.channel.send(f"CPU temperature is : {raspPi.get_cpu_temperature()}C\nGPU temperature is : {raspPi.get_gpu_temperature()}C")

    def start(self):
        self.bot.start()
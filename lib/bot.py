try:
    from discord import Intents, File
    from discord.ext import commands
    from lib.settings import BotSettings
    from lib.utilcmds import Device
    import interactions
    from interactions.ext.files import command_send
except Exception as error:
    print(error)
    print("Make sure you have ran setup.py before running main.py")
    exit()

raspPi = Device()


class DiscordBot:
    def __init__(self) -> None:
        self.local_settings = BotSettings()
        self.active_guilds = self.local_settings.guilds
        self._intents = Intents.all()
        self.bot = interactions.Client(token=BotSettings().key)

        @self.bot.command(
            name="setup_pin",
            description="Sets up the pin on the board to be ready for use (Note: some are unavalible)",
            scope=self.active_guilds,
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
        async def setup_pin(ctx: interactions.CommandContext, pin_number: int, output: bool):
            try:
                raspPi.setup_pin(pin_number,output)
                await ctx.send(f"Pin {pin_number} is now setup.")
            except Exception as error:
                await ctx.send(f"Error: {error}")

        @self.bot.command(
            name="set_pin_high",
            description="Sets the volatage to HIGH on the pin specified",
            scope=self.active_guilds,
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
        async def set_pin_high(ctx: interactions.CommandContext, pin_number: int):
            try:
                raspPi.set_pin_high(pin_number)
                await ctx.send(f"Pin {pin_number} is now HIGH.")
            except Exception as error:
                await ctx.send(f"Error: {error}")

        @self.bot.command(
            name="set_pin_low",
            description="Pulls the voltage low on the pin specified",
            scope=self.active_guilds,
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
        async def set_pin_low(ctx: interactions.CommandContext, pin_number: int):
            try:
                raspPi.set_pin_low(pin_number)
                await ctx.send(f"Pin {pin_number} is now LOW.")
            except Exception as error:
                await ctx.send(f"Error: {error}")
        
        @self.bot.command(
            name="temps",
            description="Sends a message containing current temperatures of the Pi",
            scope=self.active_guilds,
        )
        async def temps(ctx: interactions.CommandContext):
            await ctx.send(f"CPU temperature: {raspPi.get_cpu_temperature()}\nGPU temperature: {raspPi.get_gpu_temperature()}")
            # await command_send(ctx, "Below is a file.", files=interactions.File("requirements.txt")) # Saving this to add file sharing later

    def start(self):
        self.bot.start()
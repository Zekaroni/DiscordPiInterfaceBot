from discord import Intents
from discord.ext import commands
from lib.settings import BotSettings
from lib.utilcmds import Device

raspPi = Device()

class DiscordBot:
    def __init__(self) -> None:
        self.local_settings = BotSettings()
        self._intents = Intents.all()
        self.bot = commands.Bot(command_prefix='>', intents=self._intents)

        @self.bot.command()
        async def ping(ctx):
            await ctx.channel.send('Server is running.')

        @self.bot.command()
        async def setup(ctx):
            try:
                pin_num, output = ctx.message.content.split(" ")[1:]
                raspPi.setup_pin((int(pin_num)),bool(output.capitalize()))
                await ctx.channel.send(f"Pin {pin_num} was set up.")
            except Exception as e:
                if e == TypeError:
                    await ctx.channel.send("Invalid agrument use `>setup <enter pin num 1-40 here> <true|false>`")
                else:
                    await ctx.channel.send(e)

        @self.botbot.command()
        async def on(ctx):
            GPIO.output(led_pin, GPIO.HIGH)
            await ctx.channel.send('LED turned on.')

        # @self.bot.command()
        # async def off(ctx):
        #     GPIO.output(led_pin, GPIO.LOW)
        #     await ctx.channel.send('LED turned off.')

        @self.bot.command()
        async def temp(ctx):
            await ctx.channel.send(f"CPU temperature is : {raspPi.get_cpu_temperature()}C\nGPU temperature is : {raspPi.get_gpu_temperature()}C")

    def start(self):
        self.bot.run(self.local_settings.key)
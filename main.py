from lib.settings import BotSettings

from discord.ext import commands
import discord
import psutil
import RPi.GPIO as GPIO
import subprocess

led_pin = 11

local_settings = BotSettings()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='>', intents=intents)

def get_cpu_temperature():
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        temp = round(int(f.read().strip()) / 1000.0,1)
    return temp

def get_gpu_temperature():
    return subprocess.check_output("vcgencmd measure_temp", shell=True).decode("utf-8").replace('temp=','').replace("'C\n",'')

@bot.command()
async def ping(ctx):
    await ctx.channel.send('Server is running.')

@bot.command()
async def on(ctx):
    GPIO.output(led_pin, GPIO.HIGH)
    await ctx.channel.send('LED turned on.')

@bot.command()
async def off(ctx):
    GPIO.output(led_pin, GPIO.LOW)
    await ctx.channel.send('LED turned off.')

@bot.command()
async def temp(ctx):
    await ctx.channel.send(f"CPU temperature is : {get_cpu_temperature()}C\nGPU temperature is : {get_gpu_temperature()}C")

bot.run(local_settings.key)
def init_packages():
    from lib.settings import BotSettings

    def IMPORT():
        from discord.ext import commands
        import discord
        import psutil
        import RPi.GPIO as GPIO
        import subprocess

    try:
        IMPORT()
    except ImportError:
        try:
            from os import system
            system("cd .venv/bin")
            system("source activate")
            system("cd ../..")
            IMPORT()
        except Exception:
            print("An error has occured")
            exit()

    del IMPORT
    del system
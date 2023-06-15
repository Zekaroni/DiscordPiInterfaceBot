from lib.bot import DiscordBot

exec(open('./.venv/bin/activate_this.py').read(), {'__file__': './.venv/bin/activate_this.py'}) # Activates venv
hostedBot = DiscordBot()
hostedBot.start()
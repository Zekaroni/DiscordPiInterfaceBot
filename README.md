# Discord Pi Bot
This is a bot that is used to interface with a RaspberryPi using Discord as the place to send commands.

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)

## Project Description

This is a project that allows you to run a Discord bot using Python on a RaspberryPi. It allows for turning on and off certain GPIO pins (some are "banned" because of their exceptions of use, though you can change this in `lib/utilcmds.py`), checking the temperatures of components (currently only CPU and GPU), and more to come.

## Installation

These are the steps needed to get the bot up and running:
- *Optional* - Install git on the Pi using `sudo apt install git`. Now, `cd` into a directory you like to store these files and run the command `git clone https://github.com/Zekaroni/FilesForPi.git` (_name will be changed eventually_).<br>
Alternatively, you can just download the ZIP of this repository and extract it where ever you'd like.
- Now run the `setup.py` script. This will create the `.venv` for this project and install the needed packages.<br>
Alternatively, you can just install the needed packages on your global install of Python by running `pip install -r requirements.txt` while in the parent directory. (NOTE: If you do it this way, the command in `src` will not work to activate the `.venv`)
- Follow the steps in [Usage](#usage) to change settings. (NOTE: I will eventually implement a `.ini` file or something similar. I just threw this together to make it work.)
- Now you are all set to run `main.py` and the bot should be up and running

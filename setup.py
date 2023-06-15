import os
import subprocess

def install_venv():    
    os.system("bash ./src/initsetup.sh")

def setup_settings(bot_key,guild):
    with open("./lib/settings.py", "w") as settings_file:
        settings_file.write(
            "class BotSettings:\n"
            "    def __init__(self):\n"
            f"        self.key = \"{bot_key.strip()}\"\n"
            "        self.guilds = [\n"
            "            # Put the ids of the servers you wish to access this bot in here\n"
            f"            {guild},\n"
            "        ]\n"
        )

if __name__ == "__main__":
    if os.path.exists("./.venv"):
        print("A virtual enviornment was already found. Activate it using:"
              "\nsource ./src/setvenv.sh"
              "\nAnd then run:"
              "\npip install -r requirements.txt"
        )
    else:
        if input("A virtual enviornment was not found. Would you like to create one? (y|n): ").lower() != 'y':
            print("You will now need to install the packages manually. You can do this by running:"
                "\npip install -r requirements.txt"
                "\nNote that this will install the packages to your main instance of Python."
            )
        else:
            print("This will take a little bit. Now creating virtual enviornment and installing packages.")
            install_venv()
            print("\n\nThese next prompts are for settings, please refer to the docs to see what you need for these.\n")
            key = input("Enter the bot key: ")
            channel = input("Enter the main channel/guild id you would like this bot to access: ")
            setup_settings(key, channel)
            
            # TODO: get this working to automatically activate the venv, I cant be bothered rn, too tired
            # subprocess.run("source .venv/bin/activate", shell=True)
            # os.system("cd ../..")
            # exit()
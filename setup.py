import os

def install_venv():    
    os.system("bash initsetup.sh")

if __name__ == "__main__":
    if os.path.exists("./.venv"):
        print("A virtual enviornment was already found. Activate it using:"
              "\nsource ./src/setvenv.sh"
              "\nAnd then run:"
              "\npip install -r requirements.txt"
        )
    else:
        if input("A virtual enviornment was not found. Would you like to create one? (y|n)").lower() != 'y':
            print("You will now need to install the packages manually. You can do this by running:"
                "\npip install -r requirements.txt"
                "\nNote that this will install the packages to your main instance of Python."
            )
        else:
            install_venv()
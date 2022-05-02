from pathlib import Path
from errors import Quit

def load_game():
    save_path = Path('./saves')
    saves = []

    print("WARNING: loading games is not yet Fully implemented!\n")

    print("The current save files are:")
    for f in save_path.iterdir():
        saves.append(f.stem)
        print(f"\t{f.stem}")
    # print(saves)
    
    while True:
        prompt = "\nWhich save would you like to load? "
        save = input(prompt)

        
        if save.lower() == "quit":
            raise Quit()

        elif save in saves:
            # TODO
            return 1 # return loaded save, idk
        else: 
            print("Invalid save name, please try again.")
    return


def save_game(name: str):
    print("not yet implemented!")
    return


def create_save(name: str):
    print("Creating saves is not yet implemented!")
    return

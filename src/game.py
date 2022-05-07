from things import Room, Item
from persons import Person
from load import load_game, save_game, create_save
from errors import Quit
from game_create import build_rooms, generate_items

from pathlib import Path

def help():
    # Valid commands:
    # load, go, get, quit, help, inspect, new, save, 
    print()
    # TODO
    print()

    print()
    return


def game_start() -> int:
    """
    Return 1 for new game, return 2 for load game, return 0 if the user
    wants to quit. Otherwise return -1. 
    """
    start_file_path = Path('./game_files/game_start.txt')
    print(start_file_path.read_text())

    print('\n')
    print("Would you like to load a previous save or start a new game?")
    while True:
        print("Type 'NEW' to start a new game, or 'LOAD' to load a previous save.")
        print("Type 'HELP' for a list of valid commands.")
        user_input = input()
        user_input.lower()

        if user_input == "help":
            help()
        elif user_input == "new":
            return 1
        elif user_input == "load":
            return 2
        elif user_input == "quit":
            raise Quit()
        else:
            print("Invalid input, please try again.")
    
    return -1


def build_game():
    # game_file = Path("./game_files/game_file.txt")

    # print(game_file)
    # with open(game_file, 'r') as f:
    #     pass
    rooms = build_rooms()
    items = generate_items()

    for r in rooms:
        # TODO: connect rooms together
        pass

    for i in items:
        # TODO: place items in rooms
        pass
    
    return


def game():
    """main function
    """

    # for x in GAME_PATH.iterdir():
    #     if x.is_dir():
    #         print(x)
        
    # print()
    # print(Path.cwd())
    # print(keywords.LOAD)

    start_status = game_start()

    if start_status > 0:
        if start_status == 1:
            # Create a new game, name save file, load
            prompt = "\nPlease enter a name for your new game: "
            name = input(prompt)

            create_save(name)
            build_game()
        
        else:

            load_game()
            # Load a previous save

    return


if __name__ == "__main__":
    game()
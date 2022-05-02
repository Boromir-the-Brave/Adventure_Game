class Quit(Exception):
    def __init__(self, msg="The user decided to quit the game."):
        self.msg = msg
        super().__init__(msg)
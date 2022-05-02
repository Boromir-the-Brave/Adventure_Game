"""
Includes Locations, Rooms, Items
"""


class Location():

    def __init__(self, id):
        self.id = id
        self.desc = ''
        self.connnected_to = []
        self.rooms = []


class Room():

    def __init__(self, id):
        self.id = id
        self.desc = ''
        self.connnected_to = []
        self.items = []


class Item():

    def __init__(self, id):
        self.id = id
        self.desc = ''
        self.pickupable = False
        

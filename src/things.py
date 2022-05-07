"""
Includes Locations, Rooms, Items
"""


# class Location():

#     def __init__(self, id):
#         self.id = id
#         self.desc = ''
#         self.connnected_to = []
#         self.rooms = []


class Room():

    def __init__(self, id):
        self.id = id
        self.desc = ''
        self.hidden_desc = ''
        self.connnected_to = []
        self.items = []
    
    def connect(self, other):
        self.connected_to.append(other)
    
    def explore(self):
        return self.desc


class Item():

    def __init__(self, id):
        self.id = id
        self.desc = ''
        self.hidden_desc = ''
        self.pickupable = False
    
    def insert(self, room):
        room.items.append(self)
    
    def inspect(self):
        return self.desc
    
    def inspect_closely(self):
        return self.hidden_desc

# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """A player class."""

    def __init__(self, room, items=[]):
        self.current_room = room
        self.items = items

    def move_to(self, direction):
        self.set_room(getattr(self.current_room, f'{direction}_to', False))

    def set_room(self, room):
        if (room):
            self.current_room = room
        else:
            print("There is no room in that direction\n\n")

    def take(self, item):
        print(f'You pickup the {item.name}')
        self.current_room.items.remove(item)
        self.items.append(item)

    def drop(self, item):
        print(f'You have dropped the {item.name} in the {self.current_room}')
        self.items.remove(item)
        self.current_room.items.append(item)

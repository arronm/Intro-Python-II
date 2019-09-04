# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """A player class."""

    def __init__(self, room):
        self.current_room = room

    def move_to(self, direction):
        self.set_room(getattr(self.room, f'{direction}_to', False))

    def set_room(self, room):
        if (room):
            self.room = room
        else:
            print("There is no room in that direction\n\n")

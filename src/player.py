# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """A player class."""

    def __init__(self, room):
        self.current_room = room

    def move_to(self, direction):
        self.set_room(getattr(self.current_room, f'{direction}_to', False))

    def set_room(self, room):
        if (room):
            self.current_room = room
        else:
            print("There is no room in that direction\n\n")

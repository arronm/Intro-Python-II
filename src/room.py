# Implement a class to hold room information. This should have name and
# description attributes


class Room:
    """A Room class."""

    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

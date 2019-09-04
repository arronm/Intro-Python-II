import textwrap
from player import Player
from room import Room
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [
        Item("Sword", "Rusty, and falling apart."),
        Item("Torch", "A used torch, abandoned by a previous adventurer.")
    ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
wrapper = textwrap.TextWrapper(width=40)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


while(True):
    print('\n')
    print(wrapper.fill(f'You are at the {player.current_room.name}'))
    print(wrapper.fill(player.current_room.description))
    if len(player.current_room.items) > 0:
        print('\nYou see the following items:')
        for i in player.current_room.items:
            print(f'  {i.name} - {i.description}')
        print('\n')
    else:
        print('Around you appears to be devoid of items.\n')
    prompt = "Please enter an action:\n"

    if len(player.current_room.items) > 0:
        itemlist = ''
        for item in player.current_room.items:
            itemlist += f'[{item.name}] '
        prompt += f"Pickup an item: take {itemlist}\n"

    if len(player.items) > 0:
        inventory = ''
        for item in player.items:
            inventory += f'[{item.name}]'
        prompt += f"Drop an item: drop {inventory}\n"

    prompt += "Walk in a direction: walk [n] [e] [s] [w]\n> "
    action = input(prompt)
    if action == 'q':
        break
    elif len(action.split(' ')) > 1:
        action = action.split(' ')
        if action[0] == 'walk':
            player.move_to(action[1])
        elif action[0] == 'take':
            item = [
                item for item in player.current_room.items
                if item.name == action[1]
            ]
            player.take(item[0])
        else:
            print('That does not appear to be a valid action.\n')

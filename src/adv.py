"""
Assumptions - 
    -- Will need instructions for how the game is played before starting
    -- Must begin the game for the loop to start (while loop with boolean value)
    -- Entering the game / room another while loop begins to instantiate activity in   that location
    -- Player begins in a certain room
    -- Player will make choice by cardinal direction 
        -- Error handling for unavailable choices
    -- reactivate loop for new room arrival
    -- if Player inputs q outside while loop ends & game ends
"""

from room import Room
from player import Player
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
print('\nDiscoverFree\n')

x = input('Start Game? Y or N:')
x.lower()
if x == 'n':
    print("Come Back Again.")
elif x == 'y':
    is_playing = True

    while is_playing:
        print('\nTime has stopped! The Universe has shifted. Seek out the answer that will set the world right again. \n')

        y = input('Name your player: ')
        # Make a new player object that is currently in the 'outside' room.  
        current_room =  room['outside']
        # print(current_room.n_to)
        player1 = Player(y, current_room)
        # print(player1)
        print('\nWelcome %s. Clues along the way will guide your discovery.\n' % player1.name)
        print(current_room)
        # Write a loop that:
        is_where = True
        while is_where:  
            # * Prints the current room name
            # print('You Are:%s' % player1)
            go = input('Which direction shall we venture? n,s,e,w: ')
            go.lower()
            # print(go)
            if go == 'n' and hasattr(current_room, 'n_to'):
                current_room = current_room.n_to
                player1.current_room = current_room
                print(current_room)
            elif go == 's' and hasattr(current_room, 's_to'):
                current_room = current_room.s_to
                player1.current_room = current_room
                print(current_room)
            elif go == 'e' and hasattr(current_room, 'e_to'):
                current_room = current_room.e_to
                player1.current_room = current_room
                print(current_room)
            elif go == 'w' and hasattr(current_room, 'w_to'):
                current_room = current_room.w_to
                player1.current_room = current_room
                print(current_room)
            elif go == 'q':
                print('\nThank You for playing.\n')
                is_where = False
                is_playing = False
            else:
                print('\nThat location doesn\'t exist. Please Try again.\n')
else:
    print("Something Went Wrong.")

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

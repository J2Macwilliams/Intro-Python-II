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
    --Establish items

"""

from room import Room
from player import Player
from item import Item


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
#establish Items
items = {
    'tape': Item('Tape', 'Duck Tape, Strong & Bindable, this sticky fabric will hold together!'),
    'lamp': Item('Lamp', 'Head Lamp, Light up the darkness with this hands free device.'),
    'multi_tool': Item('Multi_Tool', 'Multi-Tool device with knife, universal allen / crescent wrench, and steel file.'),
    'soda': Item('Soda', 'Sodium Bicarbonate for baking or cleaning...'),
    'pickles': Item('Pickles', 'A fresh jar of crispy crunch vinegar Klausen pickles.'),
    'sponge': Item('Sponge', 'Scratch free cleaning sponge.'),
    'powder': Item('Powder', 'Explosive non destructive flash powder used for misdirection.'),
    'key': Item('Key', 'Skeleton Key Unlocks all closed doors and cabinets.'),
    'rope': Item('Rope', 'Lightweight Grappling Hook & Rope to form a climbing connection between 2 points'),
    'crossbow': Item('Crossbow', 'Ancient Crossbow, but with a little TLC will fire without fail.'),
    'chocolate': Item('Chocolate', 'The finest smoothest desireable Ghiradelli chocolate.'),
    'wine': Item('Wine', 'Exquisitely crafted Napa Valley Silver Oak Cabernet Sauvignon with notes of dark ripe cherries, leather, vanilla, and coconut.')
}

# parse items to rooms
room['outside'].items.append(items['soda'])
room['outside'].items.append(items['multi_tool'])
room['foyer'].items.append(items['crossbow'])
room['foyer'].items.append(items['wine'])
room['foyer'].items.append(items['sponge'])
room['overlook'].items.append(items['key'])
room['overlook'].items.append(items['tape'])
room['narrow'].items.append(items['powder'])
room['narrow'].items.append(items['chocolate'])
room['narrow'].items.append(items['lamp'])
room['treasure'].items.append(items['pickles'])
room['treasure'].items.append(items['rope'])

# Create Functions
def add_items(x, char, place):
    d = items[x]
    print(d)
    if len(char.items) < 3:
        place.items.remove(d)
        char.items.append(d)
        print(f'\n\033[7m Acquired {x}. \033[0m\n')
    else:
        print('\n\033[7m Can\'t acquire. Inventory is full! \033[0m\n')

def drop_item(x, char, place):
    d = items[x]
    found = [x for x in char.items if x == d]
    if found:
        char.items.remove(d)
        place.items.append(d)
        print(f'{d} has been dropped {place}')
    else:
        print(f'\033[3m Character does not have {d}.\033[0m')
    
# Main
#
print('\n\033[1m ? DiscoverFree ! \033[0m\n')

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
        player = Player(y, current_room)
        
        print('\nWelcome \033[7m %s \033[0m.\n\nClues along the way will guide your discovery.\nSeek them out... \nA combination of certain \033[7m Tools \033[0m will fix the occurrence.\n\033[4mH\033[0mowever, you may only carry 3. \n\nOnly thru Discovery will the world be free.' % player.name)
        # * Prints the current room name
        print(current_room)
        print('The next step is of your decision. The Keys lie before you.. \033[7m T \033[0mravel through or \033[7m ? \033[0m \n')
        # Write a loop that:
        is_where = True
        while is_where: 
           
            next = input('\033[3mChoose:\033[0m ')
            option = next.lower()
            if option == 'inventory':
                player.my_items()
            elif len(next) > 1:
                action = next.split(' ')
                verb = action[0].lower()
                thing = action[1].lower()
                
                if verb == 'get' or verb == 'take':
                    add_items(thing, player, current_room)
                elif verb == 'drop':
                    print(thing)
                    drop_item(thing, player, current_room)
                else:
                    print('Unable to perform request')
            else:
                if option == 'i':
                    player.my_items()
                elif next == '?' and len(current_room.items) < 1:
                    print('There are no tools here.')
                elif next == '?':  
                    current_room.search()
                    print('To acquire: Type \033[2mget\033[0m \033[3mor\033[0m \033[2mtake\033[0m \033[2mitem\033[0m, To Unload: \033[2m drop item\033[0m \n')
                    
                
                elif next == 't':
                    go = input('\033[3mWhich direction shall we venture?\033[0m n,s,e,w: ')
                    go.lower()
                
                    if go == 'n' and hasattr(current_room, 'n_to'):
                        current_room = current_room.n_to
                        player.current_room = current_room
                        # * Prints the current description (the textwrap module might be useful here).
                        print(current_room)
                        # * Waits for user input and decides what to do.
                    elif go == 's' and hasattr(current_room, 's_to'):
                        current_room = current_room.s_to
                        player.current_room = current_room
                        # * Prints the current description (the textwrap module might be useful here).
                        print(current_room)
                        # * Waits for user input and decides what to do.
                    elif go == 'e' and hasattr(current_room, 'e_to'):
                        current_room = current_room.e_to
                        player.current_room = current_room
                        # * Prints the current description (the textwrap module might be useful here).
                        print(current_room)
                        # * Waits for user input and decides what to do.
                    elif go == 'w' and hasattr(current_room, 'w_to'):
                        current_room = current_room.w_to
                        player.current_room = current_room
                        # * Prints the current description (the textwrap module might be useful here).
                        print(current_room)
                        # * Waits for user input and decides what to do.
                    elif go == 'q':
                        # If the user enters "q", quit the game.
                        print('\nThank You for playing.\n')
                        is_where = False
                        is_playing = False
                    else:
                        # Print an error message if the movement isn't allowed.
                        # If the user enters a cardinal direction, attempt to move to the room there.
                        print('\nThat location doesn\'t exist. Please Try again.\n')
else:
    print("Something Went Wrong.")




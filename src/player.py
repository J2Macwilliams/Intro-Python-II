# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    pass
    def __init__(self, name, current_room ):
        self.name = name
        self.current_room = current_room
        self.items = []

    def __str__(self):
        return ' %s' % (self.current_room)

    def my_items(self):
        print(f" \033[3m I'm carrying: \033[0m {self.items}\n") 

    
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    
    def __init__(self, name, description, ):
        self.name = name 
        self.description = description
        self.items = []

    def __repr__(self):
        return '\nYour location is: \033[2m%s, %s.\033[0m \n' % (self.name, self.description)


    def search(self):
        print(f'\n {self.name} contains: {self.items}\n')
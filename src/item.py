class Item:
    pass
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __repr__(self):
        return '\n\033[7m %s \033[0m -- %s\n' % (self.name, self.description)


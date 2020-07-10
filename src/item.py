class Item:
    pass
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __repr__(self):
        return '\033[7m %s \033[0m -- %s' % (self.name, self.description)


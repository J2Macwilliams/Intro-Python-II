class Item:
    pass
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __repr__(self):
        return '\n %s - %s' % (self.name, self.description)


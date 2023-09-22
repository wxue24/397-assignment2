class Location(object):
    def __init__(self, name: int, treasure: bool):
        self.name = name
        self.treasure = treasure
        self.dug = False
    
    def getLocation(self):
        '''Returns name (index) of location'''
        return self.name
    
    def dig(self):
        '''Returns true if exists treasure, else false'''
        self.dug = True
        return self.treasure
    
    def hasBeenDug(self):
        return self.dug


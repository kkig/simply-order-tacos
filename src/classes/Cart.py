from classes.Menu import Menu
from collections import Counter

__all__ = ["Cart"]

class Cart():    
    def __init__(self):
        self.picked = Counter()
        self.total = 0
        self.menu = Menu()
        
    def add(self, name):
        name = name.strip()
        item = self.menu.get(name)
        if item:
            self.picked[item.name] += 1
            self.total += item.price
            return self.total
        return None
    
    def clear(self):
        self.picked.clear()
        self.total = 0

    
from classes.Menu import Menu

__all__ = ["Cart"]

class Cart(Menu):    
    def __init__(self):
        self.picked = dict()
        self.total = 0

    def __str__(self):
        return f"Total: ${self.total}"
        
    def add(self, name):
        item = super().get(name)
        if item:
            self.picked[item.name] = self.picked.get(item.name, 0) + item.price
            self.total = sum(self.picked.values())
            return self.total
        return None

    
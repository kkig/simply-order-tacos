from dataclasses import dataclass
from typing import List

__all__ = ["Manu"]


@dataclass
class Item:
    __slots__ = ["name", "price"]
    name: str
    price: float


class Menu:
    items = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    @classmethod
    def get_price(cls, name):
        name = name.title()
        if name in cls.items:
            return cls.items.get(name)
        return None
    
    @classmethod
    def get(cls, name):
        name = name.title()
        if name in cls.items:
            return Item(name, cls.items.get(name))
        return None

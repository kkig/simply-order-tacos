from dataclasses import dataclass
from csv import DictReader

__all__ = ["Manu"]


@dataclass
class Item:
    __slots__ = ["name", "price"]
    name: str
    price: float


class Menu:
    items = {}

    with open("src/db/menu.csv") as file:
        reader = DictReader(file)
        for row in reader:
            items[row["name"]] = float(row["price"])
    
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

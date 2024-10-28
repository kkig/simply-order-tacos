from dataclasses import dataclass
from csv import DictReader

__all__ = ["Manu", "MenuState"]


@dataclass
class Item:
    __slots__ = ["name", "price"]
    name: str
    price: float


class MenuState:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MenuState, cls).__new__(cls)
            cls._instance.db = cls._create_connection()
        return cls._instance
    
    @staticmethod
    def _create_connection():
        data = {}
        try:
            with open("src/db/menu.csv") as file:
                reader = DictReader(file)
                for row in reader:
                    data[row["name"]] = float(row["price"])
            return data
        except:
            return None

    def get(self):
        return self.db


class Menu:
    items = MenuState().get()
    
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

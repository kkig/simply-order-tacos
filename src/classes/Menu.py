from dataclasses import dataclass
from typing import List

__all__ = ["Item", "Manu"]


@dataclass
class Item:
    __slots__ = ["name", "price"]
    name: str
    price: float


@dataclass
class Menu:
    items: List[Item]
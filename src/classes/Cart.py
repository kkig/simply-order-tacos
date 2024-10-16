from classes.Menu import Menu, Item

__all__ = ["Cart"]

# def selections():
#     return [
#         Item("Baja Taco", 4.25),
#         Item("Burrito", 7.50),
#         Item("Bowl", 8.50),
#         Item("Nachos", 11.00),
#         Item("Quesadilla", 8.50),
#         Item("Super Burrito", 8.50),
#         Item("Super Quesadilla", 9.50),
#         Item("Taco", 3.00),
#         Item("Tortilla Salad", 8.00)
#         ]


class Cart:    
    def __init__(self, *selections) -> None:
        self.menu = selections
        # self.selected: dict[str, float] | None = None

    def __str__(self):
        return self.menu

    def get_price(self):
        item = self.menu[0]
        return item
        
    
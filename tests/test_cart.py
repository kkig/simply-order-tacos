import pytest   
from classes.Cart import Cart
from classes.Menu import Item
# from order_taqueria.get_orders import get_orders

@pytest.fixture
def list():
    return [
        Item("Baja Taco", 4.25),
        Item("Burrito", 7.50),
        Item("Bowl", 8.50),
        Item("Nachos", 11.00),
        Item("Quesadilla", 8.50),
        Item("Super Burrito", 8.50),
        Item("Super Quesadilla", 9.50),
        Item("Taco", 3.00),
        Item("Tortilla Salad", 8.00)
        ]

# @pytest.fixture
# def sample():
#     return ["Hello", "world"]

def test_nonselect(list):
    cart = Cart([Item("Taco", 3.00)]).get_price()
    assert cart == None
    # menu = list

    # # assert get_orders() == None
    # assert menu == None
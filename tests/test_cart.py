import pytest   
from classes.Cart import Cart

@pytest.fixture
def list():
    return {
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

def test_lower(list):
    cart = Cart(list)
    assert cart.add("taco") == {"Taco": 3.0}


def test_upper(list):
    cart = Cart(list)
    assert cart.add("Taco") == {"Taco": 3.0}
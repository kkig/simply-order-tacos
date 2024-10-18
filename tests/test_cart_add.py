from classes.Cart import Cart

def test_invalid():
    cart = Cart()
    cart.add("Banana")
    assert cart.total == 0


def test_upper():
    cart = Cart()
    cart.add("BOWL")
    assert cart.total == 8.5


def test_multiple():
    cart = Cart()
    cart.add("Baja Taco")
    assert cart.total == 4.25

    cart.add("Tortilla Salad")
    assert cart.total == 12.25


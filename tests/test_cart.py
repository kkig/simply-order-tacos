from classes.Cart import Cart

class TestCartAdd:
    def test_invalid(self):
        cart = Cart()
        cart.add("Banana")
        assert cart.total == 0

    def test_whitespace(self):
        cart = Cart()
        cart.add(" bowl ")
        assert cart.total == 8.5

    def test_upper(self):
        cart = Cart()
        cart.add("BOWL")
        assert cart.total == 8.5

    def test_multiple(self):
        cart = Cart()
        cart.add("Baja Taco")
        assert cart.total == 4.25

        cart.add("Tortilla Salad")
        assert cart.total == 12.25

class TestCartClear:
    def test_clear(self):
        cart = Cart()
        cart.add("Taco")
        cart.clear()
        assert cart.total == 0
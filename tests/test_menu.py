from src.classes import Menu, Item, MenuState

class TestMenuGet:
    def test_invalid(self):
        item = Menu.get("")
        assert item == None

    def test_upper(self):
        item = Menu.get("BOWL")
        assert item == Item(name='Bowl', price=8.5)


class TestMenuGetPrice:
    def test_name(self):
        item = Menu.get_price("Bowl")
        assert item == 8.50

    def test_invalid_name(self):
        assert Menu.get_price("Cheese") == None

    def test_upper(self):
        assert Menu.get_price("BOWL") == 8.50

    def test_lower(self):
        assert Menu.get_price("bowl") == 8.50

    
    class TestMenuState:
        def test_get(self):
            assert MenuState().get() is not None

        def test_instance(self):
            state1 = MenuState()
            state2 = MenuState()

            assert state1 == state2

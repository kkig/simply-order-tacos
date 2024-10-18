from src.classes import Menu

def test_name():
    item = Menu.get_price("Bowl")
    assert item == 8.50


def test_invalid_name():
    assert Menu.get_price("Cheese") == None


def test_upper():
    assert Menu.get_price("BOWL") == 8.50


def test_lower():
    assert Menu.get_price("bowl") == 8.50
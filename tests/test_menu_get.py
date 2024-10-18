from src.classes import Menu, Item

def test_invalid():
    item = Menu.get("")
    assert item == None

def test_upper():
    item = Menu.get("BOWL")
    assert item == Item(name='Bowl', price=8.5)
import pytest

from inventory import Inventory


def test_add_accumulates():
    inv = Inventory()
    inv.add("apple", 2)
    inv.add("apple", 3)
    assert inv.quantity("apple") == 5


def test_add_rejects_non_positive():
    with pytest.raises(ValueError):
        Inventory().add("apple", 0)


def test_total_value():
    inv = Inventory()
    inv.add("apple", 2)
    inv.add("pear", 1)
    assert inv.total_value({"apple": 0.5, "pear": 2.0}) == 3.0


def test_remove_negative_stock():
    inv = Inventory()
    inv.add("apple", 2)
    with pytest.raises(ValueError, match="not enough stock"):
        inv.remove("apple", 5)
    assert inv.quantity("apple") == 2


def test_remove_unknown_item():
    inv = Inventory()
    with pytest.raises(ValueError, match="item unknown"):
        inv.remove("apple", 5)


def test_remove_non_positive_quantity():
    inv = Inventory()
    inv.add("apple", 2)
    with pytest.raises(ValueError, match="quantity must be positive"):
        inv.remove("apple", 0)
    with pytest.raises(ValueError, match="quantity must be positive"):
        inv.remove("apple", -1)
    assert inv.quantity("apple") == 2


def test_remove_to_zero():
    inv = Inventory()
    inv.add("apple", 2)
    inv.remove("apple", 2)
    assert inv.quantity("apple") == 0
    assert "apple" not in inv.items()


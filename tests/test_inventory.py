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

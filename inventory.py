class Inventory:
    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def add(self, item: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._stock[item] = self._stock.get(item, 0) + quantity

    def remove(self, item: str, quantity: int) -> None:
        self._stock[item] = self._stock.get(item, 0) - quantity

    def quantity(self, item: str) -> int:
        return self._stock.get(item, 0)

    def items(self) -> list[str]:
        return sorted(self._stock)

    def total_value(self, prices: dict[str, float]) -> float:
        return sum(prices[item] * count for item, count in self._stock.items())

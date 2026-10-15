class Inventory:
    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def add(self, item: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self._stock[item] = self._stock.get(item, 0) + quantity

    def remove(self, item: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        if item not in self._stock:
            raise ValueError("item unknown")
        if self._stock[item] < quantity:
            raise ValueError("not enough stock")
        
        self._stock[item] -= quantity
        if self._stock[item] == 0:
            del self._stock[item]

    def quantity(self, item: str) -> int:
        return self._stock.get(item, 0)

    def items(self) -> list[str]:
        return sorted(self._stock)

    def total_value(self, prices: dict[str, float]) -> float:
        return sum(prices[item] * count for item, count in self._stock.items())

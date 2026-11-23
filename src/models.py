from typing import List


class Product:
    """Класс для описания товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация товара."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для описания категории товаров."""

    # Атрибуты класса — общие для всех объектов
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.products = products

        # Автоматически увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(products)

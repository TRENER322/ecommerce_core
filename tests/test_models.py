import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Сбрасывает счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


def test_product_initialization():
    """Тест корректности инициализации Product."""
    product = Product("Смартфон", "Мощный телефон", 59999.99, 10)
    assert product.name == "Смартфон"
    assert product.description == "Мощный телефон"
    assert product.price == 59999.99
    assert product.quantity == 10


def test_category_initialization():
    """Тест корректности инициализации Category."""
    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 2)

    category = Category("Электроника", "Все для дома", [p1, p2])

    assert category.name == "Электроника"
    assert category.description == "Все для дома"
    assert len(category.products) == 2
    assert category.products[0].name == "Товар 1"


def test_category_count():
    """Тест подсчета количества категорий."""
    Category("Категория 1", "Описание", [])
    Category("Категория 2", "Описание", [])
    assert Category.category_count == 2


def test_product_count():
    """Тест подсчета количества продуктов."""
    p1 = Product("Товар 1", "Описание", 100.0, 1)
    p2 = Product("Товар 2", "Описание", 200.0, 1)
    p3 = Product("Товар 3", "Описание", 300.0, 1)

    Category("Категория 1", "Описание", [p1, p2])
    Category("Категория 2", "Описание", [p3])

    assert Category.product_count == 3

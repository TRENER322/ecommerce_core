# E-commerce Core

Ядро интернет-магазина на ООП.

## Реализовано
- Класс `Product` — товар (название, описание, цена, количество).
- Класс `Category` — категория товаров с автоматическим подсчетом количества категорий (`category_count`) и товаров (`product_count`).

## Запуск
```bash
poetry install
poetry run python main.py
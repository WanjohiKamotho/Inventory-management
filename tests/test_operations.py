import pytest

from app.operations import (
    get_all_products,
    get_product_by_id,
    add_product,
    update_product
)
from app.data import inventory


def test_get_all_products():
    products = get_all_products()

    assert products == inventory


def test_get_product_by_id():
    product = get_product_by_id(1)

    assert product["id"] == 1


def test_add_product():
    original_length = len(inventory)

    new_product = {
        "barcode": "123456789",
        "product_name": "Test Product",
        "brands": "Test Brand",
        "ingredients_text": "Test Ingredients",
        "category": "Test Category",
        "price": 100,
        "stock": 5
    }

    added_product = add_product(new_product)

    assert len(inventory) == original_length + 1
    assert added_product["product_name"] == "Test Product"


def test_update_product():
    updated_product = update_product(1, {
        "price": 500
    })

    assert updated_product["price"] == 500
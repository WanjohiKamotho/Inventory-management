from unittest.mock import patch

from app.external_api import fetch_product_by_barcode


@patch("app.external_api.requests.get")
def test_fetch_product_by_barcode(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "status": 1,
        "code": "123456789",
        "product": {
            "product_name": "Mock Product",
            "brands": "Mock Brand",
            "ingredient_text": "Mock Ingredients",
            "categories": "Mock Category"
        }
    }

    product = fetch_product_by_barcode("123456789")

    assert product["barcode"] == "123456789"
    assert product["product_name"] == "Mock Product"
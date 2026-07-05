import requests

BASE_URL = "https://world.openfoodfacts.org/api/v2/product"
HEADERS = {
    "User-Agent": "InventoryManagement/1.0 (learning project)"
}

def fetch_product_by_barcode(barcode):
    url = f"{BASE_URL}/{barcode}.json"

    response = requests.get(url, headers=HEADERS)
    if response .status_code != 200:
        return None
    
    data = response.json()

    if data.get("status") != 1:
        return None
    
    product = data.get("product", {})

    return {
        "barcode": data.get("code"),
        "product_name": product.get("product_name"),
        "brands": product.get("brands"),
        "ingredient_text": product.get("ingredient_text"),
        "category": product.get("categories")
    }


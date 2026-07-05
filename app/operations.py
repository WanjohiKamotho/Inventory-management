from app.data import inventory
from app.external_api import fetch_product_by_barcode

def get_all_products():
    return inventory


def get_product_by_id(product_id):
    return next(
        (product for product in inventory if product["id"] == product_id),None
    )

def add_product(product):
    next_id = max(item["id"] for item in inventory) + 1

    product ["id"] = next_id
    inventory.append(product)

    return product

def update_product(product_id, updated_data):
    product = get_product_by_id(product_id)

    if product:
        product.update(updated_data)
        return(product)
    
    return None

def delete_product(product_id):
    product = get_product_by_id(product_id)

    if product:
        inventory.remove(product)
        return True
    
    return False

def import_product(barcode):
    product = fetch_product_by_barcode(barcode)

    if product is None:
        return None
    
    existing_product = next((item for item in inventory if item["barcode"] == barcode), None)
    if existing_product:
        return existing_product
    
    
    new_id = max(item["id"] for item in inventory) + 1

    product["id"] = new_id
    product["price"] = 0
    product["stock"] = 0

    inventory.append(product)
    return product
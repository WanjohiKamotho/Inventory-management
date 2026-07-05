from flask import Flask, jsonify, request
from app.operations import (
    get_all_products,
    get_product_by_id,
    add_product,
    update_product,
    delete_product
)

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Inventory-Management"}), 200


@app.route("/inventory", methods=["GET"])
def get_inventory():
    products = get_all_products()
    return jsonify(products), 200

@app.route("/inventory/<int:product_id>", methods=["GET"])
def get_item(product_id):
    product = get_product_by_id(product_id)

    if product:
        return jsonify(product), 200
    
    return jsonify({"error": "Product not found"}), 404

@app.route("/inventory", methods=["POST"])
def create_product():
    product = request.get_json()

    new_product=add_product(product)
    return jsonify(new_product), 201

@app.route("/inventory/<int:product_id>", methods=["PATCH"])
def edit_product(product_id):
    updated_data = request.get_json()

    updated_product = update_product(product_id, updated_data)

    if updated_product:
        return jsonify(updated_product), 200
    
    return jsonify({"error": "Product not found"}),404

@app.route("/inventory/<int:product_id>", methods=["DELETE"])
def remove_item(product_id):
    deleted = delete_product(product_id)
    if deleted:
        return jsonify({"message": "Product deleted successfully"}),200
    return jsonify({"error": "Product not found"}),404


if __name__ == "__main__":
    app.run(debug=True)
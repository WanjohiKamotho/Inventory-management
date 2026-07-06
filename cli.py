import requests

BASE_URL = "http://127.0.0.1:5000"



while True:

    print ("\n======Inventory Management=====")
    print("1. View inventory")
    print("2. View product by ID")
    print("3. Add products")
    print("4. Update product")
    print("5. Delete Product")
    print("6. Search OpenFoodFacts")
    print("7. Import Products")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice  == "1":
        response = requests.get(f"{BASE_URL}/inventory")

        if response.status_code == 200:
            products = response.json()

            for product in products:
                print(product)
        else:
            print("Error retrieving data")

    elif choice == "2":
        product_id = input("Enter product ID: ")

        response = requests.get(f"{BASE_URL}/inventory/{product_id}")
        if response.status_code == 200:
            print(response.json())
        else:
            print("Product not found.")

    elif choice == "3":
        barcode = input("Barcode: ")
        product_name = input("Product name: ")
        brands = input("Brand: ")
        ingredients_text = input("Ingredients: ")
        category = input("Category: ")
        price = float(input("Price: "))
        stock = int(input("stock: "))

        product = {
        "barcode": barcode,
        "product_name": product_name,
        "brands": brands,
        "ingredients_text": ingredients_text,
        "category": category,
        "price": price,
        "stock": stock
        }
        response = requests.post(f"{BASE_URL}/inventory", json=product)

        if response.status_code == 201:
            print("Product added successfully!")
            print(response.json())
        else:
            print("Failed to add product, try again!")
    
    elif choice == "4":
        product_id = input("Enter producct ID: ")

        updated_data = {}

        price = input("New price: ")
        stock = input("New stock: ")

        if price:
            updated_data["price"] = float(price)
        if stock:
            updated_data["stock"] = int(stock)
        
        response = requests.patch(f"{BASE_URL}/inventory/{product_id}", json=updated_data)
        if response.status_code == 200:
            print("Product updated successfully!")
            print(response.json())

        else:
            print("Failed to update product")

    elif choice == "5":
        product_id = input("Enter product ID: ")

        response = requests.delete(f"{BASE_URL}/inventory/{product_id}")
        if response.status_code == 200:
            print("Product deleted successfully!")
        else:
            print("Product not found")

    elif choice == "6":
        barcode = input("Enter barcode: ")

        response = requests.get(f"{BASE_URL}/search/{barcode}")

        if response.status_code == 200:
            print(response.json())
        else:
            print("Product not found.")

    elif choice == "7":
        barcode = input("Enter barcode: ")

        response = requests.post(f"{BASE_URL}/inventory/import/{barcode}")

        if response.status_code == 201:
            print("Product imported successfully!")
            print(response.json())
        else:
            print("Failed to import product")
    


    elif choice == "8":
        break
    
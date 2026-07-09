# Inventory Management System

## Description

A Flask-based Inventory Management System that allows users to manage products through a REST API and a Command Line Interface (CLI). The application also integrates with the OpenFoodFacts API to search and import product information using barcodes.

## Features

* View all products
* View a product by ID
* Add a new product
* Update an existing product
* Delete a product
* Search products using the OpenFoodFacts API
* Import products from OpenFoodFacts into the inventory
* Command Line Interface (CLI)
* Unit tests using Pytest

## Technologies Used

* Python
* Flask
* Requests
* Pytest

## Installation

1. Clone the repository.
2. Navigate into the project folder.
3. Create and activate a virtual environment.
4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python3 -m app.main
```

Run the CLI in another terminal:

```bash
python3 cli.py
```

Run the tests:

```bash
pytest
```

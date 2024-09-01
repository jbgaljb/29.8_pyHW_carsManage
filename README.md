# Car and Customer Management System

This Python project is a simple command-line interface (CLI) for managing cars and customers stored in SQLite databases. The system allows you to add, delete, and view records in the "cars" and "customers" tables.

## Features

- **Add Customers:** Add a new customer to the `customers` table.
- **Delete Customers:** Delete an existing customer from the `customers` table by their ID.
- **View Customers:** View all customers stored in the `customers` table.
- **Add Cars:** Add a new car to the `cars` table, associating it with an existing customer.
- **Delete Cars:** Delete an existing car from the `cars` table by its ID.
- **View Cars:** View all cars stored in the `cars` table.

## Prerequisites

- **Python 3.x**
- **SQLite3**

## Setup and Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your machine.
3. Make sure you have `sqlite3` installed (it typically comes with Python).
4. Create the necessary SQLite databases (`cars.py` and `customers.py`) and corresponding tables:
   - `cars` table: should include columns like `customer_id`, `car_id`, `brand`, `model`, `color`.
   - `customers` table: should include columns like `id`, `full_name`, `telephone`, `email`.

## How to Use

1. **Run the Application:**

   Execute the script by running:

   ```bash
   python app.py

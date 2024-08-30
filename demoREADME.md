# JSON Database Structure

This project consists of two JSON files representing a simple database structure: `customers.json` and `cars.json`. These files simulate a basic relational database, where `customers.json` contains customer information, and `cars.json` contains car information linked to customers through a foreign key relationship.
Pandas has to installed.

## `customers.json`

The `customers.json` file stores details about customers. Each customer has the following fields:

- **id:** A unique identifier (UUID) for each customer. This serves as the primary key.
- **full_name:** The full name of the customer.
- **telephone:** The customer's telephone number.
- **email:** The customer's email address.

### Example:
```json
{
  "id": "c1b8fce3-7a9f-42a9-b3b9-3d5f6b7e2b4f",
  "full_name": "John Doe",
  "telephone": "+1-555-1234",
  "email": "john.doe@example.com"
}
{
  "customer_id": "c1b8fce3-7a9f-42a9-b3b9-3d5f6b7e2b4f",
  "brand": "Toyota",
  "model": "Camry",
  "color": "Blue"
}

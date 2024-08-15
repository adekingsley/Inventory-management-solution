# Inventory Management System

## Overview

The Inventory Management System is a comprehensive solution designed to manage and track inventory, categories, items, suppliers, purchases, and sales. This system provides an efficient way to handle stock levels, purchase records, sales transactions, and supplier information. The project is built using Django and Django REST Framework (DRF), ensuring a robust and scalable backend.

## Features

- **Category Management:** Organize items into various categories.
- **Item Management:** Add, update, and track items and their stock levels.
- **Supplier Management:** Manage supplier information.
- **Purchase Management:** Record purchases and update stock levels accordingly.
- **Sales Management:** Record sales and update stock levels accordingly.
- **Stock Status Tracking:** Automatically track stock status (in stock, out of stock, overstock) based on predefined thresholds.
- **API Documentation:** Detailed API documentation available via Postman.

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default, can be configured for other databases)
- **Containerization:** Docker
- **Environment Management:** Python venv

## Getting Started

### Prerequisites

- Docker (for Docker-based setup)
- Python 3.8+ (for non-Docker setup)
- Git

### Setup Using Docker

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/adekingsley/Inventory-management-solution.git
   cd inventory-management
   ```

2. **Build and Run the Docker Containers:**

   ```sh
   docker-compose up --build
   ```

3. **Apply Migrations:**

   ```sh
   docker-compose run web python manage.py migrate
   ```

4. **Create a Superuser:**

   ```sh
   docker-compose run web python manage.py createsuperuser
   ```

5. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8000`.

### Setup Without Docker

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/adekingsley/inventory-management-solution.git
   cd inventory-management
   ```

2. **Create and Activate a Virtual Environment:**

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**

   ```sh
   python manage.py runserver
   ```

7. **Access the Application:**
   Open your web browser and navigate to `http://localhost:8000`.

### API Documentation

Detailed API documentation is available on Postman. You can access it using the following link:

[Postman Documentation](https://www.postman.com/xmcideas/workspace/inventory-management/documentation/33017052-eb76d1b7-062d-4c87-a058-433fae606397)

## Models and Their Relationships

### Category

- **Attributes:**
  - `id`: UUID
  - `name`: CharField (unique)
  - `description`: TextField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### Item

- **Attributes:**
  - `id`: UUID
  - `name`: CharField
  - `slug`: SlugField (unique)
  - `price`: DecimalField
  - `description`: TextField
  - `category`: ForeignKey (Category)
  - `image`: ImageField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### Supplier

- **Attributes:**
  - `id`: UUID
  - `name`: CharField (unique)
  - `contact_name`: CharField
  - `contact_email`: EmailField
  - `contact_phone`: CharField
  - `address`: TextField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### Purchase

- **Attributes:**
  - `id`: UUID
  - `item`: ForeignKey (Item)
  - `supplier`: ForeignKey (Supplier)
  - `quantity`: FloatField
  - `price`: FloatField
  - `total_amount`: FloatField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### Sale

- **Attributes:**
  - `id`: UUID
  - `item`: ForeignKey (Item)
  - `quantity`: FloatField
  - `total_amount`: FloatField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### Stock

- **Attributes:**
  - `id`: UUID
  - `item`: ForeignKey (Item)
  - `quantity`: PositiveIntegerField
  - `status`: CharField (choices: `OUT_OF_STOCK`, `IN_STOCK`, `OVERSTOCK`)
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

### Inventory

- **Attributes:**
  - `id`: UUID
  - `item`: ForeignKey (Item)
  - `purchase`: ForeignKey (Purchase)
  - `sale`: ForeignKey (Sale)
  - `purchase_quantity`: FloatField
  - `sale_quantity`: FloatField
  - `total_balance_quantity`: FloatField
  - `created_at`: DateTimeField
  - `updated_at`: DateTimeField

## How It Works

### Stock Status

The `Stock` model includes a `status` field to indicate whether an item is in stock, out of stock, or overstocked. This status is automatically updated based on the quantity thresholds defined:

- **Out of Stock:** Quantity < 10
- **In Stock:** 10 ≤ Quantity ≤ 50
- **Overstock:** Quantity > 50

### Signals

Django signals are used to update stock status before saving a `Purchase` or `Sale` instance.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Submit a pull request.

## License

This project is licensed under the XMC License.

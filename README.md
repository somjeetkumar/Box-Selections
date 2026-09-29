# Box Selection System

This is a small Django REST Framework project for selecting a suitable shipping box for an order.

The idea is simple. An order contains one or more products. Every product has length, width, height and weight. Boxes also have their internal dimensions, maximum weight and cost.

The system checks the products in an order and tries to find a box in which the products can fit.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Git and GitHub

## Project Features

- Create products
- Create boxes
- Create orders with products and quantity
- Check product weight
- Check box maximum weight
- Check product dimensions
- Check different product orientations
- Recommend a suitable box
- Basic API validation

## Setup

First clone the project.

```bash
git clone <your-github-repository-url>
cd <project-folder>
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the packages:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Run the server:

```bash
python manage.py runserver
```

The project will run on:

```text
http://127.0.0.1:8000/
```

## Main APIs

### Product API

```text
POST /products/
```

Example:

```json
{
    "name": "Laptop",
    "length": 30,
    "width": 20,
    "height": 5,
    "weight": 2
}
```

### Box API

```text
POST /boxes/
```

Example:

```json
{
    "name": "Small Box",
    "internal_length": 40,
    "internal_width": 30,
    "internal_height": 10,
    "max_weight": 5,
    "cost": 50
}
```

### Order API

```text
POST /orders/
```

Example:

```json
{
    "items": [
        {
            "product": 1,
            "quantity": 2
        }
    ]
}
```

### Recommend Box

```text
GET /orders/<order_id>/recommend-box/
```

## How Box Selection Works

First I calculate the total weight of all products in the order.

I also calculate the total volume.

Then I get boxes which can handle the total weight.

After that I check whether the products can physically fit inside the box.

A product can be rotated in different ways, so the code checks different orientations of the product.

After finding suitable boxes, the code selects the box according to the selection rule used in the project.

## Testing

Run the tests using:

```bash
python manage.py test
```

The test cases are explained in `TEST_CASES.md`.

The actual test command and output are kept in `TEST_OUTPUT.md`.

## AI Usage

I used AI tools while working on this assignment.

More information about the AI usage is available in:

```text
AI_USAGE.md
```

## Learning

My learning from this assignment is written in:

```text
LEARNING.md
```

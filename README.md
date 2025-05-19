### coffee-shop-style-domain
A simple Python backend application that models a coffee shop domain using object-oriented design. This app tracks customers, the coffees they order, and individual orders. It's ideal for experimenting with object relationships, data validation, and business logic modeling.

## Features
Manage Customers with validated names

Define Coffee types with immutable properties

Track Orders between customers and coffees

Query order history, customer preferences, and coffee popularity

Built-in logic for calculating averages, totals, and customer rankings

## Domain Model
This app models a basic coffee shop system using three main entities:

- Customer

- Coffee

- Order

### Relationships
- A Customer can place many Orders

- A Coffee can be part of many Orders

- An Order belongs to both a Customer and a Coffee

This forms a many-to-many relationship between Customer and Coffee via the Order model.

  ## Getting Started
# 1. Clone the Repository
- git clone git@github.com:<ErnestKamau/coffee-shop.git
- cd coffee-shop

# 2. Install Dependencies
Use pipenv to install the development environment.
- pipenv install
- pipenv shell

# 3. Run the Project
You can run the project in interactive mode using the built-in debug.py script.
- python debug.py

Use this script to manually create customers, coffees, and orders and print results to the console.

## AUTHOR
- GitHub: @ErnestKamau
- Ernest Kamau

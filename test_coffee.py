import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    """Test that a Coffee object is correctly initialized."""
    coffee = Coffee(name="Latte")
    assert coffee.name == "Latte"

def test_coffee_invalid_name():
    """Test that setting an invalid Coffee name raises a ValueError."""
    with pytest.raises(ValueError):
        Coffee(name="")

def test_coffee_orders():
    """
    Test that orders can be associated with a Coffee object and retrieved correctly.
    """
    coffee = Coffee(name="Latte")
    customer = Customer(name="Alice")
    customer.create_order(coffee, 5.0)
    orders = coffee.orders()
    assert len(orders) == 1
    assert orders[0].coffee == coffee

def test_coffee_customers():
    """
    Test that customers who ordered a specific Coffee can be retrieved.
    """
    coffee = Coffee(name="Latte")
    customer1 = Customer(name="Alice")
    customer2 = Customer(name="Bob")
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    customers = coffee.customers()
    assert customer1 in customers
    assert customer2 in customers

def test_coffee_num_orders():
    """
    Test that the number of orders for a specific Coffee is calculated correctly.
    """
    coffee = Coffee(name="Latte")
    customer = Customer(name="Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2

def test_coffee_average_price():
    """
    Test that the average price of orders for a Coffee is calculated correctly.
    """
    coffee = Coffee(name="Latte")
    customer = Customer(name="Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 7.0)
    assert coffee.average_price() == 6.0

def test_coffee_no_orders():
    """
    Test that a Coffee with no orders has a num_orders of 0 and average_price of 0.0.
    """
    coffee = Coffee(name="Latte")
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0.0

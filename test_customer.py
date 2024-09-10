import pytest
from customer import Customer
from order import Order
from coffee import Coffee

def test_customer_initialization():
    """Test that a Customer object is correctly initialized."""
    customer = Customer(name="Faith")
    assert customer.name == "Faith"

def test_customer_invalid_name():
    """
    Test that initializing a Customer with an invalid name raises a ValueError.

    The name should be a string between 1 and 15 characters.
    """
    with pytest.raises(ValueError):
        Customer(name="")

def test_create_order():
    """
    Test that creating an order correctly associates a Customer with a Coffee
    and sets the correct price.
    """
    customer = Customer(name="Faith")
    coffee = Coffee(name="Americano")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_customer_orders():
    """
    Test that the orders method returns all orders associated with a Customer.
    """
    customer = Customer(name="Faith")
    coffee1 = Coffee(name="Americano")
    coffee2 = Coffee(name="Flat white")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)
    orders = customer.orders()
    assert len(orders) == 2
    assert any(order.price == 5.0 for order in orders)
    assert any(order.price == 6.0 for order in orders)

def test_customer_coffees():
    """
    Test that the coffees method returns all unique Coffee objects ordered by the Customer.
    """
    customer = Customer(name="Alice")
    coffee1 = Coffee(name="Americano")
    coffee2 = Coffee(name="Flat white")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)
    coffees = customer.coffees()
    assert coffee1 in coffees
    assert coffee2 in coffees
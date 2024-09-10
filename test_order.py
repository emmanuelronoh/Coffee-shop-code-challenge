import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_order_initialization():
    """Test that an Order object is correctly initialized."""
    customer = Customer(name="Faith")
    coffee = Coffee(name="Americano")
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_customer():
    """
    Test that initializing an Order with an invalid customer raises a ValueError.

    The customer must be an instance of Customer.
    """
    coffee = Coffee(name="Americano")
    with pytest.raises(ValueError):
        Order("InvalidCustomer", coffee, 5.0)

def test_order_invalid_coffee():
    """
    Test that initializing an Order with an invalid coffee raises a ValueError.

    The coffee must be an instance of Coffee.
    """
    customer = Customer(name="Faith")
    with pytest.raises(ValueError):
        Order(customer, "InvalidCoffee", 5.0)

def test_order_invalid_price():
    """
    Test that initializing an Order with an invalid price raises a ValueError.

    The price must be between 1.0 and 10.0.
    """
    customer = Customer(name="Faith")
    coffee = Coffee(name="Americano")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)

def test_order_repr():
    """
    Test that the __repr__ method of the Order class returns the correct string representation.
    """
    customer = Customer(name="Faith")
    coffee = Coffee(name="Americano")
    order = Order(customer, coffee, 5.0)
    assert repr(order) == "Order(customer='Faith', coffee='Americano', price=5.0)"

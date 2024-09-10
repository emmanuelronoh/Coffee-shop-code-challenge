import pytest
from coffee import Coffee
from customer import Customer
from order import Order

@pytest.fixture
def setup_data():
    """Fixture to set up test data."""
    # Create customers
    customer1 = Customer("Faith")
    customer2 = Customer("Victor")
    customer3 = Customer("Charlie")
    
    # Create coffees
    coffee1 = Coffee("Flat white")
    coffee2 = Coffee("Americano")
    
    # Create orders
    Order(customer1, coffee1, 5.0)
    Order(customer2, coffee1, 4.5)
    Order(customer3, coffee2, 6.0)
    
    return coffee1, coffee2, customer1, customer2, customer3

def test_coffee_initialization():
    coffee = Coffee("Mocha")
    assert coffee.name == "Mocha"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("so")  # Name too short

    with pytest.raises(ValueError):
        Coffee(1234)  # Name is not a string

def test_orders_method(setup_data):
    coffee1, coffee2, customer1, customer2, _ = setup_data
    orders = coffee1.orders()
    assert len(orders) == 2
    assert all(order.coffee == coffee1 for order in orders)

def test_customers_method(setup_data):
    coffee1, _, customer1, customer2, _ = setup_data
    customers = coffee1.customers()
    assert len(customers) == 2
    assert customer1 in customers
    assert customer2 in customers

def test_num_orders_method(setup_data):
    coffee1, coffee2, _, _, _ = setup_data
    assert coffee1.num_orders() == 2
    assert coffee2.num_orders() == 1

def test_average_price_method(setup_data):
    coffee1, coffee2, _, _, _ = setup_data
    assert coffee1.average_price() == (5.0 + 4.5) / 2
    assert coffee2.average_price() == 6.0

def test_no_orders_for_new_coffee():
    coffee = Coffee("Americano")
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0.0

def test_order_repr():
    coffee = Coffee("Cappuccino")
    customer = Customer("Faith")
    order = Order(customer, coffee, 3.5)
    assert repr(order) == f"Order(customer={customer.name!r}, coffee={coffee.name!r}, price={order.price})"

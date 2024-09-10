"""Debugging script to test Customer class methods."""

from customer import Customer
from coffee import Coffee
from order import Order

# Sample data for testing
coffee1 = Coffee(name="Americano")
coffee2 = Coffee(name="Flat white")

customer1 = Customer(name="Victor")
customer2 = Customer(name="Faith")

# Create some orders
order1 = customer1.create_order(coffee1, 5.0)
order2 = customer1.create_order(coffee2, 4.0)
order3 = customer2.create_order(coffee1, 6.0)

# Print outputs
print("Customer 1 orders:", customer1.orders())
print("Customer 1 coffees:", customer1.coffees())
print("Customer 2 orders:", customer2.orders())
print("Coffee1 orders:", coffee1.orders())
print("Coffee2 orders:", coffee2.orders())
print("Customer who spent most on Coffee1:", Customer.most_aficionado(coffee1))



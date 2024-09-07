"""This module defines the Order class for managing orders in the coffee shop."""

from coffee import Coffee
from customer import Customer

class Order:
    """Represents an order made by a customer for a specific coffee."""
    
    orders = []  # Class-level attribute to store all orders

    def __init__(self, customer, coffee, price):
        """
        Initializes an Order object and appends it to the class-level orders list.

        Args:
            customer (Customer): The customer who made the order.
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order.

        Raises:
            ValueError: If the arguments are not of the correct type.
        """
        self._customer = None
        self._coffee = None
        self._price = None
        self.customer = customer  # This will trigger the setter
        self.coffee = coffee      # This will trigger the setter
        self.price = price        # This will trigger the setter
        Order.orders.append(self)  # Add the order to the class-level list

    @property
    def customer(self):
        """Returns the customer who made the order."""
        return self._customer

    @customer.setter
    def customer(self, value):
        """
        Sets the customer for the order with validation.

        Args:
            value (Customer): The customer making the order.

        Raises:
            ValueError: If the value is not an instance of Customer.
        """
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        self._customer = value

    @property
    def coffee(self):
        """Returns the coffee being ordered."""
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        """
        Sets the coffee for the order with validation.

        Args:
            value (Coffee): The coffee being ordered.

        Raises:
            ValueError: If the value is not an instance of Coffee.
        """
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee.")
        self._coffee = value

    @property
    def price(self):
        """Returns the price of the order."""
        return self._price

    @price.setter
    def price(self, value):
        """
        Sets the price of the order with validation.

        Args:
            value (float): The price of the order.

        Raises:
            ValueError: If the price is not between 1.0 and 10.0.
        """
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = value

    def __repr__(self):
        """Returns a string representation of the order."""
        return (f"Order(customer={self.customer.name!r}, coffee={self.coffee.name!r}, "
                f"price={self.price})")

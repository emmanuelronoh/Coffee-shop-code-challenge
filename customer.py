"""This module defines the Customer class for managing customer information and their orders."""

from coffee import Coffee

class Customer:
    """Represents a customer in the coffee shop."""

    def __init__(self, name):
        """
        Initializes a Customer object with a name.

        Args:
            name (str): The name of the customer.

        Raises:
            ValueError: If the name is not a valid string.
        """
        self._name = None
        self.name = name  

    @property
    def name(self):
        """Returns the name of the customer."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the customer with validation.

        Args:
            value (str): The name of the customer.

        Raises:
            ValueError: If the name is not a string between 1 and 15 characters.
        """
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def __repr__(self):
        """Returns a string representation of the customer."""
        return f"Customer(name={self.name!r})"

    def orders(self):
        """
        Retrieves all orders made by the customer.

        Returns:
            list: A list of Order objects associated with the customer.
        """
        from order import Order  
        return [order for order in Order.orders if order.customer == self]

    def coffees(self):
        """
        Retrieves all unique coffees ordered by the customer.

        Returns:
            list: A list of unique Coffee objects ordered by the customer.
        """
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        """
        Creates a new order for the customer.

        Args:
            coffee (Coffee): The coffee being ordered.
            price (float): The price of the order.

        Returns:
            Order: The created Order object.
        """
        from order import Order  # Local import to avoid circular import
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """
        Finds the customer who has spent the most on a specific type of coffee.

        Args:
            coffee (Coffee): The coffee to check.

        Returns:
            Customer or None: The customer who has spent the most on the given coffee,
                               or None if no orders exist for that coffee.

        Raises:
            ValueError: If the provided argument is not an instance of Coffee.
        """
        if not isinstance(coffee, Coffee):
            raise ValueError("The provided argument must be an instance of Coffee.")

        from order import Order  # Local import to avoid circular import
        customer_orders = {}
        for order in Order.orders:
            if order.coffee == coffee:
                if order.customer not in customer_orders:
                    customer_orders[order.customer] = 0
                customer_orders[order.customer] += order.price
        
        if not customer_orders:
            return None
        
        return max(customer_orders, key=customer_orders.get)

"""This module defines the Coffee class for managing coffee types and their orders."""

class Coffee:
    """Represents a type of coffee."""

    def __init__(self, name):
        """
        Initializes a Coffee object with a name.

        Args:
            name (str): The name of the coffee.

        Raises:
            ValueError: If the name is less than 3 characters long.
        """
        self._name = None
        self.name = name  # Use property setter for validation

    @property
    def name(self):
        """Returns the name of the coffee."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the coffee with validation.

        Args:
            value (str): The name of the coffee.

        Raises:
            ValueError: If the name is less than 3 characters long.
        """
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = value

    def __repr__(self):
        """Returns a string representation of the coffee."""
        return f"Coffee(name={self.name!r})"

    def orders(self):
        """
        Retrieves all orders associated with this coffee.

        Returns:
            list: A list of Order objects where this coffee is ordered.
        """
        from order import Order  # Local import to avoid circular dependency
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        """
        Retrieves all unique customers who have ordered this coffee.

        Returns:
            list: A list of unique Customer objects who have ordered this coffee.
        """
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        """
        Counts the number of orders for this coffee.

        Returns:
            int: The number of orders for this coffee.
        """
        return len(self.orders())

    def average_price(self):
        """
        Calculates the average price of orders for this coffee.

        Returns:
            float: The average price of the orders. Returns 0.0 if no orders exist.
        """
        orders = self.orders()
        if not orders:
            return 0.0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)

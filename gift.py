"""Contains the Gift class for the registry."""


class Gift:
    """Represents a gift in the registry."""

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.purchased = False

    def to_dict(self):
        """Convert a gift into a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "purchased": self.purchased
        }
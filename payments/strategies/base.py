
from abc import ABC, abstractmethod
from decimal import Decimal


class PaymentStrategy(ABC):
    """
    Abstract base class for all payment methods.

    Every payment method must implement the pay() method.
    """

    @abstractmethod
    def pay(self, amount: Decimal) -> str:
        """
        Simulate processing a payment.

        Args:
            amount: Amount to be paid.

        Returns:
            A payment confirmation message.
        """
        pass

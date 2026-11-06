
from decimal import Decimal
from .strategies import PaymentStrategy


class Checkout:
    """
    Handles checkout using an interchangeable payment strategy.
    """

    def __init__(self, payment_strategy: PaymentStrategy):
        self.set_payment_strategy(payment_strategy)

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        """
        Set or change the payment strategy.
        """
        if not isinstance(payment_strategy, PaymentStrategy):
            raise TypeError(
                "Payment strategy must be an instance of PaymentStrategy."
            )

        self.payment_strategy = payment_strategy

    def process_payment(self, amount: Decimal) -> str:
        """
        Delegate payment processing to the selected strategy.
        """
        return self.payment_strategy.pay(amount)

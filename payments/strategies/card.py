
from decimal import Decimal
from .base import PaymentStrategy


class CardPayment(PaymentStrategy):
    """
    Simulates a debit or credit card payment.
    """

    def pay(self, amount: Decimal) -> str:
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        return f"Card payment of GHS {amount:.2f} successful."

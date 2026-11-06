
from decimal import Decimal
from .base import PaymentStrategy


class MobileMoneyPayment(PaymentStrategy):
    """
    Simulates a Mobile Money payment.
    """

    def pay(self, amount: Decimal) -> str:
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        return f"Mobile Money payment of GHS {amount:.2f} successful."

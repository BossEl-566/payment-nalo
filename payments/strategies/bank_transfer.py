
from decimal import Decimal
from .base import PaymentStrategy


class BankTransferPayment(PaymentStrategy):
    """
    Simulates a bank transfer payment.
    """

    def pay(self, amount: Decimal) -> str:
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        return f"Bank Transfer payment of GHS {amount:.2f} successful."

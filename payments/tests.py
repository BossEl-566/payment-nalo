
from decimal import Decimal

from django.test import SimpleTestCase

from .checkout import Checkout
from .strategies import (
    PaymentStrategy,
    MobileMoneyPayment,
    CardPayment,
    BankTransferPayment,
)


class PaymentStrategyTests(SimpleTestCase):
    """
    Tests for the individual payment strategies.
    """

    def test_abstract_class_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            PaymentStrategy()

    def test_mobile_money_payment(self):
        payment = MobileMoneyPayment()

        result = payment.pay(Decimal("100.00"))

        self.assertEqual(
            result,
            "Mobile Money payment of GHS 100.00 successful."
        )

    def test_card_payment(self):
        payment = CardPayment()

        result = payment.pay(Decimal("200.00"))

        self.assertEqual(
            result,
            "Card payment of GHS 200.00 successful."
        )

    def test_bank_transfer_payment(self):
        payment = BankTransferPayment()

        result = payment.pay(Decimal("300.00"))

        self.assertEqual(
            result,
            "Bank Transfer payment of GHS 300.00 successful."
        )

    def test_zero_amount_is_rejected(self):
        strategies = [
            MobileMoneyPayment(),
            CardPayment(),
            BankTransferPayment(),
        ]

        for strategy in strategies:
            with self.subTest(strategy=type(strategy).__name__):
                with self.assertRaises(ValueError):
                    strategy.pay(Decimal("0.00"))

    def test_negative_amount_is_rejected(self):
        strategies = [
            MobileMoneyPayment(),
            CardPayment(),
            BankTransferPayment(),
        ]

        for strategy in strategies:
            with self.subTest(strategy=type(strategy).__name__):
                with self.assertRaises(ValueError):
                    strategy.pay(Decimal("-50.00"))


class CheckoutTests(SimpleTestCase):
    """
    Tests for checkout and strategy switching.
    """

    def test_checkout_with_mobile_money(self):
        checkout = Checkout(MobileMoneyPayment())

        result = checkout.process_payment(Decimal("150.00"))

        self.assertEqual(
            result,
            "Mobile Money payment of GHS 150.00 successful."
        )

    def test_checkout_can_switch_payment_method(self):
        checkout = Checkout(MobileMoneyPayment())

        first_result = checkout.process_payment(
            Decimal("100.00")
        )

        checkout.set_payment_strategy(CardPayment())

        second_result = checkout.process_payment(
            Decimal("250.00")
        )

        checkout.set_payment_strategy(BankTransferPayment())

        third_result = checkout.process_payment(
            Decimal("500.00")
        )

        self.assertIn("Mobile Money", first_result)
        self.assertIn("Card payment", second_result)
        self.assertIn("Bank Transfer", third_result)

    def test_invalid_strategy_on_creation(self):
        with self.assertRaises(TypeError):
            Checkout("cash")

    def test_invalid_strategy_on_switch(self):
        checkout = Checkout(MobileMoneyPayment())

        with self.assertRaises(TypeError):
            checkout.set_payment_strategy("cash")

    def test_checkout_delegates_to_strategy(self):
        class SpyPayment(PaymentStrategy):
            def __init__(self):
                self.last_amount = None

            def pay(self, amount: Decimal) -> str:
                self.last_amount = amount
                return "Simulated spy payment"

        strategy = SpyPayment()
        checkout = Checkout(strategy)

        result = checkout.process_payment(
            Decimal("75.00")
        )

        self.assertEqual(result, "Simulated spy payment")
        self.assertEqual(
            strategy.last_amount,
            Decimal("75.00")
        )
from django.test import TestCase

# Create your tests here.

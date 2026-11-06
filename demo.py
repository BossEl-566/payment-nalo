
from decimal import Decimal

from payments.checkout import Checkout
from payments.strategies import (
    MobileMoneyPayment,
    CardPayment,
    BankTransferPayment,
)


def main():
    print("PAYMENT NALO - STRATEGY DESIGN PATTERN")


    # Step 1: Create checkout with Mobile Money
    checkout = Checkout(MobileMoneyPayment())

    print("\n[1] Payment using Mobile Money")
    result = checkout.process_payment(Decimal("100.00"))
    print(result)

    # Step 2: Switch to Card
    print("\n[2] Switching to Card Payment")
    checkout.set_payment_strategy(CardPayment())

    result = checkout.process_payment(Decimal("250.00"))
    print(result)

    # Step 3: Switch to Bank Transfer
    print("\n[3] Switching to Bank Transfer")
    checkout.set_payment_strategy(BankTransferPayment())

    result = checkout.process_payment(Decimal("500.00"))
    print(result)

    # Step 4: Demonstrate invalid amount handling
    print("\n[4] Testing invalid payment amount")

    try:
        checkout.process_payment(Decimal("-50.00"))
    except ValueError as error:
        print(f"Payment failed: {error}")


if __name__ == "__main__":
    main()

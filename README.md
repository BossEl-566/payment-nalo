
# Payment Nalo

A Django-based educational project demonstrating
the Strategy Design Pattern using simulated payments.

## Overview

Payment Nalo demonstrates how different payment
methods can be implemented using a common interface.

The project supports three simulated methods:

- Mobile Money
- Card Payment
- Bank Transfer

No real transactions are processed.

## Technologies

- Python 3.12
- Django
- Python ABC (Abstract Base Classes)
- Python Decimal
- Django SimpleTestCase

## Design Pattern

This project implements the Strategy Design Pattern.

### Components

**PaymentStrategy**

An abstract class defining the common pay() method.

**Concrete Strategies**

- MobileMoneyPayment
- CardPayment
- BankTransferPayment

Each strategy implements its own pay() behaviour.

**Checkout**

Maintains a reference to a PaymentStrategy instance.

Checkout delegates payment processing to the
selected strategy and supports switching strategies
at runtime.

## Project Structure

    payment-nalo/
    ├── config/
    │   ├── settings.py
    │   └── urls.py
    ├── payments/
    │   ├── strategies/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── mobile_money.py
    │   │   ├── card.py
    │   │   └── bank_transfer.py
    │   ├── checkout.py
    │   └── tests.py
    ├── demo.py
    ├── manage.py
    ├── requirements.txt
    └── README.md

## Installation

Clone the repository and enter the project directory.

Create a virtual environment:

    python -m venv .venv

Activate it on Windows CMD:

    .venv\Scripts\activate.bat

Install dependencies:

    python -m pip install -r requirements.txt

## Run the Demonstration

    python demo.py

The demonstration simulates payments and switches
between the three payment strategies.

## Run Tests

    python manage.py test payments

For detailed test output:

    python manage.py test payments --verbosity 2

## Benefits of the Strategy Pattern

1. Supports interchangeable payment methods.
2. Separates checkout logic from payment behaviour.
3. Reduces conditional statements in checkout.
4. Makes new payment strategies easy to add.
5. Improves maintainability and testability.

## Limitations

This is an educational simulation.

- No real payment gateway integration.
- No actual bank or Mobile Money transactions.
- No payment persistence.
- No production payment security infrastructure.
- No payment processing API or web checkout UI.

## Future Improvements

- Add a Django REST API.
- Create a basic checkout frontend.
- Introduce a simulated transaction history.
- Add structured payment result objects.
- Add more payment strategies.
